.. _gs_creating_bootable_usb:

Creating a bootable USB to install the OS
##########################################

Here's how to create a USB drive that initiates the process for
:ref:`gs_installing_clr_as_host`. Alternatively, you can test the 
OS by :ref:`vm-kvm`.


What you need
=============

* A USB stick, formatted as ``ext4``. Remember that the process of 
  flashing data to a USB completely deletes the contents of the
  drive; as always, run ``dd`` with caution.
* A Clear Linux* OS for Intel® Architecture image; the most current
  release versions can be found at the following link:
  `https://download.clearlinux.org/image <https://download.clearlinux.org/image>`_
* Older versions can be found on our `downloads page`_.


Download and checksum
=====================

::

  $ wget https://download.clearlinux.org/image/clear-[release_number]-installer.img.xz
  $ sha512sum clear-[release_number]-installer.img.xz


Confirm the mount point on the USB drive
========================================

Using ``$ lsblk`` is helpful to show the block-level devices; 
a USB drive usually shows up under ``/sdb`` or ``/sdc`` (almost never
under ``/sda``), and should indicate disk space approximately the 
size of the USB drive::

	$ lsblk /dev/sdb
	NAME MAJ:MIN RM SIZE RO TYPE MOUNTPOINT
	?? sdb  8:16 1 14.9G 0
	?? sdb1 8:17 1 14.9G 0 part

Make sure the drive isn't already mounted. The easiest way is with 
``umount`` or

::

	# df


Flash the image to the USB
==========================

Flash the image with the following command, adding the ``-v`` option 
for verbose mode (recommended), as the image file may be large, and the 
write can take a while. This may need to be done as root or with sudo::

  $ xzcat -v clear-[release_number]-installer.img.xz | dd of=/dev/sdb


Wait for the final confirmation
===============================

This example shows ``clear-9130-installer.img.xz`` flashed to a 16GB 
USB drive mounted on ``/sdb``.

.. image:: _static/images/gs_confirmation_screen.png
   :align: center
   :alt: confirmation

Success!  Your USB stick is now ready to boot and initiate the process for
:ref:`gs_installing_clr_as_host`.



.. _downloads page: https://download.clearlinux.org
