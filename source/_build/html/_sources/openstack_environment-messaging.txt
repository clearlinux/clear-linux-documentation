.. openstack_environment-messaging: 

Message queue
~~~~~~~~~~~~~

OpenStack uses a ``message queue`` to coordinate operations and
status details among services. The message queue service typically
runs on the controller node. OpenStack supports several message queue
services. This guide implements the ``RabbitMQ`` message queue service.

Install the message queue service
---------------------------------

  .. code-block:: console

     # clr_bundle_add message-broker-rabbitmq


Configuring the message broker service
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Complete the following steps to configure the message broker service:

1. Message broker service needs to be able to resolve to itself. Add the
   following line to :file:`/etc/hosts`

  .. code-block:: literal
     
     127.0.0.1 controller


2. Start the message broker service and configure it to start when the
   system boots:

  .. code-block:: console

     # systemctl enable rabbitmq-server.service
     # systemctl start rabbitmq-server.service


3. Add the OpenStack user:

  .. code-block:: console

     # rabbitmqctl add_user openstack RABBIT_PASS
     Creating user openstack ...
     ...done.

  Replace ``RABBIT_PASS`` with a suitable password.


4. Permit configuration, write, and read access for the OpenStack user:

  .. code-block:: console

    # rabbitmqctl set_permissions openstack ".*" ".*" ".*"
    
    Setting permissions for user "openstack" in vhost "/" ...
    ...done.
