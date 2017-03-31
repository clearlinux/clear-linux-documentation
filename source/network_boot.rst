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
network booting computers which lack built-in PXE support.

Figure 1 depicts the flow of information between a PXE server and a PXE client
that needs to be created for network booting |CL|.

.. figure:: _static/images/network-boot-flow.png
   :alt: PXE information flow

   Figure 1: PXE information flow

This guide covers how to network boot |CL| with iPXE using
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
* Your PXE clients have a boot order where the network boot option is
  prioritized before the disk boot option.

.. note::

   The secure boot option must be disabled because the UEFI binaries used to
   boot |CL| are not signed.

The required computer and network setup is depicted in figure 2.

.. figure:: _static/images/network-boot-setup.png
   :alt: NAT network topology

   Figure 2: NAT network topology

Configuration
=============

The configuration process to boot using iPXE has been automated with the
:file:`configure-ipxe.sh` script included with :abbr:`ICIS (Ister Cloud Init Service)`, thus
quickly enabling a bulk provisioning setup.  For additional instructions on
how to get started with the script, refer to the guide on the `ICIS GitHub
repository`_.

#. Define the variables used to parameterize the configuration of an iPXE
   boot.

   .. code-block:: console

      uwsgi_app_dir=/usr/share/uwsgi
      uwsgi_socket_dir=/run/uwsgi
      icis_app_name=icis
      ipxe_app_name=ipxe

      ipxe_port=50000
      icis_port=60000

      web_root=/var/www
      ipxe_root=$web_root/$ipxe_app_name
      icis_root=$web_root/$icis_app_name
      tftp_root=/srv/tftp

      external_iface=eno1
      internal_iface=eno2
      pxe_subnet=192.168.1
      pxe_internal_ip=$pxe_subnet.1
      pxe_subnet_mask_ip=255.255.255.0

#. Add the ``pxe-server`` bundle to your system.  This bundle has all of the
   files needed run a PXE server.

   .. code-block:: console

      swupd bundle-add pxe-server

#. Download the latest network-bootable release of |CL|, and extract the
   files.

   .. code-block:: console

      rm -rf $ipxe_root
      mkdir -p $ipxe_root
      curl -o /tmp/clear-pxe.tar.xz
      https://download.clearlinux.org/current/clear-$(curl
      https://download.clearlinux.org/latest)-pxe.tar.xz
      tar -xJf /tmp/clear-pxe.tar.xz -C $ipxe_root
      ln -sf $(ls $ipxe_root | grep 'org.clearlinux.*') $ipxe_root/linux

   .. important::

      Ensure that the initial ramdisk file is named :file:`initrd` and
      the kernel file is named :file:`linux`, which is a symbolic link to the
      actual kernel file.

#. Create an iPXE boot script. During an iPXE boot, the iPXE boot script directs
   the PXE client to the files needed to network boot |CL|. Use the names given
   to the initial ramdisk and kernel files.

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
   ``nginx``. Create a configuration file for ``nginx`` to serve |CL| to PXE
   clients.

   .. code-block:: console

      mkdir -p /etc/nginx
      cat > /etc/nginx/$ipxe_app_name.conf << EOF
      server {
        listen $ipxe_port;
        server_name localhost;
        location /$ipxe_app_name/ {
          root $web_root;
          autoindex on;
        }
      }
      EOF

   .. note::

      Creating a separate configuration file for ``nginx`` to serve network-
      bootable images on a non-standard port number preserves existing nginx
      configurations.

#. Start ``nginx`` and enable startup on boot.

   .. code-block:: console

      systemctl start nginx
      systemctl enable nginx

#. The ``pxe-server`` bundle contains a lightweight DNS server that conflicts
   with the DNS stub listener provided by ``systemd-resolved``.  Disable the DNS
   stub listener and temporarily stop ``systemd-resolved``.

   .. code-block:: console

      mkdir -p /etc/systemd
      cat > /etc/systemd/resolved.conf << EOF
      [Resolve]
      DNSStubListener=no
      EOF

      systemctl stop systemd-resolved

#. Assign a static IP address to the network adapter for the private network and
   restart ``systemd-networkd``.

   .. code-block:: console

      mkdir -p /etc/systemd/network
      cat > /etc/systemd/network/70-internal-static.network << EOF
      [Match]
      Name=$internal_iface
      [Network]
      DHCP=no
      Address=$pxe_internal_ip/$pxe_subnet_bitmask
      EOF

      systemctl restart systemd-networkd

#. Configure NAT to route traffic from the private network to the public
   network, effectively turning the PXE server into a router.  Persist these
   changes across reboots by saving the changes to the firewall.

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

#. Tell the kernel to forward network packets on to different
   interfaces. Otherwise, NAT will not work.

   .. code-block:: console

      mkdir -p /etc/sysctl.d
      echo net.ipv4.ip_forward=1 > /etc/sysctl.d/80-nat-forwarding.conf
      echo 1 > /proc/sys/net/ipv4/ip_forward

#. The ``pxe-server`` bundle contains iPXE firmware images which allow
   computers without an iPXE implementation to perform an iPXE boot. Create a
   TFTP hosting directory and populate it with the iPXE firmware images.

   .. code-block:: console

      rm -rf $tftp_root
      mkdir -p $tftp_root
      ln -sf /usr/share/ipxe/undionly.kpxe $tftp_root/undionly.kpxe

#. The ``pxe-server`` bundle contains a lightweight TFTP, DNS, and DHCP server
   known as ``dnsmasq``.  Create a configuration file for ``dnsmasq`` to listen
   on a dedicated IP address for these functions.  PXE clients on the private
   network will use this IP address to access these functions.

   .. code-block:: console

      cat > /etc/dnsmasq.conf << EOF
      listen-address=$pxe_internal_ip
      EOF

#. Add to the configuration file for ``dnsmasq`` options to serve iPXE firmware
   images to PXE clients over TFTP.

   .. code-block:: console

      cat >> /etc/dnsmasq.conf << EOF
      enable-tftp
      tftp-root=$tftp_root
      EOF

#. Add to the configuration file for ``dnsmasq`` options to host a DHCP server
   for PXE clients.

   .. code-block:: console

      cat >> /etc/dnsmasq.conf << EOF
      dhcp-leasefile=/var/db/dnsmasq.leases

      dhcp-authoritative
      dhcp-option=option:router,$pxe_internal_ip
      dhcp-option=option:dns-server,$pxe_internal_ip

      dhcp-match=set:pxeclient,60,PXEClient*
      dhcp-range=tag:pxeclient,$pxe_subnet.2,$pxe_subnet.253,$pxe_subnet_mask_ip,15m
      dhcp-range=tag:!pxeclient,$pxe_subnet.2,$pxe_subnet.253,$pxe_subnet_mask_ip,6h

      dhcp-match=set:ipxeboot,175
      dhcp-boot=tag:ipxeboot,http://$pxe_internal_ip:$ipxe_port/$ipxe_app_name/ipxe_boot_script.txt
      dhcp-boot=tag:!ipxeboot,undionly.kpxe,$pxe_internal_ip
      EOF

   This configuration provides the following important functions:

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

#. Create a file where ``dnsmasq`` can record the IP addresses it hands
   out to PXE clients.

   .. code-block:: console

      mkdir -p /var/db
      touch /var/db/dnsmasq.leases

#. Start ``dnsmasq`` and enable startup on boot.

   .. code-block:: console

      systemctl enable dnsmasq
      systemctl restart dnsmasq

#. Start ``systemd-resolved``.

   .. code-block:: console

      systemctl start systemd-resolved

   .. important::

      Using the ``dnsmasq`` DNS server allows ``systemd-resolved`` to
      dynamically update the list of DNS servers for the private network from
      the public network. This setup effectively creates a pass-through DNS
      server which relies on the DNS servers listed in ``/etc/resolv.conf``.

#. Power on the PXE client and watch it boot |CL|.

Congratulations!  You have successfully installed and configured a PXE server
that can network boot PXE clients with |CL|.


.. _iPXE:
   http://ipxe.org/

.. _ICIS GitHub repository:
   https://github.com/clearlinux/ister-cloud-init-svc
