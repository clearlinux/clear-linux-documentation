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

#. Open the system BIOS setup menu, normally by pressing the :kbd:`F2` key.
   Your BIOS setup menu entry point may vary.

#. In the setup menu, enable the UEFI boot and set the USB drive as the first
   option in the device boot order.

#. Save these settings and exit.

#. Reboot the target system.

#. The |CL| Installer menu will start as shown in Figure 1.
   Select :guilabel:`Clear Linux OS for Intel Architecture` and press the
   :kbd:`Enter` key or wait five seconds to automatically select it.

   .. figure:: figures/cmi1.png
      :scale: 50 %
      :alt: Clear Linux boot menu

      Figure 1: :guilabel:`Clear Linux boot menu`

#. This will take you into the ``Clear Linux OS for Intel Architecture Installer``
   menu as shown in figure 2 and explains how to navigate through the |CL|
   installer setup menus.

   .. figure:: figures/cmi2.png
      :scale: 50 %
      :alt: Clear Linux OS for Intel Architecture Installer

      Figure 2: :guilabel:`Clear Linux OS for Intel Architecture Installer`

   Press the :kbd:`Enter` key.

#. The ``Keyboard selection`` menu shown in figure 3 allows you to set up the
   keyboard layout that you will be using to navigate within the |CL|
   installer setup menus.

   .. figure:: figures/cmi3.png
      :scale: 50 %
      :alt: Keyboard Selection

      Figure 3: :guilabel:`Keyboard Selection`

   For this guide we will select :guilabel:`< * us >`
   for the keyboard mapping, which should already be highlighted. Press the
   :kbd:`Enter` key to continue to the next menu.

Network requirements
====================

This will bring you to the ``Network Requirements`` menu, the first step of the
installer setup process, and will attempt to connect to the |CL| update
server where the installer image is located. Once the connection to the update
server is established you will see a screen similar to the one shown in figure 4:

.. figure:: figures/cmi4.png
   :scale: 50 %
   :alt: Network Requirements

   Figure 4: :guilabel:`Network Requirements`

If you need to configure ``Proxy Settings`` to gain access to the update
server, enter the appropriate address and port of your proxy server in the
:guilabel:`HTTPS proxy:` field, select the
:guilabel:`< Set proxy configuration >` field and press :kbd:`Enter`. You will
then see the connection to the update server established.

Optionally, set up a ``static IP configuration`` to your installer image.
Enter the required information in the :guilabel:`Interface`,
:guilabel:`IP address`, :guilabel:`Subnet mask`, :guilabel:`Gateway` and
:guilabel:`DNS` fields and then select the
:guilabel:`< Set static IP configuration >` field and press the :kbd:`Enter`
key.

The information displayed in the lower right quadrant of the screen
shows the current IP configuration for the update server where the installer
image is located.

.. note::

   If you are having difficulty establishing a connection to the update server
   and you see the message ``none detected, install will fail``, you can
   :kbd:`Tab` to the :guilabel:`< Refresh >` field and press :kbd:`Enter` to
   attempt to reconnect to the update server. If this fails to establish a
   connection after multiple attempts, reboot your system and return to this
   step.

Once the connection to the |CL| udpate server is established, use the
:kbd:`Tab` key to advance to the :guilabel:`< Next >` field and press
:kbd:`Enter` to advance to the next installer setup menu.

Choose action
=============

The ``Choose Action`` menu is where you can choose to install, repair, open
a shell, or exit the installer.

#. Select the :guilabel:`Install` menu item in the ``Choose action`` menu.
   This menu is shown in figure 5:

   .. figure:: figures/cmi5.png
      :scale: 50 %
      :alt: Choose Action

   Figure 5: :guilabel:`Choose Action`

   By choosing :guilabel:`Install`, the installer setup process will continue
   to the next menu screen.

   The :guilabel:`Repair` menu option will run the :command:`swupd --fix` command
   to correct any issues found with the system software that has been installed
   and correct any issues found by overwriting the incorrect file content, adding
   missing files, fixing permissions and any additional changes required to 
   return the file to it's original content and permissions.

   The :guilabel:`Shell` menu item opens a terminal session on your
   system as the root user and you will be able to manage your system from
   this
   console. When you are finished, type :command:`exit` to return to the
   ``Choose Action`` menu.

   The :guilabel:`Exit` menu option terminates the installation process
   and the system will shut down.

#. You will be prompted to join the ``Stability Enhancement Program`` as shown
   in figure 6. Press the :kbd:`Spacebar` or :kbd:`Enter` key while the cursor
   is in the :guilabel:`[ ]  Yes.` field to enable this functionality and then
   select the :guilabel:`< Next >` field to advance to the next menu item.

   .. figure:: figures/cmi3of6.png
      :scale: 50 %
      :alt: Stability Enhancement Program

      Figure 6: :guilabel:`Stability Enhancement Program`

   If you choose not to enable this functionality during this step, you can
   install the ``telemetrics`` software bundle at a later time. As stated in
   the menu,
   this feature only collects anonymous information about your system to help
   improve system stability and no personally identifiable information is
   collected. Please visit our website to `learn more about telemetry.`_

Choose installation type
************************

The next menu of the |CL| installer setup is ``Choose installation Type`` and
is shown in figure 7. This menu will allow you to install |CL|
**automatically** or **manually**. You can also terminate the |CL| Installer
to stop the |CL| installer setup process by selecting :guilabel:`< Exit >` and
shutting down the system.

.. figure:: figures/cai4of6.png
   :scale: 50 %
   :alt: Choose installation type

   Figure 7: :guilabel:`Choose installation Type`

Manual installation
===================

If you select :guilabel:`< Automatic >` as the installation type, the |CL|
Installer will add the minimum amount of functionality required for a fully
functional |CL| system. You will not be able to modify the disk layout, add
a user or any other tasks that the manual installation process will allow.

With the :guilabel:`< Manual(Advanced) >` option you can do the following
additional tasks during |CL| Installer setup:

* modify the disk layout using the cgdisk utility.
* add additional command-line parameters to the kernel.
* create a hostname for your system.
* create an administrative user.
* add additional software bundles to enhance the functionality of your initial
  |CL| installation.
* optionally, set up a static IP address for your system.

To implement any of the additional items listed above for the
manual option, select the :guilabel:`< Manual(Advanced) >` menu item and
follow the steps outlined in the :ref:`bare-metal-manual-install`. This guide
is a continuation from this point.

.. toctree::
   :maxdepth: 1

   bare-metal-manual-install

Automatic installation
**********************

If you only want to install the minimum components for your |CL|
implementation the recommended action is to select the
:guilabel:`< Automatic >` menu item shown in figure 7.

#. Move your cursor to this field and press the :kbd:`Enter` key.

#. This will bring you to the ``Choose target device for installation``
   screen as shown in figure 8. Move your cursor to the desired target and
   press the :kbd:`Enter` key.

   .. figure:: figures/cai5of6.png
      :scale: 50 %
      :alt: Choose target device for installation

      Figure 8: :guilabel:`Choose target device for installation`

   In this example we select the single primary partition from our hard drive.

#. With all the |CL| installer setup information gathered for the automatic
   installation option, the |CL| Installer will prompt you to begin the actual
   installation as shown in figure 9.

   .. figure:: figures/cai6of6.png
      :scale: 50 %
      :alt: Begin installation

      Figure 9: :guilabel:`Begin installation`

   If you are satisfied with the information you have entered, select the
   :guilabel:`< Yes >` field and press :kbd:`Enter` to begin installing |CL|.

|CL| Installation begins...each step will show it's status as it progresses
through the automated installation process.

Complete installation process
=============================

#. Once all steps have completed, you will see the :guilabel:`< Ok >` prompt
   as shown in figure 10. Press the
   :kbd:`Enter` key to continue.

   .. figure:: figures/caisuccess.png
      :scale: 50 %
      :alt: Installation complete

      Figure 10: :guilabel:`Installation complete`

#. The final screen is shown in figure 11 and you will be prompted that the
   installation was successful and the system will be rebooted. Press the
   :kbd:`Enter` key and remove the USB media while the system restarts.

   .. figure:: figures/cairestart.png
      :scale: 50 %
      :alt: Successful installation

      Figure 11: :guilabel:`Successful Installation`

Set up your root and user accounts
==================================

With the USB device removed and the system restarted, your newly installed
|CL| system boots and presents a full screen console requesting ``login:`` as
shown in figure 12:

.. figure:: figures/cairoot.png
   :scale: 50 %
   :alt: Login screen

   Figure 12: :guilabel:`Login screen`

#. At the initial login prompt, enter: ``root``

#. Once you are prompted, enter a new password

#. Re-enter the password to verify it.

   You have now set your root password and are logged in with root privileges.

**Congratulations!**

You have successfully installed |CL| on a bare metal system using the
automatic installation method and set the password for the ``root`` user.

The automatic installation of |CL| is designed to install with minimal
software overhead. Therefore, some housekeeping and package installations
must occur before you have a full-featured |CL| operating system. These
instructions are captured in the :ref:`enable-user-space` section:

* Update the OS to its most current version using `swupd`.
* Install the most common applications for system administrators and
  developers using bundles.
* Setup a new user.
* Setup `sudo` privileges for that new user.
* Install a GUI using those `sudo` privileges.


.. _`information about stateless`:
   https://clearlinux.org/features/stateless

.. _`learn more about telemetry.`:
   https://clearlinux.org/features/telemetry

.. _`NUC6i5SYH product page`:
   http://www.intel.com/content/www/us/en/nuc/nuc-kit-nuc6i5syh.html

