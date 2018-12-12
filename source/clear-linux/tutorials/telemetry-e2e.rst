.. _telemetry-e2e:


|CL-ATTR| includes a telemetry and analytics solution (also known as telemetrics) as part of the OS, which records events of interest and reports them back to the development team using the telemetrics client daemons.

End users can enable or disable the telemetry client component of |CL| and also redirect where records are sent if they wish to collect records for themselves by using their own telemetry backend server. More detailed information about using and configuring the telemetrics client is found in the :ref:`telemetrics` guide.

This tutorial walks you through setting up a telemetry backend server to manage your records, and how to use the telemetry API to add telemetry to your own applications.

.. contents:: :local:
   :depth: 1


Prerequisites
=============


For this tutorial, you can use an existing |CL| system, or you can start with a clean installation of |CL| on a new system.

New Installation
****************

To setup a new system for your telemetry backend server, follow the :ref:`bare-metal-install` getting started guide and:

#. Choose to install |CL|.
#. Join the :guilabel:`Stability Enhancement Program` during the installation process to enable the telemetrics client components.
#. Select the manual installation method with the following settings:
   * Set the hostname to :guilabel:`clr-telem-server`
   * Create an administrative user named :guilabel:`clear` and add this user to sudoers :ref:`enable-user-space`
   * Choose the :file:`dev-utils`, :file:`network-basic`, and :file:`openssh-server` bundles from the bundle list


.. note::

   Bundles can also be added to your system after this install process completed.  The bundles listed here are a minimal set needed to complete the setup of the telemetry backend server and applications.

Existing System
***************

If you are using an existing |CL| system, make sure you have installed the telemetry and dev-utils bundles.  Use the :command:`swupd` utility with the `bundle-list` option and check for "telemetrics" in the list:

.. code-block:: bash

   sudo swupd bundle-list

If you need to install the bundles, use :command:`swupd` to do so.

.. code-block:: bash

   sudo swupd bundle-add telemetrics dev-utils

More information about enabling and configuring the telemetry client can be found at :ref:`telemetry-enable`.

You will need to run some of the commands in this tutorial with root privileges.  You can create a new user or add your user to the sudoers list :ref:`enable-user-space`.

Setting up the telemetry backend server
=======================================
We'll be using the :file:`deploy.sh` file from the `clearlinux/telemetrics-backend`_ Git repository to install required dependencies for the web server applications.  The script also configures nginx and uwsgi, deploys snapshots of the applications, and starts all required services.

Clone the clearlinux/telemetrics-backend Git repository
*******************************************************

With all prerequisite software bundles installed, log in with your administrative user, and from your :file:`$HOME` directory, run :command:`git` to clone the :guilabel:`telemetrics-backend` repository into the :file:`$HOME/telemetrics-backend` directory:

.. code-block:: bash

   git clone https://github.com/clearlinux/telemetrics-backend

.. note::

   You may need to set up the :envvar:`https_proxy` environment variable if you have issues reaching github.com.

Run the deploy.sh script to install the backend server
******************************************************

Change your current working directory to :file:`telemetrics-backend/scripts`.

.. code-block:: bash

   cd telemetrics-backend/scripts

Run the :command:`./deploy.sh -h` to see the list of options for the :command:`deploy.sh` script:

.. code-block:: console

   ./deploy.sh -h
   Deploy snapshot of the telemetrics-backend

        -a    Perform specified action (deploy, install, migrate, resetdb,
              restart, uninstall; default: deploy)
        -d    Distro to deploy to (ubuntu, centos or clr; default: ubuntu)
        -h    Print these options
        -H    Set domain for deployment (only accepted value is "localhost" for
              now)
        -r    Set repo location to deploy from
              (default: https://github.com/clearlinux/telemetrics-backend)
        -s    Set source location (default: "master" branch from git repo)
        -t    Set source type (tarball, or git; default: git)
        -u    Perform complete uninstallation

The :command:`deploy.sh` is a bash shell script that allows you to perform the following actions:

* *deploy* - install a complete instance of the telemetrics backend server and all required components. This is the default action if no *-a* argument is given on the command line.
* *install* - installs and enables all required components for the telemetrics backend server.
* *migrate* - migrate database to new schema.
* *resetdb* - reset the database.
* *restart* - restart the nginx and uWSGI services.
* *uninstall* - uninstall all packages.

.. note::

   The *uninstall* option does not perform any actions if the distro is set to |CL| and will only uninstall packages if the distro is Ubuntu

Next, we will install the telemetrics backend server with the following options:

* *-a install* to perform an install
* *-d clr* to install to a |CL| distro
* *-H localhost* to set the domain to localhost

We do not need to set the following options since the values are set to the correct values we want by default:

* *-r https://github.com/clearlinux/telemetrics-backend* sets the repo location for :command:`git` to clone from.
* *-s master* to set the location, or branch.
* *-t git* to set the source type to git.

.. caution::
   The :file:`deploy.sh` shell script has minimal error checking and makes several changes to your system.  Be sure that the options you define on the cmdline are correct before proceeding.

To begin the installation with the options defined:

Run the shell script from the :file:`$HOME/telemetrics-backend/scripts` directory:

.. code-block:: bash

   ./deploy.sh -H localhost -a install -d clr

The script will start and list all the defined options and prompt you for the :guilabel:`PostgreSQL` database password as shown below:

.. code-block:: console

    Options:
      host: localhost
      distro: clr
      action: install
      repo: https://github.com/clearlinux/telemetrics-backend
      source: master
      type: git
    DB password: (default: postgres):

For the :guilabel:`DB password:`, press the :kbd:`Enter` key to accept the default password `postgres`.

The :command:`swupd` begins installing the required software bundles to set up the telemetrics backend server. The output will look similar to the following:

.. code-block:: console

   swupd-client bundle adder 3.12.7
       Copyright (C) 2012-2017 Intel Corporation

    Downloading packs...

    Extracting application-server pack for version 18740
         ...5%
    Extracting database-basic-dev pack for version 18670
         ...10%
    Extracting database-basic pack for version 18670
         ...15%
    .
    .
    .
    Extracting c-basic pack for version 18800
         ...89%
    Extracting os-core-dev pack for version 18800
         ...94%
    Extracting web-server-basic pack for version 18680
         ...100%
    Installing bundle(s) files...
         ...100%
    Calling post-update helper scripts.
    Possible filedescriptor leak : 8 (socket:[30833])
    Bundle(s) installation done.

.. note::

   This script uses :command:`sudo` to run commands and you may be prompted to enter your user password at any time while the script is executing. If this occurs, enter your user password to execute the :command:`sudo` command.

    .. code-block:: console

       Password:


   You may also see an informational message about setting the :envvar:`https_proxy` environment variable if this variable isn't set.


Once the :command:`swupd` command is complete, the script begins processing the requirements to install and implement the telemetrics server. Finally, the script enables the server and provides output that finishes with something similar to:

.. code-block:: console

  .
  .
  Successfully built alembic Flask-Migrate itsdangerous Mako MarkupSafe python-editor SQLAlchemy uWSGI WTForms
  Installing collected packages: SQLAlchemy, MarkupSafe, Mako, python-editor, six, python-dateutil, alembic, click, Werkzeug, Jinja2, itsdangerous, Flask, Flask-SQLAlchemy, Flask-Migrate, WTForms, Flask-WTF, psycopg2, uWSGI
  Running setup.py install for psycopg2 ... done
  Successfully installed Flask-0.12.2 Flask-Migrate-2.1.0 Flask-SQLAlchemy-2.2 Flask-WTF-0.14.2 Jinja2-2.9.6 Mako-1.0.7 MarkupSafe-1.0 SQLAlchemy-1.1.13 WTForms-2.1 Werkzeug-0.12.2 alembic-0.9.5 click-6.7 itsdangerous-0.24 psycopg2-2.7.3 python-dateutil-2.6.1 python-editor-1.0.3 six-1.10.0 uWSGI-2.0.15

Once all the server components have been installed you are prompted to enter the :guilabel:`PostgreSQL` database password to change it as illustrated below:

.. code-block:: console

   Enter password for 'postgres' user:
   New password:
   Retype new password:
   passwd: password updated successfully


Enter `postgres` for the current value of the password and then enter a new password, retype it to verify the new password and the :guilabel:`PostgreSQL` database password will be updated.

The script finalizes installation and finishes.

.. code-block:: console

   Created symlink /etc/systemd/system/multi-user.target.wants/postgresql.service → /usr/lib/systemd/system/postgresql.service.
   Cloning into 'telemetrics-backend'...
   remote: Counting objects: 344, done.
   remote: Compressing objects: 100% (53/53), done.
   remote: Total 344 (delta 30), reused 50 (delta 20), pack-reused 268
   Receiving objects: 100% (344/344), 130.20 KiB | 1.40 MiB/s, done.
   Resolving deltas: 100% (177/177), done.
   .
   .
   .
   Already using interpreter /usr/bin/python3
   Using base prefix '/usr'
   New python executable in /var/www/telemetry/venv/bin/python3
   Not overwriting existing python script /var/www/telemetry/venv/bin/python (you must use /var/www/telemetry/venv/bin/python3)
   Installing setuptools, pip, wheel...done.
   INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
   INFO  [alembic.runtime.migration] Will assume transactional DDL.
   INFO  [alembic.runtime.migration] Running upgrade  -> 3230c615d6e0, empty message
   INFO  [alembic.runtime.migration] Running upgrade 3230c615d6e0 -> 466cf2f35d67, empty message

   Install complete (installation folder: /var/www/telemetry)

Once the installation is complete you can use your web browser and view the new server by opening the web browser on your system and type in ``localhost`` in the address bar.

You should see a web page similar to the one shown in figure 1:

.. TODO fix links for figures
.. figure:: ../guides/telemetrics/telemetry-backend-1.png
   :scale: 50 %
   :alt: Telemetry UI

   Figure 1: :guilabel:`Telemetry UI`

Redirect telemetry records
**************************

Telemetry records generated by the telemetrics clients are sent to the server location defined in the :file:`/usr/share/defaults/telemetrics/telemetrics.conf` configuration file. You can customize this setting by copying this file to :file:`/etc/telemetrics/telemetrics.conf` and changing the ``server=`` setting to your new server location.

#. Create the :file:`/etc/telemetrics` directory and make it your current working directory.

     .. code-block:: bash

        sudo mkdir -p /etc/telemetrics
        cd /etc/telemetrics


#. Copy the default :file:`telemetrics.conf` file to the new :file:`/etc/telemetrics` directory.

     .. code-block:: bash

        sudo cp /usr/share/defaults/telemetrics/telemetrics.conf

#. Edit the new :file:`/etc/telemetrics/telemetrics.conf` file with your editor using the :command:`sudo` directive and change the :guilabel:`server=` setting to ``http://localhost/v2/collector`` and save this change in the new file.

     .. code-block:: console

        server=http://localhost/v2/collector

    You can also use the fully qualified domain name for your server instead of :guilabel:`localhost`.

#. Restart the telemetry daemons to reload the configuration file.

      .. code-block:: bash

         telemctl restart

Test the new telemetry backend server
*************************************

|CL| includes a telemetry test probe called :command:`hprobe` that will send a ``hello`` record to the telemetry backend server.  To test that the telemetry records are now going to your new destination, run the :command:`hprobe` command to send a ``hello`` record to the server as follows:

   .. code-block:: bash

      hprobe

The record should show up on your new server console as shown in figure 2:

.. figure:: ../guides/telemetrics/telemetry-backend-2.png
      :scale: 50 %
      :alt: Telemetry UI

      Figure 2: :guilabel:`Telemetry UI`

You have now set up the |CL| telemetry backend server, and redirected records from your client to your server.

Creating custom telemetry events
================================
For the following steps, we'll be sending records to the backend server we've just set up. If you prefer to keep records locally and not send them to a server, follow the :ref:`telemetrics` guide and enable :record_retention_enabled: in your :file:`etc/telemetrics/telemetrics.conf` to keep the records locally.

There are two ways to create custom telemetry events: using :command:`telem-record-gen` and using the telemetry API in your applications.

Using telem-record-gen
**********************

Enabling telemetry during installation gives us everything we need to create custom telemetry events, even from C programs, because the telemetry bundle provides a simple pipe-based :abbr:`CLI (Commandline Interface)` program named :file:`telem-record-gen` that can be called trivially:


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
*********************************************

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


.. _clearlinux/telemetrics-backend: https://github.com/clearlinux/telemetrics-backend
