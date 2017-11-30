.. _bootable-usb-mac:

Create a bootable USB drive on macOS
************************************

Follow these instructions to create a bootable |CLOSIA| USB drive.
Use an **8GB** or larger USB drive.

Alternative instructions for other operating systems are available:

* :ref:`bootable-usb-linux`
* :ref:`bootable-usb-windows`

.. include bootable-usb-linux.rst
..   :Start-after: download-cl-image:
..   :end-before: verify-checksum

.. include:: ../../guides/maintenance/download-image.rst
   :Start-after: types-of-cl-images:
   :end-before: verify-image-checksum

.. include:: ../../guides/maintenance/download-image.rst
   :Start-after: verify-image-checksum:
   :end-before: verify-image-checksum-on-linux

.. include:: ../../guides/maintenance/download-image.rst
   :Start-after: verify-image-checksum-on-macos:
   :end-before: verify-image-checksum-on-windows


.. Verify the integrity of the download (recommended)
.. ==================================================

.. #. Start the Terminal app.
.. #. Go to the directory with the downloaded files.
.. #. To verify the integrity of the image, enter the following commands:

..   .. code-block console

..      $ shasum -a512 ./clear-<version>-live.img.xz | diff ./clear-<version>-live.img.xz-SHA512SUMS -

..   If the checksum of the downloaded image is different than the original's,
..   the differences will displayed.  Otherwise, an empty output indicates a match.

.. include:: ../../guides/maintenance/download-image.rst
   :Start-after: uncompress-image:
   :end-before: uncompress-image-on-linux

.. include:: ../../guides/maintenance/download-image.rst
   :Start-after: uncompress-image-on-mac:
   :end-before: uncompress-gz-on-mac

Burn the Clear Linux image onto a USB drive
===========================================

.. include:: bootable-usb-linux.rst
   :Start-after: caution-burn-usb-drive:
   :end-before: end-caution-burn-usb-drive

.. **Caution:** Backup important data before proceeding. The process of burning 
.. an image onto the USB drive completely formats the USB drive and any existing 
.. content will be destroyed.

#. Launch the Terminal app.
#. Go to the directory with the uncompressed image.
#. Plug in a USB drive and get its identifier by entering the command 
   `diskutil list`.  See Figure 1.

   .. code-block:: console

      $ diskutil list

   .. figure:: figures/bootable-usb-mac-1.png
      :scale: 100 %
      :alt: Get USB drive identifier

#. Unmount the USB drive identified in the previous step.  The command-line 
   example below umounts `/dev/disk2`:

   .. code-block:: console

      $ diskutil umountDisk /dev/disk2

#. Burn the image onto the drive.  The command-line example below burns an 
   uncompressed image onto `/dev/disk2`:

   .. code-block:: console

      $ sudo dd if=./clear-<version number>-<image type> of=/dev/rdisk2 bs=4m

   * Adding an ‘r’ in front of the disk identifier should help speed up the
     imaging process.
   * Press :kbd:`<CTL>-T` to check imaging progress.

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
