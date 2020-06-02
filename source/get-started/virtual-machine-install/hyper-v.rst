.. _hyper-v:

|CL-ATTR| on Microsoft Hyper-V\*
################################

This page explains how to run a |CL-ATTR| :abbr:`VM (virtual machine)` on a
Microsoft\* Hyper-V\* hypervisor.

.. contents::
   :local:
   :depth: 1


Overview
********

Hyper-V is a type 1 bare-metal hypervisor that runs directly on system
hardware. It is available for `Windows\* server`_ and client operating 
systems, including `Windows 10`_.

|CL| provides a virtual disk image for Hyper-V, which also includes
a :ref:`Hyper-V specific kernel <compatible-kernels>` and drivers.

Prerequisites
*************

* Enable virtualization on the host system from EFI/BIOS, such as:

  * `Intel® Virtualization Technology`_ (Intel® VT)
  * `Intel® Virtualization Technology for Directed I/O`_ (Intel® VT-d)

* Install Hyper-V on the appropriate Windows operating system:

  * `Install the Hyper-V role on Windows Server`_
  * `Install Hyper-V on Windows 10`_

* Configure the appropriate virtual networking in Hyper-V:

  * `Create a virtual network on Windows Server`_
  * `Create a virtual network on Windows 10`_


Download the |CL| disk image for Hyper-V
****************************************

#. Download the :file:`clear-[VERSION]-azure-hyperv.vhd.gz` for Microsoft* 
   Hyper-V from the `downloads`_ website.

#. Verify and extract the image using these instructions:
   :ref:`download-verify-decompress`.

#. Extract the compressed file using software such as the 
   7-Zip\* tool or the WinZip\* tool. 

   After extraction, the file should be named :file:`clear-[VERSION]-azure-hyperv.vhd`.

Create and configure new VM
****************************

#. Open the **Hyper-V Manager** from the Start menu.

   .. figure:: figures/hyper-v/hyper-v-01.png
      :scale: 100%
      :alt: Hyper-V Manager from the Start menu

      Figure 1: Hyper-V Manager from the Start menu

   .. note::

      You may need to manually enable Hyper-V on a Windows\* machine. Review 
      ``Windows Features``.

#. Create a *New Virtual Machine* by clicking the :guilabel:`Action` menu,
   then selecting :guilabel:`New` and :guilabel:`Virtual Machine...`.

   .. figure:: figures/hyper-v/hyper-v-02.png
      :scale: 100%
      :alt: New Virtual Machine in Hyper-V Manager

      Figure 2: New Virtual Machine in Hyper-V Manager

#. Follow the *New Virtual Machine Wizard* to create a new virtual machine
   specifying the options below:

   - **Name**: Choose name (for example, ClearLinuxOS-VM)
   - **Specify Generation**: Generation 1
   - **Startup memory**: 2048 MB or more
   - **Configure Networking**: Change :guilabel:`Connection` to `Default Switch`
   - **Connect Virtual Hard Disk**: Select :guilabel:`Use an existing virtual
     hard disk` and browse to find the 
     :file:`clear-[VERSION]-azure-hyperv.vhd` file.

   After finishing the wizard, the VM will be created but not powered on.

#. Configure the VM by right-clicking it in the Hyper-V Manager and selecting
   :guilabel:`Settings...`. Figure 3 shows the Settings page after configuration selections.

   **Optional**

   - If you wish to `Encrypt state and virtual machine traffic, under 
     :guilabel:`Security`, select :guilabel:`Add Key Storage Drive`.

   - Under :guilabel:`Processor`, consider increasing the number of virtual
     processors assigned to the |CL| VM to improve performance.

   .. figure:: figures/hyper-v/hyper-v-03.png
      :scale: 100%
      :alt: |CL| VM Settings in Hyper-V Manager

      Figure 3: |CL| VM Settings page after configuration

#. Click :guilabel:`Apply` at the bottom of the VM Settings screen.

#. Click :guilabel:`OK` at the bottom of the VM Settings screen.


Start the VM
************

#. Start the |CL| VM by right-clicking the VM in Hyper-V Manager and 
   selecting :guilabel:`Start`.

#. Connect to the VM console by right-clicking the VM in Hyper-V Manager and
   selecting :guilabel:`Connect...`. A new *Virtual Machine Connection* 
   window is displayed.

#. After |CL| is booted, log in to the console with user *root*. You are
   prompted to set a new password immediately.

   .. code-block:: console

      > User: root

|CL-ATTR| on Microsoft Hyper-V\* is ready for use.

Related topics
**************

* :ref:`increase-virtual-disk-size`

*Intel and the Intel logo are trademarks of Intel Corporation or its subsidiaries.*

.. _`Windows\* Server`: https://docs.microsoft.com/en-us/windows-server/virtualization/hyper-v/hyper-v-on-windows-server
.. _`Windows 10`: https://docs.microsoft.com/en-us/virtualization/hyper-v-on-windows/index
.. _`Intel® Virtualization Technology`: http://www.intel.com/content/www/us/en/virtualization/virtualization-technology/intel-virtualization-technology.html
.. _`Intel® Virtualization Technology for Directed I/O`: https://software.intel.com/en-us/articles/intel-virtualization-technology-for-directed-io-vt-d-enhancing-intel-platforms-for-efficient-virtualization-of-io-devices
.. _`Install the Hyper-V role on Windows Server`: https://docs.microsoft.com/en-us/windows-server/virtualization/hyper-v/get-started/install-the-hyper-v-role-on-windows-server
.. _Install Hyper-V on Windows 10: https://docs.microsoft.com/en-us/virtualization/hyper-v-on-windows/quick-start/enable-hyper-v
.. _`Create a virtual network on Windows Server`: https://docs.microsoft.com/en-us/windows-server/virtualization/hyper-v/get-started/create-a-virtual-switch-for-hyper-v-virtual-machines
.. _`Create a virtual network on Windows 10`: https://docs.microsoft.com/en-us/virtualization/hyper-v-on-windows/quick-start/connect-to-network
.. _downloads: https://clearlinux.org/downloads

