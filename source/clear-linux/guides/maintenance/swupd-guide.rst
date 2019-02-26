.. _swupd-guide:

swupd
#####

`swupd` links a |CL-ATTR| installation with upstream updates and software.

.. contents::
   :local:
   :depth: 2

Description
***********

`swupd` has two main functions:

#. It manages software replacing APT or YUM, installing bundles
   rather than packages. 
#. It checks for system updates and installs them. 

:ref:`bundles` are the smallest granularity component that is
managed by |CL| and contain everything needed to deliver a software
capability. Rather than downloading a cascade of package dependencies when
installing a piece of software, a bundle comes with all of its dependencies.
`swupd` manages overlapping dependencies behind the scenes ensuring that all
software is compatible across the system.

A big difference between package-based distributions and |CL| is how updates
and software are managed. On a package-based OS, system administrators
have to track updates at a package level, which means tracking the version
of the OS, kernel, and each of the installed packages which can easily
become out of sync. |CL| guarantees that any installation with the same OS
version has the same kernel and supporting software. In other words, it
isn't possible for any OS component to get out of sync as long as `swupd`
is used for system updates. It also means that only one version number is
needed to know whether a |CL| installation has the latest security patches
installed. 

|CL| enforces regular updating of the OS by default and will automatically
check for updates against a version server. The content server provides the
file and metadata content for all versions and can be the same as the
version server. The content url server provides metadata in the form of
manifests. These Manifest files list and describe file contents, symlinks,
and directories. Additionally, the actual content is
provided to clients in the form of archive files.

Software updates with |CL| are also efficient. Unlike package-based
distributions, `swupd` only updates files that have changed rather than
entire packages. For example, it is quite common for an OS security patch to
be as small as 15 KB. Using binary deltas, the |CL| is able to apply only
what is needed.

To get a more detailed understanding of how generate update content for |CL|
see the :ref:`mixer` tool. 

How it works
************

Prerequisites
=============

* The device is on a well-connected network.
* The device is able to connect to an update server. The default server is:
  http://update.clearlinux.org

Updates explained
=================

|CL| updates are automatic by default but can be set to occur only on
demand. `swupd` makes sure that regular updates are simple and secure. It
can also check the validity of currenty installed files and software and
correct any problems.

How does it do all this? 

Bundle management explained 
===========================

Bundle Search
-------------

`swupd search` downloads |CL| manifest data and searches for
matching paths. Enter only one term, or hyphenated term, per
search. Use the command :command:`man swupd` to learn more.

`-b` `--binary`
   Restrict search to program binary paths. Omit this flag if you want a
   larger scope of search results.

Only the base bundle is returned. In |CL|, *bundles* can contain
other *bundles* via `includes`. For more details, see `Bundle Definition Files`_ and its subdirectory *bundles*.

Bundles that are already installed, will be marked *[installed]* in search
results.

Optionally, you can review our `bundles`_ or individual `packages`_

Examples
********

Example 1: Disable and Enable automatic updates
===============================================

|CL| updates are automatic by default but can be set to occur only
on demand.

#. First verify your current auto-update setting.

   .. code-block:: bash

      sudo swupd autoupdate

   .. code-block:: console

      Enabled

#. Disable automatic updates.

   .. code-block:: bash

      sudo swupd autoupdate --disable

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

      sudo swupd update -m <version number>

#. Re-enable automatic installs.

   .. code-block:: bash

      sudo swupd autoupdate --enable

.. _swupd-guide-example-install-bundle:

Example 2: Find and install Kata\* Containers
=============================================

Kata Containers is a popular container implementation. Unlike other
container implementations, each Kata Container has its own
kernel instance and runs on its own :abbr:`Virtual Machine (VM)` for
improved security. 

|CL| makes it very easy to install, since you only need to add
`one bundle`_ to use `Kata Containers`_: `containers-virt`, despite a
number of dependencies.  Also, check out our tutorial: :ref:`kata`.

#. Find the right bundle. 

   * To return all possible matches for the search string enter
     :command:`swupd search`, followed by 'kata':

     .. code-block:: bash

        sudo swupd search kata

   * If you're only interested in searching binaries, add the `-b`
     flag:

     .. code-block:: bash

        sudo swupd search -b kata

     The output should be similar to:

     .. code-block:: console

        Bundle containers-virt    (834 MB to install)
            /usr/bin/kata-virtfs-lite-proxy-helper
            /usr/bin/kata-runtime
            /usr/bin/kata-qemu-lite-system-x86_64
            /usr/bin/kata-qemu-lite-pr-helper
            /usr/bin/kata-qemu-lite-ga
            /usr/bin/kata-collect-data.sh

     .. note::

        If your search of binaries does not produce results with a specific
        term, shorten the search term. For example, use *kube* instead of
        *kubernetes*.

#. Add the bundle.

   .. code-block:: bash

      sudo swupd bundle-add containers-virt

   .. note::

      To add multiple bundles simply add a space followed by the bundle name.

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

Quick Reference
***************

swupd info
   To see the currently installed version and update servers.

swupd update <version number>
   To update to a specific version or with no arguments to update to latest.

swupd bundle-list [--all]
   To list installed bundles.

swupd bundle-add [-b] <search term>
   To find a bundle that contains your search term.

swupd bundle-add <bundle name>
   To add a bundle.

swupd bundle-remove <bundle name>
   To remove a bundle.

swupd --help
   For additional :command:`swupd` commands.

man swupd
   To reference the :command:`swupd` man page, or see the 
   `source documentation`_ available on github.

Related topics
**************

.. _source documentation: https://github.com/clearlinux/swupd-client/blob/master/docs/swupd.1.rst

.. _Kata Containers: https://clearlinux.org/containers

.. _one bundle: https://github.com/clearlinux/clr-bundles/blob/master/bundles/containers-virt

.. _Bundle Definition Files: https://github.com/clearlinux/clr-bundles

.. _bundles: https://github.com/clearlinux/clr-bundles/tree/master/bundles

.. _packages: https://github.com/clearlinux/clr-bundles/blob/master/packages