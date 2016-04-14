.. _launcher:

Launcher
########

Launcher is an SSNTP client that manages VM instances. It runs on a
compute node and listens to commands from SSNTP servers. Its current
feature set includes:

#. The commands ``START``, ``DELETE``, ``RESTART``, ``STOP``.
#. Basic monitoring of VMs.
#. Collection and transmission of statistics about compute node.
#. Reconnect to existing VMs on startup.

We'll take a look features in more detail a little later on.  First, let's see
what is required to install and run launcher.

Installation
============

Getting the Code
----------------

Launcher can be downloaded and installed using go get::

  $ go get [[INSERT non-internal URL]]

The resulting binary will be placed in ``$GOPATH/bin``, which you should
already have in your ``$PATH``.

Setting up Directories
----------------------

Launcher requires write access to the following directory::

  /var/lib/ciao

So to get started, pre-create this directory and assign the correct
permissions and ownership::

  $ sudo mkdir /var/lib/ciao
  $ sudo chown $USER:$USER /var/lib/ciao


Installing Certificates
-----------------------

Secondly, generate a certificate pair to allow launcher to connect to
the SSNTP server.  The default location for these certificates is::

  /etc/pki/ciao/{ssntp_certs}

So you can either copy the certs to this location::

  $ sudo mkdir -p /etc/pki/ciao
  $ cp CAcert-server-localhost.pem /etc/pki/ciao/{ssntp_certs}
  $ cp cert-client-localhost.pem /etc/pki/ciao/{ssntp_certs}

or provide alternative locations for these files via the ``-cert`` and
``-cacert`` command-line options.


Install Dependencies
--------------------

Launcher has external packages dependencies:

#. On ``qemu-system-x86_64`` to launch the VMs.
#. On ``qemu-img`` to manipulate disk images.
#. On ``xorriso`` to create ISO images for cloudinit.
#. On ``ovmf``, which contains EFI firmware required for some images.
#. On ``fuser``, for process statistics (part of most distros' psmisc package).
#. On ``docker``, to manage docker containers.

All of these packages need to be installed on your :abbr:`compute node (CN)`
before launcher can be run.

An optimized OVMF is available from ClearLinux.  Download the `OVMF.fd`_
file and save it to /usr/share/qemu/OVMF.fd on each compute node.

To create a new instance, launcher needs a template ``.iso`` image to use
as a backing file. Currently, launcher requires all such backing files to
be stored in ``/var/lib/ciao/images``  The names of these image files must
exactly match the ``image_uuid`` field passed in the payload of the ``START`` command.  Here's an example setup::

  /var/lib/ciao/images/
   └── b286cd45-7d0c-4525-a140-4db6c95e41fa

The images should have ``cloudinit`` installed and configured to use
the ``ConfigDrive`` datasource. This is the only datasource
supported by launcher at the present time.

Launching Launcher
------------------

Launcher can be launched from the command line as follows::

  $ launcher -server <URL of my server> -network [cn|nn|none]

As previously mentioned, the :option:`-cacert` and :option:`-cert` options
can be used to override the SSNTP certificates.  You can also specify
the ``--with-ui`` parameter, which forces launcher to launch VMs in the foreground, and can be useful for debugging.  The :option:`-max-vm` option allows the user to specify the maximum number of VM instances that a given launcher
instance is prepared to manage. This is a soft, rather than a hard limit,
and will be discussed in the reporting section below.

Launcher uses `glog`_ for logging. By default, launcher stores logs
in files written to :file:`/var/lib/ciao/logs`. This behavior can be
overridden with a number of different command-line arguments (
``-alsologtostderr``, for example) added by `glog`_.

Here is a full list of the command-line parameters supported by launcher::

  Usage of launcher:
    -alsologtostderr
      	log to standard error as well as files
    -cacert string
      	Client certificate (default /etc/pki/ciao/CAcert-server-localhost.pem)
    -cert string
      	CA certificate (default /etc/pki/ciao/cert-client-localhost.pem)
    -compute-net string
      	Compute Subnet
    -log_backtrace_at value
      	when logging hits line file:N, emit a stack trace (default :0)
    -log_dir string
      	If non-empty, write log files in this directory
    -logtostderr
      	log to standard error instead of files
    -max-vm int
      	Maximum number of permitted instances (default 32)
    -mgmt-net string
      	Management Subnet
    -network value
      	Can be "none", "cn" (compute node), or "nn" (network node);
        the default is "none"
    -server string
      	URL of SSNTP server (default "localhost")
    -stderrthreshold value
      	logs at or above this threshold go to stderr
    -v value
      	log level for V logs
    -vmodule value
      	comma-separated list of pattern=N settings for file-filtered logging
    -with-ui
      	Indicates whether VMs should be launched in a window


Commands
========

START
-----

`START` is used to create and launch a new VM instance. Three example
`START` payloads are shown below.

This first payload example will create a new CN VM instance using the backing file
stored in ``/var/lib/ciao/images/b286cd45-7d0c-4525-a140-4db6c95e41fa``.
The disk image has a maximum size of 80GBs, and the VM will be run with two
CPUS and 256MBs of memory. The first part of the payload corresponds to the
``cloudinit`` user-data file. This data will be extracted from the payload
stored in an ISO image and passed to the VM instance. Assuming ``cloudinit``
is correctly configured on the backing image, the file :file:`/etc/bootdone`
will be created, and the hostname of the image will be set to the instance uuid::

  #cloud-config
    runcmd:
      - [ touch, "/etc/bootdone" ]
    start:
      requested_resources:
         - type: vcpus
           value: 2
         - type: mem_mb
           value: 256
         - type: disk_mb
           value: 80000
      instance_uuid: 67d86208-b46c-4465-9018-fe14087d415f
      tenant_uuid: 67d86208-000-4465-9018-fe14087d415f
      image_uuid: b286cd45-7d0c-4525-a140-4db6c95e41fa
      fw_type: legacy
      networking:
        vnic_mac: 02:00:e6:f5:af:f9
        vnic_uuid: 67d86208-b46c-0000-9018-fe14087d415f
        concentrator_ip: 192.168.42.21
        concentrator_uuid: 67d86208-b46c-4465-0000-fe14087d415f
        subnet: 192.168.8.0/21
        private_ip: 192.168.8.2

The following payload creates a CN VM instance using a different image that needs to be booted with EFI::

  #cloud-config
    runcmd:
      - [ touch, "/etc/bootdone" ]
    start:
      requested_resources:
         - type: vcpus
           value: 2
         - type: mem_mb
           value: 256
         - type: disk_mb
           value: 80000
      instance_uuid: 67d86208-b46c-4465-9018-fe14087d415
      tenant_uuid: 67d86208-000-4465-9018-fe14087d415f
      image_uuid: clear-1ff6bf3883708a56446d863f20c810c99b3aea6f
      networking:
        vnic_mac: 02:00:fa:69:71:d0
        vnic_uuid: 00d86208-b46c-0000-9018-fe14087d415f
        concentrator_ip: 192.168.42.21
        concentrator_uuid: 67d86208-b46c-4465-0000-fe14087d415f
        subnet: 192.168.8.0/21
        private_ip: 192.168.8.3


Lastly, here's an example payload to start a VM instance on a NN.  Note that
the networking parameters are different::

  #cloud-config
    runcmd:
      - [ touch, "/etc/bootdone" ]
    start:
      requested_resources:
         - type: vcpus
           value: 2
         - type: mem_mb
           value: 256
         - type: disk_mb
           value: 80000
         - type: network_node
           value: 1
    instance_uuid: 67d86208-b46c-4465-0000-fe14087d415f
    tenant_uuid: 67d86208-0000-0000-9018-fe14087d415f
    image_uuid: b286cd45-7d0c-4525-a140-4db6c95e41fa
    fw_type: legacy
    networking:
      vnic_mac: 02:00:e6:f5:af:f9
      vnic_uuid: 67d86208-b46c-0000-0000-fe14087d415f

Launcher detects and returns a number of errors when executing the start command.
These are listed below:

* ``invalid_payload`` if the YAML is corrupt

* ``invalid_data`` if the start section of the payload is corrupt or
  missing information, such as ``image-id``

* ``already_running`` if you try to start an existing instance that is already
  running

* ``instance_exists`` if you try to start an instance that has already been created but is not currently running

* ``image_failure`` if launcher is unable to prepare the file for the instance;
  this happens, for example, if the ``image_uuid`` tries to refer to an non-existant backing image

* ``network_failure`` if it was impossible to initialize networking for
  the instance

* ``launch_failure`` if the instance was successfully created but,
  could not be launched. This is sort of an odd situation as the ``START``
  command partially succeeded. Launcher returns an error code, but the instance has been created and could be booted a later stage via ``RESTART``.

If the user specifies a size for ``disk_mb`` that is smaller than the
virtual size of the backing image, launcher ignores the user-specified
value and creates an image for the instance whose virtual size matches
that size of the chosen backing image.

The launcher doesn't currently report the error ``full_cn``; it supports
only *persistent* instances at the moment. Any VM instances created
by the ``START`` command are persistent; the persistence YAML field is currently
ignored.


DELETE
------

``DELETE`` can be used to destroy an existing VM instance. It removes all the
files associated with that instance from the compute node. If the VM instance
is running when the ``DELETE`` command is received, it will be powered down.
An example of the  ``DELETE`` command is as follows::

 delete:
   instance_uuid: 67d86208-b46c-4465-9018-fe14087d415f


STOP
----

``STOP`` can be used to power-down an existing VM instance. The state
associated with the VM remains intact on the compute node, and the instance
can be restarted at a later date via the ``RESTART`` command

An example of the ``STOP`` command is as follows::

 stop:
   instance_uuid: 67d86208-b46c-4465-9018-fe14087d415f


RESTART
-------

``RESTART`` can be used to power-up an existing VM instance that has
either been powered down by the user explicitly or shut down via the
``STOP`` command.  The instance will be restarted with the settings
contained in the payload of the ``START`` command that originally created
it. It is not possible to override these settings (that is, to change the
number of CPUs used) with the ``RESTART`` command; they remain persistent
from the initial settings.

An example of the RESTART command is as follows::

 restart:
   instance_uuid: 67d86208-b46c-4465-9018-fe14087d415f


Recovery
========

When launcher starts up, it checks to see if any VM instances exist; and
if they do, it tries to connect to them. This means that you can easily
kill launcher, restart it, and continue to use it to manage any of the
previously-created VMs.  One thing that it does not yet do is to restart VM instances that have been powered down. This might be a feature in a
later release of CIAO launcher.


Reporting
=========

Launcher sends ``STATS`` commands and STATUS updates to the SSNTP
server to which it is connected. STATUS updates are sent when launcher
connects to the SSNTP server. They are also sent when a VM instance
is successfully created or destroyed, informing the upper levels of the
stack that the capacity of launcher's compute node has changed. The STATS
command is sent when launcher connects to the SSNTP server and every 30
seconds thereafter.

Launcher computes the information that it sends back in the STATS command
and STATUS update payloads as follows:

+-----------------+--------------------------------------------------------+
| Datum           | Source                                                 |
+=================+========================================================+
| MemTotalMB      | /proc/meminfo:MemTotal                                 |
+-----------------+--------------------------------------------------------+
| MemAvailableMB  | /proc/meminfo:MemFree + Active(file) + Inactive(file)  |
+-----------------+--------------------------------------------------------+
| DiskTotalMB     | "/var/lib/ciao/instances"                              |
+-----------------+--------------------------------------------------------+
| DiskAvailableMB | statfs("/var/lib/ciao/instances")                 |
+-----------------+--------------------------------------------------------+
| Load            | /proc/loadavg (Average over last minute reported)      |
+-----------------+--------------------------------------------------------+
| CpusOnLine      | Number of cpu[0-9]+ entries in /proc/stat              |
+-----------------+--------------------------------------------------------+

Launcher sends two different STATUS updates: ``READY`` and ``FULL``.

* ``FULL`` is sent when the number of VM instances monitored by launcher
  *equals* or *exceeds* the maximum number of VM instances as specified by the :option:`-max-vm` command line option.
* If the number of VM instances is less than maximum number of supported VMs,
  launcher sends ``READY``.

The running status of the VMs does not have any effect on the STATUS update. For example, if the maximum number of VM instances was defined to be 32, and 32 VMs had been started on the compute node, launcher would send a ``FULL`` status update, even if none of those instances were actually running.

This is a rather trivial implementation of ``READY`` and ``FULL`` implemented
quickly to allow us to test the scheduler.  More complete capacity management
code will be implemented once the criteria have been identified.

Finally, launcher does **not** currently reject ``START`` requests when
the number of VMs it manages has reached the limit defined by :option:`-max-vm`.
Again, the behavior of launcher in this situation needs to be agreed.


.. _glog: https://google-glog.googlecode.com/svn/trunk/doc/glog.html
.. _OVMF.fd: https://download.clearlinux.org/image/OVMF.fd
