.. _openstack_telemetry:

OpenStack* Telemetry
############################################################

Overview
---------

The Telemetry service performs the following functions:

-  Efficiently polls metering data related to OpenStack services;
-  Collects event and metering data by monitoring notifications sent
   from services;
-  Publishes collected data to various targets, including data stores
   and message queues;
-  Creates alarms when collected data breaks defined rules.

Installing and configure
------------------------

This section describes how to install and configure the Telemetry
service, code-named ceilometer, on the controller node. The Telemetry
service collects measurements from most OpenStack services and optionally
triggers alarms.


Prerequisites
~~~~~~~~~~~~~~~

Before installing and configuring the ``telemetry`` service, install
MongoDB* and create a MongoDB database, service credentials, and API
endpoint.

#. Install the MongoDB bundle::

   	# swupd bundle-add database-mongodb
   	# swupd verify --fix

#. Create the ``/etc/mongodb/`` folder and the
   ``/etc/mongodb/openstack.cnf`` file.::

    # mkdir /etc/mongodb
    # touch /etc/mongodb/openstack.cnf

#. Configure the ``bind_ip`` key to use the management interface IP
   address of the controller node by editing the ``/etc/mongodb/openstack.cnf`` file::

   	bind_ip = 10.0.0.11

#. Start the database service and configure it to start when the system
   boots with the following commands::

   	# systemctl enable mongodb.service
   	# systemctl start mongodb.service

#. Create the ``ceilometer`` database. Replace *CEILOMETER_DBPASS*
   with a suitable password::

    # mongo --host controller --eval '
    db = db.getSiblingDB("ceilometer");
    db.createUser({user: "ceilometer",
    pwd: "CEILOMETER_DBPASS",
    roles: [ "readWrite", "dbAdmin" ]})'

    MongoDB shell version: 3.1.7
    connecting to: controller:27017/test
    Successfully added user: { "user" : "ceilometer", "roles" : [ "readWrite", "dbAdmin" ] }

#. Source the ``admin`` credentials to gain access to admin-only CLI
   commands::

   	$ source admin-openrc.sh

#. To create the service credentials, complete these steps:

   * Create the ``ceilometer`` user::

      $ openstack user create --domain default --password-prompt ceilometer
      User Password:
      Repeat User Password:
      +-----------+----------------------------------+
      | Field     | Value                            |
      +-----------+----------------------------------+
      | domain_id | default                          |
      | enabled   | True                             |
      | id        | c859c96f57bd4989a8ea1a0b1d8ff7cd |
      | name      | ceilometer                       |
      +-----------+----------------------------------+

   * Add the ``admin`` role to the ``ceilometer`` user::

		$ openstack role add --project service --user ceilometer admin

   * Create the ``ceilometer`` service entity::

		$ openstack service create --name ceilometer \
		--description "Telemetry" metering
		+-------------+----------------------------------+
		| Field       | Value                            |
		+-------------+----------------------------------+
		| description | Telemetry                        |
		| enabled     | True                             |
		| id          | 3405453b14da441ebb258edfeba96d83 |
		| name        | ceilometer                       |
		| type        | metering                         |
		+-------------+----------------------------------+

#. Create the Telemetry service API endpoints::

    $ openstack endpoint create --region RegionOne \
      metering public http://controller:8777
      +--------------+----------------------------------+
      | Field        | Value                            |
      +--------------+----------------------------------+
      | enabled      | True                             |
      | id           | 340be3625e9b4239a6415d034e98aace |
      | interface    | public                           |
      | region       | RegionOne                        |
      | region_id    | RegionOne                        |
      | service_id   | 8c2c7f1b9b5049ea9e63757b5533e6d2 |
      | service_name | celiometer                       |
      | service_type | metering                         |
      | url          | http://controller:8777           |
      +--------------+----------------------------------+

    $ openstack endpoint create --region RegionOne \
      metering internal http://controller:8777
      +--------------+----------------------------------+
      | Field        | Value                            |
      +--------------+----------------------------------+
      | enabled      | True                             |
      | id           | 340be3625e9b4239a6415d034e98aace |
      | interface    | internal                         |
      | region       | RegionOne                        |
      | region_id    | RegionOne                        |
      | service_id   | 8c2c7f1b9b5049ea9e63757b5533e6d2 |
      | service_name | celiometer                       |
      | service_type | metering                         |
      | url          | http://controller:8777           |
      +--------------+----------------------------------+

    $ openstack endpoint create --region RegionOne \
      metering admin http://controller:8777
      +--------------+----------------------------------+
      | Field        | Value                            |
      +--------------+----------------------------------+
      | enabled      | True                             |
      | id           | 340be3625e9b4239a6415d034e98aace |
      | interface    | admin                            |
      | region       | RegionOne                        |
      | region_id    | RegionOne                        |
      | service_id   | 8c2c7f1b9b5049ea9e63757b5533e6d2 |
      | service_name | celiometer                       |
      | service_type | metering                         |
      | url          | http://controller:8777           |
      +--------------+----------------------------------+


Install and configure components
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Install the OpenStack Telemetry Controller bundle::

   	# swupd bundle-add openstack-telemetry-controller

#. Custom configurations will be located at ``/etc/ceilometer``.

   * Create ``/etc/ceilometer`` directory::

      	# mkdir /etc/ceilometer

   * Create the empty ceilometer configuration file::

       	# touch /etc/ceilometer/ceilometer.conf

#. Edit the ``/etc/ceilometer/ceilometer.conf`` file and
   complete the following actions:

   * In the ``[database]`` section, configure database access. Replace
     *CEILOMETER_DBPASS* with the password you chose for the
     Telemetry module database. You must escape special characters such
     as ':', '/', '+', and '@' in the connection string in accordance
     with RFC2396::

      	[database]
      	...
      	connection = mongodb://ceilometer:CEILOMETER_DBPASS@controller:27017/ceilometer

   * In the ``[DEFAULT]`` and ``[oslo_messaging_rabbit]`` sections,
     configure RabbitMQ message queue access. Replace *RABBIT_PASS*
     with the password you chose for the ``openstack`` account in
     RabbitMQ::

		[DEFAULT]
		...
		rpc_backend = rabbit

		[oslo_messaging_rabbit]
		...
		rabbit_host = controller
		rabbit_userid = openstack
		rabbit_password = RABBIT_PASS

   * In the ``[DEFAULT]`` and ``[keystone_authtoken]`` sections,
     configure Identity service access. Replace *CEILOMETER_PASS*
     with the password you chose for the ``celiometer`` user in the
     Identity service::

      [DEFAULT]
      ...
      auth_strategy = keystone

      [keystone_authtoken]
      ...
      auth_uri = http://controller:5000
      auth_url = http://controller:35357
      auth_plugin = password
      project_domain_id = default
      user_domain_id = default
      project_name = service
      username = ceilometer
      password = CEILOMETER_PASS

   * In the ``[service_credentials]`` section, configure service
     credentials. Replace *CEILOMETER_PASS* with the password you
     chose for the ``ceilometer`` user in the Identity service::

		[service_credentials]
		...
		os_auth_url = http://controller:5000/v2.0
		os_username = ceilometer
		os_tenant_name = service
		os_password = CEILOMETER_PASS
		os_endpoint_type = internalURL
		os_region_name = RegionOne

   * Ensure files have proper ownership by running the following command::

        # systemctl restart update-triggers.target


Finalizing installation
~~~~~~~~~~~~~~~~~~~~~~~~

#. Start the Telemetry services and configure them to start when the system boots::

    # systemctl enable ceilometer-agent-central.service \
                       ceilometer-agent-notification.service \
                       ceilometer-api.service \
                       ceilometer-collector.service \
                       ceilometer-alarm-evaluator.service \
                       ceilometer-alarm-notifier.service

    # systemctl start ceilometer-agent-central.service \
                      ceilometer-agent-notification.service \
                      ceilometer-api.service \
                      ceilometer-collector.service \
                      ceilometer-alarm-evaluator.service \
                      ceilometer-alarm-notifier.service
