.. _parallels:

Run |CL-ATTR| as a Parallels\* guest OS
#######################################

Parallels Desktop for Mac is virtualization software that allows other operating
systems, such as Linux, to run side-by-side with macOS.

This tutorial shows how to run |CL| Server as a guest OS in Parallels Desktop 14.

Prerequisites
*************

* Parallels Desktop 14 installed on macOS.

Download ISO
************

#. Download the live-server ISO installer from https://clearlinux.org/downloads.
   This tutorial uses |CL| Server 30140 as its example.

#. Unzip the ISO:

   .. code-block:: bash

	  gunzip clear-30140-live-server.iso.xz

Initialize new VM
*****************

Start Parallels and initialize your VM:

#. Go to :menuselection:`File --> New`.

#. In the opening dialog window, select
   :guilabel:`Install Windows or another OS from a DVD or image` then click
   :guilabel:`Continue`. (See figure 1.)

   .. figure:: ../figures/parallels-01.png
	  :alt: Parallels opening dialog

	  Figure 1: Parallels opening dialog

#. On the next screen, select :guilabel:`Image File` and then click
   :guilabel:`Select a file...`. (See figure 2.)

   .. figure:: ../figures/parallels-02.png
	  :alt: Dialog to select source for VM

	  Figure 2: Dialog to select source for VM

#. Select your ISO file. You will see a warning "Unable to detect operating
   system" as shown in figure 3. This is ok. Click :guilabel:`Continue`.

   .. figure:: ../figures/parallels-03.png
	  :alt: Warning that OS is not detected

	  Figure 3: Warning that OS is not detected

#. Next you will be prompted to select your OS, as shown in figure 4. Select
   :menuselection:`More Linux --> Other Linux` from the dropdown and click
   :guilabel:`Continue`.

   .. figure:: ../figures/parallels-04.png
	  :alt: Select OS from dropdown

	  Figure 4: Select OS from dropdown

#. Name your VM and check :guilabel:`Customize settings before installation`.
   (See figure 5.)

   .. figure:: ../figures/parallels-05.png
   	  :alt: Name and Location screen

	  Figure 5: Name and Location screen

#. Click :guilabel:`Create`.

#. The Configuration window for the new VM will open, as shown in figure 6.
   Select :menuselection:`Hardware --> Boot Order`.

   .. figure:: ../figures/parallels-06.png
   	  :alt: VM Configuration window

	  Figure 6: VM Configuration window

#. Expand :guilabel:`Advanced Settings`. Set “BIOS” type to “EFI-64” and enter
   “vm.bios.efi=1” under :guilabel:`Boot flags:`. (See figure 7.)

   .. figure:: ../figures/parallels-07.png
   	  :alt: Advanced configuration settings

	  Figure 7: Advanced configuration settings

#. Close the Configuration window.

#. Click :guilabel:`Continue`.

#. If you encounter camera and microphone access restriction warnings, ignore
   them.

Install |CL| on VM
******************

#. Follow the prompts and install |CL| using the text-based installer as shown
   in figure 8.

   Refer to :ref:`bare-metal-install-server` for additional installation
   instructions.

   .. figure:: ../figures/parallels-08.png
   	  :alt: On screen instructions from text-based installer

	  Figure 8: On screen instructions from text-based installer

#. After installation, reboot the VM. You will be prompted to log in, as shown
   in figure 9.

   .. figure:: ../figures/parallels-09.png
   	  :alt: Log in prompt

	  Figure 9: Log in prompt


Congratulations! You have successfully set up a |CL| VM with Parallels!
