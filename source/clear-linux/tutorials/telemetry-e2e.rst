.. _telemetry-e2e:


|CL-ATTR| includes a telemetry and analytics solution (also known as telemetrics) as part of the OS, which records events of interest and reports them back to the development team using the telemetrics client daemons.
End users can enable or disable the telemetry client component of |CL| and also redirect where records are sent if they wish to collect records for themselves by using their own telemetry backend server.

This tutorial walks you through setting up a telemetry backend server to manage your records, and using the telemetry API to add telemetry to your own applications.


Prerequisites
=============

For this tutorial, you can use an existing |CL| system, or you can start with a clean installation of |CL| on a new system
using the :ref:`bare-metal-install` getting started guide and:

#. Choose the automatic install.
#. Join the :guilabel:`Stability Enhancement Program` during the installation process to enable the telemetrics client components.

If you are using an existing |CL| system, make sure you have installed the telemetry bundle.  Use the :command:`swupd` utility with the `bundle-list` option and check for "telemetrics" in the list:

.. code-block:: bash

  sudo swupd bundle-list

If you need to install the telemetrics bundle, use :command:`swupd` to do so.

.. code-block:: bash

  sudo swupd bundle-add telemetrics

More information about enabling and configuring the telemetry client can be found at :ref:`telemetry-enable`.

Setting up the telemetry backend server
=======================================

To set up a telemetry backend server you can use the same |CL| system we're working with for this tutorial, or setup on a separate system.  Follow the :ref:`telemetry-backend` guide to setup the server and redirect your telemetry records to it. Refer to the :ref:`telemetry-config` guide to configure the telemetry client and specify where to send the records.

Once the telemetry backend server is running and/or you have enabled local retention of the records, and you have verified that your client is enabled and sending records to the server by using the :command:`hprobe` utility, you're ready to begin adding custom telemetry events to your applications.

Creating custom telemetry events
================================

Enabling telemetry during installation gives us everything we need on the client side to create custom telemetry events, even from C programs, because the telemetry bundle provides a simple pipe-based :abbr:`CLI (Commandline Interface)` program named :file:`telem-record-gen` that can be called trivially:

.. code-block:: bash

   ~ $ telem-record-gen --help

.. code-block:: console

   Usage:
     telem-record-gen [OPTIONS] - create and send a custom telemetry record

   Help Options:
     -h, --help            Show help options

   Application Options:
     -f, --config-file     Path to configuration file (not implemented yet)
     -V, --version         Print the program version
     -s, --severity        Severity level (1-4) - (default 1)
     -c, --class           Classification level_1/level_2/level_3
     -p, --payload         Record body (max size = 8k)
     -P, --payload-file    File to read payload from
     -R, --record-version  Version number for format of payload (default 1)
     -e, --event-id        Event id to use in the record


.. note::

  The C library (:file:`libtelemetry.so - man 3 telemetry`) uses the same API parameters and will yield the same effect as :command:`telem-record-gen`.

Let's try generating a simple heartbeat event with :command:`telem-record-gen`, similar to the hprobe heartbeat probe that |CL| includes by default.

.. code-block:: bash

   ~ $ telem-record-gen -c org.clearlinux/hello/world -p "hello there"

We won't see anything happen on the console, but we can track existing and previous telemetry events with :command:`telemctl`:

.. code-block:: bash

  ~$ sudo telemctl journal -V -c org.clearlinux/hello/world -i

.. code-block:: console

   org.clearlinux/hello/world     Tue 2018-11-06 23:00:48 UTC 72e55923fd21c75142c24dcfe0ae0a79 143f2580dcf80267f8f1dfe448f3c975 75f547ff-e55b-44b1-9333-1106098bd448
   hello there

Using the telemetry API in your C application
=============================================

.. note::
  More details about the :ref:`telemetry-z-api` are available in the telemetry guide.

Confirm that the telemetrics header file is located on the system at :file:`/usr/include/telemetry.h`  The `latest version`_ of the file can also be found on github for reference, but installing the `telemetry` bundle will install the header file that matches your |CL| version.

You will need to include the following headers in your code to use the API:

::

 #define _GNU_SOURCE
 #include <stdlib.h>
 #include <stdio.h>
 #include <string.h>
 #include <telemetry.h>


Use the following code to create the variables we need to hold the data for the record we will be creating:

::

 uint32_t severity = 1;
 uint32_t payload_version = 1;
 char classification[30] = "org.clearlinux/hello/world";
 struct telem_ref *tm_handle = NULL;
 char *payload;
 int ret = 0;



Severity:
 | Type: uint32_t
 | Value:  Severity field value. Accepted values are in the range 1-4, with 1 being the lowest severity, and 4 being the highest severity. Values provided outside of this range are clamped to 1 or 4. [low, med, high, crit]

Payload_version:
 | Type: uint32_t
 | Value: Payload format version. The only supported value right now is 1, which indicates that the payload is a freely-formatted (unstructured) string. Values greater than 1 are reserved for future use.

Classification:
  | Type: char array
  | Value: It should have the form, DOMAIN/PROBENAME/REST: DOMAIN is the reverse domain to use as a namespace for the probe (e.g. org.clearlinux); PROBENAME is the name of the probe; and REST is an arbitrary value that the probe should use to classify the record. The maximum length for the classification string is 122 bytes. Each sub-category may be no longer than 40 bytes long. Two / delimiters are required.

Tm_handle:
  | Type: Telem_ref struct pointer
  | Value:  Struct pointer declared by the caller, The struct is initialized if the function returns success.

Payload:
  | Type: char pointer
  | Value: The payload to set



For this example, we'll set the payload to “hello” by using ``asprintf()``

::

    if (asprintf(&payload, "hello\n") < 0) {
       exit(EXIT_FAILURE);
       }



The functions ``asprintf()`` and ``vasprintf()`` are analogs of ``sprintf(3)`` and    ``vsprintf(3)``, except that they allocate a string large enough to hold the output including the terminating null byte ('\0'), and return a pointer to it via the first argument.  This pointer should be passed to ``free(3)`` to release the allocated storage when it is no longer needed.


Create the new telemetry record
*******************************

The  function  ``tm_create_record()`` initializes a telemetry record and sets the severity and classification of that record, as well as the payload version number. The memory needed to store the telemetry record is allocated and should be freed with ``tm_free_record()`` when no longer needed.

::

 if ((ret = tm_create_record(&tm_handle, severity,  classification, payload_version)) < 0) {
  printf("Failed to create record: %s\n", strerror(-ret));
  ret = 1;
  goto fail;
  }


Set the payload field of a telemetrics record
*********************************************

The function ``tm_set_payload()`` attaches the provided telemetry record data to the telemetry record. The current maximum payload size is 8192b.

::

  if ((ret = tm_set_payload(tm_handle, payload)) < 0) {
    printf("Failed to set record payload: %s\n", strerror(-ret));
    ret = 1;
    goto fail;
  }
  free(payload);

The ``free()`` function frees the memory space pointed to by ptr, which must have been returned by a previous call to ``malloc()``, ``calloc()``, or ``realloc()``.  Otherwise, or if ``free(ptr)`` has already been called before, undefined behavior occurs.  If ptr is NULL, no operation is performed.

Send a record to the telemetrics daemon
***************************************

The function ``tm_send_record()`` delivers the record to the local ``telemprobd(1)`` service. Since the telemetry record was allocated by the program it should be freed with ``tm_free_record()`` when it is no longer needed.

::

  if ((ret = tm_send_record(tm_handle)) < 0) {
    printf("Failed to send record to daemon: %s\n", strerror(-ret));
    ret = 1;
    goto fail;
  } else {
    printf("Successfully sent record to daemon.\n");
    ret = 0;
  }
  fail:
  tm_free_record(tm_handle);
  tm_handle = NULL;

  return ret;


Full sample application with compiling flags
============================================

Create a new file test.c  add the following code.

::

  #define _GNU_SOURCE
  #include <stdlib.h>
  #include <stdio.h>
  #include <string.h>
  #include <telemetry.h>

  int main(int argc, char **argv)
  {
        uint32_t severity = 1;
        uint32_t payload_version = 1;
        char classification[30] = "org.clearlinux/hello/world";
        struct telem_ref *tm_handle = NULL;
        char *payload;

        int ret = 0;

        if (asprintf(&payload, "hello\n") < 0) {
                exit(EXIT_FAILURE);
        }

        if ((ret = tm_create_record(&tm_handle, severity, classification,
                                    payload_version)) < 0) {
                printf("Failed to create record: %s\n", strerror(-ret));
                ret = 1;
                goto fail;
        }

        if ((ret = tm_set_payload(tm_handle, payload)) < 0) {
                printf("Failed to set record payload: %s\n", strerror(-ret));
                ret = 1;
                goto fail;
        }

        free(payload);

        if ((ret = tm_send_record(tm_handle)) < 0) {
                printf("Failed to send record to daemon: %s\n", strerror(-ret));
                ret = 1;
                goto fail;
        } else {
                printf("Successfully sent record to daemon.\n");
                ret = 0;
        }
  fail:
        tm_free_record(tm_handle);
        tm_handle = NULL;

        return ret;
   }



Compile with the gcc compiler, using this command:

.. code-block:: bash

  gcc test.c -ltelemetry -o test_telem


Test to ensure the program is working:

.. code-block:: bash

  ./test_telem
  Successfully sent record to daemon.

Verify record was received
*****************************

To verify that the heartbeat message was received by the telemetry backend server you can check the telemetry client journal, and specify the classification as org.clearlinux/hello/world
:

.. code-block:: bash

  sudo telemctl journal -V -c org.clearlinux/hello/world -i

.. code-block:: console

  Classification                 Time stamp                  Record ID                        Event ID                         Boot ID
  org.clearlinux/hello/world     Tue 2018-11-06 22:58:25 UTC b11db07c58c90d8f496ff963df6c43de 24699c2d60c12d154692875b599ca957 75f547ff-e55b-44b1-9333-1106098bd448
  hello
  Total records: 1



A full example of the `heartbeat probe`_ in C is documented in the source code.  For more information about telemetrics in |CL| refer to the :ref:`telemetrics` guide.


You can also look for the record on the telemetry backend server. 

.. _latest version:
https://github.com/clearlinux/telemetrics-client/tree/master/src

.. _heartbeat probe: https://github.com/clearlinux/telemetrics-client/tree/master/src/probes/hello.c
