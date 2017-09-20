.. _bootable-usb-linux:

Create a bootable USB drive on Linux 
==============================

Follow these instructions to create a bootable |CL| USB drive.
Use an **8GB** or larger USB drive.

Alternative instructions for other operatings are available:

* :ref:`bootable-usb-mac`
* :ref:`bootable-usb-windows`

.. _download-cl-image:

Download the latest Clear Linux image
-------------------------------------

#. Go to the Clear Linux `image`_ repository and download the desired type:

   * Live image: `clear-<version>-live.img.xz`
   * Installer image: `clear-<version>-installer.img.xz`

   For older versions, see the `releases`_ page.

#. Although not required, it is recommended to download the corresponding 
   checksum file (designated with `-SHA512SUMS` at the end of the filename) for 
   the image in order to verify its integrity.  


.. Get the latest available |CL| image by using your web browser and downloading the latest
.. :file:`clear-[release]-installer.img.xz` file from
.. https://download.clearlinux.org/image/ where `[release]` is the release
.. number of the current image that is available in this directory listing.

.. ..note:

..  For installing Clear Linux as a live image, look for
..  “clear-[release]-live.img.xz”.

.. This example uses release 10980 so we will download the
.. :file:`clear-10980-installer.img.xz` image file and, optionally, the
.. :file:`clear-10980-installer.img.xz-SHA512SUMS` file needed to verify the
.. download.

.. _verify-checksum:

Verify the integrity of the download (recommended)
--------------------------------------------------

#. Start a terminal emulator.
#. Go to the directory with the downloaded files.
#. To verify the integrity of the image, enter the following (a `live` image 
   is used as example):

   .. code-block:: console

      $ sha512sum ./clear-<version>-live.img.xz | diff ./clear-<version>-live.img.xz-SHA512SUMS -

   
   If the checksum of the downloaded image is different than the original's, 
   the differences will displayed.  Otherwise, an empty output indicates a match.

.. _copy-usb-linux:

Burn the Clear Linux image onto a USB drive
-----------------------------------------

.. This example was created on an Ubuntu 16.04-based system where the USB
.. drive is identified as :file:`/dev/sdb`. Make sure you map the correct USB
.. device for this process.

.. caution::

   The process of burning an image onto the USB drive completely formats it. 
   Thus, any existing contents on it will be destroyed.  Backup important data 
   before proceeding.

#. Open a terminal emulator and get root privilege.

   .. code-block:: console

      $ sudo -s
  
#. Plug in the USB drive.

#. Identify the USB drive using the `lsblk` command.  This shows all drives 
   attached to the system, including the primary hard disk.  In the example output 
   below, there are 4 drives (`/dev/sda`, `/dev/sdb`, `/dev/sdc`, and `/dev/sdd`) attached, 
   where `/dev/sda` is primary drive in this case.  The remaining are 3 USB drives.  
   The output also shows the mounted partitions (under the `MOUNTPOINT` 
   column) for each drive.   

   .. code-block:: console

      # lsblk

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

#. Before an image can be burned onto a USB drive, it should be un-mounted.  Some 
   Linux distros may automatically mount a USB drive when it is plugged in. To
   unmount, use the `umount` command followed by the device identifier/partition. 
   For example: From the above `lsblk` output, `/dev/sdd` has 2 mounted partitions.
   Both will be umounted as follows:

   .. code-block:: console

      # umount /dev/sdd2
      # umount /dev/sdd3

#. Extract the downloaded image file and burn it onto the USB drive (`/dev/sdd` is used as an example).

   .. code-block:: console

      # xzcat clear-<version>-live.img.xz | dd of=/dev/sdd bs=4M status=progress

.. . Uncompress the image.
.. codeblock console
..      # unxz clear-<version>-live.img.xz
.. Burn the image onto the USB drive (for example `/dev/sdd`).
..   codeblock console
..      # dd if=/path/to/clear-<version>-live.img of=/dev/sdd bs=4M status=progress
..   #. Ensure the device is not mounted.  
..      code-block console
..         umount /dev/sdb
..  Log in as root.
..     code-block console
..        su
..     Once prompted, enter your root password.  Alternatively you can enter:
..      code-block console
..        sudo -s

..       note

..         These commands only work in the directory containing the downloaded
..         file.

..      The decompression and copy of the image file takes some time to complete.

.. _usb-next:

Next steps
----------

With a bootable |CL| USB drive, you can:

* :ref:`bare-metal-install`
* :ref:`boot-live-image`
* :ref:`multi-boot`

.. _releases: https://download.clearlinux.org/releases
.. _image: https://download.clearlinux.org/image

