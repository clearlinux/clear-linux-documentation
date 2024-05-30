.. _change-kernel-boot:

Change Kernel Boot
########################

This tutorial explains the process of change kernel boot entry |CL-ATTR|.

.. contents::
   :local:
   :depth: 1

Description
***********

For this tutorial, you will modify your kernel list to boot with the kernel you want to use. This process is valid when you cannot compile third-party kernel modules and need to come back to old, or if you compile your custom kernel.


Get the current boot status
***************************

.. code-block:: bash

   bootctl status

This is an example output:

.. code-block:: bash

    System:
        Firmware: UEFI 2.70 (HP 265.256)
        Firmware Arch: x64
        Secure Boot: disabled
        TPM2 Support: yes
        Measured UKI: no
        Boot into FW: supported
  
    Current Boot Loader:
          Product: systemd-boot 255
         Features: ✓ Boot counting
                   ✓ Menu timeout control
                   ✓ One-shot menu timeout control
                   ✓ Default entry control
                   ✓ One-shot entry control
                   ✓ Support for XBOOTLDR partition
                   ✓ Support for passing random seed to OS
                   ✓ Load drop-in drivers
                   ✓ Support Type #1 sort-key field
                   ✓ Support @saved pseudo-entry
                   ✓ Support Type #1 devicetree field
                   ✓ Enroll SecureBoot keys
                   ✓ Retain SHIM protocols
                   ✓ Menu can be disabled
                   ✓ Boot loader sets ESP information
              ESP: /dev/disk/by-partuuid/ea2e4278-5c0c-4498-bc99-dfc48a71ceb5
             File: └─/EFI/org.clearlinux/loaderx64.efi
    
    Random Seed:
     System Token: set
           Exists: yes
    
    Available Boot Loaders on ESP:
              ESP: /boot (/dev/disk/by-partuuid/ea2e4278-5c0c-4498-bc99-dfc48a71ceb5)
             File: ├─/EFI/systemd/systemd-bootx64.efi (systemd-boot 255)
                   └─/EFI/BOOT/BOOTX64.EFI (systemd-boot 255)
    
    Boot Loaders Listed in EFI Variables:
            Title: Linux bootloader
               ID: 0x0007
           Status: active, boot-order
        Partition: /dev/disk/by-partuuid/ea2e4278-5c0c-4498-bc99-dfc48a71ceb5
             File: └─/EFI/org.clearlinux/bootloaderx64.efi
    
            Title: Linux Boot Manager
               ID: 0x0001
           Status: active, boot-order
        Partition: /dev/disk/by-partuuid/ea2e4278-5c0c-4498-bc99-dfc48a71ceb5
             File: └─/EFI/systemd/systemd-bootx64.efi
    
            Title: Windows Boot Manager
               ID: 0x0000
           Status: active, boot-order
        Partition: /dev/disk/by-partuuid/48d8a9eb-d84d-4a62-8302-edff383290e5
             File: └─/EFI/Microsoft/Boot/bootmgfw.efi
    
    Boot Loader Entries:
            $BOOT: /boot (/dev/disk/by-partuuid/ea2e4278-5c0c-4498-bc99-dfc48a71ceb5)
            token: clear-linux-os
    
    Default Boot Loader Entry:
             type: Boot Loader Specification Type #1 (.conf)
            title: Clear Linux OS (Clear-linux-native-6.8.10-1434.conf)
               id: Clear-linux-native-6.8.10-1434.conf
           source: /boot//loader/entries/Clear-linux-native-6.8.10-1434.conf
            linux: /boot//EFI/org.clearlinux/kernel-org.clearlinux.native.6.8.10-1434
           initrd: /boot//EFI/org.clearlinux/freestanding-00-early-ucode.cpio
                   /boot//EFI/org.clearlinux/initrd-org.clearlinux.native.6.8.10-1434
                   /boot//EFI/org.clearlinux/freestanding-clr-init.cpio.gz
                   /boot//EFI/org.clearlinux/freestanding-i915-firmware.cpio
          options: root=UUID=67e7ac9a-f7a1-4d5e-bbd6-012f5fa81cb5 rd.luks.uuid=abe6aaf2-3425-4eb1-b7f5-3f36746426fa quiet console=tty0 console=ttyS0,115200n8 cryptomgr.notests init=/usr/bin/initra-desktop initcall>
    lines 20-71/71 (END)
                   ✓ Support @saved pseudo-entry
                   ✓ Support Type #1 devicetree field
                   ✓ Enroll SecureBoot keys
                   ✓ Retain SHIM protocols
                   ✓ Menu can be disabled
                   ✓ Boot loader sets ESP information
              ESP: /dev/disk/by-partuuid/ea2e4278-5c0c-4498-bc99-dfc48a71ceb5
             File: └─/EFI/org.clearlinux/loaderx64.efi
    
    Random Seed:
     System Token: set
           Exists: yes
    
    Available Boot Loaders on ESP:
              ESP: /boot (/dev/disk/by-partuuid/ea2e4278-5c0c-4498-bc99-dfc48a71ceb5)
             File: ├─/EFI/systemd/systemd-bootx64.efi (systemd-boot 255)
                   └─/EFI/BOOT/BOOTX64.EFI (systemd-boot 255)
    
    Boot Loaders Listed in EFI Variables:
            Title: Linux bootloader
               ID: 0x0007
           Status: active, boot-order
        Partition: /dev/disk/by-partuuid/ea2e4278-5c0c-4498-bc99-dfc48a71ceb5
             File: └─/EFI/org.clearlinux/bootloaderx64.efi
    
            Title: Linux Boot Manager
               ID: 0x0001
           Status: active, boot-order
        Partition: /dev/disk/by-partuuid/ea2e4278-5c0c-4498-bc99-dfc48a71ceb5
             File: └─/EFI/systemd/systemd-bootx64.efi
    
            Title: Windows Boot Manager
               ID: 0x0000
           Status: active, boot-order
        Partition: /dev/disk/by-partuuid/48d8a9eb-d84d-4a62-8302-edff383290e5
             File: └─/EFI/Microsoft/Boot/bootmgfw.efi
    
    Boot Loader Entries:
            $BOOT: /boot (/dev/disk/by-partuuid/ea2e4278-5c0c-4498-bc99-dfc48a71ceb5)
            token: clear-linux-os
    
    Default Boot Loader Entry:
             type: Boot Loader Specification Type #1 (.conf)
            title: Clear Linux OS (Clear-linux-native-6.8.10-1434.conf)
               id: Clear-linux-native-6.8.10-1434.conf
           source: /boot//loader/entries/Clear-linux-native-6.8.10-1434.conf
            linux: /boot//EFI/org.clearlinux/kernel-org.clearlinux.native.6.8.10-1434
           initrd: /boot//EFI/org.clearlinux/freestanding-00-early-ucode.cpio
                   /boot//EFI/org.clearlinux/initrd-org.clearlinux.native.6.8.10-1434
                   /boot//EFI/org.clearlinux/freestanding-clr-init.cpio.gz
                   /boot//EFI/org.clearlinux/freestanding-i915-firmware.cpio
          options: root=UUID=67e7ac9a-f7a1-4d5e-bbd6-012f5fa81cb5 rd.luks.uuid=abe6aaf2-3425-4eb1-b7f5-3f36746426fa quiet console=tty0 console=ttyS0,115200n8 cryptomgr.notests init=/usr/bin/initra-desktop initcall_debug intel_iommu=igfx_off kvm-intel.nested=1 no_timer_check noreplace-smp page_alloc.shuffle=1 rcupdate.rcu_expedited=1 rootfstype=ext4,btrfs,xfs,f2fs tsc=reliable rw module.sig_unenforce rootflags=x-systemd.device-timeout=0

Get the kernel list installed
*****************************

.. code-block:: bash

   bootctl list

And example output:

.. code-block:: bash

    type: Boot Loader Specification Type #1 (.conf)
    title: Clear Linux OS (Clear-linux-preempt_rt-6.1.38-105.conf)
    id: Clear-linux-preempt_rt-6.1.38-105.conf
    source: /boot//loader/entries/Clear-linux-preempt_rt-6.1.38-105.conf
    linux: /boot//EFI/org.clearlinux/kernel-org.clearlinux.preempt_rt.6.1.38-105
    initrd: /boot//EFI/org.clearlinux/freestanding-00-early-ucode.cpio
            /boot//EFI/org.clearlinux/freestanding-clr-init.cpio.gz
            /boot//EFI/org.clearlinux/freestanding-i915-firmware.cpio
    options: root=UUID=67e7ac9a-f7a1-4d5e-bbd6-012f5fa81cb5 rd.luks.uuid=abe6aaf2-3425-4eb1-b7f5-3f36746426fa quiet console=tty0 console=ttyS0,115200n8 cryptomgr.notests init=/usr/bin/initra-desktop initcall_debug intel_iommu=igfx_off kvm-intel.nested=1 no_timer_check noreplace-smp page_alloc.shuffle=1 rcupdate.rcu_expedited=1 rootfstype=ext4,btrfs,xfs t>

    type: Boot Loader Specification Type #1 (.conf)
    title: Clear Linux OS (Clear-linux-native-6.9.1-1436.conf)
    id: Clear-linux-native-6.9.1-1436.conf
    source: /boot//loader/entries/Clear-linux-native-6.9.1-1436.conf
    linux: /boot//EFI/org.clearlinux/kernel-org.clearlinux.native.6.9.1-1436
    initrd: /boot//EFI/org.clearlinux/freestanding-00-early-ucode.cpio
            /boot//EFI/org.clearlinux/initrd-org.clearlinux.native.6.9.1-1436
            /boot//EFI/org.clearlinux/freestanding-clr-init.cpio.gz
            /boot//EFI/org.clearlinux/freestanding-i915-firmware.cpio
    options: root=UUID=67e7ac9a-f7a1-4d5e-bbd6-012f5fa81cb5 rd.luks.uuid=abe6aaf2-3425-4eb1-b7f5-3f36746426fa quiet console=tty0 console=ttyS0,115200n8 cryptomgr.notests init=/usr/bin/initra-desktop initcall_debug intel_iommu=igfx_off kvm-intel.nested=1 no_timer_check noreplace-smp page_alloc.shuffle=1 rcupdate.rcu_expedited=1 rootfstype=ext4,btrfs,xfs,f>

    type: Boot Loader Specification Type #1 (.conf)
    title: Clear Linux OS (Clear-linux-native-6.8.10-1434.conf) (default) (selected)
    id: Clear-linux-native-6.8.10-1434.conf
    source: /boot//loader/entries/Clear-linux-native-6.8.10-1434.conf
    linux: /boot//EFI/org.clearlinux/kernel-org.clearlinux.native.6.8.10-1434
    initrd: /boot//EFI/org.clearlinux/freestanding-00-early-ucode.cpio
            /boot//EFI/org.clearlinux/initrd-org.clearlinux.native.6.8.10-1434
            /boot//EFI/org.clearlinux/freestanding-clr-init.cpio.gz
            /boot//EFI/org.clearlinux/freestanding-i915-firmware.cpio
    options: root=UUID=67e7ac9a-f7a1-4d5e-bbd6-012f5fa81cb5 rd.luks.uuid=abe6aaf2-3425-4eb1-b7f5-3f36746426fa quiet console=tty0 console=ttyS0,115200n8 cryptomgr.notests init=/usr/bin/initra-desktop initcall_debug intel_iommu=igfx_off kvm-intel.nested=1 no_timer_check noreplace-smp page_alloc.shuffle=1 rcupdate.rcu_expedited=1 rootfstype=ext4,btrfs,xfs,f>

    type: Automatic
    title: Reboot Into Firmware Interface
    id: auto-reboot-to-firmware-setup
    source: /sys/firmware/efi/efivars/LoaderEntries-4a67b082-0a4c-41cf-b6c7-440b29bb8c4f

Set default kernel to boot
**************************

You can check the id from the latest command:

.. code-block:: bash

   bootctl list |grep id: |cut -f 2 -d ":"
     id: Clear-linux-preempt_rt-6.1.38-105.conf
     id: Clear-linux-native-6.9.1-1436.conf
     id: Clear-linux-native-6.8.10-1434.conf
     id: auto-reboot-to-firmware-setup


Set the kernel

.. code-block:: bash

   sudo bootctl set-default ID

For example to set 6.9.1 entry:

.. code-block:: bash

   sudo bootctl set-default Clear-linux-native-6.9.1-1436.conf

Just reboot

.. code-block:: bash

   sudo systemctl reboot

You will boot with the kernel set before.
