.. _install-configfile:

Install using clr-installer and a configuration file
####################################################

In addition to the interactive GUI and text-based modes,
:command:`clr-installer` also supports an unattended mode where you 
simply provide it a YAML configuration file.  

This guide shows you two examples of how to use its unattended mode.  

.. contents::
   :local:
   :depth: 1

Prerequisites
*************

For installation onto bare metal, ensure that your target system 
supports these requirements:

* :ref:`system-requirements`
* :ref:`compatibility-check`

Download and make bootable USB of the live server image
*******************************************************

See :ref:`bootable-usb`.

Example 1: Fresh installation onto bare metal
*********************************************

This example uses a YAML configuration file to perform a new installation.

#. Boot up the |CL| Live Server USB thumb drive.

#. Select :guilabel:`Clear Linux OS` from the menu.

#. In the console window, log in as `root` and set a password.

#. Verify you have a network connection to the Internet and configure proxy
   settings if you're working behind a firewall.

#. Download a sample YAML configuration file. For example, if you want to 
   install |CL| with a desktop GUI, you might want to use :file:`live-desktop.yaml`.
   Or you can use the :file:`live-server.yaml` if you want to install a non-GUI version
   of |CL|.

   * *Desktop:*

     .. code-block:: bash

        curl -O https://cdn.download.clearlinux.org/current/config/image/live-desktop.yaml

   * *Server:*

     .. code-block:: bash

        curl -O https://cdn.download.clearlinux.org/current/config/image/live-server.yaml

#. Edit the YAML configuration file and change the settings as needed.

   Commonly-changed settings include (refer to the example below):

   a. Under *block-devices* (line 15), set your target media.  For example: ``file: "/dev/sda"``.
   #. Under *targetMedia* (line 34), set the third partition size to “0” to use the entire disk space.
   #. Under *bundles* (line 37), add additional bundles as needed.
   #. Delete the *post-install* section unless you have post-installation scripts.
   #. Under *Version* (line 50), set a version number. To use the latest version, set to “0”.

   See `Installer YAML Syntax`_ for more details.

   .. code-block:: console
      :linenos:
      :emphasize-lines: 14,15,34,37,50

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

		keyboard: us
		language: en_US.UTF-8
		kernel: kernel-native

		version: 30010

#. Start the unattended installation using the `--config` option.

   .. code-block:: bash

      clr-installer --config live-server.yaml

#. Reboot your system after installation is completed.

Example 2: Replicate a previous installation
********************************************

This example uses a saved configuration file from a previous installation,
which you can use to easily clone the installation on additional machines
, ideally with the same hardware configuration.

.. warning::
   
   Be aware of the following when applying a saved configuration on a new machine:
   
   * Make sure the target media on the new machine matches up
   
   * The users' credentials will be replicated as well

#. On a system where |CL| was installed, open a terminal window.

#. Get root privilege.

   .. code-block:: bash

      sudo su

#. Copy the :file:`clr-installer.yaml` from :file:`/root` to a USB thumb drive.

   .. code-block:: bash

      cp /root/clr-installer.yaml <USB-thumb-drive>

#. Install on target system.

   a. Boot up the |CL| Live Server USB thumb drive.

   #. Select :guilabel:`Clear Linux OS` from the menu.

   #. In the console window, log in as `root` and set a password.

   #. Verify you have a network connection to the Internet and configure proxy
      settings if you're working behind a firewall.

   #. Plug in and mount the USB thumb drive containing the retrieved
      :file:`clr-installer.yaml` configuration file.
   
   #. Doublecheck to make sure the target media in the saved configuration file
      matches with the target system's. 

   #. Start the installation.

      .. code-block:: bash

         clr-installer --config clr-installer.yaml

   #. Reboot your system after installation is completed.

References
**********

* `Clear Linux Installer`_
* `Installer YAML Syntax`_

.. _Clear Linux Installer: https://github.com/clearlinux/clr-installer
.. _Installer YAML Syntax: https://github.com/clearlinux/clr-installer/blob/master/scripts/InstallerYAMLSyntax.md
