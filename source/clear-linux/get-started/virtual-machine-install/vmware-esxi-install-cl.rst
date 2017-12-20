.. _vmware-esxi-install-cl:

Install Clear Linux as a VMware\* ESXi guest OS
###############################################

`VMware ESXi`_ is a type 1 bare-metal hypervisor which runs directly on top of 
server hardware.  With VMware ESXi, you can create, configure, manage, and run 
|CLOSIA| virtual machines in the cloud.  

This section shows you how to create a new VM and install |CL| into it with 
VMware ESXi 6.5 Update 1.  Some of the advantages of installing |CL| into a new 
VM is that it provides you flexibility in configuring, for example: its size, the 
nummber of partitions, the initial of bundles, etc. We will perform these steps: 

#. :ref:`label-vmware-esxi-download-installer-iso`
#. :ref:`label-vmware-esxi-verify-image-checksum`
#. :ref:`label-vmware-esxi-uncompress-image`
#. :ref:`label-vmware-esxi-upload-installer-iso-to-server`
#. :ref:`label-vmware-esxi-create-and-configure-new-vm`
#. :ref:`label-vmware-esxi-install-clear-linux-into-new-vm`
#. :ref:`label-vmware-esxi-reconfigure-vm-settings-to-boot-clear`
#. :ref:`label-vmware-esxi-power-on-vm-method-1`

If you would prefer to use a pre-configured VMware ESXi |CL| image instead, 
see :ref:`vmware-esxi-preconfigured-cl-image`. 

.. note::

  VMware also offers a type 2 hypervisor called `VMware Workstation Player`_ 
  which is designed for the Desktop environment.  For information on how to 
  install |CL| as guest OS on it, see :ref:`vmware-player-install-cl`.

Method 1: Install Clear Linux into a new :abbr:`VM (Virtual Machine)` 
*********************************************************************

The general process for performing a fresh install of |CL| into a new VM is 
as follows (with expanded details below):


.. include:: ../../guides/maintenance/download-image.rst
   :Start-after: types-of-cl-images:
   :end-before: verify-image-checksum

.. _label-vmware-esxi-download-installer-iso:

Download the latest Clear Linux installer ISO
=============================================

Get the latest |CL| installer ISO image from the `image`_ directory.
Look for **clear-<version number>-installer.iso.xz**.

.. _label-vmware-esxi-verify-image-checksum:

.. include:: ../../guides/maintenance/download-image.rst
   :Start-after: verify-image-checksum:
   :end-before: verify-image-checksum-on-macos

For alternative instructions on other operating systems, see :ref:`verify-image-checksum`.

.. _label-vmware-esxi-uncompress-image:

.. include:: ../../guides/maintenance/download-image.rst
   :Start-after: uncompress-image:
   :end-before: uncompress-gz-on-linux

For alternative instructions on other operating systems, see :ref:`uncompress-image`.

.. _label-vmware-esxi-upload-installer-iso-to-server:

Upload the Clear Linux installer ISO to the VMware server
=========================================================

#.  Connect to the VMware server and log into an account with root privilege.
#.  Under the :guilabel:`Navigator` window, select :guilabel:`Storage`.
#.  Under the :guilabel:`Datastores` tab, click the :guilabel:`Datastore browser` 
    button.
    
    .. figure:: figures/vmware-esxi/vmware-esxi-1.png
      :scale: 100 %
      :alt: VMware ESXi - Navigator > Storage 

    Figure 1: VMware ESXi - Navigator > Storage 

#.  Click the :guilabel:`Create directory` button and name the directory as *ISOs*.

    .. figure:: figures/vmware-esxi/vmware-esxi-2.png
      :scale: 100 %
      :alt: VMware ESXi - Datastore > Create directory 

    Figure 2: VMware ESXi - Datastore > Create directory 
   
#.  Select the newly-created directory and click the :guilabel:`Upload` button.

    .. figure:: figures/vmware-esxi/vmware-esxi-3.png
      :scale: 100 %
      :alt: VMware ESXi - Datastore > Upload ISO 

    Figure 3: VMware ESXi - Datastore > Upload ISO 
   
#.  Select the uncompressed |CL| installer ISO file :file:`clear-<version number>-installer.iso` 
    and upload it.

.. _label-vmware-esxi-create-and-configure-new-vm:

Create and configure a new VM
=============================

In this section, you will create a new VM, configure its basic parameters such 
drive size, number of CPUs, memory size, and attach the |CL| installer ISO. 

#.  Under the :guilabel:`Navigator` window, select :guilabel:`Virtual Machines`.
#.  On the right window, click the :guilabel:`Create / Register VM` button.

    .. figure:: figures/vmware-esxi/vmware-esxi-4.png
      :scale: 100 %
      :alt: VMware ESXi - Navigator > Virtual Machines

    Figure 4: VMware ESXi - Navigator > Virtual Machines
   
#.  On the :guilabel:`Select creation type` step:
    
    #.  Select the :guilabel:`Create a new virtual machine` option.  
    #.  Click the :guilabel:`Next` button.

        .. figure:: figures/vmware-esxi/vmware-esxi-5.png
          :scale: 100 %
          :alt: VMware ESXi - Create a new virtual machine

        Figure 5: VMware ESXi - Create a new virtual machine
   
#.  On the :guilabel:`Select a name and guest OS` step:

    #.  Give the new VM a name in the :guilabel:`Name` field.  
    #.  Set the :guilabel:`Compatability` option to :guilabel:`ESXi 6.5 virtual machine`.
    #.  Set the :guilabel:`Guest OS family` option to :guilabel:`Linux`.
    #.  Set the :guilabel:`Guest OS version` option to :guilabel:`Other 3.x or later Linux (64-bit)`.
    #.  Click the :guilabel:`Next` button.

        .. figure:: figures/vmware-esxi/vmware-esxi-6.png
          :scale: 100 %
          :alt: VMware ESXi - Give a name and select guest OS type

        Figure 6: VMware ESXi - Give a name and select guest OS type

#.  On the :guilabel:`Select storage` step:

    #.  Accept the default option.
    #.  Click the :guilabel:`Next` button.

#.  On the :guilabel:`Customize settings` step:
    
    #.  Click the :guilabel:`Virtual Hardware` button.
    #.  Expand the :guilabel:`CPU` setting and enable :guilabel:`Hardware virtualization` by 
        checking :guilabel:`Expose hardware assisted virtualization to the guest OS`.

        .. figure:: figures/vmware-esxi/vmware-esxi-7.png
          :scale: 100 %
          :alt: VMware ESXi - Enable hardware virtualization
      
        Figure 7: VMware ESXi - Enable hardware virtualization

    #.  Set :guilabel:`Memory` size to 2048MB (2GB).

        .. figure:: figures/vmware-esxi/vmware-esxi-8.png
          :scale: 100 %
          :alt: VMware ESXi - Set memory size

        Figure 8: VMware ESXi - Set memory size

        .. note:: 

          The |CL| installer ISO needs a minimum of 2GB of RAM to work properly.
          After the installation is complete, the memory size can be reduced, if 
          desired, because a minimum |CL| installation can function on as little as 
          128MB of RAM. See :ref:`system-requirements` for more details.  

    #.  Set :guilabel:`Hard disk 1` to the desired capacity.

        .. figure:: figures/vmware-esxi/vmware-esxi-9.png
          :scale: 100 %
          :alt: VMware ESXi - Set hard disk size

        Figure 9: VMware ESXi - Set hard disk size

        .. note::

          A minimum |CL| installation can exist on 600MB of drive space.  
          See :ref:`system-requirements` for more details.       

    #.  Attach the |CL| installer ISO.  For the :guilabel:`CD/DVD Drive 1` setting, 
        click the drop-down list to the right of it and select the :guilabel:`Datastore ISO file`
        option.  Then select the |CL| installer ISO :file:`clear-<version number>-installer.iso` 
        that was previously uploaded to the VMware server.

        .. figure:: figures/vmware-esxi/vmware-esxi-10.png
          :scale: 100 %
          :alt: VMware ESXi - Set CD/DVD to boot installer ISO

        Figure 10: VMware ESXi - Set CD/DVD to boot installer ISO

#.  Click the :guilabel:`Next` button.
#.  Click the :guilabel:`Finish` button.

.. _label-vmware-esxi-install-clear-linux-into-new-vm:

Install Clear Linux into the new VM
===================================

#.  Power on the VM.
    
    #.  Under the :guilabel:`Navigator` window, select :guilabel:`Virtual Machines`.
    #.  On the right window, select the newly-created VM.
    #.  Click the :guilabel:`Power on` button.  
    #.  Click on the icon representing the VM to bring it into view and maximize
        its window.  

       .. figure:: figures/vmware-esxi/vmware-esxi-11.png
         :scale: 100 %
         :alt: VMware ESXi - Navigator > Virtual Machines > Power on VM

       Figure 11: VMware ESXi - Navigator > Virtual Machines > Power on VM

#.  Follow the :ref:`install-on-target` guide to complete the installation of 
    |CL|.
#.  After the installation is complete, follow the |CL| instruction to reboot it.  
    This will restart the installer again. 

.. _label-vmware-esxi-reconfigure-vm-settings-to-boot-clear:

Reconfigure the VM's settings to boot the newly-installed Clear Linux
=====================================================================

After |CL| has been installed using the installer ISO, it must be dettached so
it won't run again.  Also, in order to boot the newly-installed |CL|, you must
enable UEFI support. 

#.  Power off the VM.

    #.  Click the :guilabel:`Actions` button - located on the top-right corner 
        of the VM's windows - and go to the :guilabel:`Power` setting and  
        select the :guilabel:`Power off` option.  

        .. figure:: figures/vmware-esxi/vmware-esxi-12.png
          :scale: 100 %
          :alt: VMware ESXi - Actions > Power off

        Figure 12: VMware ESXi - Actions > Power off

#.  Edit the VM settings.

    #.  Click the :guilabel:`Actions` button again and select :guilabel:`Edit settings`.  

        .. figure:: figures/vmware-esxi/vmware-esxi-13.png
          :scale: 100 %
          :alt: VMware ESXi - Actions > Edit settings

        Figure 13: VMware ESXi - Actions > Edit settings

#.  Disconnect the CD/DVD to stop it from booting the |CL| installer ISO again.
    
    #.  Click the :guilabel:`Virtual Hardware` button.
    #.  For the :guilabel:`CD/DVD Drive 1` setting, uncheck the 
        :guilabel:`Connect` checkbox.

        .. figure:: figures/vmware-esxi/vmware-esxi-14.png
          :scale: 100 %
          :alt: VMware ESXi - Disconnect the CD/DVD drive

        Figure 14: VMware ESXi - Disconnect the CD/DVD drive

#.  |CL| needs UEFI support in order to boot.  Enable it.

    #.  Click the :guilabel:`VM Options` button.
    #.  Expand the :guilabel:`Boot Options` setting.
    #.  For the :guilabel:`Firmware` setting, click the drop-down list to the right 
        of it and select the :guilabel:`EFI` option.

        .. figure:: figures/vmware-esxi/vmware-esxi-15.png
          :scale: 100 %
          :alt: VMware ESXi - Set boot firmware to EFI

        Figure 15: VMware ESXi - Set boot firmware to EFI

#.  Click the :guilabel:`Save` button.

.. _label-vmware-esxi-power-on-vm-method-1:

Power on the virtual machine
============================

After configuring the settings above, power on the virtual machine.  

Also see:
*********

* :ref:`vmware-player`

.. _VMware ESXi: https://www.vmware.com/products/esxi-and-esx.html
.. _VMware Workstation Player: https://www.vmware.com/products/workstation-player.html
.. _image: https://download.clearlinux.org/image