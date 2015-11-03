OpenStack* Telemetry
############################################################

Overview
---------

The Telemetry module performs the following functions:

-  Efficiently polls metering data related to OpenStack services;
-  Collects event and metering data by monitoring notifications sent
   from services;
-  Publishes collected data to various targets, including data stores
   and message queues; and
-  Creates alarms when collected data breaks defined rules.

Installing and configuring controller node
-----------------------------------------------

This section describes how to install and configure the Telemetry
module, code-named ceilometer, on the controller node. The Telemetry
module uses separate agents to collect measurements from each OpenStack
service in your environment.

Prerequisites
~~~~~~~~~~~~~~~

Before installing and configuring the ``telemetry`` module, install
MongoDB* and create a MongoDB database, service credentials, and API
endpoint.

#. Install the MongoDB bundle::
   
   	# clr_bundle_add database-mongodb

#. Create the ``/etc/mongodb/`` folder and the
   ``/etc/mongodb/openstack.cnf`` file.
#. Configure the ``bind_ip`` key to use the management interface IP
   address of the controller node::

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

	MongoDB shell version: 2.6.x 
	connecting to: controller:27017/test 
	Successfully added user: { "user" : "ceilometer", "roles" : [ "readWrite", "dbAdmin" ] }

#. Source the ``admin`` credentials to gain access to admin-only CLI
   commands::

   	$ source admin-openrc.sh

#. To create the service credentials, complete these steps:

   * Create the ``ceilometer`` user::
      
		$ openstack user create --password-prompt ceilometer 
		User Password: 
		Repeat User Password: 
		+----------+----------------------------------+ 
		| Field    | Value                            | 
		+----------+----------------------------------+ 
		| email    | None                             | 
		| enabled  | True                             | 
		| id       | b7657c9ea07a4556aef5d34cf70713a3 | 
		| name     | ceilometer                       | 
		| username | ceilometer                       | 
		+----------+----------------------------------+

   * Add the ``admin`` role to the ``ceilometer`` user::
      
		$ openstack role add --project service --user ceilometer admin 
		+-------+----------------------------------+ 
		| Field | Value                            | 
		+-------+----------------------------------+ 
		| id    | cd2cb9a39e874ea69e5d4b896eb16128 | 
		| name  | admin                            | 
		+-------+----------------------------------+

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

#. Create the Telemetry module API endpoint::
   
	$ openstack endpoint create \
	  --publicurl http://controller:8777 \
	  --internalurl http://controller:8777 \
	  --adminurl http://controller:8777 \
	  --region RegionOne \
	  metering 
	+--------------+----------------------------------+ 
	| Field        | Value                            | 
	+--------------+----------------------------------+ 
	| adminurl     | http://controller:8777           | 
	| id           | d3716d85b10d4e60a67a52c6af0068cd | 
	| internalurl  | http://controller:8777           | 
	| publicurl    | http://controller:8777           | 
	| region       | RegionOne                        | 
	| service_id   | 3405453b14da441ebb258edfeba96d83 | 
	| service_name | ceilometer                       | 
	| service_type | metering                         | 
	+--------------+----------------------------------+

Installing and configuring the Telemetry module components
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Install the OpenStack Telemetry Controller bundle::
   
   	# clr_bundle_add openstack-telemetry-controller

#. Generate a random value to use as the telemetry secret::
   
   	$ openssl rand -hex 10

#. Custom configurations will be located at ``/etc/ceilometer``.

   * Create ``/etc/ceilometer`` directory::
      
      	mkdir /etc/ceilometer

   * Create the empty ceilometer configuration file::
      
      	/etc/ceilometer/ceilometer.conf
       	touch /etc/ceilometer/ceilometer.conf

#. Edit the following file:\ ``/etc/ceilometer/ceilometer.conf``\ Then
   complete the following actions:

   * In the ``[database]`` section, configure database access. Replace
     *``CEILOMETER_DBPASS``* with the password you chose for the
     Telemetry module database. You must escape special characters such
     as ':', '/', '+', and '@' in the connection string in accordance
     with RFC2396::

      	[database] 
      	... 
      	connection = mongodb://ceilometer:CEILOMETER_DBPASS@controller:27017/ceilometer

   * In the ``[DEFAULT]`` and ``[oslo_messaging_rabbit]`` sections,
     configure RabbitMQ message queue access. Replace *``RABBIT_PASS``*
     with the password you chose for the ``openstack`` account in
     RabbitMQ::

		[DEFAULT] 
		... 
		rpc_backend = rabbit 
		[oslo_messaging_rabbit] 
		rabbit_host = controller 
		rabbit_userid = openstack 
		rabbit_password = RABBIT_PASS

   * In the ``[DEFAULT]`` and ``[keystone_authtoken]`` sections,
     configure Identity service access. Replace *``CEILOMETER_PASS``*
     with the password you chose for the ``celiometer`` user in the
     Identity service::

		[DEFAULT] 
		... 
		auth_strategy = keystone 
		[keystone_authtoken] 
		auth_uri = http://controller:5000/v2.0 
		identity_uri = http://controller:35357 
		admin_tenant_name = service 
		admin_user = ceilometer 
		admin_password = CEILOMETER_PASS

   * In the ``[service_credentials]`` section, configure service
     credentials. Replace *``CEILOMETER_PASS``* with the password you
     chose for the ``ceilometer`` user in the Identity service::

		[service_credentials] 
		... 
		os_auth_url = http://controller:5000/v2.0 
		os_username = ceilometer 
		os_tenant_name = service 
		os_password = CEILOMETER_PASS 
		os_endpoint_type = internalURL 
		os_region_name = RegionOne

   * In the ``[publisher]`` section, configure the telemetry secret.
     Replace *``TELEMETRY_SECRET``* with the telemetry secret that you
     generated in a previous step::

		[publisher] 
		... 
		telemetry_secret = TELEMETRY_SECRET

Finalizing installation
~~~~~~~~~~~~~~~~~~~~~~~~

* Start the Telemetry services and configure them to start when the system boots::
  
	# systemctl enable ceilometer-api.service ceilometer-agent-notification.service ceilometer-agent-central.service ceilometer-collector.service \
	ceilometer-alarm-evaluator.service ceilometer-alarm-notifier.service 
	# systemctl start ceilometer-api.service ceilometer-agent-notification.service ceilometer-agent-central.service ceilometer-collector.service \
	ceilometer-alarm-evaluator.service ceilometer-alarm-notifier.service

