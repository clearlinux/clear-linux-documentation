OpenStack* Image
################

The OpenStack Image service (glance) enables users to discover, register, and
retrieve virtual machine images.

Install and configure the Image Service
---------------------------------------

This section describes how to install and configure the Image service,
code-named glance, on the controller node. For simplicity, this configuration
stores images on the local file system. By default, this directory is
``/var/lib/glance/images/``.

Prerequisites
~~~~~~~~~~~~~

Before you install and configure the Image service, you must create a database,
service credentials, and API endpoints.

#. To create the database, complete these steps:

   * Use the database access client to connect to the database
     server as the ``root`` user.::

       $ mysql -u root -p

   * Create the ``glance`` database::

       CREATE DATABASE glance;

   * Grant proper access to the ``glance`` database. Replace ``GLANCE_DBPASS``
     with a suitable password.::

       GRANT ALL PRIVILEGES ON glance.* TO 'glance'@'localhost' \
         IDENTIFIED BY 'GLANCE_DBPASS';
       GRANT ALL PRIVILEGES ON glance.* TO 'glance'@'%' \
         IDENTIFIED BY 'GLANCE_DBPASS';

   * Exit the database access client.

#. Source the ``admin`` credentials to gain access to admin-only CLI commands.::

       $ source admin-openrc.sh

#. To create the service credentials, complete these steps:

   * Create the ``glance`` user::

       $ openstack user create --domain default --password-prompt glance
       User Password:
       Repeat User Password:
       +-----------+----------------------------------+
       | Field     | Value                            |
       +-----------+----------------------------------+
       | domain_id | default                          |
       | enabled   | True                             |
       | id        | e38230eeff474607805b596c91fa15d9 |
       | name      | glance                           |
       +-----------+----------------------------------+

   * Add the ``admin`` role to the ``glance`` user and ``service`` project.::

       $ openstack role add --project service --user glance admin

   * Create the ``glance`` service entity.::

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

#. Create the Image service API endpoints.::

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

#. Install OpenStack Image bundle.::

    # swupd bundle-add openstack-image
    # swupd verify --fix

#. Configurations will be located at ``/etc/glance``.

   * Create ``/etc/glance`` directory.::

       # mkdir /etc/glance

   * Create ``/etc/glance/glance-api.conf`` and
     ``/etc/glance/glance-registry.conf`` configuration files.::

       # touch /etc/glance/glance-{api,registry}.conf

#. Edit the ``/etc/glance/glance-api.conf`` file and complete the following
   actions:

   * In the ``[database]`` section, configure database access. Replace
     ``GLANCE_DBPASS`` with the password you chose for the Image service
     database.::

       [database]
       ...
       connection = mysql://glance:GLANCE_DBPASS@controller/glance

   * In the ``[keystone_authtoken]`` section, configure Identity service access.
     Replace ``GLANCE_PASS`` with the password you chose for the ``glance`` user
     in the Identity service.::

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

#. Edit the ``/etc/glance/glance-registry.conf`` file and complete the following
   actions:

   * In the ``[database]`` section, configure database access. Replace
     ``GLANCE_DBPASS`` with the password you chose for the Image service
     database.::

       [database]
       ...
       connection = mysql://glance:GLANCE_DBPASS@controller/glance

   * In the ``[keystone_authtoken]`` section, configure Identity service
     access. Replace ``GLANCE_PASS`` with the password you chose for the
     ``glance`` user in the Identity service.::

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
~~~~~~~~~~~~~~~~

Verify operation of the Image service using
`CirrOS <http://launchpad.net/cirros>`__, a small
Linux image that helps you test your OpenStack deployment.

#. In each client environment script, configure the Image service
   client to use API version 2.0::

    $ echo "export OS_IMAGE_API_VERSION=2" \
      | tee -a admin-openrc.sh demo-openrc.sh

#. Source the ``admin`` credentials to gain access to admin-only CLI commands::

    $ source admin-openrc.sh

#. Download the source image::

    $ curl -Ok http://download.cirros-cloud.net/0.3.4/cirros-0.3.4-x86_64-disk.img

#. Upload the image to the Image service using the `QCOW2` disk format, `bare`
   container format, and public visibility so all projects can access it::

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
