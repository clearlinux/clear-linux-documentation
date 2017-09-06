.. _bootable-usb-linux:

Create a bootable USB on a Linux distribution
=============================================

Follow these instructions to create a bootable |CL| USB drive.
We have alternative instructions to :ref:`bootable-usb-mac` or
:ref:`bootable-usb-windows`. We recommend you use an **8GB** USB drive or
larger.

.. _download-cl-image:

Download the Latest Clear Linux Image
-------------------------------------

Get the latest available |CL| installer image that you want to install
to your system by using your web browser and downloading the latest
:file:`clear-[release]-installer.img.xz` file from
https://download.clearlinux.org/image/ where `[release]` is the release
number of the current image that is available in this directory listing.

.. note::

   For installing Clear Linux as a live image, look for
   “clear-[release]-live.img.xz”.

This example uses release 10980 so we will download the
:file:`clear-10980-installer.img.xz` image file and, optionally, the
:file:`clear-10980-installer.img.xz-SHA512SUMS` file needed to verify the
download.

Verify the download (recommended)
---------------------------------

#. Go to the directory with the downloaded files.
#. To verify the integrity of the file, enter the following commands:

   .. code-block:: console

      sha512sum ./clear-10980-installer.img.xz | diff ./clear-10980-installer.img.xz-SHA512SUMS -

If the files differ, the diff command outputs the difference to the console,
otherwise, diff does not have any output to the console and returns you to
the command prompt.

.. _copy-usb-linux:

Copy the Clear Linux image to a USB drive
-----------------------------------------

This example was created on an Ubuntu 16.04-based system where the USB
drive is identified as :file:`/dev/sdb`. Make sure you map the correct USB
device for this process.

Copying the |CL| image onto the USB drive formats the drive as a UEFI boot
device. Therefore, the contents of the USB drive will be destroyed during the
creation of the bootable USB drive. Make sure to save anything stored in the
drive before proceeding.

   #. Ensure the device is not mounted.

      .. code-block:: console

         umount /dev/sdb

   #. Log in as root.

      .. code-block:: console

         su

      Once prompted, enter your root password.  Alternatively you can enter:

      .. code-block:: console

         sudo -s

   #. Extract the downloaded image file and put it on the USB drive.

      .. code-block:: console

         xzcat clear-10980-installer.img.xz | dd of=/dev/sdb

      .. note::

         These commands only work in the directory containing the downloaded
         file.

      The decompression and copy of the image file takes some time to complete.

.. _usb-next:

Next steps
----------

With a bootable |CL| USB drive, you can:

* :ref:`bare-metal-install`
* :ref:`live-image`
