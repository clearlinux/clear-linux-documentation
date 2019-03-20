.. _kernel-modules-dkms:

Add kernel modules with DKMS
############################

Kernel modules are additional pieces of software capable of being inserted 
into the Linux kernel to add functionality, such as a hardware driver. 
Kernel modules may already be part of the Linux source tree (in-tree) or may 
come from an external source, such as directly from a vendor (out-of-tree).  

In cases where drivers beyond those enabled by default in |CL-ATTR| are
needed it may be necessary to manually build out-of-tree modules. 

Out-of-tree kernel modules can be can be  `manually built and maintained
<kernel-modules>`_. Out-of-tree kernel modules can also be managed with the
`Dynamic Kernel Module System (DKMS)`_ on |CL| using the instructions in this
document.

:abbr:`DKMS (Dynamic Kernel Module System)` is a framework that facilitates
the building and installation of kernel modules. This allows |CL| to provide
hooks that automatically rebuild modules against new kernel versions. 


.. contents:: :local:
   :depth: 1
   :backlinks: top



.. include:: kernel-modules.rst
   :start-after: kernel-modules-availability-begin:
   :end-before: kernel-modules-availability-end:




Install DKMS on |CL|
====================

.. _kernel-modules-dkms-install-begin:

The *kernel-native-dkms* bundle provides the :command:`dkms` program and
Linux kernel headers, which are required for compiling kernel modules.

The *kernel-native-dkms* bundle also:

* Adds a systemd update trigger
  (:file:`/usr/lib/systemd/system/dkms-new-kernel.service`) to automatically
  run DKMS to rebuild modules after a kernel upgrade occurs with :ref:`swupd
  update <swupd-guide>`.

* Disables kernel modules signature verification by appending a kernel
  command-line parameter (:command:`module.sig_unenforce`) from
  :file:`/usr/share/kernel/cmdline.d/clr-ignore-mod-sig.conf`.

* Adds a notification to the Message of the Day (MOTD) indicating kernel
  modules signature verification is disabled. 

.. warning::

   #. It is important to always review the output of :command:`swupd update` to
      make sure kernel modules rebuilt against the new kernel successfully. This is
      especially important for systems where a successful boot relies on a kernel
      module.


Install the *kernel-native-dkms* or *kernel-lts-dkms* bundle:

#. Determine which kernel variant is running on |CL|. Only the *native*
   and *lts* kernels are enabled to build and load out-of-tree kernel modules
   with DKMS.

   .. code-block:: bash

      $ uname -r
      5.XX.YY-ZZZZ.native

   Ensure *.native* or *.lts* is in the kernel name.

#. Install the dkms bundle corresponding to the installed kernel.
   *kernel-native-dkms* for the native kernel or *kernel-lts-dkms* for the 
   lts kernel.

   .. code-block:: bash

      sudo swupd bundle-add kernel-native-dkms

   or

   .. code-block:: bash

      sudo swupd bundle-add kernel-lts-dkms
   

#. Update the |CL| bootloader and reboot.

   .. code-block:: bash

      sudo clr-boot-manager update 
      reboot


.. _kernel-modules-dkms-install-end:

Build, install, and load an out-of-tree module
==============================================
In some cases you may need an out-of-tree kernel module that is not available
through |CL|.


Prerequisites 
-------------

You can build and load out-of-tree kernel modules, however you must:

* Disable Secure Boot in UEFI/BIOS. The loading of new out-of-tree modules
  modifies the signatures Secure Boot relies on for trust. 
  
* Have a kernel module package in the form of source code and/or precompiled
  binaries.


This approach works well for individual use or testing. For a more
scalable and customizable approach, consider using the `mixer tool`_ to
provide a custom kernel and updates.

Obtain kernel module source
---------------------------

A :file:`dkms.conf` file inside of the kernel module's source code directory
is required to inform DKMS how the kernel module should be compiled. 

Kernel modules may come packaged as:

- Source code without a dkms.conf
- Source code with a premade dkms.conf
- Source code with a premade dkms.conf and precompiled module binaries
- Precompiled module binaries only without source code

Precompiled kernel module binaries will not work on |CL| because it requires
kernel modules to be built against the same kernel source tree before they can
be loaded.

If you are only able to obtain source code without a dkms.conf, a
:file:`dkms.conf` file will need to be manually created. 

#. Download the kernel module's source code.
   
   - Review the available download options. Some kernel modules provide
     separate archives which are specifically enabled for DKMS support.
 
   - Review the README documentation because it often provides required
     information to build the module with DKMS support.

   .. code-block:: bash

      curl -O http://<URL-TO-KERNEL-MODULE-SOURCE>.tar.gz
      tar -xvf <KERNEL-MODULE-SOURCE>.tar.gz
      cd <KERNEL-MODULE-SOURCE>/
      cat README


Build kernel module with an existing dkms.conf
----------------------------------------------

If the kernel module maintainer packaged the source archive with the
:command:`dkms mktarball` command, the entire archive can be passed to the
:command:`dkms ldtarball` which will complete many steps for you.

The archive will contain the required :file:`dkms.conf` file, and may contain
a :file:`dkms_source_tree` directory and a :file:`dkms_binaries_only`
directory. 


#. Run the :command:`dkms ldtarball` command against the kernel module archive.

   .. code-block:: bash

      dkms ldtarball <KERNEL-MODULE-SOURCE_WITH_DKMS>.tar.gz


   :command:`dkms ldtarball` will place the kernel module source under
   :file:`/usr/src/<MODULE-NAME>-<MODULE-VERSION>/`, build if necessary, and
   add the module into the dkms tree.


#. Verify the kernel module is detected by checking the output of 
   :command:`dkms status`.
 
   .. code-block:: bash

      dkms status


#. Install the kernel module. 

   .. code-block:: bash

      dkms install -m <MODULE-NAME> -v <MODULE-VERSION>



Build kernel module without an existing dkms.conf
-------------------------------------------------

If the kernel module source does not contain a :file:`dkms.conf` file or the
:command:`dkms ldtarball` command encounters errors, it needs to be manually
created.

Review the kernel module README documentation for guidance on what needs to be
in the :file:`dkms.conf` including special variables that may be required to
build successfully.

Here are some additional resources that can be used for reference:

* The DKMS manual page (:command:`man dkms`) shows detailed syntax in the
  DKMS.CONF section

* `<https://help.ubuntu.com/community/Kernel/DkmsDriverPackage#Configure_DKMS>`_
  (shows an example where a single package contains multiple modules)

* `<https://github.com/dell/dkms/blob/master/sample.conf>`_


The instructions below show a generic example:

#. Create or modify the :file:`dkms.conf` file inside of the extracted source
   code directory. 

   .. code-block:: bash

      $EDITOR dkms.conf

      MAKE="make -C src/ KERNELDIR=/lib/modules/${kernelver}/build"
      CLEAN="make -C src/ clean"
      BUILT_MODULE_NAME=custom_module
      BUILT_MODULE_LOCATION=src/
      PACKAGE_NAME=custom_module
      PACKAGE_VERSION=1.0
      DEST_MODULE_LOCATION=/kernel/drivers/other

   This example identifies a kernel module named *custom_module* with version
   *1.0*.

#. Copy the kernel module source code into the :file:`/usr/src/` directory.

   .. code-block:: bash

      sudo mkdir /usr/src/<PACKAGE_NAME>-<PACKAGE_VERSION>
      sudo cp -Rv . /usr/src/<PACKAGE_NAME>-<PACKAGE_VERSION>

   .. note::
      *<PACKAGE_NAME>* and *<PACKAGE_VERSION>* should match the entries in :file:`dkms.conf`


#. Add the kernel module to the DKMS tree so that it is tracked by DKMS.

   .. code-block:: bash

      sudo dkms add -m <MODULE-NAME> 

#. Build the kernel module using DKMS. If the build encounters errors, the
   :file:`dkms.conf` may need to be adjusted.

   .. code-block:: bash

      sudo dkms build -m <MODULE-NAME> -v <MODULE-VERSION>


#. Install the kernel module using DKMS.

   .. code-block:: bash

      sudo dkms install -m <MODULE-NAME> -v <MODULE-VERSION>
      


Load kernel module
------------------

By default, DKMS installs modules "in-tree" under :file:`/lib/modules` so the
:command:`modprobe` command can be used to load them.

#.  Load the installed module with the :command:`modprobe` command.

    .. code-block:: bash

       sudo modprobe <MODULE-NAME>

#. Validate the kernel module is loaded.

   .. code-block:: bash

      lsmod | grep <MODULE-NAME>




.. include:: kernel-modules.rst
   :start-after: kernel-modules-autoload-begin:
   :end-before: kernel-modules-autoload-end:




Additional resources
====================
* `Dynamic Kernel Module System (DKMS) project on GitHub <https://github.com/dell/dkms>`_ 

* `Dell Linux Engineering Dynamic Kernel Module Support: From Theory to Practice <https://www.kernel.org/doc/ols/2004/ols2004v1-pages-187-202.pdf>`_

* `Linux Journal: Exploring Dynamic Kernel Module Support <https://www.linuxjournal.com/article/6896>`_


.. _`on GitHub`: https://github.com/clearlinux/distribution 

.. _`mixer tool`: https://clearlinux.org/features/mixer-tool

.. _`Dynamic Kernel Module System (DKMS)`: https://github.com/dell/dkms
