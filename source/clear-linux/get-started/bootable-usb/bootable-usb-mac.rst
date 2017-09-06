.. _bootable-usb-mac:

Create a bootable USB drive on macOS
####################################

Follow these instructions to create a bootable |CL| USB drive. We recommend
you use an **8GB** USB drive or larger.

.. include:: bootable-usb-linux.rst
   :Start-after: download-cl-image:
   :end-before: copy-usb-linux

Copy the Clear Linux image to a USB drive
=========================================

Copying the |CL| image onto the USB drive formats the drive as a UEFI boot
device. Therefore, the contents of the USB drive will be destroyed during the
creation of the bootable USB drive. Make sure to save anything stored in the
drive before proceeding.

#. Launch the Terminal application.

#. Uncompress the |CL| live image.

   .. code-block:: console

      $ gunzip clear-<version>-live.img.xz

#.  Plug in a USB drive and get its identifier. See Figure 1.

   .. code-block:: console

      $ diskutil list

   .. figure:: figures/bootable-usb-mac-1.png
      :alt: Get USB drive identifier

#. Unmount the USB drive identified in the previous step (using /dev/disk2 as
   the example)

   .. code-block:: console

      $ diskutil umountDisk /dev/disk2

#. Burn the image (using /dev/disk2 as the example).

   .. code-block:: console

      $ sudo dd if=/path/to/clear-<version>-live.img of=/dev/rdisk2 bs=4m

   .. note::

      *  Adding an ‘r’ in front of the disk identifier should help speed up the
         imaging process.
      *  Use <CTL>-T to check imaging progress. 

#. Eject the USB drive.

   .. code-block:: console

      $ diskutil eject /dev/disk2

Next steps
==========

With a bootable |CL| USB drive, you can:

* :ref:`bare-metal-install`
* :ref:`live-image`
