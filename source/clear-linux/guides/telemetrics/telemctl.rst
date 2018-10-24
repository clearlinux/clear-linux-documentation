.. _telemctl:

Use telemctl options
####################

The |CL-ATTR| telemetry client provides an admin tool called telemctl for
managing the telemetry services and probes. The tool is located in
:file:` /usr/bin`. Running it with no argument results in the following:

.. code-block:: bash

   sudo telemctl

.. code-block:: console

   /usr/bin/telemctl - Control actions for telemetry services
     stop       Stops all running telemetry services
     start      Starts all telemetry services
     restart    Restarts all telemetry services
     is-active  Checks if telemprobd and telempostd are active
     opt-in     Opts in to telemetry, and starts telemetry services
     opt-out    Opts out of telemetry, and stops telemetry services
     journal    Prints telemetry journal contents. Use -h argument for more
                options

telemctl commands:
******************

start/stop/restart
==================

The commands to start, stop and restart the telemetry services manage all
required services and probes on the system.  There is no need to separately
start/stop/restart the two client daemons **telemprobd** and **telempostd**.
The **restart** command option will call **telemctl stop** followed by **
telemctl start**

is-active
=========

The `is-active` option reports whether the two client daemons are active.
This is useful to verify that the **opt-in** and **opt-out** options have
taken effect, or to ensure that telemetry is functioning on the system.
Note that both daemons are verified.

.. code-block:: bash

   sudo telemctl is-active

.. code-block:: console

   telemprobd : active
   telempostd : active

.. include:: ./telemetry-enable.rst
   :start-after: incl-opt-in-out-telemetry:
   :end-before: Remove the telemetry software bundle

.. note::

   To opt-in but not immediately start telemetry services, run the command
   :command:`sudo telemctl stop` after the :command:`opt-in` command is
   entered. Once you are ready to start the service, enter the command
   :command:`sudo telemctl start`.

Next steps
==========

Learn to read records:

* :ref:`telemetry-journal`
