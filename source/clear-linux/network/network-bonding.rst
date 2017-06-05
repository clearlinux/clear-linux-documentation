.. _network-bonding:

Network Bonding
###############

Network bonding is a technique for combining multiple network interfaces into
a single, logical interface, providing some combination of redundancy and
bandwidth aggregation.

|CLOSIA| includes the bonding_ and team_ drivers. Here, we'll provide an
example of configuring systemd to use the ``bonding`` driver.

All commands in this guide should be run as root.

First, if it does not already exist, create the following directory:

.. code-block:: console

   # mkdir -p /etc/systemd/network

In this directory, you will create the configuration files for the virtual
device and the network settings for it and the underlying physical interfaces.

Next, configure systemd to create a virtual network device, ``bond1``. The
syntax for this file is defined in the systemd.netdev_ manpage.
`This example`__ may be used verbatim, or tuned to your particular requirements.
Note that ``802.3ad`` mode requires explicit support from your NICs and network
switch. This and other modes may also require additional configuration of your
network switch.

__ https://www.freedesktop.org/software/systemd/man/systemd.netdev.html#id-1.20.10

.. code-block:: ini
   :caption: 30-bond1.netdev
   :linenos:

   [NetDev]
   Name=bond1
   Kind=bond

   [Bond]
   Mode=802.3ad
   TransmitHashPolicy=layer3+4
   MIIMonitorSec=1s
   LACPTransmitRate=fast

Configure the slave interfaces, assigning them to the new ``bond1``, using the
syntax in systemd.network_.

.. code-block:: ini
   :caption: 30-bond1-enp1s0.network
   :linenos:

   [Match]
   Name=enp1s0f*

   [Network]
   Bond=bond1

   [Link]
   MTUBytes=9000

.. note::

   This guide demonstrates bonding all four ports of a quad-port NIC, with
   names in the range ``enp1s0f0-enp1s0f3``, allowing the use of a single file
   with a wildcard match. You may also create a separate file for each NIC,
   particularly if they have names that are not wildcard-friendly. This
   configuration assigns each NIC as a slave of ``bond1``. For best results,
   do not assign addresses or DHCP support to the individual NICs.

.. note::


   This example also enables jumbo frames of up to 9000 bytes to optimize large
   data transfers on the local network. Again, your NICs and switch must
   support jumbo frames, and your switch may require additional configuration.

   Finally, define the network configuration for the bonded interface.

.. code-block:: ini
   :caption: 30-bond1.network
   :linenos:

   [Match]
   Name=bond1

   [Network]
   BindCarrier=enp1s0f0 enp1s0f1 enp1s0f2 enp1s0f3
   Address=192.168.1.201/24

   [Link]
   MTUBytes=9000

.. note::

   Since ``bond1`` is a virtual interface, it has no concept of physical link
   status. The ``BindCarrier`` directive indicates that the link status of this
   interface is determined by the status of the listed slave devices.

.. note::

   This is the logical interface, so assign it an IP address. DHCP is more
   complicated with bonded interfaces, and is not covered in this guide.

.. note::

   This file also enables jumbo frames of up to 9000 bytes. This option must be
   enabled for all slave interfaces *and* the bonded interface in order to take
   effect.

Apply the new network configuration:

.. code-block:: console

   # systemctl restart systemd-networkd

.. note::

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
