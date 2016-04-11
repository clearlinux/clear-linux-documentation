.. _ssntp_frames:

SSNTP Frames
############

Each SSNTP frame is composed of a fixed-length, 8 bytes-long header and
an an optional YAML-formatted payload

+--------+--------+--------+----------+-------------------+
| Major  | Minor  | Type   | Operand  | Payload Length    |
|        |        |        |          | or Role           |
+========+========+========+==========+===================+
| 1 byte | 1 byte | 1 byte |  1 byte  | (4 bytes)         |
+--------+--------+--------+----------+-------------------+


SSNTP Header
============

The required header information detail:

* **Major** is the SSNTP version major number. It is currently 0.
* **Minor** is the SSNTP version minor number. It is currently 1.
* **Type** is the SSNTP frame type. There are 4 different frame types:
  * ``COMMAND``
  * ``STATUS``
  * ``EVENT``
  * ``ERROR``
* **Operand** is the SSNTP frame sub-type.

Supplemental header detail may include:

* **Payload Length** is the optional YAML-formatted SSNTP payload length,
  in bytes. It is set to zero for frames without the optional payload.
* **Role** is the SSNTP entity role. Only the CONNECT command and
  CONNECTED status frames are using this field as a role descriptor.



SSNTP COMMAND Frames
####################

There are 10 different SSNTP ``COMMAND`` frames:

* ``CONNECT``
* ``START``
* ``STOP``
* ``STATS``
* ``EVACUATE``
* ``DELETE``
* ``RESTART``
* ``AssignPublicIP``
* ``ReleasePublicIP``
* ``CONFIGURE``


CONNECT
=======

``CONNECT`` must be the *first* frame SSNTP clients send when trying to
connect to a SSNTP server. Any frame sent to a SSNTP server from a client
that did not initially sent a CONNECT frame will be discarded and the TLS
connection to the client will be closed.

The purpose of the ``CONNECT`` command frame is for the client to advertise
its role and for the server to verify that the advertised role matches the
client's certificate extended-key usage attributes.

The ``CONNECT`` frame is **payloadless** and its Destination UUID is the nil
UUID:

+-------+-------+-------+---------+---------------------------+-------------+----------+
| Major | Minor | Type  | Operand |          Role             | Client UUID | Nil UUID |
+=======+=======+=======+=========+===========================+=============+==========+
|       |       | (0x0) |  (0x0)  | (bitmask of client roles) |             |          |
+-------+-------+-------+---------+---------------------------+-------------+----------+


START
=====

The CIAO CSR client sends the ``START`` command to the Scheduler in order to
schedule a new workload. The `START command YAML payload`_ is mandatory and
contains a full workload description.

If the Scheduler finds a :abbr:`compute node (CN)` with enough capacity to run this
workload, it will then send a START command to the given Agent UUID managing
this CN with the same payload.

If the Scheduler cannot find a suitable CN for this workload, it will asynchronously
send an SSNTP ``ERROR`` frame back to the CSR. The error code should be ``StartFailure (0x2)``
and the payload must comply with the `StartFailure YAML schema`_ so that the CSR
eventually knows that a given instance/workload UUID could not start.

Once the Scheduler has sent the ``START`` command to an available CN Agent, it is
up to this Agent to actually initialize and start an instance that matches the
START YAML payload. If that fails, the Agent should asynchronously sends a SSNTP
ERROR back to the Scheduler and the error code should be ``StartFailure (0x2)``. The
Scheduler must then forward that error frame to the CSR.

The ``START`` command payload is mandatory:

+-------+-------+-------+---------+-----------------+----------------------+
| Major | Minor | Type  | Operand |  Payload Length | YAML-formatted       |
|       |       |       |         |                 | workload description |
+=======+=======+=======+=========+=================+======================+
|       |       | (0x0) |  (0x1)  |                 |                      |
+-------+-------+-------+---------+-----------------+----------------------+


STOP
====

The CIAO CSR client sends the ``STOP`` command to the Scheduler in order to
stop a running instance on a given CN. The `STOP command YAML payload`_ is
mandatory and contains the instance UUID to be stopped, as well as the agent
UUID that manages this instance.

To ``STOP`` an instance means you're shutting it down. Non-persistent instances
are deleted as well when you issue a STOP. Persistent instances of metadata and
disks images are stored and can be started again through the ``RESTART`` SSNTP
command.

There are several possible error cases related to the ``STOP`` command:

* If the Scheduler cannot find the Agent identified in the STOP
   command payload, it should send a SSNTP error with the
   ``StopFailure (0x3)`` error code back to the CSR.

* If the Agent cannot actually stop the instance -- such as, when it's already
  finished -- it should also send an SSNTP error with the ``StopFailure (0x3)``
  error code back to the Scheduler. It is then the Scheduler's responsibility
  to notify the CSR about it by forwarding this error frame.

+--------+--------+--------+----------+-------------------+----------------+
| Major  | Minor  |  Type  |  Operand |  Payload Length   | YAML-formatted |
|        |        |        |          |                   |     payload    |
+========+========+========+==========+===================+================+
|        |        | (0x0)  |  (0x2)   |                   |                |
+--------+--------+--------+----------+-------------------+----------------+

STATS
=====

CIAO CN Agents periodically send the ``STATS`` command to the Scheduler, in order
to provide a complete view of the compute node status. It is up to the CN Agent
implementation to define the STATS' sending period.

Upon reception of Agent STATS commands, the Scheduler must forward it to the CSR
so that it can provide a complete cloud status report back to the users.

The ``STATS`` command comes with a mandatory `YAML-formatted payload`_.

+-------+-------+-------+---------+-----------------+------------------------+
| Major | Minor | Type  | Operand |  Payload Length | YAML-formatted compute |
|       |       | (0x0) |  (0x3)  |                 | node statistics        |
+=======+=======+=======+=========+=================+========================+
|       |       | (0x0) |  (0x3)  |                 |                        |
+-------+-------+-------+---------+-----------------+------------------------+

EVACUATE
========

The CIAO CSR client sends ``EVACUATE`` commands to the Scheduler to ask a specific
CIAO Agent to evacuate its compute node; that is, to stop and migrate all of the
current workloads it is monitoring on its node.

The `EVACUATE YAML payload`_ is mandatory and describes the next state to reach
after evacuation is done. It could be ``shutdown`` for shutting the node down,
``update`` for having it run a software update, ``reboot`` for rebooting the node
or ``maintenance`` for putting the node in maintenance mode:

+-------+-------+-------+---------+-----------------+-----------------------------+
| Major | Minor | Type  | Operand |  Payload Length | YAML-formatted compute      |
|       |       |       |         |                 | node next state description |
+=======+=======+=======+=========+=================+=============================+
|       |       | (0x0) |  (0x4)  |                 |                             |
+-------+-------+-------+---------+-----------------+-----------------------------+


DELETE
======

The CIAO CSR client may send ``DELETE`` commands in order to completely remove an
already STOPped instance from the cloud. This command is only relevant for persistent
workload based instances as non persistent instances are implicitly deleted when being
STOPed.

Deleting a persistent instance means completely removing it from the cloud and thus
it should no longer be reachable like it is with, for example, a ``RESTART`` command.

When asked to delete a non existing instance the CN Agent must reply with a ``DeleteFailure``
error frame.

The `DELETE YAML payload schema`_ is the same as the STOP one.

+-------+-------+-------+---------+-----------------+----------------+
| Major | Minor | Type  | Operand |  Payload Length | YAML-formatted |
|       |       |       |         |                 |     payload    |
+=======+=======+=======+=========+=================+================+
|       |       | (0x0) |  (0x5)  |                 |                |
+-------+-------+-------+---------+-----------------+----------------+


RESTART
=======

The CIAO CSR client may send ``RESTART`` commands in order to restart previously
STOPped persistent instances. Non-persistent instances cannot be RESTARTed; they are
implicitly deleted when being STOPped.

When asked to restart a non existing instance the CN Agent must reply with a
``RestartFailure`` error frame.

The `RESTART YAML payload schema`_ is the same as the STOP one.


+-------+-------+-------+---------+-----------------+----------------+
| Major | Minor | Type  | Operand |  Payload Length | YAML-formatted |
|       |       |       |         |                 |     payload    |
+=======+=======+=======+=========+=================+================+
|       |       | (0x0) |  (0x6)  |                 |                |
+-------+-------+-------+---------+-----------------+----------------+


AssignPublicIP
==============

``AssingPublicIP`` is a command sent by the CSR to assign a publically-routable
IP to a given instance. It is sent to the Scheduler and must be forwarded to the
right CNCI.

The public IP is fetched from a pre-allocated pool managed by the CSR.

The `AssignPublicIP YAML payload schema`_ is comprised of the CNC, the tenant UUID,
the instance UUIDs, the allocated public IP, and the instance's private IP and MAC.

+-------+-------+-------+---------+-----------------+----------------+
| Major | Minor | Type  | Operand |  Payload Length | YAML-formatted |
|       |       |       |         |                 |     payload    |
+=======+=======+=======+=========+=================+================+
|       |       | (0x0) |  (0x7)  |                 |                |
+-------+-------+-------+---------+-----------------+----------------+


ReleasePublicIP
===============

``ReleasePublicIP`` is a command sent by the CSR to release a publically-routable IP
from a given instance. It is sent to the Scheduler and must be forwarded to the right CNCI.

The released public IP is added back to the CSR managed IP pool.

The `ReleasePublicIP YAML payload schema`_ is made of the CNCI and a tenant UUIDs, the released
public IP, the instance's private IP and MAC.

+-------+-------+-------+---------+-----------------+----------------+
| Major | Minor | Type  | Operand |  Payload Length | YAML-formatted |
|       |       |       |         |                 |     payload    |
+=======+=======+=======+=========+=================+================+
|       |       | (0x0) |  (0x8)  |                 |                |
+-------+-------+-------+---------+-----------------+----------------+

CONFIGURE
=========

``CONFIGURE`` commands are sent to request any SSNTP entity to configure itself according to
the ``CONFIGURE`` command payload. A CSR or any SSNTP client handling user interfaces defining
any cloud setting (image service, networking configuration, identity management...) must send
this command for any configuration change and for broadcasting the initial cloud configuration to
all CN and NN agents.

``CONFIGURE`` commands should be sent in the following cases:

* At cloud boot time, as a broadcast command.
* For every cloud configuration change.
* Everytime a new agent joins the SSNTP network.

The `CONFIGURE YAML payload`_ always includes the full cloud configuration, not only the changes
compared to the last ``CONFIGURE`` command sent.

+-------+-------+-------+---------+-----------------+-------------------------+
| Major | Minor | Type  | Operand |  Payload Length | YAML-formatted payload  |
+=======+=======+=======+=========+=================+=========================+
|       |       | (0x0) |  (0x9)  |                 |                         |
+-------+-------+-------+---------+-----------------+-------------------------+


SSNTP STATUS Frames
####################

... (wip)


.. _START command YAML payload:  https://github.com/01org/ciao/blob/master/payloads/start.go
.. _StartFailure YAML schema: https://github.com/01org/ciao/blob/master/payloads/startfailure.go
.. _STOP command YAML payload: https://github.com/01org/ciao/blob/master/payloads/stop.go
.. _YAML formatted payload: https://github.com/01org/ciao/blob/master/payloads/statistics.go
.. _EVACUATE YAML payload: https://github.com/01org/ciao/blob/master/payloads/evacuate.go
.. _DELETE YAML payload schema: https://github.com/01org/ciao/blob/master/payloads/stop.go
.. _RESTART YAML payload schema: https://github.com/01org/ciao/blob/master/payloads/start.go
.. _ AssignPublicIP YAML payload schema: https://github.com/01org/ciao/blob/master/payloads/assignpublicIP.go
.. _ReleasePublicIP YAML payload schema: https://github.com/01org/ciao/blob/master/payloads/assignpublicIP.go
.. _CONFIGURE YAML payload: https://github.com/01org/ciao/blob/master/payloads/configure.go