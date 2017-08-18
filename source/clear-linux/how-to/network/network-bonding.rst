.. _network-bonding:

Combine multiple interfaces
###########################

Network bonding is a technique for combining multiple network interfaces into
a single, logical interface, providing some redundancy and bandwidth
aggregation.

|CLOSIA| includes the bonding_ and team_ drivers. The guide example provided
below shows how to configure systemd to use the ``bonding`` driver.

.. note::
   All commands in this guide must be run as root.

1. Create the ``/etc/systemd/network`` directory (if it doesn't already exist):

   .. code-block:: console

      # mkdir -p /etc/systemd/network

   This directory contains the configuration files and network settings
   for the virtual device and its underlying physical interfaces.

2. Configure systemd to create a virtual network device, ``bond1``. Use a text
   editor to create a file named ``30-bond1.netdev`` as shown here:

   .. code-block:: ini

      [NetDev]
      Name=bond1
      Kind=bond

      [Bond]
      Mode=802.3ad
      TransmitHashPolicy=layer3+4
      MIIMonitorSec=1s
      LACPTransmitRate=fast

   The syntax for this file is defined in the systemd.netdev_ manpage.
   `This example`__ may be used verbatim, or tuned to your particular
   requirements.  Note that ``802.3ad`` mode requires explicit support from
   your NICs and network switch. This and other modes may also require
   additional configuration of your network switch.

__ https://www.freedesktop.org/software/systemd/man/systemd.netdev.html#id-1.20.10

3. Configure the slave interfaces, assigning them to the new ``bond1`` device,
   using the syntax in systemd.network_, and in a text file named
   ``30-bond1-enp1s0.network`` as shown here:

   .. code-block:: ini

      [Match]
      Name=enp1s0f*

      [Network]
      Bond=bond1

      [Link]
      MTUBytes=9000

   This example demonstrates bonding all four ports of a quad-port NIC, with
   names in the range ``enp1s0f0-enp1s0f3``, allowing the use of a single file
   with a wildcard match. You may also create a separate file for each NIC,
   particularly if they have names that are not wildcard-friendly. This
   configuration assigns each NIC as a slave of ``bond1``. For best results,
   do not assign addresses or DHCP support to the individual NICs.

   This example also enables jumbo frames of up to 9000 bytes to optimize large
   data transfers on the local network. Again, your NICs and switch must
   support jumbo frames, and your switch may require additional configuration.

4. Define the network configuration for the bonded interface in a file named
   ``30-bond1.network`` as shown here:

   .. code-block:: ini

      [Match]
      Name=bond1

      [Network]
      BindCarrier=enp1s0f0 enp1s0f1 enp1s0f2 enp1s0f3
      Address=192.168.1.201/24

      [Link]
      MTUBytes=9000

   Since ``bond1`` is a virtual interface, it has no concept of physical link
   status. The ``BindCarrier`` directive indicates that the link status of this
   interface is determined by the status of the listed slave devices.

   This is the logical interface, so assign it an IP address. DHCP is more
   complicated with bonded interfaces, and is not covered in this example.

   This file also enables jumbo frames of up to 9000 bytes. This option must be
   enabled for all slave interfaces *and* the bonded interface, in order to take
   effect.

5. Apply the new network configuration:

   .. code-block:: console

      # systemctl restart systemd-networkd

   The MTU settings will not take effect until a reboot, or if you explicitly
   apply them via ``ifconfig``, for example.

.. _bonding:
   https://www.kernel.org/doc/Documentation/networking/bonding.txt

.. _team:
   https://www.kernel.org/doc/Documentation/networking/team.txt

.. _systemd.netdev:
   https://www.freedesktop.org/software/systemd/man/systemd.netdev.html

.. _systemd.network:
   https://www.freedesktop.org/software/systemd/man/systemd.network.html
