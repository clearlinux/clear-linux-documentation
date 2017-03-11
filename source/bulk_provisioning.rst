.. _bulk_provisioning:

Bulk Provisioning
*****************

Data centers have a need to install and configure new instances of operating
systems in bulk. When managing new computers or hardware upgrades in bulk, data
center administrators need tooling for making changes with minimal effort.

The bulk provisioning scenario is a continuation of the :ref:`network_boot`
scenario.  After a network boot occurs, ``ister`` provides automation for this
task using `cloud-init`_ files by performing the following steps:

#. Finding cloud-init files
#. Creating a `micro-config-drive`_ (ucf) to store the cloud-init files
#. Creating a systemd service which runs at first reboot to apply the
   configurations defined by the cloud-init files
#. Reboots the machine to run the systemd service

At this point, the machine has been rebooted twice, once to perform a network
boot and once again to apply cloud-init configurations. Afte the second reboot,
the machine can enter into a mode ready to be managed with Ansible.

The ister cloud init service (`icis`_) is used by ister to host the cloud-init
configurations.  Ister can be directed to look for cloud-init configurations
hosted by icis.

One nice attribute of this system is that once the iPXE bits are created, many
installer behaviors can be configured without having to regenerate the iPXE
bits.

Prerequisites
=============

Stand up an iPXE server as described in the :ref:`network_boot`
docs. Note that you will be generating your own artifacts to be served by
PXE in a later step. 

Configuration
=============

The following diagram illustrates the flow of information between the pxe
server and a host booting into the installer via pxe. This diagram is intended
to show the logical flow of information, and is not a literal depiction of the
protocol-level exchanges.

.. image:: _static/images/bulk-provision-flow.png
    :align: center
    :alt: pxe-icis-install-workflow

Application server, web server, dhcp server, tftp server are hosted on a
single machine, but can be hosted anywhere visible to PXE clients.

#. Land `Ister Cloud Init Service <https://github.com/clearlinux/ister-cloud-
   init- svc>`_ on the pxe server. The README in the ICIS github repo has
   directions on how to install and configure.

#. Generate the installer that will load and boot over PXE. Copy the relevant
   files into the appropriate location on the iPXE server.

   A pxe installer is generated for every release of Clear Linux OS. It can be
   found alongside the published images in
   https://download.clearlinux.org/releases/XXXXX/clear/clear-XXXXX-pxe.tar.xz
  
   Alternatively, use the `create_pxe.sh
   <https://github.com/bryteise/ister/blob/master/create_pxe.sh>`_ script to
   roll your own. Note this creates the pxe-installer from the "provisioning"
   installer in Clear Linux.  This is a touchless installer that takes all
   installation information from a config file. You can get this image from a
   given Clear Linux release by looking in
   https://download.clearlinux.org/releases/XXXX/clear/ where XXXX is a Clear
   Linux release number. Just download the image alongside the
   ``create_pxe.sh`` script and name it ``provision.img``.
   
#. Stage config files for ``ister`` that will govern Ister's behavior. This
   includes modifying the script for ipxe boot, getting it to pass an
   additional parameter to the kernel.

   The magic that ties all of this together is that the pxe script conveys to
   ister the location of its configuration files via the kernel command line
   of the installer it kicks off. The kernel preserves its command line
   precisely, and ister inspects it via ``/proc/cmdline``.

   Here is an example pxe script:

   .. code-block:: console

    #!ipxe
    kernel linux quiet rdinit=/usr/lib/systemd/systemd-bootchart initcall_debug tsc=reliable 
    no_timer_check noreplace-smp rw initrd=initrd isterconf=http://192.168.1.1/icis/static/ister/ister.conf
    initrd initrd
    boot  

   When the pxe installer kicks off ``ister``, it will make note of the
   location of the ``conf`` file that was given on the kernel command line, and
   fetch the file. This file then tells ``ister`` where to get the json
   template file that describes partition schemes, and which version of Clear
   Linux to install. This means that so long as the contents of a release are
   compatible with the version of software update (``swupd``) in the installer,
   this pxe installer can be told to install a newer version of Clear Linux
   simply by tweaking the json on the web server, rather than rolling an
   entirely new installer.

   One other important piece of configuration data in the json configuration
   file is the location of an ICIS configuration service. Ister will query
   ICIS for a role using the MAC address of the network interface being used
   to communicate with the ICIS service. Ister will then fetch that specific
   :file:`cloud-init` file and ``configure ucd`` to run on first-boot against
   that config file.

   The `Ister Cloud Init Service <https://github.com/clearlinux/ister-cloud-init-svc>`_ github repo 
   has example ister configuration files under ``static/ister``.

   Here is an example ister-template.json file.

   .. code-block:: console

    {
      "DestinationType" : "phyiscal",
      "PartitionLayout" : [ { "disk" : "/dev/sda", "partition" : 1,
                              "size" : "64M", "type" : "EFI" },
                            { "disk" : "/dev/sda", "partition" : 2,
                              "size" : "2G", "type" : "linux" } ],
      "FilesystemTypes" : [ { "disk" : "/dev/sda", "partition" : 1, "type" : "vfat" },
                            { "disk" : "/dev/sda", "partition" : 2, "type" : "ext4" } ],
      "PartitionMountPoints" : [ { "disk" : "/dev/sda", "partition" : 1,
                                   "mount" : "/boot" },
                                 { "disk" : "/dev/sda", "partition" : 2,
                                   "mount" : "/" } ],
      "Version": 6580,
      "Bundles": ["kernel-native", "os-core-update", "os-core",
                  "bootloader", "sysadmin-hostmgmt", "openssh-server"],
      "PostNonChroot": ["./installation-image-post-update-version.py"],
      "IsterCloudInitSvc": ["http://192.168.1.1/icis/"]
    }

#. Configure ICIS to map MAC addresses to role files appropriately. Then create the role files, which 
   are ``cloud-init`` configuration files. Note, it is possible to simply specify a "default" role for 
   any unmatched MAC address; this may be handy when all install targets are to be configured identically.

#. Final pre-flight check. Assuming your iPXE server is at 192.168.1.1, all of the
   following urls need to be working:

   * http://192.168.1.1/icis/static/ister/ister.conf
   * http://192.168.1.1/icis/static/ister/ister_config.json
   * http://192.168.1.1/icis/get_config/<MAC ADDR>
   * http://192.168.1.1/icis/get_role/<role returned from previous url>
   * http://192.168.1.1/ipxe_boot_script.txt

#. Boot an iPXE client and watch Clear Linux install.


.. _icis: https://github.com/clearlinux/ister-cloud-init-svc
.. _cloud-init: https://cloudinit.readthedocs.io
.. _micro-config-drive: https://github.com/clearlinux/micro-config-drive