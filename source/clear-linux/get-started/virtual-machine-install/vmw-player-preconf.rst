.. _vmw-player-preconf:

Run pre-configured |CL-ATTR| image as a VMware\* Workstation Player guest OS
##############################################################################

`VMware Workstation 14 Player`_ is a type 2 hypervisor. It runs on top of
another operating system such as Windows\* or Linux\*. With VMware ESXi, you
can create, configure, manage, and run |CL-ATTR| :abbr:`VMs (Virtual Machines)`
on your local system.

This section shows how to deploy a pre-configured |CL| VMware image on
VMware Workstation 14 Player.

In this tutorial, we perform the following steps:

#. Install the VMware Workstation Player hypervisor
#. Download the latest |CL| pre-configured image
#. VMware image Verify the integrity of the |CL| image
#. Uncompress the |CL| image
#. Create and configure a new VM
#. Attach the pre-configured VMware |CL| image
#. Enable EFI boot support
#. Power on the VM

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

#. Depending on which OS you're running, install it by following one of these
   instructions:

   * On supported Linux distros:

     #. Enable a GUI desktop.

     #. Start a terminal emulator.

     #. Start the installer by issuing the command below and following the
        guided steps.

        .. code-block:: bash

           sudo sh ./VMware-Player-[version number].x86_64.bundle

   * On Windows:

     #. Start the installer.
     #. Follow the setup wizard.

For additional help, see the `VMware Workstation Player guide`_.

|CL| image types
****************

.. include:: ../../reference/image-types.rst
   :Start-after: image-types-content:

Download the latest |CL| VMware image
*************************************

Get the latest |CL| VMware image from the `image`_ repository.
Look for :file:`clear-[version number]-vmware.vmdk.xz`. You can also use
this command: 

.. code-block:: bash

   curl -O https://download.clearlinux.org/image/clear-$(curl https://download.clearlinux.org/latest)-vmware.vmdk.xz

.. include:: ../../guides/maintenance/download-verify-uncompress-windows.rst
   :Start-after: verify-windows:

We also provide instructions for other operating systems:

* :ref:`download-verify-uncompress-linux`
* :ref:`download-verify-uncompress-mac`

Create and configure a new VM
*****************************

#. Start the `VMware Workstation Player` app.
#. On the home screen, click :guilabel:`Create a New Virtual Machine`. See
   figure 1.

   .. figure:: figures/vmw-player-preconf/vmw-player-preconf-01.png
      :scale: 100%
      :alt: VMware Workstation 14 Player - Create a new virtual machine

      Figure 1: VMware Workstation 14 Player - Create a new virtual machine

#. On the :guilabel:`Welcome to the New Virtual Machine Wizard` screen,
   select the :guilabel:`I will install the operating system later` option.
   See figure 2.

   .. figure:: figures/vmw-player-preconf/vmw-player-preconf-02.png
      :scale: 100%
      :alt: VMware Workstation 14 Player - Select install operating system

      Figure 2: VMware Workstation 14 Player - Select install operating
      system later.

#. Click the :guilabel:`Next` button.

#. On the :guilabel:`Select a Guest Operating System` screen, set the
   :guilabel:`Guest operating system` setting to :guilabel:`Linux`.
   See figure 3.

   .. figure:: figures/vmw-player-preconf/vmw-player-preconf-03.png
      :scale: 100%
      :alt: VMware Workstation 14 Player - Select guest operating system type

      Figure 3: VMware Workstation 14 Player - Select guest operating system
      type

#. Set :guilabel:`Version` setting to
   :guilabel:`Other Linux 3.x or later kernel 64-bit`.

#. Click the :guilabel:`Next` button.

#. On the :guilabel:`Name the Virtual Machine` screen, give your new VM a
   name. See figure 4.

   .. figure:: figures/vmw-player-preconf/vmw-player-preconf-04.png
      :scale: 100%
      :alt: VMware Workstation 14 Player - Name virtual machine

      Figure 4: VMware Workstation 14 Player - Name virtual machine

#. Click the :guilabel:`Next` button.

#. On the :guilabel:`Specify Disk Capacity` screen, click 
   the :guilabel:`Next` button. Keep the default disk settings unchanged.
   When we attach the pre-configured |CL| VMware image, we will remove the
   default virtual disk and replace it with the pre-configured one. See
   figure 5.

   .. figure:: figures/vmw-player-preconf/vmw-player-preconf-05.png
      :scale: 100%
      :alt: VMware Workstation 14 Player - Set disk capacity

      Figure 5: VMware Workstation 14 Player - Set disk capacity

#. On the :guilabel:`Ready to Create Virtual Machine` screen, click the
   :guilabel:`Customize Hardware...` button. See figure 6.

   .. figure:: figures/vmw-player-preconf/vmw-player-preconf-06.png
      :scale: 100%
      :alt: VMware Workstation 14 Player - Customize hardware

      Figure 6: VMware Workstation 14 Player - Customize hardware

#. Under the :guilabel:`Device` list, select :guilabel:`Processors`. See
   figure 7.

   .. figure:: figures/vmw-player-preconf/vmw-player-preconf-07.png
      :scale: 100%
      :alt: VMware Workstation 14 Player - Set virtualization engine option

      Figure 7: VMware Workstation 14 Player - Set virtualization engine
      option

#. Under the :guilabel:`Virtualization engine` section,
   check :guilabel:`Virtualize Intel VT-x/EPT or AMD-V/RVI`.

#. To disconnect the virtual CD/DVD (IDE) since it is not needed, under the
   :guilabel:`Device` list, select :guilabel:`New CD/DVD (IDE)`. See figure 8.

   .. figure:: figures/vmw-player-preconf/vmw-player-preconf-08.png
      :scale: 100%
      :alt: VMware Workstation 14 Player - Disconnect CD/DVD (IDE)

      Figure 8: VMware Workstation 14 Player - Disconnect CD/DVD (IDE)

#. Under the :guilabel:`Device status` section, uncheck
   :guilabel:`Connect at power on`.

#. Click the :guilabel:`Close` button.

#. Click the :guilabel:`Finish` button.

Attach the pre-configured |CL| VMware image
*******************************************

#. Move the downloaded and uncompressed pre-configured |CL| VMware image file
   :file:`clear-[version number]-basic.vmdk` to the directory where your
   newly-created VM resides.

   .. note::

      Depending on the OS, you can typically find the VMware VM files under:

      * On Linux distros: :file:`/home/username/vmware`
      * On Windows: :file:`C:\Users\username\Documents\Virtual Machines`

#. On the :guilabel:`VMware Workstation Player` home screen, select your 
   newly-created VM. See figure 9.

   .. figure:: figures/vmw-player-preconf/vmw-player-preconf-09.png
      :scale: 100%
      :alt: VMware Workstation 14 Player - Edit virtual machine settings

      Figure 9: VMware Workstation 14 Player - Edit virtual machine settings

#. Click :guilabel:`Edit virtual machine settings`.

#. To remove the default hard disk, under the :guilabel:`Device` list, select
   :guilabel:`Hard Disk (SCSI)`. See figure 10.

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

Enable UEFI boot support
************************

|CL| needs UEFI support to boot.To enable it, add the
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
   VM. See figure 15.

   .. figure:: figures/vmw-player-preconf/vmw-player-preconf-15.png
      :scale: 100%
      :alt: VMware Workstation 14 Player - Power on virtual machine

      Figure 15: VMware Workstation 14 Player - Power on virtual machine

#. Click :guilabel:`Play virtual machine`.

For other guides on using the VMWare Player and ESXi, see:

* :ref:`vmw-player`
* :ref:`vmware-esxi-install-cl`
* :ref:`vmware-esxi-preconfigured-cl-image`

.. _VMware ESXi: https://www.vmware.com/products/esxi-and-esx.html
.. _VMware Workstation 14 Player: https://www.vmware.com/products/workstation-player.html
.. _VMware Workstation Player guide: https://docs.vmware.com/en/VMware-Workstation-Player/index.html
.. _latest: https://download.clearlinux.org/image/
.. _image: https://download.clearlinux.org/image




