.. _vmw-player:

|CL-ATTR| on VMware\* Workstation Player
########################################

This guide explains how to set up the VMware\* Workstation Player 15.5.1
hypervisor and instantiate a VM instance of |CL| by installing it using 
an ISO or using a pre-built image.

.. contents::
   :local:
   :depth: 1

Overview
********

`VMware Workstation Player`_ is a type 2 hypervisor. It runs on top of
Windows\* or Linux\* operating systems. With VMware Workstation Player, 
you can create, configure, manage, and run |CL-ATTR| 
:abbr:`VMs (Virtual Machines)` on your local system.

VMware offers a type 1 hypervisor called `VMware ESXi`_ designed for the
cloud environment. For information on how to install |CL| as guest OS on
it, see :ref:`vmware-esxi-install-cl`.

.. note::

   The screenshots in this document show the Windows version of the
   VMware Workstation Player 15.5.1. The menus and prompts are similar to those
   in other versions and for the Linux version, save some minor wording 
   differences.

Install the VMware Workstation Player hypervisor
************************************************

#. Enable Intel® Virtualization Technology (Intel® VT) and
   Intel® Virtualization Technology for Directed I/O (Intel® VT-d) in
   your system's BIOS.

#. `VMware Workstation Player`_ is available for Windows and Linux.
   Download your preferred version.

#. Install VMware Workstation Player by following the instructions
   appropriate for your system's OS:

   * On supported Linux distros:

     a. Ensure your Linux distro is running a GUI desktop.
     #. Start a terminal emulator.
     #. Start the installer by issuing the command below and follow the
        guided steps.

        .. code-block:: console

           sudo sh ./VMware-Player-<version number>.x86_64.bundle

   * On Windows:

     a. Start the installer.
     #. Follow the setup wizard.

For additional help, see the `VMware Workstation Player Documentation`_.

Create a blank VM
*****************

#. Start the ``VMware Workstation Player`` app.

#. On the home screen, click :guilabel:`Create a New Virtual Machine`. See
   Figure 1.

   .. rst-class:: dropshadow

   .. figure:: ../../_figures/vmw-player/vmw-player-01.png
      :scale: 100%
      :alt: VMware Workstation Player - Create a new virtual machine

      Figure 1: VMware Workstation Player - Create a new virtual
      machine

#. Select :guilabel:`I will install the operating system later`.

   .. rst-class:: dropshadow

   .. figure:: ../../_figures/vmw-player/vmw-player-02.png
      :scale: 100%
      :alt: I will install the operating system later.

      Figure 2: I will install the operating system later.

#. Click the :guilabel:`Next` button.

#. On the :guilabel:`Select a Guest Operating System` window, set the
   :guilabel:`Guest operating system` setting to :guilabel:`Linux`. See
   Figure 3.

   .. rst-class:: dropshadow

   .. figure:: ../../_figures/vmw-player/vmw-player-03.png
      :scale: 100%
      :alt: VMware Workstation Player - Select guest operating system type

      Figure 3: VMware Workstation Player - Select guest operating system
      type

#. Set the :guilabel:`Version` setting to
   :guilabel:`Other Linux 5.x or later kernel 64-bit`.

#. Click the :guilabel:`Next` button.

#. On the :guilabel:`Name the Virtual Machine` screen, name the new VM. See
   Figure 4.

   .. rst-class:: dropshadow

   .. figure:: ../../_figures/vmw-player/vmw-player-04.png
      :scale: 100%
      :alt: VMware Workstation Player - Name virtual machine

      Figure 4: VMware Workstation Player - Name virtual machine

#. Click the :guilabel:`Next` button.

#. On the :guilabel:`Specify Disk Capacity` screen, set the VM's maximum disk
   size. If you're planning to use a pre-built image, just use the default
   size for now. See Figure 5.

   .. rst-class:: dropshadow

   .. figure:: ../../_figures/vmw-player/vmw-player-05.png
      :scale: 100%
      :alt: VMware Workstation Player - Set disk capacity

      Figure 5: VMware Workstation Player - Set disk capacity

   .. note::

      For optimal performance with the |CL| Desktop image, we recommend 32GB
      of drive space. See :ref:`system-requirements` for more details.

#. Click the :guilabel:`Next` button.

#. On the :guilabel:`Ready to Create Virtual Machine` screen, click the
   :guilabel:`Customize Hardware...` button. See Figure 6.

   .. rst-class:: dropshadow

   .. figure:: ../../_figures/vmw-player/vmw-player-06.png
      :scale: 100%
      :alt: VMware Workstation Player - Customize hardware

      Figure 6: VMware Workstation Player - Customize hardware

#. Select :guilabel:`Memory` and set a desired value. See Figure 7.

   .. rst-class:: dropshadow

   .. figure:: ../../_figures/vmw-player/vmw-player-07.png
      :scale: 100%
      :alt: VMware Workstation Player - Set memory size

      Figure 7: VMware Workstation Player - Set memory size

   .. note::

      The |CL| live installer ISO needs a minimum of 1GB of RAM.
      After completing installation, |CL| can run on as little as
      128MB of RAM. Thus, you can reduce the memory size if needed.
      See :ref:`system-requirements` for more details.

#. Under the :guilabel:`Device` list, select :guilabel:`Processors`. See
   Figure 8.

   .. rst-class:: dropshadow

   .. figure:: ../../_figures/vmw-player/vmw-player-08.png
      :scale: 100%
      :alt: VMware Workstation Player - Set virtualization engine option

      Figure 8: VMware Workstation Player - Set virtualization engine
      option

#. Under :guilabel:`Processors` and :guilabel:`Number of processor cores`, 
   enter the desired number of cores. 

#. Under the :guilabel:`Virtualization engine` section,
   check the :guilabel:`Virtualize Intel VT-x/EPT or AMD-V/RVI` box.

#. Click the :guilabel:`Close` button.

#. Click the :guilabel:`Finish` button.

Enable UEFI boot support
************************

|CL| needs UEFI support to boot and work properly. To enable it:

#. Close the ``VMware Workstation Player`` app.

#. Add the following line to the end of your VM's :file:`.vmx` file.

   .. code-block:: console

      firmware = "efi"

   .. note::

      Depending on the OS, you can typically find the VMware VM files under:

        * On Linux distros: :file:`/home/username/vmware`
        * On Windows: :file:`C:\\Users\\username\\Documents\\Virtual Machines`
      
Instantiate |CL| 
****************

If you want to install |CL| from scratch, following the instructions
in the **Install |CL| using ISO** tab.  Otherwise, follow the 
**Use |CL| pre-built VMware image** tab to use our pre-built image.
 
.. tabs::

   .. tab:: Install |CL| using ISO 

      #. Navigate to the |CL| `Downloads`_ page and download either the ``Server``
         or ``Desktop`` ISO image.  After the download is complete, you will 
         attach this image.

      #. Start the ``VMware Workstation Player`` app.

      #. Select the VM that was created in section `Create a blank VM`_. 
         See Figure 9.

      #. Click :guilabel:`Edit virtual machine settings`.

         .. rst-class:: dropshadow

         .. figure:: ../../_figures/vmw-player/vmw-player-09.png
            :scale: 100%
            :alt: VMware Workstation Player - Edit virtual machine settings

            Figure 09: VMware Workstation Player - Edit virtual machine settings

      #. In the :guilabel:`Virtual Machine settings` window, 
         under :guilabel:`Hardware`, select guilabel:`CD/DVD (IDE)`.
         See Figure 10.

      #. Under :guilabel:`Connection` at the right, select 
         :guilabel:`Use ISO image file`. 

      #. Click :guilabel:`Browse` and select the 
         |CL| installer ISO. 
            
         .. rst-class:: dropshadow

         .. figure:: ../../_figures/vmw-player/vmw-player-10.png
            :scale: 100%
            :alt: VMware Workstation Player - Select |CL| installer ISO

            Figure 10: VMware Workstation Player - Select |CL| installer ISO   

      #. Click :guilabel:`OK` to close the :guilabel:`Virtual Machine settings`
         window.

      #. Start the VM by clicking :guilabel:`Play virtual machine`.

      #. Follow one of these guides to complete the installation of |CL|. 
         
         * *Desktop* version: :ref:`install-clr-desktop-start` 
         * *Server* version: :ref:`install-clr-server-start` 

      #. Reboot the VM after the installation completes.

      #. Install the ``os-cloudguest-vmware`` bundle, the open source
         VMware Tools for Linux\* guest operating systems, which enables
         new features and improves general performance.

         .. code-block:: bash

            sudo swupd bundle-add os-cloudguest-vmware
            sudo systemctl enable --now open-vm-tools

         More information is available on the `VMWare Tools Product Documentation`_
         site.

   .. tab:: Use |CL| pre-built VMWare image

      #. Navigate to the |CL| `Downloads`_ page and download the ``VMware`` 
         image. 

      #. Decompress the downloaded file and move it to the
         directory where your newly-created VM files reside.

         .. note::

            Depending on the OS, you can typically find the VMware VM
            files under:

            * Linux distros :file:`/home/username/vmware`
            * Windows :file:`C:\\Users\\username\\Documents\\Virtual Machines`

      #. Start the ``VMware Workstation Player`` app.

      #. Select the VM that was created in section `Create a blank VM`_. 
         See Figure 9.

      #. Click :guilabel:`Edit virtual machine settings`.

         .. rst-class:: dropshadow

         .. figure:: ../../_figures/vmw-player/vmw-player-09.png
            :scale: 100%
            :alt: VMware Workstation Player - Edit virtual machine settings

            Figure 9: VMware Workstation Player - Edit virtual machine settings

      #. Under :guilabel:`Hardware` and :guilabel:`Device` list, select 
         :guilabel:`Hard Disk (SCSI)`. See Figure 11.

         .. rst-class:: dropshadow

         .. figure:: ../../_figures/vmw-player/vmw-player-11.png
            :scale: 100%
            :alt: VMware Workstation Player - Remove hard drive

            Figure 11: VMware Workstation Player - Remove hard drive

      #. Click the :guilabel:`Remove` button.

      #. To add a new hard disk and attach the pre-built |CL| 
         VMware image, click the :guilabel:`Add` button. See Figure 12.

         .. rst-class:: dropshadow

         .. figure:: ../../_figures/vmw-player/vmw-player-12.png
            :scale: 100%
            :alt: VMware Workstation Player - Add new device

            Figure 12: VMware Workstation Player - Add new device

      #. Under the :guilabel:`Hardware types` section, select 
         :guilabel:`Hard Disk`. See Figure 13.

         .. rst-class:: dropshadow

         .. figure:: ../../_figures/vmw-player/vmw-player-13.png
            :scale: 100%
            :alt: VMware Workstation Player - Add hard drive

            Figure 13: VMware Workstation Player - Add hard drive

      #. Click the :guilabel:`Next` button.

      #. Select your preferred :guilabel:`Virtual disk type`. 
         See Figure 14.

         .. rst-class:: dropshadow

         .. figure:: ../../_figures/vmw-player/vmw-player-14.png
            :scale: 100%
            :alt: VMware Workstation Player - Select virtual disk type

         Figure 14: VMware Workstation Player - Select virtual disk type

      #. Select the :guilabel:`Use an existing virtual disk` option. 
         See Figure 15.

         .. rst-class:: dropshadow

         .. figure:: ../../_figures/vmw-player/vmw-player-15.png
            :scale: 100%
            :alt: VMware Workstation Player - Use existing virtual disk

            Figure 15: VMware Workstation Player - Use existing virtual disk

      #. Click the :guilabel:`Browse` button and select the
         pre-built |CL| VMware image file. See Figure 16.

         .. rst-class:: dropshadow

         .. figure:: ../../_figures/vmw-player/vmw-player-16.png
            :scale: 100%
            :alt: VMware Workstation Player - Select pre-built VMware |CL| image file

            Figure 16: VMware Workstation Player - Select pre-built VMware |CL| 
            image file

      #. Click the :guilabel:`Finish` button.

         .. note::

            When asked to convert the existing virtual disk to a newer format, 
            selecting either option works.

      #. Click the :guilabel:`OK` button. 

      #. Start the VM by clicking :guilabel:`Play virtual machine`.
 
         .. note::

            If you need to increase the disk size of the pre-built |CL| image, see
            :ref:`increase-virtual-disk-size`.

Related topics
**************

For other guides on using the VMWare Player and ESXi, see:

* :ref:`vmware-esxi-install-cl`

*Intel and the Intel logo are trademarks of Intel Corporation or its subsidiaries.*

.. _VMware ESXi: https://www.vmware.com/products/esxi-and-esx.html

.. _VMware Workstation Player:
   https://www.vmware.com/products/workstation-player.html

.. _VMware Workstation Player Documentation:
   https://docs.vmware.com/en/VMware-Workstation-Player/index.html

.. _Downloads: https://clearlinux.org/downloads

.. _VMWare Tools Product Documentation: https://docs.vmware.com/en/VMware-Tools/10.1.0/com.vmware.vsphere.vmwaretools.doc/GUID-8B6EA5B7-453B-48AA-92E5-DB7F061341D1.html
