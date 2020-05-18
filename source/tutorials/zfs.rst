.. _zfs: 

ZFS
###

This tutorial covers the setup of ZFS-on-Linux under Clear Linux, 
using a non-root device for your zpools. ZFS on root is a work-in-progress. 

.. contents:: 
   :local:
   :depth: 1

Background
**********

Clear Linux will not ship with a binary kernel module to support ZFS (zfs.ko). 
ZFS is licensed under the CDDL while Linux is licensed under the GPL. These 
licenses are not compatible. Most Linux kernel developers assert that zfs.ko 
cannot be distributed in binary form alongside the kernel.

Some distributions of Linux have a different opinion of the
CDDL / GPL issue -- most notably Canonical's Ubuntu -- and
argue that a binary kernel module can be distributed alongside 
Linux without infringement. Clear Linux does not share that view. 
Therefore zfs.ko must be built by the user under Clear Linux.

It is worth understanding the `argument against shipping zfs.ko along 
with Linux`_ in addition to `the argument in favor`_.

.. `argument against shipping zfs.ko along 
with Linux`: https://sfconservancy.org/blog/2016/feb/25/zfs-and-linux/

.. `the argument in favor`: https://ubuntu.com/blog/zfs-licensing-and-linux

If you follow this tutorial and build zfs.ko on your system, 
*you should not redistribute that work in binary form* unless 
you consult an intellectual property lawyer.

Note that there is no issue with distributing ZFS in
*source* form alongside Linux. According to those who argue
both against and in favor of binary distribution, the CDDL and
GPL are not incompatible with respect to redistribution of
source code.

So what?
========

Since it is legal to use ZFS with Linux, there is nothing
stopping a user from downloading the ZFS drivers, compiling
them, then installing them for their own use. This is no different
from downloading and using proprietary drivers like the Nvidia
Graphics drivers.

Since the binaries for ZFS cannot be distributed with the
Linux kernel binaries, you'll have some work to  ensure compatbility 
when new kernels are released.

This is not always trivial, since new kernel release candidates will
invariably break *something* in ZFS. The ZFS-on-Linux team is
very good about catching up quickly, but on occasion you will find
a lag between a new kernel release and a supported ZFS driver.

Installation types
******************

It is easiest to install ZFS for use on non-root devices. It is substantially
harder to get ZFS working on a root partition. A non-root build and installation 
is a prerequisite to a root installation, so we cover the non-root install first. 

Prerequisites
*************

In order to build ZFS, you need:

DKMS kernel
===========

This tutorial assumes you are using a DKMS kernel. You should read and 
understand the `Clear Linux tutorial on DKMS`_.

.. `Clear Linux tutorial on DKMS`: https://docs.01.org/clearlinux/latest/guides/kernel/kernel-modules-dkms.html?highlight=dkms

If you do not currently use a DKMS kernel, you can install it with the following steps. 

Check whether you have an lts or native kernel:  

.. code-block:: bash

    uname -r

If 'native' appears in the kernel name, then install a native kernel with DKMS support:  

.. code-block:: bash
   
    sudo swupd bundle-add kernel-native-dkms

If 'lts' appears in the kernel name, then install the latest TLS kernel with DKMS support:  

.. code-block:: bash

    sudo swupd bundle-add kernel-lts-dkms 
  
Reboot and make sure you can start the new kernel.
    
Bundles
=======

Install these build tools before you install ZFS.

If you are using a native kernel:   

.. code-block:: bash

    sudo swupd bundle-add linux-dev

If you are using an LTS kernel:  
 
.. code-block:: bash

    sudo swupd bundle-add linux-lts-dev
   
Finally, install need these bundles, no matter which kernel you are using: 

.. code-block:: bash

    sudo swupd bundle-add os-core-dev devpkg-openssl devpkg-util-linux

Installing and running ZFS
**************************

Get the ZFS code
================

The ZFS codebase moves quickly, just like the kernel codebase. Therefore
it's best that you get the source code from the ZFS on Linux repository,
hosted on Github.

How the ZFS on Linux github repository is organized
---------------------------------------------------

The master branch contains the latest code and bugfixes, but may also be bleeding edge.

Release branches exist for major releases (0.6, 0.7, 0.8, etc)
Minor release tags exist for minor updates (0.8.1 , 0.8.2, 0.8.3, etc)

The latest tag or the latest release branch is likely the one you want:

`zfs-0.8-release (in sync with zfs-0.8.4 tag)`

Selecting the right combination of ZFS module code and kernel code
------------------------------------------------------------------

Ensure that the kernel you are using can be used with the ZFS kernel module.
Depending on whether you are using a LTS or mainline kernel, you may need to s
elect a different version of the ZFS module.

kernel-org.clearlinux.native.5.6.4 - zfs-0.8-release branch or the zfs-0.8.4 tag or later

kernel-org.clearlinux.lts. - TBD

Generally speaking, you want to download the latest ZFS release, and you *might* need
to use a kernal that is behind by a dot-release or two. If you cannot get ZFS to build against
your native kernel, try an lts kernel.

So, with all of that said, let's fetch the code via git: 

.. code-block:: bash

   git clone https://github.com/openzfs/zfs.git /opt/src/zfs

Remember where you check-out the git repository, because you will need it when you upgrade ZFS. 
I have chosen /opt/src/zfs, but you can choose any workspace you like. ZFS will not run from this location -- we will be copying the source code into a directory where DKMS can find it in the next step. 

Building
********
We will build the module using DKMS. This will help us keep the 
module up to date later as new kernels are released. 

You have already fetched the zfs codebase. Check out the tagged version 
that you plan to use. As of the time of this writing, the latest release
tag is `0.8.4`:

.. code-block:: command

    cd /opt/src/zfs
    git checkout 0.8.4

Copy the source code into `/usr/src/zfs-0.8.4`. This exposes the source 
code to DKMS. We will build the code from the new location: 

.. code-block:: command
    sudo cp -Rv /opt/src/zfs /usr/src/zfs-0.8.4 
    cd /usr/src/zfs-0.8.4

The ZFS distribution provides a script to build a suitable dkms.conf file. 
Build dkms.conf and install it into the DKMS tree. 

..code-block:: bash

   cd /usr/src/zfs-0.8.4
   scripts/dkms.mkconf -n zfs -v 0.8.4 -f dkms.conf 
   sudo dkms add -m zfs -v 0.8.4
   sudo dkms build -m zfs -v 0.8.4
   sudo dkms install -m zfs -v 0.8.4

This will install the zfs kernel modules to:

    /usr/lib/modules/<kernel-name>/extra/zfs 

This will install the zfs userspace tools to:
::

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


Load the new kernel module: 

.. code-block: command

   sudo modprobe zfs


Systemd 
-------

You should now have these unit files available: 

```
zfs-env-bootfs.service
zfs-zed.service
zfs-import-cache.service
zfs-import-scan.service
zfs-mount.service
zfs-share.service
zfs-volume-wait.service
```

If you want to use ZFS automatic zpool import and filesystem 
mount services, copy the systemd.unit files into /etc and enable them:

.. code-block:: command
   
   sudo cp ./etc/systemd/system/*.service /etc/systemd/system/
   sudo cp ./contrib/dracut/90zfs/zfs-env-bootfs.service /etc/systemd/system/
   
   systemctl enable zfs-import-cache
   systemctl enable zfs-import.target

   systemctl enable zfs-mount
   systemctl enable zfs.target

@TODO: Detail installation of zfs-mount-generator instead of zfs-mount

Load the kernel module at boot
==============================

The ZFS module will not load automatically at boot. Load the zfs.ko module 
at boot time by with systemd.

First, allow unsigned modules: 

    echo "module.sig_unenforce" | sudo tee /etc/kernel/cmdline.d/allow-unsigned-modules.conf

Systemd uses the `/etc/modules-load.d/` directory to load out-of-tree kernel modules. 
Make sure that the directory exists:

    sudo mkdir -p /etc/modules-load.d

Create the configuration file:

    sudo echo "zfs" | sudo tee /etc/modules-load.d/01-zfs.conf 

Reboot -- zfs.ko should be loaded automatically.

Caution
*******
When the Clear Linux kernel is upgraded, DKMS will attempt to rebuild your
zfs module for the new kernel. If you boot a new kernel and cannot find 
your zpools:

- DKMS may not have rebuilt the module
- DKMS may not have autoinstalled the module
- The new kernel might introduce breaking changes that prevent zfs from compiling

To fix this situation, you may have to recompile zfs.ko with the new kernel code. 
ZFS *might* not compile at all with the new kernel. 

**So, be sure you don't put anything on that ZFS pool that you would need
in order to rebuild kernel modules.**

Next steps
**********
You are ready to create zpools and datasets! For more information on using ZFS: 

`FreeBSD Handbook chapter on ZFS`_
`Arch Linux ZFS Guide`_

.. _`FreeBSD Handbook chapter on ZFS`: https://www.freebsd.org/doc/handbook/zfs.html
.. _`Arch Linux ZFS Guide`: https://wiki.archlinux.org/index.php/ZFS

Acknowledgements: 
*****************

https://wiki.archlinux.org/index.php/ZFS#Configuration
https://github.com/openzfs/zfs/issues/10068


