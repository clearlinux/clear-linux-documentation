.. _swupd-guide:

swupd
#####

:command:`swupd` links a |CL-ATTR| installation with upstream updates and
software.

.. contents::
   :local:
   :depth: 1

Description
***********

:command:`swupd` has two main functions:

#. Manage software and replace APT or YUM, by installing bundles
   rather than packages.
#. Check for system updates and install them.

:command:`swupd` manages overlapping dependencies behind the scenes, ensuring
that all software is compatible across the system. It can be used to verify
the OS, clean cached files, and fix issues.

:ref:`Bundles <bundles>` contain everything needed to deliver a software
capability. They are the smallest granularity component that is
managed by |CL|. A bundle comes with all of its dependencies rather than
downloading a cascade of package dependencies when installing a piece of
software.

Versioning
==========

Using package managers to monitor software version compatibility or
compare multiple systems on many Linux distributions can be cumbersome.

With |CL| :command:`swupd`, versioning happens at the individual file level.
This means |CL| generates an entirely new OS version with any set of software
changes to the system, including software downgrades or removals. This
rolling release versioning model is similar to :command:`git` internal version
tracking, where any of the individual file commits are tracked and move the
pointer forward when changed.

A number that represents the **current** release of the OS describes the
versions of all the software on the OS. Each build is composed of a specific
set of bundles made from a particular version of packages. On a daily basis,
this matters to system administrators who need to determine which of their
systems do not have the latest security fixes, or which combinations of
software have been tested. Every release of the same number is guaranteed to
contain the same versions of software, so there's no ambiguity between two
systems running the same version of |CL|.

Updating
========

|CL| enforces regular updating of the OS by default and automatically
checks for updates against a version server. The content server provides the
file and metadata content for all versions and can be the same as the
version server. The content url server provides metadata in the form of
*manifests*, which list and describe file contents, symlinks,
and directories. Additionally, the actual content is provided to clients
in the form of archive files.

Software updates with |CL| are also efficient. Unlike package-based
distributions, :command:`swupd` only updates files that have changed, rather
than entire packages. For example, it is quite common for an OS security
patch to be as small as 15 KB. Using binary deltas, |CL| is able to
apply only what is needed.

For details on how to generate update content for |CL|, see the
:ref:`mixer <mixer>` tool.

How it works
************

Prerequisites
=============

* The device is on a well-connected network.
* The device is able to connect to an update server. The default server is:
  http://update.clearlinux.org

Updates
=======

|CL| updates are automatic by default, but can be set to occur only on
demand. :command:`swupd` makes sure that regular updates are simple and
secure. It can also check the validity of currently installed files and
software, and can correct any problems.

Manifests
---------

The |CL| software update content consists of data and metadata. The data is
the files that end up in the OS. The metadata contains relevant information to
properly provision the data to the OS file system, as well as update the
system and add or remove additional content to the OS.

The manifests are mostly long lists of hashes that describe content.
Each bundle gets its own manifest file. There is a master manifest
file that describes all manifests to tie it all together.

Fullfiles, packs, and delta packs
---------------------------------

To speed up updates and optimize content delivery, update data provisioned to
a system is obtained by one of the following methods:

* *Fullfiles* are always generated for every file in every release. This
  allows any |CL| to obtain the exact copy of the content
  for each version directly. This is used if the OS verification
  needs to replace a single file, for instance.

* *Packs* are available for some releases. They combine many files to speed
  up the creation of installation media and large updates.

* *Delta packs* are an optimized version of packs that only contain updates
  (binary diffs). They cannot be used without having the original file content.

Bundle search
=============

:command:`swupd` searches download manifest data for
bundles that match the term. Enter only one term, or hyphenated term, per
search. Use the command :command:`man swupd` to learn more.

Only the base bundle is returned. Bundles can contain other bundles via
includes. For more details, see `Bundle Definition Files`_ and its
subdirectory bundles.

Bundles that are already installed are marked **(installed)** in search
results.

Optionally, you can review our `bundles`_ on GitHub\*.

Examples
********

Example 1: Disable and enable automatic updates
===============================================

|CL| updates are automatic by default, but can be set to occur only
on demand.

#. Verify your current auto-update setting.

   .. code-block:: bash

      sudo swupd autoupdate

   Output:

   .. code-block:: console

      Enabled

#. Disable automatic updates.

   .. code-block:: bash

      sudo swupd autoupdate --disable

   Output:

   .. code-block:: console

      Warning: disabling automatic updates may take you out of compliance with your IT policy

      Running systemctl to disable updates
      Created symlink /etc/systemd/system/swupd-update.service → /dev/null.
      Created symlink /etc/systemd/system/swupd-update.timer → /dev/null.

#. Check manually for updates.

   .. code-block:: bash

      sudo swupd check-update

#. Install an update after identifying one that you need.

   .. code-block:: bash

      sudo swupd update --version <version number>

#. Re-enable automatic installs.

   .. code-block:: bash

      sudo swupd autoupdate --enable

.. _swupd-guide-example-install-bundle:

Example 2: Find and install Kata Containers\*
=============================================

Kata Containers is a popular container implementation. Unlike other
container implementations, each Kata Container has its own
kernel instance and runs on its own :abbr:`VM (Virtual Machine)` for
improved security.

|CL| makes it very easy to install, since you only need to add
one bundle to use `Kata Containers`_: `containers-virt`_, despite a
number of dependencies.  Also, check out our tutorial: :ref:`kata`.

#. Find the correct bundle.

   To return all possible matches for the search string, enter
   :command:`swupd search`, followed by 'kata':

   .. code-block:: bash

      sudo swupd search kata

   The output should be similar to:

   .. code-block:: console

      Bundle with the best search result:

      containers-virt - Run container applications from Dockerhub in
      lightweight virtual machines

      This bundle can be installed with:

           swupd bundle-add  containers-virt

      Alternative bundle options are

           cloud-native-basic - Contains ClearLinux native software for Cloud

   .. note::

      If your search does not produce results with a specific term, shorten
      the search term. For example, use *kube* instead of *kubernetes*.

#. Add the bundle.

   .. code-block:: bash

      sudo swupd bundle-add containers-virt

   .. note::

      To add multiple bundles, add a space followed by the bundle name.

   The output of a successful installation should be similar to:

   .. code-block:: console

      Downloading packs...

      Extracting containers-virt pack for version 24430
          ...50%
      Extracting kernel-container pack for version 24430
          ...100%
      Starting download of remaining update content. This may take a while...
          ...100%
      Finishing download of update content...
      Installing bundle(s) files...
          ...100%
      Calling post-update helper scripts.
      Successfully installed 1 bundle

Example 3: Verify and correct system file mismatch
==================================================

:command:`swupd` can determine whether system directories and files have
been added to, overwritten, removed, or modified (e.g., permissions).

.. code-block:: bash

   sudo swupd diagnose

All directories that are watched by :command:`swupd` are verified according
to the manifest data. Hash mismatches are flagged as follows:

.. code-block:: console

   Verifying version 23300
   Verifying files
      ...0%
   Hash mismatch for file: /usr/bin/chardetect
   ...
   ...
   Hash mismatch for file: /usr/lib/python3.6/site-packages/urllib3/util/wait.py
      ...100%
   Inspected 237180 files
      423 files did not match
   Verify successful

In this case, Python\* packages that were installed on top of the default
install were flagged as mismatched. :command:`swupd` can be directed to
ignore or fix issues based on command line options.

:command:`swupd` can correct any issues it detects. Additional directives
can be added including a white list of directories to be ignored.

The following command repairs issues, removes unknown items, and
ignores files or directories matching :file:`/usr/lib/python`:

.. code-block:: bash

   sudo swupd repair --picky --picky-whitelist=/usr/lib/python

.. _swupd-quick-ref:

Quick reference
***************

swupd info
   Returns the currently installed version and update servers.

swupd update <version number>
   Updates to a specific version or updates to latest version if no
   arguments are used.

swupd bundle-list [--all]
   Lists installed bundles.

swupd bundle <search term>
   Finds a bundle that contains your search term.

swupd bundle-add <bundle name>
   Adds a bundle.

swupd bundle-remove <bundle name>
   Removes a bundle.

swupd --help
   Lists additional :command:`swupd` commands.

man swupd
   Opens the :command:`swupd` man page.

Refer to `swupd source documentation`_ on GitHub for more details.

Related topics
**************

* :ref:`autospec`
* :ref:`mixer`
* :ref:`bundles`

.. _swupd source documentation: https://github.com/clearlinux/swupd-client/blob/master/docs/swupd.1.rst

.. _Kata Containers: https://clearlinux.org/downloads/containers

.. _containers-virt: https://github.com/clearlinux/clr-bundles/blob/master/bundles/containers-virt

.. _Bundle Definition Files: https://github.com/clearlinux/clr-bundles

.. _bundles: https://github.com/clearlinux/clr-bundles/tree/master/bundles