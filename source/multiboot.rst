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
  enough. Generally, users like to have some free space for data.
  If you're unsure, 20 GB for each should be sufficient for a dual-boot
  of Linux and Windows.  Windows tends to need at least 10 GB of disk space.

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
  is too much.

* In general, the last OS installed will write the EFI. Since we want
  Linux to write its own EFI, it makes sense to install it afterward.

* We will use ``efibootmgr`` to manipulate the boot manager, so double
  check that your alternative Linux distribution has it (most do).

* Centos 7 uses anaconda as the installer software. Fedora and RedHat
  do also, so you should follow the installation guide as it is the
  same for any of these Linux distributions.


Prerequisites
=============

OS installation images
----------------------

The Clearlinux image can be downloaded from
`*https://download.clearlinux.org/releases/* <https://download.clearlinux.org/releases/>`__
where you can find all the versions and flavors of images. Choose a
recent one and the installer flavor which contains installer software
and sizes around 300 MB.

The Centos image can be found in their homepage, they have 3 flavors:
DVD, Everything and Minimal, in this case, a Minimal image will be used,
but should be the same for anyone. Besides this you can found another
distro image in it’s own page.

And for the windows image, get it from somewhere.

If you have Non-installer versions of the images, then pre partitioning
work should be done, and then land the images into the partitions.

Bootable media
--------------

This documentation includes the installation in an Intel’s NUC using a
USB flash memory, however it may also work if you burn the image in a
DVD or something and use a DVD drive. The USB stick capacity will depend
on the size of the image, for Linux’s images shouldn’t be a problem, but
I have seen Windows images of 10Gb, so take that in count.

Network connection
------------------

The Clearlinux installer uses swupd software to manage the installation
and it’s being done through internet. If no internet is available, then
you can do 2 things: to land a Clearlinux live image in the hard disk or
to use a private network to connect to a mixer server, these cases won’t
be covered in this documentation and we will assume that internet access
is available.

UEFI
----

Since ``systemd-boot`` uses this capability, it is required that the
images support UEFI.

Installing Windows
==================

Creating a bootable USB stick
-----------------------------

**This process has not been verified as it has known issues.**

I think that the best way is to use some kind of ISOtoUSB software for
windows or to get an already bootable Windows USB stick. What I did was
inject the Master Boot Record into the first bytes of the USB stick,
these file can be found in the syslinux distribution
(`*http://www.syslinux.org/wiki/index.php?title=Mbr* <http://www.syslinux.org/wiki/index.php?title=Mbr>`__)
I used the gptmbr.bin as I wanted UEFI to boot:

1. Using GPT: Format USB stick with NTFS format and bootable flag.

2. Write MBR using: # dd if=/usr/share/syslinux/gptmbr.bin of=/dev/sdb

3. Copy Windows files into USB stick.

4. Make sure to remove USB safely by # sync

This makes a WIndows bootable USB stick, but ran into permission access
error.

Installing Windows
------------------

Follow the installer until the screen where you select the disk
partition, then create a new partition of 20Gb which windows will
automatically split into its own partitions, then select the one that
says primary partition to continue installation.

If you already have a previous OS installed, in order to avoid duplicate
of the ESP, just delete the system partition created by windows.

Wait until finish and then reboot.

Installing Centos 7
===================

Creating a bootable USB stick
-----------------------------

It is very simple, after you download the image, insert the USB stick
and unmount it. You will need to make sure that you are using the
correct device mapped to your USB stick, in my case is /dev/sdb, and
execute with root privileges::

  # dd if=/path/to/your/CentOS-7-x86_64-Minimal.iso of=/dev/sdb
  # sync

Wait for it to finish, may take long, and that’s it.

Disk Partitioning and Installation
----------------------------------

Insert a Centos 7 bootable USB, turn on the computer wait it to boot and
start installation program by selecting “Install Centos 7” option. Next
select keyboard layout and click “Continue”. You can set at this moment
your hostname in the “Network & Hostname” section.

Click on “Installation destination” section.

1. Select the HDD.

2. Select the “I will configure partitioning” option

3. Click “Done” (Left upper corner)

4. Create a 20Gb ext4 partition mounted in “/” for root filesystem, by
   clicking the “+” button

5. Mount the ESP partition in /boot/efi

6. Click “Done” (Left upper corner)

7. Accept changes.

Click on “Begin installation” button. Select the root password. Wait to
end and reboot.

Installing Clearlinux
=====================

Creating a bootable USB stick
-----------------------------

After you download the Clearlinux image you will need to uncompress it
using unxz and do the same as for Centos image::

  # dd if=/path/to/your/clear-9990-installer.img of=/dev/sdb
  # sync

Disk partitioning and Installation
----------------------------------

Insert a Clearlinux bootable USB, turn on the computer wait it to boot
and installation software will start automatically. Then follow these
steps:

1. Select “Manual installation”, then “I will configure partitioning”.

2. Select the disk where you want your root filesystem and create a 20Gb
   Linux filesystem, then select “Next” .

3. Configure the mount point of the recently created partition as root
   (“/”), and the ESP as boot (“/boot”, remember NOT to format).

4. Continue with the installation process (Select bundles, user creation
   and DHCP enabling).

5. Start the installation and reboot.

Configuring Boot Loader
=======================

For this section we will rely on efibootmgr tool
(`*http://linux.die.net/man/8/efibootmgr* <http://linux.die.net/man/8/efibootmgr>`__).
If your system automatically boots Windows, then you will need to find a
way to do this from Windows or boot a Linux live media to use
efibootmgr.

EFI boot manager
----------------

See the current EFI settings:

# efibootmgr -v

You should see the boot entries for your installed OS, except for
windows. Nevertheless, the EFI always comes with a Windows entry named
“Windows Boot Manager”.

The systemd-boot entry should be the first one, you can identify it
because is the one whose EFI points to ‘/EFI/systemd/systemd-boot.efi’.
You can specify new order with option -o, for example, if systemd-boot
entry is number 0006, you should type::

  # efibootmgr -o 6

If there is no systemd-boot entry, then you should create it::

  # efibootmgr -c -L “Systemd-Boot” -l “\EFI\systemd\systemd-boot.efi”

**Note the backslashes instead of normal slashes.**

And then set it as first boot entry.

Configuring Systemd-boot
------------------------

The configuration file of the loader is found in /loader/loader.conf in
the ESP partition, where you can set the following options:

-  default - default entry to select (without the .conf suffix); can be
   a wildcard like arch-*

-  timeout - menu timeout in seconds. If this is not set, the menu will
   only be shown on key press during boot.

-  editor - whether to enable the kernel parameters editor or not. 1
   (default) is to enable, 0 is to disable. Since the user can add
   init=/bin/bash to bypass root password and gain root access, it's
   strongly recommended to set this option to 0.

I strongly recommend setting timeout option to 5 or more, since it will
allow us to use a specific entry if default won’t boot due a mistake
made in configuring a boot entry.

Adding boot entries
-------------------

Systemd boot searches for boot menu items in /loader/entries/*.conf in
ESP partition, each file found must contain exactly one boot entry. The
possible options are:

-  title - operating system name. Required.

-  version - kernel version, shown only when multiple entries with same
   title exist. Optional.

-  machine-id - machine identifier from /etc/machine-id, shown only when
   multiple entries with same title and version exist. Optional.

-  efi - EFI program to start, relative to your ESP (esp); e.g.
   /vmlinuz-linux. Either this or linux (see below) is required.

-  options - command line options to pass to the EFI program or kernel
   boot parameters. Optional, but you will need at least initrd=efipath
   and root=dev if booting Linux.

To learn more about this spec, go to:

`*https://www.freedesktop.org/wiki/Specifications/BootLoaderSpec/* <https://www.freedesktop.org/wiki/Specifications/BootLoaderSpec/>`__.

Centos boot entry
~~~~~~~~~~~~~~~~~

At this point you can find the Clearlinux entry but missing the
centos.conf, here is an example::

  # cat loader/entries/centos.conf

  title		Centos 7
  linux 	/vmlinuz-linux-3.10.0-300.4.6.el7.x86_64
  initrd 	initramfs-3.10.0-300.4.6.el7.x86_64.img
  options 	root=PARTUUID=14420948-2cea-4de7-b042-40f67c618660 ro quiet
  rhgb crashkernel=auto LANG en\_US.UTF-8

If we want this entry to work correctly, then we need to be sure that
the kernel image and initramfs image are found in the correct path in
the ESP partition. For centos you can find them in /boot, so if you have
ESP mounted in /boot/efi you should execute this commands::

  # cp /boot/vmlinuz-linux-3.10.0-300.4.6.el7.x86_64 /boot/efi
  # cp /boot/initramfs-3.10.0-300.4.6.el7.x86_64.img /boot/efi

The correct UUID of the root partition can be found executing the
following command::

  # ls -l /dev/disk/by-uuid

If you want the PARTUUID as the example above, then this is the command::

  # ls -l /dev/disk/by-partuuid

And finally, the kernel boot options are found in the grub2.cfg file,
just find and inspect the file to know if your OS needs specific
options.

Windows boot entry
~~~~~~~~~~~~~~~~~~

As I mentioned before Systemd-boot comes with a predefined Windows entry
named “Windows Boot Manager” which you can select to boot Windows, using
the following path to boot: /EFI/Microsoft/Boot/bootmgfw.efi.

If you want Windows to be the default boot, then you will have to create
a custom entry, like this::

  # cat loader/entries/windows.conf
  title Windows 8
  efi /EFI/Microsoft/Boot/bootmgfw.efi

And then change the default value in loader.conf to “windows”, to
automatically boot Windows next reboot.

Within Windows
--------------

If you have Windows started and want another OS to be the next default
boot OS, then you will need to modify the default value in the
loader.conf file.

Windows does not mount ESP automatically, you will need to open a
console with administrator privileges and type::

  # mountvol b: /s

Where b: is the letter assigned to the new drive.

If you want to unmount it, just::

  # mountvol b: /d

TODO: Find a way to use efibootmgr capabilities within Windows.
