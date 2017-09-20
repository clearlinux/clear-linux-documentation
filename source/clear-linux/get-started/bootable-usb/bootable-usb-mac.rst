.. _bootable-usb-mac:

Create a bootable USB drive on macOS
====================================

Follow these instructions to create a bootable |CL| USB drive.
Use an **8GB** or larger USB drive.

Alternative instructions for other operatings are available:

* :ref:`bootable-usb-linux`
* :ref:`bootable-usb-windows`

.. include:: bootable-usb-linux.rst
   :Start-after: download-cl-image:
   :end-before: verify-checksum:

Verify the integrity of the download (recommended)
--------------------------------------------------

#. Start the Terminal app.
#. Go to the directory with the downloaded files.
#. To verify the integrity of the image, enter the following commands:

   .. code-block:: console

      $ shasum -a512 ./clear-<version>-live.img.xz | diff ./clear-<version>-live.img.xz-SHA512SUMS -

   If the checksum of the downloaded image is different than the original's, 
   the differences will displayed.  Otherwise, an empty output indicates a match.

Burn the Clear Linux image onto a USB drive
-----------------------------------------
.. This example was created on an Ubuntu 16.04-based system where the USB
.. drive is identified as :file:`/dev/sdb`. Make sure you map the correct USB
.. device for this process.

.. caution::

   The process of burning an image onto the USB drive completely formats it. 
   Thus, any existing contents on it will be destroyed.  Backup important data 
   before proceeding.

.. Copy the Clear Linux image to a USB drive
.. -----------------------------------------

.. Copying the |CL| image onto the USB drive formats the drive as a UEFI boot
.. device. Therefore, the contents of the USB drive will be destroyed during the
.. creation of the bootable USB drive. Make sure to save anything stored in the
.. drive before proceeding.

#. Launch the Terminal application.

#. Uncompress the |CL| image.

   .. code-block:: console

      $ gunzip clear-<version>-live.img.xz

#. Plug in a USB drive and get its identifier. See Figure 1.

   .. code-block:: console

      $ diskutil list

   .. figure:: figures/bootable-usb-mac-1.png
      :alt: Get USB drive identifier

#. Unmount the USB drive identified in the previous step (using `/dev/disk2` as 
   the example)

   .. code-block:: console

      $ diskutil umountDisk /dev/disk2

#. Burn the image onto the drive.

   .. code-block:: console

      $ sudo dd if=/path/to/clear-<version>-live.img of=/dev/rdisk2 bs=4m

   * Adding an ‘r’ in front of the disk identifier should help speed up the imaging process.
   * Use `<CTL>-T` to check imaging progress. 

#. Eject the USB drive.

   .. code-block:: console

      $ diskutil eject /dev/disk2

Next steps
----------

With a bootable |CL| USB drive, you can:

* :ref:`bare-metal-install`
* :ref:`boot-live-image`
* :ref:`multi-boot`

.. _releases: https://download.clearlinux.org/releases
.. _image: https://download.clearlinux.org/image
