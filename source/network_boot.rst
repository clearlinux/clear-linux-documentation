.. _network_boot:

Network Booting
###############

|CLOSIA| can boot from a :abbr:`PXE (pre-boot execution environment)`. PXE
is an industry standard which describes the client-server interaction to
network boot software using the DHCP and TFTP protocols. One possible use of
this environment is to automatically install an operating system.

The PXE extension known as `iPXE`_\* adds support for additional protocols
such as HTTP, iSCIS, :abbr:`AoE (ATA over Ethernet)`, and
:abbr:`FCoE (Fiber Channel over Ethernet)`. iPXE can also be used to enable
network-booting computers which lack built-in PXE support.

This guide covers how to boot |CL| with iPXE using
:abbr:`NAT (network address translation)`.

Prerequisites
=============

Before booting with iPXE, ensure the following preparations have been
made:

* Your PXE server has an ethernet/LAN boot option.
* Your PXE server has at least two network adapters.
* Your PXE server is connected to a public network.
* Your PXE server and PXE clients are connected to a switch on a private
  network.
* Your PXE server has the secure boot option disabled.

.. note::

   The secure boot option must be disabled because the UEFI binaries used to
   boot the |CLOSIA| are not signed.

The required computer and network setup are depicted in figure 1.

.. figure:: _static/images/network-boot-setup.png
   :alt: NAT network topology

   Figure 1: NAT network topology

Configuration
=============

The configuration to boot using iPXE has been automated with the
:file:`configure-ipxe.sh` script which ran during the installation of the
`Ister Cloud Init Service`_, thus quickly enabling a bulk provisioning
setup. Before running the configuration script, modify
:file:`parameters.conf` with your specific configurations.

Figure 2 depicts the information flow enabled by the configuration script.

.. figure:: _static/images/network-boot-flow.png
   :alt: PXE information flow

   Figure 2: PXE information flow

#. Define the variables used to parameterize the configuration of an iPXE
   boot.

   .. code-block:: console

      web_root=/var/www
      ipxe_root=$web_root/ipxe
      tftp_root=/srv/tftp

      external_iface=eno1
      internal_iface=eno2
      pxe_subnet=192.168.1
      pxe_internal_ip=$pxe_subnet.1
      pxe_subnet_mask_ip=255.255.255.0
      pxe_subnet_bitmask=24

#. Add the ``pxe-server`` bundle to your system.  This bundle has all the
   packages needed run a PXE server.

   .. code-block:: console

      swupd bundle-add pxe-server

#. Create an iPXE hosting directory.

   .. code-block:: console

    rm -rf $ipxe_root
    mkdir -p $ipxe_root

#. Download the latest network-bootable release of |CL|, and extract the
   files.

   .. code-block:: console

      curl -o /tmp/clear-pxe.tar.xz
      https://download.clearlinux.org/current/clear-$(curl
      https://download.clearlinux.org/latest)-pxe.tar.xz
      tar -xJf /tmp/clear-pxe.tar.xz -C $ipxe_root
      ln -sf $(ls $ipxe_root | grep 'org.clearlinux.*') $ipxe_root/linux

   .. important::

      Ensure that the initial ramdisk file is named :file:`initrd` and
      the kernel file is named :file:`linux`, which is a symbolic link to the
      actual kernel file.

#. Create an iPXE boot script. During an iPXE boot, the iPXE boot script
   directs the PXE client to the files needed to network-boot the latest
   release. Use the  names given to the initial ramdisk and kernel
   files.

   .. code-block:: console

      cat > $ipxe_root/ipxe_boot_script.txt << EOF
      #!ipxe
      kernel linux quiet init=/usr/lib/systemd/systemd-bootchart
      initcall_debug tsc=reliable no_timer_check noreplace-smp rw
      initrd=initrd
      initrd initrd
      boot
      EOF

#. The ``pxe-server`` bundle contains a lightweight web-server known as
   ``nginx``. Create a configuration file for ``nginx`` to serve the latest
   release to PXE clients.

   .. code-block:: console

      mkdir -p /etc/nginx
      cat > /etc/nginx/nginx.conf << EOF
      server {
        listen 80;
        server_name localhost;
        location / {
          root $ipxe_root;
          autoindex on;
        }
      }
      EOF

#. Start ``nginx`` and enable startup on boot.

   .. code-block:: console

      systemctl start nginx
      systemctl enable nginx

#. The ``pxe-server`` bundle contains iPXE firmware images which allow
   computers without an iPXE implementation to perform an iPXE boot. Create a
   TFTP hosting directory and populate it with the iPXE firmware images.

   .. code-block:: console

      rm -rf $tftp_root
      mkdir -p $tftp_root
      ln -sf /usr/share/ipxe/ipxe-x86_64.efi $tftp_root/ipxe-x86_64.efi
      ln -sf /usr/share/ipxe/undionly.kpxe $tftp_root/undionly.kpxe

#. The ``pxe-server`` bundle contains a lightweight TFTP server known as
   ``dnsmasq``. Create a configuration file for ``dnsmasq`` to serve iPXE
   firmware images to PXE clients over TFTP.

   .. code-block:: console

      cat > /etc/dnsmasq.conf << EOF
      enable-tftp
      tftp-root=$tftp_root
      EOF

#. Enable ``dnsmasq`` to start automatically on boot.

   .. code-block:: console

      systemctl enable dnsmasq

   .. note::

      At this point in the configuration process, ``dnsmasq`` is only being
      enabled to start automatically on boot but it is not started because
      its DNS server conflicts with the DNS stub listener of
      ``systemd-resolved``.

#. Set ``dnsmasq`` to listen on a dedicated IP address. PXE clients on the
   private network will use this IP address for DNS resolution. Disable
   the DNS stub listener included with ``systemd-resolved`` to avoid a
   conflict with the ``dnsmasq`` DNS server.

   .. code-block:: console

      mkdir -p /etc/systemd
      cat > /etc/systemd/resolved.conf << EOF
      [Resolve]
      DNSStubListener=no
      EOF

      cat >> /etc/dnsmasq.conf << EOF
      listen-address=$pxe_internal_ip
      EOF

   .. note::

      ``dnsmasq`` is a lightweight implementation of a DNS server, a DHCP
      server, and a TFTP server.  For the purposes of this guide, the DHCP
      server included with ``dnsmasq`` is not being used.

   .. important::

      Using the ``dnsmasq`` DNS server allows ``systemd-resolved`` to
      dynamically update the list of DNS servers for the private network from
      the public network. This setup effectively creates a pass-through DNS
      server which relies on the DNS servers listed in ``/etc/resolv.conf``.

#. Start ``dnsmasq`` and avoid conflicts with ``systemd-resolved``.

   .. code-block:: console

      systemctl stop systemd-resolved
      systemctl restart dnsmasq
      systemctl start systemd-resolved

#. Assign a static IP address to the network adapter for the private network.

   .. code-block:: console

      mkdir -p /etc/systemd/network

      ln -sf /dev/null /etc/systemd/network/80-dhcp.network

      cat > /etc/systemd/network/80-external-dynamic.network << EOF
      [Match]
      Name=$external_iface
      [Network]
      DHCP=yes
      EOF

      cat > /etc/systemd/network/80-internal-static.network << EOF
      [Match]
      Name=$internal_iface
      [Network]
      DHCP=no
      Address=$pxe_internal_ip/$pxe_subnet_bitmask
      EOF

    systemctl restart systemd-networkd

   .. note::

      By default, ``systemd-networkd`` uses DHCP for all network adapters.
      This functionality must be disabled prior to assigning a static IP
      address. Consequently, DHCP functionality for the network adapter
      connected to the public network is also disabled. Thus, this functionality must be explicitly re-enabled for the network adapter.

#. The ``pxe-server`` bundle contains a full DHCP server implementation
   compliant with the specifications defined by the
   :abbr:`ISC (Internet Systems Consortium)` known as ``dhcpd``. Configure
   ``dhcpd`` to dynamically allocate IP addresses to PXE clients on the
   private network.

   .. code-block:: console

      cat > /etc/dhcpd.conf << EOF
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

      class "PXE-Chainload" {
      match if substring(option vendor-class-identifier, 0, 9) = "PXEClient";

      next-server $pxe_internal_ip;
      if exists user-class and option user-class = "iPXE" {
        filename "http://$pxe_internal_ip/ipxe_boot_script.txt";
      }
      elsif substring(option vendor-class-identifier, 0, 20) = "PXEClient:Arch:00007" or substring(option vendor-class-identifier, 0, 20) = "PXEClient:Arch:00008" or substring(option vendor-class-identifier, 0, 20) = "PXEClient:Arch:00009" {
        filename "ipxe-x86_64.efi";
      }
      elsif substring(option vendor-class-identifier, 0, 20) = "PXEClient:Arch:00000" {
        filename "undionly.kpxe";
      }
      }

      subnet $pxe_subnet.0 netmask $pxe_subnet_mask_ip {
      authoritative;
      option routers $pxe_internal_ip;
      option domain-name-servers $pxe_internal_ip;

      pool {
        allow members of "PXE-Chainload";
        range $pxe_subnet.128 $pxe_subnet.253;
        default-lease-time 600;
        max-lease-time 3600;
      }

      pool {
        deny members of "PXE-Chainload";
        range $pxe_subnet.2 $pxe_subnet.127;
        default-lease-time 3600;
        max-lease-time 21600;
      }
      }
      EOF

   This configuration provides the following important functions:

   * Enables ``dhcpd`` to be iPXE-aware with `iPXE-specific options`_.
   * Directs PXE clients without an iPXE implementation to the TFTP server
     for acquiring architecture-specific iPXE firmware images to allow them
     to perform an iPXE boot.
   * Is only active on the network adapter which has an IP address on the
     defined subnet.
   * Directs PXE clients to the DNS server.
   * Directs PXE clients to the PXE server for routing via NAT.
   * Divides the private network into two pools of IP addresses, one for
     network booting and another for usage after boot; each with their own
     lease times.

   .. important::

      There are three providers of a DHCP server on the system at this point:
      ``systemd-networkd``, ``dnsmasq``, and ``dhcpd``. ``dhcpd`` is used
      because it is maintained by ISC and is more flexible for iPXE booting.

#. Create a file where ``dhcpd`` can record the IP addresses it hands
   out to PXE clients.

   .. code-block:: console

      mkdir -p /var/db
      touch /var/db/dhcpd.leases

#. Start ``dhcpd`` and enable startup on boot.

   .. code-block:: console

      systemctl enable dhcp4
      systemctl restart dhcp4

#. Configure NAT to route traffic from the private network to the public
   network, effectively turning the PXE server into a router.

   .. code-block:: console

      iptables -t nat -F POSTROUTING
      iptables -t nat -A POSTROUTING -o $external_iface -j MASQUERADE
      systemctl enable iptables-save.service
      systemctl restart iptables-save.service
      systemctl enable iptables-restore.service
      systemctl restart iptables-restore.service

   .. note::

      The firewall masquerades or translates packets to make them appear as
      coming from the PXE server. Thus, it hides the PXE clients from the
      public network.

#. Tell the Linux kernel to forward network packets on to different
   interfaces. Otherwise, NAT will not work.

   .. code-block:: console

      mkdir -p /etc/sysctl.d
      echo net.ipv4.ip_forward=1 > /etc/sysctl.d/80-nat-forwarding.conf
      echo 1 > /proc/sys/net/ipv4/ip_forward

#. Power on the PXE client and watch it boot the latest release of the
   |CLOSIA|

Congratulations you have successfully installed and configured PXE network-booting for |CL|.


.. _iPXE:
   http://ipxe.org/

.. _Ister Cloud Init Service:
   https://github.com/clearlinux/ister-cloud-init-svc

.. _iPXE-specific options:
   http://www.ipxe.org/howto/dhcpd#ipxe-specific_options
