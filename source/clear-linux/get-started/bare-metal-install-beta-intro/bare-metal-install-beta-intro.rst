.. _bare-metal-install-beta-intro: 

Install |CL-ATTR| with live install image
#########################################

The live install image allows you to boot the |CL| GNOME desktop and install 
|CL|. Access our |CL| image installer from the GNOME desktop and explore the power. 

First, prepare your environment: 

* Create a bootable :ref: `USB compatible with your OS on which you will 
  write the live install image <bootable-usb-beta-all>`. 

* `Download the live install image`_. [link img/dir or state filename]

Get started 
***********

After you've successfully downloaded and burned the live install image on a 
USB drive, follow these steps. 

#. Insert the USB drive into an available USB slot.

#. Power on the system.

#. Open the system BIOS setup menu by pressing the F2 key. 

   .. note:: 

   	  Your BIOS setup menu entry point may vary.

#. In the setup menu, enable the UEFI boot and set the USB drive as the
   first option in the device boot order.

#. Save these settings and exit.

	..TODO: We can clarify that "Reboot your OS where you plan to install." 

#. Reboot the target system.

#. The |CL| live install image will boot as shown in Figure 1. 

   .. figure:: figures/live-desktop-1.png
	  :scale: 50 %
	  :alt: The |CL| GNOME desktop

	  Figure 1: The |CL| GNOME desktop

#. Select the Activities menu in the upper left. 

#. Select the |CL| icon, **Install CLear Linux OS**, shown in Figure 2. 

   .. figure:: figures/live-desktop-2.png
	  :scale: 50 %
	  :alt: Install Clear Linux icon

	  Figure 2: Install Clear Linux icon

#. Upon selecting the |CL| icon, the installer user interface is 
   launched, as shown in Figure 3.

   .. figure:: figures/live-desktop-3.png
	  :scale: 50 %
	  :alt: Install Clear Linux icon

	  Figure 3: Install Clear Linux icon

#. Continue with installation by following :ref:`bare-metal-install-beta`


.. _Download the live install image here: https://download.clearlinux.org/image/
