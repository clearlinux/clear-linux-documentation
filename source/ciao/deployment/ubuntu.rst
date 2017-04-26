.. contents::

.. _ubuntu:

Deploying ciao via automation -- Ubuntu 16.04
#############################################

Cloud Integrated Advanced Orchestrator (``ciao``) is a new workload
scheduler designed to address limitations of current cloud OS projects.
Ciao provides a lightweight, fully TLS-based minimal config, is
workload-agnostic, easy to update, offers an optimized-for-speed
scheduler, and is currently optimized for OpenStack\*.

For more information, see https://clearlinux.org/ciao.

Environment
===========

For this example, we'll use a total of five nodes:
 - A deployment machine which will be used to run the playbooks.
 - A `controller`_ node which will be used to communicate with Keystone.
 - Two `compute nodes`_, which will spawn the VMs and containers.
 - A `network node`_ which will handle the networking for the workloads.

 Note: The deployment machine is not a necessary part of the cluster; it
 could be the sysadmin's computer or a CI/CD server.

Prerequisites
=============

Ansible* uses :command:`ssh` to run commands on the remote nodes. In
order to do that, the nodes must be configured to allow passwordless SSH
connections from the deployment machine to the cluster nodes. The user
should also have sudo privileges on the cluster nodes.

The deployment machine needs::

  Python 2.7
  Ansible >= 2.1
  Golang >= 1.7
  qemu-utils
  python-docker
  python-openstackclient
  Ansible ciao roles from ansible-galaxy

The managed nodes need::

  python 2.6 >=


Proxy
=====

If you are running behind a proxy, the following additional steps are needed:

In the deployment node
----------------------

Make sure apt can run. Edit ``/etc/apt/apt.conf`` (to install ansible and
dependencies), appending it with::

  Acquire::http::Proxy "http://yourproxyaddress:proxyport";
  Install the CIAO roles from ansible-galaxy:
  $ sudo -E ansible-galaxy -r requirements --ignore-certs

In the managed nodes
--------------------

Make sure apt can run. Edit ``/etc/apt/apt.conf``, appending it with::

  Acquire::http::Proxy "http://yourproxyaddress:proxyport";

Install Docker and make sure you can pull images. Edit
``/etc/systemd/system/docker.service.d/http-proxy.conf``, appending it
with::

  [Service]
  Environment="HTTP_PROXY=http://hostname:port/"
  Environment="HTTPS_PROXY=http://hostname:port/"
  Environment=”NO_PROXY=localhost,127.0.0.1,.example.com”

Note: replace the hostname and port of your proxy server and append your local domain name.

Reload and restart the docker daemon::

  $ sudo systemctl daemon-reload && sudo systemctl restart docker

  (OPTIONAL): You can download the docker images used in the CIAO deployment.
  $ sudo docker pull clearlinux/keystone
  $ sudo docker pull clearlinux/ciao-webui


Install the software
====================

Install ansible from ubuntu packages if the package version is >= 2.1.0;
otherwise, install it from pip (``pip install ansible``).

Install Dependencies in the deployment machine
----------------------------------------------

::

  python-docker (apt-get) or docker-py (pip)
  python-openstackclient (apt-get)
  qemu-utils (apt-get)

Download the ``clear-config-management`` project from github::

  $ git clone https://github.com/clearlinux/clear-config-management.git


Create the playbook
===================

The ``clear-config-management`` project includes some sample playbooks that
you may use and customize for your own needs. Start by making a copy of the
sample playbook into your home folder::

  # cp -r clear-config-management/examples/ciao ~/


Note: These files are also hosted in github

The relevant files in the playbook are the following:

  * The `ciao.yml`_ file is the master playbook file and includes a playbook
    for each component of the cluster.

  * The `hosts`_ file is the hosts inventory file and contains the IP
    addresses/FQDN of your nodes, grouped under the roles they will serve

  * The `groups_vars/all`_ file contains variables that will be applied
    to your ciao setup. The mandatory variables are already there; be
    sure to change the values accordingly to fit your environment

  * The ``ciao_guest_key`` value in :file:`groups_var/all` is the key
    to be used to connect to the VMs created by ciao; you can use the
    ``ssh-keygen`` command to create one.

A full list of available variables can be found in the :file:`defaults/main.yml`
file of each role at https://github.com/clearlinux/clear-config-management/tree/master/roles


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

Note: If you want the latest CIAO changes, change the  ``ciao_dev``
variable to ``True`` in the :file:`group_vars/all` file In the
``clear-config-management`` project.


Verify
======

After ansible is done with the setup, you can verify the cluster is ready
by running the following command on the controller node. Change the **username**,
**password**, **controller**, and **identity** values to match your setup, as
was specified in the ``groups_var/all`` file:

.. code-block:: console

   # ciao-cli -identity=https://ciao-controller.example.com:35357 \
   -username admin \
   -password secret \
   -controller=ciao-controller.example.com
   # node status
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
.. _ciao.yml: https://github.com/clearlinux/clear-config-management/blob/master/examples/ciao/ciao.yml
.. _hosts: https://github.com/clearlinux/clear-config-management/blob/master/examples/ciao/hosts
.. _groups_vars/all: https://github.com/clearlinux/clear-config-management/blob/master/examples/ciao/group_vars/all
.. _github: https://github.com/clearlinux/clear-config-management/tree/master/examples/ciao
