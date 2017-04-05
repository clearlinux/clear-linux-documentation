.. _vm-vmware-esxi:

Using *VMware** ESXi guest
##########################


This topic, which is based on *VMware vSphere 6*, explains how to use Clear Linux* OS
for Intel® Architecture as ESXi Guest.

Please ensure you have enabled `Intel® Virtualization Technology
<http://www.intel.com/content/www/us/en/virtualization/virtualization-technology/intel-virtualization-technology.html>`_ 
(Intel® VT) and `Intel® Virtualization Technology for Directed I/O
<https://software.intel.com/en-us/articles/intel-virtualization-technology-for-directed-io-vt-d-enhancing-intel-platforms-for-efficient-virtualization-of-io-devices>`_ 
(Intel® VT-d) in your BIOS/UEFI firmware configuration.

Run Clear Linux OS for Intel Architecture
=========================================

#. Download the `latest`_ |CL| **live** version (clear-XXXX-live.img.xz)

#. Decompress the downloaded image. Uncompressed image size is ~ **5GB**.

   + On Linux ::

       $ xz -d clear-XXXX-live.img.xz

   + On Windows you can use `7zip`_.

     - Right-click the file to *extract in the same directory*.

       .. image:: _static/images/7zipwin.png
          :alt: 7zip extract here command

#. Create a virtual machine with the following configuration:

   - **Guest OS**: Linux, Distribution Other 3.x Linux (64-bits)

   - **UEFI support**: Clear Linux uses `systemd-boot` as the UEFI boot manager
     for EFI images. To add UEFI support,
     find the settings for this option using the vSphere GUI; go
     to the "Configuration settings of the virtual machine", " General Tab"
     and select **EFI boot firmware**.

   - **SCSI Para-virtualized disk**: Convert to VMDK and attach the Clear
     Linux image you downloaded above. To convert Clear Linux image to
     VMware DisK (VMDK) you can use the
     ``qemu-img`` command::

       $ qemu-img convert -f raw -O vmdk -o adapter_type=lsilogic -o compat6 -p clear-vmware.img clear-vmware.vmdk

     * On Windows, you can convert the live image to VMDK format
       (from RAW format to VMDK) with a tool like *VBoxManage* from
       `VirtualBox`_. You can refer on
       :ref:`how to create a VM on VirtualBox <create_vm_vbox>` as example.

#. Transfer the Clear Linux image to the VMware ESXi server and use the
   :command:`vmkfstools` command (you need to access to ESXi command line )::

     $ vmkfstools -i clear-vmware.vmdk -d zeroedthick clear-vmware-fix.vmdk

#. Add the converted image to the guest by using VMware vSphere virtual
   machine settings

#. Start the virtual machine

.. _latest: https://download.clearlinux.org/image/
.. _7zip: http://www.7-zip.org/
.. _VirtualBox: https://www.virtualbox.org/

