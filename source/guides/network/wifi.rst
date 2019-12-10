.. _wi-fi:

Configure Wi-Fi
###############

We recommend using `NetworkManager <https://developer.gnome.org/NetworkManager/stable/NetworkManager.html>`_ to manage network connections. If you
choose to connect to Wi-Fi while using the
:ref:`live installer <bare-metal-install-desktop>` image, your Wi-Fi settings
will be added to your system during the installation process.

NetworkManager provides three simple methods for configuring Wi-Fi: Desktop,
CLI, and TUI. NetworkManager uses :command:`wpa_supplicant`, which can also be
used on its own for a more lightweight installation.

.. contents::
   :local:
   :depth: 1

Using Network Manager
*********************

Desktop GUI (Graphical User Interface)
======================================

1. Click anywhere on the icons at the right side of the top of the screen to
   bring up a menu and click on :guilabel:`Wi-Fi Not Connected` then
   choose :guilabel:`Select Network`.

   .. figure:: /_figures/wifi/wifi-1.1.png

2. Scroll through the list and select the network you'd like to connect to and
   click :guilabel:`Connect`.

   .. figure:: /_figures/wifi/wifi-2.png

3. Enter the password and click :guilabel:`Connect`.

   .. figure:: /_figures/wifi/wifi-3.png

4. The Wi-Fi icon should now show the signal strength of the connection.

   .. figure:: /_figures/wifi/wifi-4.png

5. If you are installing using the live image, resume the
   :ref:`installation process <install-on-target-end>` now. Your Wi-Fi
   configuration will automatically be included in the install. 

   .. figure:: /_figures/wifi/wifi-5.png

CLI (Command Line Interface)
============================

#. List the available Wi-Fi networks

   .. code-block:: bash

      nmcli device wifi list

   .. code-block:: console

      IN-USE  SSID                           MODE   CHAN  RATE        SIGNAL  BARS  SECURITY         
              1st Network                    Infra  1     54 Mbit/s   65      ▂▄▆_  --               
              2nd Network                    Infra  1     130 Mbit/s  52      ▂▄__  --               
              3rd Network                    Infra  10    195 Mbit/s  29      ▂___  WPA2             

#. Join the network.

   .. code-block:: bash

      nmcli device wifi connect $SSID password $password

   .. code-block:: console

      Device 'wlp1s0' successfully activated with 'f2501e67-27a3-4cf2-a8d9-cce3d029b788'.

.. note::

   To avoid having the Wi-Fi password stored in bash history, consider using the TUI.

TUI (Text-based User Interface)
===============================

#. Launch the NetworkManager Text User Interface

   .. code-block:: bash

      nmtui

#. Select :guilabel:`Activate a connection` and hit :kbd:`return`.

   .. figure:: /_figures/wifi/nmtui_1.png

#. Use the arrow keys to select your network and then select
   :guilabel:`Activate` and hit :kbd:`return`. 

   .. figure:: /_figures/wifi/nmtui_2.png

#. Enter your password and hit :kbd:`return` to select :guilabel:`OK`.

   .. figure:: /_figures/wifi/nmtui_3.png

#. Select :guilabel:`Back` and hit :kbd:`return`.

   .. figure:: /_figures/wifi/nmtui_4.png

#. Select :guilabel:`Quit` and hit :kbd:`return` to exit. 

   .. figure:: /_figures/wifi/nmtui_5.png

Using wpa_supplicant
********************

Make sure NetworkManager is either stopped, disabled by maksing the service,
or not installed before using wpa_supplicant.

.. code-block:: bash

   sudo systemctl stop NetworkManager.service
   sudo systemctl mask NetworkManager.service

#. Create a ``wpa_supplicant`` configuration directory.

   .. code-block:: bash

      sudo mkdir /etc/wpa_supplicant

#. Determine your wireless interface name.

   .. code-block:: bash

      iw dev

   Use the name following "Interface" on the first line (eg. wlp1s0)

   .. code-block:: console

       Interface wlp1s0
          ifindex 3
          wdev 0x1
          addr 00:xx:xx:38:34:7a
          type managed
          txpower 0.00 dBm

   Set the $INTERFACE_NAME environment variable to take advantage of copying
   and pasting commands.

   .. code-block:: bash

      export INTERFACE_NAME=wlp1s0

#. Create a minimal configuration file called
   :file:`/etc/wpa_supplicant/wpa_supplicant-$INTERFACE_NAME.conf`
   and add the following:

   .. code-block:: bash

      ctrl_interface_group=wheel
      ctrl_interface=/run/wpa_supplicant
      update_config=1

#. Complete the configuration process.

   .. code-block:: bash

      sudo wpa_supplicant -B -i $INTERFACE_NAME -c /etc/wpa_supplicant/wpa_supplicant-$INTERFACE_NAME.conf

#. Use :command:`wpa_cli` (interactive mode) to scan for available networks.

   .. code-block:: bash

      sudo wpa_cli
      > scan
      OK
      <3>CTRL-EVENT-SCAN-STARTED
      <3>CTRL-EVENT-SCAN-RESULTS
      > scan_results
      bssid / frequency / signal level / flags / ssid
      00:xx:xx:73:7b:46 5180 -55 [WPA2-PSK-CCMP][ESS] Network1
      00:xx:xx:5d:d9:23 2412 -47 [RSN--CCMP][MESH] 1137e9
      00:xx:xx:73:7b:43 2412 -49 [RSN--CCMP][MESH] 1137e9
      00:xx:xx:5d:d9:25 2412 -47 [WPA2-PSK-CCMP][ESS] Network1
      00:xx:xx:37:25:05 2412 -49 [WPA2-PSK-CCMP][ESS] Network1
      00:xx:xx:73:7b:45 2412 -59 [WPA2-PSK-CCMP][ESS] Network1
      00:xx:xx:83:fa:6a 2437 -57 [WPA-EAP-CCMP+TKIP][WPA2-EAP-CCMP+TKIP][ESS]
      00:xx:xx:83:fa:70 5240 -76 [WPA2-EAP-CCMP][ESS] Network2
      00:xx:xx:4f:e9:2c 2412 -67 [WPA2-PSK-CCMP][ESS][P2P] Printer
      00:xx:xx:af:fe:3e 5765 -79 [WPA2-PSK-CCMP][ESS] Network3
      00:xx:xx:e9:eb:29 2412 -76 [WPA2-PSK-CCMP][ESS] Network4
      00:xx:xx:26:4a:b9 2412 -79 [WPA2-PSK-CCMP][ESS][P2P] Printer2
      00:xx:xx:b9:0d:d4 2462 -79 [WPA2-PSK-CCMP][ESS] Network5

#. Set up your network connection replacing Network1 with your SSID name and
   Network1Password with the password for you network.

   .. code-block:: bash

      > add_network
      0
      > set_network 0 ssid "Network1"
      OK
      > set_network 0 psk "Network1Password"
      OK
      > enable_network 0
      OK
      <3>CTRL-EVENT-SCAN-STARTED
      <3>CTRL-EVENT-SCAN-RESULTS
      <3>SME: Trying to authenticate with 00:xx:xx:5d:d9:26 (SSID='Network1' freq=5180 MHz)
      <3>Trying to associate with 00:xx:xx:5d:d9:26 (SSID='Network1' freq=5180 MHz)
      <3>Associated with 00:xx:xx:5d:d9:26
      <3>CTRL-EVENT-SUBNET-STATUS-UPDATE status=0
      <3>WPA: Key negotiation completed with 00:xx:xx:5d:d9:26 [PTK=CCMP GTK=CCMP]
      <3>CTRL-EVENT-CONNECTED - Connection to 00:xx:xx:5d:d9:26 completed [id=0 id_str=]

#. Save the configuration, quit :command:`wpa_cli`. 

   .. code-block:: bash

      > save_config
      OK
      > quit

.. note:: 

   The password is saved as plaintext in
   :file:`/etc/wpa_supplicant/wpa_supplicant-$INTERFACE_NAME.conf`. 
   Use `wpa_passphrase <https://wiki.archlinux.org/index.php/WPA_supplicant#Connecting_with_wpa_passphrase>`_ for a more secure method.

Now, set up ``systemd-networkd.service`` to request an IP address. 

#. Create the :file:`/etc/systemd/network` directory and
   :file:`/etc/systemd/network/25-wireless.network`. Add the following (you
   will need to use the actual interface name rather than $INTERFACE_NAME in
   this case).

   .. code-block:: bash

      [Match]
      Name=$INTERFACE_NAME

      [Network]
      DHCP=ipv4

#. Restart the ``systemd-networkd.service`` and enable for future boots.

   .. code-block:: bash

      sudo systemctl restart systemd-networkd.service
      sudo systemctl enable --now wpa_supplicant@$INTERFACE_NAME.service

Other resources
***************

* NetworkManager CLI `documentation <https://developer.gnome.org/NetworkManager/stable/nmcli.html>`_.
* Additional CLI `examples <https://developer.gnome.org/NetworkManager/stable/nmcli-examples.html>`_.
* wpa_supplicant `advanced usage documentation <https://wiki.archlinux.org/index.php/WPA_supplicant#Advanced_usage>`_