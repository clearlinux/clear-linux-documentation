.. _zfs:

OpenZFS*
########

This tutorial shows how to set up `OpenZFS* file system and volume manager`_ on |CL-ATTR|, using a non-root device for zpools. 

.. contents::
   :local:
   :depth: 1

Background
**********

The OpenZFS storage platform provides volume management, snapshot capabilities, and redundancy detection. |CL| **does not** ship with a binary ZFS kernel module (zfs.ko). |CL| users who wish to incorporate the zfs.ko kernel module must build and maintain this work themselves.

.. CAUTION::

   Use of the OpenZFS kernel module in connection with |CL| is neither recommended nor officially endorsed by the Clear Linux* Project.  Users who follow this tutorial and build zfs.ko kernel module are encouraged to seek independent legal counsel regarding any plan to redistribute a software package containing zfs.ko and |CL|. 

Known Issues
************

Using a long-term-support (LTS) kernel when running OpenZFS reduces the risk of incompatibilities with kernel updates. When new kernels or new versions of OpenZFS are released, users bear the responsibility to test those releases and ensure compatibility before deploying any updates. 

Prerequisites
*************

* Learn to :ref:`kernel-modules-dkms`
* Learn to use :ref:`swupd-guide`

Install the DKMS kernel
=======================

If you do not currently use a DKMS kernel, install it by using one of the options below.

#.  Check whether you have an LTS or native kernel:

    .. code-block:: bash
  
       uname -r

    a. If 'native' appears in the kernel name, then install a native
       kernel with DKMS support:

       .. code-block:: bash

          sudo swupd bundle-add kernel-native-dkms

    #. If 'lts' appears in the kernel name, then install the latest LTS
       kernel with DKMS support:

       .. code-block:: bash

          sudo swupd bundle-add kernel-lts-dkms

#. Reboot and make sure you can start the new kernel.

Bundles
=======

Before you install OpenZFS, install the bundles that contain the build dependencies.

.. code-block:: bash

    sudo swupd bundle-add os-core-dev devpkg-openssl devpkg-util-linux

Install
*******

Clone OpenZFS code
==================


In this section, you download the source code directly from the `ZFS on Linux repository`_.

.. note::
   
   OpenZFS will not run from this location. We copy the source code into a DKMS directory in the following steps. 

#. Create a directory. In this example, we use :file:`/opt/src/zfs`, 
   but you can choose any workspace you like. 

   .. code-block:: bash

      sudo mkdir -p /tmp/zfs/ 

#. Clone the repository.

   .. code-block:: bash

      git clone https://github.com/openzfs/zfs.git /tmp/zfs
      sudo cp -Rv /tmp/zfs /opt/src/zfs

Remember where you clone the git repository because you will need it
when you upgrade ZFS. Do not delete the source location when you have completed this tutorial. You will need it later.

Compile the module
==================

We will build the module using DKMS. This will enable us to keep the module up to date as new kernels are released in the future.


#. Check out the tagged version that you plan to use. As of the time of this
   writing, the latest release tag is `0.8.4`:

   .. code-block:: bash

      cd /opt/src/zfs
      git checkout zfs-0.8.4

#. Copy the source code into `/usr/src/zfs-0.8.4`. This exposes the source
   code to DKMS. We will build the code from the new location:

   .. code-block:: bash

      sudo cp -Rv /opt/src/zfs /usr/src/zfs-0.8.4

#. The ZFS distribution provides a script to build a suitable dkms.conf file.
   Build dkms.conf and install it into the DKMS tree.

   .. code-block:: bash

      cd /usr/src/zfs-0.8.4
      sudo scripts/dkms.mkconf -n zfs -v 0.8.4 -f dkms.conf
      sudo dkms add -m zfs -v 0.8.4
      sudo dkms build -m zfs -v 0.8.4
      sudo dkms install -m zfs -v 0.8.4

#. Observe that this install the zfs kernel modules to: 
   :file:`/usr/lib/modules/<kernel-name>/extra/zfs`

   In addition, this installs the zfs userspace tools to:

   .. code-block:: console

      + /usr/local/
      |--+ bin/
         |--zvol_wait
         |--zgenhostid
         |--raidz_test
      |--+ etc/
         |--+ zfs/
            |--* zed.d/
            |--+ zpool.d/
            |--zfs-functions
      |--+ include/libzfs/ [contents omitted]
      |--+ lib/
      |--+ libexec/
         |--+ zfs/
            |-- zpool.d/
            |-- zed.d
      |--+ share/zfs/ [contents omitted]
      |--+ sbin/
         |--fsck.zfs
         |--zpool
         |--zdb
         |--zed
         |--zfs
         |--zhack
         |--zinject
         |--zpool
         |--ztest
         |--zstreamdump
      |--+ src/
         |--+ zfs-0.8.4/
         |--+ spl-0.8.4/


#. Load the new kernel module:

   .. code-block: bash

      sudo modprobe zfs


Set up systemd
==============

You should now have these unit files available. 

.. code-block:: console

   zfs-env-bootfs.service
   zfs-zed.service
   zfs-import-cache.service
   zfs-import-scan.service
   zfs-mount.service
   zfs-share.service
   zfs-volume-wait.service
  
OpenZFS requires you to explicitly install and enable the services you want. 
If you want to use other ZFS service units, you could create symlinks for them, similar to the example below.

To use ZFS automatic zpool import and filesystem mount services, link the systemd.unit files into :file:`/etc` and enable them.

.. code-block:: bash

   sudo ln -s ./etc/systemd/system/zfs-import-cache.service /etc/systemd/system/
   sudo ln -s ./etc/systemd/system/zfs-mount.service /etc/systemd/system/

   sudo systemctl enable zfs-import-cache
   sudo systemctl enable zfs-import.target

   sudo systemctl enable zfs-mount
   sudo systemctl enable zfs.target


Load the kernel module at boot
==============================

OpenZFS kernel modules must be loaded before any OpenZFS filesystems are mounted. For convenience, load the kernel modules at boot.

#. Systemd uses the `/etc/modules-load.d/` directory to load out-of-tree
   kernel modules. Make sure that the directory exists:

   .. code-block:: bash

      sudo mkdir -p /etc/modules-load.d

#. Create the configuration file:

   .. code-block:: bash

      echo "zfs" | sudo tee /etc/modules-load.d/01-zfs.conf

#. Reboot your system. zfs.ko should be loaded automatically.

.. CAUTION::

   When the |CL| kernel is upgraded, DKMS will attempt to rebuild your OpenZFS module for the new kernel. 

   - DKMS may not have rebuilt the module
   - DKMS may not have auto-installed the module
   - The new kernel might introduce breaking changes that prevent zfs
     from compiling

To fix this situation, you may have to recompile zfs.ko with the new kernel code. OpenZFS *might* not compile at all with the new kernel.

.. CAUTION::
   
   **Be sure you don't put anything on an OpenZFS pool that you would need
   in order to rebuild kernel modules.** You must ensure the compatibility of OpenZFS with new Linux kernels when they are released.

Troubleshooting
===============

If you suspect an issue with DKMS rebuilding your module, you can check two places for information. The dkms-new-kernel service will show status that may help in troubleshooting:

.. code-block:: bash

   systemctl status dkms-new-kernel.service

Also, the systemd journal may have important information:

.. code-block:: bash

   journalctl -xe

Next steps
**********
You are ready to create zpools and datasets! For more information on using ZFS, see:

* `FreeBSD Handbook chapter on ZFS`_
* `ZFS-on-Linux issue tracker`_

.. _FreeBSD Handbook chapter on ZFS: https://www.freebsd.org/doc/handbook/zfs.html
.. _ZFS-on-Linux issue tracker: https://github.com/openzfs/zfs/issues/10068
.. _ZFS on Linux repository: https://github.com/openzfs/zfs
.. _OpenZFS* file system and volume manager: https://github.com/openzfs/zfs