OpenStack* Image
################

The OpenStack Image service (glance) enables users to discover,
register, and retrieve virtual machine images. It offers a
`REST` API that enables you to query virtual
machine image metadata and retrieve an actual image.
You can store virtual machine images made available through
the Image service in a variety of locations, from simple file
systems to object-storage systems like OpenStack Object Storage.

  **Important:** For simplicity, this guide describes configuring the Image service to
  use the ``file`` back end, which uploads and stores in a
  directory on the controller node hosting the Image service. By
  default, this directory is ``/var/lib/glance/images/``.

  Before you proceed, ensure that the controller node has at least
  several gigabytes of space available in this directory.

  For information on requirements for other back ends, see
  `Configuration Reference <http://docs.openstack.org/liberty/
  config-reference/content/
  ch_configuring-openstack-image-service.html>`_.

Install and configure the Image Service
---------------------------------------

This section describes how to install and configure the Image service,
code-named glance, on the controller node. For simplicity, this
configuration stores images on the local file system.

Prerequisites
~~~~~~~~~~~~~

Before you install and configure the Image service, you must
create a database, service credentials, and API endpoints.

#. To create the database, complete these steps:

   * Use the database access client to connect to the database
     server as the ``root`` user::

       $ mysql -u root -p

   * Create the ``glance`` database::

       CREATE DATABASE glance;

   * Grant proper access to the ``glance`` database::

       GRANT ALL PRIVILEGES ON glance.* TO 'glance'@'localhost' \
         IDENTIFIED BY 'GLANCE_DBPASS';
       GRANT ALL PRIVILEGES ON glance.* TO 'glance'@'%' \
         IDENTIFIED BY 'GLANCE_DBPASS';

     Replace ``GLANCE_DBPASS`` with a suitable password.

   * Exit the database access client.

#. Source the ``admin`` credentials to gain access to
   admin-only CLI commands::

      $ source admin-openrc.sh
#. To create the service credentials, complete these steps:

   * Create the ``glance`` user. Replace ``GLANCE_PASS`` with a suitable
     password::

       $ openstack user create --domain default --password GLANCE_PASS glance
       +-----------+----------------------------------+
       | Field     | Value                            |
       +-----------+----------------------------------+
       | domain_id | default                          |
       | enabled   | True                             |
       | id        | e38230eeff474607805b596c91fa15d9 |
       | name      | glance                           |
       +-----------+----------------------------------+

   * Add the ``admin`` role to the ``glance`` user and
     ``service`` project::

       $ openstack role add --project service --user glance admin

   * Create the ``glance`` service entity::

       $ openstack service create --name glance \
         --description "OpenStack Image service" image
       +-------------+----------------------------------+
       | Field       | Value                            |
       +-------------+----------------------------------+
       | description | OpenStack Image service          |
       | enabled     | True                             |
       | id          | 8c2c7f1b9b5049ea9e63757b5533e6d2 |
       | name        | glance                           |
       | type        | image                            |
       +-------------+----------------------------------+

#. Create the Image service API endpoints::

     $ openstack endpoint create --region RegionOne \
       image public http://controller:9292
     +--------------+----------------------------------+
     | Field        | Value                            |
     +--------------+----------------------------------+
     | enabled      | True                             |
     | id           | 340be3625e9b4239a6415d034e98aace |
     | interface    | public                           |
     | region       | RegionOne                        |
     | region_id    | RegionOne                        |
     | service_id   | 8c2c7f1b9b5049ea9e63757b5533e6d2 |
     | service_name | glance                           |
     | service_type | image                            |
     | url          | http://controller:9292           |
     +--------------+----------------------------------+

     $ openstack endpoint create --region RegionOne \
       image internal http://controller:9292
     +--------------+----------------------------------+
     | Field        | Value                            |
     +--------------+----------------------------------+
     | enabled      | True                             |
     | id           | a6e4b153c2ae4c919eccfdbb7dceb5d2 |
     | interface    | internal                         |
     | region       | RegionOne                        |
     | region_id    | RegionOne                        |
     | service_id   | 8c2c7f1b9b5049ea9e63757b5533e6d2 |
     | service_name | glance                           |
     | service_type | image                            |
     | url          | http://controller:9292           |
     +--------------+----------------------------------+

     $ openstack endpoint create --region RegionOne \
       image admin http://controller:9292
     +--------------+----------------------------------+
     | Field        | Value                            |
     +--------------+----------------------------------+
     | enabled      | True                             |
     | id           | 0c37ed58103f4300a84ff125a539032d |
     | interface    | admin                            |
     | region       | RegionOne                        |
     | region_id    | RegionOne                        |
     | service_id   | 8c2c7f1b9b5049ea9e63757b5533e6d2 |
     | service_name | glance                           |
     | service_type | image                            |
     | url          | http://controller:9292           |
     +--------------+----------------------------------+

Install and configure components
--------------------------------

#. Install OpenStack Image bundle::

    # clr_bundle_add openstack-image

#. configurations will be located at ``/etc/glance``.

   * Create ``/etc/glance`` directory::

       # mkdir /etc/glance

   * Create empty configuration files ``/etc/glance/glance-api.conf``
     and ``/etc/glance/glance-registry.conf``::

       # touch /etc/glance/glance-{api,registry}.conf

#. Edit the ``/etc/glance/glance-api.conf`` file and complete
   the following actions:

   * In the ``[database]`` section, configure database access::

       [database]
       ...
       connection = mysql://glance:GLANCE_DBPASS@controller/glance

     Replace ``GLANCE_DBPASS`` with the password you chose for the
     Image service database.

   * In the ``[keystone_authtoken]`` section, configure Identity
     service access::

       [keystone_authtoken]
       ...
       auth_uri = http://controller:5000
       auth_url = http://controller:35357
       auth_plugin = password
       project_domain_id = default
       user_domain_id = default
       project_name = service
       username = glance
       password = GLANCE_PASS

     Replace ``GLANCE_PASS`` with the password you chose for the
     ``glance`` user in the Identity service.

#. Edit the ``/etc/glance/glance-registry.conf`` file and
   complete the following actions:

   * In the ``[database]`` section, configure database access::

       [database]
       ...
       connection = mysql://glance:GLANCE_DBPASS@controller/glance

     Replace ``GLANCE_DBPASS`` with the password you chose for the
     Image service database.

   * In the ``[keystone_authtoken]`` section, configure Identity
     service access::

       [keystone_authtoken]
       ...
       auth_uri = http://controller:5000
       auth_url = http://controller:35357
       auth_plugin = password
       project_domain_id = default
       user_domain_id = default
       project_name = service
       username = glance
       password = GLANCE_PASS

     Replace ``GLANCE_PASS`` with the password you chose for the
     ``glance`` user in the Identity service.

#. Ensure files have proper ownership by running the following command::

    # systemctl restart update-triggers.target

#. Populate the Image Service database::

    # su -s /bin/sh -c "glance-manage db_sync" glance

Finalize installation
---------------------

#. Start the Image Service services and configure them to start when the
   system boots::

    # systemctl enable glance-api.service glance-registry.service
    # systemctl start glance-api.service glance-registry.service

Verify operation
----------------

Verify operation of the Image service using
`CirrOS <http://launchpad.net/cirros>`__, a small
Linux image that helps you test your OpenStack deployment.

For more information about how to download and build images, see
`OpenStack Virtual Machine Image Guide
<http://docs.openstack.org/image-guide/content/index.html>`__.
For information about how to manage images, see the
`OpenStack User Guide
<http://docs.openstack.org/user-guide/common/cli_manage_images.html>`__.

#. In each client environment script, configure the Image service
   client to use API version 2.0::

      $ echo "export OS_IMAGE_API_VERSION=2" \
        | tee -a admin-openrc.sh demo-openrc.sh

#. Source the ``admin`` credentials to gain access to
   admin-only CLI commands::

      $ source admin-openrc.sh

#. Download the source image::

      $ curl -Ok http://download.cirros-cloud.net/0.3.4/cirros-0.3.4-x86_64-disk.img

#. Upload the image to the Image service using the
   `QCOW2` disk format, `bare` container format, and
   public visibility so all projects can access it::

      $ openstack image create cirros --file cirros-0.3.4-x86_64-disk.img \
        --disk-format qcow2 --container-format bare --public
        +------------------+------------------------------------------------------+
        | Field            | Value                                                |
        +------------------+------------------------------------------------------+
        | checksum         | ee1eca47dc88f4879d8a229cc70a07c6                     |
        | container_format | bare                                                 |
        | created_at       | 2015-10-26T23:40:03Z                                 |
        | disk_format      | qcow2                                                |
        | file             | /v2/images/fcf6fa55-56e9-4402-8137-3e9315c84905/file |
        | id               | fcf6fa55-56e9-4402-8137-3e9315c84905                 |
        | min_disk         | 0                                                    |
        | min_ram          | 0                                                    |
        | name             | cirros                                               |
        | owner            | 2e3093872ebf4143a122e2cc01a50d13                     |
        | protected        | False                                                |
        | schema           | /v2/schemas/image                                    |
        | size             | 13287936                                             |
        | status           | active                                               |
        | tags             |                                                      |
        | updated_at       | 2015-10-26T23:40:03Z                                 |
        | virtual_size     | None                                                 |
        | visibility       | public                                               |
        +------------------+------------------------------------------------------+

#. Confirm upload of the image and validate attributes::

      $ openstack image list
      +--------------------------------------+--------+
      | ID                                   | Name   |
      +--------------------------------------+--------+
      | 38047887-61a7-41ea-9b49-27987d5e8bb9 | cirros |
      +--------------------------------------+--------+

