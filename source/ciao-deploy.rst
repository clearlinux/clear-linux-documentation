.. _ciao-deploy:

.. contents::

Deploying ciao via automation
#############################

Cloud Integrated Advanced Orchestrator (``ciao``) is a new workload 
scheduler designed to address limitations of current cloud OS projects. 
CIAO provides a lightweight, fully TLS-based minimal config, is 
workload-agnostic, easy to update, offers an optimized-for-speed 
scheduler, and is currently optimized for OpenStack*.

For more information, see https://clearlinux.org/ciao.


Environment
===========

For this example, we'll use a total of four nodes:
 - A `controller`_ node which will be used to communicate with Keystone.
 - Two `compute nodes`_, which will spawn the VMs and containers.
 - A `network node`_ which will handle the networking for the workloads.


.. _prerequisites:

Prerequisites
=============
Ansible* uses :command:`ssh` to run commands on the remote nodes. In order to do 
that, the nodes must be configured to allow passwordless ssh connections 
from the root user. Follow these steps to configure your nodes.

#. Generate ssh keys:
   
   .. code-block:: console

      # ssh-keygen

#. Enable root login:
   
   .. code-block:: console

      # echo "PermitRootLogin yes" >> /etc/ssh/sshd_config

#. Enable sshd service:
   
   .. code-block:: console

      # systemctl enable sshd
      # systemctl start sshd

#. Allow passwordless login:

   .. code-block:: console
      
      # ssh-copy-id -i <ssh_key> root@node


Install the software
====================

Install the ``sysadmin-hostmgmt`` bundle on the development node. This
bundle contains the Ansible software required to run the playbooks, as 
well as some Ansible roles and sample playbooks that you can use to 
build your own:

.. code-block:: console

   # swupd bundle-add sysadmin-hostmgmt


Create the playbook
===================

The ``sysadmin-hostmgmt`` bundle includes some sample playbooks that 
you may use and customize for your own needs. Start by making a copy 
of the sample playbook into your home folder

.. code-block:: console

   # cp -r /usr/share/ansible/examples/ciao ~/

The playbook consists of three files that you should modify to fit 
your needs::

    ciao/
    |-- ciao.yml
    |-- group_vars
    |   -- all
    +-- hosts

The :file:`hosts` file contains the IP addresses/hostnames of your
nodes, grouped under the roles they will serve. For this example
it should look like this::

    [dbservers]
    ciao-controller.example.com
    
    [openstack_identity]
    ciao-controller.example.com
    
    [openstack_image]
    ciao-controller.example.com
    
    [ciao_controller]
    ciao-controller.example.com
    
    [ciao_network]
    ciao-network.example.com
    
    [ciao_compute]
    ciao-compute1.example.com
    ciao-compute2.example.com

This ``groups_var/all`` file contains variables that will be applied 
to your ciao setup. The mandatory variables are already there; be 
sure to change the values accordingly to fit your environment. It 
should look something like this::

    ---
    # Vars required for mariadb and os-common
    # https://github.com/clearlinux/clear-config-management/tree/master/roles/mariadb
    # https://github.com/clearlinux/clear-config-management/tree/master/roles/os-common
    database_root_password: secret
    
    # Vars required for os-common
    # https://github.com/clearlinux/clear-config-management/tree/master/roles/os-common
    keystone_fqdn: ciao-controller.example.com
    keystone_admin_password: secret
    
    # Vars required for os-keystone
    # https://github.com/clearlinux/clear-config-management/tree/master/roles/os-keystone
    keystone_database_password: secret
    keystone_root_domain: example.com
    keystone_p12password: secret
    
    # Vars required for ciao-common
    # https://github.com/clearlinux/clear-config-management/tree/master/roles/ciao-common
    ciao_controller_fqdn: ciao-controller.example.com
    
    # Vars required for ciao-controller
    # https://github.com/clearlinux/clear-config-management/tree/master/roles/ciao-controller
    ciao_service_user: csr
    ciao_service_password: secret
    ciao_admin_email: admin@example.com
    ciao_cert_organization: Example, Inc.
    ciao_guest_user: demouser
    ciao_guest_key: ~/.ssh/guest_vms.pub
    

The ``ciao_guest_key`` is the key to be used to connect to the VMs created by
ciao; you can use the ``ssh-keygen`` command to create one as explained in the
:ref:`prerequisites` section.

A full list of available variables can be found in the ciao-* roles at
https://github.com/clearlinux/clear-config-management/tree/master/roles


Run the playbook
================
Once you have your variables and hosts file configured, the deployment can 
be fired with the following command:

.. code-block:: console
   
   # ansible-playbook -i hosts ciao.yml --private-key=<ssh_key>


Verify
======
After ansible is done with the setup, you can verify the cluster is ready
by running the following command on the controller node. Change the **username**, 
**password**, **controller**, and **identity** values to match your setup, as 
was specified in the ``groups_var/all`` file:

.. code-block:: console

   # ciao-cli -identity=https://ciao-controller.example.com:35357 -username admin -password secret -controller=ciao-controller.example.com node status
   Total Nodes 3
    Ready 0
    Full 3
    Offline 0
    Maintenance 0

You could also take a look at the :file:`~/ciaorc` file that contains the
following environment variables:

.. code-block:: console

   # cat ciaorc
   export CIAO_CONTROLLER=ciao-controller.example.com
   export CIAO_IDENTITY=https://ciao-controller.example.com:35357
   export CIAO_USERNAME=csr
   export CIAO_PASSWORD=secret

then you could verify with the following command:

.. code-block:: console

   # source ciaorc
   # ciao-cli node status
   Total Nodes 3
    Ready 0
    Full 3
    Offline 0
    Maintenance 0

.. _controller: https://github.com/01org/ciao/tree/master/ciao-controller
.. _compute nodes: https://github.com/01org/ciao/tree/master/ciao-launcher
.. _network node: https://github.com/01org/ciao/tree/master/ciao-launcher
