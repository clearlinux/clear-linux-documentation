.. _zfs: 

ZFS
###

This tutorial is not quite ready for prime-time. I think
a reasonably skilled Linux user will be able to use these
steps to get up and running with ZFS on Clear.

If you use this document, YMMV and you might break stuff. Be
careful.

.. contents:: Contents
   :depth: 2

Background
**********

Clear Linux does not, and will likely never, ship with a
binary kernel module to support ZFS (zfs.ko). There is a
copyright issue that arises from ZFS being licensed under
the CDDL while Linux is licensed under the GPL. Because of
that incompatibilty, most Linux kernel developers assert
that zfs.ko cannot be distributed in binary form alongside
the kernel.

Some distributions of Linux take a different read of the
CDDL / GPL issue -- most notably Canonical's Ubuntu -- and
argue that distributing a binary kernel module alongside Linux
does not infringe on the GPL nor the CDDL, since no derivative
work has been created. The Clear Linux team does not share
that optimistic view, and therefore zfs.ko must be built by
the user under Clear Linux.

To read the argument against shipping zfs.ko along with Linux:
https://sfconservancy.org/blog/2016/feb/25/zfs-and-linux/

To read the argument in favor of shipping zfs.ko along with Linux:
https://ubuntu.com/blog/zfs-licensing-and-linux

Suffice it to say, if you follow this tutorial and get zfs.ko
built and installed on your system, *you should not redistribute
that work in binary form* unless you consult an intellectual
property lawyer. I am not your lawyer.

Please note that there is no issue with distributing ZFS in
*source* form alongside Linux. According to those who argue
both against and in favor of binary distribution, the CDDL and
GPL are not incompatible with respect to redistribution of
source code.

So What?
========

Since it is legal to use ZFS with Linux, there is nothing
stopping a user from downloading the ZFS drivers, compiling
them, then installing them for their own use. This is no different
from downloading and using proprietary drivers like the Nvidia
Graphics drivers.

But, since the binaries for ZFS cannot be distributed with the
Linux kernel binaries (again, depending on who you ask), you'll
have some work to do when new kernels come out to ensure compatbility.
This is not always trivial, since new kernel release candidates will
invariably break *something* in ZFS. The ZFS-on-Linux team is
very good about catching up quickly, but on occasion you will find
a lag between a new kernel release and a supprted ZFS driver.

Installation Types
******************

Root installations
==================

Since there is a lag between kernel releases and ZFS support, I recommend
that you use a long term support kernel along with the latest ZFS driver
if you are going to run ZFS on root.

If you choose to use a native kernel and ZFS on root, clr-boot-manager
will refuse to update your kernels, so you will have to get comfortable
with installing new kernels to systemd-boot, which is a good skill to
have in any case.

We will explore ZFS on root after we get a working ZFS driver for non-root disks.

Non-Root installation
=====================

Before making the decision to run your CLR_ROOT partition
on a ZFS dataset, you should verify that you can get ZFS working
for a data-only partition.

If you use ZFS on a partition other than CLR_ROOT, with a root
partition that is ext4, xfs, or f2fs you may run into problems mounting
ZFS when a new kernel is released (until I have DKMS working).

In this configuration, clr-boot-manager will install your new kernel,
which may or may not work with zfs.ko.

- DKMS may not have rebuilt the module
- DKMS may not have autoinstalled the module
- The new kernel might introduce breaking changes that prevent zfs from compiling

You may end up having to manually recompile zfs.ko with the new kernel code, and zfs *might*
not compile at all with the new kernel. **So, be sure you don't put anything on that ZFS pool that you would need
in order to rebuild kernel modules.**

Prerequisites
*************

Before building ZFS, you need:

A DKMS Kernel
=============

This tutorial assumes you are using a DKMS kernel. In theory, it
should be possible to compile the ZFS module into your kernel, but

1) I didn't do this, so I can't help you and
2) you'll have to compile all of your new kernels from now on, which is likely to lead to problems.

You should read and understand the [Clear Linux tutorial on DKMS](https://docs.01.org/clearlinux/latest/guides/kernel/kernel-modules-dkms.html?highlight=dkms).

To check whether you have an lts or native kernel:  

.. code-block:: bash

    uname -r

If 'native' appears in the kernel name:  

.. code-block:: bash
   
    sudo swupd bundle-add kernel-native-dkms

If 'lts' appears in the kernel name:  

.. code-block:: bash

    sudo swupd bundle-add kernel-lts-dkms 
  
Reboot and make sure you can start the new kernel.
  
In order to make Clear Linux rebuild ZFS against new kernels using DKMS,
you need a dkms.conf file, which is not included in the zfs source.
  
TODO -- Using DKMS to rebuild ZFS against new kernels. (./configure --enable-systemd)
  
Bundles
=======

You need several build tools before you can install ZFS.

If you are using a native kernel:   

.. code-block:: bash

    sudo swupd bundle-add linux-dev

If you are using an LTS kernel:  
 
.. code-block:: bash

    sudo swupd bundle-add linux-lts-dev
   
You also need these bundles: 

.. code-block:: bash

    sudo swupd bundle-add os-core-dev devpkg-openssl devpkg-util-linux

Installing and Running ZFS
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


Building
********

Once you have fetched the zfs codebase as described in the previous
section, you can build using the following commands:

.. code-block:: bash

    cd zfs
    ./autogen.sh
    ./configure
    make -s -j$(nproc)

Testing your build
******************

You can -- and SHOULD -- test-drive zfs before installing it.

See ./scripts/zfs-tests.sh

Installing
**********

If you are satisfied with your build, you can now run:

.. code-block:: bash

    sudo make install

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

And it will deliver the zfs kernel modules to:

    /usr/lib/modules/<kernel-name>/extra/zfs 

Fortunately, `swupd repair` will not delete kernel modules from this location.

Systemd 
-------
To use ZFS automatic zpool import and filesystem mounting, copy the systemd.unit files 
into /etc:

.. code-block:: bash 
   
   sudo cp ./etc/systemd/system/*.service /etc/systemd/system/
   sudo cp ./contrib/dracut/90zfs/zfs-env-bootfs.service /etc/systemd/system/

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

Enable the zfs-import-cache and zfs-mount services:

.. code-block:: bash
   
   systemctl enable zfs-import-cache
   systemctl enable zfs-import.target

   systemctl enable zfs-mount
   systemctl enable zfs.target

@TODO: Detail installation of zfs-mount-generator instead of zfs-mount

Staying up-to-date
******************

**IMPORTANT** When you install a new kernel, you've got to reinstall the zfs modules. 
That can be automated in most cases with a dkms.conf file.

@TODO: Insert DKMS details here

Loading the new kernel module at boot
=====================================

The zfs module will not load automatically at boot. To make it do so -- in a non-root configuration -- you can load the zfs.ko module at boot time by specifying to systemd that you want the out-of-tree module to be loaded.

First, make sure your system will allow unsigned modules: 

    echo "module.sig_unenforce" | sudo tee /etc/kernel/cmdline.d/allow-unsigned-modules.conf

Clear Linux and systemd use the `/etc/modules-load.d/` directory to load
out-of-tree kernel modules. Make sure that the directory exists:

    sudo mkdir -p /etc/modules-load.d

Then create the configuration file with:

    sudo echo "zfs" | sudo tee /etc/modules-load.d/01-zfs.conf 

When you reboot, zfs should be loaded by the kernel automatically.

Using on a Non-Root device
**************************

You're ready to create zpools and datasets.

Enable automatic import of a pool by zfs-import-cache.service with:

.. code-block:: bash

   zpool set cachefile=/etc/zfs/zpool.cache <pool>

ZFS on root (/)
***************
WIP

Installing new kernels with ZFS root   systemctl enable zfs-import-cache
   systemctl enable zfs-import.target
====================================
If you use ZFS for your CLR_ROOT, then clr-boot-manager will no longer
automatically install new kernels for you: you'll have to set them up
manually when updated kernels are available.

Hopefully, by now you understand why *this is a good thing*.

When a new kernel is available, you will find that the Clear Linux tools will refuse to install your new kernel
with an error similar to this:

.. code-block:: bash

    Calling post-update helper scripts
    External command: none
    External command: [ERROR] cbm (../src/lib/system_stub.c:L31): Invalid block device: 0:29
    External command: Out of memory
    External command: [FATAL] cbm (../src/bootman/sysconfig.c:L277): sysconfig insane: Missing root device
    External command: [FATAL] cbm (../src/bootman/update.c:L389): Failed to install bootloader
    External command: [FATAL] cbm (../src/bootman/sysconfig.c:L277): sysconfig insane: Missing root device
    External command: [ERROR] cbm (../src/bootman/update.c:L218): Failed to repair running kernel
    External command: [FATAL] cbm (../src/bootman/sysconfig.c:L277): sysconfig insane: Missing root device
    External command: [FATAL] cbm (../src/bootman/update.c:L250): Failed to install default-native kernel: ///usr/lib/kernel/org.clearlinux.native.5.6.12-950

The root cause is that clr-boot-manager does not understand the ZFS partition type. This
bug is not unique to ZFS -- it also occurs with a BTRFS root partition. These github
issues are worth reading to understand the issue better (where they reference btrfs, think 'zfs'):

https://github.com/clearlinux/clr-boot-manager/issues/61  
https://github.com/clearlinux/clr-boot-manager/issues/182  
https://github.com/clearlinux/clr-boot-manager/issues/193  

Acknowledgements: 
*****************

https://wiki.archlinux.org/index.php/ZFS#Configuration



