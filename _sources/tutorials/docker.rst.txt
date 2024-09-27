.. _docker:

Docker\*
#########

|CL-ATTR| supports multiple containerization platforms, including a Docker
solution. |CL| has many unique features including a minimal default
installation, which makes it compelling to use as a host for container
workloads, management, and orchestration.

This tutorial covers:

.. contents:: :local:
   :depth: 1

.. note::

   This tutorial focuses on the installation of the Docker ecosystem.
   If you want to use |CL| as a Docker container image, refer to the
   official |CL| container image
   `published on Docker* Hub <https://hub.docker.com/_/clearlinux/>`_
   and our guide to :ref:`container-image-new`.

Prerequisites
*************

This tutorial assumes you have installed |CL| on your host system.
For detailed instructions on installing |CL| on a bare metal system, follow
the :ref:`bare metal installation instructions<bare-metal-install-server>`.

Before you install any new packages, update |CL| with the following command:

.. code-block:: bash

   sudo swupd update

Additionally, you should have:

* A basic understanding of Linux\* and Docker.

* |CL| environment that has transparent network access to the Internet.
  If you are behind a HTTP proxy server, in a corporate setting for example,
  please refer to the `Docker proxy instructions`_ .

Install the containers-basic bundle
***********************************

Software in |CL| is offered in the form of :ref:`bundles` to provide a
complete function. The *containers-basic* provides all the required software
packages to run Docker images as containers.

#. First, install the *containers-basic* bundle by running this
   :command:`swupd` command:

   .. code-block:: bash

      sudo swupd bundle-add containers-basic

#. Start the Docker daemon through systemd manager by running this command:

   .. code-block:: bash

      sudo systemctl start docker

   If you want Docker to start automatically on boot, enable the
   systemd service by running this command:

   .. code-block:: bash

      sudo systemctl enable docker

#. Finally, verify :command:`docker` has been installed by running this
   command and checking the version output for both *client* and *server*:

   .. code-block:: bash

      sudo docker version

Congratulations! At this point, you have a working installation of Docker
on |CL|. You are ready to start using container images on your system.

Integration with Kata Containers\* (optional)
*********************************************

`Kata Containers`_, is an open source project aiming to increase security
of containers by using a hardware-backed virtual machine container runtime
rather than software namespace containers that are provided by the standard
Docker *runc* runtime.

|CL| provides easy integration of the *kata-runtime* with Docker.
More information on installing and using  the *kata-runtime* may be found at :ref:`kata`.


.. note::

   The remaining sections of this tutorial are standard to Docker setup
   and configuration. If you are familiar with Docker basics, you do not
   need to continue reading. The following sections are provided here for
   sake of completeness.

.. _additional-docker-configuration:

Additional Docker configuration
*******************************

Perform additional Docker daemon configuration via a configuration file
typically located at :file:`/etc/docker/daemon.json`. |CL| features a
:ref:`stateless` system  so the configuration file :file:`daemon.json` does
*NOT* exist by default.

#. Create the :file:`daemon.json` by running this command:

   .. code-block:: bash

      sudo touch /etc/docker/daemon.json

   .. note::

      Refer to the `Docker documentation on daemon configuration`_ for the
      full list of available configuration options and examples.

#. For production systems, we follow Docker's recommendation to use the
   `OverlayFS storage driver`_ `overlay2`, shown below:

   .. code-block:: json

      {
         "storage-driver": "overlay2"
      }

   .. note::

      A testing version is found in `Docker Device Mapper storage driver`_.
      If using this storage driver, a warning message may appear: "usage of
      loopback devices is strongly discouraged for production use".

#. Save and close :file:`daemon.json`.

#. Once you've made any required changes, be sure to restart the
   Docker daemon through systemd manager by running this command:

   .. code-block:: bash

      sudo systemctl restart docker

Pulling and running an image from Docker Hub\*
**********************************************

`Docker Hub`_ is a publicly available container image repository which
comes pre-configured with Docker. In the example below we will pull and run
an the official Docker image for nginx\*, an open source reverse proxy server.

#. First, pull a container image from Docker Hub using the
   :command:`docker pull` command. Download the latest nginx\* Docker
   container image by running this command:

   .. code-block:: bash

      sudo docker pull nginx

#. Create and launch a new container using the :command:`docker run`
   command. Launch a nginx container by running this command:

   .. code-block:: bash

      sudo docker run --name test-nginx -d -p 8080:80 nginx

   .. note::

      Below is an explanation of switches used in the command above. For
      detailed :command:`docker run` switches and syntax, refer to the
      `Docker Documentation`_ .

      * The *--name* switch lets you provide a friendly name to
        target the container for future operations

      * The *-d* switch launches the container in the background

      * The *-p* switch allows the container's HTTP port (80) to be
        accessible from the |CL| host on port 8080

#. You can access the Welcome to Nginx! splash page running in the container
   by browsing to \http://127.0.0.1:8080 or by running this :command:`curl`
   command from your |CL| machine:

   .. code-block:: bash

      curl 127.0.0.1:8080

#. Finally, stop and delete the nginx container by running the
   :command:`docker stop` and :command:`docker rm` commands.

   .. code-block:: bash

      sudo docker stop test-nginx
      sudo docker rm test-nginx

Congratulations! At this point, you have successfully pulled a nginx
container image from `Docker Hub`_ and have run an example container.

Creating a Docker swarm cluster
*******************************

Clusters of Docker hosts are referred to as *swarms*.

The process in this tutorial can be repeated to install Docker on multiple
|CL| hosts with the intent to form a Docker swarm cluster.

The `Docker documentation on swarm key concepts`_ and
`Docker documentation on creating a swarm`_ can be referenced
for further instructions on setting up a swarm.

Related topics
**************

* `Docker Home`_
* `Docker Documentation`_
* `Docker Hub`_
* `Kata Containers`_


.. _Docker proxy instructions: https://docs.docker.com/config/daemon/systemd/#httphttps-proxy

.. _Docker documentation on daemon configuration: https://docs.docker.com/engine/reference/commandline/dockerd/#daemon-configuration-file

.. _Kata Containers: https://katacontainers.io/

.. _Docker Home: https://www.docker.com/

.. _Docker Documentation: https://docs.docker.com/

.. _Docker Hub: https://hub.docker.com/

.. _Docker documentation on swarm key concepts: https://docs.docker.com/engine/swarm/key-concepts/

.. _Docker documentation on creating a swarm: https://docs.docker.com/engine/swarm/swarm-tutorial/create-swarm/

.. _Configure direct lvm mode for production: https://docs.docker.com/storage/storagedriver/device-mapper-driver/

.. _OverlayFS storage driver: https://docs.docker.com/storage/storagedriver/overlayfs-driver/

.. _Docker Device Mapper storage driver: https://docs.docker.com/storage/storagedriver/device-mapper-driver/
