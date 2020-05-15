.. _zfs: 

ZFS
###

This tutorial covers the setup of ZFS-on-Linux under Clear Linux, 
using a non-root device for your zpools. ZFS on root is a work-in-progress. 

.. contents:: 
   :local:
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
work has been created. Clear Linux does not share that view, 
and therefore zfs.ko must be built by the user under Clear Linux.

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

ZFS can be easily installed for use on non-root devices. It is substantially
harder to get ZFS to work on a root partition, but it is possible if that's what
you want. 

A non-root build and installation is a prerequisite to a root installation, so 
we will cover the non-root install first. 

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

So, with all of that said, let's fetch the code via git: 

.. code-block:: bash

   git clone https://github.com/openzfs/zfs.git /opt/src/zfs

You'll want to keep the git repository in a working location. I have chosen /opt/src/zfs, but you can choose any workspace you like -- we will be copying the source code into a directory where DKMS can find it in the next step. 

Building
********
We're going to build the module using DKMS, which will help 
us keep the module up to date later when new kernels are released. 

Once you have fetched the zfs codebase as described in the previous
section, you will want to check out the tagged version that you plan to use. 
Building from `master` is optimistic -- but you'll want a tagged 
version for DKMS to pick up on later. As of the time of this writing, 
the latest released tag is `0.8.4`:

.. code-block:: bash

    cd /opt/src/zfs
    git checkout 0.8.4

Next, we will copy the source code into `/usr/src/zfs-0.8.4` so that DKMS 
can rebuild it when kernel updates occur. We'll build the code from there: 

.. code-block:: bash
    sudo cp -Rv /opt/src/zfs /usr/src/zfs-0.8.4 
    cd /usr/src/zfs-0.8.4


**OPTIONAL** -- you can skip the next code block and go right to 
DKMS configuration, or you can compile by hand wihtout using the 
DKMS tooling first: 

..code-block:: bash
 
    ./autogen.sh
    ./configure
    make -s -j$(nproc)
    sudo make install 


DKMS Configuration -- The ZFS distribution provides a script to build 
a suitable dkms.conf file. We'll build dkms.conf and install it into 
the DKMS tree. 

..code-block:: bash

   cd /usr/src/zfs-0.8.4
   scripts/dkms.mkconf -n zfs -v 0.8.4 -f dkms.conf 
   sudo dkms add -m zfs -v 0.8.4
   sudo dkms build -m zfs -v 0.8.4
   sudo dkms install -m zfs -v 0.8.4

   sudo modprobe zfs

This will deliver the zfs kernel modules to:

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


You're ready to create zpools and datasets.

Potential Issues on a Non-Root device
*************************************
When the Clear Linux kernel is upgraded, DKMS will attempt to rebuild your
zfs module for use with the new kernel. If you boot a new kernel and cannot
find your zpools:

- DKMS may not have rebuilt the module
- DKMS may not have autoinstalled the module
- The new kernel might introduce breaking changes that prevent zfs from compiling

You may end up having to manually recompile zfs.ko with the new kernel code, and zfs *might*
not compile at all with the new kernel. 

**So, be sure you don't put anything on that ZFS pool that you would need
in order to rebuild kernel modules.**

ZFS on root (/)
***************

Since there is a lag between kernel releases and ZFS support, I recommend
that you use a long term support kernel along with the latest ZFS driver
if you are going to run ZFS on root.

If you choose to use a native kernel and ZFS on root, clr-boot-manager
will refuse to update your kernels, so you will have to get comfortable
with installing new kernels to systemd-boot, which is a good skill to
have in any case.

Installing new kernels with ZFS root   
====================================
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
https://github.com/openzfs/zfs/issues/10068


