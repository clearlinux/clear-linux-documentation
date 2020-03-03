  .. _kata:

Kata Containers\*
#################

This tutorial describes how to install, configure, and run `Kata Containers`_
on |CL-ATTR|.

.. contents::
   :local:
   :depth: 1

Description
***********

Kata Containers is an open source project developing a lightweight
implementation of :abbr:`VMs (Virtual Machines)` that offer the speed of
containers and the security of VMs.

Prerequisites
*************

This tutorial assumes you have installed |CL| on your host system.
For detailed instructions on installing |CL| on a bare metal system, follow
the :ref:`bare metal installation tutorial<bare-metal-install-desktop>`.

If you have Clear Containers installed on your |CL| system, then follow the
:ref:`migrate Clear Containers to Kata Containers tutorial<kata_migration>`.

Update |CL| with the following command:

.. code-block:: bash

   sudo swupd update

Install Kata Containers
***********************

Kata Containers is included in the :file:`containers-virt` bundle.
To install the framework:

#. Install the containers-virt bundle:

   .. code-block:: bash

      sudo swupd bundle-add containers-virt

#. Reload and restart the Docker\* systemd service.

   .. code-block:: bash

      sudo systemctl daemon-reload
      sudo systemctl restart docker

Run Kata Containers
*******************

To use kata as the runtime for an individual container, add
:command:`--runtime=kata-runtime` to the :command:`docker run` command. For
example:

.. code-block:: bash

   sudo docker run --runtime=kata-runtime -ti busybox sh


To use kata as the default runtime for all Docker containers:

#. Set the default runtime for the Docker daemon:

   .. note:: 

      The method below uses a systemd drop-in configuration to add a
      command-line (CLI) parameter to the Docker daemon for setting the
      *default-runtime*. Alternatively, the default runtime can be set in the
      `Docker daemon configuration file
      <https://docs.docker.com/engine/reference/commandline/dockerd/#daemon-configuration-file>`_.
      The Docker daemon will not start if the *default-runtime* configuration
      in set multiple locations.

   .. code-block:: bash

      sudo mkdir -p /etc/systemd/system/docker.service.d/

      cat <<EOF | sudo tee /etc/systemd/system/docker.service.d/50-runtime.conf
      [Service]
      Environment="DOCKER_DEFAULT_RUNTIME=--default-runtime kata-runtime"
      EOF

#. Reload and restart the Docker\* systemd service.

   .. code-block:: bash

      sudo systemctl daemon-reload
      sudo systemctl restart docker

#. Verify the default runtime reported by docker is **kata-runtime**.

   .. code-block:: bash

      sudo docker info | grep "Default Runtime"
         Default Runtime: kata-runtime


Troubleshooting
===============

- If you are behind a HTTP proxy server, in a corporate setting for
  example, please refer to the `Docker proxy instructions`_.

- To change the Docker storage driver, see
  :ref:`additional-docker-configuration`.

- To check the version of |CL| on your system, enter: :command:`sudo swupd
  info`.

- |CL| versions before 27000 require manually configure Docker\* to use Kata
  Containers as shown in this tutorial.

- |CL| versions between 27000 and 31930 had a mechanism to automatically set
  kata as the default runtime for docker. To disable this mechanism run the
  commands below:

  .. code-block:: bash
     
     sudo systemctl mask docker-set-runtime.service
     sudo rm /etc/systemd/system/docker.service.d/50-runtime.conf
     sudo systemctl daemon-reload
     sudo systemctl restart docker.service


.. _Kata Containers: https://katacontainers.io/

.. _Docker proxy instructions: https://docs.docker.com/config/daemon/systemd/#httphttps-proxy
