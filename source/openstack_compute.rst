OpenStack* Compute
##################

Use OpenStack Compute to host and manage cloud computing systems.
OpenStack Compute interacts with OpenStack Identity for authentication,
OpenStack Image Service for disk and server images, and OpenStack
Dashboard for the user and administrative interface. Image access is
limited by projects, and by users; quotas are limited per project (the
number of instances, for example). OpenStack Compute can scale
horizontally on standard hardware and download images to launch
instances.

Install and configure controller node
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This section describes how to install and configure the
Compute service, code-named nova, on the controller node.

Prerequisites
-------------

Before you install and configure the Compute service, you must
create a database, service credentials, and API endpoints.

#. To create the database, complete these steps:

   * Use the database access client to connect to the database server
     as the root user::

        $ mysql -u root -p

   * Create the ``nova`` database::

        CREATE DATABASE nova;

   * Grant proper access to the nova database. Replace ``NOVA_DBPASS``
     with a suitable password::

        GRANT ALL PRIVILEGES ON nova.* TO 'nova'@'localhost' \
        IDENTIFIED BY 'NOVA_DBPASS';
        GRANT ALL PRIVILEGES ON nova.* TO 'nova'@'%' \
        IDENTIFIED BY 'NOVA_DBPASS';

   * Exit the database access client.

#. Source the admin credentials to gain access to admin-only CLI
   commands::

    $ source admin-openrc.sh

#. To create the service credentials, complete these steps:

   * Create the ``nova`` user::

        $ openstack user create --domain default --password-prompt nova
        User Password:
        Repeat User Password:
        +-----------+----------------------------------+
        | Field     | Value                            |
        +-----------+----------------------------------+
        | domain_id | default                          |
        | enabled   | True                             |
        | id        | 8c46e4760902464b889293a74a0c90a8 |
        | name      | nova                             |
        +-----------+----------------------------------+

   * Add the ``admin`` role to the ``nova`` user::

        $ openstack role add --project service --user nova admin

   * Create the ``nova`` service entity::

        $ openstack service create --name nova \
        --description "OpenStack Compute" compute
        +-------------+----------------------------------+
        | Field       | Value                            |
        +-------------+----------------------------------+
        | description | OpenStack Compute                |
        | enabled     | True                             |
        | id          | 060d59eac51b4594815603d75a00aba2 |
        | name        | nova                             |
        | type        | compute                          |
        +-------------+----------------------------------+

#. Create the Compute service API endpoints::

      $ openstack endpoint create --region RegionOne \
        compute public http://controller:8774/v2/%\(tenant_id\)s
      +--------------+-----------------------------------------+
      | Field        | Value                                   |
      +--------------+-----------------------------------------+
      | enabled      | True                                    |
      | id           | 3c1caa473bfe4390a11e7177894bcc7b        |
      | interface    | public                                  |
      | region       | RegionOne                               |
      | region_id    | RegionOne                               |
      | service_id   | e702f6f497ed42e6a8ae3ba2e5871c78        |
      | service_name | nova                                    |
      | service_type | compute                                 |
      | url          | http://controller:8774/v2/%(tenant_id)s |
      +--------------+-----------------------------------------+

      $ openstack endpoint create --region RegionOne \
        compute internal http://controller:8774/v2/%\(tenant_id\)s
      +--------------+-----------------------------------------+
      | Field        | Value                                   |
      +--------------+-----------------------------------------+
      | enabled      | True                                    |
      | id           | e3c918de680746a586eac1f2d9bc10ab        |
      | interface    | internal                                |
      | region       | RegionOne                               |
      | region_id    | RegionOne                               |
      | service_id   | e702f6f497ed42e6a8ae3ba2e5871c78        |
      | service_name | nova                                    |
      | service_type | compute                                 |
      | url          | http://controller:8774/v2/%(tenant_id)s |
      +--------------+-----------------------------------------+

      $ openstack endpoint create --region RegionOne \
        compute admin http://controller:8774/v2/%\(tenant_id\)s
      +--------------+-----------------------------------------+
      | Field        | Value                                   |
      +--------------+-----------------------------------------+
      | enabled      | True                                    |
      | id           | 38f7af91666a47cfb97b4dc790b94424        |
      | interface    | admin                                   |
      | region       | RegionOne                               |
      | region_id    | RegionOne                               |
      | service_id   | e702f6f497ed42e6a8ae3ba2e5871c78        |
      | service_name | nova                                    |
      | service_type | compute                                 |
      | url          | http://controller:8774/v2/%(tenant_id)s |
      +--------------+-----------------------------------------+

Installing and configuring the Compute controller components
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To install and configure the Compute controller components:

#. Install OpenStack Compute Controller bundle::

    # clr_bundle_add openstack-compute-controller

#. Custom configurations will be located at ``/etc/nova``.

   * Create ``/etc/nova directory``::

        # mkdir /etc/nova

   * Create empty nova configuration file ``/etc/nova/nova.conf``::

        # touch /etc/nova/nova.conf

#. Edit the ``/etc/nova/nova.conf`` file and complete the following
   actions:

   * In the ``[database]`` section, configure database access. Replace
     ``NOVA_DBPASS`` with the password you chose for the Compute database::

        [database]
        ...
        connection=mysql://nova:NOVA_DBPASS@controller/nova

   * In the ``[DEFAULT]`` and ``[oslo_messaging_rabbit]`` sections,
     configure ``RabbitMQ`` message queue access. Replace ``RABBIT_PASS``
     with the password you chose for the guest account in RabbitMQ::

        [DEFAULT]
        ...
        rpc_backend = rabbit

        [oslo_messaging_rabbit]
        ...
        rabbit_host = controller
        rabbit_userid = openstack
        rabbit_password = RABBIT_PASS

   * In the ``[DEFAULT]`` and ``[keystone_authtoken]`` sections,
     configure Identity service access. Replace ``NOVA_PASS`` with the
     password you chose for the nova user in the Identity service::

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
        username = nova
        password = NOVA_PASS


   * In the ``[DEFAULT]`` section, configure the ``my_ip`` option to
     use the management interface IP address of the controller node::

        [DEFAULT]
        ...
        my_ip = 10.0.0.11

   * In the ``[DEFAULT]`` section, enable support for the Networking service::

        [DEFAULT]
        ...
        network_api_class = nova.network.neutronv2.api.API
        security_group_api = neutron
        linuxnet_interface_driver = nova.network.linux_net.NeutronLinuxBridgeInterfaceDriver
        firewall_driver = nova.virt.firewall.NoopFirewallDriver

   * In the ``[vnc]`` section, configure the VNC proxy to use the
     management interface IP address of the controller node::

        [vnc]
        ...
        vncserver_listen = 10.0.0.11
        vncserver_proxyclient_address = 10.0.0.11

   * In the ``[glance]`` section, configure the location of the
     Image Service::

        [glance]
        ...
        host = controller

#. Ensure files have proper ownership by running the following command::

    # systemctl restart update-triggers.target

#. Populate the Compute database::

    su -s /bin/sh -c "nova-manage db sync" nova

Finalizing Compute installation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Complete the following steps to finalize Compute installation:

#. Create the ``/etc/nginx`` directory if doesn't exists and setup the
   nova-api to start with the Nginx http server::

    # mkdir -p /etc/nginx
    # cp /usr/share/nginx/conf.d/nova-api.template /etc/nginx/nova-api.conf

#. Start the Compute Service services and configure them to start
   when the system boots::

    # systemctl enable uwsgi@nova-api.socket \
      nova-cert.service nova-consoleauth.service \
      nova-scheduler.service nova-conductor.service \
      nova-novncproxy.service
    # systemctl start uwsgi@nova-api.socket \
      nova-cert.service nova-consoleauth.service \
      nova-scheduler.service nova-conductor.service \
      nova-novncproxy.service

Install and configure a compute note
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This section describes how to install and configure the Compute service
on a compute node. This configuration uses the QEMU hypervisor with the
KVM extension on compute nodes that support hardware acceleration for
virtual machines.

Install and configure components
--------------------------------

#. Install OpenStack Compute bundle::

    # clr_bundle_add openstack-compute

#. Custom configurations will be located at ``/etc/nova``.

   * Create ``/etc/nova`` directory::

        # mkdir /etc/nova

   * Create empty nova configuration file ``/etc/nova/nova.conf``::

        # touch /etc/nova/nova.conf

#. Edit the ``/etc/nova/nova.conf`` file and complete the following
   actions:

   * In the ``[DEFAULT]`` and ``[oslo_messaging_rabbit]`` sections,
     configure RabbitMQ message broker access. Replace ``RABBIT_PASS``
     with the password you chose for the ``openstack`` account in ``RabbitMQ``::

        [DEFAULT]
        ...
        rpc_backend = rabbit

        [oslo_messaging_rabbit]
        ...
        rabbit_host = controller
        rabbit_userid = openstack
        rabbit_password = RABBIT_PASS

   * In the ``[DEFAULT]`` and ``[keystone_authtoken]`` sections,
     configure Identity service access. Replace ``NOVA_PASS`` with the
     password you chose for the nova user in the Identity service::

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
        username = nova
        password = NOVA_PASS

   * In the ``[DEFAULT]`` section, configure the ``my_ip`` option.
     Replace ``MANAGEMENT_INTERFACE_IP_ADDRESS`` with the IP address of
     the management network interface on your compute node, typically
     ``10.0.0.31`` for the first node in the example architecture::

        [DEFAULT]
        ...
        my_ip = MANAGEMENT_INTERFACE_IP_ADDRESS

   * In the ``[DEFAULT]`` section, enable support for the Networking service::

        [DEFAULT]
        ...
        network_api_class = nova.network.neutronv2.api.API
        security_group_api = neutron
        linuxnet_interface_driver = nova.network.linux_net.NeutronLinuxBridgeInterfaceDriver
        firewall_driver = nova.virt.firewall.NoopFirewallDriver

   * In the ``[vnc]`` section, enable and configure remote console access::

        [vnc]
        ...
        enabled = True
        vncserver_listen = 0.0.0.0
        vncserver_proxyclient_address = MANAGEMENT_INTERFACE_IP_ADDRESS
        novncproxy_base_url = http://controller:6080/vnc_auto.html

     The server component listens on all IP addresses and the proxy
     component only listens on the management interface IP address of
     the compute node. The base URL indicates the location where you
     can use a web browser to access remote consoles of instances on
     this compute node.

   * In the ``[glance]`` section, configure the location of the
     Image Service::

        [glance]
        ...
        host = controller

Finalize compute node installation
----------------------------------

#. Determine whether your compute node supports hardware acceleration
   for virtual machines::

    $ egrep -c '(vmx|svm)' /proc/cpuinfo

   If this command returns a value of ``one or greater``, your compute
   node supports hardware acceleration which typically requires no
   additional configuration.

   If this command returns a value of ``zero`` , your compute node does
   not support hardware acceleration and you must configure ``libvirt``
   to use QEMU instead of KVM.

   * Edit the ``[libvirt]`` section in the ``/etc/nova/nova.conf`` file
     as follows::

        [libvirt]
        ...
        virt_type = qemu

#. Ensure files have proper ownership by running the following command::

    # systemctl restart update-triggers.target

#. Start the Compute service including its dependencies and configure
   them to start automatically when the system boots::

     # systemctl enable libvirtd.service \
       nova-compute.service
     # systemctl start libvirtd.service  \
       nova-compute.service

Verify operation
~~~~~~~~~~~~~~~~
Verify operation of the Compute service.

*Note:* Perform these commands on the controller node.

#. Source the ``admin`` credentials to gain access to
   admin-only CLI commands::

      $ source admin-openrc.sh

#. List service components to verify successful launch and
   registration of each process::

      $ nova service-list
      +----+------------------+------------+----------+---------+-------+--------------+-----------------+
      | Id | Binary           | Host       | Zone     | Status  | State | Updated_at   | Disabled Reason |
      +----+------------------+------------+----------+---------+-------+--------------+-----------------+
      | 1  | nova-conductor   | controller | internal | enabled | up    | 2014-09-16.. | -               |
      | 2  | nova-consoleauth | controller | internal | enabled | up    | 2014-09-16.. | -               |
      | 3  | nova-scheduler   | controller | internal | enabled | up    | 2014-09-16.. | -               |
      | 4  | nova-cert        | controller | internal | enabled | up    | 2014-09-16.. | -               |
      | 5  | nova-compute     | compute1   | nova     | enabled | up    | 2014-09-16.. | -               |
      +----+------------------+------------+----------+---------+-------+--------------+-----------------+

#. List API endpoints in the Identity service to verify connectivity
   with the Identity service::

      $ nova endpoints
      +-----------+------------------------------------------------------------+
      | nova      | Value                                                      |
      +-----------+------------------------------------------------------------+
      | id        | 1fb997666b79463fb68db4ccfe4e6a71                           |
      | interface | public                                                     |
      | region    | RegionOne                                                  |
      | region_id | RegionOne                                                  |
      | url       | http://controller:8774/v2/ae7a98326b9c455588edd2656d723b9d |
      +-----------+------------------------------------------------------------+
      +-----------+------------------------------------------------------------+
      | nova      | Value                                                      |
      +-----------+------------------------------------------------------------+
      | id        | bac365db1ff34f08a31d4ae98b056924                           |
      | interface | admin                                                      |
      | region    | RegionOne                                                  |
      | region_id | RegionOne                                                  |
      | url       | http://controller:8774/v2/ae7a98326b9c455588edd2656d723b9d |
      +-----------+------------------------------------------------------------+
      +-----------+------------------------------------------------------------+
      | nova      | Value                                                      |
      +-----------+------------------------------------------------------------+
      | id        | e37186d38b8e4b81a54de34e73b43f34                           |
      | interface | internal                                                   |
      | region    | RegionOne                                                  |
      | region_id | RegionOne                                                  |
      | url       | http://controller:8774/v2/ae7a98326b9c455588edd2656d723b9d |
      +-----------+------------------------------------------------------------+

      +-----------+----------------------------------+
      | glance    | Value                            |
      +-----------+----------------------------------+
      | id        | 41ad39f6c6444b7d8fd8318c18ae0043 |
      | interface | admin                            |
      | region    | RegionOne                        |
      | region_id | RegionOne                        |
      | url       | http://controller:9292           |
      +-----------+----------------------------------+
      +-----------+----------------------------------+
      | glance    | Value                            |
      +-----------+----------------------------------+
      | id        | 50ecc4ce62724e319f4fae3861e50f7d |
      | interface | internal                         |
      | region    | RegionOne                        |
      | region_id | RegionOne                        |
      | url       | http://controller:9292           |
      +-----------+----------------------------------+
      +-----------+----------------------------------+
      | glance    | Value                            |
      +-----------+----------------------------------+
      | id        | 7d3df077a20b4461a372269f603b7516 |
      | interface | public                           |
      | region    | RegionOne                        |
      | region_id | RegionOne                        |
      | url       | http://controller:9292           |
      +-----------+----------------------------------+

      +-----------+----------------------------------+
      | keystone  | Value                            |
      +-----------+----------------------------------+
      | id        | 88150c2fdc9d406c9b25113701248192 |
      | interface | internal                         |
      | region    | RegionOne                        |
      | region_id | RegionOne                        |
      | url       | http://controller:5000/v2.0      |
      +-----------+----------------------------------+
      +-----------+----------------------------------+
      | keystone  | Value                            |
      +-----------+----------------------------------+
      | id        | cecab58c0f024d95b36a4ffa3e8d81e1 |
      | interface | public                           |
      | region    | RegionOne                        |
      | region_id | RegionOne                        |
      | url       | http://controller:5000/v2.0      |
      +-----------+----------------------------------+
      +-----------+----------------------------------+
      | keystone  | Value                            |
      +-----------+----------------------------------+
      | id        | fc90391ae7cd4216aca070042654e424 |
      | interface | admin                            |
      | region    | RegionOne                        |
      | region_id | RegionOne                        |
      | url       | http://controller:35357/v2.0     |
      +-----------+----------------------------------+

   *Note:* Ignore any warnings in this output.

#. List images in the Image service catalog to verify connectivity
   with the Image service::

      $ nova image-list
      +--------------------------------------+--------+--------+--------+
      | ID                                   | Name   | Status | Server |
      +--------------------------------------+--------+--------+--------+
      | 38047887-61a7-41ea-9b49-27987d5e8bb9 | cirros | ACTIVE |        |
      +--------------------------------------+--------+--------+--------+
