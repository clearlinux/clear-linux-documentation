.. _kata_migration:

Clear Containers to Kata Containers migration
#############################################

`Clear Containers`_ and `Kata Containers`_ can co-exist in the same system; at the moment both can be installed through the :file:`containers-virt bundle`. However, it is recommended to migrate to Kata Containers as Clear Containers is no longer maintained_ and will soon be deprecated on |CL|

.. _Clear Containers: https://github.com/clearcontainers
.. _Kata Containers: https://github.com/kata-containers
.. _maintained: https://github.com/kata-containers/documentation/blob/master/Upgrading.md#maintenance-warning

To switch to Kata Containers in |CL|, complete the following:

Stop Clear Containers instances
*******************************

Before doing any change, all running Clear Containers must be stopped:

.. code-block:: bash

    $ for container in $(sudo docker ps -q); do sudo docker stop $container; done

..
    NOTE: It is assumed Clear Containers is on a Docker system.

Manually migrate customized configuration files
***********************************************

There is no way to do an automatic migration of customized configuration files, thus if any change was made on the `Clear Containers configuration`_ and is also required on the `Kata Containers configuration`_, such changes should be done manually. Please note this step should be done before going any further as all Clear Containers configuration files will eventually be removed from the system it is installed in.

.. _Clear Containers configuration: https://github.com/clearcontainers/runtime#configuration
.. _Kata Containers configuration: https://github.com/kata-containers/runtime#configuration

No need to remove Clear Containers packages
*******************************************
Clear Linux still supports Clear Containers, but as said before, it will soon be deprecated. All systems with versions above 22860 should have both Clear Containers and Kata Containers, but changes are to be expected on the bundle containing them (containers-virt) meaning Clear Containers will soon be removed. It is recommended to migrate to use Kata Containers as soon as possible before all Clear Containers packages are removed. In the meantime, there is no need to manually remove any Clear Containers package.

Disable Clear Containers manager configuration
**********************************************

If present, any manager configuration should be removed:

.. code-block:: bash

    $ sudo rm /etc/systemd/system/docker.service.d/clear-containers.conf

Enable Kata Containers as default
*********************************

As mentioned, Clear Containers and Kata Containers can co-exist in the same system, meaning either runtime must be defined as default before running containers. Kata Containers can be configured to be the default as follows:

Configure Docker* to use the Kata Containers runtime by default

.. code-block:: bash

    $ sudo mkdir -p /etc/systemd/system/docker.service.d/
    $ cat <<EOF | sudo tee /etc/systemd/system/docker.service.d/kata-containers.conf
    [Service]
    ExecStart=
    ExecStart=/usr/bin/dockerd -D --add-runtime kata-runtime=/usr/bin/kata-runtime --default-runtime=kata-runtime
    EOF

Restart the Docker* systemd services

.. code-block:: bash

   $ sudo systemctl daemon-reload
   $ sudo systemctl restar docker

Verify Docker* is in fact using Kata Containers

.. code-block:: bash

   $ sudo docker info | grep -i 'default runtime'
   Default Runtime: kata-runtime

Run Kata Containers
*******************

.. code-block:: bash

    $ sudo docker run -ti busybox sh

**Congratulations!**

You've successfully migrated to use Kata Containers on |CLOSIA|.
