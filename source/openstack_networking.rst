OpenStack* Networking
############################################################

OpenStack* Networking allows you to create and attach interface devices
managed by other OpenStack services to networks. Plug-ins can be
implemented to accommodate different networking equipment and software,
providing flexibility to OpenStack architecture and deployment.

Installing and configuring the controller node
-------------------------------------------------

Prerequisites
~~~~~~~~~~~~~

Before configuring the OpenStack Networking (neutron) service, create a
database, service credentials, and an API endpoint.

#. Create the database:

   * Use the database access client to connect to the database server
     as the ``root`` user::

      	$ mysql -u root -p

   * Create the ``neutron`` database::
      
      	CREATE DATABASE neutron;

   * Grant proper access to the ``neutron`` database. Replace
     *``NEUTRON_DBPASS``* with a suitable password::

		GRANT ALL PRIVILEGES ON neutron.* TO 'neutron'@'localhost' \
		IDENTIFIED BY 'NEUTRON_DBPASS'; 
		GRANT ALL PRIVILEGES ON neutron.* TO 'neutron'@'%' \
		IDENTIFIED BY 'NEUTRON_DBPASS';

   * Exit the database access client.

#. Source the ``admin`` credentials to gain access to admin-only CLI
   commands::

   	$ source admin-openrc.sh

#. To create the service credentials, complete these steps:

   * Create the ``neutron`` user::
      
		$ openstack user create --password-prompt neutron 
		User Password: 
		Repeat User Password: 
		+----------+----------------------------------+ 
		| Field    | Value                            | 
		+----------+----------------------------------+ 
		| email    | None                             | 
		| enabled  | True                             | 
		| id       | ab67f043d9304017aaa73d692eeb4945 | 
		| name     | neutron                          | 
		| username | neutron                          | 
		+----------+----------------------------------+

   * Add the ``admin`` role to the ``neutron`` user::
      
		+-------+----------------------------------+ 
		| Field | Value                            | 
		+-------+----------------------------------+ 
		| id    | cd2cb9a39e874ea69e5d4b896eb16128 | 
		| name  | admin                            | 
		+-------+----------------------------------+

   * Create the ``neutron`` service entity::
      
		$ openstack service create --name neutron \
		--description "OpenStack Networking" network 
		+-------------+----------------------------------+ 
		| Field       | Value                            | 
		+-------------+----------------------------------+ 
		| description | OpenStack Networking             | 
		| enabled     | True                             | 
		| id          | f71529314dab4a4d8eca427e701d209e | 
		| name        | neutron                          | 
		| type        | network                          | 
		+-------------+----------------------------------+
 
#. Create the Networking service API endpoint::
   
		--publicurl http://controller:9696 \
		--adminurl http://controller:9696 \
		--internalurl http://controller:9696 \
		--region RegionOne \
		network 
		+--------------+----------------------------------+ 
		| Field        | Value                            | 
		+--------------+----------------------------------+ 
		| adminurl     | http://controller:9696           | 
		| id           | 04a7d3c1de784099aaba83a8a74100b3 | 
		| internalurl  | http://controller:9696           | 
		| publicurl    | http://controller:9696           | 
		| region       | RegionOne                        | 
		| service_id   | f71529314dab4a4d8eca427e701d209e | 
		| service_name | neutron                          | 
		| service_type | network                          | 
		+--------------+----------------------------------+

Installing the Networking components
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Complete the following step to install the Networking components:

-  Install OpenStack networking bundle::
   
   	# clr_bundle_add openstack-network

Configuring the Networking server component
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Complete the following steps to configure the Networking server component:

The Networking server component configuration includes the database,
authentication mechanism, message queue, topology change notifications,
and plug-in.

Edit the ``/etc/neutron/neutron.conf `` file:

#. Custom configurations will be located at ``/etc/neutron``.

   * Create /etc/neutron directory::
      
      	$ mkdir /etc/neutron

   * Create empty neutron configuration
     file::

      	$ touch /etc/neutron/neutron.conf

#. In the ``[database]`` section, configure database access. Replace
   *NEUTRON_DBPASS* with the password you chose for the database::

		[database] 
		... 
		connection = mysql://neutron:NEUTRON_DBPASS@controller/neutron

#. In the ``[DEFAULT]`` and ``[oslo_messaging_rabbit]`` sections,
   configure RabbitMQ message queue access. Replace *``RABBIT_PASS``*
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
   
#. In the ``[DEFAULT]`` and ``[keystone_authtoken]`` sections, configure
   Identity service access. Replace *``NEUTRON_PASS``* with the password
   you chose for the ``neutron`` user in the Identity service::

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
		username = neutron 
		password = NEUTRON_PASS
 
#. In the ``[DEFAULT]`` section, enable the Modular Layer 2 (ML2)
   plug-in, router service, and overlapping IP addresses::

	[DEFAULT] 
	... 
	core_plugin = ml2 
	service_plugins = router 
	allow_overlapping_ips = True

#. In the ``[DEFAULT]`` and ``[nova]`` sections, configure Networking to
   notify Compute of network topology changes. Replace ``NOVA_PASS``
   with the password you chose for the ``nova`` user in the Identity
   service::

		[DEFAULT] 
		... 
		notify_nova_on_port_status_changes = True 
		notify_nova_on_port_data_changes = True 
		nova_url = http://controller:8774/v2 
		[nova] 
		... 
		auth_url = http://controller:35357 
		auth_plugin = password 
		project_domain_id = default 
		user_domain_id = default 
		region_name = RegionOne 
		project_name = service 
		username = nova 
		password = NOVA_PASS

Configuring the Modular Layer 2 (ML2) plug-in
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ML2 plug-in uses the Open vSwitch (OVS) mechanism (agent) to build
the virtual networking framework for instances. However, the controller
node does not need the OVS components because it does not handle
instance network traffic.

#. Custom configuration for ML2 plug-in will be stored in ``/etc/neutron/plugins/ml2``::
   
   	mkdir -p /etc/neutron/plugins/ml2
   	touch /etc/neutron.plugins/ml2/ml2_conf.ini

#. Edit the ``/etc/neutron/plugins/ml2/ml2_conf.ini`` file as follows:

   * In the ``[ml2]`` section, enable the flat, VLAN, generic routing
     encapsulation (GRE), and virtual extensible LAN (VXLAN) network
     type drivers, GRE tenant networks, and the OVS mechanism driver::

		[ml2] 
		... 
		type_drivers = flat,vlan,gre,vxlan 
		tenant_network_types = gre 
		mechanism_drivers = openvswitch

   * In the ``[ml2_type_gre]`` section, configure the tunnel identifier
     (id) range::
      
		[ml2_type_gre] 
		... 
		tunnel_id_ranges = 1:1000

   * In the ``[securitygroup]`` section, enable security groups, enable
     ipset, and configure the OVS iptables firewall driver::

		[securitygroup] 
		... 
		enable_security_group = True 
		enable_ipset = True 
		firewall_driver = neutron.agent.linux.iptables_firewall.OVSHybridIptablesFirewallDriver

Configuring Compute to use Networking
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

By default, distribution packages configure Compute to use legacy
networking. You must reconfigure Compute to manage networks through
Networking.

#. Edit the ``/etc/nova/nova.conf`` file on the controller node as
   follows:

   * In the ``[DEFAULT]`` section, configure the APIs and drivers::
      
	[DEFAULT] 
	... 
	network_api_class = nova.network.neutronv2.api.API 
	security_group_api = neutron 
	linuxnet_interface_driver = nova.network.linux_net.LinuxOVSInterfaceDriver 
	firewall_driver = nova.virt.firewall.NoopFirewallDriver

   * In the ``[neutron]`` section, configure access
     parameters. Replace *NEUTRON_PASS* with the password you
     chose for the ``neutron`` user in the Identity service::

		[neutron] 
		... 
		url = http://controller:9696 
		auth_strategy = keystone 
		admin_auth_url = http://controller:35357/v2.0 
		admin_tenant_name = service 
		admin_username = neutron 
		admin_password = NEUTRON_PASS

Finalizing installation
~~~~~~~~~~~~~~~~~~~~~~~~

#. The Networking service initialization scripts expect a symbolic link
   ``/etc/neutron/plugin.ini`` pointing to the ML2 plug-in configuration
   file, ``/etc/neutron/plugins/ml2/ml2_conf.ini``. If this symbolic
   link does not exist, create it using the following command::

   	# ln -s /etc/neutron/plugins/ml2/ml2_conf.ini /etc/neutron/plugin.ini

#. Populate the database::
   
   	# su -s /bin/sh -c "neutron-db-manage --config-file /etc/neutron/neutron.conf \ 
   	--config-file /etc/neutron/plugins/ml2/ml2_conf.ini upgrade head" neutron

#. Let ``systemd`` set the correct permissions for files in ``/etc/neutron``::

    # systemctl restart update-triggers.target

#. Restart the Compute services::
   
	# systemctl restart nova-api.service nova-scheduler.service \ 
	nova-conductor.service

#. Start the Networking service and configure it to start when the
   system boots::

   	# systemctl enable neutron-server.service 
   	# systemctl start neutron-server.service
