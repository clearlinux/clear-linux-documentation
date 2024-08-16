.. _kata_migration:

Migrate Clear Containers to Kata Containers\*
#############################################

This tutorial explains how to migrate from Clear Containers to Kata Containers.

.. contents::
   :local:
   :depth: 1

Description
***********

`Clear Containers`_ and `Kata Containers`_ can co-exist in the same system.
Both can be installed through the :command:`containers-virt` bundle. However,
we recommend that you migrate to Kata Containers because Clear Containers is no
longer `maintained`_ and will soon be deprecated on |CL-ATTR|.

Prerequisites
*************

*  Clear Containers is on a Docker\* system.
*  Kata Containers is installed. See :ref:`kata`.


Stop Clear Containers instances
*******************************

As an unprivileged user, stop all running instances of Clear Containers:

.. code-block:: bash

    for container in $(sudo docker ps -q); do sudo docker stop $container; done


Manually migrate customized configuration files
***********************************************

If you have made changes to your `Clear Containers configuration`_, review
those changes and decide whether to manually apply those changes to your
`Kata Containers configuration`_.

Make any required changes before continuing this process.

.. note::

  You do not need to manually remove any Clear Containers packages.


Enable Kata Containers as default
*********************************

#. Configure Docker to use the Kata Containers runtime by default.

   .. code-block:: bash

      sudo mkdir -p /etc/systemd/system/docker.service.d/
      cat <<EOF | sudo tee /etc/systemd/system/docker.service.d/51-runtime.conf
      [Service]
      Environment="DOCKER_DEFAULT_RUNTIME=--default-runtime kata-runtime"
      EOF

#. Restart the Docker systemd services.

   .. code-block:: bash

      sudo systemctl daemon-reload
      sudo systemctl restart docker

#. Verify Docker is using Kata Containers.

   .. code-block:: bash

      sudo docker info | grep -i 'default runtime'
      Default Runtime: kata-runtime

Run Kata Containers
*******************

Use the following command:

.. code-block:: bash

   sudo docker run -ti busybox sh

**Congratulations!**

You've successfully migrated from Clear Containers to Kata Containers.


.. _Clear Containers: https://github.com/clearcontainers

.. _Kata Containers: https://github.com/kata-containers

.. _maintained: https://github.com/kata-containers/documentation/blob/master/Upgrading.md#maintenance-warning

.. _Clear Containers configuration: https://github.com/clearcontainers/runtime#configuration

.. _Kata Containers configuration: https://github.com/kata-containers/runtime#configuration

