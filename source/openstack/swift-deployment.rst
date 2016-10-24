.. _openstack_swift_deployment_scenarios:

OpenStack* Swift* Deployment Scenarios
######################################

You can install OpenStack Swift using clear-config-management through two
possible scenarios.

- **Scenario #1:** All the storage nodes are identical, with the same number of storage devices with the same names.

- **Scenario #2:** The storage setup is heterogeneous. The list of storage devices must be provided for each storage node individually.


Scenario #1: Identical storage nodes scenario
=============================================

To set up this scenario, the ``swift_storage_devices`` variable needs to be
defined in ``../group_vars/all`` as follows:

.. code-block:: yaml

   ...
   swift_storage_device_path: /dev/
   swift_storage_devices:
     - sda
     - sdb
     ...

Scenario #2: Different storage nodes scenario
=============================================

With this setup, specific information about each storage node has to be provided.

First, in the root of your Ansible* directory setup, create a new directory called ``host_vars``.
Inside ``host_vars``, for each storage node, create a new file with the name of the
storage node's hostname or IP. In each file, provide the list of the storage
devices.

The Ansible directory setup should look similar to the following directory tree:

.. code-block:: console

   openstack/
   ├── group_vars
   │   └── all
   ├── hosts
   ├── host_vars
   │   ├── storage-one
   │   └── storage-two
   ├── openstack_deployment.yml
   └── README.md

And the ``storage-one`` and ``storage-two`` storage node files should look similar to this:

.. code-block:: yaml

   ---
   devices:
     - sdb
     - sdc
     - sdd


.. code-block:: yaml

   ---
   devices:
     - vdb
     - vdc
