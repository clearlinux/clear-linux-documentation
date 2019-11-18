.. _wi-fi:

Configure Wi-Fi
###############

We recommend using `NetworkManager <https://developer.gnome.org/NetworkManager/stable/NetworkManager.html>`_ to manage network connections. If you
choose to connect to Wi-Fi while using the
:ref:`live installer <bare-metal-install-desktop>` image, your Wi-Fi settings
will be added to your system during the installation process.

NetworkManager provides three simple methods for configuring Wi-Fi.

.. contents::
   :local:
   :depth: 1

Desktop GUI (Graphical User Interface)
**************************************

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
****************************

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
*******************************

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

Other resources
***************

* NetworkManager CLI `documentation <https://developer.gnome.org/NetworkManager/stable/nmcli.html>`_.
* Additional CLI `examples <https://developer.gnome.org/NetworkManager/stable/nmcli-examples.html>`_.