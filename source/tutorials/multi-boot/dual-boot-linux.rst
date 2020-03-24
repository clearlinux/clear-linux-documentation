.. _dual-boot-linux:

Dual-boot |CL-ATTR| with Any GRUB-based Linux\* Distro
##########################################################

In this tutorial, we show how to install |CL| alongside any GRUB-based 
Linux\* distro. To do so, we resize the existing Linux root partition to 
make room to install |CL|. Then we show 3 methods to dual-boot |CL| 
with an existing Linux distro.  

Although we use Ubuntu\* 19.04 Desktop as the example here, 
these instructions also work for other distros such as Mint\*, Kubuntu\*, 
Fedora\*, CentOS\*, among others.

.. contents::
   :local:
   :depth: 1

Prerequisites
*************

* Ubuntu 19.04 Desktop is already installed. 
* There is no unallocated space available, but there is free space 
  on the Ubuntu root partition.
* Follow the Preliminary steps that follow below. 

.. include:: ../../get-started/bare-metal-install-desktop.rst
   :start-after: preliminary-steps-install-desktop:
   :end-before: install-on-target-start:

Install |CL| with Advanced Installation
***************************************

#. Shut down the Ubuntu OS before proceeding.

#. Boot up the |CL| live desktop image, and click the penguin 
   icon, at left, to launch the installer.

#. Complete the :guilabel:`Required Options` until you reach 
   :guilabel:`Select Installation Media`. See Figure 1.

   .. rst-class:: dropshadow

   .. figure:: ../../_figures/multi-boot/dual-boot-linux-01.png
      :scale: 100%
      :alt: Required options

      Figure 1: Required options  

#. Click :guilabel:`Select Installation Media`.  

#. Select the “Advanced Installation” option. See Figure 2.  

   .. rst-class:: dropshadow

   .. figure:: ../../_figures/multi-boot/dual-boot-linux-02.png
      :scale: 100%
      :alt: Advanced Installation

      Figure 2: Advanced Installation 

#. Click :guilabel:`Partition Media` to start the GParted tool. 

#. Shrink the Ubuntu root partition to free up some space for |CL|.

   a. Select the Ubuntu root partition (in this example: /dev/sda2). 
      Right-click it and select “Resize/Move”.  See Figure 3.

      .. rst-class:: dropshadow

      .. figure:: ../../_figures/multi-boot/dual-boot-linux-03.png
         :scale: 100%
         :alt: Ubuntu root partition

         Figure 3: Ubuntu root partition

   #. In the :guilabel:`New size (MiB)` field, reduce the size of the root
      partition, leaving at least 22GB free. This allows enough space to 
      create a swap partition (250MB) and root partition (approx. 21GB) for 
      |CL|.  

      .. note:: 

         The resulting free space appears in the “Free space following 
         (MiB)”. Click the “Resize/Move” button.  See Figure 4.

      .. rst-class:: dropshadow

      .. figure:: ../../_figures/multi-boot/dual-boot-linux-04.png
         :scale: 100%
         :alt: Resize Ubuntu root

         Figure 4: Resize Ubuntu root

   #. Click the green checkmark button to proceed. See Figure 5.  

      .. rst-class:: dropshadow

      .. figure:: ../../_figures/multi-boot/dual-boot-linux-05.png
         :scale: 100%
         :alt: New unallocated space

         Figure 5: New unallocated space

#. Share the existing EFI system partition by designating as such.

   a. Right-click the :guilabel:`EFI System Partition` (e.g., /dev/sda1)
      and select :guilabel:`Name Partition`.  

   #. Set the name to “CLR_BOOT”.  See Figure 6 and Figure 7.  

      .. rst-class:: dropshadow

      .. figure:: ../../_figures/multi-boot/dual-boot-linux-06.png
         :scale: 100%
         :alt: Name CLR_BOOT partition

         Figure 6: Name CLR_BOOT partition

      .. rst-class:: dropshadow

      .. figure:: ../../_figures/multi-boot/dual-boot-linux-07.png
         :scale: 100%
         :alt: Resulting CLR_BOOT main screen

         Figure 7: Resulting CLR_BOOT main screen

#. Create a swap partition for |CL|.

   a. Right-click the “unallocated” partition and select :guilabel:`New` 
      to add a new partition.

   #. Enter “250” in the :guilabel:`New Size (MiB)` field to create a 
      250MB swap space. 

   #. Enter “CLR_SWAP” in the :guilabel:`Partition name` field and select
      “linux-swap” as the “File system” type.  

   #. Click the “Add” button.  See Figure 8.

      .. rst-class:: dropshadow

      .. figure:: ../../_figures/multi-boot/dual-boot-linux-08.png
         :scale: 100%
         :alt: Create CLR_SWAP partition

         Figure 8: Create CLR_SWAP partition

#. Create |CL| root partition.

   a. Right-click “unallocated” partition again and select :guilabel:`New` 
      to add a new partition.

   #. Create a partition that is at least 21GB, enter “CLR_ROOT” in the 
      :guilabel:`Partition name` field, and select a :guilabel:`File system` 
      type of your choice.    

   #. Click the “Add” button.  See Figure 9. 

      .. rst-class:: dropshadow

      .. figure:: ../../_figures/multi-boot/dual-boot-linux-09.png
         :scale: 100%
         :alt: Create CLR_ROOT partition

         Figure 9: Create CLR_ROOT partition

#. Click the green checkmark button to create the newly-defined partitions. 
   See Figure 10.  

   .. rst-class:: dropshadow

   .. figure:: ../../_figures/multi-boot/dual-boot-linux-10.png
      :scale: 100%
      :alt: Partitions to be created

      Figure 10: Partitions to be created

#. Close the GParted window, and the |CL| installer will reappear with 
   the newly-defined partitions to use.  See Figure 11.

   .. rst-class:: dropshadow

   .. figure:: ../../_figures/multi-boot/dual-boot-linux-11.png
      :scale: 100%
      :alt: |CL| installer partitions defined

      Figure 11: |CL| installer partitions defined

#. Complete the remaining steps of :guilabel:`Required Options` to 
   to install |CL|. Complete any :guilabel:`Advanced Options` as desired.
    
Boot |CL| Using One of Three Methods
************************************

Although we installed |CL| last, Ubuntu is still the default boot OS.  
There are three methods to boot |CL|:

#. Make systemd-boot, the boot loader that |CL| uses, the default
   boot loader to boot |CL| and also chain-boot GRUB; therefore, boot 
   Ubuntu.  See `boot-clr-method-1`_.

#. Use GRUB to chain-boot systemd-boot, therefore boot |CL|.
   See `boot-clr-method-2`_.

#. Use your BIOS “Boot Menu” to select and boot |CL|.  
   Refer to your system's manual on how to bring up the "Boot Menu".

.. _boot-clr-method-1:

Method 1: Use systemd-boot to Boot |CL| and also Chain-boot GRUB
================================================================

systemd-boot is the bootloader used by |CL|.  Because |CL| was installed
after a GRUB-based distro, GRUB is still the default bootloader.
In this method, we make systemd-boot the default bootloader instead and 
also provide a path to chain-boot GRUB.  

#. Boot up the |CL| installer image.

#. Open a terminal window. 

#. Identify the EFI system partition, Ubuntu root partition, and |CL| root
   partition. 

   .. code-block:: bash

      sudo fdisk -l

   Example output:

   .. code-block:: console

      clrlinux@clr-live~ $ sudo fdisk -l 
      ... 

      Disk /dev/sda: 335.4 GiB, 360080695296 bytes, 703282608 sectors
      Disk model: INTEL SSDSCKKF36
      Units: sectors of 1 * 512 = 512 bytes
      Sector size (logical/physical): 512 bytes / 512 bytes
      I/O size (minimum/optimal): 512 bytes / 1048576 bytes
      Disklabel type: gpt
      Disk identifier: D5CB69E9-2C27-4A16-9552-3CD6BFA5DA77

      Device         Start       End   Sectors   Size Type
      /dev/sda1       2048   1050623   1048576   512M EFI System
      /dev/sda2    1050624 498481151 497430528 237.2G Linux filesystem
      /dev/sda3  498481152 498993151    512000   250M Linux swap
      /dev/sda4  498993152 703281151 204288000  97.4G Linux root (x86-64)
      ...

   The above example output contains these partitions:

   * ``/dev/sda1`` is the EFI system partition originally created by Ubuntu 
     and shared with |CL|
   * ``/dev/sda2`` is the Ubuntu root partition
   * ``/dev/sda3`` is the swap partition for |CL|
   * ``/dev/sda4`` is the |CL| root partition

   The remaining steps will work with these partitions.

#. Mount these partitions.

   .. code-block:: bash
      
      sudo mkdir /mnt/clearlinux
      sudo mount /dev/sda4 /mnt/clearlinux/
      sudo mount /dev/sda1 /mnt/clearlinux/boot

#. Make systemd-boot the default bootloader.

   .. code-block:: bash	

      sudo bootctl install --esp-path=/mnt/clearlinux/boot

#. Add a timeout to systemd-boot so that it will present the menu of
   bootable OSes and give you time to select the one you want to boot. 

   .. code-block:: bash	

      sudo clr-boot-manager set-timeout 20 --path=/mnt/clearlinux

#. Add a system-boot boot entry for GRUB.
   
   .. code-block:: bash	

      sudo tee -a /mnt/clearlinux/boot/loader/entries/grub.conf << EOF
      title GRUB menu
      efi /EFI/ubuntu/grubx64.efi
      EOF

#. Umount all partitions. 

   .. code-block:: bash	
     
      sudo umount /mnt/clearlinux/boot /mnt/clearlinux

#. Reboot.

   .. code-block:: bash
   
      sudo reboot

#. Remove the |CL| installer USB thumb drive.

#. You should be presented with the :command:`systemd-boot` menu.
   See Figure 12. 

   .. figure:: ../../_figures/multi-boot/dual-boot-linux-12.png
      :scale: 100%
      :alt: systemd-boot menu showing GRUB

      Figure 12: systemd-boot menu showing GRUB

.. _boot-clr-method-2:

Method 2: Use GRUB to Boot |CL|
===============================

In this method, we keep GRUB as the default bootloader, but configure it
to chain-boot systemd-boot, thus allowing us to boot |CL|.  Again, we're using 
Ubuntu as our working example.

#. Boot up Ubuntu.

#. Open a terminal window.

#. Set a timeout value for the GRUB menu so it will be visible at boot time and 
   allow you select one which OS to boot.

   a. sudoedit :file:`/etc/default/grub`

      .. code-block:: bash

         sudoedit /etc/default/grub

   #. Set the ``GRUB_TIMEOUT`` variable to a desired value.

#. Create a menu entry for systemd-boot bootloader.

   a. Identify the UUID for EFI system partition that systemd-boot resides on.
      The example below shows the UUID for the EFI system on /dev/sda1 is 
      "A5A0-337D".

      .. code-block:: bash

         sudo blkid 

      Example output:
    
      .. code-block:: console
         :emphasize-lines: 1

         /dev/sda1: UUID="A5A0-337D" TYPE="vfat" PARTLABEL="CLR_BOOT" PARTUUID="ee664fec-1ade-40d0-9ce4-c08805003c8d"
         /dev/sda2: UUID="219969c5-1106-4e9f-b6f5-8188d7d94b8b" TYPE="ext4" PARTUUID="00bdf0dc-264d-493c-bf23-a85105011175"
         /dev/sda3: UUID="65221b07-33cb-40b7-9812-ea484c7606c9" TYPE="swap" PARTLABEL="CLR_SWAP" PARTUUID="5a7926b4-bd11-4bad-b932-cc31c0a75d27"
         /dev/sda4: UUID="0bedd545-58a7-4f34-b22a-c50bb4a1c2f5" TYPE="ext4" PARTLABEL="CLR_ROOT" PARTUUID="2d60cd03-5739-4cd5-adcc-51a107cde388"

   #. sudoedit :file:`/etc/grub.d/40_custom` and add a menu entry 
      for |CL| using UUID from the previous step (for example):

      .. code-block:: console
         :linenos:
         :emphasize-lines: 7-10

         #!/bin/sh
    	 exec tail -n +3 $0
         # This file provides an easy way to add custom menu entries. Simply type the
         # menu entries you want to add after this comment. Be careful not to change
         # the 'exec tail' line above.

         menuentry 'Clear Linux OS' {
            search --fs-uuid --no-floppy --set=root A5A0-337D
            chainloader (${root})/EFI/org.clearlinux/bootloaderx64.efi
         } 

   #. Update GRUB.

      .. code-block:: bash

         sudo update-grub

#. Reboot.

#. At the GRUB boot menu, select :guilabel:`Clear Linux OS` to boot |CL|.

#. Log in.

#. Open a terminal window.

#. By default, any future calls to :command:`clr-boot-manager`, such as 
   after a kernel update by :command:`swupd` or setting the timeout 
   value for systemd-boot, will modify the UEFI boot order 
   which will result in making systemd-boot the first boot 
   entry and you won't be able to boot Ubuntu any longer. And in order 
   to boot Ubuntu first, you must change the UEFI boot order back. 
   To prevent :command:`clr-boot-manager` from touching the UEFI boot 
   order, which is especially important in a dual-boot setup, 
   follow these steps:

   .. code-block:: bash

      sudo mkdir -p /etc/kernel
      sudo tee -a /etc/kernel/update_efi_vars << EOF
      false
      EOF
   
.. tip:: 
      
   The default installation of |CL| does not set a timeout value for 
   systemd-boot. Thus, you will not see the systemd-boot menu and the 
   default kernel will boot right away.  
   To set a timeout value (for example: 25 seconds), enter: 

   .. code-block:: bash

      sudo clr-boot-manager set-timeout 25

.. _download the live desktop image: https://clearlinux.org/downloads

.. _Downloads: https://clearlinux.org/downloads

