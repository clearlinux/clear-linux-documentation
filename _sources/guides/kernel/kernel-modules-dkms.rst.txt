.. _kernel-modules-dkms:

Add kernel modules with DKMS
############################

This guide describes how to add kernel modules with
:abbr:`DKMS (Dynamic Kernel Module System)`.

.. contents:: :local:
   :depth: 1
   :backlinks: top

Overview
********

Certain kernel modules are enabled by default in |CL-ATTR|. To use additional
kernel modules that are not part of the Linux source tree, you may need to
build out-of-tree kernel modules. Use this guide to add kernel modules with
DKMS or refer to :ref:`kernel-modules`.

Description
***********

Kernel modules are additional pieces of software capable of being inserted
into the Linux kernel to add functionality, such as a hardware driver.
Kernel modules may already be part of the Linux source tree (in-tree) or may
come from an external source, such as directly from a vendor (out-of-tree).

DKMS is a framework that facilitates the building and installation of kernel
modules. DKMS allows |CL| to provide hooks that automatically rebuild modules
against new kernel versions.

.. include:: kernel-modules.rst
   :start-after: kernel-modules-availability-begin:
   :end-before: kernel-modules-availability-end:

Install DKMS
************

.. _kernel-modules-dkms-install-begin:

The :command:`kernel-native-dkms` bundle provides the DKMS program and Linux
kernel headers, which are placed under :file:`/usr/lib/modules/$(uname
-r)/build/include/` and are required to compile kernel modules.

The :command:`kernel-native-dkms` bundle also:

* Adds a `systemd` update trigger
  (:file:`/usr/lib/systemd/system/dkms-new-kernel.service`) to automatically
  run DKMS to rebuild modules after a kernel upgrade occurs with :ref:`swupd
  update <swupd-guide>`.

* Disables kernel module signature verification by appending a kernel
  command-line parameter (:command:`module.sig_unenforce`) from the
  :file:`/usr/share/kernel/cmdline.d/clr-ignore-mod-sig.conf` file.

* Adds a notification to the Message of the Day (MOTD) indicating kernel
  module signature verification is disabled.

.. warning::

   We recommend that you always review the :command:`swupd update` output
   to make sure kernel modules were successfully rebuilt against the new
   kernel. This is especially important for systems where a successful boot
   relies on a kernel module.

.. _kernel-modules-dkms-install-begin-alt:

Install the :command:`kernel-native-dkms` or :command:`kernel-lts-dkms`
bundle.

#. Determine which kernel variant is running on |CL|. Only the *native*
   and *lts* kernels are enabled to build and load out-of-tree kernel modules
   with DKMS.

   .. code-block:: console

      $ uname -r
      5.XX.YY-ZZZZ.native

   Ensure *.native* or *.lts* is in the kernel name.

#. Install the DKMS bundle corresponding to the installed kernel. Use
   :command:`kernel-native-dkms` for the native kernel or
   :command:`kernel-lts-dkms` for the lts kernel.

   .. code-block:: bash

      sudo swupd bundle-add kernel-native-dkms

   or

   .. code-block:: bash

      sudo swupd bundle-add kernel-lts-dkms


#. Update the |CL| bootloader and reboot, and 
   ensure that you can start the new kernel.

   .. code-block:: bash

      sudo clr-boot-manager update
      reboot

.. _kernel-modules-dkms-install-end:

Build, install, and load an out-of-tree module
**********************************************

Follow the steps in this section if you are an individual user or testing,
and you need an out-of-tree kernel module that is not available through
|CL|. For a more scalable and customizable approach, we recommend using
:ref:`mixer` to provide a custom kernel and updates.

Prerequisites
=============

Before you begin, you must:

* Disable Secure Boot in UEFI/BIOS. The loading of new out-of-tree modules
  modifies the signatures that Secure Boot relies on for trust.

* Obtain a kernel module package in the form of source code or
  pre-compiled binaries.

Obtain kernel module source
===========================

A required :file:`dkms.conf` file inside of the kernel module's source code
directory informs DKMS how the kernel module should be compiled.

Kernel modules may come packaged as:

- Source code without a :file:`dkms.conf` file
- Source code with a premade :file:`dkms.conf` file
- Source code with a premade :file:`dkms.conf` file and precompiled module
  binaries
- Precompiled module binaries only (without source code)

Of the package types listed above, only precompiled kernel module binaries
will not work, because |CL| requires kernel modules to be built against the
same kernel source tree before they can be loaded. If you are only able to
obtain source code without a :file:`dkms.conf` file, you must manually create
a :file:`dkms.conf` file, described later in this document.

#. Download the kernel module's source code.

   * Review the available download options. Some kernel modules provide
     separate archives that are specifically enabled for DKMS support.

   * Review the README documentation, because it often provides required
     information to build the module with DKMS support.

   .. code-block:: bash

      curl -O http://<URL-TO-KERNEL-MODULE-SOURCE>.tar.gz
      tar -xvf <KERNEL-MODULE-SOURCE>.tar.gz
      cd <KERNEL-MODULE-SOURCE>/
      cat README

Build kernel module with an existing dkms.conf
==============================================

If the kernel module maintainer packaged the source archive with the
:command:`dkms mktarball` command, the entire archive can be passed to the
:command:`dkms ldtarball` which completes many steps for you.

The archive contains the required :file:`dkms.conf` file, and may contain
a :file:`dkms_source_tree` directory and a :file:`dkms_binaries_only`
directory.

#. Run the :command:`dkms ldtarball` command against the kernel
   module archive.

   .. code-block:: bash

      dkms ldtarball <KERNEL-MODULE-SOURCE_WITH_DKMS>.tar.gz


   :command:`dkms ldtarball` places the kernel module source under
   :file:`/usr/src/<MODULE-NAME>-<MODULE-VERSION>/`, builds it if necessary,
   and adds the module into the DKMS tree.


#. Verify the kernel module is detected by checking the output of the
   :command:`dkms status` command.

   .. code-block:: bash

      dkms status


#. Install the kernel module.

   .. code-block:: bash

      dkms install -m <MODULE-NAME> -v <MODULE-VERSION>

Build kernel module without an existing dkms.conf
=================================================

If the kernel module source does not contain a :file:`dkms.conf` file or the
:command:`dkms ldtarball` command encounters errors, you must manually
create the file.

Review the kernel module README documentation for guidance on what needs to be
in the :file:`dkms.conf` file, including special variables that may be
required to build successfully.

Here are some additional resources that can be used for reference:

* DKMS manual page (:command:`man dkms`) shows detailed syntax in the
  DKMS.CONF section.

* Ubuntu community wiki entry for the `Kernel DKMS Package`_ shows an example
  where a single package contains multiple modules.

* Sample `dkms.conf`_ file in the GitHub\* repository for the DKMS project.

.. note::

   :command:`AUTOINSTALL=yes` must be set in the dkms.conf for the module to
   be automatically recompiled with |CL| updates.

The instructions below show a generic example:

#. Create or modify the :file:`dkms.conf` file inside of the extracted source
   code directory.

   .. code-block:: ShellSession

      $ EDITOR dkms.conf

      MAKE="make -C src/ KERNELDIR=/lib/modules/${kernelver}/build"
      CLEAN="make -C src/ clean"
      BUILT_MODULE_NAME=custom_module
      BUILT_MODULE_LOCATION=src/
      PACKAGE_NAME=custom_module
      PACKAGE_VERSION=1.0
      DEST_MODULE_LOCATION=/kernel/drivers/other
      AUTOINSTALL=yes

   This example identifies a kernel module named *custom_module* with version
   *1.0*.

#. Copy the kernel module source code into the :file:`/usr/src/` directory.

   .. code-block:: bash

      sudo mkdir /usr/src/<PACKAGE_NAME>-<PACKAGE_VERSION>
      sudo cp -Rv . /usr/src/<PACKAGE_NAME>-<PACKAGE_VERSION>

   .. note::

      *<PACKAGE_NAME>* and *<PACKAGE_VERSION>* must match the entries in the
      :file:`dkms.conf` file.

#. Add the kernel module to the DKMS tree so that it is tracked by DKMS.

   .. code-block:: bash

      sudo dkms add -m <MODULE-NAME>

#. Build the kernel module using DKMS. If the build encounters errors,
   you may need to edit the :file:`dkms.conf` file.

   .. code-block:: bash

      sudo dkms build -m <MODULE-NAME> -v <MODULE-VERSION>

#. Install the kernel module using DKMS.

   .. code-block:: bash

      sudo dkms install -m <MODULE-NAME> -v <MODULE-VERSION>

Load kernel module
==================

By default, DKMS installs modules "in-tree" under :file:`/lib/modules` so the
:command:`modprobe` command can be used to load them.

#. Load the installed module with the :command:`modprobe` command.

    .. code-block:: bash

       sudo modprobe <MODULE-NAME>

#. Validate the kernel module is loaded.

   .. code-block:: bash

      lsmod | grep <MODULE-NAME>

Examples
********

.. include:: kernel-modules.rst
   :start-after: kernel-modules-autoload-begin:
   :end-before: kernel-modules-autoload-end:

Related topics
**************

* `Dynamic Kernel Module System (DKMS)`_

* `Dell Linux Engineering Dynamic Kernel Module Support: From Theory to Practice <https://www.kernel.org/doc/ols/2004/ols2004v1-pages-187-202.pdf>`_

* `Linux Journal: Exploring Dynamic Kernel Module Support <https://www.linuxjournal.com/article/6896>`_

.. _Dynamic Kernel Module System (DKMS): https://github.com/dell/dkms

.. _Kernel DKMS Package: https://help.ubuntu.com/community/Kernel/DkmsDriverPackage#Configure_DKMS

.. _dkms.conf: https://github.com/dell/dkms/blob/master/sample.conf
