  .. _kata:

Install Kata Containers\*
#########################

This tutorial describes how to install, configure, and run `Kata Containers`_
on |CLOSIA|. Kata Containers is an open source project developing a
lightweight implementation of :abbr:`VMs (Virtual Machines)` that offer the
speed of containers and the security of VMs.

Prerequisites
*************

This tutorial assumes you have installed |CL| on your host system.
For detailed instructions on installing |CL| on a bare metal system, follow
the :ref:`bare metal installation tutorial<bare-metal-install>`.

If you have Clear Containers installed on your |CL| system, then follow the
:ref:`migrate Clear Containers to Kata Containers tutorial<kata_migration>`.

Before you install any new packages, update |CL| with the following command:

.. code-block:: bash

   sudo swupd update

Install Kata Containers
***********************

Kata Containers is included in the :file:`containers-virt` bundle. To install the
framework, enter the following command:

.. code-block:: bash

   sudo swupd bundle-add containers-virt

Configure Docker\* to use Kata Containers by default.

.. code-block:: bash

   sudo mkdir -p /etc/systemd/system/docker.service.d/
   cat <<EOF | sudo tee /etc/systemd/system/docker.service.d/51-runtime.conf
   [Service]
   Environment="DOCKER_DEFAULT_RUNTIME=--default-runtime kata-runtime"
   EOF

Restart the Docker and Kata Containers systemd services.

.. code-block:: bash

   sudo systemctl daemon-reload
   sudo systemctl restart docker

Run Kata Containers
*******************

.. code-block:: bash

   sudo docker run -ti busybox sh

.. note::

   If you use a proxy server and your proxy environment variables are already
   set, run the following commands as a shell script to configure Docker:

   .. code-block:: bash

      docker_service_dir="/etc/systemd/system/docker.service.d/"
      sudo mkdir -p "$docker_service_dir"
      cat <<EOF | sudo tee "$docker_service_dir/proxy.conf"
      [Service]
      Environment="HTTP_PROXY=$http_proxy"
      Environment="HTTPS_PROXY=$https_proxy"
      EOF
      echo "Reloading unit files and starting docker service"
      sudo systemctl daemon-reload
      sudo systemctl restart docker
      sudo docker info

**Congratulations!**

You've successfully installed and set up Kata Containers on |CLOSIA|.

More information about Docker
*****************************

Docker on |CLOSIA| provides a :file:`docker.service` file to start the Docker
daemon. The daemon will use runc or kata-runtime depending on the
environment:

*  If you are running |CL| on bare metal or on a VM with Nested
   Virtualization activated, Docker uses kata-runtime as the
   default runtime.
*  If you are running |CL| on a VM without Nested Virtualization,
   Docker uses runc as the default runtime.

You do not need to manually configure the runtime for Docker, because
it automatically uses the runtime supported by the system.

Check which runtime your system is using with the command:

.. code-block:: bash

   sudo docker info | grep runtime

.. _Kata Containers: https://katacontainers.io/
