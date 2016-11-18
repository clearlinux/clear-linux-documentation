OpenStack* Telemetry - Enable image service meters
############################################################

Telemetry uses notifications to collect Image service meters.
Perform these steps on the controller node.


Configure the Image service to use Telemetry
-----------------------------------------------

Edit the ``/etc/glance/glance-api.conf`` and ``/etc/glance/glance-registry.conf``
files and complete the following actions:

#. In the ``[DEFAULT]`` section, configure notifications and RabbitMQ message broker access::

    [DEFAULT]
    ...
    notification_driver = messagingv2
    rpc_backend = rabbit

    [oslo_messaging_rabbit]
    ...
    rabbit_host = controller
    rabbit_userid = openstack
    rabbit_password = RABBIT_PASS

   Replace the ``RABBIT_PASS`` with the password you chose for the openstack account in RabbitMQ.

Finalize the installation
----------------------------

#. Restart the image service::

   	# systemctl restart glance-registry.service
   	# systemctl restart glance-api.service
