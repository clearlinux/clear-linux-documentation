.. _kernel-modules:

Kernel Modules 
##############
Kernel modules are additional pieces of software capable of interacting with 
the kernel to add functionality, such as a hardware driver. Kernel modules 
may already be part of the Linux source tree (in-tree) or may come from an 
external source, such as a directly from vendor (out-of-tree).  

In many cases kernel modules are already available through |CL|. 
In other cases, a kernel module may not exist but can be requested to be 
enabled in the |CL| kernel. Finally, a situation may call for manually 
building and loading out-of-tree kernels. 

.. contents:: :local:
   :depth: 2



Adding a kernel module to a Clear Linux system
**********************************************
Using an existing module is significantly easier to maintain and retains 
signature verification of the |CL| kernel. For more information on |CL| 
security practices, see the :ref:`security` page.


Check if the module is already available through Clear Linux
============================================================
|CL| comes with many upstream kernel modules available for use.  If 
you require a kernel module, be sure to check whether it is already available in |CL| first. 


You can search for kernel modules using the :command:`swupd search` command. 
See :ref:`swupd-search` for more information. 


Consider requesting the module be added to |CL|
===============================================
If the kernel module you're needing is open source and likely to be useful to 
others, consider submitting a request to add or enable to the |CL| kernel.

You can make enhancement  requests to the |CL| distribution `on GitHub`_ .



Building and loading out-of-tree modules
========================================
In some cases you may need an out-of-tree kernel module that is not able 
to be made available through |CL|.

.. note::

   You can build and load out-of-tree kernel modules however secure boot must be 
   disabled, kernel module integrity checking must be disabled, and you are 
   responsible for building the module against new versions of the Linux kernel.
   
   Any time the kernel is upgraded on your Clear Linux system, you will 
   need to rebuild your out-of-tree modules.


This approach works well for individual development or testing. 
For a more scalable and customizable approach, consider using the 
`mixer tool`_ to provide a custom kernel and updates.


Building kernel modules
-----------------------

#. From a |CL| system, ensure you are running the *native* kernel. 
   Currently only the native kernel is enabled to build and load
   out-of-tree modules.

    .. code-block:: bash

        $ uname -r
        4.XX.YY-ZZZZ.native

    Ensure *.native* is in the kernel name

#. Install the `linux-dev` bundle to obtain the kernel headers, which are
   required for compiling kernel modules

    .. code-block:: bash

        sudo swupd bundle-add linux-dev

#. Follow instructions from the kernel module source code to compile the 
   kernel module


Loading kernel modules
----------------------

#. Disable Secure Boot in your BIOS or EFI you have enabled it. The loading of 
   new out-of-tree modules modifies the signatures  Secure Boot relies on for 
   trust. 


#. Disable signature checking for the kernel by modifying the kernel boot 
   parameters and reboot the system. 

   All kernel modules from |CL| have been signed to enforce kernel security. 
   However, out-of-tree modules break this chain of trust so this mechanism 
   needs to be disabled.
  
    .. code-block:: bash

        sudo mkdir -p /etc/kernel/cmdline.d
        sudo echo “module.sig_unenforce” > /etc/kernel/cmdline.d/load-modules.conf

#. Update the boot manager and reboot the system to implement the changed 
   kernel parameters.

    .. code-block:: bash

        sudo clr-boot-manager update
        sudo reboot

   
#. After rebooting, out-of-tree modules can be manually loaded with 
   :command:`modprobe` command. 

    .. code-block:: bash

        sudo modprobe ${module_name}



Optional: Use `modprobe` to specify module options and aliases
--------------------------------------------------------------

The :command:`modprobe` command can be used to load a module and set options.  

Because :command:`modprobe` can add or remove more than one module, due to 
modules having dependencies, a method of specifying what options are 
to be used with individual modules is useful. This can be done with 
configuration files under the :file:`/etc/modprobe.d` directory. 

    .. code-block:: bash

        sudo mkdir /etc/modprobe.d

All files underneath the :file:`/etc/modprobe.d` directory 
which end with the :file:`.conf` extension specify module options to use when
loading. This can also be used to create convenient aliases for modules or 
they can override the normal loading behavior altogether for those with 
special requirements. 

You can find more info on module loading in the modprobe.d manual page:

    .. code-block:: bash

        man modprobe.d



Optional: Configure kernel modules to load at boot
--------------------------------------------------

The :file:`/etc/modules-load.d` configuration directory can be used to 
specify kernel modules that should be automatically loaded at boot.

    .. code-block:: bash

        sudo mkdir /etc/modules-load.d


All files underneath the :file:`/etc/modules-load.d` directory 
which end with the :file:`.conf` extension contain a list of module names 
of aliases (one per line) to load at boot.


You can find more info on module loading in the modules-load.d manual page:

    .. code-block:: bash

        man modules-load.d






.. _`on GitHub`: https://github.com/clearlinux/distribution 
.. _`mixer tool`: https://clearlinux.org/features/mixer-tool

