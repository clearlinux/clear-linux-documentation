OpenStack* Telemetry - Enable compute service meters
############################################################

Telemetry uses a combination of notifications and an agent to
collect Compute meters. Perform these steps on each compute node.

Configure components
-----------------------------------------------

Edit the ``/etc/ceilometer/ceilometer.conf`` file and complete the following actions:

#. In the ``[DEFAULT]`` and ``[oslo_messaging_rabbit]`` sections, configure RabbitMQ message queue access::

    [DEFAULT]
    ...
    rpc_backend = rabbit

    [oslo_messaging_rabbit]
    ...
    rabbit_host = controller
    rabbit_userid = openstack
    rabbit_password = RABBIT_PASS

   Replace the ``RABBIT_PASS`` with the password you chose for the openstack account in RabbitMQ.

#. In the ``[DEFAULT]`` and ``[keystone_authtoken]`` sections, configure Identity service access::

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

   Replace ``CEILOMETER_PASS`` with the password you chose for the Telemetry service database.

#. In the ``[service_credentials]`` section, configure service credentials::

    [service_credentials]
    ...
    os_auth_url = http://controller:5000/v2.0
    os_username = ceilometer
    os_tenant_name = service
    os_password = CEILOMETER_PASS
    os_endpoint_type = internalURL
    os_region_name = RegionOne

   Replace ``CEILOMETER_PASS`` with the password you chose for the ceilometer user in the Identity service.


Configure Compute to use Telemetry
-----------------------------------------------

#. Edit the ``/etc/nova/nova.conf`` file and configure notifications in the ``[DEFAULT]`` section::

    [DEFAULT]
    ...
    instance_usage_audit = True
    instance_usage_audit_period = hour
    notify_on_state_change = vm_and_task_state
    notification_driver = messagingv2


Finalize the installation
-----------------------------------------------

#. Restart the agent::

    # systemctl enable ceilometer-agent-compute.service
    # systemctl restart ceilometer-agent-compute.service

#. Restart the compute service::

   	# systemctl restart nova-compute.service
