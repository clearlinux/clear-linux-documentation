.. _vmw-player:

Install |CL-ATTR| as a VMware\* Workstation Player guest OS
###########################################################

`VMware Workstation 14 Player`_ is a type 2 hypervisor. It runs on top of
another operating system such as Windows\* or Linux\*. With VMware ESXi, you can
create, configure, manage, and run |CL-ATTR| :abbr:`VMs (Virtual Machines)` on
your local system.

This section shows how to create a new VM and install |CL| into it with the
VMware Workstation 14 Player hypervisor. Installing |CL| into a new VM
provides you flexibility when configuring the VM. You can configure the VM's
size, number of partitions, installed bundles, etc.

In this tutorial, we perform the following steps:

.. contents:: :local:
   :depth: 1

If you prefer to use a pre-configured |CL| VMware image instead,
see our :ref:`vmw-player-preconf` guide.

VMware offers a type 1 hypervisor called `VMware ESXi`_ designed for the
cloud environment. For information on how to install |CL| as guest OS on
it, see :ref:`vmware-esxi-install-cl`.

.. note::

   The screenshots on this document show the Windows version of the
   VMware Workstation 14 Player. The menus and prompts are similar to those
   in the Linux version save some minor wording differences.

Install the VMware Workstation Player hypervisor
************************************************

#. Enable :abbr:`Intel® VT (Intel® Virtualization Technology)` and
   :abbr:`Intel® VT-d (Intel® Virtualization Technology for Directed I/O)` in
   your system's BIOS.

#. `VMware Workstation 14 Player`_ is available for Windows and Linux.
   Download your preferred version.

#. Install VMware Workstation 14 Player following the instructions
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

Download the latest |CL| installer ISO
**************************************

Get the latest |CL| installer ISO image from the `image`_ repository.
Look for :file:`clear-[version number]-installer.iso.xz`.

Visit :ref:`image-types` for additional information about all available |CL| images.

.. include:: ../../guides/maintenance/download-verify-decompress-windows.rst
   :Start-after: verify-windows:

We also provide instructions for other operating systems:

* :ref:`download-verify-decompress-linux`
* :ref:`download-verify-decompress-mac`

Create and configure a new VM
*****************************

#. Start the `VMware Workstation Player` app.

#. On the home screen, click :guilabel:`Create a New Virtual Machine`. See
   Figure 1.

   .. figure:: figures/vmw-player/vmw-player-01.png
      :scale: 100%
      :alt: VMware Workstation 14 Player - Create a new virtual machine

      Figure 1: VMware Workstation 14 Player - Create a new virtual
      machine

#. On the :guilabel:`Welcome to the New Virtual Machine Wizard` screen,
   select the :guilabel:`Installer disc image file (iso)` option.
   See Figure 2.

   .. figure:: figures/vmw-player/vmw-player-02.png
      :scale: 100%
      :alt: VMware Workstation 14 Player - Select |CL| installer ISO

      Figure 2: VMware Workstation 14 Player - Select |CL| installer ISO

#. Click the :guilabel:`Browse` button and select the decompressed |CL|
   installer ISO.

#. Click the :guilabel:`Next` button.

#. On the :guilabel:`Select a Guest Operating System`, set the
   :guilabel:`Guest operating system` setting to :guilabel:`Linux`. See
   Figure 3.

   .. figure:: figures/vmw-player/vmw-player-03.png
      :scale: 100%
      :alt: VMware Workstation 14 Player - Select guest operating system type

      Figure 3: VMware Workstation 14 Player - Select guest operating system
      type

#. Set the :guilabel:`Version` setting to
   :guilabel:`Other Linux 3.x or later kernel 64-bit`.

#. Click the :guilabel:`Next` button.

#. On the :guilabel:`Name the Virtual Machine` screen, name the new VM. See
   Figure 4.

   .. figure:: figures/vmw-player/vmw-player-04.png
      :scale: 100%
      :alt: VMware Workstation 14 Player - Name virtual machine

      Figure 4: VMware Workstation 14 Player - Name virtual machine

#. Click the :guilabel:`Next` button.

#. On the :guilabel:`Specify Disk Capacity` screen, set the VM's maximum disk
   size. See Figure 5.

   .. figure:: figures/vmw-player/vmw-player-05.png
      :scale: 100%
      :alt: VMware Workstation 14 Player - Set disk capacity

      Figure 5: VMware Workstation 14 Player - Set disk capacity

   .. note::
      A minimal |CL| installation can exist on 600MB of drive space.
      See :ref:`system-requirements` for more details.

#. Click the :guilabel:`Next` button.

#. On the :guilabel:`Ready to Create Virtual Machine` screen, click the
   :guilabel:`Customize Hardware...` button. See Figure 6.

   .. figure:: figures/vmw-player/vmw-player-06.png
      :scale: 100%
      :alt: VMware Workstation 14 Player - Customize hardware

      Figure 6: VMware Workstation 14 Player - Customize hardware

#. Select :guilabel:`Memory` and set the size to 2GB. See Figure 7.

   .. figure:: figures/vmw-player/vmw-player-07.png
      :scale: 100%
      :alt: VMware Workstation 14 Player - Set memory size

      Figure 7: VMware Workstation 14 Player - Set memory size

   .. note::
      The |CL| installer ISO needs a minimum of 2GB of RAM.
      After completing installation, |CL| can run on as little as
      128MB of RAM. Thus, you can reduce the memory size if needed.
      See :ref:`system-requirements` for more details.

#. Under the :guilabel:`Device` list, select :guilabel:`Processors`. See
   Figure 8.

   .. figure:: figures/vmw-player/vmw-player-08.png
      :scale: 100%
      :alt: VMware Workstation 14 Player - Set virtualization engine option

      Figure 8: VMware Workstation 14 Player - Set virtualization engine
      option

#. Under the :guilabel:`Virtualization engine` section,
   check :guilabel:`Virtualize Intel VT-x/EPT or AMD-V/RVI`.

#. Click the :guilabel:`Close` button.

#. Click the :guilabel:`Finish` button.

Install |CL| into the new VM
****************************

#. Select the newly-created VM and click the :guilabel:`Play virtual machine`
   button. See Figure 9.

   .. figure:: figures/vmw-player/vmw-player-09.png
      :scale: 100%
      :alt: VMware Workstation 14 Player - Power on virtual machine

      Figure 9: VMware Workstation 14 Player - Power on virtual machine

#. Follow the :ref:`install-on-target-start` guide to complete the
   installation of |CL|.

#. After the installation completes, reboot the VM. This reboot restarts the
   |CL| installer.

Detach the |CL| installer ISO from the VM
*****************************************

#. To enable the mouse pointer so you access VMware Workstation Player's
   menus, press :kbd:`<CTRL>` + :kbd:`<ALT>` on the keyboard.

#. To disconnect the CD/DVD to stop it from booting the |CL| installer ISO
   again, click the :guilabel:`Player` menu. See Figure 10.

   .. figure:: figures/vmw-player/vmw-player-10.png
      :scale: 100%
      :alt: VMware Workstation 14 Player - Edit CD/DVD settings

      Figure 10: VMware Workstation 14 Player - Edit CD/DVD settings

#. Go to :menuselection:`Removable Devices-->CD/DVD (IDE)-->Settings`.

#. On the :guilabel:`Device status` section, uncheck the
   :guilabel:`Connected` and the :guilabel:`Connect at power on` settings.
   See Figure 11.

   .. figure:: figures/vmw-player/vmw-player-11.png
      :scale: 100%
      :alt: VMware Workstation 14 Player - Disconnect CD/DVD

      Figure 11: VMware Workstation 14 Player - Disconnect CD/DVD

#. Click the :guilabel:`OK` button.

#. To power off the VM, click the :guilabel:`Player` menu. See Figure 12.

   .. figure:: figures/vmw-player/vmw-player-12.png
      :scale: 100%
      :alt: VMware Workstation 14 Player - Power off virtual machine

      Figure 12: VMware Workstation 14 Player - Power off virtual machine

#. Go to :guilabel:`Power` and select :guilabel:`Shut Down Guest`.

Enable UEFI boot support
************************

|CL| needs UEFI support to boot. To enable UEFI, add the
following line to the end of your VM's :file:`.vmx` file:

.. code-block:: console

   firmware = "efi"

.. note::

   Depending on the OS, you can typically find the VMware VM files under:

   * On Linux distros: :file:`/home/username/vmware`
   * On Windows: :file:`C:\\Users\\username\\Documents\\Virtual Machines`

Power on the VM
***************

After configuring the settings above, power on your |CL| virtual machine.

#. On the :guilabel:`VMware Workstation Player` home screen, select your 
   VM. See Figure 13.

   .. figure:: figures/vmw-player/vmw-player-13.png
      :scale: 100%
      :alt: VMware Workstation 14 Player - Power on virtual machine

      Figure 13: VMware Workstation 14 Player - Power on virtual machine

#. Click :guilabel:`Play virtual machine`.

Related topics
**************

For other guides on using the VMWare Player and ESXi, see:

* :ref:`vmw-player-preconf`
* :ref:`vmware-esxi-install-cl`
* :ref:`vmware-esxi-preconfigured-cl-image`

.. _VMware ESXi: https://www.vmware.com/products/esxi-and-esx.html

.. _VMware Workstation 14 Player:
   https://www.vmware.com/products/workstation-player.html

.. _VMware Workstation Player Documentation:
   https://docs.vmware.com/en/VMware-Workstation-Player/index.html

.. _image: https://cdn.download.clearlinux.org/image
