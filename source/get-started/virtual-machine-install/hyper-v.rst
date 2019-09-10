.. _hyper-v:

|CL-ATTR| on Microsoft Hyper-V\*
################################

This page explains how to run a |CL-ATTR| :abbr:`VM (virtual machine)` on a
a Microsoft Hyper-V\* hypervisor.

.. contents::
   :local:
   :depth: 1


Overview
********

Hyper-V is a type 1 bare-metal hypervisor that runs directly on system
hardware.

Hyper-V is available both on server and client Windows operating systems as
`Hyper-V on Windows Server`_ and `Hyper-V on Windows 10`_.

Prerequisites
*************

* Enable virtualization, such as `Intel® Virtualization Technology`_
  (Intel® VT) and `Intel® Virtualization Technology for Directed I/O`_ (Intel®
  VT-d), on the host system from EFI/BIOS.

* Hyper-V installed on a capable Windows operating system. Refer to the
  Microsoft documentation on `Install the Hyper-V role on Windows Server`_ or
  `Install Hyper-V on Windows 10`_.

* Configure appropriate virtual networking in Hyper-V. Refer to the Microsoft
  documentation on `Create a virtual network on Window Server`_ or `Create a
  virtual network on Window 10`_.


Download the |CL| disk image for Hyper-V
****************************************

|CL| provide a virtual disk image for Hyper-V with |CL| pre-installed. This
includes a |CL| :ref:`Hyper-V specific kernel <compatible-kernels>` with
Hyper-V Linux drivers ready-to-go. Get the latest |CL| image for Microsoft*
Hyper-V from the `downloads`_ website. The file is named
:file:`clear-[VERSION]-hyperv.vhdx.gz`.

We also provide instructions for downloading and verifying a Clear Linux
images. For more information, refer to :ref:`download-verify-decompress`.

After extraction, the file should be named
:file:`clear-[VERSION]-hyperv.vhdx`.


Create and configure new VM
****************************

#. Open the **Hyper-V Manager** from the Start menu.

   .. figure:: figures/hyper-v/hyper-v-01.png
      :scale: 100%
      :alt: Hyper-V Manager from the Start menu

   Figure 1: Hyper-V Manager from the Start menu


#. Create a *New Virtual Machine* by clicking the :guilabel:`Action` menu and
   selecting the :guilabel:`New` submenu, and selecting :guilabel:`Virtual
   Machine...`.

   .. figure:: figures/hyper-v/hyper-v-02.png
      :scale: 100%
      :alt: New Virtual Machine in Hyper-V Manager

   Figure 2: New Virtual Machine in Hyper-V Manager

#. Follow the *New Virtual Machine Wizard* to create a new virtual machine
   specifying the options below:

   - **Name**: Choose name (e.g. ClearLinuxOS-VM).
   - **Generation**: Generation 2
   - **Startup memory**: 2048 MB or more
   - **Connect Virtual Hard Disk**: select :guilabel:`Use an existing virtual
     hard disk` and browse to find the :file:`clear-[VERSION]-hyperv.vhdx`
     file.

   After finishing the wizard, the VM will be created but not powered on.

#. Go to *Virtual Machine Settings* by right-clicking the newly created |CL|
   VM in the Hyper-V Manager and selecting :guilabel:`Settings...`

   - Under :guilabel:`Firmware`, select the Virtual disk and click
     :guilabel:`Move Up...` until it is at the top of the list. 

   - Under :guilabel:`Security`, uncheck the :guilabel:`Enable Secure Boot`
     checkbox.

   - Under :guilabel:`Processor`, consider increasing the number of virtual
     processors assigned to the |CL| VM for performance.

   .. figure:: figures/hyper-v/hyper-v-03.png
      :scale: 100%
      :alt: |CL| VM Settings in Hyper-V Manager

   Figure 3: |CL| VM Settings page after selections

#. Click :guilabel:`Apply` at the bottom of the VM Settings screen.

#. Click :guilabel:`OK` at the bottom of the VM Setting screen.


Start the VM
************

#. Start the |CL| VM by right-clicking the VM in Hyper-V Manager and selecting
   :guilabel:`Start`

#. Connect to the VM console by right-clicking the VM in Hyper-V Manager and
   selecting :guilabel:`Connect...`. A new *Virtual Machine Connection* window
   will appear.

#. After |CL| is booted, login to the console with user *root*. You will be
   prompted to set a new password immediately. 

   .. code-block:: console

      > User: root   

|CL-ATTR| on Microsoft Hyper-V\* is ready for use.

Related topics
**************

* :ref:`increase-virtual-disk-size`



.. _`Hyper-V on Windows Server`: https://docs.microsoft.com/en-us/windows-server/virtualization/hyper-v/hyper-v-on-windows-server
.. _`Hyper-V on Windows 10`: https://docs.microsoft.com/en-us/virtualization/hyper-v-on-windows/index
.. _`Intel® Virtualization Technology`: http://www.intel.com/content/www/us/en/virtualization/virtualization-technology/intel-virtualization-technology.html
.. _`Intel® Virtualization Technology for Directed I/O`: https://software.intel.com/en-us/articles/intel-virtualization-technology-for-directed-io-vt-d-enhancing-intel-platforms-for-efficient-virtualization-of-io-devices
.. _`Install the Hyper-V role on Windows Server`: https://docs.microsoft.com/en-us/windows-server/virtualization/hyper-v/get-started/install-the-hyper-v-role-on-windows-server
.. _Install Hyper-V on Windows 10: https://docs.microsoft.com/en-us/virtualization/hyper-v-on-windows/quick-start/enable-hyper-v
.. _`Create a virtual network on Window Server`: https://docs.microsoft.com/en-us/windows-server/virtualization/hyper-v/get-started/create-a-virtual-switch-for-hyper-v-virtual-machines
.. _`Create a virtual network on Window 10`: https://docs.microsoft.com/en-us/virtualization/hyper-v-on-windows/quick-start/connect-to-network
.. _downloads: https://clearlinux.org/downloads

