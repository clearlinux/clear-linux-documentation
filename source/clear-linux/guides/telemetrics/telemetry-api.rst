.. _telemetry-api

Telemetry API
#############

Installing the ``telemetrics`` bundle includes the libtelemetry C library,
which exposes an API used by the telemprobd and telempostd daemons. You
can use these in your applications as well. The API documentation is found
in the :file:`telemetry.h` file in `Telemetrics client`_ repository.

Creating records with telem-record-gen
**************************************

The telemetrics bundle also provides a record generator tool called
``telem-record-gen``. This tool can be used to create records from shell
scripts, etc., when writing a probe in C is not desirable. Records are sent
to the backend server, and can also be echoed to stdout.

telem-record-gen usage
======================

.. code-block:: bash

   telem-record-gen [OPTIONS] - create and send a custom telemetry record

.. code-block:: console

   Help Options:
   -h, --help            Show help options

   Application Options:
   -V, --version         Print the program version
   -s, --severity        Severity level (1-4) - (default 1)
   -c, --class           Classification level_1/level_2/level_3 (required)
   -p, --payload         Record body (max size = 8k) (required)
   -P, --payload-file    File to read payload from
   -R, --record-version  Version number for format of payload (default 1)
   -e, --event-id        Event id to use in the record
   -o, --echo            Echo record to stdout
   -n, --no-post         Do not post record just print

The :command:`-c` and :command:`-p` options are required; defaults are
supplied for most other options. The maximum payload size is 8k
(8192 bytes). Excess is ignored, regardless of source (file/commandline/
stdin). An empty payload is allowed, but even an empty payload must be
specified in one of the three ways shown below.

telem-record-gen examples
=========================

There are three ways to supply the payload to the record.

#. On the command line, use the :command:`-p <string>` option:

   .. code-block:: bash

      telem-record-gen -c a/b/c -n -o -p 'payload goes here'

   .. code-block:: console

      record_format_version: 4
      classification: a/b/c
      severity: 1
      machine_id: FFFFFFFF
      creation_timestamp: 1539023189
      arch: x86_64
      host_type: innotek GmbH|VirtualBox|1.2
      build: 25180
      kernel_version: 4.14.71-404.lts
      payload_format_version: 1
      system_name: clear-linux-os
      board_name: VirtualBox|Oracle Corporation
      cpu_model: Intel(R) Core(TM) i7-4650U CPU @ 1.70GHz
      bios_version: VirtualBox
      event_id: 2236710e4fc11e4a646ce956c7802788

      payload goes here

#. Specify a file that contains the payload with the option
   :command:'-P path/to/file'.

   .. code-block:: bash

      telem-record-gen -c a/b/c -n -o -P ./payload_file.txt

   .. code-block:: console

      record_format_version: 4
      classification: a/b/c
      severity: 1
      machine_id: FFFFFFFF
      creation_timestamp: 1539023621
      arch: x86_64
      host_type: innotek GmbH|VirtualBox|1.2
      build: 25180
      kernel_version: 4.14.71-404.lts
      payload_format_version: 1
      system_name: clear-linux-os
      board_name: VirtualBox|Oracle Corporation
      cpu_model: Intel(R) Core(TM) i7-4650U CPU @ 1.70GHz
      bios_version: VirtualBox
      event_id: d73d6040afd7693cccdfece479df9795

      payload read from file

#. If the :command:`-p` or :command:`-P` options are absent, the tool reads
   from stdin so you can use it in a HEREDOC in scripts.

   .. code-block:: bash

      telem-record-gen -c a/b/c -n -o << HEOF
      payload read from stdin
      HEOF

   .. code-block:: console

      record_format_version: 4
      classification: a/b/c
      severity: 1
      machine_id: FFFFFFFF
      creation_timestamp: 1539023621
      arch: x86_64
      host_type: innotek GmbH|VirtualBox|1.2
      build: 25180
      kernel_version: 4.14.71-404.lts
      payload_format_version: 1
      system_name: clear-linux-os
      board_name: VirtualBox|Oracle Corporation
      cpu_model: Intel(R) Core(TM) i7-4650U CPU @ 1.70GHz
      bios_version: VirtualBox
      event_id: 2f070e8e71679f2b1f28794e3a6c42ee

      payload read from stdin

   .. note::

      Although only the classification and payload are specified, the tool supplies values for the remaining values.

Telemetry records and the REST API
==================================

If you have not configured the telemetry client to keep records locally, you
can view them using the Web UI of the server, or you can query them from the
server using the REST API provided by |CL| telemetrics. The API is
available at :file:`<server>/api/records`, and when queried, returns a JSON
response that contains a list of records. There are several parameters for
filtering queries, similar to the filters available through the telemetryui Records view.

* classification: The classification of the record
* severity: The severity of the record. Restricted to integer value
* machine_id: The id of the machine where this record was generated on
* build: The build on which the record was generated. Restricted to 256
  characters.
* created_in_days: causes the query to return records created after the last
  given days
* created_in_sec: returns the records created after the last given seconds
* limit: The maximum number of records to be returned.

Next Steps
==========

* :ref:`telemetry-backend`
* `Telemetrics client`_

Related topics
==============

* :ref:`telemetry-about`

.. _Telemetrics client: https://github.com/clearlinux/telemetrics-client/
