Fix Broken EFI Entry Post Setup
###############################

.. _fix-broken-efi-entry-post-setup:

This guide explains how to fix a EFI issue installation of |CL-ATTR| using a live 
desktop image on a USB.

.. contents::
   :local:
   :depth: 1

Overview
********

This guide assumes you have installed |CL| on a target system, but the OS
is not listed in your BIOS menu boot options.

Prerequisites
*************

* Download and burn the live desktop image on a USB. 
  See :ref:`bare-metal-install-desktop` for instructions.

Boot a live desktop image to fix target system
**********************************************

* Boot the |CL| live desktop image.

* Select |CL| in the boot menu.

Check the EFI table
*******************

  NOTE: You can see |CL| entry is not exists.

.. code-block:: bash

  sudo efibootmgr

  BootCurrent: 0003
  Timeout: 0 seconds
  BootOrder: 0003,0000
  Boot0000* Windows Boot Manager
  HD (1, GPT, 48d8a9eb-d84d-4a62-8302-edff383290e5, 0x800, 0x32000)/File(\EFI\Microsoft\Boot\bootmgfw.efi)57494e444f5753000100000088000000780000004200430044004f0042004a004500430054003d007b0039006400650061003800360
  032006300200350063006400640020034006500370030002d0061006300630031002d006600330032006200330034003400640034003700390035007d00000064000100000010000000040000007fff04000400000049535048
  Boot0003* SMI Corporation USB DISK AA00000000015194 PciRoot(0x0) /Pci (0x14,0x0) /USB (13,0)4eac0881119f594d850ee21a522c59b20980010049535048
  Boot0004* IPV6 Network - Realtek PCIe GBE Family Controller
  PciRoot (0x0) /Pci (0x1c,0x7)/Pci (0x0,0x0)/MAC (846993493dd4, 0) /IPv6 ([::]:<→>[::]:,0,0)4c0881119f594d850ee21a522c59b20000000049535048
  Boot0005 USB NETWORK BOOT: PciRoot (0x0) /Pci (0x0,0x0) /IPv4(0.0.0.00.0.0.0,0,0)4eac0881119f594d850ee21a522c59b21b08020049535048
  Boot0006 USB NETWORK BOOT: PciRoot (0x0) /Pci (0x0,0x0)/IPv6([::]:‹<->[::]:,0,0)4eac0881119f594d850ee21a522c59b21b10020049535048
  Boot0008 Seagate Basic 00000000NABC7P2Z PciRoot (0x0) /Pci (0x14,0x0) /USB (13,0)4eac0881119f594d850ee21a522c59b21180010049535048

   
Fix the entry menu
*************************************

* List the devices list entry.

  NOTE: In the next example, you can get the EFI partition located in `/dev/nvme0n1p5` and root partition `/dev/nvme0n1p6`.

.. code-block:: bash

  lsblk -o NAME,LABEL,PARTTYPE,PARTLABEL
  
  NAME       LABEL  PARTTYPE                             PARTLABEL
  nvme0n1                                                                                  
  ├─nvme0n1p1       c12a7328-f81f-11d2-ba4b-00a0c93ec93b EFI system partition
  ├─nvme0n1p2       e3c9e316-0b5c-4db8-817d-f92df00215ae Microsoft reserved partition
  ├─nvme0n1p3       ebd0a0a2-b9e5-4433-87c0-68b6b72699c7 Basic data partition
  ├─nvme0n1p4       de94bba4-06d1-4d40-a16a-bfd50179d6ac 
  ├─nvme0n1p5 boot  c12a7328-f81f-11d2-ba4b-00a0c93ec93b EFI
  └─nvme0n1p6 root  4f68bce3-e8cd-4db1-96e7-fbcaf984b709 /
    └─luks-2a2501d1-993e-4213-82df-35ab675cc0ab


* Generate a new entry

.. code-block:: bash

	sudo efibootmgr -c -d /dev/nvme0n1p5 -p 5 -L "Clear Linux" -l "\EFI\BOOT\BOOTX64.EFI"

* Check entries 

.. code-block:: bash

	sudo efibootmgr
    
    BootCurrent: 0001
    Timeout: 0 seconds
    BootOrder: 0001,0003,0000
    Boot0000* Windows Boot Manager  HD(1,GPT,48d8a9eb-d84d-4a62-8302-edff383290e5,0x800,0x32000)/File(\EFI\Microsoft\Boot\bootmgfw.efi)57494e444f5753000100000088000000780000004200430044004f0042004a004500430054003d007b00390064006500610038003600320063002d0035006300640064002d0034006500370030002d0061006300630031002d006600330032006200330034003400640034003700390035007d00000064000100000010000000040000007fff04000400000049535048
    Boot0001* Clear Linux  HD(5,GPT,1d92e9c4-13af-47f0-8f54-5f1e6b176d58,0x13423800,0x4a800)/File(\EFI\BOOT\BOOTX64.EFI)
    Boot0003* SMI Corporation USB DISK AA00000000015194  PciRoot(0x0)/Pci(0x14,0x0)/USB(13,0)4eac0881119f594d850ee21a522c59b20980010049535048
    Boot0004* IPV6 Network - Realtek PCIe GBE Family Controller  PciRoot(0x0)/Pci(0x1c,0x7)/Pci(0x0,0x0)/MAC(846993493dd4,0)/IPv6([::]:<->[::]:,0,0)4eac0881119f594d850ee21a522c59b20000000049535048
    Boot0005  USB NETWORK BOOT:    PciRoot(0x0)/Pci(0x0,0x0)/IPv4(0.0.0.00.0.0.0,0,0)4eac0881119f594d850ee21a522c59b21b08020049535048
    Boot0006  USB NETWORK BOOT:    PciRoot(0x0)/Pci(0x0,0x0)/IPv6([::]:<->[::]:,0,0)4eac0881119f594d850ee21a522c59b21b10020049535048
    Boot0008  Seagate Basic 00000000NABC7P2Z  PciRoot(0x0)/Pci(0x14,0x0)/USB(13,0)4eac0881119f594d850ee21a522c59b21180010049535048


  NOTE: If you don't see the boot order updated, you have to set the first entry to boot the system. If you have |CL| in the first option, you can avoid this step.
  
.. code-block:: bash

   sudo efibootmgr -o 0001,0003,0000

* Check entries 

.. code-block:: bash

	sudo efibootmgr
    
    BootCurrent: 0001
    Timeout: 0 seconds
    BootOrder: 0001,0003,0000
    Boot0000* Windows Boot Manager  HD(1,GPT,48d8a9eb-d84d-4a62-8302-edff383290e5,0x800,0x32000)/File(\EFI\Microsoft\Boot\bootmgfw.efi)57494e444f5753000100000088000000780000004200430044004f0042004a004500430054003d007b00390064006500610038003600320063002d0035006300640064002d0034006500370030002d0061006300630031002d006600330032006200330034003400640034003700390035007d00000064000100000010000000040000007fff04000400000049535048
    Boot0001* Clear Linux  HD(5,GPT,1d92e9c4-13af-47f0-8f54-5f1e6b176d58,0x13423800,0x4a800)/File(\EFI\BOOT\BOOTX64.EFI)
    Boot0003* SMI Corporation USB DISK AA00000000015194  PciRoot(0x0)/Pci(0x14,0x0)/USB(13,0)4eac0881119f594d850ee21a522c59b20980010049535048
    Boot0004* IPV6 Network - Realtek PCIe GBE Family Controller  PciRoot(0x0)/Pci(0x1c,0x7)/Pci(0x0,0x0)/MAC(846993493dd4,0)/IPv6([::]:<->[::]:,0,0)4eac0881119f594d850ee21a522c59b20000000049535048
    Boot0005  USB NETWORK BOOT:    PciRoot(0x0)/Pci(0x0,0x0)/IPv4(0.0.0.00.0.0.0,0,0)4eac0881119f594d850ee21a522c59b21b08020049535048
    Boot0006  USB NETWORK BOOT:    PciRoot(0x0)/Pci(0x0,0x0)/IPv6([::]:<->[::]:,0,0)4eac0881119f594d850ee21a522c59b21b10020049535048
    Boot0008  Seagate Basic 00000000NABC7P2Z  PciRoot(0x0)/Pci(0x14,0x0)/USB(13,0)4eac0881119f594d850ee21a522c59b21180010049535048


* Reboot the system, remove the live desktop USB drive, and boot into the repaired system.

.. code-block:: bash

   sudo reboot
