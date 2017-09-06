.. _bootable-usb-windows:

Create a bootable USB drive on Windows
======================================

Follow these instructions to create a bootable |CL| USB drive. We recommend
you use an **8GB** USB drive or larger.

.. include:: bootable-usb-linux.rst
   :Start-after: download-cl-image:
   :end-before: copy-usb-linux

.. _copy-usb-windows:

Copy the Clear Linux image to a USB drive
-----------------------------------------

Copying the |CL| image onto the USB drive formats the drive as a UEFI boot
device. Therefore, the contents of the USB drive will be destroyed during the
creation of the bootable USB drive. Make sure to save anything stored in the
drive before proceeding.

#. Download the `Rufus`_ tool to burn the image onto a USB drive.

#. Plug in the USB drive.

#. Select the |CL| image file and ensure that “Create a bootable disk using DD
   Image” is checked. See Figure 1.

   .. figure:: figures/bootable-usb-windows-1.png
      :alt: Burn image onto USB drive

#. Click Start.

Next steps
----------

With a bootable |CL| USB drive, you can:

* :ref:`bare-metal-install`
* :ref:`live-image`

.. _Rufus: http://rufus.akeo.ie/