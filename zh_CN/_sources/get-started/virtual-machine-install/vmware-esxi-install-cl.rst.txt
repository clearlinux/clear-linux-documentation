.. _vmware-esxi-install-cl:

|CL-ATTR| on VMware\* ESXi
##########################

This page explains how to create a new :abbr:`VM (Virtual Machine)` and
manually install |CL-ATTR| on the new VM with VMware ESXi 6.5.

.. contents::
   :local:
   :depth: 1

Overview
********

`VMware ESXi`_ is a type 1 bare-metal hypervisor that runs directly on top
of server hardware. With VMware ESXi, you can create, configure, manage, and
run |CL| virtual machines in the cloud.

Manually installing |CL| on a new VM gives additional configuration flexibility
during installation. For example: alternate disk sizes, number of partitions,
pre-installed bundles, etc.

If you prefer to use a pre-configured |CL| VMware image instead, refer to
:ref:`vmware-esxi-preconfigured-cl-image`.

.. note::

   VMware also offers a type 2 hypervisor designed for the desktop environment,
   called `VMware Workstation Player`_. Refer to :ref:`vmw-player-preconf` or
   :ref:`vmw-player` for more information.

   Visit :ref:`image-types` to learn more about all available images.

Download the latest |CL| installer ISO
**************************************

Get the latest |CL| installer ISO image from the `image`_ repository.
Look for :file:`clear-[version number]-installer.iso.xz`.

We also provide instructions for downloading and verifying a Clear Linux ISO.
For more information, refer to :ref:`download-verify-decompress`.

Upload the |CL| installer ISO to the VMware server
**************************************************

#.  Connect to the VMware server and log into an account with sufficient 
    permission to create and manage VMs.  
#.  Under the :guilabel:`Navigator` window, select :guilabel:`Storage`. 
    See Figure 1.
#.  Under the :guilabel:`Datastores` tab, click the :guilabel:`Datastore browser` 
    button.   
    
    .. figure:: figures/vmware-esxi/vmware-esxi-install-cl-1.png
      :scale: 100 %
      :alt: VMware ESXi - Navigator > Storage 

      Figure 1: VMware ESXi - Navigator > Storage 

#.  Click the :guilabel:`Create directory` button and name the directory `ISOs`.
    See Figure 2.

    .. figure:: figures/vmware-esxi/vmware-esxi-install-cl-2.png
      :scale: 100 %
      :alt: VMware ESXi - Datastore > Create directory 

      Figure 2: VMware ESXi - Datastore > Create directory 
   
#.  Select the newly-created directory and click the :guilabel:`Upload` button.
    See Figure 3.

    .. figure:: figures/vmware-esxi/vmware-esxi-install-cl-3.png
      :scale: 100 %
      :alt: VMware ESXi - Datastore > Upload ISO 

      Figure 3: VMware ESXi - Datastore > Upload ISO 
   
#.  Select the decompressed |CL| installer ISO file :file:`clear-[version number]-installer.iso` 
    and upload it.

Create and configure a new VM
*****************************

In this section, you will create a new VM, configure its basic parameters such 
as drive size, number of CPUs, memory size, and then attach the |CL| installer ISO. 

#.  Under the :guilabel:`Navigator` window, select :guilabel:`Virtual Machines`.
    See Figure 4.
#.  In the right window, click the :guilabel:`Create / Register VM` button.

    .. figure:: figures/vmware-esxi/vmware-esxi-install-cl-4.png
      :scale: 100 %
      :alt: VMware ESXi - Navigator > Virtual Machines

      Figure 4: VMware ESXi - Navigator > Virtual Machines
   
#.  On the :guilabel:`Select creation type` step:
    
    #.  Select the :guilabel:`Create a new virtual machine` option.
        See Figure 5.
    #.  Click the :guilabel:`Next` button.

        .. figure:: figures/vmware-esxi/vmware-esxi-install-cl-5.png
          :scale: 100 %
          :alt: VMware ESXi - Create a new virtual machine

          Figure 5: VMware ESXi - Create a new virtual machine
   
#.  On the :guilabel:`Select a name and guest OS` step:

    #.  Give the new VM a name in the :guilabel:`Name` field. See Figure 6.
    #.  Set the :guilabel:`Compatability` option to :guilabel:`ESXi 6.5 virtual machine`.
    #.  Set the :guilabel:`Guest OS family` option to :guilabel:`Linux`.
    #.  Set the :guilabel:`Guest OS version` option to :guilabel:`Other 3.x or later Linux (64-bit)`.
    #.  Click the :guilabel:`Next` button.

        .. figure:: figures/vmware-esxi/vmware-esxi-install-cl-6.png
          :scale: 100 %
          :alt: VMware ESXi - Give a name and select guest OS type

          Figure 6: VMware ESXi - Give a name and select guest OS type

#.  On the :guilabel:`Select storage` step:

    #.  Accept the default option.
    #.  Click the :guilabel:`Next` button.

#.  On the :guilabel:`Customize settings` step:
    
    #.  Click the :guilabel:`Virtual Hardware` button. See Figure 7.
    #.  Expand the :guilabel:`CPU` setting and enable :guilabel:`Hardware virtualization` by 
        checking :guilabel:`Expose hardware assisted virtualization to the guest OS`.

        .. figure:: figures/vmware-esxi/vmware-esxi-install-cl-7.png
          :scale: 100 %
          :alt: VMware ESXi - Enable hardware virtualization
      
          Figure 7: VMware ESXi - Enable hardware virtualization

    #.  Set :guilabel:`Memory` size to 2048MB (2GB). See Figure 8.

        .. figure:: figures/vmware-esxi/vmware-esxi-install-cl-8.png
          :scale: 100 %
          :alt: VMware ESXi - Set memory size

          Figure 8: VMware ESXi - Set memory size

        .. note:: 

          The |CL| installer ISO needs a minimum of 2GB of RAM to work properly.
          You can reduce the memory size after the installation completes if you want, 
          because a minimum |CL| installation can function on as little as 128MB of RAM.
          See :ref:`system-requirements` for more details.  

    #.  Set :guilabel:`Hard disk 1` to the desired capacity. See Figure 9.

        .. figure:: figures/vmware-esxi/vmware-esxi-install-cl-9.png
          :scale: 100 %
          :alt: VMware ESXi - Set hard disk size

          Figure 9: VMware ESXi - Set hard disk size

        .. note::

          A minimum |CL| installation can exist on 600MB of drive space.  
          See :ref:`system-requirements` for more details.       

    #.  Attach the |CL| installer ISO.  For the :guilabel:`CD/DVD Drive 1` setting, 
        click the drop-down list to the right of it and select the :guilabel:`Datastore ISO file`
        option.  Then select the |CL| installer ISO :file:`clear-[version number]-installer.iso` 
        that you previously uploaded to the VMware server. See Figure 10.

        .. figure:: figures/vmware-esxi/vmware-esxi-install-cl-10.png
          :scale: 100 %
          :alt: VMware ESXi - Set CD/DVD to boot installer ISO

          Figure 10: VMware ESXi - Set CD/DVD to boot installer ISO

#.  Click the :guilabel:`Next` button.
#.  Click the :guilabel:`Finish` button.

Install |CL| into the new VM
****************************

#.  Power on the VM.
    
    #.  Under the :guilabel:`Navigator` window, select :guilabel:`Virtual Machines`.
        See Figure 11.
    #.  In the right window, select the newly-created VM.
    #.  Click the :guilabel:`Power on` button.  
    #.  Click on the icon representing the VM to bring it into view and maximize
        its window.  

        .. figure:: figures/vmware-esxi/vmware-esxi-install-cl-11.png
          :scale: 100 %
          :alt: VMware ESXi - Navigator > Virtual Machines > Power on VM

          Figure 11: VMware ESXi - Navigator > Virtual Machines > Power on VM

#.  Follow the :ref:`install-on-target-start` guide to complete the installation of 
    |CL|.
#.  After the installation is complete, follow the |CL| instruction to reboot it.  
    This will restart the installer again. 

Reconfigure the VM's settings to boot the newly-installed |CL|
**************************************************************

After |CL| has been installed using the installer ISO, it must be detached so
it will not run again.  Also, in order to boot the newly-installed |CL|, you must
enable UEFI support. 

#.  Power off the VM.

    #.  Click the :guilabel:`Actions` button - located on the top-right corner 
        of the VM's windows - and go to the :guilabel:`Power` setting and  
        select the :guilabel:`Power off` option. See Figure 12. 

        .. figure:: figures/vmware-esxi/vmware-esxi-install-cl-12.png
          :scale: 100 %
          :alt: VMware ESXi - Actions > Power off

          Figure 12: VMware ESXi - Actions > Power off

#.  Edit the VM settings.

    #.  Click the :guilabel:`Actions` button again and select :guilabel:`Edit settings`.  
        See Figure 13.

        .. figure:: figures/vmware-esxi/vmware-esxi-install-cl-13.png
          :scale: 100 %
          :alt: VMware ESXi - Actions > Edit settings

          Figure 13: VMware ESXi - Actions > Edit settings

#.  Disconnect the CD/DVD to stop it from booting the |CL| installer ISO again.
    
    #.  Click the :guilabel:`Virtual Hardware` button.  See Figure 14.
    #.  For the :guilabel:`CD/DVD Drive 1` setting, uncheck the 
        :guilabel:`Connect` checkbox.

        .. figure:: figures/vmware-esxi/vmware-esxi-install-cl-14.png
          :scale: 100 %
          :alt: VMware ESXi - Disconnect the CD/DVD drive

          Figure 14: VMware ESXi - Disconnect the CD/DVD drive

#.  |CL| needs UEFI support in order to boot.  Enable it.

    #.  Click the :guilabel:`VM Options` button. See Figure 15.
    #.  Expand the :guilabel:`Boot Options` setting.
    #.  For the :guilabel:`Firmware` setting, click the drop-down list to the right 
        of it and select the :guilabel:`EFI` option.

        .. figure:: figures/vmware-esxi/vmware-esxi-install-cl-15.png
          :scale: 100 %
          :alt: VMware ESXi - Set boot firmware to EFI

          Figure 15: VMware ESXi - Set boot firmware to EFI

#.  Click the :guilabel:`Save` button.

Power on the VM and boot |CL|
*****************************

After configuring the settings above, power on the VM.  

#.  Under the :guilabel:`Navigator` window, select :guilabel:`Virtual Machines`.
    See Figure 16.
#.  In the right window, select the VM.
#.  Click the :guilabel:`Power on` button.  
#.  Click on the icon representing the VM to bring it into view and maximize
    its window.  

    .. figure:: figures/vmware-esxi/vmware-esxi-install-cl-16.png
      :scale: 100 %
      :alt: VMware ESXi - Navigator > Virtual Machines > Power on VM

      Figure 16: VMware ESXi - Navigator > Virtual Machines > Power on VM

Related topics
**************

* :ref:`vmware-esxi-preconfigured-cl-image`


.. _VMware ESXi: https://www.vmware.com/products/esxi-and-esx.html
.. _VMware Workstation Player: https://www.vmware.com/products/workstation-player.html
.. _image: https://cdn.download.clearlinux.org/image
