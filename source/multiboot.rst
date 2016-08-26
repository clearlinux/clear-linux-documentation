.. _multiboot: 

Creating a multiboot environment
################################

Introduction
============

Another customization option is to install Clear Linux* OS for
Intel® Architecture alongside other operating systems.

In this tutorial, we will show how to install Clear Linux build
9990 on a machine that will also be able to boot CentOS* 7 and Windows*
server 2016. These operating systems are, of course, only examples;
this process can be used to install a Clear Linux release alongside
whatever OSes you wish. 


Use case development
--------------------

For such a scenario, where the boot loader will be managed by
``systemd-boot``, we'll create disk partitioning to fit our
system requirements. If your system will require a different
partitioning, take into account the following:

* An :abbr:`EFI System Partition (ESP)` is required. Every OS can
  have its own ESP partition; and every ESP should be formatted.  

* In most cases the ESP will be mounted in ``/boot/efi``, with the
  exception of Clear Linux OS, which should be in ``/boot`` (Clear
  Linux OS doesn’t use GRUB). Windows does not mount ESPs automatically.

* The ESP partition is generally the first partition for performance
  reasons; however, Windows sets its recovery partition as first and
  ESP as second. Make note of which partition is the ESP because that
  information will be needed when configuring the boot loader.

* The size of the partition hosting root file systems should be
  large enough for core files and data. Generally, users like to have
  some free space. If you're unsure, 20 GB for each should be sufficient
  for a dual-boot, as Windows tends to need at least 10 GB of disk space.

* For Linux, there are multiple formats for disk partitioning. Some
  can be encrypted and some can be grouped; in these cases we will use
  standard partitioning formatted as ``ext4`` without any swap partitions.

* For Linux, partitions can be mounted on different paths, and in our
  use case we will use the simplest -- an ESP partition mounted in
  ``/boot/efi`` (Or ``/boot`` for Clear Linux) and an ``ext4`` Linux
  filesystem partition for root (at "``/``").

* Due to the fact that Windows creates its own partitioning scheme
  and recommends a specific order, we will install it before the others.

* Windows creates the ESP automatically, so you won’t be able to set
  the size. It defaults to 100 MB and should be enough for this case.
  Linux OSes generally reserve ~ 500 MB for this partition, but that
  much is not needed for this example.

* In general, the last OS installed will write the EFI. Since we want
  Linux to write its own EFI, it makes sense to install it afterward.

* We will use ``efibootmgr`` to manipulate the boot manager, so double
  check that your alternative Linux distribution has it (most do).

* CentOS 7 uses anaconda as the installer software. Fedora and RedHat
  do also, so the installation guide is the same as it is for either
  of these Linux distributions.


Prerequisites
=============

OS installation images
----------------------

For each OS you want to be able to boot into from the multiboot
environment, you'll need an installation image.  To create the specific
multiboot environment we proposed in the beginning of this tutorial,
you will need:

  *  A **Clear Linux OS image**, which can be downloaded from our
     `releases page`_; be sure to select a version that includes
     installer software.
  *  The **CentOS image** (select the "Minimal" version); links
     for where to download CentOS Minimal iso images can be found
     on the `CentOS website`_.
  *  A Windows installation image, or a system with Windows
     pre-installed can work just as well.

If you have non-installer versions of images you want to use in
your multiboot environment, pre-partitioning work should be done
before landing the images into the partitions.

Bootable media
--------------

Any bootable media that can be used to write installation images
will work. Our tutorial includes instructions for installing to an
Intel NUC using USB flash memory.  Burning installation images to a CD 
or DVD can also work if you don't have a flash drive handy.

Network connection
------------------

The Clear Linux OS installer uses a tool called ``swupd`` to manage
the installation, and ``swupd`` requires an internet connection. When no
internet is available, there are two ways to get around this: 

* Land a Clear Linux "live" image directly in the hard disk, or
* Use a private network to connect to a mixer server.

These edge cases won't be covered in this tutorial.  We are
assuming that the system you want to allow multiboot on has a
network connection and that internet access is available.

UEFI
----

Since ``systemd-boot`` uses this capability, it is required that the
images support UEFI.


Installing Windows
==================

Creating a bootable USB stick
-----------------------------

**This process has not been verified as it has known issues.**

An ISO-to-USB program can be used for Windows, or to get an
already bootable Windows USB stick. One way of doing this is to 
inject the :abbr:`Master Boot Record (MBR)` into the first logical
bytes of the USB stick; files can be found in the `syslinux distribution`_,
using :file:`gptmbr.bin`, since we want UEFI to boot:

1. Using GPT: Format USB stick with NTFS format and bootable flag.

2. Write MBR using: 
     
     # dd if=/usr/share/syslinux/gptmbr.bin of=/dev/sdb

3. Copy Windows files into USB stick.

4. Make sure to remove USB safely by # sync

This creates bootable Windows USB stick, (though you may run into permission
errors beyond the scope of this tutorial).


Installing Windows
------------------

Follow the installer until the screen where you select the disk
partition, then create a new partition of 20 GB, which Windows will
automatically split into its own partitions. Then select the one that
says "primary partition" to continue installation.

If you already have a previous OS installed, in order to avoid duplicate
of the ESP, just delete the system partition created by windows.

Wait until finish and then reboot.


Installing CentOS 7
===================

Creating a bootable USB stick for CentOS
----------------------------------------

Make note of where you downloaded the CentOS image.  Then insert your USB
and make note of where your system detects the USB drive.  Presuming it
is on ``dev/sdb``, you can run this command as root:

  # dd if=/path/to/your/CentOS-7-x86_64-Minimal.iso of=/dev/sdb && sync

The command should tell you when it finishes. 


Disk Partitioning and Installation
----------------------------------

Insert the bootable USB we just created and follow the instructions
as they are presented.  When you get to the "Installation destination"
section: 

1. Select the HDD.

2. Select the "I will configure partitioning" option.

3. Click "Done" (Left upper corner).

4. Create a 20 GB ``ext4`` partition mounted in ``/`` for the root file
   system, by clicking the "+" button.

5. Mount the ESP partition in ``/boot/efi``

6. Click "Done" (Left upper corner).

7. Accept changes.

Finally, click on the "Begin installation" button and enter a root password.
Wait to end and reboot.


Installing Clearlinux
=====================

Creating a bootable USB stick
-----------------------------

After you download the Clear Linux OS image, uncompress it
using ``unxz`` and do the same as for CentOS image::

  # dd if=/path/to/your/clear-9990-installer.img of=/dev/sdb
  # sync

Disk partitioning and installation
----------------------------------

Insert the Clear Linux OS bootable USB, turn on the computer, 
wait for it to boot, and installation software will start
automatically. Then follow these steps:

1. Select "Manual installation", then "I will configure partitioning".

2. Select the disk where you want your root filesystem and create a 20Gb
   Linux filesystem, then select "Next" .

3. Configure the mount point of the recently-created partition as root
   (``/``), and the ESP as ``/boot``; remember to NOT format partition.

4. Continue with the installation process, selecting bundles, user
   creation, and DHCP enabling).

5. Start the installation and reboot.


Configuring Boot Loader
=======================

For this section we will rely on ``efibootmgr`` tool, and more information
about this tool can be found here: `*http://linux.die.net/man/8/efibootmgr* <http://linux.die.net/man/8/efibootmgr>`__).
If your system automatically boots Windows, then you can find a
way to do this from Windows or to boot a Linux live media with
efibootmgr.

EFI boot manager
----------------

To see the current EFI settings:
 
  # efibootmgr -v

You should see the boot entries for your installed OSes, except for
Windows. Nevertheless, the EFI always comes with a Windows entry named
"Windows Boot Manager".

The ``systemd-boot`` entry should be the first one, and you can identify
it because is the one whose EFI points to :file:`/EFI/systemd/systemd-boot.efi`.
Specify a new order with option ``-o``; for example, if the ``systemd-boot``
entry is number 0006, you should type:

  # efibootmgr -o 6

When no ``systemd-boot`` entry exists, then you can create it as follows::

  # efibootmgr -c -L "Systemd-Boot" -l "\EFI\systemd\systemd-boot.efi"

**Note the backslashes instead of normal slashes.**

And then set it as first boot entry.


Configuring ``systemd-boot``
----------------------------

The configuration file of the loader is found in :file:`/loader/loader.conf`
in the ESP partition, where you can set the following options:

-  **default** -- Default entry to select (without the ``.conf`` suffix); may be
   a wildcard like ``arch-*``.

-  **timeout** -- Menu timeout in seconds. If this is not set, the menu will
   be shown only on key press during boot.

-  **editor** -- Whether to enable the kernel parameters editor or not. **1**
   (default) is to enable, **0** is to disable. Since the user can add
   ``init=/bin/bash`` to bypass root password and gain root access, it's
   strongly recommended to set this option to 0.

Setting the timeout option to 5 seconds or more is strongly recommended; this
will allow us to use a specific entry if default won’t boot due a mistake
made in configuring a boot entry.


Adding boot entries
-------------------

Systemd boot searches for boot menu items in ``/loader/entries/*.conf`` in
the ESP partition; each file found must contain exactly one boot entry. The
possible options are:

-  **title** -- Operating system name. *Required*.

-  **version** -- Kernel version, shown only when multiple entries with same
   title exist. *Optional*.

-  **machine-id** -- Machine identifier from ``/etc/machine-id``, shown only
   when multiple entries with same title and version exist. *Optional*.

-  **efi** -- EFI program to start, relative to your ESP (esp); for example:
   ``/vmlinuz-linux``. Either this or linux (see below) is required.

-  **options** -- Command-line options to pass to the EFI program or kernel
   boot parameters. Optional, but you will need at least ``initrd=efipath``
   and ``root=dev`` if booting Linux.

To learn more about this spec, see:

`*https://www.freedesktop.org/wiki/Specifications/BootLoaderSpec/* <https://www.freedesktop.org/wiki/Specifications/BootLoaderSpec/>`__.

CentOS boot entry
~~~~~~~~~~~~~~~~~

At this point you can find the Clear Linux OS entry, but are missing the
``centos.conf``. Here is an example::

  # cat loader/entries/centos.conf

  title		CentOS 7
  linux 	/vmlinuz-linux-3.10.0-300.4.6.el7.x86_64
  initrd 	initramfs-3.10.0-300.4.6.el7.x86_64.img
  options 	root=PARTUUID=14420948-2cea-4de7-b042-40f67c618660 ro quiet
  rhgb crashkernel=auto LANG en\_US.UTF-8

If we want this entry to work correctly, then we need to be sure that
the kernel image and initramfs image are found in the correct path in
the ESP partition. For CentOS 7, you can find them in ``/boot``; if you
have ESP mounted in ``/boot/efi``, for example, you would execute these
commands::

  # cp /boot/vmlinuz-linux-3.10.0-300.4.6.el7.x86_64 /boot/efi
  # cp /boot/initramfs-3.10.0-300.4.6.el7.x86_64.img /boot/efi

The correct UUID of the root partition can be found by executing the
following command::

  # ls -l /dev/disk/by-uuid

If you want the PARTUUID as the example above, then this is the command::

  # ls -l /dev/disk/by-partuuid

And lastly, the kernel boot options are found in the :file:`grub2.cfg`
file; find and inspect it to see what specific options your OS may need.

Windows boot entry
~~~~~~~~~~~~~~~~~~

``Systemd-boot`` comes with a predefined Windows entry named "Windows Boot
Manager", which you can select to boot Windows when using the following
path to boot: ``/EFI/Microsoft/Boot/bootmgfw.efi``.

If you want Windows to be the default boot, then you will have to create
a custom entry, like this::

  # cat loader/entries/windows.conf
  title Windows 8
  efi /EFI/Microsoft/Boot/bootmgfw.efi

And then change the default value in :file:`loader.conf` to "windows", to
automatically boot Windows next reboot.

Within Windows
--------------

If you have Windows started and want another OS to be the next default
boot OS, then you will need to modify the default value in the
:file:`loader.conf` file.

Windows does not mount ESP automatically, so open a console with
administrator privileges and type::

  # mountvol b: /s

Where ``b:`` is the letter assigned to the new drive.

If you want to unmount it, just::

  # mountvol b: /d

.. TODO: Find a way to use efibootmgr capabilities within Windows.


.. _releases page: https://download.clearlinux.org/releases
.. _CentOS website: https://www.centos.org/download/
.. _syslinux distribution: http://www.syslinux.org/wiki/index.php?title=Mbr

