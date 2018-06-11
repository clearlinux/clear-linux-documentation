.. _kata_migration:

Clear Containers to Kata Containers\* migration
###############################################

`Clear Containers`_ and `Kata Containers`_ can co-exist in the same system; at the moment both can be installed through the :file:`containers-virt bundle`. However, we recommend that you migrate to Kata Containers because Clear Containers is no longer maintained_ and will soon be deprecated on |CL|.

.. _Clear Containers: https://github.com/clearcontainers
.. _Kata Containers: https://github.com/kata-containers
.. _maintained: https://github.com/kata-containers/documentation/blob/master/Upgrading.md#maintenance-warning

To switch to Kata Containers in |CL|, complete the following:

Stop Clear Containers instances
*******************************

Before making any changes, all running Clear Containers must be stopped:

.. code-block:: bash

    for container in $(sudo docker ps -q); do sudo docker stop $container; done

.. note::

    This step assumes that Clear Containers is on a Docker\* system.

Manually migrate customized configuration files
***********************************************

There is no way to do an automatic migration of customized configuration files. If any change was made on the `Clear Containers configuration`_ which is also required on the `Kata Containers configuration`_, you must make such changes manually. 
Make any required changes before going any further, because all Clear Containers configuration files will eventually be removed.

.. _Clear Containers configuration: https://github.com/clearcontainers/runtime#configuration
.. _Kata Containers configuration: https://github.com/kata-containers/runtime#configuration

No need to remove Clear Containers packages
*******************************************
We recommend that you migrate to use Kata Containers as soon as possible before all Clear Containers packages are removed. You do not need to manually remove any Clear Containers packages.

Disable Clear Containers manager configuration
**********************************************

If present, any manager configuration should be removed:

.. code-block:: bash

    sudo rm /etc/systemd/system/docker.service.d/clear-containers.conf

Enable Kata Containers as default
*********************************

#.  Configure Docker to use the Kata Containers runtime by default.

.. code-block:: bash

    sudo mkdir -p /etc/systemd/system/docker.service.d/
    cat <<EOF | sudo tee /etc/systemd/system/docker.service.d/kata-containers.conf
    [Service]
    ExecStart=
    ExecStart=/usr/bin/dockerd -D --add-runtime kata-runtime=/usr/bin/kata-runtime --default-runtime=kata-runtime
    EOF

#.  Restart the Docker systemd services.

.. code-block:: bash

   sudo systemctl daemon-reload
   sudo systemctl restart docker

#.  Verify Docker is using Kata Containers.

.. code-block:: bash

   sudo docker info | grep -i 'default runtime'
   Default Runtime: kata-runtime

Run Kata Containers
*******************

.. code-block:: bash

    sudo docker run -ti busybox sh

**Congratulations!**

You've successfully set up Kata Containers on |CLOSIA|.
