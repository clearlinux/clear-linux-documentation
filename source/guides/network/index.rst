.. _network-guides:

Network
#######

.. container:: multicolumns three underline

   .. container:: column smallcard featurecard
 
      .. container:: smallcard content

         :ref:`vnc`
            Learn how to use VNC to connect to a remote |CL| host.

   .. container:: column smallcard featurecard
 
      .. container:: smallcard content
      
         :ref:`assign-static-ip`
            Discover how to identify which program is managing the network
            interface and set a static IP.

   .. container:: column smallcard featurecard

      .. container:: smallcard content

         :ref:`openssh-server`
            Learn how to set up the SSH service.

.. container:: multicolumns three

   .. container:: column smallcard
 
      .. container:: smallcard content

         :ref:`dpdk`
            Find out how to send packets between two platforms using the
            :abbr:`DPDK (Data Plane Development Kit)`

   .. container:: column smallcard
 
      .. container:: smallcard content

         :ref:`firewall`
            Discover how to control access to and from systems based on network packet attributes like IP address, port, and payload.

   .. container:: column smallcard
 
      .. container:: smallcard content

         :ref:`network-bonding`
            Learn how to configure :command:`systemd` to use the bonding driver
            for improved redundancy and bandwidth aggregation.

   .. container:: column smallcard
 
      .. container:: smallcard content

         :ref:`time`
            Find out how to reset the time on your |CL| system when the default
            :abbr:`NTP (Network Time Protocol)` servers cannot be reached.

   .. container:: column smallcard
 
      .. container:: smallcard content

         :ref:`wi-fi`
            Learn how to configure Wi-Fi using :command:`NetworkManager` or
            the underlying :command:`wpa_supplicant`.

.. toctree::
   :glob:
   :hidden:

   *