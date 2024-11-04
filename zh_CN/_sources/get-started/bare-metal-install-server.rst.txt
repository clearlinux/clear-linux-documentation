.. _bare-metal-install-server:

Install |CL-ATTR| from the live server
######################################

This page explains how to install |CL-ATTR| on bare metal from a bootable USB
drive using a live server image.

.. contents::
   :local:
   :depth: 1

System requirements
*******************

Before installing |CL|, verify that the host system supports the
installation:

* :ref:`system-requirements`
* :ref:`compatibility-check`

Download the latest |CL| live server image
******************************************

Get the latest |CL| installer image from the `Downloads`_ page. Look for the
:file:`clear-[version number]-live-server.iso` file.

#. Verify and decompress the file per your OS.

   * :ref:`download-verify-decompress`

#. Follow your OS instructions to create a bootable USB drive.

   * :ref:`bootable-usb`

Install |CL| on your target system
**********************************

Ensure that your system is configured to boot UEFI. The installation method
described below requires a wired Internet connection with DHCP.

.. note::

   Alternatively, you can install |CL| over a wireless connection by first
   using `nmtui`. Follow the `nmtui` instructions shown in Figure 2.

Follow these steps to install |CL| on the target system:

#. Insert the USB drive into an available USB slot.

#. Power on the system.

#. Open the system BIOS setup menu by pressing the :kbd:`F2` key.
   Your BIOS setup menu entry point may vary.

   .. note::
      |CL| supports UEFI boot. Some hardware may list UEFI and non-UEFI USB
      boot entries. In this case, you should select the `UEFI` boot
      option.

#. In the setup menu, enable the UEFI boot and set the USB drive as the first
   option in the device boot order.

#. Save these settings and exit.

#. Reboot the target system.

#. This action launches the |CL| installer boot menu, shown in figure 1.

   .. figure:: /_figures/bare-metal-install-server/bare-metal-install-server-01.png
      :scale: 100%
      :alt: Clear Linux OS Installer boot menu

      Figure 1: Clear Linux OS Installer boot menu

#. With :guilabel:`Clear Linux OS` highlighted, select :kbd:`Enter`.

Launch the |CL| Installer
*************************

#. At the :guilabel:`login` prompt, enter :command:`root`.

#. Follow the onscreen instructions, shown in Figure 2, and
   enter a temporary password.

   .. figure:: /_figures/bare-metal-install-server/bare-metal-install-server-02.png
      :scale: 100%
      :alt: root login

      Figure 2: root login

#. At the :guilabel:`root` prompt, enter :command:`clr-installer` and
   press :kbd:`Enter`.

   .. figure:: /_figures/bare-metal-install-server/bare-metal-install-server-03.png
      :scale: 100%
      :alt: clr-installer command

      Figure 3: clr-installer command

Minimum installation requirements
*********************************

To fulfill minimum installation requirements, complete the
`Required options`_. While not required, we encourage you to apply the
`Recommended options`_. `Advanced options`_ are optional.

.. note::

   * The :kbd:`Install` button is **only highlighted after** you complete
     `Required options`_.

Main Menu
*********
The |CL| Installer Main Menu appears as shown in Figure 4.

.. figure:: /_figures/bare-metal-install-server/bare-metal-install-server-04.png
   :scale: 100%
   :alt: Clear Linux OS Installer

   Figure 4: Clear Linux OS Installer

The |CL| Installer Main Menu has two tabs: :guilabel:`[R] Required options`
and :guilabel:`[A] Advanced options`. Navigate between tabs using the arrow
these shortcut keys:

* :kbd:`Shift+A` for :guilabel:`[A] Advanced options`
* :kbd:`Shift+R` for :guilabel:`[R] Required options`

To meet the minimum requirements, enter your choices in the
:guilabel:`Required options`. After confirmation, your selections appear
beside the :guilabel:`>>` chevron, below the menu options.

Navigation
**********

* Select :kbd:`Tab` or :kbd:`Up/Down` arrows to highlight your choice.

* Select :kbd:`Enter` or :kbd:`Spacebar` to confirm your choice.

* Select :kbd:`Cancel` or :kbd:`Esc` to cancel your choice.

Required options
****************

Choose Timezone
===============

#. From the Main Menu, navigate to :guilabel:`Choose Timezone`.
   `UTC` is the default.

#. Select :kbd:`Enter`.

#. In :guilabel:`Select System Timezone`, use :kbd:`Up/Down` arrows
   navigate to the desired timezone.

.. todo: User need only select Enter; can only select Confirm with mouse.

#. Press :kbd:`Enter` to confirm.

   .. figure:: /_figures/bare-metal-install-server/bare-metal-install-server-05.png
      :scale: 100%
      :alt: Select System Timezone

      Figure 5: Select System Timezone

Choose Language
===============

#. From the Main Menu, navigate to :guilabel:`Choose Language`.

#. Select :kbd:`Enter`.

#. In :guilabel:`Select System Language`, navigate to your desired language.

#. Press :kbd:`Enter` to confirm.

   .. figure:: /_figures/bare-metal-install-server/bare-metal-install-server-06.png
      :scale: 100%
      :alt: Select System Language

      Figure 6: Select System Language

Configure the Keyboard
======================

#. From the Main Menu, select :guilabel:`Configure the Keyboard`.

#. Select :kbd:`Enter`.

#. In :guilabel:`Select Keyboard`, navigate to the desired option.

#. Select :kbd:`Enter` to :kbd:`Confirm`.

#. Optional: In :guilabel:`Test keyboard`, type text to assure
   that the keys map to your keyboard.

   .. figure:: /_figures/bare-metal-install-server/bare-metal-install-server-07.png
      :scale: 100%
      :alt: Select Keyboard menu

      Figure 7: Select Keyboard menu

Configure Installation Media
============================

#. From the Main Menu, select :guilabel:`Configure Installation Media`.

#. Choose an installation method:
   * `Safe Installation`_
   * `Destructive Installation`_
   * `Advanced Configuration`_


   .. figure:: /_figures/bare-metal-install-server/bare-metal-install-server-08.png
      :scale: 100%
      :alt: Select Installation Media

      Figure 8: Select Installation Media

#. Select :guilabel:`Rescan Media` to show available installation targets.

.. todo: Revise below section to match the dev-gui-00

Safe Installation
-----------------

Use this method to safely install |CL| on media with available space, or
alongside existing partitions, and accept the `Default partition schema`_.
If enough free space exists, safe installation is allowed. See also
`Troubleshooting`_ below.

Destructive Installation
------------------------

Use this method to destroy the contents of the target device, install |CL|
on it, and accept the `Default partition schema`_.

.. note::

   From the :guilabel:`Select Installation Media` menu, select
   :guilabel:`Enable Encryption` to encrypt the root filesystem for either
   option above. See also `Disk encryption`_ for more information.

Advanced Configuration
----------------------

Use this method to manually configure partitions. These must meet
`Default partition schema`_. You may also choose `Disk encryption`_ during
configuration of each partition.

.. note::

   `Advanced Configuration` is available in the installer versions 1.2.0 and
   above.

#. From :guilabel:`Select Installation Media`, shown in Figure 8 above,
   select :guilabel:`Advanced Configuration`.

#. In :guilabel:`Advanced Configuration`, navigate to :file:`/dev/sda`
   and then press :kbd:`Enter`.

   .. figure:: /_figures/bare-metal-install-server/bare-metal-install-server-09.png
      :scale: 100%
      :alt: Advanced configuration menu

      Figure 9: Advanced configuration menu

#. Choose a partition method:

   * :guilabel:`Auto Partition` Select this option to accept the
     `Default partition schema`_.

     #. Navigate to and press :guilabel:`Confirm`.

     #. Continue with installation configuration. Jump to `Telemetry`_.

   * `Manual Partition`_ Continue below.

Manual Partition
----------------

We provide a simple example below.

#. Navigate to the unallocated media (e.g.,`/dev/sda`) until highlighted, as
   shown in Figure 9.

#. Press :guilabel:`Enter` to edit the partition.

#. The :guilabel:`Partition Setup` menu appears, shown in Figure 10.

   .. note::

      After adding the first partition, select :guilabel:`Free Space` to add another partition.

root partition
--------------

#. We configure the `root` partition as shown in Figure 10.
   Configuration of the `root` partition varies.

   .. figure:: /_figures/bare-metal-install-server/bare-metal-install-server-10.png
      :scale: 100%
      :alt: root partition

      Figure 10: root partition

#. Navigate to :guilabel:`Add` and press :guilabel:`Enter`.

boot partition
--------------

#. We configure the `boot` partition as shown in Figure 11.

   .. figure:: /_figures/bare-metal-install-server/bare-metal-install-server-11.png
      :scale: 100%
      :alt: boot partition

      Figure 11: boot partition

#. Navigate to :guilabel:`Add` and press :guilabel:`Enter`.

swap partition
--------------

#. In the :guilabel:`File System` pulldown menu, select `swap`, and
   enter a label. We enter the minimum required size (e.g., 256M).

   .. figure:: /_figures/bare-metal-install-server/bare-metal-install-server-12.png
      :scale: 100%
      :alt: swap partition

      Figure 12: swap partition

#. Navigate to :guilabel:`Add` and press :guilabel:`Enter`.

#. Next, navigate to :guilabel:`Confirm` and press :guilabel:`Enter`,
   shown in Figure 13.

   Manual partitioning is complete.

   .. figure:: /_figures/bare-metal-install-server/bare-metal-install-server-13.png
      :scale: 100%
      :alt: Final configuration of disk partitions

      Figure 13: Final configuration of disk partitions

#. You may skip to the `Telemetry`_ section below.

Disk encryption
===============

For greater security, disk encryption is supported using LUKS for the
any partition except `/boot` on |CL|. To encrypt the root partition, see the
example below. Encryption is optional.

Encryption Passphrase
---------------------

|CL| uses a single passphrase for encrypted partitions. Additional keys may
be configured post-installation using the ``cryptsetup`` tool.

#. Optional: Select :guilabel:`[X] Encrypt` to encrypt the root partition,
   as shown in Figure 14.

   .. figure:: /_figures/bare-metal-install-server/bare-metal-install-server-14.png
      :scale: 100%
      :alt: Encrypt partition

      Figure 14: Encrypt partition

#. The :guilabel:`Encryption Passphrase` dialogue appears.

   .. note::

      Minimum length is 8 characters. Maximum length is 94 characters.

   .. figure:: /_figures/bare-metal-install-server/bare-metal-install-server-15.png
      :scale: 100%
      :alt: Encryption Passphrase

      Figure 15: Encryption Passphrase

#. Enter the same passphrase in the first and second field.

#. Navigate to :guilabel:`Confirm` and press :kbd:`Enter`.

   .. note::

      :guilabel:`Confirm` is only highlighted if passphrases match.

Telemetry
=========

:ref:`telem-guide` is a |CL| feature that reports failures and crashes to
the |CL| development team for improvements.

Select your desired option on whether to participate in telemetry.

#. In the Main Menu, navigate to :guilabel:`Telemetry` and select
   :kbd:`Enter`.

#. Select :kbd:`Tab` to highlight your choice.

#. Select :kbd:`Enter` to confirm.

   .. figure:: /_figures/bare-metal-install-server/bare-metal-install-server-16.png
      :scale: 100%
      :alt: Enable Telemetry

      Figure 16: Enable Telemetry

Recommended options
*******************

After you complete the `Required options`_, we highly recommend completing
these selected `Advanced options`_ at minimum:

* `Manage User`_ Assign a new user with administrative rights
* `Assign Hostname`_ Simplify your development environment

Skip to finish installation
===========================

After selecting values for all :guilabel:`Required options`, you may skip
to `Finish installation`_.

Otherwise, continue below. In the Main Menu, select
:guilabel:`Advanced options` for additional configuration.

Advanced options
****************

Configure Network Interfaces
============================

By default, |CL| is configured to automatically detect the host network
interface using DHCP. However, if you want to use a static IP address or if
you do not have a DHCP server on your network, follow these instructions to
manually configure the network interface. Otherwise, default network
interface settings are automatically applied.

.. note::

   If DHCP is available, no user selection may be required.

#. Navigate to :guilabel:`Configure Network Interfaces` and
   select :kbd:`Enter`.

#. Navigate to the network :guilabel:`interface` you wish to change.

#. When the desired :guilabel:`interface` is highlighted, select
   :guilabel:`Enter` to edit.

   .. note:: Multiple network interfaces may appear.

   .. figure:: /_figures/bare-metal-install-server/bare-metal-install-server-17.png
      :scale: 100%
      :alt: Configure Network Interfaces

      Figure 17: Configure Network Interfaces

#. Notice :guilabel:`Automatic / dhcp` is selected by default (at bottom).

   Optional: Navigate to the checkbox :guilabel:`Automatic / dhcp` and select
   :kbd:`Spacebar` to deselect.

   .. figure:: /_figures/bare-metal-install-server/bare-metal-install-server-18.png
      :scale: 100%
      :alt: Network interface configuration

      Figure 18: Network interface configuration

#. Navigate to the appropriate fields and assign the desired
   network configuration.

#. To save settings, navigate to :guilabel:`Confirm` and select
   :kbd:`Enter`.

   .. note::

      To revert to previous settings, navigate to the :guilabel:`Cancel`
      and select :kbd:`Enter`.

#. Upon confirming network configuration, the :guilabel:`Testing Networking`
   dialogue appears. Assure the result shows success. If a failure occurs,
   your changes will not be saved.

#. Upon confirmation, you are returned to :guilabel:`Network interface`
   settings.

#. Navigate to and select :guilabel:`Main Menu`.

Optional: Skip to `Finish installation`_.

Proxy
=====

|CL| automatically attempts to detect proxy settings, as described in
:ref:`autoproxy`. If you need to manually assign proxy settings, follow this
instruction.

#. From the Advanced options menu, navigate to :guilabel:`Proxy`, and
   select :kbd:`Enter`.

#. Navigate to the field :guilabel:`HTTPS Proxy`.

   .. figure:: /_figures/bare-metal-install-server/bare-metal-install-server-19.png
      :scale: 100%
      :alt: Configure the network proxy

      Figure 19: Configure the network proxy

#. Enter the desired proxy address and port using conventional syntax,
   such as: \http://address:port.

#. Navigate to :guilabel:`Confirm` and select :kbd:`Enter`.

#. To revert to previous settings, navigate to :guilabel:`Cancel`
   and select :guilabel:`Cancel`.

Optional: Skip to `Finish installation`_.

Test Network Settings
=====================

To manually assure network connectivity before installing |CL|,
select :guilabel:`Test Network Settings` and select :guilabel:`Enter`.

A progress bar appears as shown in Figure 20.

.. figure:: /_figures/bare-metal-install-server/bare-metal-install-server-20.png
   :scale: 100%
   :alt: Testing Networking dialogue

   Figure 20: Testing Networking dialogue

.. note::

   Any changes made to network settings are automatically tested
   during configuration.

Optional: Skip to `Finish installation`_.

Bundle Selection
================

#. On the Advanced menu, select :guilabel:`Bundle Selection`

#. Navigate to the desired bundle using :kbd:`Tab` or :kbd:`Up/Down` arrows.

#. Select :kbd:`Spacebar` to select the checkbox for each desired bundle.

   .. figure:: /_figures/bare-metal-install-server/bare-metal-install-server-21.png
      :scale: 100%
      :alt: Bundle Selection

      Figure 21: Bundle Selection

#. Optional: To start developing with |CL|, we recommend
   adding :file:`os-clr-on-clr`.

#. Navigate to and select :kbd:`Confirm`.

   You are returned to the :guilabel:`Advanced options` menu.

Optional: Skip to `Finish installation`_.

Manage User
===========

Add New User
------------

#. In Advanced Options, select :guilabel:`Manage User`.

#. Select :guilabel:`Add New User` as shown in Figure 22.

   .. figure:: /_figures/bare-metal-install-server/bare-metal-install-server-22.png
      :scale: 100%
      :alt: Add New User, User Name

      Figure 22: Add New User

#. Optional: Enter a :guilabel:`User Name`.

   .. note:

      The User Name must be alphanumeric and can include spaces, commas, or
      hyphens. Maximum length is 64 characters.

   .. figure:: /_figures/bare-metal-install-server/bare-metal-install-server-23.png
      :scale: 100%
      :alt: User Name

      Figure 23: User Name

#. Enter a :guilabel:`Login`.

   .. note::

      The User Login must be alphanumeric and can include hyphens and underscores. Maximum length is 31 characters.

#. Enter a :guilabel:`Password`.

   .. note:

      Minimum length is 8 characters. Maximum length is 255 characters.

#. In :guilabel:`Confirm`, enter the same password.

#. Optional: Navigate to the :guilabel:`Administrative` checkbox and select
   :kbd:`Spacebar` to assign administrative rights to the user.

   .. note::

      Selecting this option enables sudo privileges for the user.

#. Select :kbd:`Confirm`.

   .. note::

      If desired, select :guilabel:`Reset` to reset the form.

#. In :guilabel:`Manage User`, navigate to :guilabel:`Confirm`.

#. With :guilabel:`Confirm` highlighted, select :kbd:`Enter`.

Modify / Delete User
--------------------

#. In :guilabel:`Manage User`, navigate to the user you wish
   to modify until highlighted, as shown in Figure 24.

#. Select :kbd:`Enter` to modify the user.

   .. figure:: /_figures/bare-metal-install-server/bare-metal-install-server-24.png
      :scale: 100%
      :alt: Modify User

      Figure 24: Modify User

#. Modify user details as desired.

#. Navigate to :kbd:`Confirm` until highlighted.

   .. note::

      Optional: Select :guilabel:`Reset` to rest the form.

#. Select :guilabel:`Confirm` to save the changes you made.

#. Optional: In :guilabel:`Modify User`, to delete the user, navigate to
   the :guilabel:`Delete` button and select :kbd:`Enter`.

   .. figure:: /_figures/bare-metal-install-server/bare-metal-install-server-25.png
      :scale: 100%
      :alt: Delete User

      Figure 25: Delete User

You are returned to :guilabel:`Manage User`.

#. Navigate to :kbd:`Confirm` until highlighted.

#. Select :guilabel:`Enter` to complete :guilabel:`Manage User` options.

Optional: Skip to `Finish installation`_.

Kernel Command Line
===================

For advanced users, |CL| provides the ability to add or remove kernel
arguments. If you want to append a new argument, enter the argument here.
This argument will be used every time you install or update a
new kernel.

#. In Advanced Options, select :guilabel:`Tab` to highlight
   :guilabel:`Kernel Command Line`.

#. Select :kbd:`Enter`.

   .. figure:: /_figures/bare-metal-install-server/bare-metal-install-server-26.png
      :scale: 100%
      :alt: kernel command line

      Figure 26: kernel command line

#. Choose from the following options.

   * To add arguments, enter the argument in :guilabel:`Add Extra Arguments`.

   * To remove an argument, enter the argument in
     :guilabel:`Remove Arguments`.

#. Select :kbd:`Confirm`.

Optional: Skip to `Finish installation`_.

Kernel Selection
================

#. Select a kernel option. By default, the latest kernel release is
   selected. Native kernel is shown in Figure 27.

#. To select a different kernel, navigate to it using :guilabel:`Tab`.

   .. figure:: /_figures/bare-metal-install-server/bare-metal-install-server-27.png
      :scale: 100%
      :alt: Kernel selection

      Figure 27: Kernel selection

#. Select :kbd:`Spacebar` to select the desired option.

#. Navigate to :kbd:`Confirm` and select :kbd:`Enter`.

Optional: Skip to `Finish installation`_.

Swupd Mirror
============

If you have your own custom mirror of |CL|, you can add its URL.

#. In Advanced Options, select :guilabel:`Swupd Mirror`.

#. To add a local swupd mirror, enter a valid URL in :guilabel:`Mirror URL:`

#. Select :kbd:`Confirm`.

   .. figure:: /_figures/bare-metal-install-server/bare-metal-install-server-28.png
      :scale: 100%
      :alt: Swupd Mirror

      Figure 28: Swupd Mirror

Optional: Skip to `Finish installation`_.

Assign Hostname
===============

#. In Advanced Options, select :guilabel:`Assign Hostname`.

#. In :guilabel:`Hostname`, enter the hostname only (excluding the domain).

   .. note::

      Hostname does not allow empty spaces. Hostname must start with an
      alphanumeric character but may also contain hyphens. Maximum length of
      63 characters.

   .. figure:: /_figures/bare-metal-install-server/bare-metal-install-server-29.png
      :scale: 100%
      :alt: Assign Hostname

      Figure 29: Assign Hostname

#. Navigate to :kbd:`Confirm` until highlighted.

#. Select :kbd:`Confirm`.

Optional: Skip to `Finish installation`_.

Automatic OS Updates
====================

Automatical OS updates are enabled by default. In the rare case that you
need to disable automatic software updates, follow the onscreen instructions,
shown in Figure 30.

#. In Advanced Options, select :guilabel:`Automatic OS Updates`.

#. Select the desired option.

   .. figure:: /_figures/bare-metal-install-server/bare-metal-install-server-30.png
      :scale: 100%
      :alt: Automatic OS Updates

      Figure 30: Automatic OS Updates

You are returned to the :guilabel:`Main Menu`.

Save Configuration Settings
===========================

#. In Advanced Options, select :guilabel:`Save Configuration Settings`.

#. A dialogue box shows the installation configuration was saved to
   :file:`clr-installer.yaml`

   .. figure:: /_figures/bare-metal-install-server/bare-metal-install-server-31.png
      :scale: 100%
      :alt: Automatic OS Updates

      Figure 31: Automatic OS Updates

#. Use the :file:`clr-installer.yaml` file to install |CL|, with the same
   configuration, on multiple targets.

Finish installation
*******************

#. When you are satisfied with your installation configuration, navigate to
   :guilabel:`Install` and select :kbd:`Enter`.

   .. figure:: /_figures/bare-metal-install-server/bare-metal-install-server-32.png
      :scale: 100%
      :alt: Select Install

      Figure 32: Select Install

#. Select :guilabel:`reboot`.

   .. note::

      If you do not assign an administrative user, upon rebooting,
      enter `root` and set the root password immediately.

#. When the system reboots, remove any installation media present.

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

   * - ``VFAT(FAT32)``
     - boot
     - /boot
     - 150MB

   * - ``linux-swap``
     - swap
     -
     - 256MB

   * - ``ext[234] or XFS``
     - root
     - /
     - *Size depends upon use case/desired bundles.*

Troubleshooting
***************

For Configure Installation Media
================================

If a warning message appears that no media or space is available after
entering :guilabel:`Configure Installation Media`:

- Verify that target media has enough free space.

- Confirm the USB is properly connected to and mounted on target media.

- Review the size of existing partitions on the target media:

  - Linux\* OS: :command:`lsblk -a`
  - Windows\* OS:  :command:`diskpart`, then :command:`list disk`
  - macOS\* platform: :command:`diskutil list`

.. _Downloads: https://clearlinux.org/downloads
