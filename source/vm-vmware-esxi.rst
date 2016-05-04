.. _vm-vmware-esxi:

Using *VMware** ESXi guest
##########################


This topic, which is based on *VMware vSphere 6*, explains how to use Clear Linux* OS
for Intel® Architecture as ESXi Guest.

Run Clear Linux OS for Intel Architecture
=========================================

#. Download the `latest`_ live version of the disk image.

#. Decompress the downloaded image. Uncompressed image size is ~ **5GB**.

#. Create a virtual machine with the following configuration:

   - **Guest OS**: Linux, Distribution Other 3.x Linux (64-bits)

   - **UEFI support**: Clear Linux uses `systemd-boot` as the UEFI boot manager
     for EFI images. Find the settings for this option using the vSphere GUI; go
     to the configuration settings of the virtual machine and select
     **EFI boot firmware**.

   - **IDE disk**: Convert to vmdk and attach the Clear Linux image you downloaded
     above. To convert Clear Linux image to VMware disk (vmdk) you can use the
     ``qemu-img`` command::

       $ qemu-img convert -f raw -O vmdk  -p clear-vmware.img clear-vmware.vmdk

#. Start the virtual machine


Using an optimized kernel for *VMware*
======================================

Clear Linux provides an optional bundle called *kernel-vmware* that contains a
specialized kernel with specific configuration for VMware hypervisor, including:

* **vmw_balloon** -- A technique for memory reclamation that works like a
  balloon. A guest can be inflated to reclaim physical memory. The balloon
  can also be deflated to allow the guest free memory pages.

* **vmw_pvscsi** -- A driver that allows use of the para-virtualized SCSI provided
  by *VMware* hypervisors.

* **vmxnet3** -- Allows use of VMware virtual ethernet NICs.

* **vmwgfx** -- Allows use of a DRM driver for the VMware virtual hardware

To use these features, add the ``kernel-vmware`` bundle to your Clear Linux install::

   # swupd bundle-add kernel-vmware

Now turn off the virtual machine and change the configuration as follows:

  - **Guest OS**: Linux / 3.x Linux (64-bits)

  - **UEFI support**: Clear Linux uses `systemd-boot` as the UEFI boot manager
     for EFI images. To add UEFI support, go to "Configuration settings of the
     virtual machine" -> "General Tab" -> "And select EFI boot firmware"

  - **SCSI Para-virtualized disk**: Convert the Clear Linux image to an SCSI
    VMware disk image and re-attach it.

    #. Extract the image from the EXSi server to one Linux machine and use
       ``qemu-img`` command::

       $ qemu-img convert -f raw -O vmdk -o adapter_type=lsilogic -o compat6 -p clear-vmware.img clear-vmware.vmdk

    #. Transfer the Clear Linux image to the VMware ESXi server and use the
       :command:`vmkfstools` command (you need to access to ESXi command line )::

       $ vmkfstools -i clear-vmware.vmdk -d zeroedthick clear-vmware-fix.vmdk

    #. Add the converted image to the guest by using VMware vSphere virtual
       machine settings

Finally, start the modified virtual machine.

.. _latest: https://download.clearlinux.org/latest

