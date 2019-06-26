.. _install-configfile:

Install using clr-installer and a configuration file
####################################################

This guide shows you how to install |CL-attr| using the clr-installer tool
with a configuration file. This method allows you to predefine configurations
and options, which are then fed into clr-installer, thus relieving you of
having to walkthrough the installer step by step. You can save the
configuration file and reuse it again.

System requirements
*******************

Ensure that your target system supports the installation:

* :ref:`system-requirements`
* :ref:`compatibility-check`

Process
*******

Perform the following steps:

#. Download the latest :file:`live-server.iso` file.

   For example:
   https://download.clearlinux.org/releases/29690/clear/clear-29690-live-server.iso.xz

#. Uncompress it and burn it to a USB thumb drive.
#. Boot up the USB thumb drive.
#. Select :guilabel:`Clear Linux OS` from the menu.
#. After it boots, press :guilabel:`<CTRL><Shift><F2>` to bring up a TTY console.
#. Log in as root and set a password.
#. Verify you have an IP address (network connection) and configure proxies (if needed).
#. Download an :file:`installer.yaml` template.

   For example:

   .. code-block:: bash

      # curl -O https://download.clearlinux.org/releases/29690/clear/config/image/installer.yaml

#. Edit the template and change the settings as needed. Commonly changed settings include:

   * Under *block-devices*, set “file: "/dev/sda"” or your preferred device.
   * Under *targetMedia*, set the 3rd partition size to “0” to use the entire disk space.
   * Under *bundles*, add additional bundles as needed.
   * Delete the *kernel-arguments* section unless you want to add kernel parameters.
   * Delete *post-install* section unless you have post installation scripts.
   * Under *Version*, set a version number. Use “0” for the latest version.

   .. code-block:: bash

   		# clear-linux-config

   		# c-basic-offset: 2; tab-width: 2; indent-tabs­mode: nil
   		# vi: set shiftwidth=2 tabstop=2 expandtab:
   		# :indentSize=2:tabSize=2:noTabs=true:

   		# File:  installer.yaml
   		# Use Case:  Base Text User Interface Installer
   		#
		# This YAML file generates the basic TUI installer image for
		# Clear Linux OS

		# switch between aliases if you want to install to an actual block device
		# i.e /dev/sda block-devices: [   {name: "installer", file: "/dev/sda"} ]

		targetMedia:
		- name: ${installer}  type: disk  children:
		- name: ${installer}1    fstype: vfat    mountpoint: /boot    size: "150M"   type: part
		- name: ${installer}2    fstype: swap    size: "256M"    type: part
  		- name: ${installer}3    fstype: ext4    mountpoint: /    size: "0"    type: part

		bundles: [os-core, os-core-update, clr­installer, NetworkManager]
		autoUpdate: false
		postArchive: false
		postReboot: false
		telemetry: false
		keyboard: us
		language: en_US.UTF-8
		kernel: kernel-native

		version: 28650

		#
		# Editor modelines  -  https://www.wireshark.org/tools/modelines.html
		#
		# Local variables:
		# c-basic-offset: 2
		# tab-width: 2
		# indent-tabs-mode: nil
		# End:
		#
		# vi: set shiftwidth=2 tabstop=2 expandtab:
		# :indentSize=2:tabSize=2:noTabs=true:
		#

#. Start the installation.

   .. code-block:: bash

   	  # clr-installer --config installer.yaml

References
**********

* `Clear Linux Installer`_
* `Installer YAML Syntax`_


.. _Clear Linux Installer: https://github.com/clearlinux/clr-installer

.. _Installer YAML Syntax: https://github.com/clearlinux/clr-installer/blob/master/scripts/InstallerYAMLSyntax.md