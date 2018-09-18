.. _virtualbox:

Run pre-configured |CL-ATTR| as a VirtualBox\* guest OS
###########################################################

This instruction explains how to deploy a pre-configured |CL-ATTR| image as a guest on the `VirtualBox hypervisor`_ .

Download VirtualBox
===================

VirtualBox\* is a type 2 hypervisor from Oracle. Download and use **version 5.0 or greater** from the `official VirtualBox website`_.

.. _create_vm_vbox:

Prerequisites
=============

The instruction assumes that you have: 

#. Enabled virtualization technology in the host machine's BIOS. 
   
   .. note:: 

      For help, see: Intel® `Virtualization Technology`_ (Intel® VT). 

#. Installed VirtualBox on your host machine per the 
   `appropriate instructions`_ for your platform.

If you have not completed the above steps, do so before continuing. 

Create a virtual machine in VirtualBox
======================================

#. Log in to your host and open a terminal emulator.

#. Download the `latest`_ **live** version (clear-XXXX-live.img.xz) of
   |CL|. You can also use this command: 

   .. code-block:: bash

      curl -O https://download.clearlinux.org/image/clear-$(curl https://download.clearlinux.org/latest)-live.img.xz

#. Decompress the downloaded image. Uncompressed image size is ~ **5GB**.

   + On Linux ::

       xz -d clear-XXXX-live.img.xz

   + On Windows you can use `7zip`_.

     - Right-click the file to *extract in the same directory*.

       .. image:: ./figures/7zipwin.png
          :alt: 7zip extract here command

#. To convert a raw image to :abbr:`VDI (VirtualBox Disk Image)`
   format, you can use one of the following commands::

      VBoxManage convertfromraw clear-XXXX-live.img clear-XXXX-live.vdi --format VDI

   or::

      vbox-img convert --srcfilename clear-XXXX-live.img --dstfilename clear-XXXX-live.vdi --srcformat raw --dstformat vdi


   .. note:: Be sure you have VirtualBox directory in your PATH (i.e., on
      Windows :file:`C:\\Program Files\\Oracle\\VirtualBox`).

      + On windows: launch a **Command Prompt** program and type

        .. code-block:: console

           set PATH=%PATH%;"C:\Program Files\Oracle\VirtualBox"

        .. image:: ./figures/vbox-convert-image.png
           :alt: Convert image in Windows command propt

#. Create a virtual machine using the VirtualBox assistant:

   a. Type: **Linux**
   
   b. Version: **Linux 2.6 / 3.x / 4.x (64-bit)**

      .. image:: ./figures/vbox-create-vm.png
          :alt: Create a new image in VirtualBox

   c. Select default memory size.

      .. image:: ./figures/vbox-memory-size.png

   d. Attach the virtual disk created in step number 3 as a virtual hard
      disk file. Click the folder icon (lower right) to browse to find the
      VDI file.

      .. image:: ./figures/vbox-hdisk.png

#. After it is created, go to settings to enable **EFI support**

   * System -> Enable EFI (special OSes only)

     .. image:: ./figures/vbox-efi.png
        :alt: Enable EFI on VirtualBox


Run your new VM
===============

|CL| supports VirtualBox kernel modules used
by the Linux kernel 4.14 :abbr:`LTS (Long Term Support)` 
(*kernel-lts bundle*).This kernel was selected because |CL| OS's main kernel
(``kernel-native``) bundle keeps up-to-date with the upstream Linux kernel,
and sometimes VirtualBox kernel modules aren't compatible with pre-kernel
releases.

On the first boot, |CL| requests a user login.

#. Type **root**. 

#. Enter a new password when prompted. 

To install the VirtualBox kernel modules, here are the steps:

#. Install the bundle that supports VirtualBox modules::

     swupd bundle-add kernel-lts

#. Set a timeout in the bootmanager to shows a menu at boot time::

     clr-boot-manager set-timeout 10

#. Update the bootloader entries with::

     clr-boot-manager update

#. Reboot your system with::

     reboot

   and choose **clear-linux-lts-4.14.XX-YYY** kernel version.

#. (*Optional*) Unset timeout to boot directly to LTS version::

     clr-boot-manager set-timeout 0

#. (*Mandatory*) Update bootmanger to always use LTS version::

     clr-boot-manager update

Install Guest Additions
-----------------------

The kernel modules are shipped with the ``kernel-lts`` bundle. Insert Guest 
Additions CD image using *Devices* menu you'll need to install the *user* 
Linux Guest Additions. To install the VirtualBox Guest Additions, 
follow these steps:


#. Insert Guest Additions CD image using *Devices* menu 

   .. image:: ./figures/vbox-cd.png  
      :alt: VirtualBox CD 

#. Install Linux users Guest Additions:: 

    install-vbox-lga  

#. Reboot your system::  
      
    reboot


Troubleshooting
---------------

On Windows OS, *VirtualBox* cannot do a **Hardware Virtualization** when
*Hyper-V* is enabled.

.. image:: ./figures/vbox-no-vtx.png
   :alt: VirtualBox hardware acceleration error

To disable *Hyper-V* you should execute::

  bcdedit /set {current} hypervisorlaunchtype off

in an **Administrator: Command Prompt**, then reboot your system.

To enable Hyper-V again, you should execute::

  bcdedit /set {current} hypervisorlaunchtype Auto

.. _appropriate instructions: https://www.virtualbox.org/manual/ch02.html
.. _official VirtualBox website: https://www.virtualbox.org/wiki/Downloads
.. _VirtualBox hypervisor: https://www.virtualbox.org/
.. _latest: https://download.clearlinux.org/image/
.. _7zip: http://www.7-zip.org/
.. _Virtualization Technology: https://www.intel.com/content/www/us/en/virtualization/virtualization-technology/intel-virtualization-technology.html