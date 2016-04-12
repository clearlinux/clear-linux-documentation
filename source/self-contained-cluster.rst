.. _self-contained-cluster:

Self-contained cloud integrated advanced orchestrator (ciao) cluster
####################################################################

The current iteration of self-contained ciao cluster networking
is based on the capabilities of Tunnel-Concentrator-Mode.

The followings section explains how to test the networking setup with 3 or more systems.

Typical ciao node
=================

A typical node used in the data center connects to two separate physical networks:

* **Management Network** carries command and control traffic such as the
  ciao CSR, Scheduler, SSNTP
* **Compute Network** carries all the traffic between workloads and instances; a
  Typical ciao Node

This is not strictly necessary, but the ciao Networking implementation supports
the notion that there may be separate Compute and Management networks. For example,
it's possible to connect NUCs running Clear Linux directly to a corporate
network for Management and to run your own private network with its own DHCP
server for the workload traffic.


Simple networking setup
=======================

This is an example of a 3+ NUC ciao Network test setup with the same network
for both Management and Compute, isolated from the corporate network. The
mandatory components are:

* the Gateway
* Control Node
* Network Node 1
* Compute Node 1

The setup supports any number of additional compute nodes and network
nodes, limited only by the size of the DHCP subnet configured on the
gateway.


Gateway setup
-------------

The dual-homed gateway node in this isolates the ciao Cluster from the
corporate network. It has the following functionality:

* DHCP Server for the ciao Nodes
* DNS Server for the ciao Nodes
* A NAT and basic firewall between the ciao Network and the corporate
  network

.. note::

The gateway node can be your dual-homed development system for easier deployment.


Network interface setup
-----------------------

The ``eth1`` interface is set up to have a static IP address of ``192.168.0.200``

Sample :file:`/etc/network/interfaces` file::

    /etc/network/interfaces
    # interfaces(5) file used by ifup(8) and ifdown(8)
    auto lo
    iface lo inet loopback

    # The primary network interface, connected to corporate network
    auto eth0
    iface eth0 inet dhcp

    #Static interface connected to the supernova network
    auto eth1
    iface eth1 inet static
    address 192.168.0.200
    netmask 255.255.255.0


DHCP setup
----------

The :file:`tenant_dns.cfg` can be set up to serve DHCP addresses for the ciao
Network (CN, NN, Control nodes and the CNCI). In the following sample, the DHCP
server always provides the same IP address to the same Node; however, this is
optional. Please replace the MAC addresses below with your own.

.. caution::

Please ensure the interfaces set here match yours. If you don't, and you
start responding to corporate DHCP, you will be booted off the network.

Sample :file:`tenant_dns.cfg` configuration file, presuming you're using
``dnsmasq`` as your DHCP+DNS server::

    strict-order
    bind-interfaces
    interface=eth1
    except-interface=lo
    except-interface=eth0
    pid-file=/var/run/tenant_dns.pid
    dhcp-leasefile=/var/lib/misc/tenant_dns.leases
    listen-address=192.168.0.200
    #Allows subslicing to 192.168.0.64/26
    dhcp-range=192.168.0.65,192.168.0.126,12h
    dhcp-host=*:*:*:*:*:*,id:*
    dhcp-no-override
    dhcp-lease-max=253
    dhcp-option-force=3,192.168.0.200
    dhcp-sequential-ip
    dhcp-host=B8:AE:ED:7B:51:50,192.168.0.101
    dhcp-host=C0:3F:D5:67:A7:6F,192.168.0.102
    dhcp-host=B8:AE:ED:7B:72:58,192.168.0.103
    dhcp-host=C0:3F:D5:67:A1:FB,192.168.0.104


The example above shows sub-slicing the DHCP network such that the CNCI gets
a DHCP range that can be independently routeable.


NAT setup
---------

To set your gateway node, the following commands can be used (assuming
``eth0`` is connected to the corporate network and ``eth1`` is connected
to the ciao Compute and Management private network):

Script to setup and reset your gateway and DHCP server::

    echo 0 > /proc/sys/net/ipv4/ip_forward
    iptables -F
    iptables -t nat -F
    iptables -t mangle -F
    iptables -X
    iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
    iptables -A FORWARD -i eth0 -o eth1 -m state --state RELATED,ESTABLISHED -j ACCEPT
    iptables -A FORWARD -i eth1 -o eth0 -j ACCEPT
    #iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 8889 -j DNAT --to 192.168.0.101:8889
    #iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 35357 -j DNAT --to 192.168.0.101:35357
    #iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 5000 -j DNAT --to 192.168.0.101:5000
    iptables -t nat -A PREROUTING -p tcp --dport 8889 -j DNAT --to 192.168.0.101:8889
    iptables -t nat -A PREROUTING -p tcp --dport 35357 -j DNAT --to 192.168.0.101:35357
    iptables -t nat -A PREROUTING -p tcp --dport 5000 -j DNAT --to 192.168.0.101:5000
    echo 1 > /proc/sys/net/ipv4/ip_forward
    killall dnsmasq
    rm -f /var/lib/misc/tenant_dns.leases
    dnsmasq -C tenant_dns.cfg

This setup assumes:

* Keystone VM runs on the same system that runs the CSR and Scheduler.
* The ciao nodes can reach the corporate network and Internet (being NATed by
  the gateway).
* Being able to reach the nodes by connectint to the gateway and then connecting
  to the nodes for port forwarding.  For this setup above, you can reach the WebUI
  and Keystone ports presented by the CSR and Keystone through the gateway IP
  address

Controller node setup
---------------------

One node in this sample setup, ``192.168.0.101``, is set as the
controller node. It runs the CSR, Scheduler and Keystone VM.

Network node setup
------------------

One node in this sample setup, ``192.168.0.102``, is set as the network
node. It runs the launcher that launches CNCIs.

Compute node setup
------------------

All other nodes in this sample setup ``192.168.0.103, 104, ..`` are compute
nodes. Compute nodes currently have a statically-assigned IPs. This allows
the CNCIs to come out of fixed range.


Connecting to instances
=======================

On the CNCI there will be a lease file :file:`/tmp/dnsmasq_*.leases`, which
will contain the MAC address and IP address of each instance that successfully
connected to the network.

You should be able to ping the IP address; and provided you have the ssh key provisioned in the instance, you will be able to ssh into the instance.

