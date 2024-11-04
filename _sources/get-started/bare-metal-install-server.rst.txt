.. _bare-metal-install-server:

Install |CL-ATTR| from the live server
######################################

This page explains how to install |CL-ATTR| on bare metal from a bootable USB
drive using a live server image. Alternatively, use a :ref:`YAML configuration file <install-configfile>` to install |CL|. 

.. contents::
   :local:
   :depth: 1

System requirements
*******************

Before installing |CL|, verify that the host system supports the
installation:

* Requires 4 GB or more disk space
* :ref:`system-requirements`
* :ref:`compatibility-check`

Preliminary steps
*****************

#. Visit our `Downloads`_ page.

#. Download the file :file:`clear-<release number>-live-server.iso`,
   also called the |CL| Server.

   .. note::

      <release-number> is the latest |CL| auto-numbered release.

#. Follow your OS instructions to
   :ref:`create a bootable usb drive <bootable-usb>`.

Install |CL| on your target system
**********************************

Ensure that your system is configured to boot UEFI. The installation method
described below requires a wired or wireless Internet connection with DHCP.

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

Choose boot menu option
=======================

#. Choose one of the options shown in Figure 1.

   a. Follow `Verify integrity of installer media (optional)`_.

   #. Select :guilabel:`Clear Linux OS` in the boot menu.

   .. figure:: /_figures/bare-metal-install-server/bare-metal-install-server-01.png
      :scale: 100%
      :alt: Clear Linux OS Installer boot menu

      Figure 1: Clear Linux OS Installer boot menu

   .. note::

      If no action is taken, the live image starts by default.

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

.. _install-clr-server-start:

Launch the |CL| Installer
*************************

#. At the :guilabel:`login` prompt, enter :command:`root`.

#. Follow the onscreen instructions, shown in Figure 2, and
   enter a temporary password.

   .. figure:: /_figures/bare-metal-install-server/bare-metal-install-server-02.png
      :scale: 100%
      :alt: root login

      Figure 2: root login

  .. note::

      If a wireless connection is needed, connect to the network using
      :command:`nmtui` before lauching the installer. See the documentation on
      :ref:`configuring Wifi with nmtui <wifi-nm-tui>` for more details.

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
and :guilabel:`[A] Advanced options`. Navigate between tabs using these shortcut keys:

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
   * `Advanced Installation`_

   .. figure:: /_figures/bare-metal-install-server/bare-metal-install-server-08.png
      :scale: 100%
      :alt: Select Installation Media

      Figure 8: Select Installation Media

#. Select :guilabel:`Rescan Media` to show available installation targets.

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

Advanced Installation
---------------------

Use this method to manually configure partitions using `cgdisk`.
This example uses the `Default partition schema`_. The space you allocate for
your ``root``, or additional partitions, may vary.

#. Navigate to :guilabel:`Advanced Installation` and press :kbd:`Spacebar`.

   .. figure:: /_figures/bare-metal-install-server/bare-metal-install-server-09.png
      :scale: 100%
      :alt: Advanced installation

      Figure 9: Advanced installation

#. If no target media appears, select :kbd:`Rescan Media`.

#. Navigate to :guilabel:`Partition` and and press :kbd:`Spacebar`
   to launch `cgdisk`.

Partition codes
---------------

* ef00 - EFI System
* 8200 - Linux swap
* 8300 - Linux filesystem

boot partition
--------------

#. With the free space highlighted in the cgdisk utility, select
   :guilabel:`[New]`.

   .. figure:: /_figures/bare-metal-install-server/bare-metal-install-server-10.png
      :scale: 100%
      :alt: Select New

      Figure 10: Select New

   .. note::

      The `/boot` partition must be `VFAT(FAT32)`.

#. Where :guilabel:`First sector` appears, press :kbd:`Enter`.

#. For :guilabel:`Size in sectors`, type 150M.

   .. figure:: /_figures/bare-metal-install-server/bare-metal-install-server-11.png
      :scale: 100%
      :alt: Size in sectors

      Figure 11: Size in sectors

#. Press `Enter`.

#. Enter the hex code `ef00` and press :kbd:`Enter`.

   .. figure:: /_figures/bare-metal-install-server/bare-metal-install-server-12.png
      :scale: 100%
      :alt: `ef00` partition code

      Figure 12: `ef00` partition code

#. For the partition name, enter `CLR_BOOT`, the EFI boot partition.

   .. figure:: /_figures/bare-metal-install-server/bare-metal-install-server-13.png
      :scale: 100%
      :alt: CLR_BOOT

      Figure 13: CLR_BOOT

   .. note::

      Encryption is not allowed on the CLR_BOOT partition.

Now follow the same process to configure the remaining partitions.

swap partition (optional)
-------------------------

A swapfile is generated by default during installation. However, if you
prefer to create a swap partition, follow the steps below. 

#. Use the :kbd:`Up/Down` arrow to select free space.

#. Select :guilabel:`[New]` at bottom and press :kbd:`Enter`.

#. Under :guilabel:`First sector`, press :kbd:`Enter`.

#. For :guilabel:`Size in sectors`, type 256M, and press :kbd:`Enter`.

#. Enter the hex code `8200` and press :kbd:`Enter`.

#. In :guilabel:`Enter new partition name...`, type CLR_SWAP.

#. Press :kbd:`Enter`.

root partition
--------------

#. Use the :kbd:`Up/Down` arrow to select free space.

#. Select :guilabel:`[New]` at bottom and press Enter.

#. Under :guilabel:`First sector`, press Enter.

#. For :guilabel:`Size in sectors`, type in desired size.
   Optionally, press :kbd:`Enter` to use the remaining space available.

#. Press Enter.

#. Enter the hex code `8300` and press :kbd:`Enter`.

#. In :guilabel:`Enter new partition name...`, type: CLR_ROOT.
   The `/root` partition must be `ext[234]`, `XFS`,  or `f2fs`.
   If no filesystem exists, the installer will default to `VFAT(FAT32)`
   for `/boot`, and `ext4` for all others.

   .. note::

      You may also append `_F` to the partition name to force the formatting.

      *  `CLR_ROOT_F`: Force the formatting of the root partition prior to
          use.

      *  `CLR_F_SWAP`: Force the formatting of the swap partition prior to
          use; helpful when re-using a partition for swap which was previously formatted for a file system.

      *  `CLR_F_MNT_/data`: Force the formatting of the extra data
          partition prior to use

#. Press :kbd:`Enter`.

#. After all partitions are defined, verify that your partition
   configuration is similar to Figure 14.

   .. figure:: /_figures/bare-metal-install-server/bare-metal-install-server-14.png
      :scale: 100%
      :alt: Final partition configuration

      Figure 14: Final partition configuration

Additional partitions (optional)
--------------------------------

#. Use the :kbd:`Up/Down` arrow to select free space.

#. Now select :guilabel:`[New]` at bottom and press Enter.

#. Under :guilabel:`First sector`, press Enter.

#. For :guilabel:`Size in sectors`, type in desired size.

   .. note::

      If you do not specify a size, it will use the remaining space.

#. Press :kbd:`Enter`.

#. Enter the hex code `8300`. Then press :kbd:`Enter`.

#. In :guilabel:`Enter new partition name...`, type: `CLR_MNT_<mount_point>`.
   For example, replace <mount_point> with `/home`, shown in Figure 15.

   .. figure:: /_figures/bare-metal-install-server/bare-metal-install-server-15.png
      :scale: 100%
      :alt: CLR_MNT

      Figure 15: CLR_MNT

   .. note::

      If formatting is desired, the `_F` **must precede** `_MNT`.

#. Alternatively, you may create `CLR_MNT_/srv` or other partitions.

Write configuration to disk
---------------------------

#. When you're satisfied with the partition configuration, press the
   Right Arrow until :guilabel:`[Write]` is highlighted.

#. Press :kbd:`Enter`.

#. When the prompt appears asking if you want to write the partition table
   to disk, type "yes".

#. Finally, select :guilabel:`[Quit]`.

Disk encryption
===============

For greater security, disk encryption is supported using LUKS for the
any partition except `/boot` on |CL|. To encrypt the root partition, see the
example below. Encryption is optional.

Encryption Passphrase
---------------------

|CL| uses a single passphrase for encrypted partitions. Additional keys may
be configured post-installation using the ``cryptsetup`` tool.

#. Optional: Select :guilabel:`[X] Enable encryption` to encrypt the root
   partition, as shown in Figure 16.

   .. figure:: /_figures/bare-metal-install-server/bare-metal-install-server-16.png
      :scale: 100%
      :alt: Encrypt partition

      Figure 16: Encrypt partition

#. The :guilabel:`Encryption Passphrase` dialog appears.

   .. note::

      Minimum length is 8 characters. Maximum length is 94 characters.

   .. figure:: /_figures/bare-metal-install-server/bare-metal-install-server-17.png
      :scale: 100%
      :alt: Encryption Passphrase

      Figure 17: Encryption Passphrase

#. Enter the same passphrase in the first and second field.

#. Navigate to :guilabel:`Confirm` and press :kbd:`Enter`.

   .. note::

      :guilabel:`Confirm` is only highlighted if passphrases match.

Manage User
===========

Add New User
------------

#. In Required Options, select :guilabel:`Manage User`.

#. Select :guilabel:`Add New User` as shown in Figure 18.

   .. figure:: /_figures/bare-metal-install-server/bare-metal-install-server-18.png
      :scale: 100%
      :alt: Add New User, User Name

      Figure 18: Add New User

#. Optional: Enter a :guilabel:`User Name`.

   .. note:

      The User Name must be alphanumeric and can include spaces, commas,
      underscores or hyphens. Maximum length is 64 characters.

   .. figure:: /_figures/bare-metal-install-server/bare-metal-install-server-19.png
      :scale: 100%
      :alt: User Name

      Figure 19: User Name

#. Enter a :guilabel:`Login`.

   .. note::

      The User Login must be alphanumeric and can include hyphens and underscores. Maximum length is 31 characters.

#. Enter a :guilabel:`Password`.

   .. note:

      Minimum length is 8 characters. Maximum length is 255 characters.

#. In :guilabel:`Confirm`, enter the same password.

#. The :guilabel:`Administrator` checkbox is selected by default.

   .. note::

      Selecting Administrator enables sudo privileges for the user. For the installation to proceed, at least one user must be assigned as an Administrator.

#. Select :kbd:`Confirm`. To reset the form, select :guilabel:`Reset`.

#. In :guilabel:`Manage User`, navigate to :guilabel:`Confirm`.

#. With :guilabel:`Confirm` highlighted, select :kbd:`Enter`.

Modify / Delete User
--------------------

#. In :guilabel:`Manage User`, navigate to the user you wish
   to modify until highlighted, as shown in Figure 20.

#. Select :kbd:`Enter` to modify the user.

   .. figure:: /_figures/bare-metal-install-server/bare-metal-install-server-20.png
      :scale: 100%
      :alt: Modify User

      Figure 20: Modify User

#. Modify user details as desired.

#. Navigate to :kbd:`Confirm` until highlighted.

   .. note::

      Optional: Select :guilabel:`Reset` to rest the form.

#. Select :guilabel:`Confirm` to save the changes you made.

#. Optional: In :guilabel:`Modify User`, to delete the user, navigate to
   the :guilabel:`Delete` button and select :kbd:`Enter`.

   .. figure:: /_figures/bare-metal-install-server/bare-metal-install-server-21.png
      :scale: 100%
      :alt: Delete User

      Figure 21: Delete User

You are returned to :guilabel:`Manage User`.

#. Navigate to :kbd:`Confirm` until highlighted.

#. Select :guilabel:`Enter` to complete :guilabel:`Manage User` options.

Telemetry
=========

:ref:`telem-guide` is a |CL| feature that reports failures and crashes to
the |CL| development team for improvements.

Select your desired option on whether to participate in telemetry.

#. In the Main Menu, navigate to :guilabel:`Telemetry` and select
   :kbd:`Enter`.

#. Select :kbd:`Tab` to highlight your choice.

#. Select :kbd:`Enter` to confirm.

   .. figure:: /_figures/bare-metal-install-server/bare-metal-install-server-22.png
      :scale: 100%
      :alt: Enable Telemetry

      Figure 22: Enable Telemetry

Recommended options
*******************

After you complete the `Required options`_, we highly recommend completing
some `Advanced options`_:

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

   .. figure:: /_figures/bare-metal-install-server/bare-metal-install-server-23.png
      :scale: 100%
      :alt: Configure Network Interfaces

      Figure 23: Configure Network Interfaces

#. Notice :guilabel:`Automatic / dhcp` is selected by default (at bottom).

   Optional: Navigate to the checkbox :guilabel:`Automatic / dhcp` and select
   :kbd:`Spacebar` to deselect.

   .. figure:: /_figures/bare-metal-install-server/bare-metal-install-server-24.png
      :scale: 100%
      :alt: Network interface configuration

      Figure 24: Network interface configuration

#. Navigate to the appropriate fields and assign the desired
   network configuration.

#. To save settings, navigate to :guilabel:`Confirm` and select
   :kbd:`Enter`.

   .. note::

      To revert to previous settings, navigate to the :guilabel:`Cancel`
      and select :kbd:`Enter`.

#. Upon confirming network configuration, the :guilabel:`Testing Networking`
   dialog appears. Assure the result shows success. If a failure occurs,
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

   .. figure:: /_figures/bare-metal-install-server/bare-metal-install-server-25.png
      :scale: 100%
      :alt: Configure the network proxy

      Figure 25: Configure the network proxy

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

.. note::
   If using the :command:`off-line installer`, this option is not available.

A progress bar appears as shown in Figure 26.

.. figure:: /_figures/bare-metal-install-server/bare-metal-install-server-26.png
   :scale: 100%
   :alt: Testing Networking dialog

   Figure 26: Testing Networking dialog

.. note::

   Any changes made to network settings are automatically tested
   during configuration.

Optional: Skip to `Finish installation`_.

Select Additional Bundles
=========================

This option is only available with a valid network connection.
Bundle selection is disabled if no network connection exists.

#. On the Advanced menu, select :guilabel:`Select Additional Bundles`.

#. Navigate to the desired bundle using :kbd:`Tab` or :kbd:`Up/Down` arrows.

#. Select :kbd:`Spacebar` to select the checkbox for each desired bundle.

   .. figure:: /_figures/bare-metal-install-server/bare-metal-install-server-27.png
      :scale: 100%
      :alt: Bundle Selection

      Figure 27: Bundle Selection

#. Optional: To start developing with |CL|, we recommend
   adding :file:`os-clr-on-clr`.

#. Navigate to and select :kbd:`Confirm`.

   You are returned to the :guilabel:`Advanced options` menu.

Optional: Skip to `Finish installation`_.

Assign Hostname
===============

#. In Advanced Options, select :guilabel:`Assign Hostname`.

#. In :guilabel:`Hostname`, enter the hostname only (excluding the domain).

   .. note::

      Hostname does not allow empty spaces. Hostname must start with an
      alphanumeric character but may also contain hyphens. Maximum length of
      63 characters.

   .. figure:: /_figures/bare-metal-install-server/bare-metal-install-server-28.png
      :scale: 100%
      :alt: Assign Hostname

      Figure 28: Assign Hostname

#. Navigate to :kbd:`Confirm` until highlighted.

#. Select :kbd:`Confirm`.

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

   .. figure:: /_figures/bare-metal-install-server/bare-metal-install-server-29.png
      :scale: 100%
      :alt: Kernel Command Line

      Figure 29: Kernel Command Line

#. Choose from the following options.

   * To add arguments, enter the argument in :guilabel:`Add Extra Arguments`.

   * To remove an argument, enter the argument in
     :guilabel:`Remove Arguments`.

#. Select :kbd:`Confirm`.

Optional: Skip to `Finish installation`_.

Kernel Selection
================

#. Select a kernel option. By default, the latest kernel release is
   selected. Native kernel is shown in Figure 30.

#. To select a different kernel, navigate to it using :guilabel:`Tab`.

   .. figure:: /_figures/bare-metal-install-server/bare-metal-install-server-30.png
      :scale: 100%
      :alt: Kernel selection

      Figure 30 Kernel selection

#. Select :kbd:`Spacebar` to select the desired option.

#. Navigate to :kbd:`Confirm` and select :kbd:`Enter`.

Optional: Skip to `Finish installation`_.

Swupd Mirror
============

If you have your own custom mirror of |CL|, you can add its URL.

#. In Advanced Options, select :guilabel:`Swupd Mirror`.

#. To add a local swupd mirror, enter a valid URL in :guilabel:`Mirror URL:`

#. Select :kbd:`Confirm`.

   .. figure:: /_figures/bare-metal-install-server/bare-metal-install-server-31.png
      :scale: 100%
      :alt: Swupd Mirror

      Figure 31: Swupd Mirror

Optional: Skip to `Finish installation`_.

Automatic OS Updates
====================

Automatic OS updates are enabled by default. In the rare case that you
need to disable automatic software updates, follow the onscreen instructions,
shown in Figure 32.

#. In Advanced Options, select :guilabel:`Automatic OS Updates`.

#. Select the desired option.

   .. figure:: /_figures/bare-metal-install-server/bare-metal-install-server-32.png
      :scale: 100%
      :alt: Automatic OS Updates

      Figure 32: Automatic OS Updates

You are returned to the :guilabel:`Main Menu`.

Save Configuration Settings
===========================

#. In Advanced Options, select :guilabel:`Save Configuration Settings`.

#. A dialog box shows the installation configuration was saved to
   :file:`clr-installer.yaml`

   .. figure:: /_figures/bare-metal-install-server/bare-metal-install-server-33.png
      :scale: 100%
      :alt: Save configuration to YAML file

      Figure 33: Save configuration to YAML file

#. Use the :file:`clr-installer.yaml` file to install |CL|, with the same
   configuration, on multiple targets.

Finish installation
*******************

#. When you are satisfied with your installation configuration, navigate to
   :guilabel:`Install` and select :kbd:`Enter`.

   .. figure:: /_figures/bare-metal-install-server/bare-metal-install-server-34.png
      :scale: 100%
      :alt: Select Install

      Figure 34: Select Install

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

   * - ``ext[234], `XFS`, or f2fs``
     - root
     - /
     - *Size depends upon use case/desired bundles.*

.. note:: 
   
   A 64MiB swapfile is generated by default. The default size may be set
   manually with the ``--swap-file-size`` command-line option.

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

.. _erase-lvm-troubleshooting-tip:

Erase LVM Partitions Before Installing |CL|
===========================================

If you’re planning to install |CL| on a drive that has LVM partitions, 
you must erase them first before using the clr-installer.  

Here is an example of a drive (/dev/sda) with LVMs:

.. code-block:: console
   :emphasize-lines: 6-9

   NAME         MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
   loop0          7:0    0 627.6M  1 loop 
   sda            8:0    0 335.4G  0 disk 
   ├─sda1         8:1    0   200M  0 part 
   ├─sda2         8:2    0     1G  0 part 
   └─sda3         8:3    0 334.2G  0 part 
     ├─LVM-root 252:0    0    70G  0 lvm  
     ├─LVM-home 252:1    0 248.4G  0 lvm  
     └─LVM-swap 252:2    0  15.7G  0 lvm  

If you do not erase the LVMs first, you will encounter a clr-installer 
error like this: 
 
.. code-block:: console

   root@clr-live~ # clr-installer

   Please report this crash using GitHub Issues:
   https://github.com/clearlinux/clr-installer/issues

   Include the following as attachments to enable diagnosis:
   /root/pre-install-clr-installer.yaml
   /root/clr-installer.log

   You may need to remove any personal data of concern from the attachments.
   The Installer will now exit.
   exit status 1

   Error Trace:
   errors.Wrap()
        errors/errors.go:91
   storage.makeFs()
        storage/ops.go:79

The quickest and simplest method to erasing the LVMs is to execute these
commands:

.. code-block:: bash

   sudo sgdisk -Z /dev/<device>
   sudo partprobe
   sudo dmsetup remove_all --force
   sudo partprobe

Related topics
**************

* :ref:`install-configfile`


.. _Downloads: https://clearlinux.org/downloads


