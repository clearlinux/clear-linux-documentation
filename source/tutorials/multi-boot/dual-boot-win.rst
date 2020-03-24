.. _dual-boot-win:

Dual-boot |CL-ATTR| and Windows\* 10 OS
########################################

This guide shows how to install |CL-ATTR| adjacent to an existing Windows\*
10 :abbr:`OS (operating system)`. To add |CL| to an existing Windows installation, follow a method below.

In this tutorial you'll :ref:`bare-metal-install-desktop` as
an additional partition. Alternatively, you may also
:ref:`bare-metal-install-server`.

.. contents::
   :local:
   :depth: 1

Method 1: Shrink Windows partition and install |CL|
***************************************************
For this method, we shrink the Windows 10 OS partition to make space for |CL|.

#. Boot up the Windows 10 OS.

#. Launch the :file:`Disk Management` utility found under
   :guilabel:`Create and format hard disk partitions`.

#. Right-click the primary Windows partition and select :guilabel:`Shrink Volume...`.

   .. rst-class:: dropshadow

   .. figure:: ../../_figures/multi-boot/dual-boot-win-01.png
      :scale: 85%
      :alt: Disk Management > Shrink Volume

      Figure 1: Disk Management > Shrink Volume.

#. Shrink the size of the partition by at least the following amount:

   * For *Desktop* version, allow at least 21GB.

   * For *Server* version, allow at least 4GB.


#. We shrink C by about 21GB, as shown in Figure 2.

   .. rst-class:: dropshadow

   .. figure:: ../../_figures/multi-boot/dual-boot-win-02.png
      :scale: 85%
      :alt: Shrink C

      Figure 2: Shrink C.

#. Shutdown the Windows 10 OS.

#. Follow one of these guides to install |CL|:

   * *Desktop* version: :ref:`bare-metal-install-desktop`
   * *Server* version: :ref:`bare-metal-install-server`

   a. In the :guilabel:`Required options` tab, choose :guilabel:`Select
      Installation Media`.

   #. Within that menu, select :guilabel:`Safe Installation`.

   #. Go through remaining steps to complete the installation.

   #. Reboot.

#. During the BIOS POST stage, press :kbd:`F10`, or the proper F-key for your
   system, to launch the :guilabel:`Boot Menu`.

   .. rst-class:: dropshadow

   .. figure:: ../../_figures/multi-boot/dual-boot-win-03.png
      :scale: 85%
      :alt: Boot menu

      Figure 3: Boot menu

#. In the :guilabel:`Boot Menu`, use the arrow to select the
   :guilabel:`OS bootloader` as boot device (highlighted).

   Some BIOSes do not support listing multiple partitions. In this case,
   it will only show one bootable partition.

   .. tip::

      If you don't want to use the BIOS boot menu each time to select an OS,
      follow :ref:`Advanced: Use systemd-boot to boot Windows 10 OS and 
      |CL| <advanced-systemd-boot>`.

Method 2: Add another hard disk to your system where you installed Windows
**************************************************************************

#. Shutdown your system.

#. Open your system and attach another hard drive.

#. Power up your system.

#. Follow one of these guides to install |CL|:

   * *Desktop* version: :ref:`bare-metal-install-desktop`
   * *Server* version: :ref:`bare-metal-install-server`

   a. In the :guilabel:`Required options` tab, choose :guilabel:`Select
      Installation Media`.

   #. Within that menu, select :guilabel:`Destructive Installation`, and
      select the new hard drive from the device list.

      .. warning::

         Make sure you don’t select the drive with your Windows 10 OS.

    #. Go through remaining steps to complete the installation.

    #. Reboot.

#. During the BIOS POST stage, press :kbd:`F10`, or the proper F-key for your
   system, to launch the :guilabel:`Boot Menu`.

   .. rst-class:: dropshadow

   .. figure:: ../../_figures/multi-boot/dual-boot-win-03.png
      :scale: 85%
      :alt: Boot menu

      Figure 4: Boot menu

#. In the :guilabel:`Boot Menu`, use the arrow to select the
   :guilabel:`Linux bootloader` as boot device.

   Some BIOSes do not support listing multiple partitions. In this case,
   it will only show one bootable partition.

.. tip::

   If you don't want to use the BIOS boot menu each time to select an OS,
   follow the next section.

.. _advanced-systemd-boot:

Advanced: Use systemd-boot to boot Windows 10 OS and |CL|
*********************************************************

If you prefer not to use your BIOS to load the :guilabel:`Boot Menu` and select an OS to boot, you can make :command:`systemd-boot` the default bootloader and add Windows 10 OS to the boot list. This option is also a workaround for BIOSes that don’t support booting more than one partition.

#. Boot up a |CL| live image from a USB thumb drive. 

#. Open a terminal window and enter:

   .. code-block:: bash

      lsblk -po NAME,SIZE,TYPE,FSTYPE,PARTLABEL

   Example output:

   .. code-block:: console
      :emphasize-lines: 6,8,9,11

      clrlinux@clr-live~ $ lsblk -po NAME,SIZE,TYPE,FSTYPE,PARTLABEL
      NAME          SIZE TYPE FSTYPE   PARTLABEL
      /dev/loop0    2.3G loop squashfs 
      /dev/sda    335.4G disk
      ├─/dev/sda1   450M part ntfs     Basic data partition
      ├─/dev/sda2   100M part vfat     EFI system partition
      ├─/dev/sda3    16M part          Microsoft reserved partition
      ├─/dev/sda4   286G part ntfs     Basic data partition
      ├─/dev/sda5   143M part vfat     EFI
      ├─/dev/sda6   244M part swap     linux-swap
      └─/dev/sda7  48.5G part ext4     /
      sdb             7G disk iso9660
      ├─/dev/sdb1   2.7G part iso9660
      └─/dev/sdb2   100M part vfat

   The example output shows:

   * /dev/sda2 is the EFI system partition created by Windows 10 OS
   * /dev/sda4 is the primary Windows partition
   * /dev/sda5 is the EFI system partition created by |CL|
   * /dev/sda7 is the |CL| root partition

  .. note::

     To help narrow down a partition even more, you add the ``PARTTYPE`` 
     option to :command:`lsblk` and cross-reference against the 
     `partition type GUIDs wiki`_.

#. Create mount points.

   .. code-block:: bash

      sudo mkdir /mnt/windows-efi

      sudo mkdir /mnt/clearlinux

#. Mount the EFI system partition for Windows 10 OS.

   .. code-block:: bash

      sudo mount /dev/sda2 /mnt/windows-efi

#. Mount the |CL| root partition and its EFI system partition.

   .. code-block:: bash

      sudo mount /dev/sda7 /mnt/clearlinux

      sudo mount /dev/sda5 /mnt/clearlinux/boot

#. Copy Windows 10 OS bootloader, and other data needed to boot it, to the
   |CL| EFI system partition.

   .. code-block:: bash

      sudo cp -r /mnt/windows-efi/EFI/Microsoft/ /mnt/clearlinux/boot/EFI/

#. Make :command:`systemd-boot` the default bootloader and add Windows 10
   OS Boot Manager.

   .. code-block:: bash

      sudo bootctl install --esp-path=/mnt/clearlinux/boot

#. Add a timeout value to the :command:`systemd-boot`. This allows enough
   time for you to select your preferred OS from the menu.

   .. code-block:: bash

      sudo clr-boot-manager set-timeout 20 --path=/mnt/clearlinux

#. Umount all partitions.

   .. code-block:: bash

      sudo umount /mnt/windows-efi /mnt/clearlinux/boot /mnt/clearlinux

#. Reboot

   .. code-block:: bash

      sudo reboot

#. Remove the |CL| installer USB thumb drive.

#. You should be presented with the :command:`systemd-boot` menu, as shown
   below.

   .. rst-class:: dropshadow

   .. figure:: ../../_figures/multi-boot/dual-boot-win-04.png
      :scale: 85%
      :alt: systemd-boot menu

      Figure 5: systemd-boot menu


Alternative: Install Windows 10 OS After |CL|
*********************************************

The following alternative guide shows how to install Windows 10 OS adjacent
to an existing |CL| installation.

Prerequisites
*************

* |CL| is already installed.  
* There is unallocated disk space available. If the entire disk has been
  allocated to |CL|, then shrink the root partition to make space for 
  Windows 10 OS.

Install Windows 10 OS
=====================

#. Start the Windows installer and follow the prompts.

#. At the :guilabel:`What type of installation do you want?` screen, choose 
   :guilabel:`Custom: Install Windows only (advanced)`. See Figure 6.

   .. rst-class:: dropshadow

   .. figure:: ../../_figures/multi-boot/dual-boot-win-06.png
      :scale: 85%
      :alt: Windows - Choose installation type

      Figure 6: Windows - Choose installation type

#. Select :guilabel:`Unallocated Space` and create a new partition of 
   the desired size. For this example, we will use the entire unallocated 
   space. See Figure 7.

   .. rst-class:: dropshadow

   .. figure:: ../../_figures/multi-boot/dual-boot-win-07.png
      :scale: 85%
      :alt: Windows - Create new partition

      Figure 7: Windows - Create new partition

   .. note::
     
      Normally, Windows creates its own 100MB EFI partition if none exists. 
      In our case, where an EFI partition was created by |CL|, Windows will 
      use the previously-created partition.

#. Select the newly-created partition and follow the remaining prompts to 
   complete the Windows installation. See Figure 8.

   .. rst-class:: dropshadow

   .. figure:: ../../_figures/multi-boot/dual-boot-win-08.png
      :scale: 85%
      :alt: Windows - Install on newly-created partition

      Figure 8: Windows - Install on newly-created partition

#. Finish the Windows out-of-box-experience process.

#. Restore `systemd-boot` - the bootloader |CL| uses - and add Windows to 
   its boot menu.

   At this point, you cannot boot |CL| because Windows became the default 
   bootloader after it was installed.  Follow these steps to restore 
   `systemd-boot`.

   a. Boot up a |CL| live image from a USB thumb drive. 

   #. Open a terminal window. 

   #. Find the location of the EFI partition. In this example, it is 
      ``/dev/sda1``.

      .. code-block:: bash

         lsblk -po NAME,SIZE,TYPE,FSTYPE,PARTLABEL
      
      Example output:

      .. code-block:: console
         :emphasize-lines: 5

         clrlinux@clr-live~ $ lsblk -po NAME,SIZE,TYPE,FSTYPE,PARTLABEL
         NAME          SIZE TYPE FSTYPE   PARTLABEL
         /dev/loop0    2.3G loop squashfs 
         /dev/sda      100G disk
         ├─/dev/sda1   150M part vfat     CLR_BOOT
         ├─/dev/sda2   250M part swap     CLR_SWAP
         ├─/dev/sda3     8G part ext4     CLR_ROOT
         ├─/dev/sda4    16M part          Microsoft reserved partition
         ├─/dev/sda5  91.6G part ntfs     Basic data partition
         sdb             7G disk iso9660
         ├─/dev/sdb1   2.7G part iso9660
         └─/dev/sdb2   100M part vfat
         
      .. note::

         To help narrow down a partition even more, you add the 
         ``PARTTYPE`` option to :command:`lsblk` and 
         cross-reference against the `partition type GUIDs wiki`_.

   #. Make a mount point for |CL|.

      .. code-block:: bash
         
         sudo mkdir /mnt/clearlinux

   #. Mount the root and EFI partitions.

      .. code-block:: bash

         sudo mount /dev/sda3 /mnt/clearlinux
         sudo mount /dev/sda1 /mnt/clearlinux/boot

   #. Re-install systemd-boot to make it the default bootloader.
      
      .. code-block:: bash
      
         sudo bootctl install --esp-path=/mnt/clearlinux/boot

   #. Add a timeout (for example: 25 seconds) to systemd-boot so that it 
      will present the menu of bootable OSes and give you time to select 
      the one you want to boot.

      .. code-block:: bash

         sudo clr-boot-manager set-timeout 25 --path=/mnt/clearlinux
         sudo clr-boot-manager update --path=/mnt/clearlinux

   #. Unmount the root and EFI partitions.

      .. code-block:: bash
      
         sudo umount /mnt/clearlinux/boot
         sudo umount /mnt/clearlinux

.. _partition type GUIDs wiki: https://en.wikipedia.org/wiki/GUID_Partition_Table#Partition_type_GUIDs
