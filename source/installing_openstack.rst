.. _installing_openstack:

Installing OpenStack
####################

This section details an OpenStack* installation that uses
bundles available for Clear Linux* OS for Intel® Architecture.

The sample configuration files that are included will likely
require modification for your specific environment.

This installer uses Ansible* as configuration management tool.


Components supported by this installer
======================================

At the moment, this installer can deploy any or all of the following
components:

 - MariaDB
 - RabbitMQ
 - Keystone
 - Glance
 - Nova
 - Neutron
 - Dashboard (An identity node)
 - Heat

Prerequisites
=============

Before the installer can set up your cloud environment, these requirements
should be completed (if they aren't already):

#. Create a pair of SSH keys.

#. Copy your public key to each node.

#. Create the :file:`sshd_config` in ``/etc/ssh`` if it doesn't exist::

    # mkdir -p /etc/ssh && touch /etc/ssh/sshd_config

#. Allow ssh root access by adding "PermitRootLogin yes" to the ssh
   configuration.::

    # echo "PermitRootLogin yes" >> /etc/ssh/sshd_config


Using the Installer
===================

This step presumes a Clear Linux* machine as the ansible host.


Install the bundle
------------------

#. Install the `sysadmin-hostmgmt` bundle::

     # swupd bundle-add sysadmin-hostmgmt

**Next**:  :ref:`configure_openstack_environment`
