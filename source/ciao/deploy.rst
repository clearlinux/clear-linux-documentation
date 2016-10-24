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

.. note::

  The deployment machine is not a necessary part of the cluster; it could be
  the sysadmin's computer or a CI/CD server.

.. _prerequisites:

Prerequisites
=============
Ansible* uses :command:`ssh` to run commands on the remote nodes. In order to do
that, configure a user for passwordless SSH connections from the deployment
container to the cluster nodes. This user must also have passwordless sudo
privileges on the cluster nodes.

This guide uses a Docker* container to provide all the needed deployment tools;
in order to use it, you will need Docker in the machine you're using to orchestrate
your deployment.


Configure your cluster setup
============================
You will need to download the ciao example deployment as follows:

.. code-block:: console

  $ git clone https://github.com/01org/ciao.git

Once you're cloned the repo, continue working in the
`ciao/_DeploymentAndDistroPackaging/ansible/` directory

.. code-block:: console

   # cd $(pwd)/ciao/_DeploymentAndDistroPackaging/ansible/

Next, edit the configuration files for the cluster:

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
https://github.com/01org/ciao/tree/master/_DeploymentAndDistroPackaging/ansible/roles.

To start your cluster setup, we provide a ready-to-use Docker container.
Simply download it and run your setup:

.. code-block:: console

   $ docker pull clearlinux/ciao-deploy


You can later launch the container with:

.. code-block:: console

   $ docker run --privileged -v /dev/:/dev/
                -v /path/to/your/.ssh/key:/root/.ssh/id_rsa \
                -v $(pwd)/ciao:/root/ciao \
                -it clearlinux/ciao-deploy

.. note::

  The cotainer needs `--privileged -v /dev/:/dev/` in order to
  install your certificates in the `CNCI image`_.
  To learn more about the Docker options used, please refer to the
  `Docker* documentation`_.


Run the playbook
================
Once the variables and hosts file are configured, continue in the
`/root/ciao/_DeploymentAndDistroPackaging/ansible` directory and
start the deployment:

.. code-block:: console

   # cd /root/ciao/_DeploymentAndDistroPackaging/ansible

   # ansible-playbook -i hosts ciao.yml \
       --private-key=~/.ssh/id_rsa \
       --user=<REMOTE_USER>

.. note::

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
After Ansible is done with the setup, you can verify the cluster is ready
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

Then you could verify with the following command:

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
.. _CNCI image: https://github.com/01org/ciao/tree/master/networking/ciao-cnci-agent#cnci-agent
.. _Docker* documentation: https://docs.docker.com/engine/reference/commandline/run/
