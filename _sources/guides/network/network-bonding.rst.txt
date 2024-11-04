.. _network-bonding:

Combine multiple interfaces with network bonding
################################################

This guide describes how to configure systemd to use the :command:`bonding`
driver.

Network bonding combines multiple network interfaces into a single logical
interface to provide redundancy and bandwidth aggregation.

|CL-ATTR| includes the Linux `Bonding driver`_ and `Team driver`_ .

The example demonstrates how to:

*  Bond all four ports of a quad-port NIC in 802.3ad mode.

*  Enable jumbo frames to optimize large data transfers on the local network.

Your NICs and network switch must support 802.3ad mode and jumbo frames. The
example explains how to configure your NICs for both features. Your switch may
require additional configuration. See your switch documentation for details.

.. note::

   You must run all commands in this guide as root.

#. Log in and get root privileges.

   .. code-block:: console

      sudo -s

#. Create the :file:`/etc/systemd/network` directory.

   .. code-block:: bash

      mkdir -p /etc/systemd/network

   The :file:`/etc/systemd/network` directory contains configuration files and
   network settings for the virtual device and its underlying physical
   interfaces.

#. Configure systemd to create a virtual network device called `bond1`. Use a
   text editor to create a file named :file:`30-bond1.netdev`.

   .. code-block:: console

      [NetDev]
      Name=bond1
      Kind=bond

      [Bond]
      Mode=802.3ad
      TransmitHashPolicy=layer3+4
      MIIMonitorSec=1s
      LACPTransmitRate=fast

   Refer to the `systemd.netdev`_ manpage for :file:`30-bond1.netdev` file
   syntax. This example is based on Example 9 on the manpage. Modify the
   example for your configuration.

#. Configure the slave interfaces. Create a text file named
   :file:`30-bond1-enp1s0.network`. Assign the slave interfaces to the virtual
   `bond1` device and use the syntax shown in `systemd.network`_.

   .. code-block:: console

      [Match]
      Name=enp1s0f*

      [Network]
      Bond=bond1

      [Link]
      MTUBytes=9000

   The example bonds all four ports of a quad-port NIC as a slave of `bond1`.
   The example uses a wildcard match because the NIC names are in the range
   `enp1s0f0-enp1s0f3`. If your NIC names are not wildcard-compatible, create
   a separate :file:`.network` file for each NIC.

   For best results, do not assign addresses or DHCP support to the individual
   NICs.

   The `MTUBytes` setting enables jumbo frames of up to 9000 bytes. Your
   switch may require additional configuration to support this setting.

#. Configure the bonded interface in a file named :file:`30-bond1.network`.

   .. code-block:: console

      [Match]
      Name=bond1

      [Network]
      BindCarrier=enp1s0f0 enp1s0f1 enp1s0f2 enp1s0f3
      Address=192.168.1.201/24

      [Link]
      MTUBytes=9000

   `bond1` is a virtual interface with no physical link status.

   `BindCarrier` indicates that the `bond1` link status is determined by the
   status of the listed slave devices.

   `Address` contains an IP address that you assign to the logical interface.
   DHCP bonded interfaces are complex and outside the scope of this example.

   `MTUBytes` must be set to 9000 on all slave interfaces and on the bonded
   interface for successful jumbo frames operation. If `MTUBytes` is not the
   same on all interfaces, then the lowest value is used.

#. Apply the new network configuration with the command:

   .. code-block:: bash

      systemctl restart systemd-networkd

   The `MTUBytes` settings do not take effect until you reboot or manually
   apply the settings with a utility such as ifconfig.

.. _Bonding driver: https://www.kernel.org/doc/Documentation/networking/bonding.txt

.. _Team driver: https://www.kernel.org/doc/Documentation/networking/team.txt

.. _systemd.netdev: https://www.freedesktop.org/software/systemd/man/systemd.netdev.html

.. _systemd.network: https://www.freedesktop.org/software/systemd/man/systemd.network.html
