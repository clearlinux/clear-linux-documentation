.. _swupd-run:

How to update Clear Linux
#########################

This section describes how to update |CLOSIA|.

Prerequisites
=============

* The system is up and running the Clear Linux 15400 release or later.

* The device is on a well-connected network.

* The device is able to connect to the release infrastructure
  http://update.clearlinux.org

To verify the current release running on the system, enter:

.. code-block:: console

   $ sudo swupd update -s

How to update the system
========================

Starting with version 15400, Clear Linux supports auto-update. By default, it
is turned on.

To verify the current auto-update setting:

   .. code-block:: console

      $ swupd autoupdate

To enable auto-update:

   .. code-block:: console

      $ sudo swupd autoupdate --enable

To disable auto-update:

   .. code-block:: console

      $ sudo swupd autoupdate --disable

To force a manual update:

   .. code-block:: console

      $ sudo swupd update

.. note::

   When the swupd console output indicates a kernel update, reboot
   immediately for the enhancements to take effect.


Additional information
======================

To see the man page listing additional swupd options, enter:

   .. code-block:: console

      $ man swupd
