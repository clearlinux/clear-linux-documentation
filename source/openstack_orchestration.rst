OpenStack* Orchestration
############################################################

The Orchestration service provides a template-based orchestration for
describing a cloud application by running OpenStack* API calls to generate
running cloud applications. The software integrates other core components of
OpenStack* into a one-file template system.
The templates allow you to create most OpenStack* resource types, such as
instances, floating IPs, volumes, security groups and users. It also provides
advanced functionality, such as instance high availability, instance
auto-scaling, and nested stacks. This enables OpenStack* core projects to
receive a larger user base.

Installing and configuring controller node
------------------------------------------

This section describes how to install and configure the Orchestration
service, codenamed heat, on the controller node.

Configuring prerequisites
~~~~~~~~~~~~~~~~~~~~~~~~~

Before you install and configure Orchestration, you must create a
database, service credentials, and API endpoints.

#. To create the database, complete these steps:

   * Use the database access client to connect to the database server as
     the ``root`` user::

      $ mysql -u root -p

   * Create the ``heat`` database::

      CREATE DATABASE heat;

   * Grant proper access to the ``heat`` database. Replace *HEAT_DBPASS*  
     with a suitable password::

      GRANT ALL PRIVILEGES ON heat.* TO 'heat'@'localhost' \
        IDENTIFIED BY 'HEAT_DBPASS';
      GRANT ALL PRIVILEGES ON heat.* TO 'heat'@'%' \
        IDENTIFIED BY 'HEAT_DBPASS';

   * Exit the database access client.

#. Source the ``admin`` credentials to gain access to admin-only CLI
   commands::

       $ source admin-openrc.sh

#. To create the service credentials, complete these steps:

   * Create the ``heat`` user::

        $ openstack user create --domain default --password-prompt heat
        User Password:
        Repeat User Password:
        +-----------+----------------------------------+
        | Field     | Value                            |
        +-----------+----------------------------------+
        | domain_id | default                          |
        | enabled   | True                             |
        | id        | ca2e175b851943349be29a328cc5e360 |
        | name      | heat                             |
        +-----------+----------------------------------+

   * Add the ``admin`` role to the ``heat`` user::

     $ openstack role add --project service --user heat admin

   * Create the ``heat`` and ``heat-cfn`` service entities:

      * ::

            $ openstack service create --name heat \
              --description "Orchestration" orchestration
            +-------------+----------------------------------+
            | Field       | Value                            |
            +-------------+----------------------------------+
            | description | Orchestration                    |
            | enabled     | True                             |
            | id          | 727841c6f5df4773baa4e8a5ae7d72eb |
            | name        | heat                             |
            | type        | orchestration                    |
            +-------------+----------------------------------+

      * ::

            $ openstack service create --name heat-cfn \
              --description "Orchestration" cloudformation
            +-------------+----------------------------------+
            | Field       | Value                            |
            +-------------+----------------------------------+
            | description | Orchestration                    |
            | enabled     | True                             |
            | id          | c42cede91a4e47c3b10c8aedc8d890c6 |
            | name        | heat-cfn                         |
            | type        | cloudformation                   |
            +-------------+----------------------------------+

#. Create the Orchestration service API endpoints:

      * ::

            $ openstack endpoint create --region RegionOne \
              orchestration public http://controller:8004/v1/%\(tenant_id\)s
            +--------------+-----------------------------------------+
            | Field        | Value                                   |
            +--------------+-----------------------------------------+
            | enabled      | True                                    |
            | id           | 3f4dab34624e4be7b000265f25049609        |
            | interface    | public                                  |
            | region       | RegionOne                               |
            | region_id    | RegionOne                               |
            | service_id   | 727841c6f5df4773baa4e8a5ae7d72eb        |
            | service_name | heat                                    |
            | service_type | orchestration                           |
            | url          | http://controller:8004/v1/%(tenant_id)s |
            +--------------+-----------------------------------------+

      * ::

            $ openstack endpoint create --region RegionOne \
              orchestration internal http://controller:8004/v1/%\(tenant_id\)s
            +--------------+-----------------------------------------+
            | Field        | Value                                   |
            +--------------+-----------------------------------------+
            | enabled      | True                                    |
            | id           | 9489f78e958e45cc85570fec7e836d98        |
            | interface    | internal                                |
            | region       | RegionOne                               |
            | region_id    | RegionOne                               |
            | service_id   | 727841c6f5df4773baa4e8a5ae7d72eb        |
            | service_name | heat                                    |
            | service_type | orchestration                           |
            | url          | http://controller:8004/v1/%(tenant_id)s |
            +--------------+-----------------------------------------+

      * ::

            $ openstack endpoint create --region RegionOne \
              orchestration admin http://controller:8004/v1/%\(tenant_id\)s
            +--------------+-----------------------------------------+
            | Field        | Value                                   |
            +--------------+-----------------------------------------+
            | enabled      | True                                    |
            | id           | 76091559514b40c6b7b38dde790efe99        |
            | interface    | admin                                   |
            | region       | RegionOne                               |
            | region_id    | RegionOne                               |
            | service_id   | 727841c6f5df4773baa4e8a5ae7d72eb        |
            | service_name | heat                                    |
            | service_type | orchestration                           |
            | url          | http://controller:8004/v1/%(tenant_id)s |
            +--------------+-----------------------------------------+

      * ::

            $ openstack endpoint create --region RegionOne \
              cloudformation public http://controller:8000/v1
            +--------------+----------------------------------+
            | Field        | Value                            |
            +--------------+----------------------------------+
            | enabled      | True                             |
            | id           | b3ea082e019c4024842bf0a80555052c |
            | interface    | public                           |
            | region       | RegionOne                        |
            | region_id    | RegionOne                        |
            | service_id   | c42cede91a4e47c3b10c8aedc8d890c6 |
            | service_name | heat-cfn                         |
            | service_type | cloudformation                   |
            | url          | http://controller:8000/v1        |
            +--------------+----------------------------------+

      * ::

            $ openstack endpoint create --region RegionOne \
              cloudformation internal http://controller:8000/v1
            +--------------+----------------------------------+
            | Field        | Value                            |
            +--------------+----------------------------------+
            | enabled      | True                             |
            | id           | 169df4368cdc435b8b115a9cb084044e |
            | interface    | internal                         |
            | region       | RegionOne                        |
            | region_id    | RegionOne                        |
            | service_id   | c42cede91a4e47c3b10c8aedc8d890c6 |
            | service_name | heat-cfn                         |
            | service_type | cloudformation                   |
            | url          | http://controller:8000/v1        |
            +--------------+----------------------------------+

      * ::

            $ openstack endpoint create --region RegionOne \
              cloudformation admin http://controller:8000/v1
            +--------------+----------------------------------+
            | Field        | Value                            |
            +--------------+----------------------------------+
            | enabled      | True                             |
            | id           | 3d3edcd61eb343c1bbd629aa041ff88b |
            | interface    | internal                         |
            | region       | RegionOne                        |
            | region_id    | RegionOne                        |
            | service_id   | c42cede91a4e47c3b10c8aedc8d890c6 |
            | service_name | heat-cfn                         |
            | service_type | cloudformation                   |
            | url          | http://controller:8000/v1        |
            +--------------+----------------------------------+

#. Orchestration requires additional information in the Identity service to
   manage stacks. To add this information, complete these steps:

   * Create the ``heat`` domain that contains projects and users for stacks::

      $ openstack domain create --description "Stack projects and users" heat
      +-------------+----------------------------------+
      | Field       | Value                            |
      +-------------+----------------------------------+
      | description | Stack projects and users         |
      | enabled     | True                             |
      | id          | 0f4d1bd326f2454dacc72157ba328a47 |
      | name        | heat                             |
      +-------------+----------------------------------+

   * Create the ``heat_domain_admin`` user to manage projects and users in the
     ``heat`` domain::

      $ openstack user create --domain heat --password-prompt heat_domain_admin
      User Password:
      Repeat User Password:
      +-----------+----------------------------------+
      | Field     | Value                            |
      +-----------+----------------------------------+
      | domain_id | 0f4d1bd326f2454dacc72157ba328a47 |
      | enabled   | True                             |
      | id        | b7bd1abfbcf64478b47a0f13cd4d970a |
      | name      | heat_domain_admin                |
      +-----------+----------------------------------+

   * Add the ``admin`` role to the ``heat_domain_admin`` in the ``heat`` domain
     to enable administrative stack management privileges by the
     ``heat_domain_admin`` user::

      $ openstack role add --domain heat --user heat_domain_admin admin

   * Create the ``heat_stack_owner`` role::

      $ openstack role create heat_stack_owner
      +-------+----------------------------------+
      | Field | Value                            |
      +-------+----------------------------------+
      | id    | 15e34f0c4fed4e68b3246275883c8630 |
      | name  | heat_stack_owner                 |
      +-------+----------------------------------+

   * Create the ``heat_stack_user`` role::

      $ openstack role create heat_stack_user
      +-------+----------------------------------+
      | Field | Value                            |
      +-------+----------------------------------+
      | id    | 88849d41a55d4d1d91e4f11bffd8fc5c |
      | name  | heat_stack_user                  |
      +-------+----------------------------------+

Installing and configuring components
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To install and configure the Orchestration components:

#. Install OpenStack Orchestration bundle::

    # swupd bundle-add openstack-orchestration
    # swupd verify --fix

#. Custom configuration will be located at ``/etc/heat/heat.conf file``.

   * Create the ``/etc/heat`` directory::

      # mkdir /etc/heat

   * Create empty heat configuration file ``/etc/heat/heat.conf``::

      # touch /etc/heat/heat.conf

#. Edit the ``/etc/heat/heat.conf`` file and complete the following
   actions:

   * In the ``[database]`` section, configure database access.
     Replace *HEAT_DBPASS*  with the password you chose for the
     Orchestration database::

        [database]
        ...
        connection = mysql://heat:HEAT_DBPASS@controller/heat

   * In the ``[DEFAULT]`` and ``[oslo_messaging_rabbit]`` sections, configure
     RabbitMQ message queue access. Replace ``RABBIT_PASS``  with the password
     you chose for the ``openstack`` account in RabbitMQ::

        [DEFAULT]
        ...
        rpc_backend = rabbit

        [oslo_messaging_rabbit]
        ...
        rabbit_host = controller
        rabbit_userid = openstack
        rabbit_password = RABBIT_PASS

   * In the ``[keystone_authtoken]``, ``[trustee]``, ``[clients_keystone]``,
     and ``[ec2authtoken]`` sections, configure Identity service access. Replace
     ``HEAT_PASS`` with the password you chose for the heat user in the Identity
     service.::

            [keystone_authtoken]
            ...
            auth_uri = http://controller:5000
            auth_url = http://controller:35357
            auth_plugin = password
            project_domain_id = default
            user_domain_id = default
            project_name = service
            username = heat
            password = HEAT_PASS

            [trustee]
            ...
            auth_uri = http://controller:5000
            auth_url = http://controller:35357
            auth_plugin = password
            project_domain_id = default
            user_domain_id = default
            project_name = service
            username = heat
            password = HEAT_PASS

            [clients_keystone]
            ...
            auth_uri = http://controller:5000

            [ec2authtoken]
            ...
            auth_uri = http://controller:5000


   * In the ``[DEFAULT]`` section, configure the metadata and wait
     condition URLs::

            [DEFAULT]
            ...
            heat_metadata_server_url = http://controller:8000
            heat_waitcondition_server_url = http://controller:8000/v1/waitcondition

   * In the ``[DEFAULT]`` section, configure the stack domain and administrative
     credentials. Replace ``HEAT_DOMAIN_PASS`` with the password you chose for
     the ``heat_domain_admin`` user in the Identity service.::

            [DEFAULT]
            ...
            stack_domain_admin = heat_domain_admin
            stack_domain_admin_password = HEAT_DOMAIN_PASS
            stack_user_domain_name = heat


#. Ensure files have proper ownership by running the following command::

       # systemctl restart update-triggers.target

#. Populate the Orchestration database::

       # su -s /bin/sh -c "heat-manage db_sync" heat

Finalize installation
~~~~~~~~~~~~~~~~~~~~~~~~

Complete this step to finalize the installation:

* Start the Orchestration services and configure them to start when the
  system boots::

       # systemctl enable heat-api.service heat-api-cfn.service heat-engine.service
       # systemctl start heat-api.service heat-api-cfn.service heat-engine.service

Verify operation
----------------

#. Source the ``admin`` tenant credentials::

    $ source admin-openrc.sh

#. List service components to verify successful launch and registration of each
   process::

    $ heat service-list
    +------------+-------------+--------------------------------------+------------+--------+----------------------------+--------+
    | hostname   | binary      | engine_id                            | host       | topic  | updated_at                 | status |
    +------------+-------------+--------------------------------------+------------+--------+----------------------------+--------+
    | controller | heat-engine | 3e85d1ab-a543-41aa-aa97-378c381fb958 | controller | engine | 2015-10-13T14:16:06.000000 | up     |
    | controller | heat-engine | 45dbdcf6-5660-4d5f-973a-c4fc819da678 | controller | engine | 2015-10-13T14:16:06.000000 | up     |
    | controller | heat-engine | 51162b63-ecb8-4c6c-98c6-993af899c4f7 | controller | engine | 2015-10-13T14:16:06.000000 | up     |
    | controller | heat-engine | 8d7edc6d-77a6-460d-bd2a-984d76954646 | controller | engine | 2015-10-13T14:16:06.000000 | up     |
    +------------+-------------+--------------------------------------+------------+--------+----------------------------+--------+
