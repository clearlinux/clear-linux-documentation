.. _openstack_sys_req_and_pw_summary:

System requirements and password summary
############################################################

System requirements
----------------------------

For best performance, we recommend that your environment meets or
exceeds the following hardware requirements:

-  Controller Node: 1 processor, 2 GB memory, and 5 GB storage.
-  Compute Node: 1 processor, 2 GB memory, and 10 GB storage.

For OpenStack* services, this guide uses \ ``SERVICE_PASS``\ to reference
service account passwords and ``SERVICE_DBPASS`` to reference database
passwords.

Prerequisites
---------------------

All nodes require Internet access to install OpenStack bundles and
perform maintenance tasks such as periodic updates.

OpenStack and supporting services require administrative privileges
during installation and operation.

You must also configure networking so that each node can resolve the
other nodes by name in addition to IP address. For example, the
``controller`` name must resolve to ``10.0.0.11``, the IP address of the
management interface on the controller node.

To configure name resolution:

#. Set the hostname of the node to ``controller``::

       # hostnamectl set-hostname controller

#. Edit the ``/etc/hosts`` file to contain the following::

       # controller 10.0.0.11 controller
       # compute1 10.0.0.31 compute1

Password summary
------------------------

The following table provides a list of services that require passwords
and their associated references in the guide:

+----------------------------------------+--------------------------------------------------+
| **Password name**                      | **Description**                                  |
+----------------------------------------+--------------------------------------------------+
| Database password (no variable used)   | Root password for the database                   |
+----------------------------------------+--------------------------------------------------+
| RABBIT_PASS                            | Password of user guest of RabbitMQ               |
+----------------------------------------+--------------------------------------------------+
| KEYSTONE_DBPASS                        | Database password of Identity service            |
+----------------------------------------+--------------------------------------------------+
| DEMO_PASS                              | Password of user demo                            |
+----------------------------------------+--------------------------------------------------+
| ADMIN_PASS                             | Password of user admin                           |
+----------------------------------------+--------------------------------------------------+
| GLANCE_DBPASS                          | Database password for Image Service              |
+----------------------------------------+--------------------------------------------------+
| GLANCE_PASS                            | Password of Image Service user glance            |
+----------------------------------------+--------------------------------------------------+
| NOVA_DBPASS                            | Database password for Compute service            |
+----------------------------------------+--------------------------------------------------+
| NOVA_PASS                              | Password of Compute service user nova            |
+----------------------------------------+--------------------------------------------------+
| DASH_DBPASS                            | Database password for the dashboard              |
+----------------------------------------+--------------------------------------------------+
| CINDER_DBPASS                          | Database password for the Block Storage service  |
+----------------------------------------+--------------------------------------------------+
| CINDER_PASS                            | Password of Block Storage service user cinder    |
+----------------------------------------+--------------------------------------------------+
