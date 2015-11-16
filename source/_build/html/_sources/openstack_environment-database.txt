.. openstack_environment-database:

Database
~~~~~~~~
Most OpenStack services use an SQL database to store information. The
database typically runs on the controller node. The procedures in this
guide use MariaDB.

Install and configure the database server
-----------------------------------------

#. Install MariaDB bundle:

  .. code-block:: console

     # clr_bundle_add database-mariadb

#. Create the ``/etc/mariadb/`` folder and the ``/etc/mariadb/openstack.cnf`` file.

  .. code-block:: console

     # mkdir /etc/mariadb
     # touch /etc/mariadb/openstack.cnf

#. Add the ``[mysqld]`` section, set the bind-address key to the
   management IP address of the controller node to enable access by
   other nodes via the management network and enable useful options for
   UTF-8 character set:

  .. code:: console

    [mysqld]
    bind-address = 10.0.0.11
    default-storage-engine = innodb
    innodb_file_per_table
    collation-server = utf8_general_ci
    init-connect = 'SET NAMES utf8'
    character-set-server = utf8

Finalizing database installation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Complete the following steps to finalize database installation:

#. Start the database service and configure it to start when the system
   boots:

  .. code:: console

    # systemctl enable mariadb.service
    # systemctl start mariadb.service

2. Secure the database service including choosing a suitable password
   for the root account:

  .. code:: console

    # mysql_secure_installation
