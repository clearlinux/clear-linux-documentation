.. _bare-metal-install-desktop:

Install |CL-ATTR| from the live desktop
#######################################

This page explains how to boot the |CL-ATTR| live desktop image, from which
you can install |CL| or explore without modifying the host system. 
Alternatively, use a :ref:`YAML configuration file <install-configfile>` 
to install |CL|. 

.. contents::
   :local:
   :depth: 1

System requirements
*******************

Before installing |CL|, verify that the host system supports the
installation:

* Requires 20 GB or more disk space
* :ref:`system-requirements`
* :ref:`compatibility-check`

.. _preliminary-steps-install-desktop:

Preliminary steps
*****************

#. Visit our `Downloads`_ page.

#. Download the file :file:`clear-<release number>-live-desktop.iso`,
   also called the |CL| Desktop.

   .. note::

      <release-number> is the latest |CL| auto-numbered release.

#. Follow your OS instructions to
   :ref:`create a bootable usb drive <bootable-usb>`.

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

.. _preliminary-steps-install-desktop-end:

Choose boot menu option
=======================

#. Choose one of the options shown in Figure 1.

   a. Follow `Verify integrity of installer media (optional)`_.

   #. Select :guilabel:`Clear Linux OS` in the boot menu.

      .. figure:: /_figures/bare-metal-install-desktop/bare-metal-install-desktop-01.png
         :scale: 100%
         :alt: Clear Linux OS in boot menu

         Figure 1: Clear Linux OS in boot menu

      .. note::

         If no action is taken, the live image starts by default.

.. _install-on-target-end:

Verify integrity of installer media (optional)
==============================================

Use :guilabel:`Verify ISO Integrity` to verify the checksum of 
the image burned to the installer media. The checksum ensures that the ISO 
is uncorrupted (see Figure 1). For every ISO generated, the 
:guilabel:`clr-installer` implants checksums, which are verified during 
early boot stage as part of :command:`initrd`. 
 
#. Select :guilabel:`Verify ISO Integrity`. The media will be validated.

#. If the check passes, it will boot into the live image. Continue in 
   the next section.

#. If the check fails, a failure message appears. 
   
   * Restart the process at `Preliminary Steps`_. 

.. _install-clr-desktop-start:

Launch the |CL| installer
=========================

#. After the live desktop image boots, scroll over the vertical
   :guilabel:`Activities` menu at left.

#. Click the |CL| penguin icon to launch the installer, shown in Figure 2.

   .. figure:: /_figures/bare-metal-install-desktop/bare-metal-install-desktop-02.png
      :scale: 100%
      :alt: Install Clear Linux OS icon

      Figure 2: |CL| installer icon

#. After the installer is launched, it will appear as shown in Figure 3.

   .. figure:: /_figures/bare-metal-install-desktop/bare-metal-install-desktop-03.png
      :scale: 100%
      :alt: |CL| Desktop Installer

      Figure 3: |CL| OS Desktop Installer

#. In :guilabel:`Select Language`, select a language from the options, or
   type your preferred language in the search bar.

#. Select :guilabel:`Next`.


Network Proxy (optional)
------------------------

#. Configure :guilabel:`Network Proxy` settings.

#. In the top right menu bar, select the :guilabel:`Power button`.

#. Select :guilabel:`Wired Connected` and then :guilabel:`Wired Settings`.

   #. In :guilabel:`Network Proxy`, select the :guilabel:`Gear` icon to view
      options.

   #. Select an option from `Automatic`, `Manual` or `Disabled`.

   #. Close :guilabel:`Network Proxy`.

#. Close :guilabel:`Settings`.

.. _incl-bare-metal-beta-start:

Minimum installation requirements
*********************************

To fulfill minimum installation requirements, complete the
`Required options`_. We also recommend completing `Advanced options`_.

.. note::

   * The :kbd:`Install` button is only highlighted **after** you complete
     `Required options`_.

   * Check marks indicate a selection has been made.

   * The installer image contains the default bundles required for  
     installation. An Internet connection is only required if you install
     additional bundles from `Advanced options`_.

|CL| Desktop Installer
**********************

The |CL| Desktop Installer Main Menu appears as shown in Figure 4. To meet
the minimum requirements, enter values in all submenus for the
:guilabel:`Required options`. After you complete them, your selections appear
below submenus and a check mark appears at right.

.. figure:: /_figures/bare-metal-install-desktop/bare-metal-install-desktop-04.png
   :scale: 100%
   :alt: Clear Linux OS Desktop Installer - Main Menu

   Figure 4: Clear Linux OS Desktop Installer - Main Menu

Navigation
**********

* Use the :kbd:`mouse` to navigate or select options.

* Use :kbd:`Tab` key to navigate between :guilabel:`Required options`
  and :guilabel:`Advanced options`

* Use :kbd:`Up` or :kbd:`Down` arrow keys to navigate the submenus.

* Select :kbd:`Confirm`, or :kbd:`Cancel` in submenus.

Required options
****************

Select Time Zone
================

#. From the Main Menu, select :guilabel:`Select Time Zone`. `UTC` is selected
   by default.

#. In :guilabel:`Select Time Zone`, navigate to the desired time zone.
   Or start typing the region and then the city.
   (.e.g., :file:`America/Los_Angeles`).

#. Select :guilabel:`Confirm`.

   .. figure:: /_figures/bare-metal-install-desktop/bare-metal-install-desktop-05.png
      :scale: 100%
      :alt: Select System Timezone

      Figure 5: Select System Time Zone

Select Keyboard
===============

#. From the Main Menu, select :guilabel:`Select Keyboard`.

#. Navigate to your desired keyboard layout. We select "us" for the
   United States.

#. Select :guilabel:`Confirm`.

   .. figure:: /_figures/bare-metal-install-desktop/bare-metal-install-desktop-06.png
      :scale: 100%
      :alt: Select Keyboard menu

      Figure 6: Select Keyboard menu

Select Installation Media
=========================

#. From the Main Menu, select :guilabel:`Select Installation Media`.

#. Choose an installation method: `Safe Installation`_ or
   `Destructive Installation`_.

   .. figure:: /_figures/bare-metal-install-desktop/bare-metal-install-desktop-07.png
      :scale: 100%
      :alt: Select Installation Media

      Figure 7: Select Installation Media

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

Use this method to destroy the contents of the target device, install |CL|
on it, and accept the `Default partition schema`_.

Disk encryption
---------------

For greater security, disk encryption is supported using LUKS. Encryption is
optional.

#. To encrypt the root partition, select :guilabel:`Enable Encryption`,
   as shown in Figure 8.

   .. figure:: /_figures/bare-metal-install-desktop/bare-metal-install-desktop-08.png
      :scale: 100%
      :alt: Enable Encryption

      Figure 8: Enable Encryption

#. When :guilabel:`Encryption Passphrase` appears, enter a passphrase.

   .. figure:: /_figures/bare-metal-install-desktop/bare-metal-install-desktop-09.png
      :scale: 100%
      :alt: Encryption Passphrase

      Figure 9: Encryption Passphrase

   .. note::

      Minimum length is 8 characters. Maximum length is 94 characters.

#. Enter the same passphrase in the second field.

#. Select :guilabel:`Confirm` in the dialogue box.

   .. note::

      :guilabel:`Confirm` is only highlighted if passphrases match.

#. Select :guilabel:`Confirm` in submenu.

Advanced Installation
---------------------

Use this method to manually partition the target media using `gparted`.
Our example uses the `Default partition schema`_. The space you allocate for
``root``, or additional partitions, may vary.

#. Select :guilabel:`Advanced Installation`.

#. Select :guilabel:`Partition Media`, shown in Figure 11.

   .. figure:: /_figures/bare-metal-install-desktop/bare-metal-install-desktop-10.png
      :scale: 100%
      :alt: Advanced Installation

      Figure 10: Advanced Installation

boot partition
--------------

#. Select the available target media shown as `unallocated`.

   .. figure:: /_figures/bare-metal-install-desktop/bare-metal-install-desktop-11.png
      :scale: 100%
      :alt: Advanced Disk Partitioning

      Figure 11: Advanced Disk Partitioning

#. Choose :menuselection:`Device --> Create Partition Table`.

#. In the `Warning` screen, under :guilabel:`Select new partition table type`
   , select `gpt` from the pull-down menu.

#. Select :guilabel:`Apply`.

#. Select :menuselection:`Partition --> New`.

   .. note::

      The `/boot` partition must be `VFAT(FAT32)`.

#. In :guilabel:`Create new Partition`, complete the following fields to
   match Figure 12. Don't change other default values.

   * :guilabel:`New size:`                150
   * :guilabel:`Partition name:`          CLR_BOOT
   * :guilabel:`File system:`             fat32
   * :guilabel:`Label:`                   boot

   .. figure:: /_figures/bare-metal-install-desktop/bare-metal-install-desktop-12.png
      :scale: 100%
      :alt: boot partition

      Figure 12: boot partition

#. Select :guilabel:`Add`.

swap partition (optional)
-------------------------

A swapfile is generated by default during installation. However, if you prefer to create a swap partition, follow the steps below.

#. With :guilabel:`unallocated` highlighted, select from the menu
   :menuselection:`Partition --> New`.

#. In :guilabel:`Create new Partition`, complete the following fields to
   match Figure 13. Don't change other default values.

   * :guilabel:`New size:`                256
   * :guilabel:`Partition name:`          CLR_SWAP
   * :guilabel:`File system:`             linux-swap
   * :guilabel:`Label:`                   swap

   .. figure:: /_figures/bare-metal-install-desktop/bare-metal-install-desktop-13.png
      :scale: 100%
      :alt: swap partition

      Figure 13: swap partition

#. Select :guilabel:`Add`.

root partition
--------------

#. With :guilabel:`unallocated` highlighted, select from the menu
   :menuselection:`Partition --> New`.

#. In :guilabel:`Create new Partition`, complete the following fields to
   match Figure 14. Don't change other default values.

#. In :guilabel:`New size`, enter the desired size, or leave as is
   to accept the *default: remaining size*.

   * :guilabel:`New size:`                <varies>
   * :guilabel:`Partition name:`          CLR_ROOT
   * :guilabel:`File system:`             ext[234], XFS, or f2fs
   * :guilabel:`Label:`                   root

   .. figure:: /_figures/bare-metal-install-desktop/bare-metal-install-desktop-14.png
      :scale: 100%
      :alt: root partition

      Figure 14: root partition

#. After all partitions are defined, verify your partition
   configuration is similar to Figure 15.

   .. figure:: /_figures/bare-metal-install-desktop/bare-metal-install-desktop-15.png
      :scale: 100%
      :alt: Final partition configuration

      Figure 15: Final partition configuration

#. Select :menuselection:`Edit --> Apply All Operations`.

#. A dialog box appears asking "Are you sure you want to apply the pending
   operations?"

#. Select :guilabel:`Apply`.

#. When dialog :guilabel:`Applying pending operations` is complete, select
   :guilabel:`Close`.

#. Select :menuselection:`GParted --> Quit`.

You are returned to installer.

Manage User
===========

#. In Required Options, select :guilabel:`Manage User`.

#. In :guilabel:`User Name`, enter a user name.

   .. figure:: /_figures/bare-metal-install-desktop/bare-metal-install-desktop-16.png
      :scale: 100%
      :alt: Manage User

      Figure 16: Manage User

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
team for improvements.

#. From :guilabel:`Required Options`, select :guilabel:`Telemetry`.

#. Select :kbd:`Yes`.

   .. figure:: /_figures/bare-metal-install-desktop/bare-metal-install-desktop-17.png
      :scale: 100%
      :alt: Enable Telemetry

      Figure 17: Enable Telemetry

#. If you don't wish to participate, select :kbd:`No`.

Advanced options
****************

After you complete the `Required options`_, we recommend completing
:guilabel:`Advanced options`--though they're not required. Doing so
customizes your development environment, so you're ready to go immediately
after reboot.

.. note::

   You can always add more bundles later with :ref:`swupd-guide`.

Select Additional Bundles
=========================

This option is only available with a valid network connection.
Bundle selection is disabled if no network connection exists.

#. On the Advanced menu, select :guilabel:`Select Additional Bundles`.

#. Select your desired bundles.

   .. figure:: /_figures/bare-metal-install-desktop/bare-metal-install-desktop-18.png
      :scale: 100%
      :alt: Bundle Selection

      Figure 18: Bundle Selection

#. Select :kbd:`Confirm`.

#. View the bundles that you selected.

   .. figure:: /_figures/bare-metal-install-desktop/bare-metal-install-desktop-19.png
      :scale: 100%
      :alt: Select Additional Bundles

      Figure 19: Select Additional Bundles

Optional: Skip to `Finish installation`_.

Assign Hostname
===============

#. In Advanced Options, select :guilabel:`Assign Hostname`.

#. In :guilabel:`Hostname`, enter the hostname only (excluding the domain).

   .. figure:: /_figures/bare-metal-install-desktop/bare-metal-install-desktop-20.png
      :scale: 100%
      :alt: Assign Hostname

      Figure 20: Assign Hostname

   .. note::

      Hostname does not allow empty spaces. Hostname must start with an
      alphanumeric character but may also contain hyphens. Maximum length of
      63 characters.

#. Select :kbd:`Confirm`.

Optional: Skip to `Finish installation`_.

Kernel Configuration
====================

#. In :guilabel:`Kernel Configuration`, navigate to select your desired
   kernel. :guilabel:`Native` is selected by default.

   .. figure:: /_figures/bare-metal-install-desktop/bare-metal-install-desktop-21.png
      :scale: 100%
      :alt: Kernel Configuration

      Figure 21: Kernel Configuration

#. To add arguments, enter the argument in :guilabel:`Add Extra Arguments`.

#. To remove an argument, enter the argument in :guilabel:`Remove Arguments`.

#. Select :kbd:`Confirm`.

Software Updater Configuration
==============================

#. In Advanced Options, select :guilabel:`Software Updater Configuration`.

#. In :guilabel:`Mirror URL`, follow the instructions if you wish to
   specify a different installation source.

#. :guilabel:`Enable Auto Updates` is selected by default. If you **do not**
   wish to enable automatic software updates, uncheck the box.

   .. figure:: /_figures/bare-metal-install-desktop/bare-metal-install-desktop-22.png
      :scale: 100%
      :alt: Software Updater Configuration

      Figure 22: Software Updater Configuration

#. Select :kbd:`Confirm`.

Finish installation
*******************

#. When you are satisfied with your installation configuration, select
   :guilabel:`Install`.

   .. figure:: /_figures/bare-metal-install-desktop/bare-metal-install-desktop-23.png
      :scale: 100%
      :alt: Assign Hostname

      Figure 23: Finish installation

   .. note:

      All check marks must appear in :guilabel:`Required Options` for the
      :guilabel:`Install` button to be enabled.

#. If you do not enter a selection for all :guilabel:`Required Options`,
   the :guilabel:`Install` button remains disabled, as shown
   in Figure 24. Return to `Required Options`_ and make selections.

   .. figure:: /_figures/bare-metal-install-desktop/bare-metal-install-desktop-24.png
      :scale: 100%
      :alt: Required Options - Incomplete

      Figure 24: Required Options - Incomplete

#. After installation is complete, select :guilabel:`Exit`.

#. Shut down the target system.

#. Remove the USB or any installation media.

#. Power on your system.

   .. note::

      Allow time for the graphical login to appear. A login prompt shows the administrative user that you created.

#. Log in as the administrative user.

Congratulations. You successfully installed |CL|.

Default partition schema
========================

Create partitions per requirements in Table 1.

.. list-table:: **Table 1. Default partition schema**
   :widths: 25, 25, 25, 25
   :header-rows: 1

   * - FileSystem
     - Label
     - Mount Point
     - Default size

   * - ``VFAT (FAT32)``
     - boot
     - /boot
     - 150MB

   * - ``ext[234], XFS, or f2fs``
     - root
     - /
     - *Size depends upon use case/desired bundles.*

.. note:: 
   
   A 64MiB swapfile is generated by default. The default size may be set
   manually with the ``--swap-file-size`` command-line option.

Troubleshooting
***************

:ref:`erase-lvm-troubleshooting-tip`

Related topics
**************

* :ref:`install-configfile`

.. _Downloads: https://clearlinux.org/downloads
