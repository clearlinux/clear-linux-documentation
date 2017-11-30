.. _bootable-usb-windows:

Create a bootable USB drive on Windows
**************************************

Follow these instructions to create a bootable |CLOSIA| USB drive.
Use an **8GB** or larger USB drive.

Alternative instructions for other operating systems are available:

* :ref:`bootable-usb-mac`
* :ref:`bootable-usb-linux`

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
   :Start-after: verify-image-checksum-on-windows:
   :end-before: uncompress-imag

.. Verify the integrity of the download (recommended)
.. ==================================================

.. #. Start Command-Prompt.
.. #. Go to the directory with the downloaded files.
.. #. To verify the integrity of the image, enter the following commands:

..	.. code-block console

..		C:\> CertUtil -hashfile ./clear-<version>-live.img.xz sha512

..   Compare the output with the original checksum to make sure they match.

Burn the Clear Linux image onto a USB drive
===========================================

.. include:: bootable-usb-linux.rst
   :Start-after: caution-burn-usb-drive:
   :end-before: end-caution-burn-usb-drive

.. caution

..   Backup important data before proceeding. The process of burning an image
..   onto the USB drive completely formats the
..   USB drive and any existing content will be destroyed.

#. Download the `Rufus`_ tool to burn the image onto a USB drive.
#. Plug in the USB drive.
#. Click the CD-ROM icon button and select the |CL| image file.  See Figure 1.
#. Ensure that :guilabel:`Create a bootable disk using DD
   Image` is checked. 

   .. figure:: figures/bootable-usb-windows-1.png
      :scale: 100 %
      :alt: Burn image onto USB drive

#. Click :guilabel:`Start`.

Next steps
----------

With a bootable |CL| USB drive, you can:

* :ref:`bare-metal-install`
* :ref:`boot-live-image`
* :ref:`multi-boot`

.. _Rufus: http://rufus.akeo.ie/
.. _releases: https://download.clearlinux.org/releases
.. _image: https://download.clearlinux.org/image
