.. _bare-metal-install:

Install Clear Linux OS on bare metal
####################################

This instruction set will guide you through the installation of |CLOSIA|
on bare metal using a bootable USB drive.

.. include:: ../compatibility-check.rst
   :Start-after: compatibility-check:

.. include:: ../bootable-usb/bootable-usb-linux.rst
   :Start-after: bootable-usb-linux:
   :end-before: download-cl-image

.. include:: ../bootable-usb/bootable-usb-linux.rst
   :Start-after: download-cl-image:
   :end-before: verify-checksum

.. include:: ../bootable-usb/bootable-usb-linux.rst
   :Start-after: verify-checksum:
   :end-before: copy-usb-linux

.. include:: ../bootable-usb/bootable-usb-linux.rst
   :Start-after: copy-usb-linux:
   :end-before: usb-next

.. _install-on-target:

Install Clear Linux on your target system
*****************************************

The USB drive that was created in the previous step has been formatted as a
UEFI boot device. Our target system has a hard drive installed containing a
single primary partition. The target system needs a wired Internet connection
with DHCP.

Follow these steps to install |CL| on the target system:

#. Insert the USB drive into an available USB slot.

#. Power on the system.

#. Open the system BIOS setup menu, normally by pressing the F2 key. Your
   BIOS setup menu entry point may vary.

#. In the setup menu, enable the UEFI boot and set the USB drive as the first
   option in the device boot order.

#. Save these settings and exit.

#. Reboot the target system and the |CL| Installer menu will start as shown in
   Figure 1.

.. figure:: figures/cmi1.png
   :scale: 50 %
   :alt: |CL| boot menu

   Figure 1: :guilabel:`|CL| boot menu`

Select :guilabel:`Clear Linux OS for Intel Architecture` and press the 
``Enter`` key or wait 5 seconds to automatically select it.  This will take 
you into the ``Clear Linux OS for Intel Architecture Installer`` menu as shown 
in figure 2 and explains how to navigate through the |CL| installer setup 
menus.

.. figure:: figures/cmi2.png
   :scale: 50 %
   :alt: Clear Linux OS for Intel Architecture Installer

   Figure 2: :guilabel:`Clear Linux OS for Intel Architecture Installer`

Press the ``Enter`` key to continue to the ``Keyboard selection`` menu, 
shown in figure 3.  This menu allows you to set up the keyboard layout that 
you will be using to navigate within the |CL| installer setup menus.  For 
this guide we will select :guilabel:`< * us >` for the keyboard mapping, which 
should already be highlighted.  Press the ``Enter`` key to continue to the 
next menu.

.. figure:: figures/cmi3.png
   :scale: 50 %
   :alt: Keyboard Selection

   Figure 3: :guilabel:`Keyboard Selection`

This will bring you to the ``Network Requirements`` menu, the 1st step of the 
installer setup process, and will attempt to connect to the |CL| update
server.  Once the connection to the update server is established you will see 
a screen similar to the one shown in figure 4:

.. figure:: figures/cmi4.png
   :scale: 50 %
   :alt: Network Requirements

   Figure 4: :guilabel:`Network Requirements`

If you need to configure ``Proxy Settings`` to gain access to the update 
server, enter the appropriate address and port of your proxy server in the 
:guilabel:`HTTPS proxy:` field, select :guilabel:`< Set proxy configuration >`
field and press ``Enter``.  If you entered the address correctly you should 
then see the connection to the update server established.

You can optionally set up a ``static IP configuration`` to your update server 
by entering the required information in the :guilabel:`Interface`, 
:guilabel:`IP address`, :guilabel:`Subnet mask`, :guilabel:`Gateway` and 
:guilabel:`DNS` fields and then selecting the 
:guilabel:`< Set static IP configuration >` field and pressing the ``Enter`` 
key.

The information displayed in the lower right quadrant of the screen 
shows the current IP configuration for the update server where the installer 
image is located.

.. note::

   If you are having difficulty establishing a connection to the update server 
   and you see the message ``none detected, install will fail``, you can 
   ``Tab`` to the :guilabel:`< Refresh >` field and press ``Enter`` to attempt
   to reconnect to the update server.  If this fails to establish a connection
   after multiple attempts, reboot your system and return to this step.

Once the connection to the |CL| udpate server is established, use the ``Tab``
key to advance to the :guilabel:`< Next >` field and press ``Enter`` to
advance to the next installer setup menu.

The ``Choose Action`` menu is where you can choose to Install, Repair, open 
a Shell or Exit the installer.  This menu is shown in figure 5:

.. figure:: figures/cmi5.png
   :scale: 50 %
   :alt: Choose Action

   Figure 5: :guilabel:`Choose Action`

If you choose :guilabel:`Install`, the installer setup process will continue 
to the next menu screen.

Choosing the :guilabel:`Repair` menu option will reinstall all software 
packages that have been installed on the existing |CL| system using the 
:command:`swupd` command and update all installed software bundles including 
the core OS to the latest bundle release.  Since |CL| is a stateless system, 
the default configuration files in the :file:`/usr` and :file:`/etc` 
directories will be restored and the system will be returned to a factory 
default state.  See our website for more `information about stateless`_.  
Once the repair process has completed you will be returned to the 
``Choose Action`` menu.

Selecting the :guilabel:`Shell` menu item will open a terminal session on your 
system as the root user and you will be able to manage your system from this 
console.  When you are finished, type :command:`exit` to return to the 
``Choose Action`` menu.

By selecting :guilabel:`Exit`, you will terminate the installation process 
and the system will shut down.

Install Clear Linux OS
----------------------

If you select the ``Install`` menu item in the ``Choose action`` menu, you 
will be prompted to join the ``Stability Enhancement Program`` as shown in 
figure 6.  Press the ``Spacebar`` or ``Enter`` key while the cursor 
is in the :guilabel:`[ ]  Yes.` field to enable this functionality and then 
select the :guilabel:`< Next >` field to advance to the next menu item.  If 
you choose not to enable this functionality during this step, you can install 
the ``telemetrics`` software bundle at a later time.  As stated in the menu, 
this feature only collects anonymous information about your system to help 
improve system stability and no personally identifiable information is 
collected.  Please visit our website to `learn more about telemetry.`_ 

.. figure:: figures/cmi3of6.png
   :scale: 50 %
   :alt: Stability Enhancement Program

   Figure 6: :guilabel:`Stability Enhancement Program`

Choose installation type
------------------------

The next menu of the |CL| installer setup is ``Choose installation Type`` and 
is shown in figure 7.  This menu will allow you to install |CL| 
**automatically** or **manually**.  You can also terminate the |CL| Installer 
to stop the |CL| installer setup process by selecting :guilabel:`< Exit >` and 
shutting down the system.

.. figure:: figures/cai4of6.png
   :scale: 50 %
   :alt: Choose installation Type

   Figure 7: :guilabel:`Choose installation Type`

Automatic vs. Manual installation
---------------------------------

If you select :guilabel:`< Automatic >` as the installation type, the |CL| 
Installer will add the minimum amount of functionality required for a fully 
functional |CL| system.  You will not be able to modify the disk layout, add 
a user or any other tasks that the manual installation process will allow.

With the :guilabel:`< Manual(Advanced) >` option you can do the following 
additional tasks during |CL| Installer setup:

* modify the disk layout using the cgdisk utility
* add additional command-line parameters to the kernel
* create a hostname for your system
* create an administrative user
* add additional software bundles to enhance the functionality of your initial 
  |CL| installation
* optionally set up a static IP address for your system

If you want to complete the |CL| installation with minimum amount of 
functionality, select the :guilabel:`< Automatic >` option and follow the 
steps outlined in the

.. toctree::
   :maxdepth: 1

   bare-metal-auto-install

If you want to implement any of the additional items listed above for the 
manual option, select the :guilabel:`< Manual(Advanced) >` menu item and
follow the steps outlined in the

.. toctree::
   :maxdepth: 1

   bare-metal-manual-install

.. _`information about stateless`:
   https://clearlinux.org/features/stateless

.. _`learn more about telemetry.`:
   https://clearlinux.org/features/telemetry
