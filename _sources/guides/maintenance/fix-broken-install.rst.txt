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
:ref:`swupd<swupd-guide>` owns in :file:`/usr` and :file:`/var`. Files outside 
of this path, such as :file:`/home/`, :file:`/etc`, etc., cannot be 
repaired by this process.

Prerequisites
*************

* Download and burn the live desktop image on a USB. 
  See :ref:`bare-metal-install-desktop` for instructions.

Boot a live desktop image to fix target system
**********************************************

#. Boot the |CL| live desktop image.

#. Select |CL| in the boot menu.
   
Mount root partition, verify, and fix
*************************************

#. Ensure the system is connected to the Internet in order to access the 
   the |CL| update server.

#. Open a terminal window.

#. Find the |CL| root partition by using the :command:`lsblk` command with
   these options: ``-o NAME,LABEL,PARTTYPE,PARTLABEL``.

   .. code-block:: bash

      lsblk -o NAME,LABEL,PARTTYPE,PARTLABEL

   Example output:

   .. code-block:: console
      :emphasize-lines: 9 

      NAME          SIZE LABEL       PARTTYPE                             PARTLABEL
      /dev/loop0  643.6M                                                  
      /dev/sda     14.3G CLR_ISO                                          
      ├─/dev/sda1   835M CLR_ISO     0x0                                  
      └─/dev/sda2   100M "CLEAR_EFI" 0xef                                 
      /dev/sdb     74.5G                                                  
      ├─/dev/sdb1   142M boot        c12a7328-f81f-11d2-ba4b-00a0c93ec93b EFI
      ├─/dev/sdb2   244M swap        0657fd6d-a4ab-43c4-84e5-0933c84b4f4f linux-swap
      └─/dev/sdb3  74.2G root        4f68bce3-e8cd-4db1-96e7-fbcaf984b709 /

   In the example above, ``/dev/sdb3/`` is the root partition.  

#. Next, mount the root partition.

   .. code-block:: bash

      sudo mount /dev/sdb3 /mnt

#. Verify that you mounted the correct root partition by verifying the content
   of ``/mnt/usr/lib/os-release`` looks similar to the example below.  

   .. code-block:: bash

      cat /mnt/usr/lib/os-release

   Example output:

   .. code-block:: console

      NAME="Clear Linux OS"
      VERSION=1
      ID=clear-linux-os
      ID_LIKE=clear-linux-os
      VERSION_ID=32150
      PRETTY_NAME="Clear Linux OS"
      ANSI_COLOR="1;35"
      HOME_URL="https://clearlinux.org"
      SUPPORT_URL="https://clearlinux.org"
      BUG_REPORT_URL="mailto:dev@lists.clearlinux.org"
      PRIVACY_POLICY_URL="http://www.intel.com/privacy"

#. Next, run :command:`swupd repair` to fix any issues on the target system.

   .. code-block:: bash

      sudo swupd repair --picky --path=/mnt --statedir=/mnt/var/lib/swupd

   :ref:`Learn more about how swupd works <swupd-guide>`.

#. After the process is complete, unmount the root partition.

   .. code-block:: bash

      sudo umount /mnt

#. Reboot the system, remove the live desktop USB drive,
   and boot into the repaired system.

   .. code-block:: bash

      sudo reboot
