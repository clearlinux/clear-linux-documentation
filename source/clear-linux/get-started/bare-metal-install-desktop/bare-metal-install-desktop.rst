.. _bare-metal-install-desktop:

Install |CL-ATTR| from the live desktop
#######################################

The live desktop allows you to boot |CL-ATTR| in a GNOME desktop without
modifying the host system, offering the chance to explore developing
on |CL|. Better yet, launch the |CL| installer to install on your target
system.

.. contents:: :local:
   :depth: 1

System requirements
*******************

Assure that your target system supports the installation:

* :ref:`system-requirements`
* :ref:`compatibility-check`

Preliminary steps
*****************

#. `Visit our Downloads page`_.

#. Download the file :file:`clear-<release number>-live-desktop.iso`

   .. note::

      <release-number> is the latest |CL| auto-numbered release.

#. Follow your OS instructions to create a bootable USB drive.

   * :ref:`bootable-usb`

.. _install-on-target-start:

Install from live image
***********************

After you download and burn the live desktop image on a USB drive, follow
these steps.

#. Insert the USB drive into an available USB slot.

#. Power on the system.

#. Open the system BIOS setup menu by pressing the :kbd:`F2` key.
   Your BIOS setup menu entry point may vary.

#. In the setup menu, enable the UEFI boot and set the USB drive as the
   first option in the device boot order.

#. Save these settings, e.g. :kbd:`F10`, and exit.

#. Reboot the target system.

#. Select :guilabel:`Clear Linux OS` in the boot menu, shown in Figure 1.

   .. figure:: figures/bare-metal-install-desktop-01.png
      :scale: 100%
      :alt: Clear Linux OS in boot menu

      Figure 1: Clear Linux OS in boot menu

.. _install-on-target-end:

Confirm network connection
==========================

Confirm there is a network connection before launching the installer.
Choose a method: `Wired Connection`, or `WiFi Connected`. This guide shows
an example of a **Wired Connection**.

#. In the upper right of the top menu bar, select the square icon to view
   Network settings, shown in Figure 2.

#. Select :guilabel:`Wired Connected` and then :guilabel:`Wired Settings`.

   .. figure:: figures/bare-metal-install-desktop-02.png
      :scale: 100%
      :alt: Software icon, Network settings

      Figure 2: Software icon, Network settings

#. View the :guilabel:`Wired` menu to assure that you're target system and
   installer are connected to a network.

#. Optional: Configure Proxy settings.

   #. To view :guilabel:`Network Proxy`, select its :guilabel:`Gear` icon.

   #. Select from `Automatic`, `Manual` or `Disabled` as desired.

   #. Close the dialogue box.

#. Select the :guilabel:`Gear` icon to view Network settings.

#. If desired, select :guilabel:`Connect automatically`.
   Select other options as desired.

#. Select :guilabel:`Apply` button to confirm change to settings.

Software
--------

Optional: Explore |CL| bundles and other software available. Double-click the :guilabel:`Software` icon from the Activities menu, shown in Figure 2.

.. note::

   `Sofware` application is *only intended for exploring* available bundles,
   applications, and images. Do not attempt to install them.

   Assure there is a network connection before launching `Software`.

Launch the |CL| installer
=========================

#. After the live desktop image boots, find the |CL| icon in
   the :guilabel:`Activities` menu at left, shown in Figure 3.

#. Click the icon, :guilabel:`Install Clear Linux OS`.

   .. figure:: figures/bare-metal-install-desktop-02.png
      :scale: 100%
      :alt: Install Clear Linux OS icon

      Figure 3: Install Clear Linux OS icon

#. The installer is launched, as shown in Figure 4.

   .. figure:: figures/bare-metal-install-desktop-04.png
      :scale: 100%
      :alt: |CL| Desktop Installer

      Figure 4: |CL| OS Desktop Installer

#. In :guilabel:`Select Language`, select a language from the options, or
   type your preferred language in the search bar.

#. Select :guilabel:`Next`.


.. _incl-bare-metal-beta-start:

Minimum installation requirements
*********************************

To fulfill minimum installation requirements, complete the
`Required options`_. We also recommend completing `Advanced options`_.

.. note::

   * The :kbd:`Install` button is only highlighted **after** you complete
     `Required options`_.

   * Checkmarks indicate a selection has been made.

   * An Internet connection is required. You may want to launch a browser
     prior to installation to verify your Internet connection.

|CL| Desktop Installer
**********************

The |CL| Desktop Installer Main Menu appears as shown in Figure 5. To meet
the minimum requirements, enter values in all submenus for the
:guilabel:`Required options`. After you complete them, your selections appear
below submenus and a checkmark appears at right.

.. figure:: figures/bare-metal-install-desktop-05.png
   :scale: 100%
   :alt: Clear Linux OS Desktop Installer - Main Menu

   Figure 5: Clear Linux OS Desktop Installer - Main Menu

Navigation
**********

* Use the :kbd:`mouse` to navigate or select options.

* Use :kbd:`Tab` key to navigate between :guilabel:`Required options`
  and :guilabel:`Advanced options`

* Use :kbd:`Up` or :kbd:`Down` arrow keys to navigate submenu list.

* Select :kbd:`Confirm`, or :kbd:`Cancel` in submenus.

Required options
****************

Select Time Zone
================

#. From the Main Menu, select :guilabel:`Select Time Zone`. `UTC` is selected
   by default.

#. In :guilabel:`Select Time Zone`, navigate to the desired time zone.
   Or start typing the region and then city.
   (.e.g., :file:`America/Los_Angeles`).

#. Select :guilabel:`Confirm`.

   .. figure:: figures/bare-metal-install-desktop-06.png
      :scale: 100%
      :alt: Select System Timezone

      Figure 6: Select System Time Zone

Select Keyboard
===============

#. From the Main Menu, select :guilabel:`Select Keyboard`.

#. Navigate to your desired keyboard layout. We select "us" for the
   United States.

#. Select :guilabel:`Confirm`.

   .. figure:: figures/bare-metal-install-desktop-07.png
      :scale: 100%
      :alt: Select Keyboard menu

      Figure 7: Select Keyboard menu

Select Installation Media
=========================

#. From the Main Menu, select :guilabel:`Select Installation Media`.

#. Choose an installation method: `Safe Installation`_ or
   `Destructive Installation`_.

   .. figure:: figures/bare-metal-install-desktop-08.png
      :scale: 100%
      :alt: Select Installation Media

      Figure 8: Select Installation Media

Safe Installation
-----------------
Use this method to safely install |CL| on media with available space, or
alongside existing partitions, and accept the `Default partition schema`_.
If enough free space exists, safe installation is allowed.

.. note::

   |CL| allows installation alongside another OS. Typically, when you boot
   your system, you can press an `F key` to view and select a bootable
   device or partition during the BIOS POST stage. Some BIOSes present the
   |CL| partition, and you can select and boot it. However, other
   BIOSes may only show the primary partition, in which case you will not be
   able boot |CL|. Be aware of this possible limitation.


Destructive Installation
------------------------

Use this method to destroy the contents of the target device, install |CL| on it, and accept the `Default partition schema`_.

Disk encryption
===============

For greater security, disk encryption is supported using LUKS. Encryption is
optional.

#. To encrypt the root partition, select :guilabel:`Enable Encryption`,
   as shown in Figure 9.

   .. figure:: figures/bare-metal-install-desktop-09.png
      :scale: 100%
      :alt: Enable Encryption

      Figure 9: Enable Encryption

#. When :guilabel:`Encryption Passphrase` appears, enter a passphrase.

   .. figure:: figures/bare-metal-install-desktop-10.png
      :scale: 100%
      :alt: Encryption Passphrase

      Figure 10: Encryption Passphrase

   .. note::

      Minimum length is 8 characters. Maximum length is 94 characters.

#. Enter the same passphrase in the second field.

#. Select :guilabel:`Confirm` in the dialogue box.

   .. note::

      :guilabel:`Confirm` is only highlighted if passphrases match.

#. Select :guilabel:`Confirm` in submenu.

Manage User
===========

#. In Required Options, select :guilabel:`Manage User`.

#. In :guilabel:`User Name`, enter a user name.

   .. figure:: figures/bare-metal-install-desktop-11.png
      :scale: 100%
      :alt: Manage User

      Figure 11: Manage User

#. In :guilabel:`Login`, create a login name. It must start with a letter
   and can use numbers, hyphens, and underscores. Maximum length is 31
   characters.

#. In :guilabel:`Password`, enter a password. Minimum length is
   8 characters. Maximum length is 255 characters.

#. In :guilabel:`Confirm`, enter the same password.

   .. note::

      :guilabel:`Administrator` rights are selected by default.
      For security purposes, the default user must be assigned as an
      Administrator.

#. Select :kbd:`Confirm`.

   .. note::

      Select :guilabel:`Cancel` to return to the Main Menu.

Modify User
-----------

#. In Manager User, select :guilabel:`Manage User`.

#. Modify user details as desired.

#. Select :guilabel:`Confirm` to save the changes you made.

   .. note::

      Optional: Select :guilabel:`Cancel` to return to the Main Menu to
      revert changes.

Optional: Skip to `Finish installation`_.

Telemetry
=========

Choose whether to participate in `telemetry`. :ref:`telem-guide` is a |CL|
feature that reports failures and crashes to the |CL| development
team for improvements. For more information, see :ref:`telemetry-about`.

#. From :guilabel:`Required Options`, select :guilabel:`Telemetry`.

#. Select :kbd:`Confirm`.

#. If you don't wish to participate, deselect :kbd:`Enable Telemetry`.

#. Select :kbd:`Confirm`.

   .. figure:: figures/bare-metal-install-desktop-12.png
      :scale: 100%
      :alt: Enable Telemetry

      Figure 12: Enable Telemetry

Advanced options
****************

After you complete the `Required options`_, we recommend completing
:guilabel:`Advanced options`--though they're not required. Doing so
customizes your development environment, so you're ready to go immediately
after reboot.

* `Bundle Selection`_

* `Assign Hostname`_

As for bundles, you can always add more later with :ref:`swupd-guide`.

Bundle Selection
================

#. On the Advanced menu, select :guilabel:`Bundle Selection`

#. Select your desired bundles.

   .. figure:: figures/bare-metal-install-desktop-13.png
      :scale: 100%
      :alt: Bundle Selection

      Figure 13: Bundle Selection

#. Select :kbd:`Confirm`.

#. View the bundles that you selected.

   .. figure:: figures/bare-metal-install-desktop-14.png
      :scale: 100%
      :alt: Bundle Selections - Advanced Options

      Figure 14: Bundle Selections - Advanced Options

Optional: Skip to `Finish installation`_.

Assign Hostname
===============

#. In Advanced Options, select :guilabel:`Assign Hostname`.

#. In :guilabel:`Hostname`, enter the hostname only (excluding the domain).

   .. figure:: figures/bare-metal-install-desktop-15.png
      :scale: 100%
      :alt: Assign Hostname

      Figure 15: Assign Hostname

   .. note::

      Hostname does not allow empty spaces. Hostname must start with an
      alphanumeric character but may also contain hyphens. Maximum length of
      63 characters.

#. Navigate to :kbd:`Confirm` until highlighted.

#. Select :kbd:`Confirm`.

Optional: Skip to `Finish installation`_.

Finish installation
*******************

#. When you are satisfied with your installation configuration, select
   :guilabel:`Install`.

   .. figure:: figures/bare-metal-install-desktop-16.png
      :scale: 100%
      :alt: Assign Hostname

      Figure 16: Finish installation

   .. note:

      All checkmarks must be visible in :guilabel:`Required Options` for you to select :guilabel:`Install`.

#. If you do not enter a selection for all :guilabel:`Required Options`,
   the :guilabel:`Install` button remains greyed out, as shown
   in Figure 17. Return to `Required Options`_ and make selections.


   .. figure:: figures/bare-metal-install-desktop-17.png
      :scale: 100%
      :alt: Required Options - Incomplete

      Figure 17: Required Options - Incomplete

#. After installation is complete, select :guilabel:`Exit`.

#. Shut down the target system.

#. Remove the USB or any installation media.

#. Power on your system.

   .. note::

      Allow time for the graphical login to appear. A login prompt shows the administrative user that you created.

#. Log in as the adminstrative user.

Congratulations. You successfully installed |CL|.

Default partition schema
========================

Table 1 shows the defult partition schema with the exception of root,
which varies.

.. list-table:: **Table 1. Disk Partition Setup**
   :widths: 33, 33, 33
   :header-rows: 1

   * - FileSystem
     - Mount Point
     - Minimum size
   * - ``VFAT``
     - /boot
     - 150M
   * - ``swap``
     -
     - 256MB
   * - ``root``
     - /
     - *Size depends upon use case/desired bundles.*

Next steps
**********

:ref:`guides`

.. _Visit our downloads page: https://clearlinux.org/downloads
.. _Autoproxy: https://clearlinux.org/features/autoproxy

