.. _zfs:

ZFS
###

This tutorial covers the setup of ZFS-on-Linux under Clear Linux,
using a non-root device for your zpools. ZFS as a CLR_ROOT device
is a not covered in this tutorial.

.. contents::
   :local:
   :depth: 1

Background
**********

Clear Linux does not ship with a binary ZFS kernel module (zfs.ko).
ZFS is licensed under the CDDL. Linux is licensed under the GPL. These
licenses are not compatible. Most Linux kernel developers assert that zfs.ko
cannot be distributed in binary form alongside the kernel.

Some distributions of Linux have a different opinion of
CDDL / GPL compatibility -- most notably Canonical's Ubuntu -- and
argue that a binary kernel module can be distributed alongside
Linux without infringement. Clear Linux does not share that view.
Therefore, zfs.ko must be built by the user under Clear Linux.

It is worth understanding the `argument against shipping zfs.ko along
with Linux`_ in addition to `the argument in favor`_.

If you follow this tutorial and build zfs.ko on your system,
*you should not redistribute that work in binary form*.

Note that there is no issue with distributing ZFS in
*source* form alongside Linux. According to those who argue
both against and in favor of binary distribution, the CDDL and
GPL are not incompatible with respect to redistribution of
source code.

There is nothing stopping a user from downloading the ZFS drivers,
compiling them, then installing them for their own use. This is no
different from downloading and using proprietary drivers like the Nvidia
Graphics or Broadcom wireless drivers.

Since the binaries for ZFS cannot be distributed with the
Linux kernel binaries, you'll have some work to ensure compatibility
when new kernels are released.

This is not always trivial, since new kernel release candidates will
invariably break *something* in ZFS. The ZFS-on-Linux team is
very good about catching up quickly, but on occasion you will find
a lag between a new kernel release and a supported ZFS driver. It is
safest to use a long-term-support (LTS) kernel if you run ZFS: you
are much less likely to run into incompatabilities with and LTS kernel.
When new kernels or new versions of ZFS are releases, users should
test those releases carefully before deploying any updates.

Prerequisites
*************

To build ZFS, you need:

DKMS kernel
===========

This tutorial assumes you are using a DKMS kernel. You should read and
understand how to :ref:`kernel-modules-dkms`.

If you do not currently use a DKMS kernel, install it with the following steps.

Check whether you have an LTS or native kernel:

.. code-block:: bash

    uname -r

If 'native' appears in the kernel name, then install a native kernel with DKMS support:

.. code-block:: bash

    sudo swupd bundle-add kernel-native-dkms

If 'lts' appears in the kernel name, then install the latest LTS kernel with DKMS support:

.. code-block:: bash

    sudo swupd bundle-add kernel-lts-dkms

Reboot and make sure you can start the new kernel.

Bundles
=======

Install these build tools before you install ZFS.

.. code-block:: bash

    sudo swupd bundle-add os-core-dev devpkg-openssl devpkg-util-linux

Install
*******

Get the ZFS code
================

The ZFS codebase moves quickly, just like the kernel codebase. Therefore
it's best that you get the source code from the ZFS on Linux repository,
hosted on Github.

Fetch the ZFS repository via git:

.. code-block:: bash

   git clone https://github.com/openzfs/zfs.git /opt/src/zfs

Remember where you check-out the git repository, because you will need it
when you upgrade ZFS. I have chosen /opt/src/zfs, but you can choose any
workspace you like. ZFS will not run from this location -- we copy the
source code into a DKMS directory in the next step.

Do not delete the source location when you have completed this tutorial:
you will need it later.

Compile the module
==================

We will build the module using DKMS. This will keep the module up to date
later as new kernels are released.

You have already fetched the zfs codebase. Check out the tagged version
that you plan to use. As of the time of this writing, the latest release
tag is `0.8.4`:

.. code-block:: bash

    cd /opt/src/zfs
    git checkout 0.8.4

Copy the source code into `/usr/src/zfs-0.8.4`. This exposes the source
code to DKMS. We will build the code from the new location:

.. code-block:: bash

    sudo cp -Rv /opt/src/zfs /usr/src/zfs-0.8.4
    cd /usr/src/zfs-0.8.4

The ZFS distribution provides a script to build a suitable dkms.conf file.
Build dkms.conf and install it into the DKMS tree.

.. code-block:: bash

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

.. code-block: bash

   sudo modprobe zfs


Set up systemd
==============

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
mount services, link the systemd.unit files into /etc and enable them.

.. code-block:: bash

   sudo ln -s ./etc/systemd/system/zfs-import-cache.service /etc/systemd/system/
   sudo ln -s ./etc/systemd/system/zfs-mount.service /etc/systemd/system/

   systemctl enable zfs-import-cache
   systemctl enable zfs-import.target

   systemctl enable zfs-mount
   systemctl enable zfs.target

ZFS requires you to explicitly install and enable the services you want. If you
want to use other ZFS service units, symlink them similarly to the example above.

If you prefer to use the zfs-mount-generator instead of zfs-mount, refer to the
Arch Linux Guide's `ZFS Mount Generator`_ section for details.

Load the kernel module at boot
==============================

The ZFS module will not load automatically at boot. Load the zfs.ko module
at boot time with systemd.

Systemd uses the `/etc/modules-load.d/` directory to load out-of-tree kernel modules.
Make sure that the directory exists:

.. code-block:: bash

    sudo mkdir -p /etc/modules-load.d

Create the configuration file:

.. code-block:: bash

    echo "zfs" | sudo tee /etc/modules-load.d/01-zfs.conf

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

If you suspect an issue with DKMS rebuilding your module, you can check two places
for information. The dkms-new-kernel service will show status that may help in troubleshooting:

.. code-block:: bash

   systemctl status dkms-new-kernel.service

Also, the systemd journal may have important information:

.. code-block:: bash

  journalctl -xe

Next steps
**********
You are ready to create zpools and datasets! For more information on using ZFS:

`FreeBSD Handbook chapter on ZFS`_
`Arch Linux ZFS Guide`_
`ZFS-on-Linux issue tracker`_

Acknowledgements:
*****************
.. _FreeBSD Handbook chapter on ZFS: https://www.freebsd.org/doc/handbook/zfs.html
.. _Arch Linux ZFS Guide: https://wiki.archlinux.org/index.php/ZFS
.. _ZFS Mount Generator: https://wiki.archlinux.org/index.php/ZFS#Using_zfs-mount-generator
.. _argument against shipping zfs.ko along with Linux: https://sfconservancy.org/blog/2016/feb/25/zfs-and-linux/
.. _the argument in favor: https://ubuntu.com/blog/zfs-licensing-and-linux
.. _ZFS-on-Linux issue tracker: https://github.com/openzfs/zfs/issues/10068
