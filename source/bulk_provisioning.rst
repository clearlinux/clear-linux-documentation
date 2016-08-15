.. _bulk_provisioning:

Bulk Provisioning
=================

In the data center new machines are often landed in large groups. When dealing with large amounts of new hardware, data center admins need a way to install and configure these machines with a minimal amount of effort. In support of this use case the Clear Linux team has developed some tooling and instructions on how to bulk-load machines with Clear Linux using iPXE.

This bulk provisioning scenario is a variation on the Network Booting and installation scenario with some alterations to facillitate installing and configuring many hosts. The Clear Linux installer (Ister) was augmented to detect and find cloud-init configuration data during the install. If this data is found a cloud-init file is fetched and the host, after being rebooted by ister, uses micro config drive (ucf) to configure the host as directed by the cloud-init configuration file.

In our pilot of this workflow we used ucf to install the trust relationships for the host to be further managed by Ansible. The cloud-init configuration file was served by a simple little web-application that Ister knows how to query for host configuration data. This allowed us to power on one hundered machines, each of which picked up the Clear Linux installer via PXE, installed Clear Linux, rebooted, and came up ready to be managed through Ansible.

The web application that serves cloud-init configurations to Ister is uninspiringly named "Ister Cloud Init Service" (ICIS), and is available at github - https://github.com/clearlinux/ister-cloud-init-svc

One nice attribute of this system is that once the iPXE bits are created many installer behaviors can be configured without having to regenerate the iPXE bits.

System Architecture
~~~~~~~~~~~~~~~~~~~

The following diagrams illustrate the system architecture.

.. image:: _static/images/icis_pxe_diagram.png
    :align: center
    :alt: pxe-server-overview

As can be seen, ICIS is a web application (specifically a Flask application, hence managed by uwsgi under nginx) that can really run anywhere visible to hosts booting from PXE, though in our example we simply hosted it on the same system serving the pxe content.

The following diagram illustrates the flow of information between the pxe server and a host booting into the installer via pxe.

.. image:: _static/images/icis_installer_workflow.png
    :align: center
    :alt: pxe-icis-install-workflow

Configuration Overview
~~~~~~~~~~~~~~~~~~~~~~

Here is a high-level overview describing setting up and configuring a bulk provisioning solution.

* First, stand up an iPXE server as described in the :doc:`network boot <network_boot>` docs. Note that you will be generating your own artifacts to be served by PXE in a later step.

* Land `Ister Cloud Init Service <https://github.com/clearlinux/ister-cloud-init-svc>`_ on the pxe server. The README in the ICIS github repo has directions on how to install and configure.

* Generate the installer that will load and boot over PXE. Copy the relevant files into the appropriate location on the iPXE server.

  Use the `create_pxe.sh <https://github.com/bryteise/ister/blob/master/create_pxe.sh>`_ script to make this easy. Note this creates the pxe-installer from the "provision" installer in Clear Linux which is a touchless installer that takes all installation information from a config file. You can get this image from a given Clear Linux release by looking in https://download.clearlinux.org/releases/XXXX/clear/ where XXXX is a Clear Linux release number. Just download the image alongside the create_pxe.sh script and name it provision.img.

* Stage config files for ister that will govern Ister's behavior. This includes modifying the ipxe boot script to pass an additional parameter to the kernel.

  The magic that ties all of this together is that the pxe script conveys to ister the location of its configuration files via the kernel command line of the installer it kicks off. The kernel preserves its command line precisely, and ister inspects it via /proc/cmdline.

  Here is an example pxe script:

  .. code-block:: console

    #!ipxe
    kernel linux quiet rdinit=/usr/lib/systemd/systemd-bootchart initcall_debug tsc=reliable no_timer_check noreplace-smp rw initrd=initrd isterconf=http://192.168.1.1/static/ister/ister.conf
    initrd initrd
    boot

  When the pxe installer kicks off ister it will notice location of its conf file was given on the kernel command line and fetch the file. This file in turn tells ister where to get the json template file that describes partition schemes, and which version of Clear Linux to install. This means that so long as the contents of a release are compatible with the version of software update (swupd) in the installer, this pxe installer can be told to install a newer version of Clear Linux simply by tweaking the json on the web server instead of rolling an entire new installer.

  One other important piece of configuration data in the json configuration file is the location of an ICIS configuration service. Ister will query ICIS for a role using the MAC address of the network interface being used to communicate with the ICIS service. Ister will then fetch that specific cloud-init file and configure ucd to run on first-boot against that config file.

  The `Ister Cloud Init Service <https://github.com/clearlinux/ister-cloud-init-svc>`_ github repo has example ister configuration files under ``static/ister``.

  Here is an example ister-template.json file.

  .. code-block:: console

    {
      "DestinationType" : "virtual",
      "PartitionLayout" : [ { "disk" : "installer.img", "partition" : 1, "size" : "64M", "type" : "EFI" },
                          { "disk" : "installer.img", "partition" : 2, "size" : "2G", "type" : "linux" } ],
      "FilesystemTypes" : [ { "disk" : "installer.img", "partition" : 1, "type" : "vfat" },
                          { "disk" : "installer.img", "partition" : 2, "type" : "ext4" } ],
      "PartitionMountPoints" : [ { "disk" : "installer.img", "partition" : 1, "mount" : "/boot" },
                               { "disk" : "installer.img", "partition" : 2, "mount" : "/" } ],
      "Version": 6580,
      "Bundles": ["kernel-native", "os-installer", "os-core-update", "os-core", "os-core-dev", "bootloader"],
      "PostNonChroot": ["./installation-image-post-update-version.py"],
      "IsterCloudInitSvc": ["http://192.168.1.1/"]
    }

* Configure ICIS to map MAC addresses to role files appropriately. Note, it is possible to simply specify a "default" role for any unmatched MAC address, which is handy if all install targets are to be configured identically. Then create the role files, which are cloud-init configuration files.

* Final pre-flight check. Assuming your iPXE server is at 192.168.1.1, all of the following urls need to be working.

  - http://192.168.1.1/icis/static/ister/ister.conf
  - http://192.168.1.1/icis/static/ister/ister_config.json
  - http://192.168.1.1/icis/get_config/<MAC ADDR>
  - http://192.168.1.1/icis/get_role/<role returned from previous url>
  - http://192.168.1.1/ipxe_boot_script.txt

* Boot an iPXE client and watch Clear Linux install.
