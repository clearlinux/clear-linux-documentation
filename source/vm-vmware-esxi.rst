.. _vm-vmware-esxi:

Using VMware* ESXi guest
========================

This documentation explains how to use Clear Linux as ESXi Guest.
This docuemnt is based on VMware vSphere 6.


****************
Run Clear Linux* 
****************

1. In order to boot Clear Linux* download the latest_ live disk image from
   https://download.clearlinux.org/image/

2. Decompress Clear Linux image. Uncompressed image size is ~ **5GiB**.

3. Create and configure a virtual machine with the following configuration:

  - Guest Operating system: **Linux, Distribution Other 3.x Linux (64-bits)**

  - **UEFI support**: Clear Linux uses as default bootloader systemd-boot a
    UEFI boot manager for EFI images

  .. tip::
    In VMware vShere GUI go to the configuration settings of the
    virtual machine->General Tab-> And select **EFI boot firmware**


  - **IDE disk**: Convert to vmdk and attach the Clear Linux image downloaded
    above. To convert Clear Linux image to VMWare* disk (vmdk) you can use
    qemu-img command::

      $qemu-img convert -f raw -O vmdk  -p clear-vmware.img clear-vmware.vmdk

4. Start the Clear Linux* virtual machine

*********************************
Using optimized kernel for VMware
*********************************

Clear Linux provides a bundle called *kernel-vmware* that contains a specialized
kernel that uses an specific configuration for *VMware hypervisor* such as:

- **vmw_balloon**: Use a technique for memory reclamation that works   a "balloon".
  The guest can be inflated to reclaim physical memory. The balloon can also be
  deflated to allow the guest free memory pages
- **vmw_pvscsi**: A driver that allows to use a paravirtualized SCSI provided by
  VMware* hypervisors
- **vmxnet3**: Allows to use  VMware virtual ethernet NIC
- **vmwgfx**: Allows to use DRM driver for the VMware virtual hardware

In order to use this features install the kernel-vmware bundle in you Clear
Linux using a virtual machine configured in the previos version::

  # swupd bundle-add kernel-vmware

Turn off virtual machine and change the virtual machine configuration as follow:

- Guest Operating system: Linux, Distribution Other 3.x Linux (64-bits)
- UEFI support: Clear Linux use as default bootloader systemd-boot  a UEFI boot
  manager for  EFI images. To add UEFI support go to:

  .. tip::
    Go to "Configuration settings of the virtual machine" -> "General Tab" ->
    "And select EFI boot firmware"

- SCSI Paravirtualized disk: Convert the Clear Linux image to a SCSI VMWare*
  disk imagek and attach it again
  To do this you can follow this steps:

  1. Extract the image from the EXSi server to one Linux machine and use
     qemu-img command::

       $ qemu-img convert -f raw -O vmdk -o adapter_type=lsilogic -o compat6 -p
       clear-vmware.img clear-vmware.vmdk

  2. Transfer the Clear Linux* image to the VMware* ESXi server and use
     :command:`vmkfstools` command (you need to access to ESXi command line )::

       $ vmkfstools -i clear-vmware.vmdk -d zeroedthick clear-vmware-fix.vmdk

  3. Add the converted image to the guest by using VMware* vSphere virtual
     machine settings

- Start the modificated virtual machine

.. _latest: https://download.clearlinux.org/latest

