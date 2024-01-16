.. _query-upstream:

Query package info from upstream repository
###########################################

This guide describes how to query package information from the |CL| upstream
repositories. This guide is intended for developers and advanced users.

.. contents::
   :local:
   :depth: 1
   :backlinks: top

Overview
********

In |CL-ATTR|, the :ref:`swupd<swupd-guide>` tool manages software
dependencies and installs bundles instead of packages. Although a bundle is
a collection of one or more packages, |CL| does not work with packages on
the client side. However, on the upstream/factory side, |CL| does work with
packages using a process called *mixing*.

Currently, :command:`swupd` does not report which packages are installed,
provide package version information, or return other package details. This
guide describes a method for retrieving package information from the |CL|
upstream repositories using :abbr:`DNF(Dandified Yum)` commands.

Prerequisites
*************

This guide assumes you have installed |CL| on your host system.
For detailed instructions on installing |CL| on a bare metal system, visit
the :ref:`bare metal installation guide <bare-metal-install-desktop>`.

Before you install any new packages, update |CL| with the following command:

.. code-block:: bash

   sudo swupd update

Configure DNF
*************

#. Install the DNF bundle with the command:

   .. code-block:: bash

	  sudo swupd bundle-add dnf

#. Create a :file:`dnf.conf` file with the commands:

   .. code-block:: bash

	  sudo mkdir -p /etc/dnf
	  sudo curl -L https://github.com/clearlinux/common/raw/master/conf/dnf.conf --output /etc/dnf/dnf.conf


#. Edit the :file:`/etc/dnf/dnf.conf` file and set the **baseurl** variable
   for binary and source RPMs as shown in lines 3 and 9 in the following
   example.

   .. code-block:: bash
	  :linenos:
	  :emphasize-lines: 3,9

	  [clear]
	  name=Clear
	  baseurl=https://cdn.download.clearlinux.org/releases/$releasever/clear/x86_64/os/
	  enabled=1
	  gpgcheck=0
	  [clear-source]
	  name=Clear sources
	  failovermethod=priority
	  baseurl=https://cdn.download.clearlinux.org/releases/$releasever/clear/source/SRPMS/
	  enabled=1
	  gpgcheck=0

#. Initialize the RPM database with the command:

   .. code-block:: bash

	  sudo rpm --initdb


DNF command usage examples
**************************

.. contents:: :local:
   :depth: 1
   :backlinks: top

List all binary and source RPMs in the current release
======================================================

Command:

.. code-block:: bash

	dnf repoquery --releasever=current

Sample output:

.. code-block:: console

   Clear                                    5.1	MB/s |  13 MB     00:02
   Clear sources                            1.8	MB/s | 1.7 MB     00:00
   AVB-AudioModules-0:4.1.0-1.src
   AVB-AudioModules-0:4.1.0-1.x86_64
   AVB-AudioModules-data-0:4.1.0-1.x86_64
   AVB-AudioModules-dev-0:4.1.0-1.x86_64
   AVB-AudioModules-lib-0:4.1.0-1.x86_64
   AVB-AudioModules-license-0:4.1.0-1.x86_64
   AVBStreamHandler-0:1.1.0-21.src
   AVBStreamHandler-0:1.1.0-21.x86_64
   AVBStreamHandler-abi-0:1.1.0-21.x86_64
   AVBStreamHandler-bin-0:1.1.0-21.x86_64
   AVBStreamHandler-data-0:1.1.0-21.x86_64
   AVBStreamHandler-dev-0:1.1.0-21.x86_64
   AVBStreamHandler-lib-0:1.1.0-21.x86_64
   AVBStreamHandler-license-0:1.1.0-21.x86_64
   ...
   <trimmed>

Show version information for a package in current release
=========================================================

This example queries version information for the zstd package.

Command:

.. code-block:: bash

   dnf repoquery --releasever=current zstd

Sample output:

.. code-block:: console

	Last metadata expiration check: 0:02:30 ago on Tue 16 Jul 2019 03:03:34 PM PDT.
	zstd-0:1.4.0-46.src
	zstd-0:1.4.0-46.x86_64


Show version information for a package in a specific release
============================================================

This example queries version information for the zstd package in release
21000.

Command:

.. code-block:: bash

   dnf repoquery --releasever=21000 zstd

Sample output:

.. code-block:: console

   Clear
   2.7 MB/s | 3.9 MB     00:01
   Clear sources
   628 kB/s | 559 kB     00:00
   zstd-0:1.3.3-20.src
   zstd-0:1.3.3-20.x86_64

Show only version and release information for a package in a specific release
=============================================================================

This example queries version and release information for the zstd package in
release 15000.

Command:

.. code-block:: bash

   dnf repoquery --releasever=15000 --qf="%{VERSION}\n%{RELEASE}" zstd

Sample output:

.. code-block:: console

   Clear
   3.4 MB/s | 3.9 MB     00:01
   Clear sources
   345 kB/s | 528 kB     00:01
   1.1.4
   5

Show the binary package for a specified binary file
===================================================

This example returns the binary package that contains the
:file:`/usr/bin/zip` binary file.

Command:

.. code-block:: bash

   dnf repoquery --releasever=current --whatprovides /usr/bin/zip

Sample output:

.. code-block:: console

   Last metadata expiration check: 0:04:47 ago on Tue 16 Jul 2019 03:03:34 PM PDT.
   zip-bin-0:3.0-23.x86_64

Show the source package for a specified binary file
===================================================

This example returns the source package that contains the
:file:`/usr/bin/zip` binary file.

Command:

.. code-block:: bash

   dnf repoquery --releasever=current --whatprovides /usr/bin/zip --srpm

Sample output:

.. code-block:: console

   Last metadata expiration check: 0:05:50 ago on Tue 16 Jul 2019 03:03:34 PM PDT.
   zip-0:3.0-23.src
