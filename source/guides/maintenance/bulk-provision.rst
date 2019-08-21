.. _bulk-provision:

Bulk provision
##############

This guide explains how to perform a bulk provision of |CL-ATTR| using a
combination of the |CL| installer, Ister, and
:abbr:`ICIS (Ister Cloud Init Service)`.

.. contents::
   :local:
   :depth: 1

Overview
********

To configure a bulk provision:

* Define Ister configuration files to customize the installation process
* Define cloud-init\* files to customize the installation instance
* Host the configuration files in ICIS to allow Ister to use them during
  the installation

Figure 1 depicts the flow of information between a PXE server and a PXE
client that needs to be set up to perform a bulk provision.

.. figure:: ./figures/bulk-provision-flow.png
   :alt: Bulk provision information flow

   Figure 1: Bulk provision information flow

Prerequisites
*************

Before performing a bulk provision, verify you have a PXE server capable
of performing network boots of |CL|. Please refer to our
:ref:`guide on how to perform an iPXE boot<ipxe-install>` using
:abbr:`NAT (network address translation)` for details.

Because a bulk provision relies on a reboot, ensure the following
preparations have been made:

* No existing disks are bootable.
* The network boot option must come immediately after the disk boot option
  on any computer performing the installation.

Configuration
*************

#. Install ICIS by following the getting started guide on the
   `ICIS`_ GitHub\* repository.

#. Create an Ister installation file and save it to the
   :file:`static/ister` directory within the web hosting directory for
   ICIS. The installation file is a JSON block and provides Ister
   with the steps it needs to perform an installation. The file outlines
   what partitions, file systems, and mount points Ister should set
   up. Lastly, the file outlines which bundles to install. See our
   :ref:`bundles` document for the list of available bundles. The
   following example shows the contents of an Ister installation file:

   .. code-block:: json

      {
          "DestinationType":"physical",
          "PartitionLayout":[
              {"disk":"sda", "partition":1, "size":"512M", "type":"EFI"},
              {"disk":"sda", "partition":2, "size":"512M", "type":"swap"},
              {"disk":"sda", "partition":3, "size":"rest", "type":"linux"}
          ],
          "FilesystemTypes":[
              {"disk":"sda", "partition":1, "type":"vfat"},
              {"disk":"sda", "partition":2, "type":"swap"},
              {"disk":"sda", "partition":3, "type":"ext4"}
          ],
          "PartitionMountPoints":[
              {"disk":"sda", "partition":1, "mount":"/boot"},
              {"disk":"sda", "partition":3, "mount":"/"}
          ],
          "Version":"latest",
          "Bundles":[
              "kernel-native",
              "os-core",
              "os-core-update",
              "os-cloudguest"
          ],
          "IsterCloudInitSvc":"http://192.168.1.1:60000/icis/"
      }

   .. important::

      Every Ister installation file hosted on ICIS must contain the
      the `IsterCloudInitSvc` parameter as well as the :command:`os-cloudguest`
      bundle. These entries allow Ister to customize an instance of of an
      install.

#. Create an Ister configuration file to define the location of the
   Ister installation file. Save it to the :file:`static/ister` directory
   within the web hosting directory of ICIS. The following example shows
   an Ister configuration file:

   .. code-block:: none

      template=http://192.168.1.1:60000/icis/static/ister/ister.json

#. Modify the iPXE boot script by adding a kernel parameter to the command line
   for booting the network image. Add the kernel parameter `isterconf` with
   the location of the Ister configuration file hosted on ICIS as the
   kernel parameter value.  The following example shows an iPXE boot script
   with the `isterconf` parameter:

   .. code-block:: none

      #!ipxe
      kernel linux quiet init=/usr/lib/systemd/systemd-bootchart initcall_debug tsc=reliable no_timer_check noreplace-smp rw initrd=initrd isterconf=http://192.168.1.1:60000/icis/static/ister/ister.conf
      initrd initrd
      boot

   .. note::

      After the network image of |CL| boots, Ister inspects the
      parameters used during boot in :file:`/proc/cmdline` to find the
      location of the Ister configuration file.

#. Write a cloud-init document to customize the instance of the installation
   according to your requirements. The `cloud-init`_ documentation provides a
   guide on how to write a cloud-init document. The guide covers the
   customization options provided by cloud-init after an installation.

#. Save the cloud-init document to the :file:`static/roles` directory within
   the web hosting directory for ICIS with the name of a role you would
   like to create. For example, a role may be "database", "web", or "ciao".

#. After creating the roles, also known as cloud-init files, assign roles to
   MAC addresses of PXE clients. To do so, modify the :file:`config.txt` file
   in the :file:`static` directory within the web hosting directory of ICIS.
   The following example shows an example assignment:

   .. code-block:: none

      # MAC address,role
      00:01:02:03:04:05,ciao

   If MAC addresses of PXE clients are not listed within the
   :file:`config.txt` file, a default role for those MAC address may be
   defined as follows:

   .. code-block:: none

      # MAC address,role
      default,ciao

#. Verify the following URLs are accessible on your local network:

   * \http://192.168.1.1:60000/icis/static/ister/ister.conf
   * \http://192.168.1.1:60000/icis/static/ister/ister.json
   * \http://192.168.1.1:60000/icis/get_config/<MAC address>
   * \http://192.168.1.1:60000/icis/get_role/<role>
   * \http://192.168.1.1:60000/ipxe/ipxe_boot_script.txt

#. Power on the PXE client and watch it boot and install |CL|.

#. Power-cycle the PXE client and watch it customize the |CL| installation.

**Congratulations!** You have successfully performed a bulk provision of |CL|.


.. _ICIS:
   https://github.com/clearlinux/ister-cloud-init-svc

.. _cloud-init:
   https://cloudinit.readthedocs.io
