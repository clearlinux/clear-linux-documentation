<<<<<<< HEAD
Block Storage
############################################################
=======
.. _openstack_block_storage:
>>>>>>> staging

Block Storage
########################

The OpenStack Block Storage service (cinder) adds persistent storage to
a virtual machine. Block Storage provides an infrastructure for managing
volumes, and interacts with OpenStack Compute to provide volumes for
instances. The service also enables management of volume snapshots, and
volume types.

Install and configure controller node
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This section describes how to install and configure the Block
Storage service, code-named cinder, on the controller node. This
service requires at least one additional storage node that provides
volumes to instances.

<<<<<<< HEAD
**Create a database:**

#. Use the database access client to connect to the database server as
   the root user::
=======
Prerequisites:
--------------

Before you install and configure the Block Storage service, you
>>>>>>> staging

#. To create the database, complete these steps:

<<<<<<< HEAD
#. Create the cinder database::
   
   	CREATE DATABASE cinder;

#. Grant proper access to the cinder database. Replace ``CINDER_DBPASS``
   with a suitable password::
=======
   * Use the database access client to connect to the database
     server as the ``root`` user::

        $ mysql -u root -p

   * Create the ``cinder`` database::

        CREATE DATABASE cinder;
>>>>>>> staging

   * Grant proper access to the ``cinder`` database::

        GRANT ALL PRIVILEGES ON cinder.* TO 'cinder'@'localhost' \
          IDENTIFIED BY 'CINDER_DBPASS';
        GRANT ALL PRIVILEGES ON cinder.* TO 'cinder'@'%' \
          IDENTIFIED BY 'CINDER_DBPASS';

     Replace ``CINDER_DBPASS`` with a suitable password.

<<<<<<< HEAD
#. Now source the admin credentials to gain access to admin-only CLI
   commands::
=======
   * Exit the database access client.

#. Source the ``admin`` credentials to gain access to admin-only
   CLI commands::
>>>>>>> staging

    $ source admin-openrc.sh

#. To create the service credentials, complete these steps:

<<<<<<< HEAD
   * Create a cinder user::
      
		$ openstack user create --password-prompt cinder
		User Password:
		Repeat User Password: 
		+----------+----------------------------------+
		| Field    | Value                            |
		+----------+----------------------------------+
		| email    | None                             |
		| enabled  | True                             |
		| id       | 881ab2de4f7941e79504a759a83308be |
		| name     | cinder                           |
		| username | cinder                           |
		+----------+----------------------------------+ 

   * Add the admin role to the cinder user::
      
		$ openstack role add --project service --user cinder admin 
		+-------+----------------------------------+
		| Field | Value                            |
		+-------+----------------------------------+
		| id    | cd2cb9a39e874ea69e5d4b896eb16128 |
		| name  | admin                            |
		+-------+----------------------------------+ 

   * Now create the cinder service entities::
      
 		$ openstack service create --name cinder \ 
		--description "OpenStack Block Storage" volume 
		| Field       | Value                            |
		+-------------+----------------------------------+
		| description | OpenStack Block Storage          |
		| enabled     | True                             |
		| id          | 1e494c3e22a24baaafcaf777d4d467eb |
		| name        | cinder                           |
		| type        | volume                           |
		+-------------+----------------------------------+
		$ openstack service create --name cinderv2 
		--description "OpenStack Block Storage" volumev2
		+-------------+----------------------------------+
		| Field       | Value                            |
		+-------------+----------------------------------+
		| description | OpenStack Block Storage          |
		| enabled     | True                             |
		| id          | 16e038e449c94b40868277f1d801edb5 |
		| name        | cinderv2                         |
		| type        | volumev2                         |
		+-------------+----------------------------------+ 

**Create service endpoints:**

The last prerequisite is to create the Block Storage service API endpoints::

	$ openstack endpoint create \ 
	--publicurl http://controller:8776/v2/%\(tenant_id\)s \ 
	--internalurl http://controller:8776/v2/%\(tenant_id\)s \ 
	--adminurl http://controller:8776/v2/%\(tenant_id\)s \ 
	--region RegionOne \ 
	volume
	+--------------+-----------------------------------------+
	|Field         | Value                                   +
	|--------------+-----------------------------------------+
	| adminurl     | http://controller:8776/v2/%(tenant_id)s |
	| id           | d1b7291a2d794e26963b322c7f2a55a4        |
	| internalurl  | http://controller:8776/v2/%(tenant_id)s |
	| publicurl    | http://controller:8776/v2/%(tenant_id)s |
	| region       | RegionOne                               |
	| service_id   | 1e494c3e22a24baaafcaf777d4d467eb        |
	| service_name | cinder                                  |
	| service_type | volume                                  |
	+--------------+-----------------------------------------+
	$ openstack endpoint create \ 
	--publicurl http://controller:8776/v2/%\(tenant_id\)s \ 
	--internalurl http://controller:8776/v2/%\(tenant_id\)s \ 
	--adminurl http://controller:8776/v2/%\(tenant_id\)s \ 
	--region RegionOne \ 
	volumev2
	+--------------+-----------------------------------------+
	| Field        | Value                                   |
	+--------------+-----------------------------------------+
	| adminurl     | http://controller:8776/v2/%(tenant_id)s |
	| id           | 097b4a6fc8ba44b4b10d4822d2d9e076        |
	| internalurl  | http://controller:8776/v2/%(tenant_id)s |
	| publicurl    | http://controller:8776/v2/%(tenant_id)s |
	| region       | RegionOne                               |
	| service_id   | 16e038e449c94b40868277f1d801edb5        |
	| service_name | cinderv2                                |
	| service_type | volumev2                                |
	+--------------+-----------------------------------------+

Installing and configuring Block Storage controller components
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once your prerequisites are finished, you can install and configure
Block Storage controller components:

#. Install OpenStack Block Storage Controller bundle::
   
   	# clr_bundle_add openstack-block-storage-controller
=======
   * Create a ``cinder`` user::

        $ openstack user create --domain default --password-prompt cinder
        User Password:
        Repeat User Password:
        +-----------+----------------------------------+
        | Field     | Value                            |
        +-----------+----------------------------------+
        | domain_id | default                          |
        | enabled   | True                             |
        | id        | bb279f8ffc444637af38811a5e1f0562 |
        | name      | cinder                           |
        +-----------+----------------------------------+

   * Add the ``admin`` role to the ``cinder`` user::

        $ openstack role add --project service --user cinder admin

   * Create the ``cinder`` and ``cinderv2`` service entities::

        $ openstack service create --name cinder \
          --description "OpenStack Block Storage" volume
        +-------------+----------------------------------+
        | Field       | Value                            |
        +-------------+----------------------------------+
        | description | OpenStack Block Storage          |
        | enabled     | True                             |
        | id          | ab3bbbef780845a1a283490d281e7fda |
        | name        | cinder                           |
        | type        | volume                           |
        +-------------+----------------------------------+

        $ openstack service create --name cinderv2 \
          --description "OpenStack Block Storage" volumev2
        +-------------+----------------------------------+
        | Field       | Value                            |
        +-------------+----------------------------------+
        | description | OpenStack Block Storage          |
        | enabled     | True                             |
        | id          | eb9fd245bdbc414695952e93f29fe3ac |
        | name        | cinderv2                         |
        | type        | volumev2                         |
        +-------------+----------------------------------+

   .. note::

      The Block Storage services requires two service entities.

#. Create the Block Storage service API endpoints::

    $ openstack endpoint create --region RegionOne \
      volume public http://controller:8776/v1/%\(tenant_id\)s
    +--------------+-----------------------------------------+
    | Field        | Value                                   |
    +--------------+-----------------------------------------+
    | enabled      | True                                    |
    | id           | 03fa2c90153546c295bf30ca86b1344b        |
    | interface    | public                                  |
    | region       | RegionOne                               |
    | region_id    | RegionOne                               |
    | service_id   | ab3bbbef780845a1a283490d281e7fda        |
    | service_name | cinder                                  |
    | service_type | volume                                  |
    | url          | http://controller:8776/v1/%(tenant_id)s |
    +--------------+-----------------------------------------+

    $ openstack endpoint create --region RegionOne \
      volume internal http://controller:8776/v1/%\(tenant_id\)s
    +--------------+-----------------------------------------+
    | Field        | Value                                   |
    +--------------+-----------------------------------------+
    | enabled      | True                                    |
    | id           | 94f684395d1b41068c70e4ecb11364b2        |
    | interface    | internal                                |
    | region       | RegionOne                               |
    | region_id    | RegionOne                               |
    | service_id   | ab3bbbef780845a1a283490d281e7fda        |
    | service_name | cinder                                  |
    | service_type | volume                                  |
    | url          | http://controller:8776/v1/%(tenant_id)s |
    +--------------+-----------------------------------------+

    $ openstack endpoint create --region RegionOne \
      volume admin http://controller:8776/v1/%\(tenant_id\)s
    +--------------+-----------------------------------------+
    | Field        | Value                                   |
    +--------------+-----------------------------------------+
    | enabled      | True                                    |
    | id           | 4511c28a0f9840c78bacb25f10f62c98        |
    | interface    | admin                                   |
    | region       | RegionOne                               |
    | region_id    | RegionOne                               |
    | service_id   | ab3bbbef780845a1a283490d281e7fda        |
    | service_name | cinder                                  |
    | service_type | volume                                  |
    | url          | http://controller:8776/v1/%(tenant_id)s |
    +--------------+-----------------------------------------+

    $ openstack endpoint create --region RegionOne \
      volumev2 public http://controller:8776/v2/%\(tenant_id\)s
    +--------------+-----------------------------------------+
    | Field        | Value                                   |
    +--------------+-----------------------------------------+
    | enabled      | True                                    |
    | id           | 513e73819e14460fb904163f41ef3759        |
    | interface    | public                                  |
    | region       | RegionOne                               |
    | region_id    | RegionOne                               |
    | service_id   | eb9fd245bdbc414695952e93f29fe3ac        |
    | service_name | cinderv2                                |
    | service_type | volumev2                                |
    | url          | http://controller:8776/v2/%(tenant_id)s |
    +--------------+-----------------------------------------+

    $ openstack endpoint create --region RegionOne \
      volumev2 internal http://controller:8776/v2/%\(tenant_id\)s
    +--------------+-----------------------------------------+
    | Field        | Value                                   |
    +--------------+-----------------------------------------+
    | enabled      | True                                    |
    | id           | 6436a8a23d014cfdb69c586eff146a32        |
    | interface    | internal                                |
    | region       | RegionOne                               |
    | region_id    | RegionOne                               |
    | service_id   | eb9fd245bdbc414695952e93f29fe3ac        |
    | service_name | cinderv2                                |
    | service_type | volumev2                                |
    | url          | http://controller:8776/v2/%(tenant_id)s |
    +--------------+-----------------------------------------+

    $ openstack endpoint create --region RegionOne \
      volumev2 admin http://controller:8776/v2/%\(tenant_id\)s
    +--------------+-----------------------------------------+
    | Field        | Value                                   |
    +--------------+-----------------------------------------+
    | enabled      | True                                    |
    | id           | e652cf84dd334f359ae9b045a2c91d96        |
    | interface    | admin                                   |
    | region       | RegionOne                               |
    | region_id    | RegionOne                               |
    | service_id   | eb9fd245bdbc414695952e93f29fe3ac        |
    | service_name | cinderv2                                |
    | service_type | volumev2                                |
    | url          | http://controller:8776/v2/%(tenant_id)s |
    +--------------+-----------------------------------------+

   .. note::

      The Block Storage services requires endpoints for each service
      entity.

Install and configure components
--------------------------------

#. Install OpenStack Block Storage Controller bundle::

    # swupd bundle-add openstack-block-storage-controller
    # swupd verify --fix
>>>>>>> staging

#. Custom configurations will be located at ``/etc/cinder``.

   * Create ``/etc/cinder`` directory::
<<<<<<< HEAD
      
      	mkdir /etc/cinder
=======

       mkdir /etc/cinder
>>>>>>> staging

   * Create empty cinder configuration file in
     ``/etc/cinder/cinder.conf``::

<<<<<<< HEAD
      	touch /etc/cinder/cinder.conf
=======
       touch /etc/cinder/cinder.conf
>>>>>>> staging

#. Edit the ``/etc/cinder/cinder.conf`` file and complete the following
   actions:

   * In the ``[database]`` section, configure database access. Replace
     ``CINDER_DBPASS`` with the password you chose for the
     database::
<<<<<<< HEAD

      	[database]
      	... 
      	connection=mysql://cinder:CINDER_DBPASS@controller/cinder

=======

       [database]
       ...
       connection=mysql://cinder:CINDER_DBPASS@controller/cinder

>>>>>>> staging
   * In the ``[DEFAULT]`` and ``[oslo_messaging_rabbit]`` section,
     configure RabbitMQ message queue access. Replace ``RABBIT_PASS``
     with the password you chose for the account in
     RabbitMQ::

        [DEFAULT]
        ...
        rpc_backend = rabbit

<<<<<<< HEAD
   * In the ``[DEFAULT]`` and ``[keystone_authtoken]`` sections,
     configure Identity service access. Replace ``CINDER_PASS`` with the
     password you chose for the cinder user in the Identity
     service::
=======
        [oslo_messaging_rabbit]
        ...
        rabbit_host = controller
        rabbit_userid = openstack
        rabbit_password = RABBIT_PASS

   * In the ``[DEFAULT]`` and ``[keystone_authtoken]`` sections, configure
     Identity service access. Replace ``CINDER_PASS`` with the password you
     chose for the ``cinder`` user in the Identity service.::
>>>>>>> staging

        [DEFAULT]
        ...
        auth_strategy = keystone

<<<<<<< HEAD
   * In the ``[DEFAULT]`` section, configure the ``my_ip`` option to
     use the management interface IP address of the controller node::

       	[DEFAULT] ... my_ip = 10.0.0.11

#. Let ``systemd`` set the correct permissions for files in ``/etc/cinder``::
   
   	# systemctl restart update-triggers.target

#. Populate the Block Storage database::
   
   	# su -s /bin/sh -c "cinder-manage db sync" cinder
=======
        [keystone_authtoken]
        ...
        auth_uri = http://controller:5000
        auth_url = http://controller:35357
        auth_plugin = password
        project_domain_id = default
        user_domain_id = default
        project_name = service
        username = cinder
        password = CINDER_PASS

   * In the ``[DEFAULT]`` section, configure the ``my_ip`` option to
     use the management interface IP address of the controller node::

        [DEFAULT]
        ...
        my_ip = 10.0.0.11

#. Populate the Block Storage database::

    # su -s /bin/sh -c "cinder-manage db sync" cinder

Configure Compute to use Block Storage
--------------------------------------

* Edit the ``/etc/nova/nova.conf`` file and add the following
  to it::
>>>>>>> staging

    [cinder]
    os_region_name = RegionOne

<<<<<<< HEAD
To finalize installation, enable and start the Block Storage services::
=======
Finalize installation
---------------------

#. Restart the Compute API service::
>>>>>>> staging

    # systemctl restart uwsgi@nova-api.service

#. Start the Block Storage services and configure them to start when
   the system boots::

    # systemctl enable cinder-api cinder-scheduler
    # systemctl start cinder-api cinder-scheduler

Install and configure a storage node
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

<<<<<<< HEAD
Install the packages::
=======
This section describes how to install and configure storage nodes
for the Block Storage service. For simplicity, this configuration
references one storage node with an empty local block storage device.
The instructions use ``/dev/sdb``, but you can substitute a different
value for your particular node.

The service provisions logical volumes on this device using the
LVM driver and provides them to instances via iSCSI transport.
You can follow these instructions with minor modifications to
horizontally scale your environment with additional storage nodes.
>>>>>>> staging

Prerequisites
-------------

#. Install the openstack block storage bundle::

    # swupd bundle-add openstack-block-storage
    # swupd verify --fix

#. Create the LVM physical volume: ``/dev/sdb1`` If your system uses a
   different device name, adjust these steps accordingly::
<<<<<<< HEAD
=======

    # pvcreate /dev/sdb1
    Physical volume "/dev/sdb1" successfully created
>>>>>>> staging

#. Create the LVM volume group ``cinder-volumes``::

<<<<<<< HEAD
#. Create the LVM volume group ``cinder-volumes``::
   
   	# vgcreate cinder-volumes /dev/sdb1 
   	Volume group "cinder-volumes" successfully created 
=======
    # vgcreate cinder-volumes /dev/sdb1
    Volume group "cinder-volumes" successfully created
>>>>>>> staging

   The Block Storage service creates logical volumes in this volume
   group.

   Only instances can access Block Storage volumes. However, the
   underlying operating system manages the devices associated with the
   volumes. By default, the LVM volume scanning tool scans the ``/dev``
   directory for block storage devices that contain volumes. If projects
   use LVM on their volumes, the scanning tool detects these volumes and
   attempts to cache them which can cause a variety of problems with
   both the underlying operating system and project volumes. You must
   reconfigure LVM to scan only the devices that contain the
   ``cinder-volume`` volume group. 

<<<<<<< HEAD
#. Edit the ``/etc/lvm/lvm.conf`` file
   and complete the following action:

=======
>>>>>>> staging
   * In the ``devices`` section, add a filter that accepts the
     ``/dev/sdb`` device and rejects all other devices::

        devices {
        filter = [ "a/sdb/", "r/.*/"]
        }

Install and configure components
--------------------------------

#. Edit the ``/etc/cinder/cinder.conf`` file and complete the following
   actions:

   * In the ``[database]`` section, configure database access. Replace
     ``CINDER_DBPASS`` with the password you chose for the Block Storage
     database::

      [database]
      ...
      connection = mysql://cinder:CINDER_DBPASS@controller/cinder

   * In the ``[DEFAULT]`` and ``[oslo_messaging_rabbit]`` sections,
<<<<<<< HEAD
     configure *RabbitMQ* message queue access. Replace ``RABBIT_PASS``
     with the password you chose for the openstack account in
     *RabbitMQ*::
=======
     configure ``RabbitMQ`` message queue access. Replace ``RABBIT_PASS``
     with the password you chose for the openstack account in
     ``RabbitMQ``::

        [DEFAULT]
        ...
        rpc_backend = rabbit
>>>>>>> staging

        [oslo_messaging_rabbit]
        ...
        rabbit_host = controller
        rabbit_userid = openstack
        rabbit_password = RABBIT_PASS

   * In the ``[DEFAULT]`` and ``[keystone_authtoken]`` sections,
     configure Identity service access. Replace ``CINDER_PASS`` with the
     password you chose for the cinder user in the Identity service::
<<<<<<< HEAD
=======

        [DEFAULT]
        ...
        auth_strategy = keystone
>>>>>>> staging

        [keystone_authtoken]
        ...
        auth_uri = http://controller:5000
        auth_url = http://controller:35357
        auth_plugin = password
        project_domain_id = default
        user_domain_id = default
        project_name = service
        username = cinder
        password = CINDER_PASS

   * In the ``[DEFAULT]`` section, configure the ``my_ip`` option.
<<<<<<< HEAD
     Replace *MANAGEMENT_INTERFACE_IP_ADDRESS* with the IP address
     of the management network interface on your storage node,
     typically 10.0.0.41 for the first node in the example
     architecture::
=======
     Replace ``MANAGEMENT_INTERFACE_IP_ADDRESS`` with the IP address
     of the management network interface on your storage node,
     typically 10.0.0.41 for the first node in the example
     architecture::

        [DEFAULT]
        ...
        my_ip = MANAGEMENT_INTERFACE_IP_ADDRESS
>>>>>>> staging

   * In the ``[lvm]`` section, configure the LVM back end with the LVM
     driver, ``cinder-volumes`` volume group, iSCSI protocol, and
     appropriate iSCSI service::

<<<<<<< HEAD
   * In the ``[lvm]`` section, configure the LVM back end with the LVM
     driver, ``cinder-volumes`` volume group, iSCSI protocol, and
     appropriate iSCSI service::
=======
        [lvm]
        ...
        volume_driver = cinder.volume.drivers.lvm.LVMVolumeDriver
        volume_group = cinder-volumes
        iscsi_protocol = iscsi
        iscsi_helper = tgtadm

   * In the ``[DEFAULT]`` section, enable the LVM back end::
>>>>>>> staging

        [DEFAULT]
        ...
        enabled_backends = lvm

<<<<<<< HEAD
   * In the ``[DEFAULT]`` section, enable the LVM back end::
      
		[DEFAULT] 
		... 
		enabled_backends = lvm

   * In the ``[DEFAULT]`` section, configure the location of the Image
     service::
=======
   * In the ``[DEFAULT]`` section, configure the location of the Image
     service::

        [DEFAULT]
        ...
        glance_host = controller

#. Let systemd set the correct permissions for files in ``/etc/cinder``::

    # systemctl restart update-triggers.target
>>>>>>> staging

Finalize installation
---------------------

<<<<<<< HEAD
#. Let systemd set the correct permissions for files in ``/etc/cinder``::
   
   	# systemctl restart update-triggers.target

Finalizing installation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Restart the Block Storage volume service including its dependencies::
=======
#. Start the Block Storage volume service including its dependencies
   and configure them to start when the system boots::

    # systemctl enable iscsid tgtd cinder-volume
    # systemctl start iscsid tgtd cinder-volume

Configuring a compute node to use Block Storage
-----------------------------------------------

#. Perform the following steps to enable a compute node to work with
   block storage::
>>>>>>> staging

    # systemctl enable iscsid
    # systemctl start iscsi-gen-initiatorname iscsid

Verify operation
~~~~~~~~~~~~~~~~
Verify operation of the Block Storage service.

<<<<<<< HEAD
Perform the following steps to enable a compute node to work with block
storage::
=======
#. Source the ``admin`` credentials to gain access to
   admin-only CLI commands::

    $ source admin-openrc.sh
>>>>>>> staging

#. List service components to verify successful launch of each process::

    $ cinder service-list
    +------------------+------------+------+---------+-------+----------------------------+-----------------+
    |      Binary      |    Host    | Zone |  Status | State |         Updated_at         | Disabled Reason |
    +------------------+------------+------+---------+-------+----------------------------+-----------------+
    | cinder-scheduler | controller | nova | enabled |   up  | 2014-10-18T01:30:54.000000 |       None      |
    | cinder-volume    | block1@lvm | nova | enabled |   up  | 2014-10-18T01:30:57.000000 |       None      |
    +------------------+------------+------+---------+-------+----------------------------+-----------------+

Next topic: :ref:`openstack_dashboard`.
