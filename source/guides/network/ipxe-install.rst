.. _ipxe-install:

Install over the network with iPXE
##################################

This guide describes how to install |CL-ATTR| using :abbr:`PXE (Pre-boot
Execution Environment)` over the network.

.. contents::
   :local:
   :depth: 1

Overview
********

PXE is an industry standard that describes client-server interaction with
network-boot software and uses the DHCP and TFTP protocols. This guide shows one
method of using the PXE environment to install |CL|.

The PXE extension called `iPXE`_ adds support for additional protocols such as
HTTP, :abbr:`iSCSI (Internet Small Computer Systems Interface)`, :abbr:`AoE
(ATA over Ethernet\*)`, and :abbr:`FCoE (Fiber Channel over Ethernet\*)`. iPXE
enables network booting on computers with no built-in PXE support.

To install |CL| through iPXE, you must create a PXE client. Figure 1 depicts
the flow of information between a PXE server and a PXE client.

.. figure:: ./figures/network-boot-flow.png
   :alt: PXE information flow

   Figure 1: PXE information flow.

.. caution::

   The |CL| image that boots through the PXE process automatically erases all
   data and partitions on the PXE client system and creates 3 new partitions
   to install onto.

Prerequisites
*************

Before booting with iPXE, make the following preparations.

Connect the PXE server and PXE clients to a switch on a private network, as
shown in figure 2.

.. figure:: ./figures/network-boot-setup.png
   :alt: Network topology

   Figure 2: Network topology.

Your PXE client must have a boot order where the network boot option is
prioritized before the disk boot option.

Your PXE server must have:

* Ethernet/LAN boot option.
* At least two network adapters.
* Connection to a public network.
* Secure boot option disabled.

.. note::

   You must disable the secure boot option in the BIOS because the UEFI
   binaries used to boot |CL| are not signed.


Configuration
*************

To set up |CL| using iPXE automatically, use the :file:`configure-ipxe.sh`
script included with :abbr:`ICIS (Ister Cloud Init Service)`. For additional
instructions on the script, refer to the guide on the `ister-cloud-init-svc`_
GitHub\* repository.

To set up |CL| manually, perform the steps below.

#. Define the variables used for iPXE boot configuration.

   .. code-block:: console

      ipxe_app_name=ipxe
      ipxe_port=50000
      web_root=/var/www
      ipxe_root=$web_root/$ipxe_app_name
      tftp_root=/srv/tftp
      external_iface=eno1
      internal_iface=eno2
      pxe_subnet=192.168.1
      pxe_internal_ip=$pxe_subnet.1
      pxe_subnet_mask_ip=255.255.255.0
      pxe_subnet_bitmask=16

#. Log in and get root privilege.

   .. code-block:: bash

      sudo -s

#. Add the :command:`pxe-server` bundle to your |CL| system. The bundle contains all
   files needed to run a PXE server.

   .. code-block:: bash

      sudo swupd bundle-add pxe-server

#. Download the latest network-bootable release of |CL| and extract the
   files.

   .. code-block:: bash

      sudo mkdir -p $ipxe_root
      sudo curl -o /tmp/clear-pxe.tar.xz \
        https://cdn.download.clearlinux.org/current/clear-$(curl \
        https://cdn.download.clearlinux.org/latest)-pxe.tar.xz
      sudo tar -xJf /tmp/clear-pxe.tar.xz -C $ipxe_root
      sudo ln -sf $(ls $ipxe_root | grep 'org.clearlinux.*') $ipxe_root/linux

   .. note::

      Ensure that the initial ramdisk file is named :file:`initrd` and
      the kernel file is named :file:`linux`, which is a symbolic link to the
      actual kernel file.

#. Create an iPXE boot script with the following contents. During an iPXE
   boot, the iPXE boot script directs the PXE client to download the files to
   boot and install |CL|. Use the names previously given to the initial
   ramdisk and kernel files.

   .. code-block:: console

      sudo cat > $ipxe_root/ipxe_boot_script.ipxe << EOF
      #!ipxe
      kernel linux quiet init=/usr/lib/systemd/systemd-bootchart \
      initcall_debug tsc=reliable no_timer_check noreplace-smp rw \
      initrd=initrd
      initrd initrd
      boot
      EOF

#. The :command:`pxe-server` bundle contains a lightweight web-server known as
   nginx. Create a configuration file for nginx to serve |CL| to PXE
   clients with the following contents:

   .. code-block:: console

      sudo mkdir -p /etc/nginx/conf.d
      sudo cat > /etc/nginx/conf.d/$ipxe_app_name.conf << EOF
      server {
        listen $ipxe_port;
        server_name localhost;
        location /$ipxe_app_name/ {
          root $web_root;
          autoindex on;
        }
      }
      EOF

      sudo cp /usr/share/nginx/conf/nginx.conf.example /etc/nginx/nginx.conf

   .. note::

      Create a separate nginx configuration file to serve network-bootable
      images on a non-standard port number. This action saves existing nginx
      configurations.

#. Start nginx and enable the startup on boot option.

   .. code-block:: bash

      sudo systemctl start nginx
      sudo systemctl enable nginx

#. The :command:`pxe-server` bundle contains a lightweight DNS server which
   conflicts with the DNS stub listener provided in `systemd-resolved`.
   Disable the DNS stub listener and temporarily stop `systemd-resolved`.

   .. code-block:: console

      sudo mkdir -p /etc/systemd
      sudo cat > /etc/systemd/resolved.conf << EOF
      [Resolve]
      DNSStubListener=no
      EOF

      sudo systemctl stop systemd-resolved

#. Assign a static IP address to the network adapter for the private network
   and restart `systemd-networkd` with the following commands:

   .. code-block:: console

      sudo mkdir -p /etc/systemd/network
      sudo cat > /etc/systemd/network/70-internal-static.network << EOF
      [Match]
      Name=$internal_iface
      [Network]
      DHCP=no
      Address=$pxe_internal_ip/$pxe_subnet_bitmask
      EOF

      sudo systemctl restart systemd-networkd

#. Configure :abbr:`NAT (Network Address Translation)` to route traffic from
   the private network to the public network. This action makes the PXE
   server act as a router. To make these changes persistent during reboots, save the
   changes to the firewall with the following commands:

   .. code-block:: bash

      sudo iptables -t nat -F POSTROUTING
      sudo iptables -t nat -A POSTROUTING -o $external_iface -j MASQUERADE
      sudo systemctl enable iptables-save.service
      sudo systemctl restart iptables-save.service
      sudo systemctl enable iptables-restore.service
      sudo systemctl restart iptables-restore.service

   .. note::

      The firewall masks packets to make them appear as coming from the PXE
      server and hides PXE clients from the public network.

#. Configure the kernel to forward network packets to different
   interfaces. Otherwise, NAT will not work.

   .. code-block:: bash

      sudo mkdir -p /etc/sysctl.d
      sudo echo net.ipv4.ip_forward=1 > /etc/sysctl.d/80-nat-forwarding.conf
      sudo echo 1 > /proc/sys/net/ipv4/ip_forward

#. The :command:`pxe-server` bundle contains iPXE firmware images that allow computers
   without an iPXE implementation to perform an iPXE boot. Create a TFTP
   hosting directory and populate the directory with the iPXE firmware images
   with the following commands:

   .. code-block:: bash

      sudo mkdir -p $tftp_root
      sudo ln -sf /usr/share/ipxe/undionly.kpxe $tftp_root/undionly.kpxe

#. The :command:`pxe-server` bundle contains a lightweight TFTP, DNS, and DHCP
   server known as `dnsmasq`. Create a configuration file for `dnsmasq`
   to listen on a dedicated IP address for those functions. PXE clients on
   the private network will use this IP address.

   .. code-block:: console

      sudo cat > /etc/dnsmasq.conf << EOF
      listen-address=$pxe_internal_ip
      EOF

#. Add the options to serve iPXE firmware images to PXE clients over TFTP to
   the `dnsmasq` configuration file.

   .. code-block:: console

      sudo cat >> /etc/dnsmasq.conf << EOF
      enable-tftp
      tftp-root=$tftp_root
      EOF

#. Add the options to host a DHCP server for PXE clients to the :file:`dnsmasq`
   configuration file.

   .. code-block:: console

      sudo cat >> /etc/dnsmasq.conf << EOF
      dhcp-leasefile=/var/db/dnsmasq.leases

      dhcp-authoritative
      dhcp-option=option:router,$pxe_internal_ip
      dhcp-option=option:dns-server,$pxe_internal_ip

      dhcp-match=set:pxeclient,60,PXEClient*
      dhcp-range=tag:pxeclient,$pxe_subnet.2,$pxe_subnet.253,$pxe_subnet_mask_ip,15m
      dhcp-range=tag:!pxeclient,$pxe_subnet.2,$pxe_subnet.253,$pxe_subnet_mask_ip,6h

      dhcp-match=set:ipxeboot,175
      dhcp-boot=tag:ipxeboot,http://$pxe_internal_ip:$ipxe_port/$ipxe_app_name/ipxe_boot_script.ipxe
      dhcp-boot=tag:!ipxeboot,undionly.kpxe,$pxe_internal_ip
      EOF


   The configuration provides the following important functions:

   * Directs PXE clients without an iPXE implementation to the TFTP server
     to acquire architecture-specific iPXE firmware images that allow them
     to perform an iPXE boot.
   * Activates only on the network adapter that has an IP address on the
     defined subnet.
   * Directs PXE clients to the DNS server.
   * Directs PXE clients to the PXE server for routing via NAT.
   * Divides the private network into two pools of IP addresses. One pool
     is for network boot and one pool is used after boot. Each pool has
     their own lease times.

#. Create a file for `dnsmasq` to record the IP addresses it provides
   to PXE clients.

   .. code-block:: bash

      sudo mkdir -p /var/db
      sudo touch /var/db/dnsmasq.leases

#. Start `dnsmasq` and enable startup on boot.

   .. code-block:: bash

      sudo systemctl enable dnsmasq
      sudo systemctl restart dnsmasq

#. Start `systemd-resolved`.

   .. code-block:: bash

      sudo systemctl start systemd-resolved

   .. note::

      `systemd-resolved` dynamically updates the list of DNS servers for the
      private network if you use the `dnsmasq` DNS server. The setup creates a
      pass-through DNS server that relies on the DNS servers listed in
      :file:`/etc/resolv.conf`.

#. Power on the PXE client and watch the client boot and install |CL|.

   After booting, |CL| automatically partitions the hard drive,
   installs itself, updates to the latest version, and reboots.


**Congratulations!** You have successfully installed and configured a PXE
server that enables PXE clients to boot and install |CL| over the network.


.. _iPXE:
   http://ipxe.org/

.. _ister-cloud-init-svc:
   https://github.com/clearlinux/ister-cloud-init-svc
