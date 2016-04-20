Ceph
####

Ceph is a distributed storage system designed to scale well and can be integrated with
OpenStack as the storage backend for the OS images and Volumes.

The deployment of a ceph storage cluster is really easy in ClearLinux* with the help of
Ansible which we will demonstrate on this blog post.

Environment
===========
For this example we are going to use 5 nodes. A deployment node which we will use to run
the playbooks, a monitor node and 3 storage nodes.

It is recommended to install each component on its own server, however, for testing
purposes you can install the monitor and storage nodes on the same hosts.

Prerequisites
=============
Ansible uses ssh to run commands on the remote servers, in order to do that, the servers should be configured to allow passwordless ssh connections from the root user. Follow these steps to configure your nodes.

#. Generate ssh keys::

    # ssh-keygen

#. Enable root login::

    # echo "PermitRootLogin yes" >> /etc/ssh/sshd_config

#. Enable sshd service::

    # systemctl enable sshd
    # systemctl start sshd

#. Allow passwordless login::

    # ssh-copy-id root@node

Install the software
====================
Install the sysadmin-hostmgmt bundle on the development node.
This bundle contains the ansible software required to run the playbooks as well as some ansible roles and sample playbooks that you can use to make your own.::

    # swupd bundle-add sysadmin-hostmgmt

Create the playbook
===================
sysadmin-hostmgmt bundle ships some sample playbooks that you cant tweak to your own needs.
Start by making a copy of the sample playbook into your home folder.::

    # cp /usr/share/ansible/examples/ceph ~/

The playbook consist of 4 files that you should modify to your needs::

    ceph
    |-- group_vars/
    |    |-- all
    |    +-- mons
    |-- hosts
    +-- ceph_deploy.yml

The hosts file contains the ip addresses of your servers grouped under the roles they will serve.::

    [mons]
    172.28.128.7

    [osds]
    172.28.128.8
    172.28.128.9
    172.28.128.10

This groups_var/all file contains variables that will be used in all your nodes.
The mandatory variables are already there, make sure to change the values accordingly to your environment. It should look like this.::

    ---
    journal_size: 1024
    monitor_interface: enp0s8
    public_network: 172.28.128.0/24
    cluster_network: "{{ public_network }}"

A full list of available variables can be found in /usr/share/ansible/roles/<role>/defaults/main.yml

This groups_var/osd file contains the variables that will apply only to the hosts under the mons section in your hosts file.
You can choose one of the three available scenarios for this playbooks

#. Journal and osd_data on the same device: This will collocate both journal and data on the same disk creating a partition at the beginning of the device::

    journal_collocation: true
    devices:
      - /dev/sdb
      - /dev/sdc
      - /dev/sdd

#. N journal devices for N OSDs: In this example: sdb will be used for journaling of sdc and sdd sdf will be used for journaling of sde::

    raw_multi_journal: true
    devices:
      - /dev/sdc
      - /dev/sdd
      - /dev/sde
    raw_journal_devices:
      - /dev/sdb
      - /dev/sdb
      - /dev/sdf

#. Use directory instead of disk for OSDs::

    osd_directory: true
    osd_directories:
      - /var/lib/ceph/osd/mydir1
      - /var/lib/ceph/osd/mydir2
      - /var/lib/ceph/osd/mydir3

Run the playbook
================
Once you have your variables and hosts file configured, the deployment can be fired with the following command::

    # ansible-playbook -i hosts ceph_deploy.yml

Verify
======
Now that ansible has finished with the deployment, you can verify the health of the cluster with ceph util::

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
