.. _firewall:

Firewall
#########

Firewalls control access to and from systems based on network packet
attributes like IP address, port, payload and more. 

The `Netfilter <https://netfilter.org/>`_ framework in the Linux kernel
performs packet filtering and provides the means for implementing a software
firewall in Linux. |CL-ATTR| has a couple different firewall front-end options
for managing the Linux firewall.


.. contents:: :local:
    :depth: 2
   

Default ruleset
***************

|CL| does not impose a firewall policy out of the box. All traffic is allowed
inbound and all traffic is allowed outbound. However, `tallow`_ is installed
by default and may dynamically create a rule temporarily restricting access
from external hosts.

.. warning::

   Changing firewall configuration can cause abrupt network disconnection. If
   this happens on a remote host, local recovery may be required.
   
   Be sure to test your firewall configuration before committing it
   permanently to ensure your system will remain accessible remotely, if
   required.

Firewall software
*****************

iptables 
========

:command:`iptables` is a well-known user-space administration tool for
configuring IPv4 Linux firewall rules. :command:`ip6tables` is the
complimentary tool for configuring IPv6 Linux firewall rules. 

Below is information on using :command:`iptables` on |CL|: 

#. Make sure the *iptables* bundle is installed

   .. code:: bash

      sudo swupd bundle-add iptables


#. Define new iptables rules/chains for the running configuration using the
   :command:`iptables` command. See :command:`man iptables` for iptables
   concepts and configuration options.

   Below is a common restrictive firewall configuration which denies all
   incoming connections, unless the connection was initiated by the host. 

   .. code:: bash

      # Set default chain policies 
      sudo iptables -P INPUT DROP
      sudo iptables -P FORWARD DROP
      sudo iptables -P OUTPUT ACCEPT

      # Accept on localhost loopback device
      sudo iptables -A INPUT -i lo -j ACCEPT
      sudo iptables -A OUTPUT -o lo -j ACCEPT

      # Allow established sessions to receive traffic
      sudo iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT


#. Test the running firewall configuration to make sure it behaving as
   you expect. 

#. Run the *iptables-save* service to make the running configuration
   persistent. This will perform a one-time save of the running configuration
   to :file:`/etc/iptables.rules` :

   .. code:: bash

      sudo systemctl start iptables-save

#. Enable the *iptables-resolve* service the iptables rules to be
   automatically applied at boot from the :file:`/etc/iptables.rules` file:

   .. code :: bash

      sudo systemctl enable iptables-restore.service


ipset
=====

`ipset <http://ipset.netfilter.org/>`_ is a framework in the Linux kernel for
storing and efficiently indexing combinations of IP addresses, networks,
(TCP/UDP) port numbers, MAC addresses, and interface names. 

IP sets makes writing network policy rules simpler and processing them against
a large and/or changing sets of hosts more efficient. 

By themselves, IP sets do not enforce network traffic rules but can be used to
extend iptables rules for matching. It is important to note that the ipset
must be defined before a netfilter rule can match against it.

* Running IP sets can be manipulated with the :command:`ipset` utility. 

* Custom IP sets can be stored in the :file:`/etc/ipset.conf` file

* IP sets in :file:`/etc/ipset.conf` can be automatically applied at boot by
  enabling the *ipset* service with the command :command:`sudo systemctl
  enable ipset`.

See :command:`man ipset` to learn more about using ipsets. 


firewalld
=========

`firewalld <https://firewalld.org/>`_ is based on nftables, the successor to
iptables and parts of the netfilter framework. The description of firewalld
helps highlight some of the differences compared to iptables:

    firewalld provides a dynamically managed firewall with support for
    network/firewall zones to define the trust level of network connections or
    interfaces. It has support for IPv4, IPv6 firewall settings and for
    ethernet bridges and has a separation of runtime and permanent
    configuration options. It also supports an interface for services or
    applications to add firewall rules directly.

See :command:`man firewalld` for more information. 

Below is information on using :command:`firewalld` on |CL|: 

#. Install he *firewalld* bundle:

   .. code:: bash

      sudo swupd bundle-add firewalld


#. Disable *iptables* and *ipset* services as they conflict with firewalld:

   .. code:: 

      sudo systemctl mask iptables-restore ipset


#. :command:`firewall-cmd` can be used to configure the running or permanent
   firewall configuration. See the `firewalld documentation
   <https://firewalld.org/documentation/>`_ to learn more about
   firewalld concepts and configuration options.

   Below is a common example to allow HTTPS traffic in public zones:

   .. code::

      sudo firewall-cmd --permanent --zone=public --add-service=https


#. Enable the *firewalld* service the so that the firewalld daemon is
   automatically started and rules applied at boot from the
   :file:`/etc/firewalld/*` file:

   .. code :: bash

      sudo systemctl enable --now firewalld.service


#. Verify that firewalld is running:

   .. code :: bash

      sudo firewall-cmd --state



Troubleshooting
***************

When troubleshooting connectivity issues that may be related to firewall
rules.

* Consider restrictions at the physical network level.

* For inbound connections, make sure your application is listening on the
  network port you're expecting with :command:`lsof` or :command:`netstat`.

* For outbound connections, make sure the destination host is responding to
  the network port you're expecting with :command:`nc`. If the connection is
  refused, then there may be a problem with the destination server.

* If you're using firewalld, check the daemon status with the command:
  :command:`systemctl status firewalld`.


.. _`tallow`: https://github.com/clearlinux/tallow
