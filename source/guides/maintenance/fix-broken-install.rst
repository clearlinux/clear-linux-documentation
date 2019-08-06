.. _fix-broken-install:

Fix a broken installation
#########################

This guide explains how to fix a broken installation of |CL-ATTR| using a live
desktop image on a USB.

.. contents::
   :local:
   :depth: 1

Overview
********

This guide assumes you have installed |CL| on a target system, but the OS
does not boot or function properly.

The process described in this guide can only verify and fix files that
:ref:`swupd<swupd-guide>` owns in :file:`/usr`. Files outside of this path, such
as :file:`/home/`, :file:`/etc`, :file:`/var`, etc., cannot be repaired by this
process.

Prerequisites
*************

* Download and install the live desktop image on a USB. See
  :ref:`bare-metal-install-desktop` for install instructions.

Boot a live desktop image to fix target system
**********************************************

#. Boot the |CL| live desktop image.

.. include:: ../../get-started/bare-metal-install-desktop.rst
   :start-after: install-on-target-start:
   :end-before: install-on-target-end:

Mount root partition, verify, and fix
*************************************

#. Open a Terminal window.

#. Ensure the system is connected to the network.

#. Mount the system’s root partition.

   #. To find the root partition, run:

      .. code-block:: bash

         lsblk

      We'll use :file:`/dev/sda3/` as the root partition example.

   #. Next, mount the partition to the :file:`/mnt` folder.

      .. code-block:: bash

         sudo mount /dev/sda3 /mnt

#. Verify that you mounted the correct root partition by checking for some
   files commonly found on |CL| systems.

   .. code-block:: bash

      cat /mnt/usr/lib/os-release
      ls /mnt/usr/share/clear/bundles

#. Next, run swupd to fix any issues on the target system.

   .. code-block:: bash

      sudo swupd repair --picky --path=/mnt

   :ref:`Learn more about how swupd works <swupd-guide>`.

#. After the process is complete, unmount the root partition:

   .. code-block:: bash

      sudo umount /mnt

#. Reboot the system, remove the live desktop USB drive,
   and boot into the repaired system.

   .. code-block:: bash

      sudo reboot

**Congratulations!** You successfully restored |CL|.
