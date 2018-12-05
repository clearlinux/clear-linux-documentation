.. _telemetry-journal:

telemctl journal
################

The telemctl ``journal`` command gives you access to features and options of
the telemetry journal to assist with system analytics and debug. The
:command:`telemctl journal` has a number of options to help filter
records. Use :command:`-h` or :command:`--help` to view usage options.

.. code-block:: bash

   sudo telemctl journal -h

::

   -r,  --record_id        Print record with specific record_id
   -e,  --event_id         Print records with specific event_id
   -c,  --classification   Print records with specific classification
   -b,  --boot_id          Print records with specific boot_id
   -i,  --include_record   Include record content
   -V,  --verbose          Verbose output
   -h,  --help             Display this help message

Journal Output
**************

To see the listing of records in the journal, run the command:

.. code-block:: bash

   sudo telemctl journal -V

This will produce output like the following:

.. list-table:: **Table 1. Journal Output**
   :widths:  10 30 20 20 20
   :header-rows: 1

   * - Classification
     - Time stamp
     - Record ID
     - Event ID
     - Boot ID

   * - org.clearlinux/heartbeat/ping
     - Fri 2018-09-21 00:00:57 UTC
     - 269e8e4026e6aa440c4d2ed71e38efcd
     - b3a51b5e62a008ed0b56d1740be67d48
     - 853a75aa-da3b-4356-a085-079abab3ffe1

   * - org.clearlinux/hello/world
     - Fri 2018-09-21 17:53:21 UTC
     - b06c8d31adf5ccc7d5d3f8959d8d3e72
     - 57c64c79a9b911d68f4dab10a00267d7
     - 853a75aa-da3b-4356-a085-079abab3ffe1

   * - org.clearlinux/crash/clr
     - Fri 2018-09-21 17:57:59 UTC
     - b62cd4278672ae3331cf121bc7a8e1c6
     - b6adb5751382c48eebb7ee007fe1790a
     - 853a75aa-da3b-4356-a085-079abab3ffe1

Each line gives information about a distinct record.  The :command:`-V` or
:command:`--verbose` option adds the header to identify the Classification,
Time Stamp, Record ID, Event ID and Boot ID for each record. The journal
feature can filter records according to the Classification, Record ID, Event
ID and Boot ID by using the :command:`-c`,:command:`-r`, :command:`-e` and
:command:`-b` options accordingly.

Payload Information
********************

From the previous output, you may want to get more information about the
record with the "org.clearlinux/crash/clr" classification to help debug a
crash.  You can use the :command:`-c` and :command:`-i` options to see the payload of the record, like this:

.. code-block:: bash

   sudo telemctl journal -c org.clearlinux/crash/clr -i

.. code-block:: console

   org.clearlinux/crash/clr       Tue 2018-09-25 18:43:50 UTC 07ae583edbd13829965d67e9ba97d70c 69c600470769c841649266178375d67e d32c13d1-fda0-49c6-8431-e6c5b29cbefa
   Process: /usr/bin/bash
   PID: 685
   Signal: 11

   Backtrace (TID 685):
   #0 kill() - [libc.so.6]
   #1 bash_tilde_expand() - [/usr/bin/bash]
   #2 maybe_execute_file() - [/usr/bin/bash]
   #3 main() - [/usr/bin/bash]
   #4 __libc_start_main() - [libc.so.6]
   #5 _start() - [/usr/bin/bash]

If you have records of multiple crashes, you can use the :command:'-r'
option to specify the record more precisely, rather than going by
classification. You can also specify a classification of record and use the
:command:'-i' option to see the payload of each record with that
classification.

Next steps
==========

Adding telemetry to your applications:

* :ref:`telemetry-api`
