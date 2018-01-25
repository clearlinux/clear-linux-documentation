.. _vmware-player-install-cl:

Install Clear Linux as a VMware\* Workstation Player guest OS
#############################################################

`VMware Workstation 14 Player`_ is a type 2 hypervisor which runs on top of 
another operating system such as Windows or Linux. With VMware ESXi, you can 
create, configure, manage, and run |CLOSIA| :abbr:`VMs (Virtual Machine)` on 
your local system. 

This section shows you how to create a new VM and install |CL| into it with 
the VMware Workstation 14 Player hypervisor.  Some of the advantages of 
installing |CL| into a new VM is that it provides you flexibility in configuring, 
for example: its size, the number of partitions, bundles, etc. 
We will perform these steps: 

#.  Install the VMware Workstation Player hypervisor
#.  Download the latest |CL| installer ISO
#.  Verify the integrity of the |CL| image
#.  Uncompress the |CL| image
#.  Create and configure a new VM
#.  Attach the |CL| installer ISO to the VM
#.  Install Clear Linux into the new VM
#.  Detach the |CL| installer ISO from the VM
#.  Power off the VM
#.  Enable EFI boot support
#.  Power on the VM

If you would prefer to use a pre-configured |CL| VMware image instead, 
see :ref:`vmware-player-preconfigured-cl-image`. 

.. note::

  VMware also offers a type 1 hypervisor called `VMware ESXi`_ 
  which is designed for the cloud environment.  For information on how to 
  install |CL| as guest OS on it, see :ref:`vmware-esxi-install-cl`.

.. note::

  The figures shown throughout this document are from the Windows\* version of 
  VMware Workstation 14 Player.  The menus and prompts in these figures are 
  similar as those for the Linux version with some minor wording differences.

Install the VMware Workstation Player hypervisor
************************************************

#.  Enable `Intel® Virtualization Technology`_ (Intel® VT) and 
    `Intel® Virtualization Technology for Directed I/O`_ (Intel® VT-d) in your
    system's BIOS.
#.  `VMware Workstation 14 Player`_ is available for Windows and Linux.  Download 
    your preferred version.
#.  Depending on which OS you're running, install it by following one of these
    instructions:

    * For Linux distros supported by VMware: 

      #.  Enable a GUI desktop.  
      #.  Start a terminal emulator.
      #.  Start the installer by issuing the command below and follow the 
          guided steps.

          .. code-block:: console

            $ sudo sh ./VMware-Player-[version number].x86_64.bundle

    * For Windows:

      #.  Start the installer and follow the Setup Wizard.

For additional help, see the `VMware Workstation Player guide`_.

Clear Linux image types
***********************

.. include:: ../../guides/maintenance/image-types.rst
   :Start-after: image-types-content:


Download the latest Clear Linux installer ISO
*********************************************

Get the latest |CL| installer ISO image from the `image`_ repository.
Look for :file:`clear-[version number]-installer.iso.xz`.

.. include:: ../../guides/maintenance/download-verify-uncompress-windows.rst
   :Start-after: verify-windows:

We also provide instructions for other operating systems: 

* :ref:`download-verify-uncompress-linux`
* :ref:`download-verify-uncompress-mac`

Create and configure a new VM 
*****************************

#.  Start the `VMware Workstation Player` app.
#.  On the home screen:

    #.  Click :guilabel:`Create a New Virtual Machine`.  See Figure 1.  

        .. figure:: figures/vmware-player/vmware-player-install-cl-1.png
          :scale: 100%
          :alt: VMware Workstation 14 Player - Create a new virtual machine

          Figure 1: VMware Workstation 14 Player - Create a new virtual machine
   
#.  On the :guilabel:`Welcome to the New Virtual Machine Wizard` step:

    #.  Select the :guilabel:`Installer disc image file (iso)` option.
        See Figure 2. 
    #.  Click the :guilabel:`Browse` button and select the uncompressed |CL| 
        installer ISO. 
    #.  Click the :guilabel:`Next` button.

        .. figure:: figures/vmware-player/vmware-player-install-cl-2.png
          :scale: 100%
          :alt: VMware Workstation 14 Player - Select |CL| installer ISO 

          Figure 2: VMware Workstation 14 Player - Select |CL| installer ISO   

#.  On the :guilabel:`Select a Guest Operating System` step:

    #.  Set the :guilabel:`Guest operating system` setting to :guilabel:`Linux`.
        See Figure 3.
    #.  Set the :guilabel:`Version` setting to :guilabel:`Other Linux 3.x or later kernel 64-bit`.
    #.  Click the :guilabel:`Next` button.

        .. figure:: figures/vmware-player/vmware-player-install-cl-3.png
          :scale: 100%
          :alt: VMware Workstation 14 Player - Select guest operating system type
        
          Figure 3: VMware Workstation 14 Player - Select guest operating system type

#.  On the :guilabel:`Name the Virtual Machine` step:

    #.  Give your new VM a name.  See Figure 4.
    #.  Click the :guilabel:`Next` button.

        .. figure:: figures/vmware-player/vmware-player-install-cl-4.png
          :scale: 100%
          :alt: VMware Workstation 14 Player - Name virtual machine

          Figure 4: VMware Workstation 14 Player - Name virtual machine

#.  On the :guilabel:`Specify Disk Capacity` screen:

    #.  Set the desired maximum disk size for your VM.  See Figure 5.

    #.  Click the :guilabel:`Next` button.

        .. figure:: figures/vmware-player/vmware-player-install-cl-5.png
          :scale: 100%
          :alt: VMware Workstation 14 Player - Set disk capacity

          Figure 5: VMware Workstation 14 Player - Set disk capacity

        .. note::

          A minimum |CL| installation can exist on 600MB of drive space.  
          See :ref:`system-requirements` for more details.   

#.  On the :guilabel:`Ready to Create Virtual Machine` step:

    #.  Click the :guilabel:`Customize Hardware...` button.  See Figure 6.
    
        .. figure:: figures/vmware-player/vmware-player-install-cl-6.png
          :scale: 100%
          :alt: VMware Workstation 14 Player - Customize hardware

        Figure 6: VMware Workstation 14 Player - Customize hardware

    #.  Select :guilabel:`Memory` and set the size to 2GB.  See Figure 7.

        .. figure:: figures/vmware-player/vmware-player-install-cl-7.png
          :scale: 100%
          :alt: VMware Workstation 14 Player - Set memory size

          Figure 7: VMware Workstation 14 Player - Set memory size

        .. note:: 

          The |CL| installer ISO needs a minimum of 2GB of RAM to work properly.
          After the installation is complete, |CL| can function on as little as 
          128MB of RAM. Thus, you can reduce the memory size if needed.  
          See :ref:`system-requirements` for more details.  

    #.  Under the :guilabel:`Device` list, select :guilabel:`Processors`. 
        See Figure 8.
        Under the :guilabel:`Virtualization engine` section,  
        check :guilabel:`Virtualize Intel VT-x/EPT or AMD-V/RVI`.

        .. figure:: figures/vmware-player/vmware-player-install-cl-8.png
          :scale: 100%
          :alt: VMware Workstation 14 Player - Set virtualization engine option

          Figure 8: VMware Workstation 14 Player - Set virtualization engine option

    #.  Click the :guilabel:`Close` button.

#.  Click the :guilabel:`Finish` button.

Install Clear Linux into the new VM
***********************************

#.  Select your newly-created VM and click the :guilabel:`Play virtual machine`
    button.  See Figure 9.

    .. figure:: figures/vmware-player/vmware-player-install-cl-9.png
      :scale: 100%
      :alt: VMware Workstation 14 Player - Power on virtual machine

      Figure 9: VMware Workstation 14 Player - Power on virtual machine

#.  Follow the :ref:`install-on-target` guide to complete the installation of 
    |CL|.

#.  After the installation is complete, follow the |CL| instruction to reboot the VM.  
    This will restart the |CL| installer again.    

Detach the |CL| installer ISO from the VM 
*****************************************

#.  Enable the mouse pointer so you access VMware Workstation Player's menus.

    #.  On your keyboard, press :kbd:`<CTRL>` + :kbd:`<ALT>`.

#.  Disconnect the CD/DVD to stop it from booting the |CL| installer ISO again.
    See Figure 10.
    
    #.  Click the :guilabel:`Player` menu.
    #.  Go to :guilabel:`Removable Devices` > :guilabel:`CD/DVD (IDE)` > 
        :guilabel:`Settings`.

        .. figure:: figures/vmware-player/vmware-player-install-cl-10.png
          :scale: 100%
          :alt: VMware Workstation 14 Player - Edit CD/DVD settings

          Figure 10: VMware Workstation 14 Player - Edit CD/DVD settings

    #.  Under the :guilabel:`Device status` section, uncheck the :guilabel:`Connected` 
        and the :guilabel:`Connect at power on` settings.  See Figure 11.
    
    #.  Click the :guilabel:`OK` button.

        .. figure:: figures/vmware-player/vmware-player-install-cl-11.png
          :scale: 100%
          :alt: VMware Workstation 14 Player - Disconnect CD/DVD

          Figure 11: VMware Workstation 14 Player - Disconnect CD/DVD

#.  Power off the VM.

    #.  Click the :guilabel:`Player` menu.  See Figure 12.
    #.  Go to :guilabel:`Power` and select :guilabel:`Shut Down Guest`.

        .. figure:: figures/vmware-player/vmware-player-install-cl-12.png
          :scale: 100%
          :alt: VMware Workstation 14 Player - Power off virtual machine

          Figure 12: VMware Workstation 14 Player - Power off virtual machine

Enable UEFI boot support
************************

|CL| needs UEFI support in order to boot. You can enable it by appending the 
following to the end of your VM's :file:`.vmx` file:

  .. code-block:: console

    firmware = "efi"

VMware VM files are typically located in:

  * Linux distros: `/home/username/vmware`
  * Windows: `C:/\Users/\username/\Documents/\Virtual Machines` (The file type 
    is `VMware virtual machine configuration`.)

Power on the VM
***************

After configuring the settings above, power on your |CL| virtual machine.  

Also see:

   * :ref:`vmware-player-preconfigured-cl-image`
   * :ref:`vmware-esxi-install-cl`
   * :ref:`vmware-esxi-preconfigured-cl-image`

.. _VMware ESXi: https://www.vmware.com/products/esxi-and-esx.html
.. _VMware Workstation 14 Player: https://www.vmware.com/products/workstation-player.html
.. _VMware Workstation Player guide: https://docs.vmware.com/en/VMware-Workstation-Player/index.html
.. _latest: https://download.clearlinux.org/image/
.. _image: https://download.clearlinux.org/image
.. _Intel® Virtualization Technology: https://www.intel.com/content/www/us/en/virtualization/virtualization-technology/intel-virtualization-technology.html
.. _Intel® Virtualization Technology for Directed I/O: https://software.intel.com/en-us/articles/intel-virtualization-technology-for-directed-io-vt-d-enhancing-intel-platforms-for-efficient-virtualization-of-io-devices


