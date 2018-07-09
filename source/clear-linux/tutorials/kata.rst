  .. _kata:

Install Kata Containers\*
#######################

This tutorial describes how to install, configure and run Kata Containers\* on
|CLOSIA|. Kata Containers\* is an open source project and community working to
build a standard implementation of lightweight Virtual Machines (VMs) that feel
and perform like containers, but provide the workload isolation and security
advantages of VMs. Kata Containers\* is available in Clear Linux versions above 23380.

Prerequisites
*************

This tutorial assumes you have installed |CL| on your host system.
For detailed instructions on installing |CL| on a bare metal system, visit
the :ref:`bare metal installation tutorial<bare-metal-install>`.

Before you install any new packages, update |CL| with the following command:

.. code-block:: bash

   sudo swupd update

Install Kata Containers\*
***********************

Kata Containers\* is included in the :file:`containers-virt` bundle. To install the
framework, enter:

.. code-block:: bash

   sudo swupd bundle-add containers-virt

Configure Docker to use Kata Containers\* by default

.. code-block:: bash

   sudo mkdir -p /etc/systemd/system/docker.service.d/
   cat <<EOF | sudo tee /etc/systemd/system/docker.service.d/kata-containers.conf
   [Service]
   ExecStart=
   ExecStart=/usr/bin/dockerd -D --add-runtime kata-runtime=/usr/bin/kata-runtime --default-runtime=kata-runtime
   EOF
   
Restart the Docker\* and Kata Containers\* systemd services

.. code-block:: bash

   sudo systemctl daemon-reload
   sudo systemctl restart docker

Run Kata Containers\*
*******************

.. code-block:: bash

   sudo docker run -ti busybox sh

**Congratulations!**

You successfully installed and set up Kata Containers\* on |CLOSIA|.

More information about Docker\* in |CLOSIA|.
#############################################

Docker\* on |CLOSIA| provides a docker.service service file to start the Docker\*
daemon. The daemon will use runc or cc-runtime depending on the environment:

If you are running |CL| on baremetal or on a VM with Nested
Virtualization activated, Docker\* will use cc-runtime as the default runtime.
If you are running |CL| on a VM without Nested Virtualization, Docker\*
will use runc as the default runtime. It is not necessary to configure Docker\*
to use cc-runtime manually since Docker\* itself will automatically use this
runtime on systems that support it.

To check which runtime your system is using, run:

.. code-block:: bash

   sudo docker info | grep runtime
