.. _dbrs:

Database Reference Stack
########################

This guide describes the hardware and installation requirements for using the
:abbr:`DBRS (Database Reference Stack)`, along with getting started configuration examples, using |CL-ATTR| as the host system.

.. contents::
   :local:
   :depth: 1

Overview
********

The Database Reference Stack is integrated, highly-performant, open source,
and optimized for 2nd generation Intel® Xeon® Scalable Processors and Intel®
Optane™ DC Persistent Memory. This open source community release is part of
an effort to ensure developers have easy access to the features and
functionality of Intel Platforms.

Stack Features
==============

Current supported  database applications are Cassandra* and Redis*, which
have been enabled for `Intel Optane DC PMM`_.

DBRS with Cassandra can be deployed as a standalone container or inside a
Kubernetes* cluster.

The Redis stack application is enabled for a multinode Kubernetes
environment, using AEP persistent memory DIMM in fsdax mode for storage.

.. note::

   The Database Reference Stack is a collective work, and each piece
   of software within the work has its own license.  Please see the
   `DBRS Terms of Use`_ for more details about licensing and usage of the Database Reference Stack.


Hardware Requirements
*********************

* Intel Xeon Scalable Platform with Intel C620 chipset series
* 2nd Gen Intel Xeon Scalable processor CPU (Intel Optane DC PMM-enabled stepping) Provides cache & memory control.  Intel Optane DC persistent memory works only on systems powered by 2nd Generation Intel® Xeon® Platinum or Gold processors.
* BIOS with Reference Code
* Intel Optane DC persistent memory

Hardware configuration used in stacks development
=================================================

* Intel® Server System R2208WFTZSR
* BIOS with Reference Code
  * BIOS ID: SE5C620.86B.0D.01.0438.032620191658
  * BMC Firmware: 1.94.6b42b91d
  * Apache Pass Firmware: 1.2.0.5310
* 2x Intel Xeon Platinum 8268 Processor
* Intel SSD DC S5600 Series 960GB 2.5in SATA Drive
* 64 GB RAM - Distributed in 4x 16 GB DDR4 DIMM's
* 2x Intel Optane DC Persistent Memory 256GB Module
* 1-1-1 Layout 8 Optane : 1 RAM ratio


.. list-table:: **Table 1. IMC**
   :widths: 16,16,16,16,16,16
   :header-rows: 1

   * - Channel 2
     - Channel 2
     - Channel 1
     - Channel 1
     - Channel 0
     - Channel 0

   * - Slot 1
     - Slot 0
     - Slot 1
     - Slot 0
     - Slot 1
     - Slot 0

   * -
     - 256 AEP
     -
     - 16 GB DRAM
     -
     - 16 GB DRAM

Firmware configuration
**********************

.. important::

   When updating DCPMM Firmware, all DCPMM parts must be in the same mode (you cannot mix 1LM and 2LM parts).

The latest firmware download for the Intel® Server System S2600WF Family is available at the `Intel Download Center`_

Firmware Update Steps
=====================

#. Unzip the contents of the update package and copy all files to the root directory of a removable media (USB flash drive).
#. Insert the USB flash drive to any available USB port on the system to be updated.
#. Boot to EFI shell.
#. Input "fsx(x:0,1,...):" to enter into your usb disk
#. Run "startup.nsh"
#. After update BMC firmware, system BIOS, ME firmware,FD, FRUSDR, system will reboot automatically.


If Intel Optane DC Persistent Memory is installed, run startup.nsh a second time after the first reboot to upgrade Intel Optane DC Persistent Memory Firmware:

* Boot to EFI shell.
* Input "fsx(x:0,1,...):" to enter into your usb disk
* Run "startup.nsh" again to update the corresponding AEP FW.


Hardware Configuration
**********************


Online Resources
================

Before going through the configuration steps, we strongly recommend visiting the following resources and wikis to have a broader understanding of what is being done

* `Quick Start Guide`_ Configure Intel Optane DC Persistent Memory Modules on Linux
* `Managing NVDIMMs`_
* `Configure, Manage, and Profile`_ Intel Optane DC Persistent Memory Modules

Optane DIMM Configuration
=========================

The persistent memory DIMMs can be configured in devdax or fsdax mode. The use case to enable database stack on a kubernetes environment currently only support fsdax mode.

Configuration Steps
===================

.. important::

   Run the following steps with root privileges (sudo) as shown in the examples


#. To configure Optane DIMMs for App direct mode run this command and then reboot the system

   .. code-block:: bash

      sudo ipmctl create -goal PersistentMemoryType=AppDirect


#. Next, list the pmem devices in the system

   .. code-block:: bash

      sudo ndctl list –N


#. Create namespaces based on the regions and set mode as fsdax  -- use the names of the regions listed in previous step as the –-region parameter

   .. code-block:: bash

      sudo ndctl create-namespace --region=region0 --mode=fsdax


#. Create the filesystem and mount it. We are using /mnt/dax{#} as a convention in this guide to mount our devices

   .. code-block:: bash

      sudo mkfs.ext4 /dev/pmem{n}
      sudo mount -o dax /dev/pmem0 /mnt/dax0


Running DBRS with Cassandra*
***************************

DBRS with Cassandra can be deployed as a standalone container or inside
Kubernetes\*. Instructions for both cases is included here. Note that you can
use the released `Docker image with Cassandra`_ (Docker\* examples below).
These instructions provide a baseline for creating your own container image.
If you are using the released image, skip this section.

.. important::

   At the initial release of DBRS, Cassandra is considered to be Engineering Preview release quality and may not be suitable for production release.  Please take this into consideration when planning your project.



Build the DBRS with Cassandra container
=======================================

To build the container with Cassandra, you must build cassandra-pmem, and then build the container using the :command:`docker build` command. We are using |CL| as our container host as well as the OS in the container.

Build cassandra-pmem
====================

.. important::

   At the initial release of DBRS, the pmem-csi driver is considered to be Engineering Preview release quality and may not be suitable for production release.  Please take this into consideration when planning your project.


In the `DBRS github repository`_, there is a file called `build-cassandra-pmem.sh`_, which handles all the requirements for compiling cassandra-pmem for Dockerfile usage. The dependencies for this build can be installed with :command:`swupd`.

.. code-block:: bash

   sudo swupd bundle-add c-basic java-basic devpkg-pmdk pmdk


Once installed, we run the script

.. code-block:: bash

   ./build-cassandra-pmem.sh


At the completion of the build you will have a file called :file:`cassandra-pmem-build.tar.gz`. Place this file in the same directory with the Dockerfile  to build the Docker image.

Build the Docker container
==========================

To build the Docker image, run the Dockerfile in the same directory with the :file:`cassandra-pmem-build.tar.gz`

.. code-block:: bash

   docker build --force-rm --no-cache -f Dockerfile -t $build_image_name .


Once it completes, the Docker image is ready to be used.

Deploy Cassandra PMEM as a standalone container
===============================================

Requirements
------------

To deploy Cassandra PMEM, you must meet the following requirements

* PMEM memory must be configured in `devdax` or `fsdax`    mode. The container image is able to handle both modes and depending on the PMEM mode, the mount points inside the container must be different.
* In order to make available `devdax` pmem devices inside the container you must use the `--device` directive. Internally the container always uses :command:`/dev/dax0.0`, so the mapping should be: :command:`--device=/dev/<host-device>:/dev/dax0.0`
* In a similar fashion for `fsdax` we need the device to be mapped to :command:`/mnt/pmem` inside the container: :command:`--mount type=bind,source=<source-mount-point>,target=/mnt/pmem`


Preparing PMEM for container use
--------------------------------

The cassandra-pmem image is capable of using both `fsdax`   and `devdax`, the necessary steps to configure the PMEM to work with cassandra are documented here.

fsdax
-----

Verify that the PMEM is in `fsdax` mode

.. code-block:: bash

   sudo ndctl list -u

.. code-block:: console

  {
    "dev":"namespace0.0",
    "mode":"fsdax",
    "map":"mem",
    "size":"4.00 GiB (4.29 GB)",
    "sector_size":512,
    "blockdev":"pmem0"
  }


If for some reason the device is not in `fsdax` mode you can reconfigure the namespace as follows:

.. code-block:: bash

   sudo `ndctl create-namespace -fe <namespace-name>  --mode=fsdax`


Once the PMEM namespace is configured, you will see a device named :file:`/dev/pmem{0-9}`. We will create a filesystem on that device. The filesystem could be `ext4` or `xfs`, for this example we are going to use `ext4`.

.. code-block:: bash

   sudo mkfs.ext4 /dev/pmem0

.. code-block:: console

   mke2fs 1.45.2 (27-May-2019)
   Creating filesystem with 1031680 4k blocks and 258048 inodes
   Filesystem UUID: 303c03f5-ac4e-4462-8bf9-bc6b0fae53fe
   Superblock backups stored on blocks:
	   32768, 98304, 163840, 229376, 294912, 819200, 884736

   Allocating group tables: done
   Writing inode tables: done
   Creating journal (16384 blocks): done
   Writing superblocks and filesystem accounting information: done


Once the filesystem is created, we mount it with the dax option

.. code-block:: bash

   sudo mount /dev/pmem0 /mnt/pmem -o dax


When using `fsdax` mode cassandra-pmem creates a pool file on the pmem mountpoint, so the `jvm.options` configuration should look like the output below:

.. code-block:: console

   -Dpmem_path=/mnt/pmem/cassandra_pool
   -Dpool_size=3221225472



Where
* `pmem_path` is the path to the pool file, which should include the path itself and the file name
* `pool_size` is the size of the pool file in bytes. If you are using the `Docker image with Cassandra`_ you can pass this value as an environment variable to the container runtime in Gb and the calculation is done automatically.

Is important to note that when creating the filesystem in the pmem device certain amount of space of the device is used by the filesystem metadata so the pool_size should be smaller than the total pmem namespace size.

When using the `Docker image with Cassandra`_, the file `jvm.options` is automatically populated with the environment variables `CASSANDRA_PMEM_POOL_NAME` and `CASSANDRA_FSDAX_POOL_SIZE_GB`.

devdax
------
We need to verify the device we want to use is in `devdax` mode

.. code-block:: bash

   sudo ndctl create-namespace -fe namespace0.0  --mode=devdax

.. code-block:: console

   {
     "dev":"namespace0.0",
     "mode":"devdax",
     "map":"dev",
     "size":"3.94 GiB (4.23 GB)",
     "uuid":"cb738cc7-711d-4578-bebf-1f7ba02ca169",
     "daxregion":{
     "id":0,
     "size":"3.94 GiB (4.23 GB)",
     "align":2097152,
     "devices":[
       {
         "chardev":"dax0.0",
         "size":"3.94 GiB (4.23 GB)"
       }
     ]
    },
    "align":2097152
   }


If needed, we can reconfigure it using :command:`ndctl create-namespace -fe <namespace-name>  --mode=devdax`.

Before using a `devdax` device we need to clear the device:

.. code-block:: bash

   sudo pmempool rm -vaf /dev/dax0.0


The `jvm.options` configuration for Cassandra should look like the following:

.. code-block:: console

   -Dpmem_path=/dev/dax0.0
   -Dpool_size=0

Where
* pmem_path is the `devdax` device.
* pool_size=0 indicates to use the entire `devdax` device.

When using the `Docker image with Cassandra`_, the file `jvm.options` is automatically populated.


Run the DBRS Container
======================

Replace `<image-id>` in the following commands with the name of the image you are using.

In `devdax` mode:

.. code-block:: bash

   docker run --device=/<devdax-device>:/dev/dax0.0 --ulimit nofile=262144:262144 -p 9042:9042 -p 7000:7000 -it --name cassandra-test <image-id>


In `fsdax` mode:

.. code-block:: bash

   docker run --mount type=bind,source=/<fsdax-mountpoint>,target=/mnt/pmem  --ulimit nofile=262144:262144 -p 9042:9042 -p 7000:7000 -it -e 'CASSANDRA_FSDAX_POOL_SIZE_GB=<fsdax-pool-size-in-gb>' --name cassandra-test <image-id>


Container Configuration
=======================

Using environment variables
---------------------------

The container listens on the primary container IP address, but if required, some parameters can be provided as environment variables using `--env`.

* `CASSANDRA_CLUSTER_NAME`  Cassandra cluster name, by default `Cassandra Cluster`
* `CASSANDRA_LISTEN_ADDRESS`  Cassandra listen address
* `CASSANDRA_RPC_ADDRESS`  Cassandra RPC address
* `CASSANDRA_SEED_ADDRESSES`  A comma separated list of hosts in the cluster, if not provided, cassandra is going to run as a single node.
* `CASSANDRA_SNITCH`  The snitch type for the cluster, by default it is `SimpleSnitch`, for more complex snitches you can mount your own `cassandra-rackdc.properties` file.
* `LOCAL_JMX`  If set to `no` the JMX service will listen on all IP addresses, the default is `yes` and listens just on localhost 127.0.0.1
* `JVM_OPTS` When set you can pass additional arguments to the JVM for cassandra execution, for example for specifying memory heap sizes `JVM_OPTS=-Xms16G -Xmx16G -Xmn12G`

When using PMEM in `fsdax` mode, there are some parameters to control the allocation of memory:


* `CASSANDRA_FSDAX_POOL_SIZE_GB`  The size of the fsdax pool in GB, if it is not specified the pool size is `1`
* `CASSANDRA_PMEM_POOL_NAME`  The filename of the pool created in PMEM, by default `cassandra_pool`

Using custom files
------------------

For more complex deployments it is also possible to provide custom `cassandra.yaml` and `jvm.options` files as shown below:

.. code-block:: bash

   docker run --mount type=bind,source=/<fsdax-mountpoint>,target=/mnt/pmem -it  --ulimit nofile=262144:262144 --mount type=bind,source=/<path-to-file>/cassandra.yaml,target=/workspace/cassandra/conf/cassandra.yaml --mount type=bind,source=/path-to-file>/jvm.options,target=/workspace/cassandra/conf/jvm.options --name cassandra-custom-files


Clustering
==========

For a simple two node cluster using PMEM in `fsdax` mode on both containers:

Node 1
------

* IP: 172.17.0.2
* PMEM mountpoint: /mnt/pmem1

.. code-block:: bash

   docker run --mount type=bind,source=/mnt/pmem1,target=/mnt/pmem  --ulimit nofile=262144:262144 -it -e 'CASSANDRA_FSDAX_POOL_SIZE_GB=2' -e 'CASSANDRA_SEED_ADDRESSES=172.17.0.2:7000,172.17.0.3:7000'  --name cassandra-node1 <image-id>


Node 2
------

* IP: 172.17.0.3
* PMEM mountpoint: /mnt/pmem2

.. code-block:: bash

   docker run --mount type=bind,source=/mnt/pmem2,target=/mnt/pmem  --ulimit nofile=262144:262144 -it -e 'CASSANDRA_FSDAX_POOL_SIZE_GB=2' -e 'CASSANDRA_SEED_ADDRESSES=172.17.0.2:7000,172.17.0.3:7000'  --name cassandra-node2 <image-id>


Once both nodes are running, eventually the gossip is settled and we can use `nodetool` on either container to check cluster status.

.. code-block:: bash

   docker exec -it <container-id> bash /workspace/cassandra/bin/nodetool status


The output should look similar to this:

.. code-block:: console


   Datacenter: datacenter1
   =======================
   Status=Up/Down
   |/ State=Normal/Leaving/Joining/Moving
   --  Address     Load       Tokens       Owns (effective)  Host ID                               Rack
   UN  172.17.0.3  0 bytes    256          100.0%            22387159-8192-41cf-8b6c-8bf0e1049eb7  rack1
   UN  172.17.0.2  0 bytes    256          100.0%            219b56ba-c07c-400b-a018-a5dc20edeb09  rack1



Persistence
===========

By default you can access the data written to Cassandra  as long as the container exists. In order to persist the data past that, you can mount volumes or bind mounts on :file:`/workspace/cassandra/data` and :file:`/workspace/cassandra/logs` and in this way the data can still be accessed once the container is deleted.

Deploy A Cassandra-PMEM cluster on Kubernetes*
**********************************************

Many containerized workloads are deployed in clusters and orchestration software like Kubernetes can be useful. We will use the `cassandra-pmem-helm`_ Helm* chart in this example.

Requirements
============

* Kubectl* must be configured to access the Kubernetes Cluster

* A Kubernetes cluster with `pmem-csi`_ enabled

* The Kubernetes cluster must have `helm`_ and tiller installed

* PMEM hardware

.. important::

   When selecting the `fsdax` pool file size, it is important to consider that when requesting a volume, certain amount of space is used by the filesystem metadata on that volume and the available space turns out to be less than total amount specified. Taking this into consideration the size of the fsdax pool file should be ~2G less than the total volume size requested.


Configuration
=============

In order to configure the Cassandra PMEM cluster some variables and values are provided. These values are set in :file:`test/cassandra-pmem-helm/values.yaml`, and can be modified according to your specific needs. A summary of those parameters is shown below:


* clusterName:  The cluster Name set across all deployed nodes
* replicaCount:  The number of nodes in the cluster to be deployed
* image.repository:  The address of the container registry where the cassandra-pmem image should be pulled
* image.tag:  The tag of the image to be pulled during deployment
* image.name:  The name of the image to be pulled during deployment
* pmem.containerPmemAllocation:  The size of the persistent volume claim to be used as heap, it uses the storage class `pmem-csi-sc-ext4` from pmem-csi  The size of the fsdax pool to be created inside the persistent volume claim, in practice it shuld be `1G` less than pmem.containerPmemAllocation
* pmem.fsdaxPoolSizeInGB: The size of the fsdax pool to be created inside the persistent volume claim, in practice it should be 1G less than pmem.containerPmemAllocation
* enablePersistence: If set to `true`, K8s persistent volumes are deployed to store data and logs
* persistentVolumes.logsVolumeSize:  The size of the persistent volume used for storing logs on each node, the default is `4G`
* persistentVolumes.dataVolumeSize:  The size of the persistent volume used for storing data on each node, the default is `4G`
* persistentVolumes.logsStorageClass:  Storage class used by  the logs pvc, by default it uses `pmem-csi-sc-ext4`
* persistentVolumes.dataStorageClass:  Storage class used by  the data pvc, by default it uses `pmem-csi-sc-ext4`
* provideCustomConfig:  If set to `true`, it mounts all the files located on `<helm-chart-dir>/files/conf` on `/workspace/cassandra/conf` inside each container in order to provide a way to customize the deployment beyond the options provided here
* exposeJmxPort:  When set to `true` it exposes the JMX port as part of the Kubernetes headless service. It should be used together with `enableAdditionalFilesConfigMap` in order to provide authentication files needed for JMX when the remote connections are allowed. When set to `false` only local access through 127.0.0.1 is granted and no additional authentication is needed.
* enableClientToolsPod:  If set to `true`, an additional pod independent from the cluster is deployed, this pod contains various Cassandra client tools and mounts test profiles located under `<helm-chart-dir>/files/testProfiles` to `/testProfiles` inside the pod. This pod is useful to test and launch benchmarks
* enableAdditionalFilesConfigMap:  When set to true, it takes the files located in `<helm-chart-dir>/files/additionalFiles` and mount them in `/etc/cassandra` inside the pods, some additional files for cassandra can be stored here, such as JMX auth files
* jvmOpts.enabled:  If set to `true` the environment variable `JVM_OPTS` is overriden with the value provided on jvmOpts.value
* jvmOpts.value: Sets the value of the environment variable `JVM_OPTS`, in this way some java runtime configurations can be provided such as RAM heap usage
* resources.enabled:  if set to `true`, the resource constraints are set on each pod using the values under resources.requests and resources.limits
* resources.requests.memory: Initial resource allocation for each pod in the cluster
* resources.request.cpu: Initial resource allocation for each pod in the cluster
* resources.limits.memory:  Limits for memory allocation for each pod in the cluster
* resources.limits.cpu: Limits for cpu allocation for each pod in the cluster

Installation
============

Once all the configurations are set, to install the chart inside a given Kubernetes cluster you must run:

.. code-block:: bash

   helm install ./cassandra-pmem-helm


Eventually all the given nodes will be shown as running using :command:`kubectl get pods`.


Running DBRS with Redis
***********************

The Redis stack application is enabled for a multinode Kubernetes environment using Intel Optane DCPMM persistent memory DIMMs in fsdax mode for storage.

The source code used for this application can be found in the `Github repository`_

The following examples will use the `Docker image with Redis`_.  You can also build your own image with Docker by using the :file:`Dockerfile` and running with this command

.. code-block:: bash

   docker build --force-rm --no-cache -f Dockerfile -t ${DOCKER_IMAGE} .



Single node
===========

Prior to starting the container, you will need to have the Intel Optane DCPMM module in fsdax with a file system and mounted in `/mnt/dax0` as shown above.

Use the following to start the container, replacing ${DOCKER_IMAGE} with the name of the image you are using.

.. code-block:: bash

   docker run --mount type=bind,source=/mnt/dax0,target=/mnt/pmem0 -i -d --name pmem-redis ${DOCKER_IMAGE} --nvm-maxcapacity 200 --nvm-dir /mnt/pmem0 --nvm-threshold 64 --protected-mode no




Redis Operator in a Kubernetes cluster
======================================

After setting up :ref:`kubernetes` in |CL|, you will need to enable it to support DCPMM using the pmem-cls driver.  To install the driver follow the instructions in the `pmem-csi`_ repository.

We are using source code from the `Redis operator`_ .

.. note::

   If you already have a redis-operator, you will need to delete it before installing a new one.




After installing the operator you are ready to deploy redisfailover instances using a yaml file, like this `example for persistent memory`_. You can download it and change the source of the image to reflect your environment. We have named our yaml `redis-failover.yml`

To start a redisfailover instance in Kubernetes run the following

.. code-block:: bash

   kubectl create -f redis-failover.yml


.. important::

   There is a `known issue`_ in which the sentinels do not have enough memory to create the InitContainer. The current workaround is to build the image increasing the limits for the InitContainer memory to 32Mb




.. _Intel Download Center: https://downloadcenter.intel.com/download/28695/Intel-Server-Board-S2600WF-Family-BIOS-and-Firmware-Update-Package-for-UEFI

.. _Quick Start Guide: https://software.intel.com/en-us/articles/quick-start-guide-configure-intel-optane-dc-persistent-memory-on-linux

.. _Managing NVDIMMs: https://docs.pmem.io/ndctl-users-guide/managing-nvdimms

.. _Configure, Manage, and Profile: https://software.intel.com/en-us/articles/configure-manage-and-profile-intel-optane-dc-persistent-memory-modules

.. _DBRS github repository: https://github.com/clearlinux/dockerfiles/tree/master/stacks/dbrs

.. _build-cassandra-pmem.sh: https://github.com/clearlinux/dockerfiles/tree/master/stacks/dbrs/cassandra/scripts/

.. _cassandra-pmem-helm: https://github.com/clearlinux/dockerfiles/tree/master/stacks/dbrs/cassandra/cassandra-pmem-helm

.. _helm: https://helm.sh/

.. _Github repository: https://github.com/pmem/pmem-redis

.. _Redis operator: https://github.com/spotahome/redis-operator

.. _example for persistent memory: https://github.com/spotahome/redis-operator/blob/master/example/redisfailover/pmem.yaml

.. _known issue: https://github.com/spotahome/redis-operator/issues/176

.. _Docker image with Cassandra: https://hub.docker.com/r/clearlinux/stacks-dbrs-cassandra

.. _Docker image with Redis: https://hub.docker.com/r/clearlinux/stacks-dbrs-redis

.. _Intel Optane DC PMM: https://www.intel.com/content/www/us/en/architecture-and-technology/optane-technology/optane-for-data-centers.html

.. _pmem-csi: https://github.com/intel/pmem-csi/blob/release-0.5/README.md

.. _DBRS Terms of Use: https://clearlinux.org/stacks/database/terms-of-use
