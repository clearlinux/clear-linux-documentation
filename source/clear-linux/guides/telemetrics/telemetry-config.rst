.. _telemetry-config:

Telemetry Client Configuration
##############################

The telemetry client will look for the configuration file located at
:file:`/etc/telemetrics/telemetrics.conf` and use it if it exists. If the
file does not exist, the client will use the default configuration located
at :file:`/usr/share/defaults/telemetrics/telemetrics.conf`. To modify or
customize the configuration, copy the file from
:file:`/usr/share/defaults/telemetrics` to
:file:`/etc/telemetrics` and edit it.

Configuration Options
*********************
The client uses the following configuration options from the config file:

* **server**: This specifies the web server to which telempostd sends the
  telemetry records.
* **socket_path**: This specifies the path of the unix domain socket that
  the telemprobd listens on for connections from the probes.
* **spool_dir**: This configuration option is related to spooling. If the
  daemon is not able to send the telemetry records to the backend server due
  to reasons such as the network availability, then it stores the records in
  a spool directory. This option specifies that path of the spool directory.
  This directory should be owned by the same user as the daemon.

  - mkdir -p /var/spool/telemetry
  - chown -R telemetry:telemetry /var/spool/telemetry
  - systemctl restart telemprobd.service

* **record_expiry**: This is the time in minutes after which the records in
  the spool directory are deleted by the daemon.
* **spool_process_time**: This specifies the time interval in seconds that
  the daemon waits for before checking the spool directory for records. The
  daemon picks up the records in the order of modification date and tries to
  send the record to the server. It sends a maximum of 10 records at a time.
  If it was able to send a record successfully, it deletes the record from
  the spool. If the daemon finds a record older than the "record_expiry"
  time, then it deletes that record. The daemon looks at a maximum of 20
  records in a single spool run loop.
* **rate_limit_enabled**: This determines whether rate-limiting is enabled or
  disabled. When enabled, there is a threshold on both records sent within a
  window of time, and record bytes sent within a window a time.
* **record_burst_limit**: This is the maximum amount of records allowed to be
  passed by the daemon within the record_window_length of time. If set to
  -1, the rate-limiting for record bursts is disabled.
* **record_window_length**: The time in minutes (0-59) that
  establishes the window length for the record_burst_limit. EX: if
  record_burst_window=1000 and record_window_length=15, then no more than
  1000 records can be passed within any given fifteen minute window.
* **byte_burst_limit**: This is the maximum amount of bytes that can be
  passed by the daemon within the byte_window_length of time. If set to -1, the rate-limiting for byte bursts is disabled.
* **byte_window_length**: This is the time, in minutes (0-59), that
  establishes the window length for the byte_burst_limit.
* **rate_limit_strategy**: This is the strategy chosen once the rate-limiting
  threshold has been reached. Currently the options are 'drop' or 'spool',
  with spool being the default. If spool is chosen, records will be spooled
  and sent at a later time.
* **record_retention_enabled**: When this key is enabled (true) the daemon
  saves a copy of the payload on disk from all valid records. To avoid the
  excessive use of disk space only the latest 100 records are kept. The
  default value for this configuration key is false.
* **record_server_delivery_enabled**: This key controls the delivery of
  records to server; when enabled (default value), the record will be posted
  to the address in the configuration file. If this configuration key is
  disabled (false), records will not be spooled or posted to backend. This
  configuration key can be used in combination with record_retention_enabled
  to keep copies of telemetry records locally only.

  .. note::

  	 Configuration options may change as the telemetry client evolves.
  	 Please use the comments in the file itself as the most accurate
  	 reference for configuration.

Setting a static machine id
===========================

The machine id reported by the telemetry client is rotated every 3 days for
privacy reasons. If you wish to have a static machine id for testing
purposes, you can opt in by creating a static machine id file named
"opt-in-static-machine-id" under the directory  :file:`/etc/telemetrics/`.
Where "unique machine ID" is your desired static machine ID.

.. code-block:: bash

   sudo mkdir -p /etc/telemetrics

.. code-block:: bash

   sudo echo "unique machine ID" > /etc/telemetrics/opt-in-static-machine-id

.. note::

   The machine id mentioned here is not the same as the system hostname. Learn how to :ref:`hostname`: 

Next steps
==========

* :ref:`telemctl`
