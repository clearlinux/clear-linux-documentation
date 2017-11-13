.. _vmware-player:

Run Clear Linux as a VMware\* Workstation Player guest OS
#########################################################

`VMware Workstation 14 Player`_ is a type 2 hypervisor which runs on top of another
operating system such as Windows or Linux.  Creation, configuration, management, and execution of virtual
machines are done on the local system.  For the cloud version of VMware, see 
:ref:`vmware-esxi`.

This section explains how to run |CLOSIA| as a virtual machine using the 
VMware Workstation 14 Player hypervisor.

There are 2 ways to create a |CL| :abbr:`VM (Virtual Machine)` to run in VMware:

* `Method #1`: Install |CL| into a new VM.  This provides flexibility 
  in configuring the VM size, partitions, initial |CL| bundles selection, etc.
* `Method #2`: Use a ready-made VMware |CL| image.  

Both are discussed below.  

.. note::

  The figures shown throughout this document are from the Windows\* version of 
  VMware Workstation 14 Player.  The menus and prompts in these figures are 
  similar as those for the Linux version with some minor wording differences.

Install the VMware Workstation Player hypervisor
================================================

#. Enable the `Intel® Virtualization Technology`_ (Intel® VT) and the
   `Intel® Virtualization Technology for Directed I/O`_ (Intel® VT-d) in the
   host machine’s BIOS.
#.  `VMware Workstation 14 Player`_ is available for Windows and Linux.  Download 
    the preferred version of choice.
#.  Install it.

    * For Linux distros supported by VMware: 

      #.  Enable a GUI desktop.  
      #.  Start a terminal emulator.
      #.  Start the installer and follow the guided steps.

        .. code-block:: console

          $ sudo sh ./VMware-Player-<version>.x86_64.bundle

    * For Windows:

      #.  Start the installer and follow the Setup Wizard.

For additional help, see the `VMware Workstation Player guide`_.

Download the latest Clear Linux image
=====================================

Go to the |CL| `image`_ repository and download the desired type:

* ISO installer image: `clear-<version>-installer.iso.xz` (for Method 1)
* VMware image: `clear-<version>-basic.vmdk.xz` (for Method 2)

For older versions, see the `releases`_ page.

Although not required, it is recommended to download the corresponding 
checksum file (designated with `-SHA512SUMS` at the end of the filename) 
for the image in order to verify its integrity.

Verify the integrity of the download (recommended)
==================================================

* For Linux distros:

  #.  Start a terminal emulator.
  #.  Go to the directory with the downloaded files.
  #.  To verify the integrity of the image, enter (an installer ISO
      image is used as an example):

      .. code-block:: console

        $ sha512sum ./clear-<version>-installer.iso.xz | diff ./clear-<version>-installer.iso.xz-SHA512SUMS -

      If the checksum of the downloaded image is different than the original
      checksum, the differences will displayed. An empty output indicates a match.

* For Windows:

  #.  Start Command-Prompt.
  #.  Go to the directory with the downloaded files.
  #.  To verify the integrity of the image, enter:

      .. code-block:: console

        C:\> CertUtil -hashfile ./clear-<version>-installer.iso.xz sha512

      Manually compare the output with the original checksum value shown in 
      the downloaded checksum file (i.e. `clear-<version>-installer.iso.xz-SHA512SUMS`) 
      to make sure they match.

Uncompress the image
====================

* For Linux distros (an installer ISO image is used as an example):

  .. code-block:: console

    $ unxz clear-<version>-installer.iso.xz

* For Windows:

  Use `7zip`_ to uncompress it.

Method 1: Install Clear Linux into a new VM 
===========================================

The general process for performing a fresh installation of |CL| into a new VM 
is as follows (with expanded details below):

* Create a new VM and configure its settings
* Attach the installer ISO to it
* Install |CL|
* Detach the installer ISO
* Power off the VM
* Enable EFI boot support
* Power on the VM

Create and configure a new VM 
*****************************

#.  Start the `VMware Workstation Player` app.
#.  On the home screen:

    * Click :guilabel:`Create a New Virtual Machine`.

      .. figure:: figures/vmware-player/vmware-player-1.png
        :scale: 100%
        :alt: VMware Workstation 14 Player - Create a new virtual machine

      Figure 1: VMware Workstation 14 Player - Create a new virtual machine
   
#.  :guilabel:`Welcome to the New Virtual Machine Wizard`:

    * Select :guilabel:`Installer disc image file (iso)`.
    * Click :guilabel:`Browse` and select the uncompressed |CL| installer ISO. 
    * Click :guilabel:`Next`.

      .. figure:: figures/vmware-player/vmware-player-2.png
        :scale: 100%
        :alt: VMware Workstation 14 Player - Select |CL| installer ISO 

      Figure 2: VMware Workstation 14 Player - Select |CL| installer ISO   

#.  :guilabel:`Select a Guest Operating System`:

    * Set :guilabel:`Guest operating system` to :guilabel:`Linux`.
    * Set :guilabel:`Version` to :guilabel:`Other Linux 3.x or later kernel 64-bit`.
    * Click :guilabel:`Next`.

      .. figure:: figures/vmware-player/vmware-player-3.png
        :scale: 100%
        :alt: VMware Workstation 14 Player - Select guest operating system type
      
      Figure 3: VMware Workstation 14 Player - Select guest operating system type

#.  :guilabel:`Name the Virtual Machine`:

    * Give it a name.
    * Click :guilabel:`Next`.

      .. figure:: figures/vmware-player/vmware-player-4.png
        :scale: 100%
        :alt: VMware Workstation 14 Player - Name virtual machine

      Figure 4: VMware Workstation 14 Player - Name virtual machine

#.  :guilabel:`Specify Disk Capacity`:

    * Set the desired maximum disk size.  

    * Click :guilabel:`Next`.

      .. figure:: figures/vmware-player/vmware-player-5.png
        :scale: 100%
        :alt: VMware Workstation 14 Player - Set disk capacity

      Figure 5: VMware Workstation 14 Player - Set disk capacity

      .. note::

        A minimum |CL| installation can exist on 600MB of drive space.  
        See :ref:`system-requirements` for more details.   

#.  :guilabel:`Ready to Create Virtual Machine`:

    * Click :guilabel:`Customize Hardware...`
    
      .. figure:: figures/vmware-player/vmware-player-6.png
        :scale: 100%
        :alt: VMware Workstation 14 Player - Customize hardware

      Figure 6: VMware Workstation 14 Player - Customize hardware

    * Select :guilabel:`Memory` and set the size to 2GB.  

      .. figure:: figures/vmware-player/vmware-player-7.png
        :scale: 100%
        :alt: VMware Workstation 14 Player - Set memory size

      Figure 7: VMware Workstation 14 Player - Set memory size

      .. note:: 

        The |CL| installer ISO needs a minimum of 2GB of RAM to work properly.
        After the installation is complete, the memory size can be reduced, if 
        desired.  A minimum |CL| installation can function on as little as 
        128MB of RAM. See :ref:`system-requirements` for more details.  

    * Select :guilabel:`Processors` > :guilabel:`Virtualization engine`, and 
      check :guilabel:`Virtualize Intel VT-x/EPT or AMD-V/RVI`.

      .. figure:: figures/vmware-player/vmware-player-8.png
        :scale: 100%
        :alt: VMware Workstation 14 Player - Set virtualization engine option

      Figure 8: VMware Workstation 14 Player - Set virtualization engine option

    * Click :guilabel:`Close`.

    * Click :guilabel:`Finish`.

Install Clear Linux into the new VM
***********************************

#.  Select the newly created VM and click :guilabel:`Play virtual machine`.  

    .. figure:: figures/vmware-player/vmware-player-9.png
      :scale: 100%
      :alt: VMware Workstation 14 Player - Power on virtual machine

    Figure 9: VMware Workstation 14 Player - Power on virtual machine

#.  Follow the :ref:`install-on-target` guide to complete the installation of 
    |CL|.

#.  After the installation is complete, follow the |CL| instruction to reboot the VM.  
    This will restart the installer again.    

Reconfigure the VM settings to boot the newly installed Clear Linux
*******************************************************************

#.  Enable the mouse pointer.

    * Press :kbd:`<CTRL>` + :kbd:`<ALT>`.

#.  Disconnect the CD/DVD to stop it from booting the installer ISO again.
    
    * Click :guilabel:`Player`.
    * Go to :guilabel:`Removable Devices` > :guilabel:`CD/DVD (IDE)` > 
      :guilabel:`Settings`.

      .. figure:: figures/vmware-player/vmware-player-10.png
        :scale: 100%
        :alt: VMware Workstation 14 Player - Edit CD/DVD settings

      Figure 10: VMware Workstation 14 Player - Edit CD/DVD settings

    * Under :guilabel:`Device status`, uncheck :guilabel:`Connected` and 
      :guilabel:`Connect at power on`.
    * Click `OK`.

      .. figure:: figures/vmware-player/vmware-player-11.png
        :scale: 100%
        :alt: VMware Workstation 14 Player - Disconnect CD/DVD

      Figure 11: VMware Workstation 14 Player - Disconnect CD/DVD

#.  Power off the VM.

    * Click :guilabel:`Player`.
    * Go to :guilabel:`Power` and select :guilabel:`Shut Down Guest`.

      .. figure:: figures/vmware-player/vmware-player-12.png
        :scale: 100%
        :alt: VMware Workstation 14 Player - Power off virtual machine

      Figure 12: VMware Workstation 14 Player - Power off virtual machine

Enable UEFI boot support
************************

|CL| needs UEFI support in order to boot.  Enable it by appending to the end 
of the VM's :file:`.vmx` file:

  .. code-block:: console

    firmware = "efi"

.. note::

  VMware VM files are typically located in:

  * Linux distros: `/home/username/vmware`
  * Windows: `C:/\Users/\username/\Documents/\Virtual Machines` (The file type 
    is `VMware virtual machine configuration`.)

Power on the virtual machine
****************************

After configuring the settings above, power on the virtual machine.  

Method 2: Use a ready-made VMware Clear Linux image
===================================================

The general process for booting a ready-made VMware |CL| image is as follows 
(with expanded details below):

* Create a new VM and configure its base settings
* Attach the ready-made VMware |CL| image
* Enable EFI boot support
* Power on the VM

Create a new VM and configure its base settings
***********************************************

#.  Start the `VMware Workstation Player` app.
#.  On the home screen:

    * Click :guilabel:`Create a New Virtual Machine`.

      .. figure:: figures/vmware-player/vmware-player-1.png
        :scale: 100%
        :alt: VMware Workstation 14 Player - Create a new virtual machine

      Figure 13: VMware Workstation 14 Player - Create a new virtual machine
   
#.  :guilabel:`Welcome to the New Virtual Machine Wizard`:

    * Select :guilabel:`I will install the operating system later`.
    * Click :guilabel:`Next`.

      .. figure:: figures/vmware-player/vmware-player-14.png
        :scale: 100%
        :alt: VMware Workstation 14 Player - Select install operating system 

      Figure 14: VMware Workstation 14 Player - Select install operating system 
      later  

#.  :guilabel:`Select a Guest Operating System`:

    * Set :guilabel:`Guest operating system` to :guilabel:`Linux`.
    * Set :guilabel:`Version` to :guilabel:`Other Linux 3.x or later kernel 64-bit`.
    * Click :guilabel:`Next`.

      .. figure:: figures/vmware-player/vmware-player-3.png
        :scale: 100%
        :alt: VMware Workstation 14 Player - Select guest operating system type

      Figure 15: VMware Workstation 14 Player - Select guest operating system type

#.  :guilabel:`Name the Virtual Machine`:

    * Give it a name.
    * Click :guilabel:`Next`.

      .. figure:: figures/vmware-player/vmware-player-4.png
        :scale: 100%
        :alt: VMware Workstation 14 Player - Name virtual machine

      Figure 16: VMware Workstation 14 Player - Name virtual machine

#.  :guilabel:`Specify Disk Capacity`:

    * Click :guilabel:`Next`.  The default disk size does not matter because it 
      will be removed when the ready-made VMware |CL| image is attached later.

      .. figure:: figures/vmware-player/vmware-player-17.png
        :scale: 100%
        :alt: VMware Workstation 14 Player - Set disk capacity

      Figure 17: VMware Workstation 14 Player - Set disk capacity

#.  :guilabel:`Ready to Create Virtual Machine`:

    * Click :guilabel:`Customize Hardware...`
    
      .. figure:: figures/vmware-player/vmware-player-6.png
        :scale: 100%
        :alt: VMware Workstation 14 Player - Customize hardware

      Figure 18: VMware Workstation 14 Player - Customize hardware

    * Select :guilabel:`Processors` > :guilabel:`Virtualization engine`, and 
      check :guilabel:`Virtualize Intel VT-x/EPT or AMD-V/RVI`.

      .. figure:: figures/vmware-player/vmware-player-8.png
        :scale: 100%
        :alt: VMware Workstation 14 Player - Set virtualization engine option

      Figure 19: VMware Workstation 14 Player - Set virtualization engine option

    * Click :guilabel:`Close`.
    * Click :guilabel:`Finish`.
    
Attach the ready-made VMware Clear Linux image
**********************************************

#.  Move or copy the ready-made VMware |CL| image file (i.e. `clear-<version>-basic.vmdk`)
    to the directory where the newly created VM resides.

    .. note::

      VMware VM files are typically located in:

      * Linux distros: `/home/username/vmware`
      * Windows: `C:/\Users/\username/\Documents/\Virtual Machines`

#.  On the `VMware Workstation Player` home screen:

    * Select the newly created VM.
    * Click :guilabel:`Edit virtual machine settings`.  

      .. figure:: figures/vmware-player/vmware-player-20.png
        :scale: 100%
        :alt: VMware Workstation 14 Player - Edit virtual machine settings

      Figure 20: VMware Workstation 14 Player - Edit virtual machine settings

#.  Disconnect the CD/DVD (IDE):

    * Select :guilabel:`CD/DVD (IDE)` and under :guilabel:`Device status`, uncheck :guilabel:`Connect at 
      power on`. 

      .. figure:: figures/vmware-player/vmware-player-21.png
        :scale: 100%
        :alt: VMware Workstation 14 Player - Disconnect CD/DVD (IDE)

      Figure 21: VMware Workstation 14 Player - Disconnect CD/DVD (IDE)

#.  Remove the default hard disk:

    * Under the :guilabel:`Hardware` tab, select :guilabel:`Hard Disk (SCSI)`.
    * Click :guilabel:`Remove`.

      .. figure:: figures/vmware-player/vmware-player-22.png
        :scale: 100%
        :alt: VMware Workstation 14 Player - Remove hard drive

      Figure 22: VMware Workstation 14 Player - Remove hard drive

#.  Add a new hard disk and attach the ready-made VMware |CL| image:

    * Click :guilabel:`Add`.
    * Under :guilabel:`Hardware types`, select :guilabel:`Hard Disk`.
    * Click :guilabel:`Next`.

      .. figure:: figures/vmware-player/vmware-player-23.png
        :scale: 100%
        :alt: VMware Workstation 14 Player - Add new hard drive

      Figure 23: VMware Workstation 14 Player - Add new hard drive

    * Select the preferred :guilabel:`Virtual disk type`.

      .. figure:: figures/vmware-player/vmware-player-24.png
        :scale: 100%
        :alt: VMware Workstation 14 Player - Select virtual disk type

      Figure 24: VMware Workstation 14 Player - Select virtual disk type

    * Select :guilabel:`Use an existing virtual disk`.
 
      .. figure:: figures/vmware-player/vmware-player-25.png
        :scale: 100%
        :alt: VMware Workstation 14 Player - Use existing virtual disk

      Figure 25: VMware Workstation 14 Player - Use existing virtual disk
   
    * Click :guilabel:`Browse` and select the ready-made VMware |CL| image file.

      .. figure:: figures/vmware-player/vmware-player-26.png
        :scale: 100%
        :alt: VMware Workstation 14 Player - Select ready-made VMware |CL| 

      Figure 26: VMware Workstation 14 Player - Select ready-made VMware |CL| 
      image file

    * Click :guilabel:`Finish`.

      .. note::
          When asked to convert the disk image, either option works. 

Enable UEFI boot support
************************

|CL| needs UEFI support in order to boot.  Enable it by appending to the end  
of the VM's :file:`.vmx` file:

  .. code-block:: console

    firmware = "efi"

.. note::

  VMware VM files are typically located in:

  * Linux distros: `/home/username/vmware`
  * Windows: `C:/\Users/\username/\Documents/\Virtual Machines` (The file type 
    is `VMware virtual machine configuration`.)

Power on the virtual machine
****************************

After configuring the settings above, power on the virtual machine.  

Also see:

   * :ref:`vmware-esxi`

.. _VMware Workstation 14 Player: https://www.vmware.com/products/workstation-player.html
.. _VMware Workstation Player guide: https://docs.vmware.com/en/VMware-Workstation-Player/index.html
.. _latest: https://download.clearlinux.org/image/
.. _7zip: http://www.7-zip.org/
.. _VirtualBox: https://www.virtualbox.org/
.. _image: https://download.clearlinux.org/image
.. _releases: https://download.clearlinux.org/releases
.. _Intel® Virtualization Technology: https://www.intel.com/content/www/us/en/virtualization/virtualization-technology/intel-virtualization-technology.html
.. _Intel® Virtualization Technology for Directed I/O: https://software.intel.com/en-us/articles/intel-virtualization-technology-for-directed-io-vt-d-enhancing-intel-platforms-for-efficient-virtualization-of-io-devices


