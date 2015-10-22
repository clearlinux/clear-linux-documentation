OpenStack block storage
############################################################

Clear Linux* OS for Intel® Architecture can be used with the
OpenStack Block Storage service (cinder) to add persistent storage
options to a virtual machine. Block Storage provides an infrastructure
for managing volumes and interacting with OpenStack Compute (nova) to
provide volumes for specific instances. These volumes can be easily
managed (types and snapshots) under Block Storage. Here's how to get
OpenStack Block Storage working with Clear Linux OS for Intel
Architecture:

Installing and configuring the controller node
----------------------------------------------------

The first step is to install and configure the Block Storage service,
code-named cinder, on the controller node. This service requires at
least one additional storage node that provides volumes to instances.

Prerequisites:
~~~~~~~~~~~~~~~~~~

Before installing and configuring the Block Storage service, create a
database, service credentials, and an API endpoint. To create the
database, complete these steps:

**Create a database:**

#. Use the database access client to connect to the database server as
   the root user:

   .. code:: text

   	$ mysql -u root -p

#. Create the cinder database.
   
   .. code:: text

   	CREATE DATABASE cinder;

#. Grant proper access to the cinder database. Replace ``CINDER_DBPASS``
   with a suitable password.

   .. code:: text

   	GRANT ALL PRIVILEGES ON cinder.* TO 'cinder'@'localhost' \ 
   	IDENTIFIED BY 'CINDER_DBPASS'; 
   	GRANT ALL PRIVILEGES ON cinder.* TO 'cinder'@'%' \ 
   	IDENTIFIED BY 'CINDER_DBPASS'; 

#. Exit the database access client.

**Create service credentials:**

#. Now source the admin credentials to gain access to admin-only CLI
   commands:

   .. code:: text

   	$ source admin-openrc.sh

#. To create the service credentials, complete these steps:

   #. Create a cinder user:
      
      .. code:: text

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

   #. Add the admin role to the cinder user:
      
      .. code:: text

		$ openstack role add --project service --user cinder admin 
		+-------+----------------------------------+
		| Field | Value                            |
		+-------+----------------------------------+
		| id    | cd2cb9a39e874ea69e5d4b896eb16128 |
		| name  | admin                            |
		+-------+----------------------------------+ 

   #. Now create the cinder service entities:
      
      .. code:: text

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

The last prerequisite is to create the Block Storage service API endpoints:

.. code:: text

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

#. Install OpenStack Block Storage Controller bundle:
   
   .. code:: text

   	# clr_bundle_add openstack-block-storage-controller

#. Custom configurations will be located at ``/etc/cinder``.

   #. Create ``/etc/cinder`` directory.
      
      .. code:: text

      	mkdir /etc/cinder

   #. Create empty cinder configuration file in
      ``/etc/cinder/cinder.conf``

      .. code:: text

      	touch /etc/cinder/cinder.conf

#. Edit the ``/etc/cinder/cinder.conf`` file and complete the following
   actions:

   #. In the ``[database]`` section, configure database access. Replace
      ``CINDER_DBPASS`` with the password you chose for the
      database.

      .. code:: text

      	[database]
      	... 
      	connection=mysql://cinder:CINDER_DBPASS@controller/cinder

   #. In the ``[DEFAULT]`` and ``[oslo_messaging_rabbit]`` section,
      configure RabbitMQ message queue access. Replace ``RABBIT_PASS``
      with the password you chose for the account in
      RabbitMQ.

      .. code:: text

		[DEFAULT] 
		... 
		rpc_backend = rabbit 
		... 
		[oslo_messaging_rabbit] 
		rabbit_host = controller 
		rabbit_userid = openstack 
		rabbit_password = RABBIT_PASS

   #. In the ``[DEFAULT]`` and ``[keystone_authtoken]`` sections,
      configure Identity service access. Replace ``CINDER_PASS`` with the
      password you chose for the cinder user in the Identity
      service.

      .. code:: text

		[DEFAULT] 
		... 
		auth_strategy = keystone 
		... 
		[keystone_authtoken] 
		auth_uri = http://controller:5000/v2.0 
		admin_tenant_name = service 
		admin_user = cinder 
		admin_password = CINDER_PASS

   #. In the ``[DEFAULT]`` section, configure the ``my_ip`` option to
      use the management interface IP address of the controller node:

      .. code:: text

      	[DEFAULT] ... my_ip = 10.0.0.11

#. Let ``systemd`` set the correct permissions for files in ``/etc/cinder``.
   
   .. code:: text

   	# systemctl restart update-triggers.target

#. Populate the Block Storage database:
   
   .. code:: text

   	# su -s /bin/sh -c "cinder-manage db sync" cinder

Finalizing installation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To finalize installation, enable and start the Block Storage services:

.. code:: text

	# systemctl enable cinder-api cinder-scheduler 
	# systemctl start cinder-api cinder-scheduler 

Installing and configuring a storage node
----------------------------------------------

This section describes how to install and configure storage nodes for
the Block Storage service. For simplicity, this configuration references
one storage node with an empty local block storage device ``/dev/sdb``
(for physical device) or ``/dev/vda`` (for virtual machine) that
contains a suitable partition table with one partition ``/dev/sdb1``
occupying the entire device. The service provisions logical volumes on
this device using the LVM driver and provides them to instances via
iSCSI transport. You can follow these instructions with minor
modifications to horizontally scale your environment with additional
storage nodes.

Install Block Storage volume components
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Install the packages:

.. code:: text

	# clr_bundle_add openstack-block-storage

**Prerequisites:**

You must configure the storage node before installing and configuring
the volume service on it. Similar to the controller node, the storage
node contains one network interface on the management network. The
storage node also needs an empty block storage device of suitable size
for your environment.

#. Create the LVM physical volume: ``/dev/sdb1`` If your system uses a
   different device name, adjust these steps accordingly.

   .. code:: text

   	# pvcreate /dev/sdb1 
	Physical volume "/dev/sdb1" successfully created

#. Create the LVM volume group ``cinder-volumes``:
   
   .. code:: text

   	# vgcreate cinder-volumes /dev/sdb1 
   	Volume group "cinder-volumes" successfully created 

   The Block Storage service creates logical volumes in this volume
   group.

#. Only instances can access Block Storage volumes. However, the
   underlying operating system manages the devices associated with the
   volumes. By default, the LVM volume scanning tool scans the ``/dev``
   directory for block storage devices that contain volumes. If projects
   use LVM on their volumes, the scanning tool detects these volumes and
   attempts to cache them which can cause a variety of problems with
   both the underlying operating system and project volumes. You must
   reconfigure LVM to scan only the devices that contain the
   ``cinder-volume`` volume group. Edit the ``/etc/lvm/lvm.conf`` file
   and complete the following action:

   #. In the ``devices`` section, add a filter that accepts the
      ``/dev/sdb`` device and rejects all other devices:

      .. code:: text

      	devices { 
      	filter = [ "a/sdb/", "r/.*/"] 
      	}

**Configure Block Storage volume components:**

#. Edit the ``/etc/cinder/cinder.conf`` file and complete the following
   actions:

   #. In the ``[database]`` section, configure database access. Replace
      ``CINDER_DBPASS`` with the password you chose for the Block Storage
      database.

      .. code:: text

      [database] 
      ... 
      connection = mysql://cinder:CINDER_DBPASS@controller/cinder

   #. In the ``[DEFAULT]`` and ``[oslo_messaging_rabbit]`` sections,
      configure *RabbitMQ* message queue access. Replace ``RABBIT_PASS``
      with the password you chose for the openstack account in
      *RabbitMQ*.

      .. code:: text

      	[DEFAULT] 
		... 
		rpc_backend = rabbit 
		[oslo_messaging_rabbit] 
		... 
		rabbit_host = controller 
		rabbit_userid = openstack 
		rabbit_password = RABBIT_PASS

   #. In the ``[DEFAULT]`` and ``[keystone_authtoken]`` sections,
      configure Identity service access. Replace ``CINDER_PASS`` with the
      password you chose for the cinder user in the Identity service.

      .. code:: text

		[DEFAULT] 
		... 
		auth_strategy = keystone 
		[keystone_authtoken] 
		... 
		auth_uri = http://controller:5000 
		identity_uri = http://controller:35357 
		admin_tenant_name = service 
		admin_user = cinder 
		admin_password = CINDER_PASS

   #. In the ``[DEFAULT]`` section, configure the ``my_ip`` option.
      Replace *MANAGEMENT_INTERFACE_IP_ADDRESS* with the IP address
      of the management network interface on your storage node,
      typically 10.0.0.41 for the first node in the example
      architecture.

      .. code:: text

		[DEFAULT] 
		... 
		my_ip = MANAGEMENT_INTERFACE_IP_ADDRESS

   #. In the ``[lvm]`` section, configure the LVM back end with the LVM
      driver, ``cinder-volumes`` volume group, iSCSI protocol, and
      appropriate iSCSI service.

      .. code:: text

		[lvm] 
		... 
		volume_driver = cinder.volume.drivers.lvm.LVMVolumeDriver 
		volume_group = cinder-volumes 
		iscsi_protocol = iscsi 
		iscsi_helper = tgtadm

   #. In the ``[DEFAULT]`` section, enable the LVM back end:
      
      .. code:: text

		[DEFAULT] 
		... 
		enabled_backends = lvm

   #. In the ``[DEFAULT]`` section, configure the location of the Image
      service:

      .. code:: text

		[DEFAULT] 
		... 
		glance_host = controller

#. Let systemd set the correct permissions for files in /etc/cinder
   
   .. code:: text

   	# systemctl restart update-triggers.target

Finalizing installation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Restart the Block Storage volume service including its dependencies:

.. code:: text

	# systemctl enable iscsid tgtd cinder-volume 
	# systemctl start iscsid tgtd cinder-volume

Configuring a compute node to use Block Storage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Perform the following steps to enable a compute node to work with block
storage:

.. code:: text

	# systemctl enable iscsid 
	# systemctl start iscsi-gen-initiatorname 
	# systemctl start iscsid 


