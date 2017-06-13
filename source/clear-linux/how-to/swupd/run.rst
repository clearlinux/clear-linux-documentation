.. _swupd-run:

How to update Clear Linux
#########################

This section describes how to update |CLOSIA|.

Prerequisites
=============

* The system is up and running the Clear Linux 15400 build or later.

* Device is on a well-connected network.

* Device is able to connect to the release infrastructure. For example:
  http://update.clearlinux.org/update/300/

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

If you wish to force a manual update:

   .. code-block:: console

      $ sudo swupd update

.. note::

   If the updater console output indicates a kernel update occurred, then at
   your convenience reboot to begin using the new OS version.

Additional information
======================

To see the man page listing additional swupd options, enter:

   .. code-block:: console

      $ man swupd
