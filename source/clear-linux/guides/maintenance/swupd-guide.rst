.. _swupd-guide:

Use swupd
#########

*swupd* manages the software update capability of |CLOSIA|. It can check for
valid system updates and, if found, download and install them. It can also
perform verification of the system software. 

|CL| uses :ref:`bundles-about<bundles>` as the base abstraction for
installing functionality on top of the core operating system. Use the `swupd`
tool to install and remove bundles.

This guide assumes:

* The device is on a well-connected network.

* The device is able to connect to the release infrastructure
  http://update.clearlinux.org

.. contents:: 
   :local:
   :depth: 2

.. _man_swupd:

For a full listing of commands and options please see the man page in |CL|

.. code-block:: bash

   man swupd

OS update and verification
**************************

|CL| is designed to promote a regular update cadence. `swupd` helps to
make sure that process is simple and secure.

View OS info
============

Current OS version and update server info:

.. code-block:: bash

   swupd info

.. code-block:: console
   Installed version: 23330
   Version URL:       https://download.clearlinux.org/update/
   Content URL:       https://cdn.download.clearlinux.org/update/

Enable or disable automatic updates
===================================

|CL| updates are automatic by default but can be set to occur only 
on demand. To verify your current auto-update setting:

.. code-block:: bash

   sudo swupd autoupdate

Disable automatic updates:

.. code-block:: bash

   sudo swupd autoupdate --disable

To re-enable automatic:

.. code-block:: bash

   sudo swupd autoupdate --enable

Check for updates
=================

.. code-block:: bash

   sudo swupd check-update

Perform a manual update
=======================

You can update to a specific version or accept the latest as the default with
no arguments. Initiate a manual update:

.. code-block:: bash

   sudo swupd update -m 23330

.. note::

   After a kernel update, reboot immediately for the enhancements to
   take effect.

System Software Verification
============================

`swupd` can determine whether system directories and files have been added
to, overwritten, removed, or modified (e.g., permissions).

.. code-block:: bash

   sudo swupd verify

All directories that are watched by `swupd` are verified according to 
the manifest data and hash mismatches are flagged as follows:

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

In this case, python packages that were installed on top of the default
install were flagged as mismatched. `swupd` can be directed to ignore
or fix issues based on :ref:`command line options <man_swupd>`. 

Fixing hash mismatches
======================

`swupd` can correct any issues it detects. Additional directives can be
added including a white list of directories that will be ignored, if
desired.

The following command will repair issues, remove unknown items, and
ignore files or directories matching `/usr/lib/python`:

.. code-block:: bash

   sudo swupd verify --fix --picky --picky-whitelist=/usr/lib/python 

Bundles
*******

Listing installed bundles
=========================

You can list all of the bundles currently installed on the system

.. code-block:: bash

   sudo swupd bundle-list --all 

Finding a bundle containing a binary
====================================

Run the following to display a list of bundles that contain a particular
binary. Note that it may be present in multiple bundles:

.. code-block:: bash

   swupd search -b <binary you want> 

Adding a bundle
===============

Start by selecting a bundle from the list of :ref:`available-bundles`. In
this example we're adding dev-utils-dev, which is useful for development.

.. code-block:: bash

   sudo swupd bundle-add dev-utils-dev

Removing a bundle
=================

Dependencies common to other bundles will not be removed

.. code-block:: bash

   sudo swupd bundle-remove dev-utils-dev

