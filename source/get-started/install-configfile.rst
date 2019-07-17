.. _install-configfile:

Install using clr-installer and a configuration file
####################################################

This page explains how to install |CL-ATTR| using the clr-installer tool
with a configuration file. The configuration file (:file:`clr-installer.yaml`)
can be reused to duplicate the same installation configuration on additional
machines.

.. contents::
   :local:
   :depth: 1

Prerequisites
*************

Ensure that your target system supports the installation:

* :ref:`system-requirements`
* :ref:`compatibility-check`

Process
*******

This guide describes two methods for using a configuration file with the
clr-installer tool. You can use either method to achieve the same goal. Choose
the method that works best for your setup.

If you are installing |CL| for the first time, we recommend Example 1.

To clone an existing |CL| setup on another system, we recommend Example 2.

Example 1
=========

This method uses a configuration file template to perform a new installation.

Perform the following steps:

#. Go to `Downloads`_ and download the latest Clear Linux OS Server image.

   For example:
   https://download.clearlinux.org/releases/30010/clear/clear-30010-live-server.iso.xz

#. Follow the instructions to :ref:`bootable-usb` based on your OS.

#. Boot up the USB thumb drive.
#. Select :guilabel:`Clear Linux OS` from the menu.
#. In the console window, log in as root and set a password.
#. Verify you have a network connection to the Internet and configure proxy
   settings if you're working behind a firewall.
#. Download a :file:`live-server.yaml` template.

   For example:

   .. code-block:: bash

      curl -O https://download.clearlinux.org/releases/30010/clear/config/image/live-server.yaml

#. Edit the template and change the settings as needed.

   Commonly-changed settings include:

.. _install-configfile-yaml-begin:

   #. Under *block-devices*, set “file: "/dev/sda"” or enter your preferred device.
   #. Under *targetMedia*, set the third partition size to “0” to use the entire disk space.
   #. Under *bundles*, add additional bundles as needed.
   #. Delete the *post-install* section unless you have post-installation scripts.
   #. Under *Version*, set a version number. To use the latest version, set to “0”.

   Commonly-changed settings are shown in lines 15, 34, 37, and 51 below.
   See `Installer YAML Syntax`_ for more details.

   .. code-block:: bash
      :linenos:
      :emphasize-lines: 14,15,34,37,51

		#clear-linux-config

		# c-basic-offset: 2; tab-width: 2; indent-tabs-mode: nil
		# vi: set shiftwidth=2 tabstop=2 expandtab:
		# :indentSize=2:tabSize=2:noTabs=true:

		# File:         developer-live-server.yaml
		# Use Case:     Live Image which boots into login prompt
		#               Optionally allows for installing Clear Linux OS
		#               using the TUI clr-installer by running clr-installer

		# switch between aliases if you want to install to an actual block device
		# i.e /dev/sda
		block-devices: [
		   {name: "bdevice", file: "/dev/sda"}
		]

		targetMedia:
		- name: ${bdevice}
		  type: disk
		  children:
		  - name: ${bdevice}1
		    fstype: vfat
		    mountpoint: /boot
		    size: "150M"
		    type: part
		  - name: ${bdevice}2
		    fstype: swap
		    size: "32M"
		    type: part
		  - name: ${bdevice}3
		    fstype: ext4
		    mountpoint: /
		    size: "0"
		    type: part

		bundles: [os-core, os-core-update, NetworkManager, clr-installer, vim]

		autoUpdate: false
		postArchive: false
		postReboot: false
		telemetry: false
		iso: true
		keepImage: true
		autoUpdate: false

		keyboard: us
		language: en_US.UTF-8
		kernel: kernel-native

		version: 30010

.. _install-configfile-yaml-end:

Start the installation with the command:

.. code-block:: bash

   clr-installer --config live-server.yaml

Example 2
=========

This method uses a saved configuration file from a previous installation,
which you can use to easily duplicate the installation on additional machines.

Perform the following steps:

#. Open a console window on a system where |CL| was installed to retrieve a
   copy of the configuration file.

#. In the console window, log in as root and enter your password.

#. Change directory to :file:`/root` and copy the :file:`clr-installer.yaml`
   file to a USB thumb drive.

   .. code-block:: bash

   	  cd /root
   	  cp clr-installer.yaml <USB-thumb-drive>

Start the installation on the target with the following steps:

#. Go to `Downloads`_ and download the latest Clear Linux OS Server image.

   For example:
   https://download.clearlinux.org/releases/30010/clear/clear-30010-live-server.iso.xz

#. Follow the instructions to :ref:`bootable-usb` based on your OS.

#. Boot up the USB thumb drive.
#. Select :guilabel:`Clear Linux OS` from the menu.
#. In the console window, log in as root and set a password.
#. Verify you have a network connection to the Internet and configure proxy
   settings if you're working behind a firewall.
#. Plug in and mount the USB thumb drive containing the retrieved
   :file:`clr-installer.yaml` configuration file.
#. Start the installation with the command:

   .. code-block:: bash

      clr-installer --config clr-installer.yaml

References
**********

* `Clear Linux Installer`_
* `Installer YAML Syntax`_

.. _Downloads: https://clearlinux.org/downloads
.. _Clear Linux Installer: https://github.com/clearlinux/clr-installer

.. _Installer YAML Syntax: https://github.com/clearlinux/clr-installer/blob/master/scripts/InstallerYAMLSyntax.md