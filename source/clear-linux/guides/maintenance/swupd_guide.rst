.. _swupd_guide:

swupd guide
###########

*swupd* manages the software update capability of |CLOSIA|. It can check for
valid system updates and, if found, download and install them. It can also
perform verification of the system software. 

|CL| uses :ref:`bundles-about<bundles>` as the base abstraction for
installing functionality on top of the core operating system. Use the `swupd`
tool to install and remove bundles.

.. contents:: 
   :local:
   :depth: 2

For a full listing of commands and options please see the man page in |CL|

.. code-block:: bash

   man swupd

OS Update and Verification
**************************

|CL| is designed to promote a regular update cadence. `swupd` helps to
make sure that process is simple and secure.

Automatic Updates
=================

|CL| updates can be toggled to happen automatically or on demand. Enable
automatic updates like this:

.. code-block:: bash

   sudo swupd autoupdate --enable

To disable use the `--disable` flag instead.

System Software Verification
============================

`swupd` can determine whether the system software has been overwritten, removed, or modified in any way.

.. code-block:: bash

   sudo swupd verify

Bundles
*******

Listing installed bundles
=========================

You can list all of the bundles currently installed on the system

.. code-block:: bash

   sudo swupd bundle-list --all 

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

