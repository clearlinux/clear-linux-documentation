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
that, configure a user for passwordless SSH connections from the deployment
container to the cluster nodes. This user must also have passwordless sudo
privileges on the cluster nodes.

This guide uses a docker container to provide all the needed deployment tools;
in order to use it, you will need docker in the machine you're orchestating
your deployment.


Setup your deployment machine
=============================

We provide a ready-to-use docker container. Simply download it and
setup your cluster configurations:

.. code-block:: console

   $ docker pull clearlinux/ciao-deploy


You can later launch the container with:

.. code-block:: console

   $ docker run --privileged -v /path/to/your/.ssh/key:/root/.ssh/id_rsa \
                -it clearlinux/ciao-deploy

Note: container is called in `privileged` mode in order to install your
certificates in the CNCI image.

Once you're inside the container, continue working in the `/root/` directory

.. code-block:: console

   # cd /root/

Next, set up the configuration files for the cluster:

  * The `hosts`_ file is the hosts inventory file which contains the IP
    addresses/FQDN of your nodes, grouped under the roles they will serve.

  * The `groups_vars/all`_ file contains variables that will be applied
    to your ciao setup. The mandatory variables are already there; be
    sure to change the values accordingly to fit your environment.

  * The ``ciao_guest_key`` value in :file:`groups_var/all` is the key to be
    used to connect to the VMs created by ciao; you can use the
    ``ssh-keygen`` command to create one.

A full list of available variables can be found in the
:file:`defaults/main.yml` file of each role at
https://github.com/clearlinux/clear-config-management/tree/master/roles

Note: All the files in :file:`/root/ciao/` are hosted in `github`_


Run the playbook
================
Once the variables and hosts file are configured, start deployment
with the following command:

.. code-block:: console

   # ansible-playbook -i hosts ciao.yml \
       --private-key=~/.ssh/id_rsa \
       --user=<REMOTE_USER>

Note: The playbook will create the following files in the current folder of 
the machine running the playbooks.

  * ``./certificates``: This directory contains the certificates
    that where created and copied to the cluster nodes.

  * ``./images``: This directory contains the images used by the 
    ciao cluster (fedora, clearlinux, cnci, ovmf.fd).

  * ``./ciaorc``: This file contains environment variables needed 
    by ciao cli to authenticate to the ciao cluster.

  * ``./openrc``: This file contains environment variables needed by 
    openstack cli to authenticate with the ciao cluster.

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

You could also take a look at the ``./ciaorc`` file created on your
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
.. _hosts: https://github.com/clearlinux/clear-config-management/blob/master/examples/ciao/hosts
.. _groups_vars/all: https://github.com/clearlinux/clear-config-management/blob/master/examples/ciao/group_vars/all
.. _github: https://github.com/clearlinux/clear-config-management/tree/master/examples/ciao
