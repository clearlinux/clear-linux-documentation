.. _bootable-usb-beta-all:

Create a bootable USB on your OS
################################

Follow these instructions to create a bootable |CL-ATTR| USB drive based on 
your OS.

* :ref:`bootable-usb-linux-all`
* :ref:`bootable-usb-mac-all`
* :ref:`bootable-usb-windows-all`

Return to :ref:`install-from-live-image`

Requirements: 
*************

* Use a **16GB** or larger USB drive. 

.. _bootable-usb-linux-all:

Create a bootable USB drive on Linux
************************************

.. include:: ../../guides/maintenance/download-verify-decompress-linux.rst
   :Start-after: verify-linux:


Burn the |CL| image onto a USB drive
====================================

.. caution::

   |CAUTION-BACKUP-USB|

#. Open a terminal emulator and get root privilege.

   .. code-block:: bash

      sudo -s

#. Go to the directory with the decompressed image.
#. Plug in the USB drive.
#. Identify the USB drive using the :command:`lsblk` command. This shows all
   drives attached to the system, including the primary hard disk. In the
   example output below, there are 4 drives 
   (`/dev/sda`, `/dev/sdb`, `/dev/sdc`, and `/dev/sdd`) attached, where 
   `/dev/sda` is primary drive in this case. The remaining are 3 USB drives.
   The output also shows the mounted partitions (under the `MOUNTPOINT`
   column) for each drive.

   .. code-block:: bash

      lsblk

   Example output:

   .. code-block:: console

      NAME   MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
      sdd      8:48   1    15G  0 disk
      ├─sdd2   8:50   1     5G  0 part /run/media/user1/960c184f-3bb7-42b7-bcaf-0c1282
      ├─sdd3   8:51   1     8G  0 part /run/media/user1/704f3382-b26d-4f34-af1b-cb9aab
      └─sdd1   8:49   1     2G  0 part
      sdb      8:16   1  14.8G  0 disk
      └─sdb1   8:17   1  14.8G  0 part /run/media/user1/PATRIOT_USB
      sdc      8:32   1   7.3G  0 disk
      └─sdc1   8:33   1   7.3G  0 part /run/media/user1/LINUX MINT
      sda      8:0    0 335.4G  0 disk
      ├─sda4   8:4    0    28G  0 part
      ├─sda2   8:2    0   3.7G  0 part [SWAP]
      ├─sda7   8:7    0     6G  0 part /home
      ├─sda5   8:5    0     1G  0 part /boot
      ├─sda3   8:3    0   954M  0 part /boot/efi
      ├─sda1   8:1    0    28G  0 part
      ├─sda8   8:8    0    30G  0 part /
      └─sda6   8:6    0   7.9G  0 part [SWAP]

#. Before an image can be burned onto a USB drive, it should be un-mounted.
   Some Linux* distros may automatically mount a USB drive when it is plugged
   in. To unmount, use the :command:`umount` command followed by the device
   identifier/partition. For example: From the above :command:`lsblk` output,
   `/dev/sdd` has 2 mounted partitions.  To unmount them, enter:

   .. code-block:: bash

      umount /dev/sdd2
      umount /dev/sdd3

#. Burn the image onto the USB drive. The command-line example below burns an
   uncompressed image onto `/dev/sdd`:

   .. code-block:: bash

      dd if=./clear-[version number]-[image type] of=/dev/sdd bs=4M status=progress

.. _bootable-usb-mac-all:

Create a bootable USB drive on macOS*
*************************************

.. include:: ../../guides/maintenance/download-verify-decompress-mac.rst
   :start-after: verify-mac:


Burn the |CL| image onto a USB drive
====================================

.. caution::

   |CAUTION-BACKUP-USB|

#. Launch the Terminal app.
#. Go to the directory with the decompressed image.
#. Plug in a USB drive and get its identifier by entering the command
   :command:`diskutil list`.  See Figure 1.

   .. code-block:: console

      diskutil list

   .. figure:: figures/bootable-usb-mac-1.png
      :scale: 100 %
      :alt: Get USB drive identifier

      Figure 1: macOS* - Get USB drive identifier

#. Unmount the USB drive identified in the previous step.  The command-line
   example below umounts `/dev/disk2`:

   .. code-block:: console

      diskutil umountDisk /dev/disk2

#. Burn the image onto the drive using the :command:`dd` command.  The 
   command-line example below burns an uncompressed image onto `/dev/disk2`:

   .. code-block:: console

      sudo dd if=./clear-[version number]-[image type] of=/dev/rdisk2 bs=4m


   Adding an ‘r’ in front of the disk identifier should help speed up the 
   imaging process.
   
   You can press :kbd:`<CTL>-T` to check imaging progress.

#. Eject the USB drive.

   .. code-block:: console

      diskutil eject /dev/disk2

.. _bootable-usb-windows-all:

Create a bootable USB drive on Windows\*
****************************************

.. include:: ../../guides/maintenance/download-verify-decompress-windows.rst
   :Start-after: verify-windows:

Burn the |CL| image onto a USB drive
====================================

.. caution::

   |CAUTION-BACKUP-USB|

#. Download the `Rufus`_ utility to burn the image onto a USB drive.

#. Plug in the USB drive and open Rufus.

#. Click the :guilabel:`SELECT` button. See Figure 1.

   .. figure:: figures/bootable-usb-windows-1.png
      :scale: 80 %
      :alt: Rufus utility - Click the SELECT button

      Figure 1: Rufus utility - Click the SELECT button

#. Find and select the previously extracted |CL| image file. 
   Then, click the  :guilabel:`Open` button. See Figure 2.

   .. figure:: figures/bootable-usb-windows-2.png
      :scale:  80 %
      :alt: Rufus utility - Show and select |CL| image file

      Figure 2: Rufus utility - Show and select |CL| image file
    
#. Click the :guilabel:`START` button. See Figure 3.

   .. figure:: figures/bootable-usb-windows-3.png
      :scale: 80 %
      :alt: Rufus utility - Click the START button
         
      Figure 3: Rufus utility - Click START button

Return to install from live image
*********************************

Return to :ref:`install-from-live-image`

.. _Rufus: https://rufus.ie/
