.. _openstack_networking:

Networking
############################################################

OpenStack* Networking allows you to create and attach interface devices
managed by other OpenStack services to networks. Plug-ins can be
implemented to accommodate different networking equipment and software,
providing flexibility to OpenStack architecture and deployment.

Installing and configuring the controller node
----------------------------------------------

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
     *'NEUTRON_DBPASS'* with a suitable password::

		GRANT ALL PRIVILEGES ON neutron.* TO 'neutron'@'localhost' \
		  IDENTIFIED BY 'NEUTRON_DBPASS';
		GRANT ALL PRIVILEGES ON neutron.* TO 'neutron'@'%' \
		  IDENTIFIED BY 'NEUTRON_DBPASS';

   * Exit the database access client.

#. Source the ``admin`` credentials to gain access to admin-only CLI commands::

   $ source admin-openrc.sh

#. To create the service credentials, complete these steps:

   * Create the ``neutron`` user::

      $ openstack user create --domain default --password-prompt neutron
      User Password:
      Repeat User Password:
      +-----------+----------------------------------+
      | Field     | Value                            |
      +-----------+----------------------------------+
      | domain_id | default                          |
      | enabled   | True                             |
      | id        | e51ef98012974e5287d857bc709f89d0 |
      | name      | neutron                          |
      +-----------+----------------------------------+

   * Add the ``admin`` role to the ``neutron`` user::

     $ openstack role add --project service --user neutron admin

     Note: This command provides no output.

   * Create the ``neutron`` service entity::

      $ openstack service create --name neutron \
        --description "OpenStack Networking" network
      +-------------+----------------------------------+
      | Field       | Value                            |
      +-------------+----------------------------------+
      | description | OpenStack Networking             |
      | enabled     | True                             |
      | id          | a56bcd5695b943afba528192acceff01 |
      | name        | neutron                          |
      | type        | network                          |
      +-------------+----------------------------------+

#. Create the Networking service API endpoints:

   * ::

        $ openstack endpoint create --region RegionOne \
          network public http://controller:9696
        +--------------+----------------------------------+
        | Field        | Value                            |
        +--------------+----------------------------------+
        | enabled      | True                             |
        | id           | 61a8b881c8654026be84c12b943e4ee3 |
        | interface    | public                           |
        | region       | RegionOne                        |
        | region_id    | RegionOne                        |
        | service_id   | a56bcd5695b943afba528192acceff01 |
        | service_name | neutron                          |
        | service_type | network                          |
        | url          | http://controller:9696           |
        +--------------+----------------------------------+

   * ::

        $ openstack endpoint create --region RegionOne \
          network internal http://controller:9696
        +--------------+----------------------------------+
        | Field        | Value                            |
        +--------------+----------------------------------+
        | enabled      | True                             |
        | id           | 83bf338752984e1cb5305b9a6a4b4e67 |
        | interface    | internal                         |
        | region       | RegionOne                        |
        | region_id    | RegionOne                        |
        | service_id   | a56bcd5695b943afba528192acceff01 |
        | service_name | neutron                          |
        | service_type | network                          |
        | url          | http://controller:9696           |
        +--------------+----------------------------------+

   * ::

        $ openstack endpoint create --region RegionOne \
          network admin http://controller:9696
        +--------------+----------------------------------+
        | Field        | Value                            |
        +--------------+----------------------------------+
        | enabled      | True                             |
        | id           | 19cfff5a2e9a43298182f8785ea90414 |
        | interface    | admin                            |
        | region       | RegionOne                        |
        | region_id    | RegionOne                        |
        | service_id   | a56bcd5695b943afba528192acceff01 |
        | service_name | neutron                          |
        | service_type | network                          |
        | url          | http://controller:9696           |
        +--------------+----------------------------------+

Installing the Networking components
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Complete the following step to install the Networking components:

#. Install OpenStack networking bundle::

   # swupd bundle-add openstack-network

Configuring the Networking server component
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Complete the following steps to configure the Networking server component:

#. Custom configurations will be located at ``/etc/neutron/``.

   * Create the ``/etc/neutron`` directory::

        # mkdir /etc/neutron

   * Create empty neutron configuration file ``/etc/neutron/neutron.conf``::

        # touch /etc/neutron/neutron.conf

#. Edit the ``/etc/neutron/neutron.conf`` file:

   * In the ``[database]`` section, configure database access. Replace
     *NEUTRON_DBPASS* with the password you chose for the database.::

        [database]
        ...
        connection = mysql://neutron:NEUTRON_DBPASS@controller/neutron

   * In the ``[DEFAULT]`` section, enable the Modular Layer 2 (ML2) plug-in,
     router service, and overlapping IP addresses::

        [DEFAULT]
        ...
        core_plugin = ml2
        service_plugins = router
        allow_overlapping_ips = True

   * In the ``[DEFAULT]`` and ``[oslo_messaging_rabbit]`` sections, configure
     RabbitMQ message queue access. Replace *RABBIT_PASS* with the password you
     chose for the ``openstack`` account in RabbitMQ::

        [DEFAULT]
        ...
        rpc_backend = rabbit

        [oslo_messaging_rabbit]
        ...
        rabbit_host = controller
        rabbit_userid = openstack
        rabbit_password = RABBIT_PASS

   * In the ``[DEFAULT]`` and ``[keystone_authtoken]`` sections, configure
     Identity service access. Replace *NEUTRON_PASS* with the password you
     chose for the ``neutron`` user in the Identity service::

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

   *  In the ``[DEFAULT]`` and ``[nova]`` sections, configure Networking to
      notify Compute of network topology changes. Replace *NOVA_PASS* with the
      password you chose for the ``nova`` user in the Identity service::

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

The ML2 plug-in uses the Linux bridge mechanism to build layer-2 (bridging and
switching) virtual networking infrastructure for instances.

#. Custom configuration will be located at ``/etc/neutron/plugins/ml2``.

   * Create the ``/etc/neutron/plugins/ml2`` directory::

        # mkdir -p /etc/neutron/plugins/ml2

   * Create empty ML2 configuration file
     ``/etc/neutron/plugins/ml2/ml2_conf.ini``::

        # touch /etc/neutron/plugins/ml2/ml2_conf.ini

#. Edit the ``/etc/neutron/plugins/ml2/ml2_conf.ini`` file and complete the
   following actions:

   * In the ``[ml2]`` section, enable flat, VLAN and VXLAN networks::

        [ml2]
        ...
        type_drivers = flat,vlan,vxlan

   * In the ``[ml2]`` section, enable VXLAN project (private) networks::

        [ml2]
        ...
        tenant_network_types = vxlan

   * In the ``[ml2]`` section, enable the Linux bridge and layer-2 population
     mechanisms::

        [ml2]
        ...
        mechanism_drivers = linuxbridge,l2population

   * In the ``[ml2]`` section, enable the port security extension driver::

        [ml2]
        ...
        extension_drivers = port_security

   * In the ``[ml2_type_flat]`` section, configure the public flat provider
     network::

        [ml2_type_flat]
        ...
        flat_networks = public

   * In the [ml2_type_vxlan] section, configure the VXLAN network identifier
     range for private networks::

        [ml2_type_vxlan]
        ...
        vni_ranges = 1:1000

   * In the [securitygroup] section, enable ipset to increase efficiency of
     security group rules::

        [securitygroup]
        ...
        enable_ipset = True

Configure the Linux bridge agent
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Linux bridge agent builds layer-2 (bridging and switching) virtual
networking infrastructure for instances including VXLAN tunnels for private
networks and handles security groups.

#. Custom configuration for Linux bridge agent will be stored in
   ``/etc/neutron/plugins/ml2/linuxbridge_agent.ini``::

    # touch /etc/neutron/plugins/ml2/linuxbridge_agent.ini

#. Edit the ``/etc/neutron/plugins/ml2/linuxbridge_agent.ini`` file and
   complete the following actions:

   * In the ``[linux_bridge]`` section, map the public virtual network to the
     public physical network interface. Replace *PUBLIC_INTERFACE_NAME* with
     the name of the underlying physical public network interface::

        [linux_bridge]
        physical_interface_mappings = public:PUBLIC_INTERFACE_NAME

   * In the ``[vxlan]`` section, enable VXLAN overlay networks, configure the
     IP address of the physical network interface that handles overlay networks,
     and enable layer-2 population. Replace *OVERLAY_INTERFACE_IP_ADDRESS*
     with the IP address of the underlying physical network interface that
     handles overlay networks::

        [vxlan]
        enable_vxlan = True
        local_ip = OVERLAY_INTERFACE_IP_ADDRESS
        l2_population = True

   * In the ``[agent]`` section, enable ARP spoofing protection::

        [agent]
        ...
        prevent_arp_spoofing = True

   * In the ``[securitygroup]`` section, enable security groups and configure
     the Linux bridge iptables firewall driver::

        [securitygroup]
        ...
        enable_security_group = True
        firewall_driver = neutron.agent.linux.iptables_firewall.IptablesFirewallDriver


Configure the layer-3 agent
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Layer-3 (L3) agent provides routing and NAT services for virtual networks.

#. Custom configuration for the Layer-3 agent will be stored in
   ``/etc/neutron/l3_agent.ini``::

    # touch /etc/neutron/l3_agent.ini

#. Edit the ``/etc/neutron/l3_agent.ini`` file and complete the following
   actions:

   * In the ``[DEFAULT]`` section, configure the Linux bridge interface driver
     and external network bridge::

        [DEFAULT]
        ...
        interface_driver = neutron.agent.linux.interface.BridgeInterfaceDriver
        external_network_bridge =

     Note: The ``external_network_bridge`` option intentionally lacks a value to
     enable multiple external networks on a single agent.

Configure the DHCP agent
~~~~~~~~~~~~~~~~~~~~~~~~

The DHCP agent provides DHCP services for virtual networks.

#. Custom configuration for Linux bridge agent will be stored in
   ``/etc/neutron/dhcp_agent.ini``::

    # touch /etc/neutron/dhcp_agent.ini

#. Edit the /etc/neutron/dhcp_agent.ini file and complete the following actions:

   * In the ``[DEFAULT]`` section, configure the Linux bridge interface driver,
     Dnsmasq DHCP driver, and enable isolated metadata so instances on public
     networks can access metadata over the network::

        [DEFAULT]
        ...
        interface_driver = neutron.agent.linux.interface.BridgeInterfaceDriver
        dhcp_driver = neutron.agent.linux.dhcp.Dnsmasq
        enable_isolated_metadata = True

Configure the metadata agent
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The metadata agent provides configuration information such as credentials to
instances.

#.  Custom configuration for the metadata agent will be stored in
    ``/etc/neutron/metadata_agent.ini``::

        # touch /etc/neutron/metadata_agent.ini

#. Edit the ``/etc/neutron/metadata_agent.ini`` file and complete the
   following actions:

   * In the ``[DEFAULT]`` section, configure access parameters. Replace
     *NEUTRON_PASS* with the password you chose for the ``neutron`` user
     in the Identity service::

        [DEFAULT]
        ...
        auth_uri = http://controller:5000
        auth_url = http://controller:35357
        auth_region = RegionOne
        auth_plugin = password
        project_domain_id = default
        user_domain_id = default
        project_name = service
        username = neutron
        password = NEUTRON_PASS

   * In the ``[DEFAULT]`` section, configure the metadata host::

        [DEFAULT]
        ...
        nova_metadata_ip = controller

   * In the ``[DEFAULT]`` section, configure the metadata proxy shared secret
     Replace *METADATA_SECRET* with a suitable secret for the metadata proxy::

        [DEFAULT]
        ...
        metadata_proxy_shared_secret = METADATA_SECRET


Configuring Compute to use Networking
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Edit the ``/etc/nova/nova.conf`` file on the controller node as follows:

   * In the ``[neutron]`` section, configure access parameters, enable the
     metadata proxy, and configure the secret.

     Replace *NEUTRON_PASS* with the password you chose for the ``neutron``
     user in the Identity service.

     Replace *METADATA_SECRET* with the secret you chose for the metadata
     proxy::

        [neutron]
        ...
        url = http://controller:9696
        auth_url = http://controller:35357
        auth_plugin = password
        project_domain_id = default
        user_domain_id = default
        region_name = RegionOne
        project_name = service
        username = neutron
        password = NEUTRON_PASS

        service_metadata_proxy = True
        metadata_proxy_shared_secret = METADATA_SECRET

Finalizing installation
~~~~~~~~~~~~~~~~~~~~~~~~

#. The Networking service initialization scripts expect a symbolic link
   ``/etc/neutron/plugin.ini`` pointing to the ML2 plug-in configuration
   file, ``/etc/neutron/plugins/ml2/ml2_conf.ini``. If this symbolic
   link does not exist, create it using the following command::

   	# ln -s /etc/neutron/plugins/ml2/ml2_conf.ini /etc/neutron/plugin.ini

#. Ensure files have proper ownership by running the following command::

    # systemctl restart update-triggers.target

#. Populate the database::

    # su -s /bin/sh -c "neutron-db-manage --config-file /etc/neutron/neutron.conf \
    --config-file /etc/neutron/plugins/ml2/ml2_conf.ini upgrade head" neutron

#. Restart the Compute services::

    # systemctl restart uwsgi@nova-api.service nova-scheduler.service nova-conductor.service

#. Start the Networking service and configure it to start when the
   system boots::

    # systemctl enable neutron-server.service \
                       neutron-linuxbridge-agent.service \
                       neutron-dhcp-agent.service \
                       neutron-metadata-agent.service \
                       neutron-l3-agent.service
    # systemctl start neutron-server.service \
                      neutron-linuxbridge-agent.service \
                      neutron-dhcp-agent.service \
                      neutron-metadata-agent.service \
                      neutron-l3-agent.service

Install and configure compute node
----------------------------------

Install the components
~~~~~~~~~~~~~~~~~~~~~~

* Install OpenStack networking bundle::

    # swupd bundle-add openstack-network

Configure the common component
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Edit the ``/etc/neutron/neutron.conf`` file and complete the following
   actions:

   * In the ``[DEFAULT]`` and ``[oslo_messaging_rabbit]`` sections, configure
     RabbitMQ message queue access. Replace *RABBIT_PASS* with the password you
     chose for the openstack account in RabbitMQ.::

        [DEFAULT]
        ...
        rpc_backend = rabbit

        [oslo_messaging_rabbit]
        ...
        rabbit_host = controller
        rabbit_userid = openstack
        rabbit_password = RABBIT_PASS

   * In the ``[DEFAULT]`` and ``[keystone_authtoken]`` sections, configure
     Identity service access. Replace *NEUTRON_PASS* with the password you chose
     for the ``neutron`` user in the Identity service::

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

Configure the Linux bridge agent
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Edit the ``/etc/neutron/plugins/ml2/linuxbridge_agent.ini`` file and complete
   the following actions:

   * In the ``[linux_bridge]`` section, map the public virtual network to the
     public physical network interface::

        [linux_bridge]
        physical_interface_mappings = public:PUBLIC_INTERFACE_NAME

   * In the ``[vxlan]`` section, enable VXLAN overlay networks, configure the
     IP address of the physical network interface that handles overlay
     networks, and enable layer-2 population::

        [vxlan]
        enable_vxlan = True
        local_ip = OVERLAY_INTERFACE_IP_ADDRESS
        l2_population = True

   * In the ``[agent]`` section, enable ARP spoofing protection::

        [agent]
        ...
        prevent_arp_spoofing = True

   * In the ``[securitygroup]`` section, enable security groups and configure
     the Linux bridge iptables firewall driver::

        [securitygroup]
        ...
        enable_security_group = True
        firewall_driver = neutron.agent.linux.iptables_firewall.IptablesFirewallDriver

Configure Compute to use Networking
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Edit the ``/etc/nova/nova.conf`` file and complete the following actions:

   * In the ``[neutron]`` section, configure access parameters. Replace
     *NEUTRON_PASS* with the password you chose for the ``neutron`` user in
     the Identity service.::

        [neutron]
        ...
        url = http://controller:9696
        auth_url = http://controller:35357
        auth_plugin = password
        project_domain_id = default
        user_domain_id = default
        region_name = RegionOne
        project_name = service
        username = neutron
        password = NEUTRON_PASS

Finalize installation
~~~~~~~~~~~~~~~~~~~~~

#. Restart the Compute service::

    # systemctl restart nova-compute.service

#. Restart the Linux bridge agent::

    # systemctl enable neutron-linuxbridge-agent.service
    # systemctl restart neutron-linuxbridge-agent.service

Verify Operation
----------------

#. Source the ``admin`` credentials to gain access to admin-only CLI commands::

    $ source admin-openrc.sh

#. List loaded extensions to verify successful launch of the neutron-server
   process::

    $ neutron ext-list
    +-----------------------+-----------------------------------------------+
    | alias                 | name                                          |
    +-----------------------+-----------------------------------------------+
    | dns-integration       | DNS Integration                               |
    | address-scope         | Address scope                                 |
    | ext-gw-mode           | Neutron L3 Configurable external gateway mode |
    | binding               | Port Binding                                  |
    | agent                 | agent                                         |
    | subnet_allocation     | Subnet Allocation                             |
    | l3_agent_scheduler    | L3 Agent Scheduler                            |
    | external-net          | Neutron external network                      |
    | flavors               | Neutron Service Flavors                       |
    | net-mtu               | Network MTU                                   |
    | quotas                | Quota management support                      |
    | l3-ha                 | HA Router extension                           |
    | provider              | Provider Network                              |
    | multi-provider        | Multi Provider Network                        |
    | extraroute            | Neutron Extra Route                           |
    | router                | Neutron L3 Router                             |
    | extra_dhcp_opt        | Neutron Extra DHCP opts                       |
    | security-group        | security-group                                |
    | dhcp_agent_scheduler  | DHCP Agent Scheduler                          |
    | rbac-policies         | RBAC Policies                                 |
    | port-security         | Port Security                                 |
    | allowed-address-pairs | Allowed Address Pairs                         |
    | dvr                   | Distributed Virtual Router                    |
    +-----------------------+-----------------------------------------------+

#. List agents to verify successful launch of the neutron agents::

      $ neutron agent-list
      +--------------------------------------+--------------------+------------+-------+----------------+---------------------------+
      | id                                   | agent_type         | host       | alive | admin_state_up | binary                    |
      +--------------------------------------+--------------------+------------+-------+----------------+---------------------------+
      | 08905043-5010-4b87-bba5-aedb1956e27a | Linux bridge agent | compute1   | :-)   | True           | neutron-linuxbridge-agent |
      | 27eee952-a748-467b-bf71-941e89846a92 | Linux bridge agent | controller | :-)   | True           | neutron-linuxbridge-agent |
      | 830344ff-dc36-4956-84f4-067af667a0dc | L3 agent           | controller | :-)   | True           | neutron-l3-agent          |
      | dd3644c9-1a3a-435a-9282-eb306b4b0391 | DHCP agent         | controller | :-)   | True           | neutron-dhcp-agent        |
      | f49a4b81-afd6-4b3d-b923-66c8f0517099 | Metadata agent     | controller | :-)   | True           | neutron-metadata-agent    |
      +--------------------------------------+--------------------+------------+-------+----------------+---------------------------+

Next topic: :ref:`openstack_orchestration`.
