.. _vmware-player-preconfigured-cl-image:

Run pre-configured Clear Linux image as a VMware\* Workstation Player guest OS
##############################################################################

`VMware Workstation 14 Player`_ is a type 2 hypervisor which runs on top of 
another operating system such as Windows or Linux. With VMware ESXi, you can 
create, configure, manage, and run |CLOSIA| :abbr:`VMs (Virtual Machine)` on 
your local system. 

This section shows you how to deploy a pre-configured |CL| VMware image on 
VMware Workstation 14 Player using these steps:
  
#.  Install the VMware Workstation Player hypervisor
#.  Download the latest |CL| VMware image
#.  Verify the integrity of the |CL| image
#.  Uncompress the |CL| image
#.  Create and configure a new VM
#.  Attach the pre-configured VMware |CL| image
#.  Enable EFI boot support
#.  Power on the VM

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

Download the latest Clear Linux VMware image
********************************************

Get the latest |CL| VMware image from the `image`_ repository.
Look for :file:`clear-[version number]-vmware.vmdk.xz`.

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

        .. figure:: figures/vmware-player/vmware-player-preconfigured-cl-image-1.png
          :scale: 100%
          :alt: VMware Workstation 14 Player - Create a new virtual machine

          Figure 1: VMware Workstation 14 Player - Create a new virtual machine
   
#.  On the :guilabel:`Welcome to the New Virtual Machine Wizard` step:

    #.  Select the :guilabel:`I will install the operating system later` option.
        See Figure 2.
    #.  Click the :guilabel:`Next` button.

        .. figure:: figures/vmware-player/vmware-player-preconfigured-cl-image-2.png
          :scale: 100%
          :alt: VMware Workstation 14 Player - Select install operating system 

          Figure 2: VMware Workstation 14 Player - Select install operating system 
          later  

#.  On the :guilabel:`Select a Guest Operating System` step:

    #.  Set the :guilabel:`Guest operating system` setting to :guilabel:`Linux`.
        See Figure 3.
    #.  Set :guilabel:`Version` setting to :guilabel:`Other Linux 3.x or later kernel 64-bit`.
    #.  Click the :guilabel:`Next` button.

        .. figure:: figures/vmware-player/vmware-player-preconfigured-cl-image-3.png
          :scale: 100%
          :alt: VMware Workstation 14 Player - Select guest operating system type

          Figure 3: VMware Workstation 14 Player - Select guest operating system type

#.  On the :guilabel:`Name the Virtual Machine` step:

    #.  Give your new VM a name.  See Figure 4.
    #.  Click the :guilabel:`Next` button.

        .. figure:: figures/vmware-player/vmware-player-preconfigured-cl-image-4.png
          :scale: 100%
          :alt: VMware Workstation 14 Player - Name virtual machine

          Figure 4: VMware Workstation 14 Player - Name virtual machine

#.  On the :guilabel:`Specify Disk Capacity` step:

    #.  Click the :guilabel:`Next` button.  The disk settings do not 
        matter because the default virtual disk will be removed when you attach 
        the pre-configured |CL| VMware image at a later step.  See Figure 5.

        .. figure:: figures/vmware-player/vmware-player-preconfigured-cl-image-5.png
          :scale: 100%
          :alt: VMware Workstation 14 Player - Set disk capacity

          Figure 5: VMware Workstation 14 Player - Set disk capacity

#.  On the :guilabel:`Ready to Create Virtual Machine` step:

    #.  Click the :guilabel:`Customize Hardware...` button.  See Figure 6.
    
        .. figure:: figures/vmware-player/vmware-player-preconfigured-cl-image-6.png
          :scale: 100%
          :alt: VMware Workstation 14 Player - Customize hardware

          Figure 6: VMware Workstation 14 Player - Customize hardware

    #.  Under the :guilabel:`Device` list, select :guilabel:`Processors`.  
        See Figure 7.
        Under the :guilabel:`Virtualization engine` section,  
        check :guilabel:`Virtualize Intel VT-x/EPT or AMD-V/RVI`.

        .. figure:: figures/vmware-player/vmware-player-preconfigured-cl-image-7.png
          :scale: 100%
          :alt: VMware Workstation 14 Player - Set virtualization engine option

          Figure 7: VMware Workstation 14 Player - Set virtualization engine option

    #.  Because the virtual CD/DVD (IDE) is not needed, disconnect it:

        #.  Under the :guilabel:`Device` list, select :guilabel:`New CD/DVD (IDE)`.
            See Figure 8.
        #.  Under the :guilabel:`Device status` section, uncheck 
            :guilabel:`Connect at power on`. 

            .. figure:: figures/vmware-player/vmware-player-preconfigured-cl-image-8.png
              :scale: 100%
              :alt: VMware Workstation 14 Player - Disconnect CD/DVD (IDE)

              Figure 8: VMware Workstation 14 Player - Disconnect CD/DVD (IDE)

    #.  Click the :guilabel:`Close` button.
    
#.  Click the :guilabel:`Finish` button.
    
Attach the pre-configured Clear Linux VMware image
**************************************************

#.  Move the downloaded and uncompressed pre-configured |CL| VMware image file 
    :file:`clear-[version number]-basic.vmdk` to the directory where your 
    newly-created VM resides.

    .. note::

      VMware VM files are typically located in:

      * Linux distros: `/home/username/vmware`
      * Windows: `C:/\Users/\username/\Documents/\Virtual Machines`

#.  On the `VMware Workstation Player` home screen:

    #.  Select your newly-created VM.  See Figure 9.
    #.  Click :guilabel:`Edit virtual machine settings`.  

        .. figure:: figures/vmware-player/vmware-player-preconfigured-cl-image-9.png
          :scale: 100%
          :alt: VMware Workstation 14 Player - Edit virtual machine settings

          Figure 9: VMware Workstation 14 Player - Edit virtual machine settings

#.  Remove the default hard disk:

    #.  Under the :guilabel:`Device` list, select :guilabel:`Hard Disk (SCSI)`.
        See Figure 10.
    #.  Click the :guilabel:`Remove` button.

        .. figure:: figures/vmware-player/vmware-player-preconfigured-cl-image-10.png
          :scale: 100%
          :alt: VMware Workstation 14 Player - Remove hard drive

          Figure 10: VMware Workstation 14 Player - Remove hard drive

#.  Add a new hard disk and attach the pre-configured |CL| VMware image:

    #.  Click the :guilabel:`Add...` button.  See Figure 11.
    #.  Under the :guilabel:`Hardware types` section, select :guilabel:`Hard Disk`.
    #.  Click the :guilabel:`Next` button.

        .. figure:: figures/vmware-player/vmware-player-preconfigured-cl-image-11.png
          :scale: 100%
          :alt: VMware Workstation 14 Player - Add new hard drive

          Figure 11: VMware Workstation 14 Player - Add new hard drive

    #.  Select your preferred :guilabel:`Virtual disk type`.  See Figure 12.

        .. figure:: figures/vmware-player/vmware-player-preconfigured-cl-image-12.png
          :scale: 100%
          :alt: VMware Workstation 14 Player - Select virtual disk type

          Figure 12: VMware Workstation 14 Player - Select virtual disk type

    #.  Select the :guilabel:`Use an existing virtual disk` option.  See Figure 13.
 
        .. figure:: figures/vmware-player/vmware-player-preconfigured-cl-image-13.png
          :scale: 100%
          :alt: VMware Workstation 14 Player - Use existing virtual disk

          Figure 13: VMware Workstation 14 Player - Use existing virtual disk
   
    #.  Click the :guilabel:`Browse` button and select the pre-configured |CL| 
        VMware image file.  See Figure 14.

        .. figure:: figures/vmware-player/vmware-player-preconfigured-cl-image-14.png
          :scale: 100%
          :alt: VMware Workstation 14 Player - Select ready-made VMware |CL| 

          Figure 14: VMware Workstation 14 Player - Select ready-made VMware |CL| 
          image file

    #.  Click the :guilabel:`Finish` button.

        .. note::
          
          When asked to convert the existing virtual disk to newer format, 
          selecting either option works. 

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

   * :ref:`vmware-player-install-cl`
   * :ref:`vmware-esxi-install-cl`
   * :ref:`vmware-esxi-preconfigured-cl-image`

.. _VMware ESXi: https://www.vmware.com/products/esxi-and-esx.html
.. _VMware Workstation 14 Player: https://www.vmware.com/products/workstation-player.html
.. _VMware Workstation Player guide: https://docs.vmware.com/en/VMware-Workstation-Player/index.html
.. _latest: https://download.clearlinux.org/image/
.. _image: https://download.clearlinux.org/image
.. _Intel® Virtualization Technology: https://www.intel.com/content/www/us/en/virtualization/virtualization-technology/intel-virtualization-technology.html
.. _Intel® Virtualization Technology for Directed I/O: https://software.intel.com/en-us/articles/intel-virtualization-technology-for-directed-io-vt-d-enhancing-intel-platforms-for-efficient-virtualization-of-io-devices



