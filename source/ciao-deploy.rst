.. _ciao-deploy:

.. contents::

Deploying ciao via automation
#############################

Cloud Integrated Advanced Orchestrator (``ciao``) is a new workload
scheduler designed to address limitations of current cloud OS projects.
Ciao provides a lightweight, fully TLS-based minimal config, is
workload-agnostic, easy to update, offers an optimized-for-speed
scheduler, and is currently optimized for OpenStack*.

For more information, see https://clearlinux.org/ciao.

Environment
===========

For this example, we'll use a total of five nodes:
 - A deployment machine which will be used to run the playbooks.
 - A `controller`_ node which will be used to communicate with Keystone.
 - Two `compute nodes`_, which will spawn the VMs and containers.
 - A `network node`_ which will handle the networking for the workloads.

 Note: The deployment machine is not a necessary part of the cluster; it could be
 the sysadmin's computer or a CI/CD server.

.. _prerequisites:

Prerequisites
=============
Ansible* uses :command:`ssh` to run commands on the remote nodes. In order to do
that, the nodes must be configured to allow passwordless SSH connections
from the deployment machine to the cluster nodes. The user should also have
sudo privileges on the cluster nodes.


Install the software
====================

In Clear Linux, install the ``sysadmin-hostmgmt`` bundle on the deployment node. This
bundle contains the Ansible software required to run the playbooks.

.. code-block:: console

   # swupd bundle-add sysadmin-hostmgmt

Install ``go-basic``, ``os-core-dev``, ``kvm-host`` and ``os-common`` bundles
on the deployment node. These bundles contain requirements needed by the playbooks.

.. code-block:: console

   # swupd bundle-add go-basic c-basic kvm-host openstack-common

go-basic
  provides golang, which is needed to compile ciao
c-basic
  provides gcc, which is needed to compile some ciao dependencies
kvm-host
  provides qemu, which is needed to build the CNCI image
openstack-common
  provides python-keystone client, which is a dependency of the keystone role

For Ubuntu and Fedora, follow the instructions from `github`_

Create the playbook
===================

The ``sysadmin-hostmgmt`` bundle includes some sample playbooks that
you may use and customize for your own needs. Start by making a copy
of the sample playbook into your home folder

.. code-block:: console

   # cp -r /usr/share/ansible/examples/ciao ~/

Note: These files are also hosted in `github`_

The relevant files in the playbook are the following:

  * The `ciao.yml`_ file is the master playbook file and includes a playbook
    for each component of the cluster.

  * The `hosts`_ file is the hosts inventory file and contains the IP
    addresses/FQDN of your nodes, grouped under the roles they will serve

  * The `groups_vars/all`_ file contains variables that will be applied
    to your ciao setup. The mandatory variables are already there; be
    sure to change the values accordingly to fit your environment

  * The ``ciao_guest_key`` value in :file:`groups_var/all` is the key to be used to connect to the VMs created by
    ciao; you can use the ``ssh-keygen`` command to create one.

A full list of available variables can be found in the :file:`defaults/main.yml` file of each role at
https://github.com/clearlinux/clear-config-management/tree/master/roles

Install the required ansible-roles
==================================

.. code-block:: console

   # ansible-galaxy install -r requirements.yml


Run the playbook
================
Once you have your variables and hosts file configured, the deployment can
be started with the following command:

.. code-block:: console

   $ ansible-playbook -i hosts ciao.yml --private-key=<ssh_key>

Note: The playbook will create the following files in the current folder of the machine runninng the playbooks.

  * ./certificates: This directory contains the certificates that where created and copied to the cluster nodes.

  * ./images: This directory contains the images used by the ciao cluster. (fedora, clearlinux, cnci, ovmf.fd)

  * ./ciaorc: This file contains environment variables needed by ciao cli to authenticate to the ciao cluster.

  * ./openrc: This file contains environment variables needed by openstack cli to authenticate with the ciao cluster.

Verify
======
After ansible is done with the setup, you can verify the cluster is ready
by running the following command on the controller node. Change the **username**,
**password**, **controller**, and **identity** values to match your setup, as
was specified in the ``groups_var/all`` file:

.. code-block:: console

   # ciao-cli -identity=https://ciao-controller.example.com:35357 -username ciao -password ciaoUserPassword -controller=ciao-controller.example.com node status
   Total Nodes 3
    Ready 0
    Full 3
    Offline 0
    Maintenance 0

You could also take a look at the :file:`./ciaorc` file created on your
deployment node, which contains the following environment variables:

.. code-block:: console

   # cat ciaorc
   export CIAO_CONTROLLER=ciao-controller.example.com
   export CIAO_IDENTITY=https://ciao-controller.example.com:35357
   export CIAO_USERNAME=ciao
   export CIAO_PASSWORD=ciaoUserPassword

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
.. _ciao.yml: https://github.com/clearlinux/clear-config-management/blob/master/examples/ciao/ciao.yml
.. _hosts: https://github.com/clearlinux/clear-config-management/blob/master/examples/ciao/hosts
.. _groups_vars/all: https://github.com/clearlinux/clear-config-management/blob/master/examples/ciao/group_vars/all
.. _github: https://github.com/clearlinux/clear-config-management/tree/master/examples/ciao
