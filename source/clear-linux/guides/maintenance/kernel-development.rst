.. _kernel-development:

Kernel development on Clear Linux 
#################################

This document shows how to obtain and compile a Linux kernel source 
using the |CL-ATTR| development tooling.

The `kernels available in Clear Linux`_ aim to be performant and practical. 
In some cases, it may be necessary to modify the kernel to suit your specific 
needs or test new kernel code as a developer.

.. contents:: :local:
   :depth: 2
   :backlinks: top

Source RPM files (SRPM) are also available for all |CL| kernels, and can be 
used for development instead. The latest source RPM files are available at:
`https://download.clearlinux.org/current/source/SRPMS/`_


Request the change be included with the |CL| kernel
***************************************************

If the kernel modification you need is already open source and likely to be 
useful to others, consider submitting a request to include it in the
|CL| kernels.

If your change request is accepted, you do not need to maintain your own 
modified kernel.

Make enhancement requests to the |CL| distribution `on GitHub`_ .


Customize the Linux kernel source
*********************************

In some cases, it may be necessary to modify the kernel to suit your specific 
needs or test new kernel code as a developer.

You can build and install a custom kernel, however you must:

* Disable Secure Boot
* Maintain any updates to the kernel going forward

To create a custom kernel, start with the |CL| development environment. 
Then make changes to the kernel, build it, and install it.



Install the |CL| development tooling framework
==============================================

.. include:: autospec.rst
   :start-after: install-tooling-after-header:
   :end-before: install-tooling-end:



Clone the Linux kernel package 
==============================
Clone the existing kernel package repository from |CL| as a starting point.

#. Clone the Linux kernel package from |CL|.

   .. code-block:: bash

      cd ~/clearlinux
      make clone_linux


#. Navigate into the cloned package directory.

   .. code-block:: bash

      cd ~/clearlinux/packages/linux

.. note::
    The "linux" package is the kernel that comes with |CL| in the kernel-native bundle.
    You can alternatively use a different kernel variant as the base for modification. 
    For a list of kernel package names which you can clone instead, see the `clearlinux-pkgs GitHub`_.



Change the kernel version 
=========================

|CL| tends to use the latest kernel available from `kernel.org`_, the Linux 
upstream. The kernel version that will be built can be changed in the 
RPM SPEC file.

While most packages in Clear Linux are typically packaged using 
`autospec`_, the kernel is not. This means control files provided 
by autospec are not available and changes must be made manually.


#. Open the Linux kernel package RPM SPEC file in an editor.

   .. code-block:: bash

      $EDITOR linux.spec


#. Modify the Version, Release, and Source0 URL entries at the top of the 
   file to change the version of Linux kernel that will be compiled.

   A list of current and available kernel release can be found on 
   `kernel.org`_.

   .. code-block:: bash
      
      Name:           linux
      Version:        4.20.5
      Release:        690
      License:        GPL-2.0
      Summary:        The Linux kernel
      Url:            http://www.kernel.org/
      Group:          kernel
      Source0:        https://cdn.kernel.org/pub/linux/kernel/v4.x/linux-4.20.5.tar.xz
      Source1:        config
      Source2:        cmdline

   .. note::
      Consider changing the Name in the RPM spec file to easily identify a modified kernel.

#. Commit and save the changes to the file.



Modify kernel configuration 
===========================

Existing kernel features and in-tree kernel modules can be enabled or 
disabled in the kernel configuration file, :file:`.config` , at compile time.

To manage unique changes that have been made to the kernel config file, 
|CL| uses a kernel config fragment file named :file:`config-fragment`. 
Managing kernel configuration changes with a configuration fragment file 
instead of directly editing the :file:`.config` file helps identify the 
unique configuration changes that have been made and makes applying any 
future default configuration values easier. 

The :file:`config-fragment` is the **only** file that is modified and is 
eventually merged with the main :file:`.config`.



#. Open the kernel :file:`config-fragment` file in an editor.
   
   Due to how |CL| packaging tools make use of :command:`mock` environments 
   psuedo-GUI tools that abstract kernel configuration such as menuconfig do 
   not work. 

   .. code-block:: bash

      $EDITOR config-fragment


#. Find the configuration values you are looking for. 
   If a particular setting does not already exist, it can be added manually.

   For example, the snippet below shows BTRFS support configuration indicating
   it is enabled in-tree.

   .. code-block:: bash

      CONFIG_BTRFS_FS=y
      CONFIG_BTRFS_FS_POSIX_ACL=y


#. Modify the configuration values as desired. 

   For example, the snippet below shows BTRFS support configuration changed 
   change to be disabled and commented out.

   .. code-block:: bash
      
      # CONFIG_BTRFS_FS is not set
      # CONFIG_BTRFS_FS_POSIX_ACL is not set

#. Commit and save the changes to the :file:`config-fragment` file.


#. Run the :command:`make config` command to apply the changes made in the 
   :file:`config-fragment` file and regenerate the :file:`config` file.

   .. code-block:: bash

      make config



Modify kernel source code 
=========================

Changes to kernel code are applied with patch files. Patch files are 
formatted git commits that can be applied to the main source code.

If you have a large number of patches or a more complex workflow, 
consider using a patch management tool in addition to Git such as 
`Quilt`_. 


#. Clone the linux kernel source code into a new working directory.

   .. code-block:: bash

      git clone git://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git


#. Make any code changes to the Linux source files.


#. Track and commit your changes to the local git repo. 

   .. code-block:: bash

      git commit -m "My patch for driver A"


#. Generate a patch file based on your git commits. 
   <n> represents the number of local commits to create patch file. 
   See the `git-format-patch Documentation`_ for detailed information 
   on using :command:`git format-patch`

   .. code-block:: bash
      
      git format-patch -<n>


#. Copy the patch files from the patches directory in the linux 
   source tree to the RPM build directory.

   .. code-block:: bash
      
      cp patches/*.patch ~/clearlinux/packages/linux/


#. Navigate back to the RPM build directory.

   .. code-block:: bash
      
      cd ~/clearlinux/packages/linux/


#. Open the Linux kernel package RPM SPEC file in an editor.

   .. code-block:: bash

      $EDITOR linux.spec


#. Locate the section of the SPEC file that contains existing patch 
   variable definitions and append your patch file name. Ensure the 
   patch number does not collide with an existing patch.

   .. code-block:: bash

      #
      # Small Clear Linux Tweaks
      #
      Patch0501: 0501-zero-extra-registers.patch
      Patch0502: 0502-locking-rwsem-spin-faster.patch

      #Serie1.name WireGuard
      #Serie1.git  https://git.zx2c4.com/WireGuard
      #Serie1.tag  00bf4f8c8c0ec006633a48fd9ee746b30bb9df17
      Patch1001: 1001-WireGuard-fast-modern-secure-kernel-VPN-tunnel.patch
      #Serie1.end

      Patch2001: 2001-my-patch-for-driver-A.patch


#. Locate the section of the SPEC file further down that contains 
   patch application and append your patch file number used in the step above.

   .. code-block:: bash

      #
      # Small tweaks
      #
      %patch0501 -p1
      %patch0502 -p1

      #Serie1.patch.start
      %patch1001 -p1
      #Serie1.patch.end

      %patch2001 -p1


#. Commit and save the changes to the RPM SPEC file.



Build and install the kernel
****************************
After changes have been made to the kernel SPEC file and config file, 
the kernel is ready to be compiled and packaged into an RPM.

#. Start the compilation process by issuing the :command:`make build` command. 
   This process is typically resource intensive and will take a while.

   .. code-block:: bash
      
      make build


#. The result will be multiple :file:`.rpm` files in the :file:`rpms` 
   directory as output. 

   .. code-block:: bash
      
      ls rpms/

   The kernel RPM will be named :file:`linux<name>-<version><release>.x86_64.rpm`


#. The kernel RPM file can be input to the `mixer tool`_ to create a custom 
   bundle and mix of |CL|.

   

Alternatively, the kernel RPM bundle can be installed manually on a local 
machine for testing. This approach works well for individual development or 
testing. For a more scalable and customizable approach, consider using the 
`mixer tool`_ to provide a custom kernel with updates.

1. Install the kernel RPM onto the local system with the :command:`rpm` command.

   .. code-block:: bash

      sudo rpm -ivh linux-custom.<version>.<release>.x86_64.rpm

#. Update the |CL| boot manager using :command:`clr-boot-manager` and reboot.

   .. code-block:: bash

      sudo clr-boot-manager update

      sudo clr-boot-manager list-kernels
      sudo clr-boot-manager set-kernel <name>

      sudo reboot

#. After a reboot, verify the customized kernel is running.

   .. code-block:: bash

      uname -a



Related topics
**************

* :ref:`kernel-modules`
* :ref:`mixer`

.. _`kernels available in Clear Linux`: https://clearlinux.org/documentation/clear-linux/reference/compatible-kernels
.. _`on GitHub`: https://github.com/clearlinux/distribution 
.. _`https://download.clearlinux.org/current/source/SRPMS/`: https://download.clearlinux.org/current/source/SRPMS/
.. _`mixer tool`: https://clearlinux.org/features/mixer-tool
.. _user-setup script: https://github.com/clearlinux/common/blob/master/user-setup.sh
.. _`Quilt`: http://savannah.nongnu.org/projects/quilt
.. _`clearlinux-pkgs GitHub`: https://github.com/clearlinux-pkgs?&q=linux
.. _`kernel.org`: https://www.kernel.org/
.. _`autospec`: https://clearlinux.org/documentation/clear-linux/concepts/autospec-about
.. _`git-format-patch Documentation`: https://git-scm.com/docs/git-format-patch
