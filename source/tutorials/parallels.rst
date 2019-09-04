.. _parallels:

Parallels\* Desktop for Mac\*
#############################

This tutorial describes how to run |CL| Server in
:abbr:`CLI (command-line interface)` mode as a guest OS in Parallels Desktop 14
for Mac.

Parallels Desktop for Mac is virtualization software that allows other
operating systems, such as Linux, to run side-by-side with macOS\*.

Prerequisites
*************

* Install Parallels Desktop 14 for Mac.

Download ISO image
******************

#. Download a live-server ISO installation file from https://clearlinux.org/downloads.
   This tutorial uses |CL| Server 30140 as its example.

#. Unzip the ISO image with the command:

   .. code-block:: bash

	  gunzip clear-30140-live-server.iso.xz

Initialize new VM
*****************

Start Parallels and initialize your :abbr:`VM (Virtual Machine)` with the
following steps.

#. Go to :menuselection:`File > New`.

#. In the opening dialog window, select
   :guilabel:`Install Windows or another OS from a DVD or image`, then click
   :guilabel:`Continue`. (See Figure 1.)

   .. figure:: /_figures/parallels/parallels-01.png
	  :alt: Parallels opening dialog

	  Figure 1: Parallels opening dialog

#. On the next screen, select :guilabel:`Image File`, then click
   :guilabel:`Select a file...` as shown in Figure 2.

   .. figure:: /_figures/parallels/parallels-02.png
	  :alt: Dialog to select source for VM

	  Figure 2: Dialog to select source for VM

#. Select your ISO file. The system displays the warning message "Unable to
   detect operating system", as shown in Figure 3. This message is expected and
   can be ignored. Click :guilabel:`Continue`.

   .. figure:: /_figures/parallels/parallels-03.png
	  :alt: Warning that OS is not detected

	  Figure 3: Warning that OS is not detected

#. You are prompted to select your OS, as shown in Figure 4. Select
   :menuselection:`More Linux > Other Linux` from the drop-down menu and click
   :guilabel:`Continue`.

   .. figure:: /_figures/parallels/parallels-04.png
	  :alt: Select OS from drop-down menu

	  Figure 4: Select OS from drop-down menu

#. Name your VM and check :guilabel:`Customize settings before installation`.
   (See Figure 5.)

   .. figure:: /_figures/parallels/parallels-05.png
   	  :alt: Name and Location screen

	  Figure 5: Name and Location screen

#. Click :guilabel:`Create`. The Configuration window for the new VM opens, as
   shown in Figure 6.

   Select :menuselection:`Hardware > Boot Order`.

   .. figure:: /_figures/parallels/parallels-06.png
   	  :alt: VM Configuration window

	  Figure 6: VM Configuration window

#. Expand :guilabel:`Advanced Settings`. Set :guilabel:`BIOS` to “EFI 64-bit”
   and in the :guilabel:`Boot flags` field, enter “vm.bios.efi=1” as shown in
   Figure 7.

   .. figure:: /_figures/parallels/parallels-07.png
   	  :alt: Advanced configuration settings

	  Figure 7: Advanced configuration settings

#. Close the Configuration window and click :guilabel:`Continue`.

   If camera and microphone access restriction warnings are displayed, you can
   ignore them.

Install |CL| on VM
******************

#. Follow the prompts and install |CL| using the text-based installer as shown
   in Figure 8.

   Refer to :ref:`bare-metal-install-server` for additional installation
   instructions.

   .. figure:: /_figures/parallels/parallels-08.png
   	  :alt: On screen instructions from text-based installer

	  Figure 8: On screen instructions from text-based installer

#. After installation, reboot the VM. You are prompted to log in, as shown
   in Figure 9. Log in with the credentials you used when you installed |CL|
   on the VM.

   .. figure:: /_figures/parallels/parallels-09.png
   	  :alt: Log in prompt

	  Figure 9: Log in prompt


Congratulations! You have successfully set up a |CL| VM using Parallels
Desktop for Mac.
