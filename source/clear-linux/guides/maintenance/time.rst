.. _time:

Set the time
############

|CLOSIA| uses the `systemd-timesyncd.service` daemon to synchronize time.

This section provides instructions to reset the time in your |CL| system when
the default :abbr:`NTP (Network Time Protocol)` servers cannot be reached.

#. Install the `sysadmin-basic` bundle:

   .. code-block:: console

      swupd bundle-add sysadmin-basic

#. Set your timezone. This example uses Los Angeles.

   .. code-block:: console

      timedatectl set-timezone America/Los_Angeles

   .. note::
      To see a list of timezones, enter:
      `timedatectl list-timezones | grep <locale>`

#. Create a :file:`/etc/systemd/` directory.

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

Congratulations! You have successfully set up the time in your |CL| system.

Further, you are now able to change the time and timezone from your |CL|
desktop. The :guilabel:`Date & Time` options are located in the
:guilabel:`Settings` application under the :guilabel:`Details`
tab.


