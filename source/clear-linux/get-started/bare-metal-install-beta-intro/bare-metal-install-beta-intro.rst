.. _bare-metal-install-beta-intro: 

Boot the |CL-ATTR| live install image
#####################################

The live install image allows you to boot |CL-ATTR| into a GNOME desktop 
without modifying the host system. Using the live image, you can explore the 
possibilities of developing with |CL|. You can launch the image installer 
and install |CL| on your target system. 

.. contents:: :local:
   :depth: 1

Prerequisites
*************

Before starting, assure your target system supports the installation: 

* :ref:`system-requirements`
* :ref:`compatibility-check`

Preliminary steps 
*****************

#. `Download the live install image`_. [link img/dir or filename]

#. Follow your OS instructions to create a bootable USB drive.

   * :ref:`bootable-usb-linux`
   * :ref:`bootable-usb-mac`
   * :ref:`bootable-usb-windows`

.. _install-from-live-image

Install from live image
***********************

After you've downloaded and burned the live install image on a
USB drive, follow these steps. 

#. Insert the USB drive into an available USB slot.

#. Power on the system.

#. Open the system BIOS setup menu by pressing the F2 key. 

   .. note:: 

   	  Your BIOS setup menu entry point may vary.

#. In the setup menu, enable the UEFI boot and set the USB drive as the
   first option in the device boot order.

#. Save these settings and exit.

#. Reboot the target system.


Launch the installer
********************

#. After the |CL| live install image boots, select the Activities 
   menu in the upper left. 

#. Select the |CL| icon, **Install CLear Linux OS**, shown in Figure 1. 

   .. figure:: figures/live-desktop-1.png
	  :scale: 50 %
	  :alt: Install Clear Linux icon

	  Figure 1: Install Clear Linux icon

#. After selecting the |CL| icon, the installer is launched, as shown in 
   Figure 2.

   .. figure:: figures/live-desktop-2.png
	  :scale: 50 %
	  :alt: Install Clear Linux icon

	  Figure 2: Install Clear Linux icon

#. Continue to :ref:`bare-metal-install-beta`


.. _Download the live install image here: https://download.clearlinux.org/image/
