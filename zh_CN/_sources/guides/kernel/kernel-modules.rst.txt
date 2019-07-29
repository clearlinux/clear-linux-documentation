.. _kernel-modules:

Add kernel modules manually
###########################

This guide describes how to add kernel modules manually.

.. contents:: :local:
   :depth: 1
   :backlinks: top

Overview
********

Certain kernel modules are enabled by default in |CL-ATTR|. To use additional
kernel modules that are not part of the Linux source tree, you may need to
build out-of-tree kernel modules. Use this guide to add kernel modules
manually, or refer to :ref:`kernel-modules-dkms`.

Description
***********

Kernel modules are additional pieces of software capable of being inserted
into the Linux kernel to add functionality, such as a hardware driver.
Kernel modules may already be part of the Linux source tree (in-tree) or may
come from an external source, such as directly from a vendor (out-of-tree).


.. _kernel-modules-availability-begin:

Kernel module availability
**************************

|CL| comes with many upstream kernel modules available for use. Using an
existing module is significantly easier to maintain and retains signature
verification of the |CL| kernel. For more information on |CL| security
practices, see the :ref:`security` page.

Before continuing, check if the kernel module you're looking for is already
available in |CL| or submit a request to add the module.


Check if the module is already available
========================================


You can search for kernel module file names, which end with the :file:`.ko`
file extension, using the :command:`swupd search` command, as shown in the
following example. See :ref:`swupd-guide` for more information.

.. code-block:: bash

   sudo swupd search ${module_name}.ko


Submit a request to add the module
==================================

If the kernel module you need is already open source (for example, in the Linux
upstream) and likely to be useful to others, consider submitting a request to
add or enable it in the |CL| kernel.

Make enhancement requests to the |CL| 'Distribution Project'_ on GitHub.

.. _kernel-modules-availability-end:


Build, install, and load an out-of-tree module
**********************************************

Follow the steps in this section if you are an individual user or testing, and
you need an out-of-tree kernel module that is not available through |CL|. For
a more scalable and customizable approach, we recommend using the
:ref:`mixer` to provide a custom kernel and updates.


Prerequisites
=============

Before you begin, you must:

* Disable Secure Boot.
* Disable kernel module integrity checking.
* Have a kernel module package in the form of source code.
* Rebuild the module against new versions of the Linux kernel.

.. note::

   Any time the kernel is upgraded on your Clear Linux system, you must
   rebuild your out-of-tree modules.


Build and install kernel module
===============================

#. Determine which kernel variant is running on |CL|. In the example below,
   the *native* kernel is in use.

   .. code-block:: bash

      $ uname -r
      5.XX.YY-ZZZZ.native

#. Install the kernel dev bundle corresponding to the installed kernel. The
   kernel dev bundle contains the kernel headers, which are required for
   compiling kernel modules. For example:

   * :command:`linux-dev` for developing against the native kernel.
   * :command:`linux-lts-dev` for developing against the LTS kernel.

   .. code-block:: bash

      sudo swupd bundle-add linux-dev

#. Follow instructions from the kernel module source code to compile the
   kernel module. For example:

   .. code-block:: bash

      curl -O http://<URL-TO-KERNEL-MODULE-SOURCE>.tar.gz
      tar -xvf <KERNEL-MODULE-SOURCE>.tar.gz
      cd <KERNEL-MODULE-SOURCE>/
      cat README



Load kernel module
==================

#. Disable Secure Boot in your system's UEFI settings, if you have enabled
   it. The loading of new out-of-tree modules modifies the signatures that
   Secure Boot relies on for trust.

#. Disable signature checking for the kernel by modifying the kernel boot
   parameters and reboot the system.

   All kernel modules from |CL| have been signed to enforce kernel security.
   However, out-of-tree modules break this chain of trust so this mechanism
   needs to be disabled.

   .. code-block:: bash

      sudo mkdir -p /etc/kernel/cmdline.d
      echo "module.sig_unenforce" | sudo tee /etc/kernel/cmdline.d/allow-unsigned-modules.conf

#. Update the boot manager and reboot the system to implement the changed
   kernel parameters.

   .. code-block:: bash

        sudo clr-boot-manager update
        sudo reboot

   .. note::

      If successful, the :command:`clr-boot-manager update` command does not
      return any console output.

#. After rebooting, manually load out-of-tree modules using the
   :command:`insmod` command.

   .. code-block:: bash

      sudo insmod </PATH/TO/MODULE.ko>

Examples
********

.. _kernel-modules-autoload-begin:

Optional: Specify module options and aliases
============================================

Use the :command:`modprobe` command to load a module and set options.

:command:`modprobe` may add or remove more than one module due to module
interdependencies. You can specify which options to use with individual modules,
by using configuration files under the :file:`/etc/modprobe.d` directory.

.. code-block:: bash

   sudo mkdir /etc/modprobe.d

All files underneath the :file:`/etc/modprobe.d` directory that end with the
:file:`.conf` extension specify module options to use when loading. You can use
:file:`.conf` files to create convenient aliases for modules or to override the
normal loading behavior altogether for those with special requirements.

Learn more about :command:`modprobe` on the modprobe.d manual page:

.. code-block:: bash

   man modprobe.d

Optional: Configure kernel modules to load at boot
==================================================

Use the :file:`/etc/modules-load.d` configuration directory to specify kernel
modules to load automatically at boot.

.. code-block:: bash

   sudo mkdir /etc/modules-load.d

All files underneath the :file:`/etc/modules-load.d` directory that end with
the :file:`.conf` extension contain a list of module names of aliases (one per
line) to load at boot.

Learn more about module loading in the modules-load.d manual page:

.. code-block:: bash

   man modules-load.d


.. _kernel-modules-autoload-end:

Related topic
*************

* :ref:`kernel-modules-dkms`

.. _`Distribution Project`: https://github.com/clearlinux/distribution
