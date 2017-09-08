.. _ipxe-install:

Install Clear Linux over the network with iPXE
##############################################

This guide shows how to install |CL| through :abbr:`PXE (Pre-boot Execution Environment)`. 

PXE is an industry standard describing the client-server interaction with network-boot software using
the DHCP and TFTP protocols. This guide shows one possible use of this
environment to automatically install |CL|.

The PXE extension known as `iPXE`_\* adds support for additional protocols
such as HTTP, :abbr:`iSCSI (Internet Small Computer Systems Interface)`, :abbr:`AoE (ATA over Ethernet)`, and
:abbr:`FCoE (Fiber Channel over Ethernet)`. iPXE can also be used to enable
network booting on computers which lack built-in PXE support.

Figure 1 depicts the flow of information between a PXE server and a PXE
client we must create to install |CL| through iPXE.

.. figure:: ./figures/network-boot-flow.png
   :alt: PXE information flow

   Figure 1: PXE information flow

.. caution::

   The |CL| image that boots through the PXE process automatically erases all data and partitions on the PXE client system and
   creates 3 new partitions to install onto.

Prerequisites
*************

Before booting with iPXE, the following preparations must be made:

* Your PXE server has an Ethernet/LAN boot option.
* Your PXE server has at least two network adapters.
* Your PXE server is connected to a public network.
* Your PXE server and PXE clients are connected to a switch on a private
  network.
* Your PXE server has the secure boot option disabled.
* Your PXE clients have a boot order where the network boot option is
  prioritized before the disk boot option.

.. note::

   The ``Secure Boot`` option in the BIOS must be disabled because the UEFI binaries used to
   boot |CL| are not signed.

The required computer and network setup is shown in figure 2.

.. figure:: ./figures/network-boot-setup.png
   :alt: NAT network topology

   Figure 2: NAT network topology

Configuration
*************

The configuration process to install |CL| using iPXE has been automated with
the :file:`configure-ipxe.sh` script included with
:abbr:`ICIS (Ister Cloud Init Service)`, thus quickly enabling a bulk
provisioning setup. For additional instructions on how to get started with the
script, refer to the guide on the `ICIS GitHub repository`_. Otherwise, to
setup manually, follow the steps below.

#. Define the variables used to parameterize the configuration of an iPXE
   boot.

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

   .. code-block:: console

      $ sudo -s

#. Add the ``pxe-server`` bundle to your |CL| system. This bundle has all the
   files needed to run a PXE server.

   .. code-block:: console

      # swupd bundle-add pxe-server

#. Download the latest network-bootable release of |CL| and extract the
   files.

   .. code-block:: console

      # mkdir -p $ipxe_root
      # curl -o /tmp/clear-pxe.tar.xz \
        https://download.clearlinux.org/current/clear-$(curl \
        https://download.clearlinux.org/latest)-pxe.tar.xz
      # tar -xJf /tmp/clear-pxe.tar.xz -C $ipxe_root
      # ln -sf $(ls $ipxe_root | grep 'org.clearlinux.*') $ipxe_root/linux

   .. note::

      Ensure that the initial ramdisk file is named :file:`initrd` and
      the kernel file is named :file:`linux`, which is a symbolic link to the
      actual kernel file.

#. Create an iPXE boot script with the following contents. During an iPXE
   boot, the iPXE boot script directs the PXE client to download the files to
   boot and install |CL|. Use the names previously given to the initial
   ramdisk and kernel files.

   .. code-block:: console

      # cat > $ipxe_root/ipxe_boot_script.ipxe << EOF
      #!ipxe
      kernel linux quiet init=/usr/lib/systemd/systemd-bootchart \
      initcall_debug tsc=reliable no_timer_check noreplace-smp rw \
      initrd=initrd
      initrd initrd
      boot
      EOF

#. The ``pxe-server`` bundle contains a lightweight web-server known as
   ``nginx``. Create a configuration file for ``nginx`` to serve |CL| to PXE
   clients with the following contents:

   .. code-block:: console

      # mkdir -p /etc/nginx/conf.d
      # cat > /etc/nginx/conf.d/$ipxe_app_name.conf << EOF
      server {
        listen $ipxe_port;
        server_name localhost;
        location /$ipxe_app_name/ {
          root $web_root;
          autoindex on;
        }
      }
      EOF

      # cp /usr/share/nginx/conf/nginx.conf.example /etc/nginx/nginx.conf

   .. note::

      Creating a separate configuration file for ``nginx`` to serve
      network-bootable images on a non-standard port number preserves
      existing `nginx` configurations.

#. Start ``nginx`` and enable the startup on boot option.

   .. code-block:: console

      # systemctl start nginx
      # systemctl enable nginx

#. The ``pxe-server`` bundle contains a lightweight DNS server which
   conflicts with the DNS stub listener provided by ``systemd-resolved``.
   Disable the DNS stub listener and temporarily stop ``systemd-resolved``.

   .. code-block:: console

      # mkdir -p /etc/systemd
      # cat > /etc/systemd/resolved.conf << EOF
      [Resolve]
      DNSStubListener=no
      EOF

      # systemctl stop systemd-resolved

#. Assign a static IP address to the network adapter for the private network
   and restart ``systemd-networkd`` with the following commands:

   .. code-block:: console

      # mkdir -p /etc/systemd/network
      # cat > /etc/systemd/network/70-internal-static.network << EOF
      [Match]
      Name=$internal_iface
      [Network]
      DHCP=no
      Address=$pxe_internal_ip/$pxe_subnet_bitmask
      EOF

      # systemctl restart systemd-networkd

#. Configure NAT to route traffic from the private network to the public
   network, effectively turning the PXE server into a router. To keep these
   changes in spite of reboots, save the changes to the firewall with the
   following commands:

   .. code-block:: console

      # iptables -t nat -F POSTROUTING
      # iptables -t nat -A POSTROUTING -o $external_iface -j MASQUERADE
      # systemctl enable iptables-save.service
      # systemctl restart iptables-save.service
      # systemctl enable iptables-restore.service
      # systemctl restart iptables-restore.service

   .. note::

      The firewall masks or translates packets to make them appear as
      coming from the PXE server. Thus, it hides the PXE clients from the
      public network.

#. Configure the kernel to forward network packets to different
   interfaces. Otherwise, NAT will not work.

   .. code-block:: console

      # mkdir -p /etc/sysctl.d
      # echo net.ipv4.ip_forward=1 > /etc/sysctl.d/80-nat-forwarding.conf
      # echo 1 > /proc/sys/net/ipv4/ip_forward

#. The ``pxe-server`` bundle contains iPXE firmware images that allow computers
   without an iPXE implementation to perform an iPXE boot. Create a TFTP
   hosting directory and populate it with the iPXE firmware images with the
   following commands:

   .. code-block:: console

      # mkdir -p $tftp_root
      # ln -sf /usr/share/ipxe/undionly.kpxe $tftp_root/undionly.kpxe

#. The ``pxe-server`` bundle contains a lightweight TFTP, DNS, and DHCP
   server known as ``dnsmasq``.  Create a configuration file for ``dnsmasq``
   to listen on a dedicated IP address for those functions. PXE clients on
   the private network will use this IP address to access those functions.

   .. code-block:: console

      # cat > /etc/dnsmasq.conf << EOF
      listen-address=$pxe_internal_ip
      EOF

#. Add the options to serve iPXE firmware images to PXE clients over TFTP to
   the ``dnsmasq`` configuration file.

   .. code-block:: console

      # cat >> /etc/dnsmasq.conf << EOF
      enable-tftp
      tftp-root=$tftp_root
      EOF

#. Add the options to host a DHCP server for PXE clients to the ``dnsmasq``
   configuration file.

   .. code-block:: console

      # cat >> /etc/dnsmasq.conf << EOF
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

    .. note::
  This configuration provides the following important functions:

   * Directs PXE clients without an iPXE implementation to the TFTP server
     to acquire architecture-specific iPXE firmware images that allow them
     to perform an iPXE boot.
   * Activates only on the network adapter that has an IP address on the
     defined subnet.
   * Directs PXE clients to the DNS server.
   * Directs PXE clients to the PXE server for routing via NAT.
   * Divides the private network into two pools of IP addresses, one for
     network booting and another for usage after boot, each with their own
     lease times.

#. Create a file where ``dnsmasq`` can record the IP addresses it provides
   to PXE clients.

   .. code-block:: console

      # mkdir -p /var/db
      # touch /var/db/dnsmasq.leases

#. Start ``dnsmasq`` and enable startup on boot.

   .. code-block:: console

      # systemctl enable dnsmasq
      # systemctl restart dnsmasq

#. Start ``systemd-resolved``.

   .. code-block:: console

      # systemctl start systemd-resolved

   .. note::

      Using the ``dnsmasq`` DNS server allows ``systemd-resolved`` to dynamically
      update the list of DNS servers for the private network from the public
      network. This setup effectively creates a pass-through DNS server which
      relies on the DNS servers listed in :file:`/etc/resolv.conf`.

#. Power on the PXE client and watch it boot and install |CL|.

   .. note::

      After booting, |CL| will automatically partition the hard drive,
      install itself, update to the latest version, and reboot.


**Congratulations!** You have successfully installed and configured a PXE
server that enables PXE clients to boot and install |CL| over the network.


.. _iPXE:
   http://ipxe.org/

.. _ICIS GitHub repository:
   https://github.com/clearlinux/ister-cloud-init-svc
