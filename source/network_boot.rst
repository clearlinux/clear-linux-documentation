.. _network_boot:

Network booting
################

Network booting is an important feature that every data center should have;
it can be used, among other things, to install an operating system. To do this,
a :abbr:`Pre-boot eXecution Environment (PXE)` is defined upon a foundation of
industry-standard Internet protocols and services, namely TCP/IP, DHCP, and
`TFTP <http://download.intel.com/design/archives/wfm/downloads/pxespec.pdf>`_.

.. tip::

  Clear Linux* Project for Intel® Architecture uses UEFI to boot, so your target
  machine should be UEFI capable. At present, the UEFI binary is not signed, so
  be sure to disable secure boot.

PXE + iPXE
===========

To retrieve data through other protocols such as HTTP, iSCSI, ATA over Ethernet
(AoE), and Fiber Channel over Ethernet (FCoE), an open source network boot
firmware called iPXE was created. iPXE provides a full PXE implementation,
enhanced with additional features. It can be used to enable network booting from
computers that lack built-in PXE support.

Clear Linux Project for Intel Architecture can be configured to do network
booting via HTTP with the help of iPXE. The following sets up an iPXE
environment using Clear Linux OS for Intel Architecture, but the configuration 
options may apply elsewhere. First, add the ``pxe-server`` bundle to your
system with:

.. code-block:: console

  # swupd bundle-add pxe-server


DHCP configuration
-------------------

To use PXE chainloading, set up ISC DHCPD to hand out ``undionly.kpxe`` to legacy
PXE clients and then hand out boot configuration only to iPXE clients. Do
this by telling ISC DHCPD to use different configurations based on the DHCP user class.
Here's one way to do this:

.. code-block:: console

  allow booting;
  allow bootp;

  # Set up a class to assign an IP only to devices is attempting network boot.
  class "pxeclients" {
          match if substring(option vendor-class-identifier, 0, 9) = "PXEClient";
          next-server 192.168.1.1;
          if exists user-class and option user-class = "iPXE" {
                  filename "http://my.web.server/real_boot_script.txt";
          } elsif exists client-arch and option client-arch = 9 {
                  # client-arch = 9 (64-bit EFI)
                  filename "ipxe.efi";
          } else {
                  # client-arch = 0 (Standard PC BIOS)
                  filename "undionly.kpxe";
          }
  }
  # Private subnet, in case you aren't able to run your own network wide DHCP service.
  # Works when the machine you are network booting has two network interfaces,
  # one connected to the private PXE boot network and the other connected to an external
  # network.
  subnet 192.168.1.0 netmask 255.255.255.0 {
          pool {
                  allow members of "pxeclients";
                  range 192.168.1.100 192.168.1.200;
          }
  }

This ensures that either iPXE image (undionly.kpxe for BIOS or ipxe.efi for EFI) is handed
out only when the DHCP request comes from a legacy PXE client or from a UEFI client. Once
iPXE loads, the DHCP server will direct it to boot from options configured in your
``http://my.web.server/real_boot_script.txt`` file, where ``my.web.server`` and the filename 
are replaced with your actual location.

The address ``192.168.1.1`` should be set to the address your TFTP server is using.

The subnet being used in this example is private; if the DHCPD service you use applies to your
entire network, modify the configuration as needed.

iPXE-specific options
-----------------------

There are several DHCP options specific to `iPXE <http://ipxe.org/>`_ which are not recognized by the standard ISC
dhcpd installation. To add support for these options, place the following at the start of your
:file:`/etc/dhcpd.conf`:

.. code-block:: console

  ###################################################
  #   iPXE-specific options                         #
  #   Source: http://www.ipxe.org/howto/dhcpd       #
  ###################################################
  option space ipxe;
  option ipxe-encap-opts code 175 = encapsulate ipxe;
  option ipxe.priority code 1 = signed integer 8;
  option ipxe.keep-san code 8 = unsigned integer 8;
  option ipxe.skip-san-boot code 9 = unsigned integer 8;
  option ipxe.syslogs code 85 = string;
  option ipxe.cert code 91 = string;
  option ipxe.privkey code 92 = string;
  option ipxe.crosscert code 93 = string;
  option ipxe.no-pxedhcp code 176 = unsigned integer 8;
  option ipxe.bus-id code 177 = string;
  option ipxe.bios-drive code 189 = unsigned integer 8;
  option ipxe.username code 190 = string;
  option ipxe.password code 191 = string;
  option ipxe.reverse-username code 192 = string;
  option ipxe.reverse-password code 193 = string;
  option ipxe.version code 235 = string;
  option iscsi-initiator-iqn code 203 = string;
  # Feature indicators
  option ipxe.pxeext code 16 = unsigned integer 8;
  option ipxe.iscsi code 17 = unsigned integer 8;
  option ipxe.aoe code 18 = unsigned integer 8;
  option ipxe.http code 19 = unsigned integer 8;
  option ipxe.https code 20 = unsigned integer 8;
  option ipxe.tftp code 21 = unsigned integer 8;
  option ipxe.ftp code 22 = unsigned integer 8;
  option ipxe.dns code 23 = unsigned integer 8;
  option ipxe.bzimage code 24 = unsigned integer 8;
  option ipxe.multiboot code 25 = unsigned integer 8;
  option ipxe.slam code 26 = unsigned integer 8;
  option ipxe.srp code 27 = unsigned integer 8;
  option ipxe.nbi code 32 = unsigned integer 8;
  option ipxe.pxe code 33 = unsigned integer 8;
  option ipxe.elf code 34 = unsigned integer 8;
  option ipxe.comboot code 35 = unsigned integer 8;
  option ipxe.efi code 36 = unsigned integer 8;
  option ipxe.fcoe code 37 = unsigned integer 8;
  option ipxe.vlan code 38 = unsigned integer 8;
  option ipxe.menu code 39 = unsigned integer 8;
  option ipxe.sdi code 40 = unsigned integer 8;
  option ipxe.nfs code 41 = unsigned integer 8;

Next, create an empty :file:`/var/db/dhcp.leases` file and start the dhcpd service with:

.. code-block:: console

  # mkdir -p /var/db
  # touch /var/db/dhcp.leases
  # systemctl start dhcp4.service

TFTP configuration
-----------------------

Clear Linux uses ``dnsmasq`` to provide the tftpd service. Modify
:file:`/etc/dnsmasq.conf` with the following required entries:

.. code-block:: console

  enable-tftp
  tftp-root=/srv/tftp/

Download the ``undionly.kpxe`` (legacy) and ``ipxe.efi`` (EFI) files from
`the iPXE website <http://boot.ipxe.org/>`_ and place them in your TFTP
directory. Then you can start the service with

.. code-block:: console

  # systemctl start dnsmasq.service


HTTP configuration
-----------------------

The kernel (linux), initramfs (initrd) and the iPXE scripts are transported
via HTTP. The Linux kernel and initrd files can be downloaded from
https://download.clearlinux.org/image/ where ``clear-$version-pxe.tar.xz`` is a
compressed tar file containing two clearly-labeled files that should be moved
to the http server root ``/var/www/pxe/``.

Create a configuration file for the http service (nginx in this example) to
serve the kernel and initramfs in :file:`/etc/nginx/nginx.conf` with the
following:

.. code-block:: console

  worker_processes  1;
  http {
      sendfile        on;
      keepalive_timeout  65;
      server {
          listen       80;
          server_name  hostname;
          server_name_in_redirect off;
          location / {
              root   /var/www/pxe;
              autoindex on;
              index  index.html index.htm;
          }
      }
  }

 And start the service with:

.. code-block:: console

  # systemctl start nginx.service


iPXE script
-----------------------

The iPXE script used is

.. code-block:: console

  #!ipxe

  kernel linux quiet rdinit=/usr/lib/systemd/systemd-bootchart initcall_debug
  tsc=reliable no_timer_check noreplace-smp rw initrd=initrd initrd initrd
  boot

This should be located in ``/var/www/pxe`` with the kernel and initrd.


PXE + grub
=======================

Another option for network booting Clear Linux OS for Intel Architecture is to use the GRUB bootloader
for booting in UEFI mode. The bootloader will get its files over TFTP and does
not require having another service to host the network boot artifacts. The
following sets up up a PXE using the GRUB bootloader environment and Clear Linux OS for Intel Architecture,
but the configuration options should apply elsewhere.

First add the pxe-server bundle to your system with:

.. code-block:: console

  # swupd bundle-add pxe-server


DHCP configuration
-----------------------

Add the following content to your :file:`/etc/dhcpd.conf` file:

.. code-block:: console

  allow booting;
  allow bootp;

  # Set up a class so you can give out an IP only for devices is attempting network boot.
   {
   match if substring(option vendor-class-identifier, 0, ;
          next-server 192.168.1.1;
   grubx64.
  }

  # Private subnet, in case you are able to run your own network wide DHCP service.
  # Works when the machine you are network booting has two network interfaces,
  # one connected to the private PXE boot network and the other connected to an external
  # network.
  subnet 192.168.1.0 netmask 255.255.255.0 {
          pool {
          allow members
                  range 192.168.1.100 192.168.1.200;
          }
  }


Where ``192.168.1.1`` is set to the address your TFTP server is using, and ``grubx64.efi`` is set
to the name of your grub bootloader file.

The subnet being used in this example is private; if the DHCPD service you use applies to your
entire network, modify the configuration as needed. Also, if multiple devices (including those
not using UEFI) are being supported by this DHCPD service, adding the following logic will allow
selection of the filename fetched from the client:

.. code-block:: console

  if exists client-arch and option client-arch = 9 {
          # client-arch = 9 (64-bit EFI)
          filename "grubx64.efi";
  } elsif exists client-arch and option client-arch = 6 {
          # client-arch = 6 (32-bit EFI)
          filename "grubx32.efi";
  } else {
          # client-arch = 0 (Standard PC BIOS)
          filename "pxelinux.0";
  }

Next create an empty :file:`/var/db/dhcp.leases` file and start the dhcpd service with:

.. code-block:: console

  # mkdir -p /var/db
  # touch /var/db/dhcp.leases
  # systemctl start dhcp4.service


GRUB configuration
-----------------------

Create the GRUB bootloader file (:file:`grubx64.efi`) with the following
command:

.. code-block:: console

  # grub-mkimage -O x86_64-efi -o grubx64.efi all_video boot btrfs cat
  chain configfile echo efifwsetup efinet ext2 fat font gfxmenu gfxterm
  gzio halt hfsplus iso9660 jpeg linuxefi loadenv loopback lvm mdraid09
  mdraid1x minicmd multiboot multiboot2 normal part_apple part_msdos
  part_gpt password_pbkdf2 png reboot search search_fs_uuid search_fs_file
  search_label serial sleep syslinuxcfg test tftp usbserial_pl2303
  usbserial_ftdi xfs

This file will then be placed in your current directory.

Next, a GRUB configuration file (:file:`grub.cfg`) should contain the
following content:

.. code-block:: console

  set pager=1

  export menuentry_id_option

  function load_video {
    if [ x$feature_all_video_module = xy ]; then
      insmod all_video
    else
      insmod efi_gop
      insmod efi_uga
      insmod ieee1275_fb
      insmod vbe
      insmod vga
      insmod video_bochs
      insmod video_cirrus
    fi
  }

  terminal_output console
  if [ x$feature_timeout_style = xy ] ; then
    set timeout_style=menu
    set timeout=5
  else
    set timeout=5
  fi

  menuentry 'Clear Linux Installation' --class gnu-linux --class gnu --class os {
    load_video
    set gfxpayload=keep
    insmod gzio
    insmod part_gpt
    insmod ext2
    linuxefi /linux
    initrdefi /initrd
  }

Where the Linux kernel is named "linux" and the initrd "initrd".


TFTP configuration
-----------------------

Clear Linux OS for Intel Archiecture uses ``dnsmasq`` to provide the tftpd service. It requires
the following entries exist in :file:`/etc/dnsmasq.conf`:

.. code-block:: console

  enable-tftp
  tftp-root=/srv/tftp/

The Linux kernel and initrd files can be downloaded from https://download.clearlinux.org/current/
(with a name clear-$version-pxe.tar.xz) as a compressed tar file containing two clearly-labeled
files that should be moved to the tftp root (``/srv/tftp/`` per the tftp server configuration),
as linux and initrd respectively. The bootloader :file:`grubx64.efi` and its configuration file
:file:`grub.cfg` should also be placed in the tftp root ``/srv/tftp/``.

Now start the tftp service with this command:

.. code-block:: console

  systemctl start dnsmasq.service
