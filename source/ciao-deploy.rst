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
For this example, we'll use a total of three nodes:
 - A `controller <https://github.com/01org/ciao/tree/master/ciao-controller>`_ node which will be used to communicate with Keystone.
 - A `compute node <https://github.com/01org/ciao/tree/master/ciao-launcher>`_ which will spawn the VM's and containers.

 - A `network node <https://github.com/01org/ciao/tree/master/ciao-launcher>`_ which will handle the netowrking for the workloads.

Prerequisites
=============
Ansible uses ssh to run commands on the remote servers. In order to do that, the servers
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

The hosts file contains the IP addresses/hostnames of your servers grouped under the roles
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
    ciao-compute.example.com

This ``groups_var/all`` file contains variables that will applied for your ciao setup.
The mandatory variables are already there; be sure to change the values accordingly to
fit your environment. It should look something like this::

    ---
    database_root_password: secret
    
    glance_fqdn: ciao-controller.example.com
    glance_user_password: secret
    glance_database_password: secret
    
    ciao_controller_ip: 172.17.0.6
    ciao_mgmt_subnet: 172.17.0.0/24
    ciao_compute_subnet: "{{ciao_mgmt_subnet}}"
    ciao_csr_password: secret
    ciao_ssh_public_key: ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDDhn1BIdDv2Rpx6qhYt9Z+3eOg1JIGyt6E0as3J02ymXsN2Zc4s+XXcj0tkifgZmKmm1H4dt1bVMcWcODl8qP6hjRVjSdo7KW8vXYkQv7eXNnhO+4vCttI6UsaB8LDdv6/TRGaRjj66shAC70ySH77/COAHnzTJdSWvzEVBs4hO8rii6MmyDduQhZM14JpCFP2zkZ1ICNcPjf60a4vi2GiW8PWlJwrUuzsa5qfWCExA98UD04lg+mwFCYBfgQeQcXKN+eQqV6XQ8ujE/++pLSjsSSK1/cXCkWtMGJGTgjY5zH20tfIbJPnBeOIlYvWjJDNFvCC5b9UspTLlhnggGhZ root@ciao-controller.example.com
    ciao_admin_email: admin@ciao-controller.example.com
    ciao_cert_organization: Example, Inc.
    
    keystone_fqdn: ciao-controller.example.com
    keystone_root_domain: ciao-controller.example.com
    keystone_p12password: secret
    keystone_database_password: secret
    keystone_admin_password: secret
    keystone_services:
      - service_name: "ciao"
        service_type: "compute"
    keystone_projects:
      - project_name: "demo"
    keystone_users:
      - user_name: "csr"
        password: "{{ciao_csr_password}}"
        project_name: "admin"
      - user_name: "demo"
        password: "secret"
        project_name: "demo"
    keystone_roles:
      - demo
    keystone_user_roles:
      - user_name: csr
        project_name: service
        role_name: admin
      - user_name: demo
        project_name: demo
        role_name: demo

A full list of available variables can be found under
``/usr/share/ansible/roles/<role>/defaults/main.yml``

Run the playbook
================
Once you have your variables and hosts file configured, the deployment can be fired
with the following command::

    # ansible-playbook -i hosts ciao.yml

Verify
======
Once ansible is done with the setup, on the controller node you can verify the
cluster is ready by running the following command.
Change the username, password, controller and identity values to match
your setup as specified in the ``groups_var/all`` file::

    # ciao-cli -identity=https://ciao-controller.example.com:35357 -username admin -password secret -controller=ciao-controller.example.com node status
    Total Nodes 2
            Ready 2
            Full 0
            Offline 0
            Maintenance 0

You could also create a ciaorc file that contains the following environment
variables::

    # cat ciaorc
    export CIAO_CONTROLLER=ciao-controller.example.com
    export CIAO_IDENTITY=https://ciao-controller.example.com:35357
    export CIAO_USERNAME=admin
    export CIAO_PASSWORD=secure

then you could verify with the following command::

    # source ciaorc
    # ciao-cli node status
    Total Nodes 2
            Ready 2
            Full 0
            Offline 0
            Maintenance 0
