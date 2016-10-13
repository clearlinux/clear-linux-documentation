.. _bdl-os-core:

os-core
#######

This bundle contains the basic core OS components.

Static IP
=========

To configure a static IP you should follow the next steps:

#. Create file :file:`/etc/systemd/network/50-static.network`. If a directory
   does not exist, please create it.

#. The minimum lines the :file:`50-static.network` file should contain are::
   
     [Match]
     Name=<device_name>

     [Network]
     Address=<A static IPv4 or IPv6 address and its prefix length, separated by a "/" character>
     Gateway=<The gateway address>

   The *<device_name>* is your network device name (i.e. enp1s0 or enp0s25).

#. If you want to add more options you can consult the
   `systemd network configuration`_ manual.

#. Restart *systemd-networkd* service using:: 

     # systemctl restart systemd-networkd

   or restart Clear Linux.

#. Check new IP with::
  
     # ip addr


Setting Time
============

Clear Linux utilizes **systemd-timesyncd.service** to sync time. 
Default :abbr:`NTP (Network Time Protocol)` servers are
configured as *time1.google.com, time2.google.com, time3.google.com, and
time4.google.com*. It is not possible to set the time manually, via
*timedatectl*
or to use RTC mode. In the event that those servers cannot be reached and the
time is incorrect on your system, try these steps:

#. Make sure that you've set your timezone:

   * If you at Pacific time::

       timedatectl set-timezone America/Los_Angeles

     or you can choose a preferred timezone

   * To see a list of timezones, do::

       timedatectl list-timezones | grep <locale>

#. Create :file:`/etc/systemd/` directory

#. Open your chosen editor and type into the
   :file:`/etc/systemd/timesyncd.conf` file::

    [Time]
    NTP=<Preferred Server>
    FallbackNTP=<backup server 1> <backup server 2>

#. Restart timesync daemon::

    # systemctl  restart systemd-timesyncd

.. note:: Check to make sure your time is correctly set: date





.. _systemd network configuration: https://www.freedesktop.org/software/systemd/man/systemd.network.html
