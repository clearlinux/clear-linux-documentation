.. _vmware-esxi:

Use VMware\* ESXi guest
#######################


This section is based on *VMware vSphere 6* and explains how to use |CLOSIA|
as ESXi Guest.

Ensure `Intel® Virtualization Technology`_ (Intel® VT) and
`Intel® Virtualization Technology for Directed I/O`_ (Intel® VT-d) are both
enabled in your BIOS/UEFI firmware configuration.

Run Clear Linux OS for Intel Architecture
=========================================

#. Download the `latest`_ |CL| **live** version
   :file:`clear-{release-number}-live.img.xz`.

#. Decompress the downloaded image. Uncompressed image size is ~ **5GB**.

   * On Linux:

      .. code-block:: console

         $ xz -d clear-{release-number}-live.img.xz

   * On Windows, use `7zip`_.

     - Right-click the file and select
       :menuselection:`Extract in the same directory`.

       .. image:: ./figures/7zipwin.png
          :alt: 7zip extract here command

#. Create a virtual machine with the following configuration:

   * :guilabel:`Guest OS`: Linux, Distribution: Other 3.x Linux (64-bits)

   * :guilabel:`UEFI support`: |CL| uses `systemd-boot` as the UEFI
     boot manager for EFI images. Add UEFI support. Find this option's
     settings using the vSphere GUI. Go to the
     :menuselection:`Configuration settings of the virtual machine-->General`
     Tab and select :guilabel:`EFI boot firmware`.

   * :guilabel:`SCSI Para-virtualized disk`: Convert to
      :abbr:`VMDK (VMware DisK)` and attach the |CL| image downloaded above.

      + On Linux, To convert Clear Linux image to VMDK\* you can use the
        :command:`qemu-img` command:

         .. code-block:: console

            qemu-img convert -f raw -O vmdk -o adapter_type=lsilogic -o compat6 -p clear-vmware.img clear-vmware.vmdk

      + On Windows, convert the live image from RAW to VMDK format with a
        tool like :program:`VBoxManage` from `VirtualBox`_. You can refer on
        :ref:`how to create a VM on VirtualBox <create_vm_vbox>` as an
        example.

#. Transfer the Clear Linux image to the VMware ESXi server and use the
   :command:`vmkfstools` command. Access to ESXi command line is required:

   .. code-block:: console

      vmkfstools -i clear-vmware.vmdk -d zeroedthick clear-vmware-fix.vmdk

#. Add the converted image to the guest using the VMware vSphere virtual
   machine settings.

#. Start the virtual machine.

.. _latest: https://download.clearlinux.org/image/
.. _7zip: http://www.7-zip.org/
.. _VirtualBox: https://www.virtualbox.org/
.. _Intel® Virtualization Technology:
   http://www.intel.com/content/www/us/en/virtualization/virtualization-technology/intel-virtualization-technology.html
.. _Intel® Virtualization Technology for Directed I/O:
   https://software.intel.com/en-us/articles/intel-virtualization-technology-for-directed-io-vt-d-enhancing-intel-platforms-for-efficient-virtualization-of-io-devices

