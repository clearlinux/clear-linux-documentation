.. _installing_openstack:

Installing OpenStack
####################

This section details an OpenStack* installation that uses
bundles available for Clear Linux* OS for Intel® Architecture.

The sample configuration files that are included will likely
require modification for your specific environment.

This Clear Config Management uses Ansible* as configuration management tool.


Components supported by Clear Config Management
===============================================

At the moment, this installer can deploy any or all of the following
components:

 - MariaDB
 - RabbitMQ
 - Keystone
 - Glance
 - Nova
 - Neutron
 - Dashboard (In identity node)
 - Heat

Note:
-----

Below you will find the reference to componets supported on ClearLinux* but
its support in Clear Config Management is still pending of development:

.. csv-table:: "Supported Components on ClearLinux*, but unsupported by Clear Config Management"
   :header: "Component", "Bundles", "OpenStack* official documentation"
   :widths: 20, 70, 100 

   "Swift", "openstack-object-storage and openstack-block-storage-controller", "http://docs.openstack.org/developer/swift/"
   "Cinder", "openstack-block-storage and openstack-block-storage-controller", "http://docs.openstack.org/developer/cinder/"
   "Ceilometer", "openstack-telemetry", "http://docs.openstack.org/developer/ceilometer/"


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
