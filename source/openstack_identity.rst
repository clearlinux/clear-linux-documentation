OpenStack Identity
############################################################

The OpenStack Identity service provides a single point of
integration for managing authentication, authorization, and service catalog
services. Other OpenStack services use the Identity service as a common
unified API. Additionally, services that provide information about users
but that are not included in OpenStack (such as LDAP services) can be
integrated into a pre-existing infrastructure.

In order to benefit from the Identity service, other OpenStack services need to
collaborate with it. When an OpenStack service receives a request from a user,
it checks with the Identity service whether the user is authorized to make the
request.

The Identity service contains these components:

**Server**
    A centralized server provides authentication and authorization
    services using a RESTful interface.

**Drivers**
    Drivers or a service back end are integrated to the centralized
    server. They are used for accessing identity information in
    repositories external to OpenStack, and may already exist in
    the infrastructure where OpenStack is deployed (for example, SQL
    databases or LDAP servers).

**Modules**
    Middleware modules run in the address space of the OpenStack
    component that is using the Identity service. These modules
    intercept service requests, extract user credentials, and send them
    to the centralized server for authorization. The integration between
    the middleware modules and OpenStack components uses the Python Web
    Server Gateway Interface.

When installing OpenStack Identity service, you must register each
service in your OpenStack installation. Identity service can then track
which OpenStack services are installed, and where they are located on
the network.

Install and configure
~~~~~~~~~~~~~~~~~~~~~

This section describes how to install and configure the OpenStack
Identity service, code-named keystone, on the controller node. For
performance, this configuration deploys the Nginx HTTP server to handle
requests.

Prerequisites
-------------

Before you configure the OpenStack Identity service, you must create a
database and an administration token.

#. To create the database, complete the following actions:

   * Use the database access client to connect to the database server as the
     ``root`` user:

     .. code-block:: console

        $ mysql -u root -p

   * Create the ``keystone`` database:

     .. code-block:: console

        CREATE DATABASE keystone;

   * Grant proper access to the ``keystone`` database:

     .. code-block:: console

        GRANT ALL PRIVILEGES ON keystone.* TO 'keystone'@'localhost' \
          IDENTIFIED BY 'KEYSTONE_DBPASS';
        GRANT ALL PRIVILEGES ON keystone.* TO 'keystone'@'%' \
          IDENTIFIED BY 'KEYSTONE_DBPASS';

     Replace ``KEYSTONE_DBPASS`` with a suitable password.

   * Exit the database access client.

#. Generate a random value to use as the administration token during
   initial configuration:

   .. code-block:: console

      $ openssl rand -hex 10


Install and configure components
--------------------------------


#. Run the following command to install the packages:

  .. code-block:: console

     # clr_bundle_add openstack-identity

#. Custom configurations will be located at /etc/keystone/

  * Create the /etc/keystone directory:

    .. code-block:: console

       # mkdir /etc/keystone

  * Create empty keystone configuration file /etc/keystone/keystone.conf:

    .. code-block:: console

       # touch /etc/keystone/keystone.conf

#. Edit the ``/etc/keystone/keystone.conf`` file and complete the following
   actions:

   * In the ``[DEFAULT]`` section, define the value of the initial
     administration token:

     .. code-block:: ini

        [DEFAULT]
        ...
        admin_token = ADMIN_TOKEN

     Replace ``ADMIN_TOKEN`` with the random value that you generated in a
     previous step.

   * In the ``[database]`` section, configure database access:

     .. code-block:: ini

        [database]
        ...
        connection = mysql://keystone:KEYSTONE_DBPASS@controller/keystone

     Replace ``KEYSTONE_DBPASS`` with the password you chose for the database.

#. Enter the following command:

   .. code:: console

    # systemctl restart update-triggers.target

#. Populate the Identity service database:

   .. code-block:: console

      # su -s /bin/sh -c "keystone-manage db_sync" keystone

Finalize the installation
-------------------------

#. Keystone is deployed as a uwsgi module. To start the Identity
   service, you should enable and start the nginx service

    .. code-block:: console

       # systemctl enable nginx uwsgi@keystone-admin.socket \
        uwsgi@keystone-public.socket

       # systemctl start nginx uwsgi@keystone-admin.socket \
        uwsgi@keystone-public.socket


Create the service entity and API endpoints
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Identity service provides a catalog of services and their locations.
Each service that you add to your OpenStack environment requires a
service entity and several API endpoints in the catalog.

Prerequisites
-------------

You must pass the value of the authentication token to the `openstack`
command with the ``--os-token`` parameter or set the OS_TOKEN
environment variable. Similarly, you must also pass the value of the
Identity service URL to the `openstack` command with the ``--os-url``
parameter or set the OS_URL environment variable. This guide uses
environment variables to reduce command length.

#. Configure the authentication token:

  .. code-block:: console

     $ export OS_TOKEN=ADMIN_TOKEN

  Replace ``ADMIN_TOKEN`` with the authentication token that you
  generated before. For example:

  .. code-block:: console

     $ export OS_TOKEN=294a4c8a8a475f9b9836

#. Configure the endpoint:

  .. code:: text

     $ export OS_URL=http://controller:35357/v3

#. Configure the Identity API version:

  .. code-block:: console

     $ export OS_IDENTITY_API_VERSION=3

#. Install the OpenStack Python clients bundle:

  .. code-block:: console

     # clr_bundle_add openstack-python-clients

Create the service entity and API endpoints
-------------------------------------------

#. The Identity service manages a catalog of services in your OpenStack
   environment. Services use this catalog to determine the other services
   available in your environment.

   Create the service entity for the Identity service:

   .. code-block:: console

      $ openstack service create \
        --name keystone --description "OpenStack Identity" identity
      +-------------+----------------------------------+
      | Field       | Value                            |
      +-------------+----------------------------------+
      | description | OpenStack Identity               |
      | enabled     | True                             |
      | id          | 4ddaae90388b4ebc9d252ec2252d8d10 |
      | name        | keystone                         |
      | type        | identity                         |
      +-------------+----------------------------------+

#. The Identity service manages a catalog of API endpoints associated with
   the services in your OpenStack environment. Services use this catalog to
   determine how to communicate with other services in your environment.

   OpenStack uses three API endpoint variants for each service: admin,
   internal, and public. The admin API endpoint allows modifying users and
   tenants by default, while the public and internal APIs do not allow these
   operations. In a production environment, the variants might reside on
   separate networks that service different types of users for security
   reasons. For instance, the public API network might be visible from the
   Internet so customers can manage their clouds. The admin API network
   might be restricted to operators within the organization that manages
   cloud infrastructure. The internal API network might be restricted to
   the hosts that contain OpenStack services. Also, OpenStack supports
   multiple regions for scalability. For simplicity, this guide uses the
   management network for all endpoint variations and the default
   ``RegionOne`` region.

   Create the Identity service API endpoints:

   .. code-block:: console

      $ openstack endpoint create --region RegionOne \
        identity public http://controller:5000/v3
      +--------------+----------------------------------+
      | Field        | Value                            |
      +--------------+----------------------------------+
      | enabled      | True                             |
      | id           | 30fff543e7dc4b7d9a0fb13791b78bf4 |
      | interface    | public                           |
      | region       | RegionOne                        |
      | region_id    | RegionOne                        |
      | service_id   | 8c8c0927262a45ad9066cfe70d46892c |
      | service_name | keystone                         |
      | service_type | identity                         |
      | url          | http://controller:5000/v3        |
      +--------------+----------------------------------+

      $ openstack endpoint create --region RegionOne \
        identity internal http://controller:5000/v3
      +--------------+----------------------------------+
      | Field        | Value                            |
      +--------------+----------------------------------+
      | enabled      | True                             |
      | id           | 57cfa543e7dc4b712c0ab137911bc4fe |
      | interface    | internal                         |
      | region       | RegionOne                        |
      | region_id    | RegionOne                        |
      | service_id   | 6f8de927262ac12f6066cfe70d99ac51 |
      | service_name | keystone                         |
      | service_type | identity                         |
      | url          | http://controller:5000/v3        |
      +--------------+----------------------------------+

      $ openstack endpoint create --region RegionOne \
        identity admin http://controller:35357/v3
      +--------------+----------------------------------+
      | Field        | Value                            |
      +--------------+----------------------------------+
      | enabled      | True                             |
      | id           | 78c3dfa3e7dc44c98ab1b1379122ecb1 |
      | interface    | admin                            |
      | region       | RegionOne                        |
      | region_id    | RegionOne                        |
      | service_id   | 34ab3d27262ac449cba6cfe704dbc11f |
      | service_name | keystone                         |
      | service_type | identity                         |
      | url          | http://controller:35357/v3       |
      +--------------+----------------------------------+

Creating projects, users and roles
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Complete the following steps to create projects, users and roles:

#. Create an administrative project, user, and role for administrative
   operations in your environment:

   * Create the ``admin`` project:

     .. code-block:: console

        $ openstack project create --domain default \
          --description "Admin Project" admin
        +-------------+----------------------------------+
        | Field       | Value                            |
        +-------------+----------------------------------+
        | description | Admin Project                    |
        | domain_id   | default                          |
        | enabled     | True                             |
        | id          | 343d245e850143a096806dfaefa9afdc |
        | is_domain   | False                            |
        | name        | admin                            |
        | parent_id   | None                             |
        +-------------+----------------------------------+

   * Create the ``admin`` user. Replace ``ADMIN_PASS`` with a suitable
     password and ``EMAIL_ADDRESS`` with a suitable e-mail address:

     .. code-block:: console

        $ openstack user create --domain default \
          --password ADMIN_PASS --email EMAIL_ADDRESS admin
        +-----------+----------------------------------+
        | Field     | Value                            |
        +-----------+----------------------------------+
        | domain_id | default                          |
        | email     | admin@example.com                |
        | enabled   | True                             |
        | id        | ac3377633149401296f6c0d92d79dc16 |
        | name      | admin                            |
        +-----------+----------------------------------+

   * Create the ``admin`` role:

     .. code-block:: console

        $ openstack role create admin
        +-------+----------------------------------+
        | Field | Value                            |
        +-------+----------------------------------+
        | id    | cd2cb9a39e874ea69e5d4b896eb16128 |
        | name  | admin                            |
        +-------+----------------------------------+

   * Add the ``admin`` role to the ``admin`` project and user:

     .. code-block:: console

        $ openstack role add --project admin --user admin admin

#. This guide uses a service project that contains a unique user for each
   service that you add to your environment. Create the ``service``
   project:

   .. code-block:: console

      $ openstack project create --domain default \
        --description "Service Project" service
      +-------------+----------------------------------+
      | Field       | Value                            |
      +-------------+----------------------------------+
      | description | Service Project                  |
      | domain_id   | default                          |
      | enabled     | True                             |
      | id          | 894cdfa366d34e9d835d3de01e752262 |
      | is_domain   | False                            |
      | name        | service                          |
      | parent_id   | None                             |
      +-------------+----------------------------------+

#. Regular (non-admin) tasks should use an unprivileged project and user.
   As an example, this guide creates the ``demo`` project and user.

   * Create the ``demo`` project:

     .. code-block:: console

        $ openstack project create --domain default \
          --description "Demo Project" demo
        +-------------+----------------------------------+
        | Field       | Value                            |
        +-------------+----------------------------------+
        | description | Demo Project                     |
        | domain_id   | default                          |
        | enabled     | True                             |
        | id          | ed0b60bf607743088218b0a533d5943f |
        | is_domain   | False                            |
        | name        | demo                             |
        | parent_id   | None                             |
        +-------------+----------------------------------+

   * Create the ``demo`` user.  Replace ``DEMO_PASS``
     with a suitable password and ``EMAIL_ADDRESS`` with a suitable
     e-mail address:

     .. code-block:: console

        $ openstack user create --domain default \
          --password DEMO_PASS --email EMAIL_ADDRESS demo
        +-----------+----------------------------------+
        | Field     | Value                            |
        +-----------+----------------------------------+
        | domain_id | default                          |
        | email     | demo@example.com                 |
        | enabled   | True                             |
        | id        | 58126687cbcc4888bfa9ab73a2256f27 |
        | name      | demo                             |
        +-----------+----------------------------------+

   * Create the ``user`` role:

     .. code-block:: console

        $ openstack role create user
        +-------+----------------------------------+
        | Field | Value                            |
        +-------+----------------------------------+
        | id    | 997ce8d05fc143ac97d83fdfb5998552 |
        | name  | user                             |
        +-------+----------------------------------+

   * Add the ``user`` role to the ``demo`` project and user:

     .. code-block:: console

        $ openstack role add --project demo --user demo user

Verify operation
~~~~~~~~~~~~~~~~

Verify operation of the Identity service before installing other
services.

#. For security reasons, remove the admin_token value in
   /etc/keystone/keystone.conf:

   Edit the ``[DEFAULT]`` section and remove ``admin_token``.

#. Unset the temporary ``OS_TOKEN`` and ``OS_URL`` environment variables:

  .. code-block:: console

     $ unset OS_TOKEN OS_URL

#. As the ``admin`` user, request an authentication token:

  .. code-block:: console

     $ openstack --os-auth-url http://controller:35357/v3 \
       --os-project-domain-id default --os-user-domain-id default \
       --os-project-name admin --os-username admin --os-auth-type password \
       token issue
     Password:
     +------------+----------------------------------+
     | Field      | Value                            |
     +------------+----------------------------------+
     | expires    | 2015-03-24T18:55:01Z             |
     | id         | ff5ed908984c4a4190f584d826d75fed |
     | project_id | cf12a15c5ea84b019aec3dc45580896b |
     | user_id    | 4d411f2291f34941b30eef9bd797505a |
     +------------+----------------------------------+

#. As the ``demo`` user, request an authentication token:

  .. code-block:: console

     $ openstack --os-auth-url http://controller:5000/v3 \
       --os-project-domain-id default --os-user-domain-id default \
       --os-project-name demo --os-username demo --os-auth-type password \
       token issue
     Password:
     +------------+----------------------------------+
     | Field      | Value                            |
     +------------+----------------------------------+
     | expires    | 2014-10-10T12:51:33Z             |
     | id         | 1b87ceae9e08411ba4a16e4dada04802 |
     | project_id | 4aa51bb942be4dd0ac0555d7591f80a6 |
     | user_id    | 7004dfa0dda84d63aef81cf7f100af01 |
     +------------+----------------------------------+
