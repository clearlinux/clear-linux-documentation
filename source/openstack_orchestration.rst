OpenStack orchestration
############################################################

The Orchestration module provides template-based OpenStack* API calls
on a cloud application. It integrates core components of OpenStack into
a one-file template system that allows you to create most OpenStack
resource types, including: instances, floating IPs, volumes, security
groups, and users. The module also provides advanced functionality:
instance high availability, instance auto-scaling, and nested stacks,
all of which allow OpenStack core projects to accommodate a larger user
base.  

The service enables deployers to integrate with the Orchestration module
directly, or through custom plugins.

Installing and configuring controller node
-----------------------------------------------

This section describes how to install and configure the Orchestration
module, codenamed heat, on the controller node.

Configuring prerequisites
~~~~~~~~~~~~~~~~~~~~~~~~~~

Before you install and configure Orchestration, you must create a
database, service credentials, and API endpoints.

#. To create the database, complete these steps:

   #. Use the database access client to connect to the database server
      as the ``root`` user:

      .. code:: text

      	$ mysql -u root -p

   #. Create the ``heat`` database:
      
      .. code:: text

      	CREATE DATABASE heat;

   #. Grant proper access to the ``heat`` database.
      Replace *HEAT_DBPASS*  with a suitable password.

      .. code:: text

		GRANT ALL PRIVILEGES ON heat.* TO 'heat'@'localhost' \
		IDENTIFIED BY 'HEAT_DBPASS'; 
		GRANT ALL PRIVILEGES ON heat.* TO 'heat'@'%' \
		IDENTIFIED BY 'HEAT_DBPASS';
     
   #. Exit the database access client.

#. Source the ``admin`` credentials to gain access to admin-only CLI
   commands:

   .. code:: text

   	$ source admin-openrc.sh

#. To create the service credentials, complete these steps:

   #. Create the ``heat`` user:
      
      .. code:: text

		$ openstack user create --password-prompt heat 
		User Password: 
		Repeat User Password: 
		+----------+----------------------------------+ 
		| Field    | Value                            | 
		+----------+----------------------------------+ 
		| email    | None                             | 
		| enabled  | True                             | 
		| id       | 7fd67878dcd04d0393469ef825a7e005 | 
		| name     | heat                             | 
		| username | heat                             | 
		+----------+----------------------------------+
      
   #. Add the ``admin`` role to the ``heat`` user:
      
      .. code:: text

		$ openstack role add --project service --user heat admin 
		+-------+----------------------------------+ 
		| Field | Value                            | 
		+-------+----------------------------------+ 
		| id    | cd2cb9a39e874ea69e5d4b896eb16128 | 
		| name  | admin                            | 
		+-------+----------------------------------+

   #. Create the ``heat_stack_owner`` role:
      
      .. code:: text

		$ openstack role create heat_stack_owner 
		+-------+----------------------------------+ 
		| Field | Value                            | 
		+-------+----------------------------------+ 
		| id    | c0a1cbee7261446abc873392f616de87 | 
		| name  | heat_stack_owner                 | 
		+-------+----------------------------------+

   #. Add the ``heat_stack_owner`` role to the ``demo`` tenant and
      user.

      Note: You must add the ``heat_stack_owner`` role to users that
      manage stacks.

      .. code:: text

		$ openstack role add --project demo --user demo heat_stack_owner 
		+-------+----------------------------------+ 
		| Field | Value                            | 
		+-------+----------------------------------+ 
		| id    | c0a1cbee7261446abc873392f616de87 | 
		| name  | heat_stack_owner                 | 
		+-------+----------------------------------+

   #. Create the ``heat_stack_user`` role. 
      
      Note: The Orchestration service automatically assigns the ``heat_stack_user`` role to users that it creates during stack deployment. By default, this role restricts API operations. To avoid conflicts, do not add this role to users with the heat_stack_owner role.

      .. code:: text

	$ openstack role create heat_stack_user 
	+-------+----------------------------------+ 
	| Field | Value                            | 
	+-------+----------------------------------+ 
	| id    | e01546b1a81c4e32a6d14a9259e60154 | 
	| name  | heat_stack_user                  | 
	+-------+----------------------------------+

   #. Create the ``heat`` and ``heat-cfn`` service entities:
      
      .. code:: text

		+-------------+----------------------------------+ 
		| Field       | Value                            | 
		+-------------+----------------------------------+ 
		| description | Orchestration                    | 
		| enabled     | True                             | 
		| id          | 031112165cad4c2bb23e84603957de29 | 
		| name        | heat                             | 
		| type        | orchestration                    | 
		+-------------+----------------------------------+ 
		$ openstack service create --name heat-cfn \
		--description "Orchestration" cloudformation 
		+-------------+----------------------------------+ 
		| Field       | Value                            | 
		+-------------+----------------------------------+ 
		| description | Orchestration                    | 
		| enabled     | True                             | 
		| id          | 297740d74c0a446bbff867acdccb33fa | 
		| name        | heat-cfn                         | 
		| type        | cloudformation                   | 
		+-------------+----------------------------------+

#. Create the Orchestration service API endpoints:
   
   .. code:: text

		$ openstack endpoint create \
		--publicurl http://controller:8004/v1/%\(tenant_id\)s \
		--internalurl http://controller:8004/v1/%\(tenant_id\)s \
		--adminurl http://controller:8004/v1/%\(tenant_id\)s \
		--region RegionOne \
		orchestration 
		+--------------+-----------------------------------------+ 
		| Field        | Value                                   | 
		+--------------+-----------------------------------------+ 
		| adminurl     | http://controller:8004/v1/%(tenant_id)s | 
		| id           | f41225f665694b95a46448e8676b0dc2        | 
		| internalurl  | http://controller:8004/v1/%(tenant_id)s | 
		| publicurl    | http://controller:8004/v1/%(tenant_id)s | 
		| region       | RegionOne                               | 
		| service_id   | 031112165cad4c2bb23e84603957de29        | 
		| service_name | heat                                    | 
		| service_type | orchestration                           | 
		+--------------+-----------------------------------------+ 
		$ openstack endpoint create \
		--publicurl http://controller:8000/v1 \
		--internalurl http://controller:8000/v1 \
		--adminurl http://controller:8000/v1 \
		--region RegionOne \
		cloudformation 
		+--------------+----------------------------------+ 
		| Field        | Value                            | 
		+--------------+----------------------------------+ 
		| adminurl     | http://controller:8000/v1        | 
		| id           | f41225f665694b95a46448e8676b0dc2 | 
		| internalurl  | http://controller:8000/v1        | 
		| publicurl    | http://controller:8000/v1        | 
		| region       | RegionOne                        | 
		| service_id   | 297740d74c0a446bbff867acdccb33fa | 
		| service_name | heat-cfn                         | 
		| service_type | cloudformation                   | 
		+--------------+----------------------------------+

Installing and configuring the Orchestration components
----------------------------------------------------------

To install and configure the Orchestration components:

#. Install OpenStack Orchestration bundle:
   
   .. code:: text

   	# clr_bundle_add openstack-orchestration

#. Create the ``/etc/heat/heat.conf file``.
   
   .. code:: text

   	# mkdir /etc/heat # touch /etc/heat/heat.conf

#. Edit the ``/etc/heat/heat.conf`` file and complete the following
   actions:

   #. In the ``[database]`` section, configure database access.
      Replace *HEAT_DBPASS*  with the password you chose for the
      Orchestration database.

      .. code:: text

      	[database] 
      	... 
      	connection = mysql://heat:HEAT_DBPASS@controller/heat

   #. In the ``[DEFAULT]`` and ``[oslo_messaging_rabbit]`` sections,
      configure RabbitMQ message queue access.
      Replace *``RABBIT_PASS``*  with the password you chose for
      the ``openstack`` account in RabbitMQ.

      .. code:: text

		[DEFAULT] 
		... 
		rpc_backend = rabbit 
		[oslo_messaging_rabbit] 
		... 
		rabbit_host = controller 
		rabbit_userid = openstack 
		rabbit_password = RABBIT_PASS

   #. In the ``[keystone_authtoken]`` and ``[ec2authtoken]`` sections,
      configure Identity service access. Replace *HEAT_PASS*  with
      the password you chose for the ``heat`` user in the Identity
      service.

      .. code:: text

		[keystone_authtoken] 
		... 
		auth_uri = http://controller:5000/v2.0 
		identity_uri = http://controller:35357 
		admin_tenant_name = service 
		admin_user = heat 
		admin_password = HEAT_PASS 
		[ec2authtoken] 
		... 
		auth_uri = http://controller:5000/v2.0

   #. In the ``[DEFAULT]`` section, configure the metadata and wait
      condition URLs:

      .. code:: text

		[DEFAULT] 
		... 
		heat_metadata_server_url = http://controller:8000 
		heat_waitcondition_server_url = http://controller:8000/v1/waitcondition

   #. In the ``[DEFAULT]`` section, configure information about the
      heat Identity service domain. Replace  *``HEAT_DOMAIN_PASS``*
       with the password you chose for the admin user of
      the ``heat`` user domain in the Identity service.

      .. code:: text

		[DEFAULT] 
		... 
		stack_domain_admin = heat_domain_admin 
		stack_domain_admin_password = HEAT_DOMAIN_PASS 
		stack_user_domain_name = heat_user_domain

#. Source the ``admin`` credentials to gain access to admin-only CLI
   commands:

   .. code:: text

   	$ source admin-openrc.sh

#. Create the heat domain in Identity service.
   Replace *``HEAT_DOMAIN_PASS``*  with a suitable
   password.

   .. code:: text

	$ heat-keystone-setup-domain \
	--stack-user-domain-name heat_user_domain \
	--stack-domain-admin heat_domain_admin \
	--stack-domain-admin-password HEAT_DOMAIN_PASS

#. Let systemd set the correct permissions for files in ``/etc/heat``.

   .. code:: text

   	# systemctl restart update-triggers.target

#. Populate the Orchestration database:
   
   .. code:: text

   	# su -s /bin/sh -c "heat-manage db_sync" heat``

Finalizing installation
~~~~~~~~~~~~~~~~~~~~~~~~

Complete this step to finalize the installation:

-  Start the Orchestration services and configure them to start when the
   system boots:

   .. code:: text

   	# systemctl enable heat-api.service heat-api-cfn.service heat-engine.service 
   	# systemctl start heat-api.service heat-api-cfn.service heat-engine.service``
