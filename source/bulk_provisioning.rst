.. _bulk_provisioning:

Bulk Provisioning
#################

|CLOSIA| can be automatically provisioned in bulk using a combination of
Ister and :abbr:`ICIS (Ister Cloud Init Service)`.

Configurations for a bulk provision are made by defining Ister configuration
files and cloud-init files.  By hosting them with ``ICIS``, ``Ister`` can
use them during the install process.  Ister configuration files provide a way
to customize the install and cloud-init files provide a way to customize the
instance of the install.

The following diagram depics the flow of information between a PXE server and a
PXE client that needs to be set up to perform a bulk provision.

.. figure:: _static/images/bulk-provision-flow.png
   :alt: Bulk provision information flow

   Figure 1: Bulk provision information flow

This guide covers how to perform a bulk provision of |CL| with ``Ister`` and
``ICIS``.

Prerequisites
=============

Before performing a bulk provision, verify that you have a PXE server capable
of performing network boots of |CL|.  Reference
:ref:`network_boot` for a guide on how to perform an iPXE boot using
:abbr:`NAT (network address translation)`.

Because a bulk provision relies on a reboot, some additional requirements must
be met:

* Any existing disks must not be bootable
* The boot order for the computer performing an install must have the network
  boot option come immediately after the disk boot option

Configuration
=============

#. Install ``ICIS`` by following the getting started guide on the `ICIS GitHub
   repository`_.

#. Create an Ister install file and save it to the ``static/ister``
   directory within the web hosting directory for ``ICIS``.  This
   install file is a block of JSON and describes to ``Ister`` how to
   perform an installation.  It outlines what partitions, file systems, and
   mount points ``Ister`` should set up. It also outlines what bundles to
   install.  Reference :ref:`bundles_overview` for a list of installable
   bundles.  An Ister install file may look like the example below:

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

      Every Ister install file hosted by ``ICIS`` must contain the the
      ``IsterCloudInitSvc`` parameter as well as the ``os-cloudguest`` bundle.
      These allow ``Ister`` to customize an instance of of an install.

#. Create an Ister configuration file that defines the location of the Ister
   install file.  Save it to the ``static/ister`` directory within the web
   hosting directory for ``ICIS``.  An Ister configuration file may look like
   the example below:

   .. code-block::

      template=http://192.168.1.1:60000/icis/static/ister/ister.json

#. Direct ``Ister`` to the location of the Ister configuration file as hosted
   by ``ICIS`` by modifying the kernel command line of the iPXE boot script
   and adding an ``isterconf`` parameter.  After the network image of |CL|
   boots, ``Ister`` inspects the parameters used for network booting to find
   the location of the Ister configuration file.  With the ``isterconf``
   parameter an iPXE boot script may look like the example below:

   .. code-block::

      #!ipxe
      kernel linux quiet init=/usr/lib/systemd/systemd-bootchart initcall_debug tsc=reliable no_timer_check noreplace-smp rw initrd=initrd isterconf=http://192.168.1.1:60000/icis/static/ister/ister.conf
      initrd initrd
      boot

#. Create a cloud-init file that will customize the instance of the install.
   The `cloud-init Read the Docs`_ provides a guide on what may be configured
   after an install.  Save it to the ``static/roles`` directory within the web
   hosting directory for ``ICIS``.  Give the cloud-init file a name that
   resembles a role.  For example, a role may be "compute" or "web" or "ciao".

#. After creating roles (cloud-init files), define which roles to apply to
   which PXE clients by mapping them to the corrpsoinding MAC addresses of the
   PXE clients.  Define the mapping by modifying the :file:`config.txt` file
   in the ``static`` directory within the web hosting directory for ``ICIS``.
   A mapping may look like the example below:

   .. code-block::

      # MAC address,role
      00:01:02:03:04:05,ciao

   If the MAC address of a PXE client is not found within the
   :file:`config.txt` file, a default role mapping may be defined for un-
   mapped MAC addresses as follows:

   .. code-block::

      # MAC address,role
      default,ciao

#. Verify that the following URLs are accessible:
   
   * http://192.168.1.1/icis/static/ister/ister.conf
   * http://192.168.1.1/icis/static/ister/ister.json
   * http://192.168.1.1/icis/get_config/<MAC address>
   * http://192.168.1.1/icis/get_role/<role>
   * http://192.168.1.1/ipxe/ipxe_boot_script.txt

#. Power on the PXE client and watch it boot and install |CL|.
   
Congratulations! You have successfully performed a bulk provision of |CL|.


.. _ICIS GitHub repository:
   https://github.com/clearlinux/ister-cloud-init-svc

.. _cloud-init Read the Docs:
   https://cloudinit.readthedocs.io
