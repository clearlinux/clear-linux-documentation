.. _virtualbox-cl-installer:

|CL-ATTR| on VirtualBox\*
#########################

This page explains how to create a virtual machine on the `VirtualBox`_
hypervisor with |CL-ATTR| as the guest operating system. These instructions
support the |CL| live-server installer to create the |CL| virtual machine (VM).

.. contents::
   :local:
   :depth: 1

Prerequisites
*************

#. Enable virtualization, such as `Intel® Virtualization Technology <https://www.intel.com/content/www/us/en/virtualization/virtualization-technology/intel-virtualization-technology.html>`_
   (Intel® VT), on the host system from EFI/BIOS.

#. Download and install |VB| **version 6.0 or later** from
   `VirtualBox`_ using the  `VirtualBox Installation Instructions`_ for your
   platform.

Download and extract the |CL| installer ISO
*******************************************

#. Download the :file:`clear-<VERSION>-live-server.iso.xz` of
   |CL| on the `Downloads`_ page.

#. Validate the integrity of the downloaded image by checking the file hash
   and signatures. Refer to :ref:`validate-signatures` for detailed steps.

#. Decompress the downloaded image.

   - On Windows, you can use `7zip`_ to extract the file by right-clicking the
     file to *Extract Here* (in the same directory)

   .. figure:: figures/vbox/virtualbox-cl-installer-01.png
      :scale: 100%
      :alt: 7zip extract here command

      Figure 1: 7zip extract here command

   - On Linux :

     .. code-block:: bash

        xz -d clear-<VERSION>-live-server.iso.xz

#. Delete the originally downloaded compressed file.

Create a new |VB| virtual machine
*********************************

A new :abbr:`VM (Virtual Machine)` needs to be created in |VBM| where |CL|
will be installed. General instructions for creating a virtual machine and
details about using different settings are available in the VirtualBox manual section `Creating Your First Virtual Machine`_.

#. Launch the |VBM| from your host system.

#. Click the :guilabel:`New` button to create a new VM.

#. Choose :guilabel:`Expert mode`.

#. On the :guilabel:`Create Virtual Machine` screen, enter the following settings:

   - **Name**: Choose name (e.g. ClearLinuxOS-VM).
   - **Type**: Linux
   - **Version**: **Linux 2.6 / 3.x / 4.x (64-bit)**
   - **Hard disk**: `Create a virtual hard disk now`
   - **Memory size default**: 2048 MB (Adjust appropriately.)

     .. note::
        Later, if you want to change the amount of RAM allocated, power down your VM. Return to :file:`Settings > System` and change
        :guilabel:`Base Memory` to the desired size.

   .. figure:: figures/vbox/virtualbox-cl-installer-02.png
      :scale: 100%
      :alt: Create Virtual Machine

      Figure 2: Create Virtual Machine

#. Click :guilabel:`Create`.

#. On the :guilabel:`Create Virtual Hard Disk` screen, select:

   - **File location**
   - **File size**: **32.00 GB**. Adjust size to your needs.
   - **Hard disk file type**: `VDI (VirtualBox Disk Image)`
   - **Storage on physical hard disk**: `Dynamically allocated`

   .. figure:: figures/vbox/virtualbox-cl-installer-03.png
      :scale: 100%
      :alt: Create Virtual Hard Disk

      Figure 3: Create Virtual Hard Disk

#. Click :guilabel:`Create`.

   A new virtual machine will be created and appear in the |VBM|.

#. Click :guilabel:`Settings` to configure the |CL| VM.

#. In the left-hand menu, navigate to the :menuselection:`System` menu.

#. On the :guilabel:`Motherboard` tab, select the :guilabel:`Chipset` menu, and
   then select :menuselection:`ICH9`. See Figure 4.

   .. note::

      You can select which chipset will be presented to the virtual machine.
      Consult the `VM VirtualBox User Manual`_ for more details.

#. In :guilabel:`Enabled Features`, check these boxes:

   - **Enable I/O APIC**
   - **Enable EFI (special OSes only)**

   .. figure:: figures/vbox/virtualbox-cl-installer-04.png
      :scale: 100%
      :alt: Settings > System

      Figure 4: Settings > System

   .. note::

      By default, only 1 virtual CPU is allocated to the new VM. Consider
      increasing the number of virtual processors allocated to the virtual
      machine under Settings > System > Processor for increased
      performance.

#. Click :guilabel:`OK`.

Install |CL| on the |VB| VM
***************************

|CL| is ready to be installed.

Mount the installation ISO
==========================

The |CL| installer ISO needs to be mounted as a virtual CD-ROM on the VM
before powering the VM on.

#. From the *ClearLinux-OS* :guilabel:`Settings` menu at left, select
   :guilabel:`Storage`.

#. From :guilabel:`Storage Devices`, middle column, click the blue
   disk labeled :guilabel:`Empty`.

#. From the :guilabel:`Attributes` menu, click the blue CD disk next to
   the :guilabel:`Optical Drive` drop down menu and click
   :guilabel:`Choose Virtual Optical Disk File...`

   .. figure:: figures/vbox/virtualbox-cl-installer-05.png
      :scale: 100%
      :alt: Choose Virtual Optical Disk Drive

      Figure 5: Choose Virtual Optical Disk Drive

#. Where there appears :guilabel:`Please choose a virtual optical disk file`,
   select the ISO file and click *Open*.

   .. figure:: figures/vbox/virtualbox-cl-installer-06.png
      :scale: 100%
      :alt: Mounting an ISO

      Figure 6: Mounting an ISO

#. Click :guilabel:`OK` to exit and return to the main |VBM|.

Install |CL| with live-server installer
=======================================

#. In the |VBM|, select virtual machine you created and click :guilabel:`Start`.

   .. figure:: figures/vbox/virtualbox-cl-installer-07.png
      :scale: 100%
      :alt: Start the installer

      Figure 7: Start the installer

   .. note::

      To release the mouse cursor from the VM console window, press the right
      :kbd:`Ctrl` key on the keyboard.

#. When :guilabel:`Clear Linux Installer` in boot manager appears,
   select :kbd:`Enter`. Do not install the bundle `desktop-autostart`.

#. Follow the steps in :ref:`bare-metal-install-server` to
   install |CL| onto the VM virtual disk. Note:

   #. In :guilabel:`Configure Installation Media`, navigate top
      VBOX HARDDISK, and then select :guilabel:`Confirm`.

   #. In :menuselection:`Advanced options --> Manage User`, create an
      administrative user.

   #. Do not install the bundle `desktop-autostart`.

#. When |CL| installation is complete, click :guilabel:`Exit`.

#. At the prompt, enter:

   .. code-block:: bash

      shutdown now

Unmount the ISO
===============

The |CL| installer ISO needs to be unmounted to allow the VM to boot from the
virtual hard disk.

#. Return to the |VBM|.

#. Click :guilabel:`Settings` to configure the |CL| VM.

#. From the VM :guilabel:`Settings` window, navigate to the :guilabel:`Storage`
   pane in the left menu.

#. From the middle :guilabel:`Storage Devices` column, click the blue CD disk
   labeled :guilabel:`clear-<VERSION>-live-server.iso` under the
   :guilabel:`Controller: IDE`.

#. From the :guilabel:`Attributes` column on the right, in :guilabel:`Optical Drive`,
   select the blue CD icon beside and click
   :guilabel:`Remove Disk from Virtual Drive`.

   .. figure:: figures/vbox/virtualbox-cl-installer-08.png
      :scale: 100%
      :alt: Remove Disk from Virtual Drive

      Figure 8: Remove Disk from Virtual Drive

#. Click :guilabel:`OK` to exit the :guilabel:`VM Settings` menu and return to
   the main |VBM|.

Install |VB| Linux Guest Additions
==================================

|CL| provides Linux Guest Additions drivers for full compatibility using an
install script in the **kernel-lts** (Long Term Support) bundle by |CL|.

#. From the |VBM| select the |CL| VM, and select :guilabel:`Start`.

#. In the VM Console, log in as the administrative user previously created.

   .. note::
      A message may appear: "A kernel update is available: you may wish
      to reboot the system."

      To update the kernel, enter:

      .. code-block:: bash

          sudo reboot

      At initial login, enter the administrative user's password and continue.

#. Validate the installed kernel is **kernel-lts** by checking the output
   of the :command:`uname -r` command. It should end in **.lts** or **.lts2018**.

   .. code-block:: bash

      uname -r
      <VERSION>.lts

   If the running kernel is not **lts**: install the LTS kernel manually,
   update the bootloader, and check again:

   .. code-block:: bash

      sudo swupd bundle-add kernel-lts
      clr-boot-manager set-kernel $(basename $(realpath /usr/lib/kernel/default-lts))
      clr-boot-manager update
      reboot

#. Remove any kernel bundles that do not end in *-lts* or *kernel-install*
   to simplify and avoid conflicts:

   .. code-block:: bash

      sudo swupd bundle-list | grep kernel
      sudo swupd bundle-remove <NON-LTS-KERNEL>

#. In the VM Console top menu, click :guilabel:`Devices`, and select
   :guilabel:`Insert Guest Additions CD image...` to mount the |VB| driver
   installation to the |CL| VM.

   .. figure:: figures/vbox/virtualbox-cl-installer-09.png
      :scale: 100%
      :alt: Insert Guest Additions CD image

      Figure 9: Insert Guest Additions CD image

#. If a dialogue appears, "VBx_GAs_6.0.8... Would you like to run it?",
   select :guilabel:`Cancel`.

   Instead, we provide a script to patch and install |VB| drivers on |CL|.

#. Open a Terminal and enter the script:

   .. code-block:: bash

      sudo install-vbox-lga

   .. note::

      Successful installation shows: "Guest Additions installation complete".
      If drivers are already installed, don't re-install them.

#. Shut down the system. Select :menuselection:`Machine --> ACPI Shutdown`.

   .. figure:: figures/vbox/virtualbox-cl-installer-10.png
      :scale: 100%
      :alt: Powering off a VirtualBox VM

      Figure 10: Powering off a VirtualBox VM

#. Select :guilabel:`Settings`, :guilabel:`Display`.

#. In :guilabel:`Graphics Controller`, select :guilabel:`VBoxSVGA`
   to adjust screen size dynamically.

   .. figure:: figures/vbox/virtualbox-cl-installer-11.png
      :scale: 100%
      :alt: Remove Disk from Virtual Drive

      Figure 11: VirtualBox hardware acceleration error

#. In the |VBM|, select :guilabel:`Start`.

#. In the VM console, login and verify the |VB| drivers are loaded:

   .. code-block:: bash

      lsmod | grep ^vbox

   You should see drivers loaded with names beginning with **vbox**:
   (e.g., vboxvideo, vboxguest).

#. Add `desktop-autostart` for a full desktop experience.

   .. code-block:: bash

      sudo swupd bundle-add desktop-autostart

#. Reboot the VM and log in with the administrative user.

   .. code-block:: bash

      sudo reboot

The |CL| VM running on |VB| is ready to develop and explore.

Troubleshooting
***************

#. **Problem:** On a Microsoft\* Windows\* OS, |VB| encounters an error when
   trying to start a VM indicating *VT-X/AMD-v hardware acceleration is not
   available on your system.*

   .. figure:: figures/vbox/virtualbox-cl-installer-12.png
      :scale: 100%
      :alt: Remove Disk from Virtual Drive

      Figure 12: VirtualBox hardware acceleration error

   **Solution:** First, double check the `Prerequisites`_ section to make
   sure *Hardware accelerated virtualization* extensions have been enabled
   in the host system's EFI/BIOS.

   *Hardware accelerated virtualization*, may get disabled for |VB| when
   another hypervisor, such as *Hyper-V* is enabled.

   To disable *Hyper-V* execute this command in an
   **Administrator: Command Prompt or Powershell**, and reboot the system:

   .. code-block:: bash

      bcdedit /set {current} hypervisorlaunchtype off

   To enable Hyper-V again, execute this command in an
   **Administrator: Command Prompt or Powershell**, and reboot the system:

   .. code-block:: bash

      bcdedit /set {current} hypervisorlaunchtype Auto


*Intel and the Intel logo are trademarks of Intel Corporation or its subsidiaries.*

.. _VirtualBox Installation Instructions: https://www.virtualbox.org/manual/ch02.html

.. _VirtualBox: https://www.virtualbox.org

.. _Downloads: https://clearlinux.org/downloads

.. _`Creating Your First Virtual Machine`: https://www.virtualbox.org/manual/UserManual.html#gui-createvm

.. _7zip: http://www.7-zip.org/

.. _Intel® Virtualization Technology: https://www.intel.com/content/www/us/en/virtualization/virtualization-technology/intel-virtualization-technology.html

.. _VM VirtualBox User Manual: https://docs.oracle.com/cd/E97728_01/E97727/html/settings-system.html