.. _ciao-deploy:

.. contents::

CIAO in ClearLinux
##################

Cloud Integrated Advanced Orchestrator (ciao) is a new workload scheduler
designed to address limitations in current cloud OS projects.
Ciao provides a lightweight, fully TLS-based, minimal Config, workload-agnostic,
easily updateable, optimized-for-speed scheduler, currently optimized for Openstack.

For more information visit https://clearlinux.org/ciao.

Environment
===========
For this example, we'll use a total of four nodes:
 - A `controller <https://github.com/01org/ciao/tree/master/ciao-controller>`_ node which will be used to communicate with Keystone.
 - Two `compute nodes <https://github.com/01org/ciao/tree/master/ciao-launcher>`_ which will spawn the VM's and containers.

 - A `network node <https://github.com/01org/ciao/tree/master/ciao-launcher>`_ which will handle the netowrking for the workloads.

Prerequisites
=============
Ansible uses ssh to run commands on the remote nodes. In order to do that, the nodes
must be configured to allow passwordless ssh connections from the root user. Follow these
steps to configure your nodes.

#. Generate ssh keys::

    # ssh-keygen

#. Enable root login::

    # echo "PermitRootLogin yes" >> /etc/ssh/sshd_config

#. Enable sshd service::

    # systemctl enable sshd
    # systemctl start sshd

#. Allow passwordless login::

    # ssh-copy-id -i <ssh_key> root@node

Install the software
====================

Install the ``sysadmin-hostmgmt`` bundle on the development node. This bundle contains
the Ansible software required to run the playbooks, as well as some Ansible roles and
sample playbooks that you can use to build your own::

    # swupd bundle-add sysadmin-hostmgmt

Create the playbook
===================

The ``sysadmin-hostmgmt`` bundle includes some sample playbooks that you may use and
customize for your own needs. Start by making a copy of the sample playbook into your
home folder::

    # cp -r /usr/share/ansible/examples/ciao ~/

The playbook consist of three files that you should modify to fit your needs::

    ciao/
    |-- ciao.yml
    |-- group_vars
    |   `-- all
    +-- hosts

The hosts file contains the IP addresses/hostnames of your nodes grouped under the roles
they will serve. For this example it should look like this::

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

This ``groups_var/all`` file contains variables that will applied for your ciao setup.
The mandatory variables are already there; be sure to change the values accordingly to
fit your environment. It should look something like this::

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
    

The `ciao_guest_key` is the key to be used to connect to the VMs created by ciao,
you can use the `ssh-keygen` command to create one as explained in the prerequisites
section.

A full list of available variables can be found in the ciao-* roles at
https://github.com/clearlinux/clear-config-management/tree/master/roles

Run the playbook
================
Once you have your variables and hosts file configured, the deployment can be fired
with the following command::

    # ansible-playbook -i hosts ciao.yml --private-key=<ssh_key>

Verify
======
Once ansible is done with the setup, on the controller node you can verify the
cluster is ready by running the following command.
Change the username, password, controller and identity values to match
your setup as specified in the ``groups_var/all`` file::

    # ciao-cli -identity=https://ciao-controller.example.com:35357 -username admin -password secret -controller=ciao-controller.example.com node status
    Total Nodes 3
            Ready 0
            Full 3
            Offline 0
            Maintenance 0

You could also take a look at the ciaorc file created (in `~/ciaorc`)
that contains the following environment variables::

    # cat ciaorc
    export CIAO_CONTROLLER=ciao-controller.example.com
    export CIAO_IDENTITY=https://ciao-controller.example.com:35357
    export CIAO_USERNAME=csr
    export CIAO_PASSWORD=secret

then you could verify with the following command::

    # source ciaorc
    # ciao-cli node status
    Total Nodes 3
            Ready 0
            Full 3
            Offline 0
            Maintenance 0
