.. _kernel-modules:

Add kernel modules manually
###########################

Kernel modules are additional pieces of software capable of being inserted
into the Linux kernel to add functionality, such as a hardware driver. Kernel
modules may already be part of the Linux source tree (in-tree) or may come
from an external source, such as directly from a vendor (out-of-tree).  

In cases where drivers beyond those enabled by default in |CL-ATTR| are
needed it may be necessary to manually build out-of-tree modules. 

Out-of-tree kernel modules can be managed by  `Dynamic Kernel Module System
(DKMS) <kernel-modules-dkms>`_ on |CL| for automatic rebuilding upon kernel
updates. Out-of-tree kernel modules can also be manually built and maintained
using the instructions in this document. 



.. contents:: :local:
   :depth: 1
   :backlinks: top


.. _kernel-modules-availability-begin:

Kernel module availability in |CL|
==================================

Before continuing, check if the kernel module you're looking for is already
available in |CL| or can be requested.


Check if the module is already available
----------------------------------------

|CL| comes with many upstream kernel modules available for use.  If you
require a kernel module, be sure to check whether it is already available in
|CL| first. 

Using an existing module is significantly easier to maintain and retains
signature verification of the |CL| kernel. For more information on |CL|
security practices, see the :ref:`security` page.

You can search for kernel module file names, which end with the :file:`.ko`
file extension, using the :command:`swupd search` command. For example:
:command:`sudo swupd search ${module_name}.ko`. See :ref:`swupd-search` for
more information. 


Request the module be added to |CL|
-----------------------------------

If the kernel module you need is already open source (e.g. in the Linux
upstream) and likely to be useful to others, consider submitting a request to
add or enable in the |CL| kernel.

Make enhancement requests to the |CL| distribution `on GitHub`_ .

.. _kernel-modules-availability-end:


Build, install, and load an out-of-tree module
==============================================

In some cases you may need an out-of-tree kernel module that is not available
through |CL|.


Prerequisites 
-------------

You can build and load out-of-tree kernel modules, however you must:

* Disable Secure Boot.
* Disable kernel module integrity checking.
* Have a kernel module package in the form of source code.
* Rebuild the module against new versions of the Linux kernel.

.. note::

   Any time the kernel is upgraded on your Clear Linux system, you will 
   need to rebuild your out-of-tree modules.

This approach works well for individual development or testing. For a more
scalable and customizable approach, consider using the `mixer tool`_ to
provide a custom kernel and updates.


Build and install kernel module
-------------------------------

#. Determine which kernel variant is running on |CL|. In the example below,
   the *native* kernel is in use.

   .. code-block:: bash

      $ uname -r
      5.XX.YY-ZZZZ.native

#. Install the kernel dev bundle corresponding to the installed kernel. The
   kernel dev bundle contains the kernel headers, which are required for
   compiling kernel modules.For example:
    
   * `linux-dev` for developing against the native kernel.
   * `linux-lts-dev` for developing against the LTS kernel.

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
------------------

#. Disable Secure Boot in your system's UEFI settings, if you have enabled
   it. The loading of new out-of-tree modules modifies the signatures Secure
   Boot relies on for trust. 


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

      :command:`clr-boot-manager update` does not return any
      console output if successful.

   
#. After rebooting, out-of-tree modules can be manually loaded with 
   :command:`insmod`. 

   .. code-block:: bash

      sudo insmod </PATH/TO/MODULE.ko>



.. _kernel-modules-autoload-begin:

Optional: Specify module options and aliases
============================================

Use the :command:`modprobe` command to load a module and set options.  

Because :command:`modprobe` may add or remove more than one module due to
modules having dependencies, a method of specifying what options are to be
used with individual modules is useful. This can be done with configuration
files under the :file:`/etc/modprobe.d` directory. 

.. code-block:: bash

   sudo mkdir /etc/modprobe.d

All files underneath the :file:`/etc/modprobe.d` directory that end with the
:file:`.conf` extension specify module options to use when loading. This can
also be used to create convenient aliases for modules or they can override the
normal loading behavior altogether for those with special requirements. 

You can find more info on module loading in the modprobe.d manual page:

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

You can find more info on module loading in the modules-load.d manual page:

.. code-block:: bash

   man modules-load.d


.. _kernel-modules-autoload-end:


.. _`on GitHub`: https://github.com/clearlinux/distribution 
.. _`mixer tool`: https://clearlinux.org/features/mixer-tool
