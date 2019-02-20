.. _swupd:

swupd
#####

`swupd` is the |CL-ATTR| client-side tool that manages updates including
installing bundles. It can check for valid system updates and, if found,
download and install them. It can also check the validity of currenty
installed files and software and correct any problems. `swupd` links a |CL|
installation with upstream updates and software.

.. contents::
   :local:
   :depth: 2

Description
***********

The central concept that any change to a |CL| installation is considered
an update applies here. This inclues moving from one version of |CL| to
another or simply installing a :ref:`bundle <bundle-about>`.

To remain up to date, `swupd` compares version numbers with a version url
server and downloads manfiests and content from a content url server if
needed.

.. questionable content

	A notable difference between package-based distributions and |CL|
	is how updates are managed. On a package-based OS, system administrators
	update each individual package or piece of software to a newer (or older!)
	version. With |CL|, an update translates to an entirely new OS version,
	containing one or many updates.  It is not possible to update a piece of the
	system while remaining on the same version of |CL|.

	Although it may seem like a huge restriction or limitation, this
	method has many non-obvious benefits. Imagine a cloud environment composed
	of numerous machines.  Here, a homogeneous set of software makes sense --
	from the system administrator's level down to the user level. Homogeneous
	systems allow users to focus on their contributions and code, rather than
	configuring environments or worrying about synchronizing versions and
	updates.  At the system admin level, it ensures security is tighter and
	makes it far easier to monitor and update patches.

	|CL| promotes regular updating of the OS and will automatically check
	for updates and apply them by default.

	To learn how to run an update of your system, visit our :ref:`swupd-guide` page.

The content url server can be the same as the version url server and
provides the file and metadata content for all versions. The content url 
server provides metadata in the form of manifests. These Manifest files list
and describe file contents, symlinks, and directories. Additionally, the
actual content is provided to clients in the form of archive files.

To get a more detailed understanding of how update content is generated see
the :ref:`mixer` tool. 

How it works
************

|CL| is designed to promote a regular update cadence. `swupd` helps to
make sure that process is simple and secure. |CL| updates are automatic by
default but can be set to occur only on demand. 

Prerequisites
=============

* The device is on a well-connected network.
* The device is able to connect to a release server. The default server is:
  http://update.clearlinux.org

Workflow
========

Use this to explain the basics behind the process. Whats happening? There are two basic workflows:

#. Update and Verify with upstream
#. Manage bundles

Search explained: 
-----------------

`swupd search` downloads |CL| manifest data and searches for
matching paths. Enter only one term, or hyphenated term, per
search. Use the command :command:`man swupd` to learn more.

`-b` flag, or `--binary`, means: Restrict search to program binary paths. Omit this flag if you want a larger scope of search results.

Only the base bundle is returned. In |CL|, *bundles* can contain
other *bundles* via `includes`. For more details, see `Bundle Definition Files`_ and its subdirectory *bundles*.

Bundles that are already installed, will be marked *[installed]* in search
results.

Optionally, you can review our `bundles`_ or individual `packages`_

Examples
********

#. Turn off audo update and change the servers that swupd looks at.

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