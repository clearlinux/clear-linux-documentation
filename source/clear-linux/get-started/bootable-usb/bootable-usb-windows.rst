.. _bootable-usb-windows:

Create a bootable USB drive on Windows
**************************************

Follow these instructions to create a bootable |CLOSIA| USB drive.
Use an **8GB** or larger USB drive.

Alternative instructions for other operating systems are available:

* :ref:`bootable-usb-mac`
* :ref:`bootable-usb-linux`

.. include:: ../../guides/maintenance/download-verify-uncompress-linux.rst
   :Start-after: types-of-cl-images:
   :end-before: verify-image-checksum-on-linux

.. include:: bootable-usb-linux.rst
   :Start-after: download-usb-suitable-images:
   :end-before: end-download-usb-suitable-images

.. include:: ../../guides/maintenance/download-verify-uncompress-windows.rst
   :Start-after: verify-image-checksum-on-windows:
   :end-before: uncompress-image-on-windows

.. include:: ../../guides/maintenance/download-verify-uncompress-windows.rst
   :Start-after: uncompress-image-on-windows:

Burn the Clear Linux image onto a USB drive
===========================================

.. caution::

   |CAUTION-BACKUP-USB|

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
