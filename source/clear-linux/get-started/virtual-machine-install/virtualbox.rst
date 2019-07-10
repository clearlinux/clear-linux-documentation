.. _virtualbox:

Run pre-configured |CL-ATTR| as a VirtualBox\* Virtual Machine
##############################################################

VirtualBox\* is a type 2 hypervisor from Oracle. This document explains how 
to create a virtual machine on the `VirtualBox hypervisor`_  with |CL-ATTR| 
as the guest operating system.

These instructions make use of a preinstalled |CL| disk image to setup a |CL| 
virtual machine without manual installation. |CL| can also be installed from 
scratch on a |VB| using the |CL| installed.
See: :ref:`virtualbox-cl-installer`

.. contents:: :local:
    :depth: 2



.. _vbox-prereqs-begin:

Prerequisites
*************

Before continuing make sure that you have: 

#. Enabled virtualization, such as Intel® 
   `Virtualization Technology`_ (Intel® VT), on the host system from 
   EFI/BIOS.

#. Downloaded and installed |VB| **version 6.0 or greater** from 
   the `official VirtualBox website`_ per the  `appropriate instructions`_ 
   for your platform.

.. _vbox-prereqs-end:



Download and extract |CL|
*************************

The |CL| live image needs to be downloaded and extracted. The live image will 
be used to created a |VB| virtual disk image that can be used with a 
:abbr:`VM (Virtual Machine)`.

#. Download the **live image** (:file:`clear-<VERSION-live.img.xz`) of
   |CL|. On the `downloads page`_, this is listed as 
   **Clear Linux OS live boot image**.
   
   
   You can also use this command to download from a terminal: 

   .. code-block:: bash

      curl -O https://cdn.download.clearlinux.org/image/$(curl https://cdn.download.clearlinux.org/image/latest-images | grep live.img)

#. Validate the integrity of the downloaded image by checking the file hash 
   and signatures. Refer to the document on :ref:`validate-signatures` for 
   detailed steps.

#. Decompress the downloaded image. Uncompressed image size is ~ **5GB**.

   - On Windows you can use `7zip`_ to extract the file by right-clicking the 
     file and selecting *Extract Here* (in the same directory)

       .. image:: ./figures/vbox/vbox-extract-cl-IMG.png
          :alt: 7zip extract here command

   - On Linux :

     .. code-block:: bash   

        xz -d clear-<VERSION>-live.img.xz

#. There originally downloaded compressed archive file
   (:file:`clear-<VERSION>-live.img.xz`) can now be deleted.



Convert |CL| live image to a |VB| Disk Image 
********************************************

The |CL| live image is in a RAW disk image. The live image needs to be 
converted to a :abbr:`VDI (VirtualBox Disk Image)` format which |VB| 
can utilize.

#. Launch a terminal and navigate to the directory containing the 
   extracted live image.


#. Convert RAW live image to a :abbr:`VDI (VirtualBox Disk Image)`
   format using the command-line VirtualBox Disk Utility.

   .. code-block:: bash

      VBoxManage convertfromraw clear-<VERSION>-live.img clear-VM.vdi --format VDI

   .. note::
      The :command:`PATH` environment variable may need to be updated to make the 
      :command:`VBoxManage` command easily accessible from the terminal. 
      For example, using Windows PowerShell:

      .. code-block:: bash

         $env:PATH += ";C:\Program Files\Oracle\VirtualBox"


   .. image:: ./figures/vbox/vbox-convert-raw-to-VDI.png
      :alt: Convert image in Windows command prompt

   For more information on the :command:`VBoxManage` command,
   see the `VirtualBox manual section on VBoxManage`_.


#. The originally extracted live image file 
   (:file:`clear-<VERSION>-live.img`) can now be deleted.


#. Move the converted :file:`clear-VM.vdi` disk image file to a permanent 
   location. The VDI will be attached to the |VB| VM and should not be 
   deleted.



Create a new |VB| virtual machine
*********************************

A new VM needs to be created in |VBM| to attach the VDI with |CL| installed.

General instructions for creating a virtual machine and details about using 
different settings are available on the 
`VirtualBox manual section on Creating a VM`_.


#. Launch the |VBM| from your host system.


#. Click the *New* button to create a new VM. 

   .. image:: ./figures/vbox/vbox-new-vm.png
      :alt: Create a new VM in VirtualBox


#. A *Create Virtual Machine* window will appear. 
   Select the following settings:
   
   - Type: **Linux**
   - Version: **Linux 2.6 / 3.x / 4.x (64-bit)**
   - Memory size: **1024 MB** (this can be adjusted appropriately)
   - Hard disk: **Use an existing virtual hard disk file**

   Click the folder icon next to the drop down menu:

   .. image:: ./figures/vbox/vbox-create-vm-existing-disk.png
      :alt: Create a new VM in VirtualBox with an existing disk


#. A new window will appear for choosing an existing disk. Click the *Add* 
   button, browse to the saved VDI file, and click *Choose*.

   .. image:: ./figures/vbox/vbox-create-vm-choose-disk.png
      :alt: Create a new VM in VirtualBox with an existing disk

#. Click the *Create* button.


#. A new virtual machine will be created and appear in the |VBM|. Click 
   *Settings* to configure the |CL| VM.

   .. image:: ./figures/vbox/vbox-vm-created.png
      :alt: A VM selected in VirtualBox Manager

#. A *VM - Settings* window will appear. Navigate to the *System* pane from 
   the left-hand and select the following setting:

   - **Enable I/O APIC**
   - **Enable EFI (special OSes only)**
   

   .. image:: ./figures/vbox/vbox-vm-settings-EFI.png
      :alt: Enable EFI on a VirtualBox VM settings



.. note::
   By default, only 1 virtual CPU is allocated to the new VM. Consider 
   increasing the number of virtual processors allocated to the virtual 
   machine under Settings --> System --> Processor for increased 
   performance.

.. _vbox-start-vm-and-lga-begin:

Start the |CL| VM
*****************

The |CL| VM can now be powered on and setup.

General instructions for using a |VB| virtual machine are available on the 
`VirtualBox manual section on Running a VM`_.

#. Start the VM from the |VBM| by selecting the |CL| VM and clicking *Start*

   .. image:: ./figures/vbox/vbox-start-vm.png
      :alt: Starting a VirtualBox VM

#. |CL| will boot and prompt for login.

    - Enter **root** for the username. 

#. You will be immediately prompted to set a new password for the **root** 
   user. Reference :ref:`security` for more information about |CL| security 
   concepts.

   .. image:: ./figures/vbox/vbox-cl-first-login.png
      :alt: Initial login to Clear Linux OS on a VirtualBox VM



Install |VB| Linux Guest Additions 
==================================

The |VB| Linux Guest Additions provide drivers for full compatibility and 
functionality. 

|CL| provides |VB| guest drivers and an install script in the **kernel-lts** 
(Long Term Support) bundle by |CL|.


#. Validate the installed kernel is **kernel-lts** by checking the output 
   of the :command:`uname -r` command. It should end in **.lts**.

   .. code-block:: bash

      uname -r
      4.<VERSION>.lts

   If the running kernel is not **lts**: install the LTS kernel manually, 
   update the bootloader, and check again:

   .. code-block:: bash

      swupd bundle-add kernel-lts
      clr-boot-manager set-kernel $(basename $(realpath /usr/lib/kernel/default-lts))
      clr-boot-manager update
      reboot

#. Remove any kernel bundles that are not *kernel-lts* or *kernel-install* 
   to simplify and avoid conflicts:

   .. code-block:: bash

      swupd bundle-list | grep kernel
      swupd bundle-remove <NON-LTS-KERNEL>

   .. image:: ./figures/vbox/vbox-cl-remove-non-lts-kernels.png
      :alt: Initial login to Clear Linux OS on a VirtualBox VM

#. From the VM Console window, click *Devices* on the top menu bar, and 
   select *Insert Guest Additions CD image...* to mount the |VB| driver 
   installation to the |CL| VM.

   .. image:: ./figures/vbox/vbox-vm-insert-ga-cd.png  
      :alt: VirtualBox CD 

.. note::
   To release the mouse cursor from the VM console window, press the right Ctrl key on the keyboard.


#. |CL| provides a script called :command:`install-vbox-lga` to help patch 
   and install |VB| drivers for |CL|. Inside |CL| VM run this command:

   .. code-block:: bash

      install-vbox-lga

#. After the script completes successfully, reboot the |CL| VM.

   .. code-block:: bash

      reboot

#. After the VM reboot, login and verify the |VB| drivers are loaded:

   .. code-block:: bash

      lsmod | grep ^vbox

   You should see drivers loaded with names beginning with **vbox**: (vboxguest, vboxsf, vboxvideo).


The |CL| VM running on |VB| is ready to be used.

.. _vbox-start-vm-and-lga-end:

.. _vbox-troubleshooting-begin:

Troubleshooting
***************

#. **Problem:** Out of disk space inside of |CL| and not be able to install
   additional bundles. 

   **Solution:** The |CL| images are small to minimize download time and
   initial disk space .

   Power off the VM and resize the virtual disk for the |CL| VM using the |VB|
   `Virtual Media Manager`_ found under the File menu. Afterwards, power the
   |CL| VM on and follow the instructions here to have |CL| detect the resized
   disk. :ref:`increase-virtual-disk-size`

#. **Problem:** On a Microsoft Windows OS, |VB| encounters an error when
   trying to start a VM indicating *VT-X/AMD-v hardware acceleration is not
   available on your system.*


   .. image:: ./figures/vbox/vbox-no-vtx.png
      :alt: VirtualBox hardware acceleration error


   **Solution:** First, double check the `Prerequisites`_ section to make sure
   *Hardware accelerated virtualization* extensions have been enabled in the
   host system's EFI/BIOS.

   *Hardware accelerated virtualization*, may get disabled for |VB| when another 
   hypervisor, such as *Hyper-V* is enabled.

   To disable *Hyper-V* execute this command in an 
   **Administrator: Command Prompt or Powershell**, and reboot the system:

   .. code-block:: bash

      bcdedit /set {current} hypervisorlaunchtype off


   To enable Hyper-V again, execute this command in an 
   **Administrator: Command Prompt or Powershell**, and reboot the system:

   .. code-block:: bash

      bcdedit /set {current} hypervisorlaunchtype Auto

.. _vbox-troubleshooting-end:




.. |VB| replace:: VirtualBox
.. |VBM| replace:: VirtualBox Manager

.. _appropriate instructions: https://www.virtualbox.org/manual/ch02.html

.. _official VirtualBox website: https://www.virtualbox.org/wiki/Downloads

.. _VirtualBox hypervisor: https://www.virtualbox.org/

.. _downloads page: https://clearlinux.org/downloads

.. _`VirtualBox manual section on Creating a VM`: https://www.virtualbox.org/manual/UserManual.html#gui-createvm

.. _`VirtualBox manual section on Running a VM`: https://www.virtualbox.org/manual/ch01.html#intro-starting-vm-first-time

.. _`Virtual Media Manager`: https://www.virtualbox.org/manual/ch05.html#vdis

.. _7zip: http://www.7-zip.org/

.. _Virtualization Technology: https://www.intel.com/content/www/us/en/virtualization/virtualization-technology/intel-virtualization-technology.html

.. _`VirtualBox manual section on VBoxManage`: https://www.virtualbox.org/manual/ch08.html#vboxmanage-convertfromraw
