.. _ceph-deploy:

Ceph*
#####

Ceph is a distributed storage system designed to scale well. It can be
integrated with OpenStack* as the storage backend for the OS images and
volumes.

Deploying a Ceph storage cluster is simple using Clear Linux* OS for
Intel® Architecture and Ansible*.


Environment
===========

For this example, we'll use a total of six nodes: a **deployment node**,
to run the playbooks, a **monitor node**, a **metadata node** and three 
**storage nodes**.

Install each component on its own server for best results; however,
for testing purposes you can install the monitor, metadata, and storage 
nodes all on the same host.


Prerequisites
=============

Ansible uses ``ssh`` to run commands on the remote servers. In order to
do that, the servers must be configured to allow passwordless ssh
connections from the root user. Follow these steps to configure
your nodes.

On your cluster nodes
---------------------

#. Enable root login::

    # echo "PermitRootLogin yes" >> /etc/ssh/sshd_config

#. Enable sshd service::

    # systemctl enable sshd
    # systemctl start sshd

On your deployment node
-----------------------

#. Generate an ssh key if you have not already::

    # ssh-keygen

#. Copy your public key (:file:`~/.ssh/id_rsa.pub`) to :file:`/root/.ssh/authorized_keys` on each node::

    # ssh-copy-id root@node


Install the software
====================

Install the `sysadmin-hostmgmt`_ bundle on the deployment node. This
bundle contains the Ansible software required to run the playbooks, as
well as some Ansible roles and sample playbooks that you can use to
build your own::

    # swupd bundle-add sysadmin-hostmgmt


Create the playbook
===================

The ``sysadmin-hostmgmt`` bundle includes some sample playbooks that
can be customized for your own needs. Start by making a copy of the
sample playbook into your home folder.::

    # cp -r /usr/share/ansible/examples/ceph ~/

The playbook consist of four files that you should modify to fit
your needs::

    ceph
    |-- group_vars/
    |    |-- all
    |    +-- mons
    |-- hosts
    +-- ceph_deploy.yml

The ``hosts`` file contains the IP addresses of your servers grouped
under the roles they will serve::

    [mons]
    172.28.128.7

    [osds]
    172.28.128.8
    172.28.128.9
    172.28.128.10

    [mdss]
    172.28.128.11

This :file:`groups_var/all` file contains variables that will be applied
to all your nodes. The mandatory variables are already there; be sure
to change the values accordingly to fit your environment. It should
look something like this::

    ---
    journal_size: 1024
    monitor_interface: enp0s8
    public_network: 172.28.128.0/24
    cluster_network: "{{ public_network }}"

A full list of available variables can be found under each role 
in ``defaults/main.yml``::

   * `ceph-common/defaults/main.yml`_
   * `ceph-mon/defaults/main.yml`_
   * `ceph-mds/defaults/main.yml`_
   * `ceph-osd/defaults/main.yml`_

This :file:`groups_var/osd` file contains variables that apply only
to the hosts under the ``[mons]`` section in your hosts file. You can
choose one of the three available scenarios for this playbook.

#. **Journal and osd_data on the same device**: This will co-locate both
   journal and data on the same disk, creating a partition at the
   beginning of the device::

      journal_collocation: true
      devices:
        - /dev/sdb
        - /dev/sdc
        - /dev/sdd

#. **N journal devices for N OSDs**: In this example, the ``sdb``
   partition will be used for journaling of ``sdc``. The ``sdd sdf``
   will be used for journaling of ``sde``::

      raw_multi_journal: true
      devices:
        - /dev/sdc
        - /dev/sdd
        - /dev/sde
      raw_journal_devices:
        - /dev/sdb
        - /dev/sdb
        - /dev/sdf

#. **Specify a directory instead of disk for OSDs**::

      osd_directory: true
      osd_directories:
        - /var/lib/ceph/osd/mydir1
        - /var/lib/ceph/osd/mydir2
        - /var/lib/ceph/osd/mydir3

  Note: The directories should reside on an XFS filesystem. EXT4 is not supported.


Run the playbook
================

Once the variables and hosts file is configured,
deployment is as simple as issuing the command::

    # ansible-playbook -i hosts ceph_deploy.yml


Verify
======

After Ansible has finished deployment, you may
like to verify and watch the health of the cluster
with Ceph utilites such as ``ceph status`` and
``ceph osd tree``::

    # ceph status
        cluster ee1fae3b-b95b-494c-abd7-f0629d113446
         health HEALTH_OK
         monmap e1: 1 mons at {node2=172.28.128.5:6789/0}
                election epoch 2, quorum 0 node2
         osdmap e8: 3 osds: 3 up, 3 in
                flags sortbitwise
          pgmap v14: 64 pgs, 1 pools, 0 bytes data, 0 objects
                7566 MB used, 49647 MB / 59896 MB avail
                      64 active+clean

::

    # ceph osd tree
    ID WEIGHT  TYPE NAME      UP/DOWN REWEIGHT PRIMARY-AFFINITY
    -1 0.05699 root default
    -2 0.01900     host node3
     0 0.01900         osd.0       up  1.00000          1.00000
    -3 0.01900     host node4
     1 0.01900         osd.1       up  1.00000          1.00000
    -4 0.01900     host node5
     2 0.01900         osd.2       up  1.00000          1.00000

::

    # ceph fs ls
    name: cephfs, metadata pool: cephfs_metadata, data pools: [cephfs_data ]

.. _ceph-common/defaults/main.yml: https://github.com/clearlinux/clear-config-management/blob/master/roles/ceph-common/defaults/main.yml
.. _ceph-mon/defaults/main.yml: https://github.com/clearlinux/clear-config-management/blob/master/roles/ceph-mon/defaults/main.yml
.. _ceph-mds/defaults/main.yml: https://github.com/clearlinux/clear-config-management/blob/master/roles/ceph-mds/defaults/main.yml
.. _ceph-osd/defaults/main.yml: https://github.com/clearlinux/clear-config-management/blob/master/roles/ceph-osd/defaults/main.yml
.. _sysadmin-hostmgmt: https://github.com/clearlinux/clr-bundles/blob/master/bundles/sysadmin-hostmgmt

