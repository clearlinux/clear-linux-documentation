.. _time:

Set the time
############

In |CL|, it is not possible to set the time manually, via `timedatectl`
nor `RTC` mode. |CLOSIA| instead uses the `systemd-timesyncd.service` daemon
to synchronize time.

This section provides instructions to reset the time in your |CL| system when
the default network time protocol (NTP) servers cannot be reached. The default
NTP servers are configured as
time1.google.com, time2.google.com, time3.google.com, and time4.google.com.

#. Install the `sysadmin-basic` bundle:

   .. code-block:: console

      swupd bundle-add sysadmin-basic

#. Set your timezone (this example uses Los Angeles).

   .. code-block:: console

      timedatectl set-timezone America/Los_Angeles

   .. note::
      To see a list of timezones, enter:
      `timedatectl list-timezones | grep <locale>`

#. Create a `/etc/systemd/` directory.

   .. code-block:: console

      mkdir -p /etc/systemd/

#. Create a new file named :file:`/etc/systemd/timesyncd.conf` and enter the
   following:

   .. code-block:: .conf

      [Time]
      NTP=<Preferred Server>
      FallbackNTP=<backup server 1> <backup server 2>

#. Enable the `systemd-timesyncd` service.

   .. code-block:: console

      timedatectl set-ntp true

.. note::

   Use the :command:`timedatectl status` command to check the service status.
   To restart the `timesyncd` daemon, enter :command:`systemctl restart systemd-timesyncd`
   into your terminal emulator.
