.. _vmw-player:

|CL-ATTR| on VMware\* Workstation Player
########################################

This page explains how to create a new VM and install |CL| on it with the
VMware Workstation Player hypervisor.

.. contents::
   :local:
   :depth: 1

Overview
********

`VMware Workstation Player`_ is a type 2 hypervisor. It runs on top of
Windows\* or Linux\* operating systems. With VMware Workstation Player, you can
create, configure, manage, and run |CL-ATTR| :abbr:`VMs (Virtual Machines)`
on your local system.

VMware offers a type 1 hypervisor called `VMware ESXi`_ designed for the
cloud environment. For information on how to install |CL| as guest OS on
it, see :ref:`vmware-esxi-install-cl`.

.. note::

   The screenshots on this document show the Windows version of the
   VMware Workstation 15 Player. The menus and prompts are similar to those
   in other versions and for the Linux OS save some minor wording differences.

If you prefer to use a pre-configured |CL| VMware image instead,
see our :ref:`vmw-player-preconf` guide.

Install the VMware Workstation Player hypervisor
************************************************

#. Enable :abbr:`Intel® VT (Intel® Virtualization Technology)` and
   :abbr:`Intel® VT-d (Intel® Virtualization Technology for Directed I/O)` in
   your system's BIOS.

#. `VMware Workstation Player`_ is available for Windows and Linux.
   Download your preferred version.

   .. note::

      By default, selecting download means you receive the latest version
      of this application. Commands may differ based on the version.

#. Install VMware Workstation Player following the instructions
   appropriate for your system's OS:

   * On supported Linux distros:

     #. Enable a GUI desktop.
     #. Start a terminal emulator.
     #. Start the installer by issuing the command below and follow the
        guided steps.

        .. code-block:: console

           sudo sh ./VMware-Player-[version number].x86_64.bundle

   * On Windows:

     #. Start the installer.
     #. Follow the setup wizard.

For additional help, see the `VMware Workstation Player Documentation`_.

Create and configure a new VM
*****************************

#. Start the `VMware Workstation Player` app.

#. On the home screen, click :guilabel:`Create a New Virtual Machine`. See
   Figure 1.

   .. figure:: figures/vmw-player/vmw-player-01.png
      :scale: 100%
      :alt: VMware Workstation Player - Create a new virtual machine

      Figure 1: VMware Workstation Player - Create a new virtual
      machine

#. Select :guilabel:`I will install the operating system later`.

   .. figure:: figures/vmw-player/vmw-player-02X.png
      :scale: 100%
      :alt: I will install the operating system later.

      Figure 2: I will install the operating system later.

#. Click the :guilabel:`Next` button.

#. On the :guilabel:`Select a Guest Operating System`, set the
   :guilabel:`Guest operating system` setting to :guilabel:`Linux`. See
   Figure 3.

   .. figure:: figures/vmw-player/vmw-player-03.png
      :scale: 100%
      :alt: VMware Workstation Player - Select guest operating system type

      Figure 3: VMware Workstation Player - Select guest operating system
      type

#. Set the :guilabel:`Version` setting to
   :guilabel:`Other Linux 5.x or later kernel 64-bit`.

#. Click the :guilabel:`Next` button.

#. On the :guilabel:`Name the Virtual Machine` screen, name the new VM. See
   Figure 4.

   .. figure:: figures/vmw-player/vmw-player-04.png
      :scale: 100%
      :alt: VMware Workstation Player - Name virtual machine

      Figure 4: VMware Workstation Player - Name virtual machine

#. Click the :guilabel:`Next` button.

#. On the :guilabel:`Specify Disk Capacity` screen, set the VM's maximum disk
   size. See Figure 5.

   .. figure:: figures/vmw-player/vmw-player-05.png
      :scale: 100%
      :alt: VMware Workstation Player - Set disk capacity

      Figure 5: VMware Workstation Player - Set disk capacity

   .. note::

      For optimal performance with the |CL| Desktop image, we recommend 32GB
      of drive space. See :ref:`system-requirements` for more details.

#. Click the :guilabel:`Next` button.

#. On the :guilabel:`Ready to Create Virtual Machine` screen, click the
   :guilabel:`Customize Hardware...` button. See Figure 6.

   .. figure:: figures/vmw-player/vmw-player-06.png
      :scale: 100%
      :alt: VMware Workstation Player - Customize hardware

      Figure 6: VMware Workstation Player - Customize hardware

#. Select :guilabel:`Memory` and set the size to 2GB. See Figure 7.

   .. figure:: figures/vmw-player/vmw-player-07.png
      :scale: 100%
      :alt: VMware Workstation Player - Set memory size

      Figure 7: VMware Workstation Player - Set memory size

   .. note::
      The |CL| installer ISO needs a minimum of 2GB of RAM.
      After completing installation, |CL| can run on as little as
      128MB of RAM. Thus, you can reduce the memory size if needed.
      See :ref:`system-requirements` for more details.

#. Under the :guilabel:`Device` list, select :guilabel:`Processors`. See
   Figure 8.

   .. figure:: figures/vmw-player/vmw-player-08.png
      :scale: 100%
      :alt: VMware Workstation Player - Set virtualization engine option

      Figure 8: VMware Workstation Player - Set virtualization engine
      option

#. Under :guilabel:`Processors`, :guiilabel:`Number of processor cores`, 
   enter 4. 

#. Under the :guilabel:`Virtualization engine` section,
   check :guilabel:`Virtualize Intel VT-x/EPT or AMD-V/RVI`.

#. Click the :guilabel:`Close` button.

#. Click the :guilabel:`Finish` button.

Enable UEFI boot support
************************

|CL| needs UEFI support to boot. To enable UEFI:

#. Power off the VM. click the :guilabel:`Player` menu. See Figure 9.

   .. figure:: figures/vmw-player/vmw-player-09.png
      :scale: 100%
      :alt: VMware Workstation Player - Power off virtual machine

      Figure 9: VMware Workstation Player - Power off virtual machine

#. Go to :guilabel:`Power` and select :guilabel:`Shut Down Guest`.

#. Add the following line to the end of your VM's :file:`.vmx` file:

   .. code-block:: console

      firmware = "efi"

   .. note::

      Depending on the OS, you can typically find the VMware VM files under:

      * On Linux distros: :file:`/home/username/vmware`
      * On Windows: :file:`C:\\Users\\username\\Documents\\Virtual Machines`

Install |CL| into the new VM
****************************

#. Select the newly-created VM and click the :guilabel:`Play virtual machine`
   button. See Figure 10.

   .. figure:: figures/vmw-player/vmw-player-10.png
      :scale: 100%
      :alt: VMware Workstation Player - Power on virtual machine

      Figure 10: VMware Workstation Player - Power on virtual machine

#. Select the appropriate image type below.

.. tabs::

   .. tab:: |CL| Desktop 

      #. On the :guilabel:`Welcome to the New Virtual Machine Wizard` screen,
         select the :guilabel:`Installer disc image file (iso)` option.
         See Figure 2.

         .. figure:: figures/vmw-player/vmw-player-02.png
            :scale: 100%
            :alt: VMware Workstation Player - Select |CL| installer ISO

            Figure 2: VMware Workstation Player - Select |CL| installer ISO

      #. Click the :guilabel:`Browse` button and select the decompressed |CL|
         installer ISO.

      #. Follow the :ref:`install-on-target-start` guide to complete the
         installation of |CL|.

      #. After the installation completes, reboot the VM. This reboot
         restarts the |CL| installer.

   .. tab:: |CL| Pre-configured VMWare image

      #. Move the downloaded and decompressed pre-configured |CL| VMware
         image file :file:`clear-[version number]-basic.vmdk` to the directory where your newly-created VM resides.

         .. note::

            Depending on the OS, you can typically find the VMware VM files under:

            * Linux distros: :file:`/home/username/vmware`
            * Windows: :file:`C:\Users\username\Documents\Virtual Machines`

      #. On the :guilabel:`VMware Workstation Player` home screen, select
         your newly-created VM. See figure 9.

         .. figure:: figures/vmw-player-preconf/vmw-player-preconf-09.png
            :scale: 100%
            :alt: VMware Workstation 14 Player - Edit virtual machine settings

            Figure 9: VMware Workstation 14 Player - Edit virtual machine settings

      #. Click :guilabel:`Edit virtual machine settings`.

      #. To remove the default hard disk, under the :guilabel:`Device` list, 
         select :guilabel:`Hard Disk (SCSI)`. See figure 10.

         .. figure:: figures/vmw-player-preconf/vmw-player-preconf-10.png
            :scale: 100%
            :alt: VMware Workstation 14 Player - Remove hard drive

            Figure 10: VMware Workstation 14 Player - Remove hard drive

      #. Click the :guilabel:`Remove` button.

      #. To add a new hard disk and attach the pre-configured |CL| VMware image,
         click the :guilabel:`Add...` button. See Figure 11.

         .. figure:: figures/vmw-player-preconf/vmw-player-preconf-11.png
            :scale: 100%
            :alt: VMware Workstation 14 Player - Add new hard drive

            Figure 11: VMware Workstation 14 Player - Add new hard drive

      #. Under the :guilabel:`Hardware types` section, select :guilabel:`Hard Disk`.

      #. Click the :guilabel:`Next` button.

      #. Select your preferred :guilabel:`Virtual disk type`. See figure 12.

         .. figure:: figures/vmw-player-preconf/vmw-player-preconf-12.png
            :scale: 100%
            :alt: VMware Workstation 14 Player - Select virtual disk type

            Figure 12: VMware Workstation 14 Player - Select virtual disk type

      #. Select the :guilabel:`Use an existing virtual disk` option. See figure 13.

         .. figure:: figures/vmw-player-preconf/vmw-player-preconf-13.png
            :scale: 100%
            :alt: VMware Workstation 14 Player - Use existing virtual disk

            Figure 13: VMware Workstation 14 Player - Use existing virtual disk

      #. Click the :guilabel:`Browse` button and select the pre-configured |CL|
         VMware image file. See figure 14.

         .. figure:: figures/vmw-player-preconf/vmw-player-preconf-14.png
            :scale: 100%
            :alt: VMware Workstation 14 Player - Select ready-made VMware |CL|

            Figure 14: VMware Workstation 14 Player - Select ready-made VMware |CL|
            image file

      #. Click the :guilabel:`Finish` button.

         .. note::

            When asked to convert the existing virtual disk to a newer format,
            selecting either option works.

   .. tab:: Custom iso image

      Text





Detach the |CL| installer ISO from the VM
*****************************************

#. To enable the mouse pointer so you access VMware Workstation Player's
   menus, press :kbd:`<CTRL>` + :kbd:`<ALT>` on the keyboard.

#. To disconnect the CD/DVD to stop it from booting the |CL| installer ISO
   again, click the :guilabel:`Player` menu. See Figure 11.

   .. figure:: figures/vmw-player/vmw-player-11.png
      :scale: 100%
      :alt: VMware Workstation Player - Edit CD/DVD settings

      Figure 11: VMware Workstation Player - Edit CD/DVD settings

#. Go to :menuselection:`Removable Devices-->CD/DVD (IDE)-->Disconnect`.

#. Click the :guilabel:`OK` button.

Install open-vm-tools
*********************

Optional: You may want to install the `open-vm-tools` in your virtual
machine. The Open Virtual Machine Tools (open-vm-tools) are the open source
implementation of VMware Tools for Linux\* guest operating systems.

#. Power on your |CL| virtual machine. On the
   :guilabel:`VMware Workstation Player` home screen, select your VM. See Figure 10.

#. Click :guilabel:`Play virtual machine`.

#. In |CL| you can install the bundle, and enable the tools, in your VM.

   .. code-block:: bash

      sudo swupd bundle-add os-cloudguest-vmware
      sudo systemctl enable --now open-vm-tools

More information is available on the `VMWare Tools Product Documentation`_
site.

Related topics
**************

For other guides on using the VMWare Player and ESXi, see:

* :ref:`vmw-player-preconf`
* :ref:`vmware-esxi-install-cl`
* :ref:`vmware-esxi-preconfigured-cl-image`

.. _VMware ESXi: https://www.vmware.com/products/esxi-and-esx.html

.. _VMware Workstation Player:
   https://www.vmware.com/products/workstation-player.html

.. _VMware Workstation Player Documentation:
   https://docs.vmware.com/en/VMware-Workstation-Player/index.html

.. _downloads: https://clearlinux.org/downloads

.. _VMWare Tools Product Documentation: https://docs.vmware.com/en/VMware-Tools/10.1.0/com.vmware.vsphere.vmwaretools.doc/GUID-8B6EA5B7-453B-48AA-92E5-DB7F061341D1.html
