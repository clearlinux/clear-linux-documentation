.. _bootable-usb:

Create a bootable USB drive
###########################

Follow the instructions applicable to your system to create a bootable
|CL-ATTR| USB drive:

* :ref:`bootable-usb-linux`
* :ref:`bootable-usb-mac`
* :ref:`bootable-usb-windows`

Prerequisites
*************

* Download the |CL| Desktop or Server image from the `Downloads`_ page
* Recommended minimum **4GB** USB drive or larger

.. _bootable-usb-linux:

Create a bootable USB drive on Linux\*
**************************************

* Make sure you completed all `Prerequisites`_.

* :ref:`verify-linux` on Linux.

Burn the |CL| image onto a USB drive
====================================

.. caution::

   Burning an image formats the USB drive and destroys all pre-existing
   content.  Back up your data before proceeding.

#. Open a terminal window.

#. Change directory to where the image resides.

#. Plug in the USB drive.

#. Identify the USB drive using the :command:`lsblk` command with these options:
   ``-po NAME,SIZE,TYPE,FSTYPE,PARTLABEL,MOUNTPOINT,VENDOR,MODEL``. This shows all
   drives attached to the system, including the primary hard disk. In the
   example output below, there are 3 drives (`/dev/sda`, `/dev/sdb`, and `/dev/sdc`) 
   attached, where `/dev/sda` is the primary drive and the remaining are USB drives.

   .. code-block:: bash

      lsblk -po NAME,SIZE,TYPE,FSTYPE,PARTLABEL,MOUNTPOINT,VENDOR,MODEL

   Example output:

   .. code-block:: console

      NAME          SIZE VENDOR   MODEL                    TRAN   TYPE PARTLABEL                    MOUNTPOINT
      /dev/sda    119.2G ATA      SAMSUNG_MZ7PC128HAFU-000 sata   disk                              
      ├─/dev/sda1   450M                                          part Basic data partition         
      ├─/dev/sda2   100M                                          part EFI system partition         
      ├─/dev/sda3    16M                                          part Microsoft reserved partition 
      ├─/dev/sda4  97.2G                                          part Basic data partition         
      ├─/dev/sda5   142M                                          part EFI                          
      ├─/dev/sda6   245M                                          part linux-swap                   [SWAP]
      └─/dev/sda7  21.1G                                          part /                            /
      /dev/sdb      7.5G General  UDisk                    usb    disk                              
      └─/dev/sdb1   7.5G                                          part Microsoft Basic Data         /run/media/clear/CENA_X64FRE
      /dev/sdc       15G          Patriot_Memory           usb    disk                              
      └─/dev/sdc1    15G                                          part                              /run/media/clear/U

   .. note::

      Some Linux distros may automatically mount a USB drive when it is plugged in.

#. If the USB drive you want to use is mounted, it must be umounted before
   burning an image onto it.  Use the :command:`umount` command followed by
   the device identifier/partition. For example, to unmount all of the 
   ``/dev/sdc`` partitions:

   .. code-block:: bash

      sudo umount /dev/sdc*

#. Burn the image onto the USB drive. This example burns an image onto ``/dev/sdc``.  
   The device name of the USB may vary.

   .. code-block:: bash

      sudo dd if=./clear-[version number]-live-[desktop | server].iso of=/dev/sdc oflag=sync bs=4M status=progress

.. caution::

   Not fully unmounting the USB drive before burning an image could cause
   file system checksum errors in it. If this happens, burn the image again,
   ensuring all the USB drive partitions are unmounted first.

.. _bootable-usb-mac:

Create a bootable USB drive on macOS\*
**************************************

* Make sure you completed all `Prerequisites`_.

* :ref:`verify-mac` on macOS.

Burn the |CL| image onto a USB drive
====================================

.. caution::

   Burning an image formats the USB drive and destroys all pre-existing
   content.  Back up your data before proceeding.

#. Open a Terminal window.

#. Change directory to where the image resides.

#. Plug in a USB drive and get its identifier:

   .. code-block:: bash

      diskutil list

   This lists available disks and their partitions, as shown in Figure 1.

   .. figure:: /_figures/bootable-usb/bootable-usb-mac-01.png
      :scale: 100 %
      :alt: Get USB drive identifier

      Figure 1: macOS - Get USB drive identifier

#. Unmount the USB drive identified in the previous step. For example, to unmount /dev/disk2. The device name of the USB may vary.

   .. code-block:: bash

      diskutil umountDisk /dev/disk2

#. Burn the image onto the drive using the :command:`dd` command.
   This example uses `./`, your current directory, and it shows how to burn
   an image onto `/dev/disk2`:

   .. code-block:: bash

      sudo dd if=./clear-[version number]-live-[desktop | server].iso of=/dev/disk2 bs=4m

   To accelerate the imaging process, add an ‘r’ before the device identifier. Example: `sudo dd if=./clear-30800-live-server.iso of=/dev/rdisk2 bs=4m`.

   Press :kbd:`<CTRL>-T` to check imaging progress.

#. Eject the USB drive.

   .. code-block:: bash

      diskutil eject /dev/disk2

.. _bootable-usb-windows:

Create a bootable USB drive on Windows
**************************************

* Make sure you completed all `Prerequisites`_.

* :ref:`verify-windows` on Windows\* OS.

Burn the |CL| image onto a USB drive
====================================

.. caution::

   Burning an image formats the USB drive and destroys all pre-existing
   content.  Back up your data before proceeding.

#. Download the `Rufus`_ utility to burn the image onto a USB drive.
   We use Rufus 3.5 for this example.
   **Only use the latest version of Rufus**.

#. Plug in the USB drive.

#. Launch Rufus.

#. Under `Device`, select the USB drive.

#. Under `Boot selection`, click the :guilabel:`SELECT` button.

   .. note::

      For other image tools, verify the `Volume label` is set to :guilabel:`CLR_ISO` **Do not change the label as installer relies on it.**

#. In the dialog, navigate to where the |CL| ISO image was downloaded and select it.

#. Click the :guilabel:`START` button. See Figure 2.

   .. figure:: /_figures/bootable-usb/bootable-usb-windows-02.png
      :scale: 80 %
      :alt: Rufus utility

      Figure 2: Rufus utility

#. When the dialogue appears, select
   :guilabel:`Write in ISO image mode (Recommended)`. See Figure 3.

   .. figure:: /_figures/bootable-usb/bootable-usb-windows-03.png
      :scale: 80 %
      :alt: ISOHybrid image detected

      Figure 3: ISOHybrid image detected

#. Click :guilabel:`OK`.

#. The process make take more than a few minutes. When the process completes,
   close Rufus.

#. Select the Windows taskbar menu for USB and select
   :guilabel:`Eject <drive name>`.

.. _Rufus: https://rufus.ie/
.. _Downloads: https://clearlinux.org/downloads
