.. _assign-static-ip:

Assign a static IP address
##########################

By default, your |CL-ATTR| system automatically gets an IP address from your
network via DHCP. If you do not have a DHCP server on your network or simply
want to use a static IP address, follow the steps in this guide.

.. contents::
   :local:
   :depth: 1

Identify which program is managing the interface
************************************************

New installations of |CL| use NetworkManager as the default network interface
manager for all network connections.

.. note:: 

   * The *cloud* |CL| images continue to use systemd-networkd to manage
     network connections.

   * In earlier |CL| versions, systemd-network was used to manage Ethernet
     interfaces and NetworkManager was used for wireless interfaces.


Before defining a configuration for assigning a static IP address, you should
verify which program is managing the network interface.

#. Check the output of :command:`nmcli device` to see if NetworkManager is
   managing the device.

   .. code-block:: bash

      nmcli device status

   If the STATE column for the device shows *connected* or *disconnected*, the
   network configuration is being managed by NetworkManager and the instructions
   for :ref:`using NetworkManager <nm-static-ip>` should be used. 

   If the STATE column for the device shows *unmanaged*, check to see if the
   device is being managed by systemd-networkd  


#. Check the output of :command:`networkctl list` to see if
   systemd-networkd is managing the device.

   .. code-block:: bash

      networkctl list 

   If the SETUP column for the device shows *configured*, the network
   configuration is being managed by systemd-networkd and the instructions for
   :ref:`using systemd-networkd <networkd-static-ip>` should be used. 


.. _nm-static-ip:

Using NetworkManager
********************

Network connections managed by NetworkManager are stored as files with the
:file:`.nmconnection` file extension in the
:file:`/etc/NetworkManager/system-connections/` directory.

A few tools exists to aid to manipulate network connections managed by
NetworkManager:

* nmcli - a command-line tool 

* nmtui - a text user interface that provides a pseudo graphical menu in the
  terminal

* nm-connection-editor - a graphical user interface

The method below uses the command line tool *nmcli* to modify network
connection. 


#. Identify the existing connection name:

   .. code:: bash

      nmcli connection show

   The output will look like this:

   .. code:: bash

      NAME                UUID                                  TYPE            DEVICE 
      Wired connection 1  00000000-0000-0000-0000-000000000000  802-3-etherneten01

   If a connection does not exist, it will need to be created with
   :command:`nmcli connection add`.  


#. Modify the connection to use a static IP address. Replace the variables in
   brackets with the appropriate values. *[CONNECTION_NAME]* should be
   replaced with the NAME from the command above. 

   .. code::

      sudo nmcli connection modify "[CONNECTION_NAME]" \
      ipv4.method "manual" \
      ipv4.addresses "[IP_ADDRESS]/[CIDR_NETMASK]" \
      ipv4.gateway "[GATEWAY_IP_ADDRESS]" \
      ipv4.dns "[PRIMARY_DNS_IP],[SECONDARY_DNS_IP]"


   See the `nmcli developer page <https://developer.gnome.org/NetworkManager/stable/nmcli.html>`_ for more
   configuration options. For advanced configurations, the
   :file:`/etc/NetworkManager/system-connections/*.nmconnection`. can be edited
   directly.

#. Restart the NetworkManager server to reload the DNS servers:

   .. code-block:: bash

      sudo systemctl restart NetworkManager


#. Verify your static IP address details have been set:

   .. code-block:: bash

      nmcli



.. _networkd-static-ip:

Using systemd-networkd 
**********************

Network connections managed by systemd-networkd are stored as files with the
:file:`.network` file extension the :file:`/etc/systemd/network/` directory.

Files to manipulate network connections managed by systemd-networkd must be
created manually. 

#. Create the :file:`/etc/systemd/network` directory if it doesn't exist already:

   .. code-block:: bash

      sudo mkdir -p /etc/systemd/network

#. Create a :file:`.network` file and add the following content. Replace the
   variables in brackets with the appropriate values. *[INTERFACE_NAME]*
   should be replaced with LINK from the output of :command:`networkctl list`
   ran previously.

   .. code-block:: bash

      sudo $EDITOR /etc/systemd/network/70-static.network

      [Match]
      Name=[INTERFACE_NAME]

      [Network]
      Address=[IP_ADDRESS]/[CIDR_NETMASK]
      Gateway=[GATEWAY_IP_ADDRESS]
      DNS=[PRIMARY_DNS_IP]
      DNS=[SECONDARY_DNS_IP]

   See the `systemd-network man page
   <https://www.freedesktop.org/software/systemd/man/systemd.network.html>`_
   for more configuration options.

#. Restart the systemd-networkd service:

   .. code-block:: bash

      sudo systemctl restart systemd-networkd

#. Verify your static IP address details have been set:

   .. code-block:: bash

      networkctl status

