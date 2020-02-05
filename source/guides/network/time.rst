.. _time:

Set system time
###############

This guide describes how to reset the time in your |CL-ATTR| system when
the default :abbr:`NTP (Network Time Protocol)` servers cannot be reached.

|CL| uses the `systemd-timesyncd.service` daemon to synchronize time.


#. Install the :command:`sysadmin-basic` bundle.

   .. code-block:: bash

      sudo swupd bundle-add sysadmin-basic

#. Set your time zone. This example uses Los Angeles.

   .. code-block:: bash

      timedatectl set-timezone America/Los_Angeles

   .. note::

      To see a list of time zones, use the command:
      :command:`timedatectl list-timezones | grep <locale>`

#. Create a :file:`/etc/systemd/` directory.

   .. code-block:: bash

      sudo mkdir -p /etc/systemd/

#. Create a new file named :file:`/etc/systemd/timesyncd.conf` and enter the
   following text.

   .. code-block:: console

      [Time]
      NTP=<Preferred Server>
      FallbackNTP=<backup server 1> <backup server 2>

#. Enable the `systemd-timesyncd` service.

   .. code-block:: bash

      sudo timedatectl set-ntp true

.. note::

   To check the service status, use the :command:`timedatectl status` command.

   To restart the `timesyncd` daemon, enter :command:`systemctl restart
   systemd-timesyncd` into your terminal emulator.

**Congratulations!** You successfully set up the time in your |CL| system.


