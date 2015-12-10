OpenStack* Object Storage
#########################

The OpenStack Object Storage services (swift) work together to provide
object storage and retrieval through a REST API. Your environment must
at least include the Identity service (keystone) prior to deploying Object Storage.

OpenStack Object Storage
------------------------

The OpenStack Object Storage is a multi-tenant object storage system.
It is highly scalable and can manage large amounts of unstructured data
at low cost through a RESTful HTTP API.

It includes the following components:

**Proxy servers (swift-proxy-server)**
 Accepts OpenStack Object Storage API and raw HTTP requests to upload files, modify metadata,
 and create containers. It also serves file or container listings to web browsers. To improve performance,
 the proxy server can use an optional cache that is usually deployed with memcache.

**Account servers (swift-account-server)**
 Manages accounts defined with Object Storage.

**Container servers (swift-container-server)**
 Manages the mapping of containers or folders, within Object Storage.

**Object servers (swift-object-server)**
 Manages actual objects, such as files, on the storage nodes.

**Various periodic processes**
 Performs housekeeping tasks on the large data store. The replication
 services ensure consistency and availability through the cluster.
 Other periodic processes include auditors, updaters, and reapers.

**WSGI middleware**
 Handles authentication and is usually OpenStack Identity.

**swift client**
 Enables users to submit commands to the REST API through a
 command-line client authorized as either a admin user, reseller user, or swift user.

**swift-init**
 Script that initializes the building of the ring file, takes daemon
 names as parameter and offers commands. Documented in
 http://docs.openstack.org/developer/swift/admin_guide.html#managing-services.

**swift-recon**
 A cli tool used to retrieve various metrics and telemetry information
 about a cluster that has been collected by the swift-recon middleware.

**swift-ring-builder**
 Storage ring build and rebalance utility. Documented in
 http://docs.openstack.org/developer/swift/admin_guide.html#managing-the-rings.

Install and configure the controller node
-----------------------------------------

This section describes how to install and configure the proxy service
that handles requests for the account, container, and object services
operating on the storage nodes. For simplicity, this guide installs and
configures the proxy service on the controller node. However, you can
run the proxy service on any node with network connectivity to the
storage nodes. Additionally, you can install and configure the proxy
service on multiple nodes to increase performance and redundancy.

To configure prerequisites
~~~~~~~~~~~~~~~~~~~~~~~~~~

The proxy service relies on an authentication and authorization
mechanism such as the Identity service. However, unlike other services,
it also offers an internal mechanism that allows it to operate without
any other OpenStack* services. However, for simplicity, this guide
references the Identity service. Before you configure the Object Storage
service, you must create service credentials and an API endpoint.

#. Source the ``admin`` credentials to gain access to admin-only CLI
   commands::

      $ source admin-openrc.sh

#. To create the Identity service credentials, complete these steps:

   * Create the ``swift`` user::

         $ openstack user create --domain default --password-prompt swift
	 User Password:
	 Repeat User Password:
	 +-----------+----------------------------------+
	 | Field     | Value                            |
	 +-----------+----------------------------------+
	 | domain_id | default                          |
	 | enabled   | True                             |
	 | id        | d535e5cbd2b74ac7bfb97db9cced3ed6 |
	 | name      | swift                            |
	 +-----------+----------------------------------+

   * Add the admin role to the ``swift`` user::

         $ openstack role add --project service --user swift admin

   * Create the ``swift`` service entity::

         $ openstack service create --name swift \
	   --description "OpenStack Object Storage" object-store
	   +-------------+----------------------------------+
	   | Field       | Value                            |
	   +-------------+----------------------------------+
	   | description | OpenStack Object Storage         |
	   | enabled     | True                             |
	   | id          | 75ef509da2c340499d454ae96a2c5c34 |
	   | name        | swift                            |
	   | type        | object-store                     |
	   +-------------+----------------------------------+

#. Create the Object Storage service API endpoint::

         $ openstack endpoint create --region RegionOne \
	   object-store public http://controller:8080/v1/AUTH_%\(tenant_id\)s
	   +--------------+----------------------------------------------+
	   | Field        | Value                                        |
	   +--------------+----------------------------------------------+
	   | enabled      | True                                         |
	   | id           | 12bfd36f26694c97813f665707114e0d             |
	   | interface    | public                                       |
	   | region       | RegionOne                                    |
	   | region_id    | RegionOne                                    |
	   | service_id   | 75ef509da2c340499d454ae96a2c5c34             |
	   | service_name | swift                                        |
	   | service_type | object-store                                 |
	   | url          | http://controller:8080/v1/AUTH_%(tenant_id)s |
	   +--------------+----------------------------------------------+

	 $ openstack endpoint create --region RegionOne \
	   object-store internal http://controller:8080/v1/AUTH_%\(tenant_id\)s
	   +--------------+----------------------------------------------+
	   | Field        | Value                                        |
	   +--------------+----------------------------------------------+
	   | enabled      | True                                         |
	   | id           | 7a36bee6733a4b5590d74d3080ee6789             |
	   | interface    | internal                                     |
	   | region       | RegionOne                                    |
	   | region_id    | RegionOne                                    |
	   | service_id   | 75ef509da2c340499d454ae96a2c5c34             |
	   | service_name | swift                                        |
	   | service_type | object-store                                 |
	   | url          | http://controller:8080/v1/AUTH_%(tenant_id)s |
	   +--------------+----------------------------------------------+

	 $ openstack endpoint create --region RegionOne \
	   object-store admin http://controller:8080/v1
	   +--------------+----------------------------------+
	   | Field        | Value                            |
	   +--------------+----------------------------------+
	   | enabled      | True                             |
	   | id           | ebb72cd6851d4defabc0b9d71cdca69b |
	   | interface    | admin                            |
	   | region       | RegionOne                        |
	   | region_id    | RegionOne                        |
	   | service_id   | 75ef509da2c340499d454ae96a2c5c34 |
	   | service_name | swift                            |
	   | service_type | object-store                     |
	   | url          | http://controller:8080/v1        |
	   +--------------+----------------------------------+

To install and configure the controller node components
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Install OpenStack Object Storage bundle::

      # swupd bundle-add openstack-object-storage
      # swupd verify --fix

#. Create the directory ``/etc/swift`` if does not exist::

      # mkdir /etc/swift

#. Copy the sample proxy-server config file to the configuration
   directory::

      # cp /usr/share/defaults/swift/proxy-server.conf /etc/swift

#. Edit the ``/etc/swift/proxy-server.conf`` file and complete the
   following actions:

   * In the ``[pipeline:main]`` section, enable the appropriate
     modules::

         [pipeline:main]
         pipeline = catch_errors gatekeeper healthcheck proxy-logging cache container_sync bulk ratelimit authtoken keystoneauth container-quotas account-quotas slo dlo versioned_writes proxy-logging proxy-server

   * In the ``[app:proxy-server]`` section, enable automatic account
     creation::

         [app:proxy-server]
         ...
         account_autocreate = true

   * In the ``[filter:keystoneauth]`` section, configure the operator
     roles::

         [filter:keystoneauth]
         use = egg:swift#keystoneauth
         ...
         operator_roles = admin,user

   * In the ``[filter:authtoken]`` section, configure Identity service
     access. Replace *SWIFT_PASS* with the password you chose for the
     ``swift`` user in the Identity service::

         [filter:authtoken]
         paste.filter_factory = keystonemiddleware.auth_token:filter_factory
         ...
         auth_uri = http://controller:5000
         auth_url = http://controller:35357
         auth_plugin = password
         project_domain_id = default
         user_domain_id = default
         project_name = service
         username = swift
         password = SWIFT_PASS
         delay_auth_decision = true

   * In the ``[filter:cache]`` section, configure the ``memcached``
     location::

         [filter:cache]
         ...
         memcache_servers = 127.0.0.1:11211

Install and configure the storage nodes
---------------------------------------

This section describes how to install and configure storage nodes that
operate the account, container, and object services. For simplicity,
this configuration references two storage nodes, each containing two
empty local block storage devices. Each of the devices, ``/dev/sdb`` and
``/dev/sdc``, must contain a suitable partition table with one partition
occupying the entire device.

Although the Object Storage service
supports any file system with extended attributes (xattr), testing and
benchmarking indicate the best performance and reliability on XFS.

To configure prerequisites
~~~~~~~~~~~~~~~~~~~~~~~~~~

You must configure each storage node before you install and configure
the Object Storage service on it. Similar to the controller node, each
storage node contains one network interface on the management network.
Optionally, each storage node can contain a second network interface on
a separate network for replication.

#. Configure unique items on the first storage node:

   * Configure the management interface::

         IP address: 10.0.0.51
         Network mask: 255.255.255.0 (or /24)
         Default gateway: 10.0.0.1

   * Set the hostname of the node to ``object1``.

#. Configure unique items on the second storage node:

   * Configure the management interface::

         IP address: 10.0.0.52
         Network mask: 255.255.255.0 (or /24)
         Default gateway: 10.0.0.1

   * Set the hostname of the node to ``object2``.

#. Configure shared items on both storage nodes:

   * Copy the contents of ``/etc/hosts`` file  from ``controller`` node to ``storage`` nodes and add the
     following ::

         # object1
         10.0.0.51 object1
         # object2
         10.0.0.52 object2

#. Install the OpenStack Object Storage bundle::

         # swupd bundle-add openstack-object-storage
         # swupd verify --fix

#. Format the ``/dev/sdb1`` and ``/dev/sdc1`` partitions as XFS::

         # mkfs.xfs /dev/sdb1
         # mkfs.xfs /dev/sdc1

#. Create the mount point directory structure::

         # mkdir -p /srv/node/sdb1
         # mkdir -p /srv/node/sdc1

#.  Edit the ``/etc/fstab`` file and add the following to it::

         /dev/sdb1 /srv/node/sdb1 xfs noatime,nodiratime,nobarrier,logbufs=8 0 2
         /dev/sdc1 /srv/node/sdc1 xfs noatime,nodiratime,nobarrier,logbufs=8 0 2

#. Mount the devices::

         # mount /srv/node/sdb1
         # mount /srv/node/sdc1

#. Edit the ``/etc/rsyncd.conf`` file and add the following to it::

      uid = swift
      gid = swift
      log file = /var/log/rsyncd.log
      pid file = /var/run/rsyncd.pid
      address = MANAGEMENT_INTERFACE_IP_ADDRESS

      [account]
      max connections = 2
      path = /srv/node/
      read only = false
      lock file = /var/lock/account.lock

      [container]
      max connections = 2
      path = /srv/node/
      read only = false
      lock file = /var/lock/container.lock

      [object]
      max connections = 2
      path = /srv/node/
      read only = false
      lock file = /var/lock/object.lock

   Replace *MANAGEMENT_INTERFACE_IP_ADDRESS* with the IP address of
   the management network on the storage node.

   Note: The ``rsync`` service requires no authentication, so consider
   running it on a private network.

#. Start the ``rsyncd`` service and configure it to start when the
   system boots::

      # systemctl enable rsyncd.service
      # systemctl start rsyncd.service

Install and configure storage node components
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Copy the accounting, container, object, container-reconciler, and
   object-expirer service configuration files to the configuration
   directory::

      # cp /usr/share/defaults/swift/account-server.conf /etc/swift
      # cp /usr/share/defaults/swift/container-server.conf /etc/swift
      # cp /usr/share/defaults/swift/object-server.conf /etc/swift
      # cp /usr/share/defaults/swift/container-reconciler.conf /etc/swift
      # cp /usr/share/defaults/swift/object-expirer.conf /etc/swift

#. Edit the ``/etc/swift/account-server.conf`` file and complete the
   following actions:

   * In the ``[DEFAULT]`` section, configure the bind IP address and
     mount point directory::

         [DEFAULT]
         ...
         bind_ip = MANAGEMENT_INTERFACE_IP_ADDRESS
         devices = /srv/node

     Replace *MANAGEMENT_INTERFACE_IP_ADDRESS* with the IP
     address of the management network on the storage node.

   * In the ``[pipeline:main]`` section, enable the appropriate
     modules::

         [pipeline:main]
         pipeline = healthcheck recon account-server

   * In the ``[filter:recon]`` section, configure the ``recon`` (metrics)
     cache directory::

         [filter:recon]
         ...
         recon_cache_path = /var/cache/swift

#. Edit the ``/etc/swift/container-server.conf`` file and complete the
   following actions:

   * In the ``[DEFAULT]`` section, configure the bind IP address and
     mount point directory::

         [DEFAULT]
         ...
         bind_ip = MANAGEMENT_INTERFACE_IP_ADDRESS
         devices = /srv/node

     Replace *MANAGEMENT_INTERFACE_IP_ADDRESS* with the IP
     address of the management network on the storage node.

   *   In the ``[pipeline:main]`` section, enable the appropriate modules::

         [pipeline:main]
         pipeline = healthcheck recon container-server

   * In the ``[filter:recon]`` section, configure the recon (metrics)
     cache directory::

         [filter:recon]
         ...
         recon_cache_path = /var/cache/swift

#. Edit the ``/etc/swift/object-server.conf`` file and complete the
   following actions:

   * In the ``[DEFAULT]`` section, configure the bind IP address and
     mount point directory::

         [DEFAULT]
         ...
         bind_ip = MANAGEMENT_INTERFACE_IP_ADDRESS
         devices = /srv/node

     Replace *MANAGEMENT_INTERFACE_IP_ADDRESS* with the IP
     address of the management network on the storage node.

   * In the ``[pipeline:main]`` section, enable the appropriate
     modules::

         [pipeline:main]
         pipeline = healthcheck recon object-server

   * In the ``[filter:recon]`` section, configure the ``recon`` (metrics)
     cache and lock directories::

         [filter:recon]
         ...
         recon_cache_path = /var/cache/swift
         recon_lock_path = /var/lock

#. Ensure proper ownership of the mount point directory structure::

   # systemctl restart update-triggers.target

About Creating initial rings
----------------------------

Before starting the Object Storage services, you must create the initial
account, container, and object rings. The ring builder creates
configuration files that each node uses to determine and deploy the
storage architecture. For simplicity, this guide uses one region and
zone with 2^10 (1024) maximum partitions, 3 replicas of each object, and
1 hour minimum time between moving a partition more than once. For
Object Storage, a partition indicates a directory on a storage device
rather than a conventional partition table.

Create Account Ring
-------------------

The account server uses the account ring to maintain lists of
containers.

To create the ring
~~~~~~~~~~~~~~~~~~

#. Create the base ``account.builder`` file::

      # swift-ring-builder account.builder create 10 3 1

#. Add each storage node to the ring::

      # swift-ring-builder account.builder \
      add --region 1 --zone 1 --ip STORAGE_NODE_MANAGEMENT_INTERFACE_IP_ADDRESS --port 6002 \
      --device DEVICE_NAME --weight DEVICE_WEIGHT

   Replace *STORAGE_NODE_MANAGEMENT_INTERFACE_IP_ADDRESS* with the
   IP address of the management network on the storage node. Replace
   *DEVICE_NAME* with a storage device name on the same storage node.
   For example, using the first storage node with the ``/dev/sdb1`` storage
   device and weight of 100::

      # swift-ring-builder account.builder add \
        --region 1 --zone 1 --ip 10.0.0.51 --port 6002 --device sdb --weight 100

   Repeat this command for each storage device on each storage node. In
   the example architecture, use the command in four variations::

      # swift-ring-builder account.builder add \
        --region 1 --zone 1 --ip 10.0.0.51 --port 6002 --device sdb --weight 100
      Device d0r1z1-10.0.0.51:6002R10.0.0.51:6002/sdb_"" with 100.0 weight got id 0
      # swift-ring-builder account.builder add \
        --region 1 --zone 2 --ip 10.0.0.51 --port 6002 --device sdc --weight 100
      Device d1r1z2-10.0.0.51:6002R10.0.0.51:6002/sdc_"" with 100.0 weight got id 1
      # swift-ring-builder account.builder add \
        --region 1 --zone 3 --ip 10.0.0.52 --port 6002 --device sdb --weight 100
      Device d2r1z3-10.0.0.52:6002R10.0.0.52:6002/sdb_"" with 100.0 weight got id 2
      # swift-ring-builder account.builder add \
        --region 1 --zone 4 --ip 10.0.0.52 --port 6002 --device sdc --weight 100
      Device d3r1z4-10.0.0.52:6002R10.0.0.52:6002/sdc_"" with 100.0 weight got id 3

#. Verify the ring contents::

      # swift-ring-builder account.builder
      account.builder, build version 4
      1024 partitions, 3.000000 replicas, 1 regions, 4 zones, 4 devices, 100.00 balance, 0.00 dispersion
      The minimum number of hours before a partition can be reassigned is 1
      The overload factor is 0.00% (0.000000)
      Devices:    id  region  zone      ip address  port  replication ip  replication port      name weight partitions balance meta
                   0       1     1       10.0.0.51  6002       10.0.0.51              6002      sdb  100.00          0 -100.00
                   1       1     2       10.0.0.51  6002       10.0.0.51              6002      sdc  100.00          0 -100.00
                   2       1     3       10.0.0.52  6002       10.0.0.52              6002      sdb  100.00          0 -100.00
                   3       1     4       10.0.0.52  6002       10.0.0.52              6002      sdc  100.00          0 -100.00

#. Rebalance the ring::

      # swift-ring-builder account.builder rebalance
      Reassigned 1024 (100.00%) partitions. Balance is now 0.00. Dispersion is now 0.00

Create Container Ring
---------------------

The container server uses the container ring to maintain lists of
objects. However, it does not track object locations.

To create the ring
~~~~~~~~~~~~~~~~~~

#. Create the base ``container.builder`` file::

      # swift-ring-builder container.builder create 10 3 1

#. Add each storage node to the ring::

      # swift-ring-builder container.builder \
          add --region 1 --zone 1 --ip STORAGE_NODE_MANAGEMENT_INTERFACE_IP_ADDRESS --port 6001 \
	  --device DEVICE_NAME --weight DEVICE_WEIGHT

   Replace *STORAGE_NODE_MANAGEMENT_INTERFACE_IP_ADDRESS* with the
   IP address of the management network on the storage node. Replace
   *DEVICE_NAME* with a storage device name on the same storage node.
   For example, using the first storage node with the ``/dev/sdb1`` storage
   device and weight of 100::

      # swift-ring-builder container.builder add \
        --region 1 --zone 1 --ip 10.0.0.51 --port 6001 --device sdb --weight 100

   Repeat this command for each storage device on each storage node. In
   the example architecture, use the command in four variations::

      # swift-ring-builder container.builder add \
        --region 1 --zone 1 --ip 10.0.0.51 --port 6001 --device sdb --weight 100
      Device d0r1z1-10.0.0.51:6001R10.0.0.51:6001/sdb_"" with 100.0 weight got id 0
      # swift-ring-builder container.builder add \
        --region 1 --zone 2 --ip 10.0.0.51 --port 6001 --device sdc --weight 100
      Device d1r1z2-10.0.0.51:6001R10.0.0.51:6001/sdc_"" with 100.0 weight got id 1
      # swift-ring-builder container.builder add \
        --region 1 --zone 3 --ip 10.0.0.52 --port 6001 --device sdb --weight 100
      Device d2r1z3-10.0.0.52:6001R10.0.0.52:6001/sdb_"" with 100.0 weight got id 2
      # swift-ring-builder container.builder add \
        --region 1 --zone 4 --ip 10.0.0.52 --port 6001 --device sdc --weight 100
      Device d3r1z4-10.0.0.52:6001R10.0.0.52:6001/sdc_"" with 100.0 weight got id 3

#. Verify the ring contents::

      # swift-ring-builder container.builder
      container.builder, build version 4
      1024 partitions, 3.000000 replicas, 1 regions, 4 zones, 4 devices, 100.00 balance, 0.00 dispersion
      The minimum number of hours before a partition can be reassigned is 1
      The overload factor is 0.00% (0.000000)
      Devices:    id  region  zone      ip address  port  replication ip  replication port      name weight partitions balance meta
                   0       1     1       10.0.0.51  6001       10.0.0.51              6001      sdb  100.00          0 -100.00
                   1       1     2       10.0.0.51  6001       10.0.0.51              6001      sdc  100.00          0 -100.00
                   2       1     3       10.0.0.52  6001       10.0.0.52              6001      sdb  100.00          0 -100.00
                   3       1     4       10.0.0.52  6001       10.0.0.52              6001      sdc  100.00          0 -100.00

#. Rebalance the ring::

      # swift-ring-builder container.builder rebalance
      Reassigned 1024 (100.00%) partitions. Balance is now 0.00. Dispersion is now 0.00

Create Object Ring
------------------

The object server uses the object ring to maintain lists of object
locations on local devices.

To create the ring
~~~~~~~~~~~~~~~~~~

#. Create the base ``object.builder`` file::

     # swift-ring-builder object.builder create 10 3 1

#. Add each storage node to the ring::

      # swift-ring-builder object.builder \
        add --region 1 --zone 1 --ip STORAGE_NODE_MANAGEMENT_INTERFACE_IP_ADDRESS --port 6000 \
        --device DEVICE_NAME --weight DEVICE_WEIGHT

   Replace *STORAGE_NODE_MANAGEMENT_INTERFACE_IP_ADDRESS* with the
   IP address of the management network on the storage node. Replace
   *DEVICE_NAME* with a storage device name on the same storage node.
   For example, using the first storage node with the ``/dev/sdb1`` storage
   device and weight of 100::

      # swift-ring-builder object.builder add \
        --region 1 --zone 1 --ip 10.0.0.51 --port 6000 --device sdb --weight 100

   Repeat this command for each storage device on each storage node. In
   the example architecture, use the command in four variations::

      # swift-ring-builder object.builder add \
        --region 1 --zone 1 --ip 10.0.0.51 --port 6000 --device sdb --weight 100
      Device d0r1z1-10.0.0.51:6000R10.0.0.51:6000/sdb_"" with 100.0 weight got id 0
      # swift-ring-builder object.builder add \
        --region 1 --zone 2 --ip 10.0.0.51 --port 6000 --device sdc --weight 100
      Device d1r1z2-10.0.0.51:6000R10.0.0.51:6000/sdc_"" with 100.0 weight got id 1
      # swift-ring-builder object.builder add \
        --region 1 --zone 3 --ip 10.0.0.52 --port 6000 --device sdb --weight 100
     Device d2r1z3-10.0.0.52:6000R10.0.0.52:6000/sdb_"" with 100.0 weight got id 2
      # swift-ring-builder object.builder add \
        --region 1 --zone 4 --ip 10.0.0.52 --port 6000 --device sdc --weight 100
      Device d3r1z4-10.0.0.52:6000R10.0.0.52:6000/sdc_"" with 100.0 weight got id 3

#. Verify the ring contents::

      # swift-ring-builder object.builder
      object.builder, build version 4
      1024 partitions, 3.000000 replicas, 1 regions, 4 zones, 4 devices, 100.00 balance, 0.00 dispersion
      The minimum number of hours before a partition can be reassigned is 1
      The overload factor is 0.00% (0.000000)
      Devices:    id  region  zone      ip address  port  replication ip  replication port      name weight partitions balance meta
                   0       1     1       10.0.0.51  6000       10.0.0.51              6000      sdb  100.00          0 -100.00
                   1       1     2       10.0.0.51  6000       10.0.0.51              6000      sdc  100.00          0 -100.00
                   2       1     3       10.0.0.52  6000       10.0.0.52              6000      sdb  100.00          0 -100.00
                   3       1     4       10.0.0.52  6000       10.0.0.52              6000      sdc  100.00          0 -100.00

#. Rebalance the ring::

      # swift-ring-builder object.builder rebalance
      Reassigned 1024 (100.00%) partitions. Balance is now 0.00. Dispersion is now 0.00

Distribute ring configuration files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Copy the ``account.ring.gz``, ``container.ring.gz``, and ``object.ring.gz`` files to
the ``/etc/swift`` directory on each storage node and any additional nodes
running the proxy service::

    # cp account.ring.gz container.ring.gz object.ring.gz /etc/swift/

Finalize installation
---------------------

Configure hashes and default storage policy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Copy the swift service configuration file to the configuration directory::

      # cp /usr/share/defaults/swift/swift.conf /etc/swift

#. Edit the ``/etc/swift/swift.conf`` file and complete the following
   actions:

   * In the ``[swift-hash]`` section, configure the hash path prefix and
     suffix for your environment. Replace *HASH_PATH_PREFIX* and
     *HASH_PATH_SUFFIX* with unique values.::

         [swift-hash]
         ...
         swift_hash_path_suffix = HASH_PATH_PREFIX
         swift_hash_path_prefix = HASH_PATH_SUFFIX

   * In the ``[storage-policy:0]`` section, configure the default storage
     policy::

        [storage-policy:0]
        ...
        name = Policy-0
        default = yes

#. Copy the ``swift.conf`` file to the ``/etc/swift`` directory on each storage
   node and any additional nodes running the proxy service.
#. On all nodes, ensure proper ownership of the configuration directory::

      # systemctl restart update-triggers.target

#. On the controller node and any other nodes running the proxy service,
   start the Object Storage proxy service including its dependencies and
   configure them to start when the system boots::

      # systemctl enable swift-proxy.service memcached.service
      # systemctl start swift-proxy.service memcached.service

#. On the storage nodes, start the Object Storage services and configure
   them to start when the system boots::

      # systemctl enable swift-account.service \
                      swift-account-auditor.service \
                      swift-account-reaper.service \
                      swift-account-replicator.service \
                      swift-container.service \
                      swift-container-auditor.service \
                      swift-container-replicator.service \
                      swift-container-updater.service \
                      swift-object.service \
                      swift-object-auditor.service \
                      swift-object-replicator.service \
                      swift-object-updater.service
      # systemctl start swift-account.service \
                      swift-account-auditor.service \
                      swift-account-reaper.service \
                      swift-account-replicator.service \
                      swift-container.service \
                      swift-container-auditor.service \
                      swift-container-replicator.service \
                      swift-container-updater.service \
                      swift-object.service \
                      swift-object-auditor.service \
                      swift-object-replicator.service \
                      swift-object-updater.service

Verify operation
----------------

Verify operation of the Object Storage service.

#. In each client environment script, configure the Object Storage service client to use the Identity API version 3::

     $ echo "export OS_AUTH_VERSION=3" \
       | tee -a admin-openrc.sh demo-openrc.sh

#. Source the demo credentials::

     $ source demo-openrc.sh

#. Show the service status::

     $ swift stat
                             Account: AUTH_ed0b60bf607743088218b0a533d5943f
			  Containers: 0
			     Objects: 0
			       Bytes: 0
     Containers in policy "policy-0": 0
        Objects in policy "policy-0": 0
          Bytes in policy "policy-0": 0
         X-Account-Project-Domain-Id: default
                         X-Timestamp: 1444143887.71539
                          X-Trans-Id: tx1396aeaf17254e94beb34-0056143bde
                        Content-Type: text/plain; charset=utf-8
                       Accept-Ranges: bytes

#. Upload a test file::

     $ swift upload container1 FILE
     FILE

Replace *FILE* with the name of a local file to upload to the ``container1`` container.

#. List containers::

     $ swift list
     container1

#. Download a test file::

     $ swift download container1 FILE
     FILE [auth 0.295s, headers 0.339s, total 0.339s, 0.005 MB/s]

Replace *FILE* with the name of the file uploaded to the ``container1`` container.
