Installing OpenStack* MVP bundles
############################################################

Note: This article walks through an OpenStack MVP installation by using
bundles available for Clear Linux* OS for Intel® Architecture. The sample
configuration files that are included would likely require modification
for your environment.

Database
-----------------

Most OpenStack services use an SQL database to store information. The
database typically runs on the controller node. The procedures in this
article use MariaDB.

Installing and configuring the database server
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To install and configure the database server using the MariaDB bundle:

#. Install MariaDB bundle:
   
  .. code:: text

    # clr_bundle_add database-mariadb

2. Create the ``/etc/mariadb/`` folder and the ``/etc/mariadb/openstack.cnf`` file.
#. Add the ``[mysqld]`` section, set the bind-address key to the
   management IP address of the controller node to enable access by
   other nodes via the management network and enable useful options for
   UTF-8 character set:

  .. code:: text

    [mysqld]
    bind-address = 10.0.0.11
    default-storage-engine = innodb
    innodb_file_per_tablecollation-server = utf8_general_ci
    init-connect = 'SET NAMES utf8'
    character-set-server = utf8

Finalizing database installation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Complete the following steps to finalize database installation:

#. Start the database service and configure it to start when the system
   boots:

  .. code:: text

    # systemctl enable mariadb.service
    # systemctl start mariadb.service

2. Secure the database service including choosing a suitable password
   for the root account:

  .. code:: text

    # mysql_secure_installation

Messaging server
----------------------

OpenStack uses a message broker to coordinate operations and status
information among services. The message broker service typically runs on
the controller node.

Installing the RabbitMQ message broker service
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Complete the following steps to install the RabbitMQ message broker service:

#. Install RabbitMQ bundle:
   
   .. code:: text

    # clr_bundle_add message-broker-rabbitmq

Configuring the message broker service
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Complete the following steps to configure the message broker service:

#. Message broker service needs to be able to resolve to itself. Add the
   following line to ``/etc/hosts``

   .. code:: text

    127.0.0.1 controller

#. Start the message broker service and configure it to start when the
   system boots:

   .. code:: text

    # systemctl enable rabbitmq-server.service
    # systemctl start rabbitmq-server.service

3. Add the OpenStack user:
   
   .. code:: text

    rabbitmqctl add_user openstack RABBIT_PASS
    Creating user openstack ...
    ...done.

#. Replace ``RABBIT_PASS`` with a suitable password.
#. Permit configuration, write, and read access for the OpenStack user:
   
   .. code:: text

    # rabbitmqctl set_permissions openstack ".*" ".*" ".*"
    Setting permissions for user "openstack" in vhost "/" ...
    ...done.

OpenStack Identity
--------------------------

The OpenStack Identity Service performs the following functions:

-  Tracking users and their permissions.
-  Providing a catalog of available services with their API endpoints.

When installing OpenStack Identity service, you must register each
service in your OpenStack installation. Identity service can then track
which OpenStack services are installed, and where they are located on
the network.

Configuring prerequisites for Identity service
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Before you configure the OpenStack Identity service, you must create a
database and an administration token.

#. To create the database, complete these steps:

   #. Use the database access client to connect to the database server
      as the root user:

      .. code:: text

        $ mysql -u root -p

   #. Create the keystone database:
      
      .. code:: text

        CREATE DATABASE keystone;

   #. Grant proper access to the keystone database. Replace
      ``KEYSTONE_DBPASS`` with a suitable password.

      .. code:: text

        GRANT ALL PRIVILEGES ON keystone.* TO 'keystone'@'localhost' 
        IDENTIFIED BY 'KEYSTONE_DBPASS';
        GRANT ALL PRIVILEGES ON keystone.* TO 'keystone'@'%' 
        IDENTIFIED BY 'KEYSTONE_DBPASS';

   #. Exit the database access client.

#. Generate a random value to use as the administration token during
   initial configuration:

   .. code:: text

    openssl rand -hex 10

Installing and configuring the Identity components
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Complete the following steps to install and configure the Identity components:

#. Install OpenStack Identity bundle:
   
   .. code:: text

    # clr_bundle_add openstack-identity

2. Custom configurations will be located at ``/etc/keystone``.

   #. Create ``/etc/keystone`` directory.
      
      .. code:: text

        mkdir /etc/keystone

   #. Create empty keystone configuration file ``/etc/keystone/keystone.conf``.
      
      .. code:: text

        touch /etc/keystone/keystone.conf

#. Edit the ``/etc/keystone/keystone.conf`` file and complete the
   following actions:

   #. In the ``[DEFAULT]`` section, define the value of the initial
      administration token. Replace ``ADMIN_TOKEN`` with the random
      value that you generated in a previous step.

      .. code:: text

        [DEFAULT]
        ... 
        admin_token = ADMIN_TOKEN

   #. In the ``[database]`` section, configure database access. Replace
      ``KEYSTONE_DBPASS`` with the password you chose for the database.

      .. code:: text

        [database]
        ...
        connection=mysql://keystone:KEYSTONE_DBPASS@controller/keystone

#. Enter the following command:
   
   .. code:: text

    # systemctl restart update-triggers.target

#. Populate the Identity service database:
   
   .. code:: text

    su -s /bin/sh -c "keystone-manage db_sync" keystone

Finalizing Identity installation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Complete the following steps to finalize Identity installation:

#. Keystone is deployed as a wsgi module. To start the Identity
   service, you should enable and start httpd service.

   .. code:: text

    # systemctl enable httpd.service memcached.service
    # systemctl start httpd.service memcached.service

About projects, users, and roles
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After you install the Identity service, you need to create projects,
users, and roles for your environment. You must use the temporary
administration token that you created and manually configure the
location (endpoint) of the Identity service before you run keystone
commands.

You can pass the value of the administration token to the keystone
command with the ``--os-token`` option or set the temporary ``OS_TOKEN``
environment variable. Similarly, you can pass the location of the
Identity service to the keystone command with the ``--os-endpoint``
option or set the temporary ``OS_URL`` environment variable. This guide
uses environment variables to reduce command length.

Configuring prerequisites for projects, users and roles
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Complete the following steps to configure prerequisites:

#. Configure the administration token:
   
   .. code:: text

    $ export OS_TOKEN=ADMIN_TOKEN 

#. Replace ``ADMIN_TOKEN`` with the administration token that you
   generated in the previous section. For example:

   .. code:: text

    $ export OS_TOKEN=294a4c8a8a475f9b9836

#. Configure the endpoint:
   
   .. code:: text

    $ export OS_URL=http://controller:35357/v2.0

**To install the OpenStack Python clients:**

#. Install OpenStack Python bundle:
   
   .. code:: text

    clr_bundle_add openstack-python-clients

Creating projects, users and roles
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Complete the following steps to create projects, users and roles:

#. Create an administrative project, user, and role for administrative
   operations in your environment:

   #. Create the admin project:
      
      .. code:: text
      
        $ openstack project create --description "Admin project" admin
        +-------------+----------------------------------+
        | Property    | Value                            |
        +-------------+----------------------------------+
        | description | Admin project                    |
        | enabled     | True                             |
        | id          | 6f4c1e4cbfef4d5a8a1345882fbca110 |
        | name        | admin                            |
        +-------------+----------------------------------+

   #. Create the admin user. Replace ``ADMIN_PASS`` with a suitable
      password and ``EMAIL_ADDRESS`` with a suitable e-mail address.

      .. code:: text

        $ openstack user create admin --password ADMIN_PASS --email EMAIL_ADDRESS
        +----------+----------------------------------+
        | Property | Value                            |
        +----------+----------------------------------+
        | email    | admin@example.com                |
        | enabled  | True                             |
        | id       | ea8c352d253443118041c9c8b8416040 |
        | name     | admin                            |
        | username | admin                            |
        +----------+----------------------------------+ 

   #. Create the admin role:
      
      .. code:: text

        $ openstack role create admin
        +----------+----------------------------------+
        | Property | Value                            |
        +----------+----------------------------------+
        | id       | bff3a6083b714fa29c9344bf8930d199 |
        | name     | admin                            |
        +----------+----------------------------------+ 

   #. Add the admin role to the admin project and user:
      
      .. code:: text

        $ openstack role add --project admin --user admin admin

#. Create a demo project and user for typical operations in your
   environment:

   #. Create the demo project:
      
      .. code:: text

        $ openstack project create --description "Demo Project" demo
        +-------------+----------------------------------+
        | Property    | Value                            |
        +-------------+----------------------------------+
        | description | Demo project                     |
        | enabled     | True                             |
        | id          | 4aa51bb942be4dd0ac0555d7591f80a6 |
        | name        | demo                             |
        +-------------+----------------------------------+ 

   #. Create the demo user under the demo project. Replace ``DEMO_PASS``
      with a suitable password and ``EMAIL_ADDRESS`` with a suitable
      e-mail address.

      .. code:: text

        $ openstack user create demo --project demo --password DEMO_PASS --email EMAIL_ADDRESS
        +----------+----------------------------------+
        | Property | Value                            |
        +----------+----------------------------------+
        | email    | demo@example.com                 |
        | enabled  | True                             |
        | id       | 7004dfa0dda84d63aef81cf7f100af01 |
        | name     | demo                             |
        | projectId| 4aa51bb942be4dd0ac0555d7591f80a6 |
        | username | demo                             |
        +----------+----------------------------------+ 

#. OpenStack services also require a project, user, and role to interact
   with other services. Each service typically requires creating one or
   more unique users with the admin role under the service project.

   #. Create the service project:
      
      .. code:: text

        $ openstack project create --description "Service Project" service
        +-------------+----------------------------------+
        | Property    | Value                            |
        +-------------+----------------------------------+
        | description | Service project                  |
        | enabled     | True                             |
        | id          | 6b69202e1bf846a4ae50d65bc4789122 |
        | name        | service                          |
        +-------------+----------------------------------+ 

Creating the service entity and API endpoint
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After you create projects, users, and roles, you must create the service
entity and API endpoints for the Identity service.

To create the service entity and API endpoints:

#. The Identity service manages a catalog of services in your OpenStack
   environment. Services use this catalog to locate other services in
   your environment. Create the service entity for the Identity service:

   .. code:: text

    $ openstack service create identity --name keystone --description "OpenStack Identity"
    +-------------+----------------------------------+
    | Property    | Value                            |
    +-------------+----------------------------------+
    | description | OpenStack Identity               |
    | enabled     | True                             |
    | id          | 15c11a23667e427e91bc31335b45f4bd |
    | name        | keystone                         |
    | type        | identity                         |
    +-------------+----------------------------------+ 

#. The Identity service manages a catalog of API endpoints associated
   with the services in your OpenStack environment. Services use this
   catalog to determine how to communicate with other services in your
   environment. OpenStack provides three API endpoint variations for
   each service: admin, internal, and public. In a production
   environment, the variants might reside on separate networks that
   service different types of users for security reasons. Also,
   OpenStack supports multiple regions for scalability. For simplicity,
   this configuration uses the management network for all endpoint
   variations and the regionOne region. Create the Identity service API
   endpoints:

   .. code:: text

    $ openstack endpoint create \
    --publicurl http://controller:5000/v2.0 \
    --internalurl http://controller:5000/v2.0 \
    --adminurl http://controller:35357/v2.0 \
    --region regionOne \
    identity
    +-------------+----------------------------------+
    | Property    | Value                            |
    +-------------+----------------------------------+
    | adminurl    | http://controller:35357/v2.0     |
    | id          | 11f9c625a3b94a3f8e66bf4e5de2679f |
    | internalurl | http://controller:5000/v2.0      |
    | publicurl   | http://controller:5000/v2.0      |
    | region      | regionOne                        |
    | service_id  | 15c11a23667e427e91bc31335b45f4bd |
    +-------------+----------------------------------+ 

OpenStack client environment scripts
------------------------------------------------------

To increase efficiency of client operations, OpenStack supports simple
client environment scripts also known as OpenRC files. These scripts
typically contain common options for all clients, but also support
unique options.

Creating the scripts
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create client environment scripts for the admin and demo projects and
users. Future portions of this guide reference these scripts to load
appropriate credentials for client operations.

#. Edit the ``admin-openrc.sh`` file and add the following content.
   Replace ``ADMIN_PASS`` with the password you chose for the admin user
   in the Identity service.

   .. code:: text

    export OS_PROJECT_DOMAIN_ID=default
    export OS_USER_DOMAIN_ID=default
    export OS_PROJECT_NAME=admin
    export OS_TENANT_NAME=admin
    export OS_USERNAME=admin
    export OS_PASSWORD=ADMIN_PASS
    export OS_AUTH_URL=http://controller:35357/v3

#. Edit the ``demo-openrc.sh`` file and add the following content.
   Replace ``DEMO_PASS`` with the password you chose for the demo user
   in the Identity service.

   .. code:: text

    export OS_PROJECT_DOMAIN_ID=default
    export OS_USER_DOMAIN_ID=default
    export OS_PROJECT_NAME=demo
    export OS_TENANT_NAME=demo
    export OS_USERNAME=demo
    export OS_PASSWORD=DEMO_PASS
    export OS_AUTH_URL=http://controller:5000/v3

Loading client environment scripts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To run clients as a certain project and user, you can simply load the
associated client environment script prior to running them. For example,
to load the location of the Identity service and admin project and user
credentials:

 .. code:: text

  $ unset OS_URL OS_TOKEN 
  $ source admin-openrc.sh

OpenStack Image Service
------------------------------

The OpenStack Image Service accepts API requests for disk or server
images, and image metadata from end users or OpenStack Compute
components.

Configuring Image Service prerequisites
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Before you install and configure the Image Service, you must create a
database, service credentials, and API endpoints.

#. To create the database, complete these steps:

   #. Use the database access client to connect to the database server
      as the root user:

      .. code:: text

        $ mysql -u root -p

   #. Create the glance database. Replace ``GLANCE_DBPASS`` with a
      suitable password.

      .. code:: text

        CREATE DATABASE glance;

   #. Grant proper access to the glance database:
      
      .. code:: text

        GRANT ALL PRIVILEGES ON glance.* TO 'glance'@'localhost' \
        IDENTIFIED BY 'GLANCE_DBPASS';
        GRANT ALL PRIVILEGES ON glance.* TO 'glance'@'%' \
        IDENTIFIED BY 'GLANCE_DBPASS';

   #. Exit the database access client.

#. Source the admin credentials to gain access to admin-only CLI
   commands:

   .. code:: text

    $ source admin-openrc.sh

#. To create the service credentials, complete these steps:

   #. Create the glance user. Replace ``GLANCE_PASS`` with a suitable
      password.

      .. code:: text

        $ openstack user create glance --password GLANCE_PASS
        +----------+----------------------------------+
        | Property | Value                            |
        +----------+----------------------------------+
        | email    |                                  |
        | enabled  | True                             |
        | id       | f89cca5865dc42b18e2421fa5f5cce66 |
        | name     | glance                           |
        | username | glance                           |
        +----------+----------------------------------+ 

   #. Add the admin role to the glance user:
      
      .. code:: text

        $ openstack role add admin --user glance --project service

   #. Create the glance service entity:
      
      .. code:: text

        $ openstack service create image --name glance \
        --description "OpenStack Image Service"
        +-------------+----------------------------------+
        | Property    | Value                            |
        +-------------+----------------------------------+
        | description | OpenStack Image Service          |
        | enabled     | True                             |
        | id          | 23f409c4e79f4c9e9d23d809c50fbacf |
        | name        | glance                           |
        | type        | image                            |
        +-------------+----------------------------------+ 

#. Create the Image Service API endpoints:
   
   .. code:: text

    $ openstack endpoint create \
    --publicurl http://controller:9292 \
    --internalurl http://controller:9292 \
    --adminurl http://controller:9292 \
    --region regionOne \
    image
    +-------------+----------------------------------+
    | Property    | Value                            |
    +-------------+----------------------------------+
    | adminurl    | http://controller:9292           |
    | id          | a2ee818c69cb475199a1ca108332eb35 |
    | internalurl | http://controller:9292           |
    | publicurl   | http://controller:9292           |
    | region      | regionOne                        |
    | service_id  | 23f409c4e79f4c9e9d23d809c50fbacf |
    +-------------+----------------------------------+ 

Installing and configuring the Image Service components
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Complete the following steps to install and configure the Image Service components:

#. Install OpenStack Image bundle:
   
   .. code:: text

    # clr_bundle_add openstack-image

#. configurations will be located at ``/etc/glance``

   #. Create ``/etc/glance`` directory:
      
      .. code:: text

        mkdir /etc/glance

   #. Create empty configuration files ``/etc/glance/glance-api.conf``
      and ``/etc/glance/glance-registry.conf``:

      .. code:: text

        touch /etc/glance/glance-{api,registry}.conf

#. Edit the ``/etc/glance/glance-api.conf`` file and complete the
   following actions:

   #. In the ``[database]`` section, configure database access. Replace
      ``GLANCE_DBPASS`` with the password you chose for the Image
      Service database.

      .. code:: text

        [database]
        ...
        connection=mysql://glance:GLANCE_DBPASS@controller/glance

   #. In the ``[keystone_authtoken]`` and ``[paste_deploy]`` sections,
      configure Identity service access. Replace ``GLANCE_PASS`` with
      the password you chose for the glance user in the Identity
      service.

      .. code:: text

        [keystone_authtoken]
        ...
        auth_uri = http://controller:5000/v2.0
        identity_uri = http://controller:35357
        admin_project_name = service
        admin_user = glance
        admin_password = GLANCE_PASS
        [paste_deploy]
        ...
        flavor = keystone

#. Edit the ``/etc/glance/glance-registry.conf`` file and complete the
   following actions. Replace ``GLANCE\_DBPASS`` with the password you
   chose for the Image Service database.

   #. In the ``[database]`` section, configure database
      access.  Replace ``GLANCE_DBPASS`` with the password you chose
      for the Image Service database.

       .. code:: text

        [database] 
        ...
        connection=mysql://glance:GLANCE_DBPASS@controller/glance

   #. In the ``[keystone_authtoken]`` and ``[paste_deploy]`` sections,
      configure Identity service access. Replace ``GLANCE_PASS`` with the password you chose
      for the glance user in the Identity service.

      .. code:: text

        [keystone_authtoken]
        ...
        auth_uri = http://controller:5000 /v2 .0
        identity_uri = http://controller:35357
        admin_project_name = service
        admin_user = glance
        admin_password = GLANCE_PASS
        [paste_deploy]
        ...
        flavor = keystone

#. Let systemd set the correct permissions for files in ``/etc/glance``.
   
   .. code:: text

    # systemctl restart update-triggers.target

6. Populate the Image Service database:
   
   .. code:: text

    su -s /bin/sh -c "glance-manage db_sync" glance

Finalizing Image Service installation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Complete the following steps to finalize Image Service installation:

#. Start the Image Service services and configure them to start when the
   system boots:

   .. code:: text

    systemctl enable glance-api.service glance-registry.service 
    systemctl start glance-api.service glance-registry.service

OpenStack Compute
----------------------------

Use OpenStack Compute to host and manage cloud computing systems.
OpenStack Compute interacts with OpenStack Identity for authentication,
OpenStack Image Service for disk and server images, and OpenStack
dashboard for the user and administrative interface. Image access is
limited by projects, and by users; quotas are limited per project (the
number of instances, for example). OpenStack Compute can scale
horizontally on standard hardware, and download images to launch
instances.

Configuring Compute prerequisites
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Before you install and configure the Compute service, you must create a
database, service credentials, and API endpoints.

#. To create the database, complete these steps:

   #. Use the database access client to connect to the database server
      as the root user:

      .. code:: text

        $ mysql -u root -p

   #. Create the nova database:
      
      .. code:: text

        CREATE DATABASE nova;

   #. Grant proper access to the nova database. Replace ``NOVA_DBPASS``
      with a suitable password.

      .. code:: text

        GRANT ALL PRIVILEGES ON nova.* TO 'nova'@'localhost' \
        IDENTIFIED BY 'NOVA_DBPASS';
        GRANT ALL PRIVILEGES ON nova.* TO 'nova'@'%' \
        IDENTIFIED BY 'NOVA_DBPASS';

   #. Exit the database access client.

#. Source the admin credentials to gain access to admin-only CLI
   commands:

   .. code:: text

    $ source admin-openrc.sh

#. To create the service credentials, complete these steps:

   #. Create the nova user. Replace ``NOVA_PASS`` with a suitable
      password.

      .. code:: text

        $ openstack user create nova --password NOVA_PASS  
        +----------+----------------------------------+
        | Property | Value                            |
        +----------+----------------------------------+
        | email    |                                  |
        | enabled  | True                             |
        | id       | 387dd4f7e46d4f72965ee99c76ae748c |
        | name     | nova                             |
        | username | nova                             |
        +----------+----------------------------------+ 

   #. Add the admin role to the nova user:
      
      .. code:: text

        $ openstack role add admin --user nova --project service

   #. Create the nova service entity:
      
      .. code:: text

        $ openstack service create compute --name nova \
        --description "OpenStack Compute"
        +-------------+----------------------------------+
        | Property    | Value                            |
        +-------------+----------------------------------+
        | description | OpenStack Compute                |
        | enabled     | True                             |
        | id          | 6c7854f52ce84db795557ebc0373f6b9 |
        | name        | nova                             |
        | type        | compute                          |
        +-------------+----------------------------------+ 

#. Create the Compute service API endpoints:
   
   .. code:: text

    $ openstack endpoint create \
    --publicurl http://controller:8774/v2/%\(project_id\)s \
    --internalurl http://controller:8774/v2/%\(project_id\)s \
    --adminurl http://controller:8774/v2/%\(project_id\)s \
    --region regionOne
    compute
    +-------------+------------------------------------------+
    | Property    | Value                                    |
    +-------------+------------------------------------------+
    | adminurl    | http://controller:8774/v2/%(project_id)s |
    | id          | c397438bd82c41198ec1a9d85cb7cc74         |
    | internalurl | http://controller:8774/v2/%(project_id)s |
    | publicurl   | http://controller:8774/v2/%(project_id)s |
    | region      | regionOne                                |
    | service_id  | 6c7854f52ce84db795557ebc0373f6b9         |
    +-------------+------------------------------------------+ 

Installing and configuring the Compute controller components
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To install and configure the Compute controller components:

#. Install OpenStack Compute Controller bundle:
   
   .. code:: text

    clr_bundle_add openstack-compute-controller

#. Custom configurations will be located at ``/etc/nova``.

   #. Create ``/etc/nova directory``.
      
      .. code:: text

        mkdir /etc/nova

   #. Create empty nova configuration file ``/etc/nova/nova.conf``.
      
      .. code:: text

        touch /etc/nova/nova.conf

#. Edit the ``/etc/nova/nova.conf`` file and complete the following
   actions:

   #. In the ``[database]`` section, configure database access. Replace
      ``NOVA_DBPASS`` with the password you chose for the Compute
      database.

      .. code:: text

        [database]
        ...
        connection=mysql://nova:NOVA_DBPASS@controller/nova

   #. In the ``[DEFAULT]`` and ``[oslo_messaging_rabbit]`` sections,
      configure RabbitMQ message broker access. Replace ``RABBIT_PASS``
      with the password you chose for the guest account in RabbitMQ.

      .. code:: text

        [DEFAULT]
        ...
        rpc_backend = rabbit

      .. code:: text

        [oslo_messaging_rabbit]
        ...
        rabbit_host = controller
        rabbit_userid = openstack
        rabbit_password = RABBIT_PASS

   #. In the ``[DEFAULT]`` and ``[keystone_authtoken]`` sections,
      configure Identity service access. Replace ``NOVA_PASS`` with the
      password you chose for the nova user in the Identity service.

      .. code:: text

        [DEFAULT]
        ...
        auth_strategy = keystone
        [keystone_authtoken]
        ...
        auth_uri = http://controller:5000/v2.0
        identity_uri = http://controller:35357
        admin_project_name = service
        admin_user = nova
        admin_password = NOVA_PASS

   #. In the ``[DEFAULT]`` section, configure the ``my_ip`` option to
      use the management interface IP address of the controller node:

      .. code:: text

        [DEFAULT]
        ...
        my_ip = 10.0.0.11

   #. In the ``[DEFAULT]`` section, configure the VNC proxy to use the
      management interface IP address of the controller node:

      .. code:: text

        [DEFAULT]
        ...
        vncserver_listen = 10.0.0.11
        vncserver_proxyclient_address = 10.0.0.11

   #. In the ``[glance]`` section, configure the location of the Image
      Service:

      .. code:: text

        [glance]
        ...
        host = controller

#. Let systemd set the correct permissions for files in ``/etc/nova``.
   
   .. code:: text

    # systemctl restart update-triggers.target

#. Populate the Compute database:
   
   .. code:: text

    su -s /bin/sh -c "nova-manage db sync" nova

Finalizing Compute installation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Complete the following steps to finalize Compute installation:

#. Start the Compute Service services and configure them to start when
   the system boots:

   .. code:: text

    systemctl enable nova-api.service nova-cert.service nova-consoleauth.service nova-scheduler.service \ 
       nova-conductor.service 
    systemctl start nova-api.service nova-cert.service nova-consoleauth.service nova-scheduler.service \ 
       nova-conductor.service

Installing and configuring the Compute service on a node
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This section describes how to install and configure the Compute service
on a compute node. This configuration uses the QEMU hypervisor with the
KVM extension on compute nodes that support hardware acceleration for
virtual machines.

To install and configure the Compute controller components:

#. Install OpenStack Compute bundle:
   
   .. code:: text

    clr_bundle_add openstack-compute

#. Custom configurations will be located at ``/etc/nova``.

   #. Create ``/etc/nova`` directory.
      
      .. code:: text

        mkdir /etc/nova

   #. Create empty nova configuration file ``/etc/nova/nova.conf``.
      
      .. code:: text

        touch /etc/nova/nova.conf

#. Edit the ``/etc/nova/nova.conf`` file and complete the following
   actions:

   #. In the ``[DEFAULT]`` and ``[oslo_messaging_rabbit]`` sections,
      configure RabbitMQ message broker access. Replace ``RABBIT_PASS``
      with the password you chose for the guest account in RabbitMQ.

      .. code:: text

        [DEFAULT]
        ...
        rpc_backend = rabbit

     .. code:: text

        [oslo_messaging_rabbit]
        ...
        rabbit_host = controller
        rabbit_userid = openstack
        rabbit_password = RABBIT_PASS

   #. In the ``[DEFAULT]`` and ``[keystone_authtoken]`` sections,
      configure Identity service access. Replace ``NOVA_PASS`` with the
      password you chose for the nova user in the Identity service.

      .. code:: text

        [DEFAULT]
        ...
        auth_strategy = keystone
        [keystone_authtoken]
        ...
        auth_uri = http://controller:5000/v2.0
        identity_uri = http://controller:35357
        admin_project_name = service
        admin_user = nova
        admin_password = NOVA_PASS

   #. In the ``[DEFAULT]`` section, configure the ``my_ip`` option.
      Replace ``MANAGEMENT_INTERFACE_IP_ADDRESS`` with the IP address of
      the management network interface on your compute node, typically
      ``10.0.0.31`` for the first node in the example architecture.

      .. code:: text

        [DEFAULT]
        ...
        my_ip = MANAGEMENT_INTERFACE_IP_ADDRESS

   #. In the ``[DEFAULT]`` section, enable and configure remote console
      access. Replace ``MANAGEMENT_INTERFACE_IP_ADDRESS`` with the IP
      address of the management network interface on your compute node,
      typically ``10.0.0.31`` for the first node in the example
      architecture.

      .. code:: text

        [DEFAULT]
        ...
        vnc_enabled = True
        vncserver_listen = 0.0.0.0
        vncserver_proxyclient_address = MANAGEMENT_INTERFACE_IP_ADDRESS
        novncproxy_base_url = http://controller:6080/vnc_auto.html
        compute_driver = libvirt.LibvirtDriver

      The server component listens on all IP addresses and the proxy
      component only listens on the management interface IP address of
      the compute node. The base URL indicates the location where you
      can use a web browser to access remote consoles of instances on
      this compute node.

   #. In the ``[glance]`` section, configure the location of the Image
      Service:

      .. code:: text

        [glance]
        ...
        host = controller

Finalize compute node installation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Complete the following steps to Finalize compute node installation:

#. Determine whether your compute node supports hardware acceleration
   for virtual machines:

   .. code:: text

    $ egrep -c '(vmx|svm)' /proc/cpuinfo

   If this command returns a value of *one or greater*, your compute node
   supports hardware acceleration which typically requires no additional
   configuration.

   If this command returns a value of *zero* , your compute node does
   not support hardware acceleration and you must configure libvirt to
   use QEMU instead of KVM.

   #. Edit the ``[libvirt]`` section in the ``/etc/nova/nova.conf`` file
      as follows:

      .. code:: text

        [libvirt]
        ...
        virt_type = qemu

#. Start the Compute service including its dependencies and configure
   them to start automatically when the system boots:

   .. code:: text

    systemctl enable libvirtd.service nova-compute.service nova-novncproxy.service
    systemctl start libvirtd.service nova-compute.service nova-novncproxy.service

Networking component
-----------------------------------------

The nova-network service enables you to deploy one network type per
instance and is suitable for basic network functionality.

Configuring network controller node
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Legacy networking primarily involves compute nodes. However, you must
configure the controller node to use legacy networking.

To configure legacy networking:

#. Edit the ``/etc/nova/nova.conf`` file and complete the following
   actions:

   #. In the ``[DEFAULT]`` section, configure the network and security
      group APIs:

      .. code:: text

        [DEFAULT]
        ...
        network_api_class = nova.network.api.API
        security_group_api = nova
        network_manager = nova.network.manager.FlatDHCPManager

#. Restart the Compute services:
   
   .. code:: text

    systemctl restart nova-api.service nova-scheduler.service nova-conductor.service

Configuring network redundancy across compute nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This section covers deployment of a simple flat network that provides IP
addresses to your instances via DHCP. If your environment includes
multiple compute nodes, the multi-host feature provides redundancy by
spreading network functions across compute nodes.

To configure legacy networking:

Edit the ``/etc/nova/nova.conf`` file as follows:.

#. Replace ``INTERFACE_NAME`` with the actual interface name for the
   external network. For example, ``eth1`` or ``ens224``.

   #. In the ``[DEFAULT]`` section, configure the network parameters:
      
      .. code:: text

        [DEFAULT]
        ...
        network_api_class = nova.network.api.API
        security_group_api = nova
        firewall_driver = nova.virt.libvirt.firewall.IptablesFirewallDriver
        network_manager = nova.network.manager.FlatDHCPManager
        network_size = 254
        allow_same_net_traffic = False
        multi_host = True
        send_arp_for_ha = True
        share_dhcp_address = True
        force_dhcp_release = True
        flat_network_bridge = br100
        flat_interface = INTERFACE_NAME
        public_interface = INTERFACE_NAME
        dhcpbridge /usr/bin/nova-dhcpbridge
        dhcpbridge_flagfile /etc/nova/nova.conf

#. Restart the services:
   
   .. code:: text

    systemctl enable nova-network.service nova-api-metadata.service
    systemctl start nova-network.service nova-api-metadata.service

  **Note:** replace ``nova-api-metadata.service`` with
  ``nova-api.service`` if you are deploying compute services in the same
  node as the controller.
