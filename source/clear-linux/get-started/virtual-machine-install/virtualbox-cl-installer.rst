.. _virtualbox-cl-installer:

Install |CL-ATTR| as a VirtualBox\* Virtual Machine
###################################################

VirtualBox\* is a type 2 hypervisor from Oracle. This document explains how 
to create a virtual machine on the `VirtualBox hypervisor`_  with |CL-ATTR| 
as the guest operating system.

These instructions make use of the |CL| installer to create a brand new |CL| 
installation. A preinstalled disk image is also available to get started 
with |CL| faster. See: :ref:`virtualbox`


.. contents:: :local:
    :depth: 2


.. include:: virtualbox.rst
   :start-after: vbox-prereqs-begin:
   :end-before: vbox-prereqs-end:



Download and extract the |CL| installer ISO image
*************************************************

The appropriate |CL| installer image needs to be downloaded and extracted.

.. note::
   The :file:`installer.iso` is for limited use on special cases where ISO 
   image format is required, such as |VB|. The preferred installer for |CL| 
   for UEFI systems is the :file:`-installer.img`.

#. Download the **installer ISO** image (:file:`clear-<VERSION>-installer.iso.xz`) of
   |CL|. On the `downloads page`_, this is listed as 
   **Clear Linux OS for Virtual Provisioning**.
   
   
   You can also use this command to download from a terminal: 

   .. code-block:: bash

      curl -O https://download.clearlinux.org/image/$(curl https://download.clearlinux.org/image/latest-images | grep installer.iso)

#. Validate the integrity of the downloaded image by checking the file hash 
   and signatures. Refer to the document on :ref:`validate-signatures` for 
   detailed steps.

#. Decompress the downloaded image. Uncompressed image size is ~ **5GB**.

   - On Windows you can use `7zip`_ to extract the file by right-clicking the 
     file to *Extract Here* (in the same directory)

       .. image:: ./figures/vbox/vbox-extract-cl-ISO.png
          :alt: 7zip extract here command

   - On Linux :

     .. code-block:: bash

         xz -d clear-<VERSION>-installer.iso.xz




#. The originally downloaded compressed archive file 
   (:file:`clear-<VERSION>-installer.iso.xz`) can now be deleted.


Create a new |VB| virtual machine
*********************************

A new :abbr:`VM (Virtual Machine)` needs to be created in |VBM| for |CL| to be installed onto. 

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
   - Hard disk: **Create a virtual hard disk now**

   .. image:: ./figures/vbox/vbox-create-vm-new-disk.png
      :alt: Create a new VM in VirtualBox with a new disk


#. Click the *Create* button.

#. A *Create Virtual Hard Disk* window will appear. 
   Select the following settings:

   - File size: **8.00 GB** (this can be adjusted appropriately)
   
   - Hard disk file type: **VDI (Virtual Box Disk Image)**

   - Storage on physical hard disk: **Dynamically allocated** 

   .. image:: ./figures/vbox/vbox-create-disk.png
      :alt: Create a new virtual hard disk in VirtualBox

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


Install |CL| on the |VB| VM
***************************

|CL| is ready to be installed.


Mount the installation ISO
==========================
At this point, the newly created VM has a blank virtual hard disk with no 
operating system.The |CL| installer ISO needs to be mounted as a virtual 
CD-ROM on the VM before powering the VM on.

#. From the *VM - Settings* window, navigate to the *Storage* pane from the 
   left-hand side.

#. From the middle *Storage Devices* column, click the blue CD disk labeled 
   *Empty* under the *Controller: IDE* from.

#. From the right-hand *Attributes* column, click the blue CD disk next to 
   the *Optical Drive* drop down menu and click *Choose Virtual Optical 
   Disk File...*

   .. image:: ./figures/vbox/vbox-vm-settings-mount-ISO.png
      :alt: Mounting an ISO in VirtualBox VM Settings  

#. A *choose a virtual optical disk file* browser window will appear. 
   Navigate to the extracted ISO file, select it, and click *Open*.

   .. image:: ./figures/vbox/vbox-vm-settings-browse-ISO.png
      :alt: Mounting an ISO in VirtualBox VM Settings  

#. Click *OK* to exit the *VM Settings* menu and return to the main 
   |VBM|.



Install |CL| using the installer
================================

#. Start the VM from the |VBM| by selecting the |CL| VM and 
   clicking *Start*

   .. image:: ./figures/vbox/vbox-start-vm.png
      :alt: Starting a VirtualBox VM

#. A new window of the VM console will appear and boot into the |CL| 
   installer. Follow the steps in the `Install Clear Linux OS`_ to 
   install |CL| onto the VM virtual disk.

.. note::
   Do not choose a different kernel from the installer. **kernel-lts**, the 
   Long Term Support (LTS) kernel is required for |VB| driver compatibility.


#. After |CL| installation is complete, the VM will reboot and return to the 
   |CL| installer. 

.. note::
   To release the mouse cursor from the VM console window, press the right Ctrl key on the keyboard.


Unmount the installation ISO
============================

The |CL| installer ISO needs to be unmounted to allow the VM to boot from the
virtual hard disk, which |CL| has been installed to.


#. Power off the |CL| VM.

   .. image:: ./figures/vbox/vbox-shutdown-vm.png
      :alt: Powering off a VirtualBox VM

#. Click *Settings* to configure the |CL| VM.

   .. image:: ./figures/vbox/vbox-vm-created.png
      :alt: A VM selected in VirtualBox Manager

#. From the *VM - Settings* window, navigate to the *Storage* pane from the 
   left-hand side.

#. From the middle *Storage Devices* column, click the blue CD disk labeled  
   *clear-<VERSION>-installer.iso* under the *Controller: IDE* from.

#. From the right-hand *Attributes* column, click the blue CD disk next to 
   the *Optical Drive* drop down menu and click *Remove Disk from Virtual 
   Drive*

   .. image:: ./figures/vbox/vbox-vm-settings-unmount-ISO.png
      :alt: Unmounting an ISO in VirtualBox VM Settings        

#. Click *OK* to exit the *VM Settings* menu and return to the main 
   |VBM|.




.. include:: virtualbox.rst
   :start-after: vbox-start-vm-and-lga-begin:
   :end-before: vbox-start-vm-and-lga-end:





.. include:: virtualbox.rst
   :start-after: vbox-troubleshooting-begin:
   :end-before: vbox-troubleshooting-end




.. |VB| replace:: VirtualBox
.. |VBM| replace:: VirtualBox Manager

.. _appropriate instructions: https://www.virtualbox.org/manual/ch02.html
.. _official VirtualBox website: https://www.virtualbox.org/wiki/Downloads
.. _VirtualBox hypervisor: https://www.virtualbox.org/
.. _downloads page: https://clearlinux.org/downloads
.. _`VirtualBox manual section on Creating a VM`: https://www.virtualbox.org/manual/UserManual.html#gui-createvm

.. _`VirtualBox manual section on Running a VM`: https://www.virtualbox.org/manual/ch01.html#intro-starting-vm-first-time
.. _`Install Clear Linux OS`: https://clearlinux.org/documentation/clear-linux/get-started/bare-metal-install#install-cl-on-your-target-system
.. _7zip: http://www.7-zip.org/
.. _Virtualization Technology: https://www.intel.com/content/www/us/en/virtualization/virtualization-technology/intel-virtualization-technology.html
