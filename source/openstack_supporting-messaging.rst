.. _openstack_supporting-messaging:

Message queue
#############

OpenStack* uses a `message queue` to coordinate operations and
status information among services. The message queue service typically
runs on the controller node. OpenStack supports several message queue
services. This guide implements the RabbitMQ message queue service.

Install the message queue service
---------------------------------

#. Install the message queue bundle.::

   # swupd bundle-add message-broker-rabbitmq
   # swupd verify --fix

Configuring the message broker service
--------------------------------------

Complete the following steps to configure the message broker service:

#. Message broker service needs to be able to resolve to itself. Add the
   following line to ``/etc/hosts``.::

    127.0.0.1 controller

#. Start the message broker service and configure it to start when the
   system boots.::

    # systemctl enable rabbitmq-server.service
    # systemctl start rabbitmq-server.service

#. Add the OpenStack user. Replace ``RABBIT_PASS`` with a suitable password.::

    # rabbitmqctl add_user openstack RABBIT_PASS
    Creating user openstack ...
    ...done.


#. Permit configuration, write, and read access for the OpenStack user.::

    # rabbitmqctl set_permissions openstack ".*" ".*" ".*"
    Setting permissions for user "openstack" in vhost "/" ...
    ...done.

Next topic: :ref:`openstack_identity`.