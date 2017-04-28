.. _os-core:

os-core
#######

This bundle contains the basic core components of the operating system.
|CLOSIA| relies on `systemd` to provide the basic OS components. The
`systemd` package contains solutions for:

* Service management
* Basic network management
* Hostname management
* Time synchronization management
* Boot control management
* Journal management

Additionally, `os-core` includes the `util-linux` and `coreutils` packages to
provide a set of basic Linux\* command line tools such as `ls`, `cp`, `rm`,
etc.


Static IP
=========

To configure a static IP, follow these steps:

#. Create the file: :file:`/etc/systemd/network/50-static.network` If the
   path does not exist, create it.

#. Add, at the very least, the following lines to the
   :file:`50-static.network` file:

   .. code-block:: console

      [Match]
      Name=<device_name>

      [Network]
      Address=<Provide a static IPv4 or IPv6 address with its
      prefix length. Separate them with the "/" character.>
      Gateway=<The gateway's address>

   The `<device_name>` is your network device name, for example: enp1s0 or
   enp0s25.

#. To add more options you can consult the `systemd network configuration`_
   manual.

#. Restart the *systemd-networkd* service with the following command:


   .. code-block:: console

      # systemctl restart systemd-networkd

   Alternatively, restart |CL|.

#. Check the new IP with the following command:

   .. code-block:: console

      # ip addr


Setting time
============

Clear Linux uses the `systemd-timesyncd.service` service to synchronize the
system's time. Default :abbr:`NTP (Network Time Protocol)` servers are
configured, for example: `time1.google.com`, `time2.google.com`,
`time3.google.com`, and `time4.google.com`. Manually setting the time via
`timedatectl` or using RTC mode is not possible. If those servers cannot be
reached and the system time is incorrect, follow these steps:

#. Set the timezone, for example, Pacific time:

   .. code-block:: console

      timedatectl set-timezone America/Los_Angeles

   To see a list of timezones, use the following command:

   .. code-block:: console

      timedatectl list-timezones

#. Go to the :file:`/etc/systemd/` directory, if it does not exist, create
   it.

#. Create the :file:`/etc/systemd/timesyncd.conf` file and enter the
   following lines:

   .. code-block:: console

      [Time]
      NTP=<Preferred Server>
      FallbackNTP=<backup server 1> <backup server 2>

#. Restart the timesync daemon with the following command:

   .. code-block:: console

      # systemctl  restart systemd-timesyncd

.. _systemd network configuration:
   https://www.freedesktop.org/software/systemd/man/systemd.network.html
