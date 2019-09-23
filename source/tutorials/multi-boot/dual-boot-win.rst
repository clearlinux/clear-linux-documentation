.. _dual-boot-win:

Dual-boot |CL-ATTR| and Windows\* 10 OS
########################################

This guide shows how to install |CL-ATTR| adjacent to an existing Windows\*
10 :abbr:`OS (operating system)`. To add |CL| to an existing Windows installation, follow a method below.

.. contents::
   :local:
   :depth: 1

Description
***********

In this tutorial you'll :ref:`bare-metal-install-desktop` as
an additional partition. Alternatively, you may also
:ref:`bare-metal-install-server`.

Method 1: Shrink Windows partition and install |CL|
***************************************************
For this method, we shrink the Windows 10 OS partition to make space for |CL|.

#. Boot up the Windows 10 OS.

#. Launch the :file:`Disk Management` utility found under
   :guilabel:`Create and format hard disk partitions`.

#. Right-click the primary Windows partition and select :guilabel:`Shrink Volume...`.

   .. figure:: ../../_figures/multi-boot/dual-boot-win-01.png
      :width: 80%
      :alt: Disk Management > Shrink Volume

      Figure 1: Disk Management > Shrink Volume.

#. Shrink the size of the partition by at least the following amount:

   * For :ref:`installing the live desktop <bare-metal-install-desktop>`,
     allow at least 21GB.

   * For :ref:`installing the live server <bare-metal-install-server>`,
     allow at least 4GB.


#. We shrink C by about 21 GB, as shown in Figure 2.

   .. figure:: ../../_figures/multi-boot/dual-boot-win-02.png
      :width: 80%
      :alt: Shrink C

      Figure 2: Shrink C.

#. Shutdown the Windows 10 OS.

#. Follow the instructions to :ref:`bare-metal-install-desktop`.

#. After booting from the |CL| image, select the icon to
   launch the installer.

#. Click :guilabel:`Select Installation Media`.

#. Select :guilabel:`Safe Installation`.

#. Go through the remaining steps to install |CL|.

#. Shut down your system and remove the USB.

#. Reboot.

#. During the BIOS POST stage, press :kbd:`F10`, or the proper F-key for your
   system, to launch the :guilabel:`Boot Menu`.

   .. figure:: ../../_figures/multi-boot/dual-boot-win-03.png
      :width: 80%
      :alt: Boot menu

      Figure 3: Boot menu

#. In the :guilabel:`Boot Menu`, use the arrow to select the
   :guilabel:`OS bootloader` as boot device (highlighted).

   Some BIOSes do not support listing multiple partitions. In this case,
   it will only show one bootable partition.

   .. tip::

      If you don't want to use the BIOS boot menu each time to select an OS,
      follow :ref:`Advanced: Use systemd-boot to boot Windows 10 OS and |CL| <advanced-systemd-boot>`.

Method 2: Add another hard disk to your system where you install |CL|
*********************************************************************

#. Shutdown your system.

#. Open your system and attach another hard drive.

#. Power up your system.

#. Follow the instructions in :ref:`bare-metal-install-desktop`, and launch
   the |CL| installer.

#. In the :guilabel:`Required options` tab, choose :guilabel:`Select
   Installation Media`.

#. Within that menu, select :guilabel:`Destructive Installation`, and
   select the new hard drive from the device list.

   .. note::

      Make sure you don’t select the drive with your Windows 10 OS.

#. Go through remaining steps to complete the installation.

#. Reboot.

#. During the BIOS POST stage, press :kbd:`F10`, or the proper F-key for your
   system, to launch the :guilabel:`Boot Menu`.

   .. figure:: ../../_figures/multi-boot/dual-boot-win-03.png
      :width: 80%
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

If you prefer not to use your BIOS to load the :guilabel:`Boot Menu` and select an OS to boot, you can make :command: `systemd-boot` the default bootloader and add Windows 10 OS to the boot list. This option is also a workaround for BIOSes that don’t support booting more than one partition.

#. Boot up the |CL| installer.

#. Open a Terminal window and enter:

   .. code-block:: bash

      lsblk

#. Example output:

   .. code-block:: console

      clrlinux@clr-live~ $ lsblk
      NAME   MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
      loop0    7:0    0   2.3G  1 loop
      sda      8:0    0 335.4G  0 disk
      ├─sda1   8:1    0   450M  0 part
      ├─sda2   8:2    0   100M  0 part
      ├─sda3   8:3    0    16M  0 part
      ├─sda4   8:4    0   286G  0 part
      ├─sda5   8:5    0   143M  0 part
      ├─sda6   8:6    0   244M  0 part
      └─sda7   8:7    0  48.5G  0 part
      sdb      8:16   1     7G  0 disk
      ├─sdb1   8:17   1   2.5G  0 part
      └─sdb2   8:18   1   100M  0 part

#. The example output shows:

   * /dev/sda2 is the EFI system partition created by Windows
   * /dev/sda4 is the primary Windows partition
   * /dev/sda5 is the EFI system partition created by Clear Linux
   * /dev/sda7 is the Clear Linux root partition

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

      sudo clr-boot-manager update --path=/mnt/clearlinux

#. Umount all partitions.

   .. code-block:: bash

      sudo umount /mnt/windows-efi /mnt/clearlinux/boot /mnt/clearlinux

#. Reboot

   .. code-block:: bash

      sudo reboot

#. Remove the |CL| installer USB thumb drive.

#. You should be presented with the :command:`systemd-boot` menu, as shown
   below.

   .. figure:: ../../_figures/multi-boot/dual-boot-win-04.png
      :width: 80%
      :alt: systemd-boot menu

      Figure 5: systemd-boot menu


