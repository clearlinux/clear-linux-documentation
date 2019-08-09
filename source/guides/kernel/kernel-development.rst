.. _kernel-development:

Kernel development
##################

This guide shows how to obtain and compile a Linux\* kernel source using
|CL-ATTR| development tooling.

.. contents::
   :local:
   :depth: 1
   :backlinks: top

Overview
********

The :ref:`compatible-kernels` available in |CL| aim to be performant and
practical. In some cases, it may be necessary to modify the kernel to suit
your specific needs or test new kernel code as a developer.

`Source RPMs (SRPMS)`_ are also available for all |CL| kernels, and can be
used for development instead.

Request changes be included with the |CL| kernel
************************************************

If the kernel modification you need is already open source and likely to be
useful to others, consider submitting a request to include it in the
|CL| kernels. If your change request is accepted, you do not need to maintain
your own modified kernel.

Make enhancement requests to the |CL| `Distribution Project`_ on GitHub\*.

Set up kernel development environment
*************************************

In some cases, it may be necessary to modify the kernel to suit your specific
needs or to test new kernel code.

You can build and install a custom kernel; however you must:

* Disable Secure Boot
* Maintain any updates to the kernel going forward

To create a custom kernel, start with the |CL| development environment.
Then make changes to the kernel, build it, and install it.


Install the |CL| development tooling framework
==============================================

.. include:: ../clear/autospec.rst
   :start-after: install-tooling-after-header:
   :end-before: install-tooling-end:

Clone the kernel package
========================

Clone the existing kernel package repository from |CL| as a starting point.

#. Clone the Linux kernel package from |CL|. Using the
   :command:`make clone_<PACKAGENAME>` command in the
   :file:`clearlinux/` directory clones the package from the
   `clearlinux-pkgs`_ repo on GitHub.

   .. code-block:: bash

      cd ~/clearlinux
      make clone_linux

#. Navigate into the cloned package directory.

   .. code-block:: bash

      cd ~/clearlinux/packages/linux


The "linux" package is the kernel that comes with |CL| in the
:command:`kernel-native` bundle. Alternatively, you can use a different kernel
variant as the base for modification. For a list of kernel package names which
you can clone instead, see the `clearlinux-pkgs`_ repo on GitHub.

.. note::

   The latest version of the |CL| kernel package is pulled as a starting
   point. An older version can pulled by switching to different git tag by using
   :command:`git checkout tag/<TAG_NAME>`.

Change the kernel version
=========================

|CL| tends to use the latest kernel available from `kernel.org`_, the Linux
upstream. The kernel version that will be built can be changed in the
RPM SPEC file. While most packages in Clear Linux are typically packaged
using :ref:`autospec`, the kernel is not. This means control files
provided by autospec are not available and changes must be made manually.

#. Open the Linux kernel package RPM SPEC file in an editor.

   .. code-block:: bash

      $EDITOR linux.spec

#. Modify the Version, Release, and Source0 URL entries at the top of the
   file to change the version of Linux kernel that will be compiled.

   A list of current and available kernel release can be found on
   `kernel.org`_.

   .. code-block:: spec
      :linenos:
      :emphasize-lines: 1-3,12

      Name:           linux
      Version:        4.20.8
      Release:        696
      License:        GPL-2.0
      Summary:        The Linux kernel
      Url:            http://www.kernel.org/
      Group:          kernel
      Source0:        https://cdn.kernel.org/pub/linux/kernel/v4.x/linux-4.20.8.tar.xz
      Source1:        config
      Source2:        cmdline

      %define ktarget  native

   .. note::
      - Consider changing the Name from *linux* in the RPM spec file to easily
        identify a modified kernel.

      - Consider changing the ktarget from *native* in the RPM spec file to
        easily identify a modified kernel.

#. Commit and save the changes to the file.

.. _pull-copy-kernel-source:

Pull a copy of the Linux kernel source code
===========================================

Obtain a local copy of the source code to make modifications against.

#. Run make sources to pull the kernel source code specified in the RPM
   SPEC file. In the example, it downloads the :file:`linux-4.20.8.tar.xz`
   file.

   .. code-block:: bash

      make sources


#. Extract the kernel source code archive. This will create a working copy
   of the Linux source that you can modify.

   .. code-block:: bash

      tar -xvf linux-4.20.8.tar.xz

#. Navigate to the extracted directory. In this example, it has been
   extracted into a :file:`linux-4.20.8` directory.

   .. code-block:: bash

      cd linux-4.20.8/


Customize the Linux kernel source
*********************************

After the kernel sources have been obtained, customizations to the kernel
configuration or source code can be made for inclusion with the kernel
build. These customizations are optional.

Modify kernel configuration
===========================

The kernel source has many configuration options available to pick support for
different hardware and software features.

These configuration values must be provided in the :file:`.config` file at
compile time. You will need to make modifications to the :file:`.config`
file, and include it in the kernel package.


#. Make sure you have followed the steps to :ref:`pull-copy-kernel-source`
   and are in the kernel source working directory.


#. If you have an existing :file:`.config` file from an old kernel, copy it
   into the working directory as :file:`.config` for comparison.
   Otherwise, use the |CL| kernel configuration file as template

   .. code-block:: bash

      cp ~/clearlinux/packages/linux/config .config


#. Make any desired changes to the :file:`.config` using a kernel
   configuration tool. Below are some popular options:

   - :command:`$EDITOR .config` - the .config file can be directly edited
     for simple changes with names that are already known.

   - :command:`make config` - a text-based tool that asks questions
     one-by-one to decide configuration options.

   - :command:`make menuconfig` - a terminal user interface that provides
     menus to decide configuration options.

   - :command:`make xconfig` - a graphical user interface that provides
     tree views to decide configuration options.


   More configuration tools can be found by looking at the make help:
   :command:`make help | grep config`

#. Commit and save the changes to the :file:`.config` file.

#. Copy the :file:`.config` file from the kernel source directory into
   the kernel package directory as :file:`config` for inclusion in the build.

   .. code-block:: bash

      cp .config ../config

Modify kernel source code
=========================

Changes to kernel code are applied with patch files. Patch files are
formatted git commits that can be applied to the main source code.

You will need to obtain a copy of the source code,
make modifications, generate patch file(s), and add them to the RPM SPEC
file for inclusion during the kernel build.

If you have a large number of patches or a more complex workflow,
consider using a patch management tool in addition to Git such as
`Quilt`_.


#. Make sure you have followed the steps to :ref:`pull-copy-kernel-source` and
   are in the kernel source working directory.


#. Initialize the kernel source directory as a new git repo and create a
   commit with all the existing source files to begin tracking changes.

   .. code-block:: bash

      git init
      git add -A
      git commit -m "Initial commit of Linux kernel source"


#. Apply patches provided by the |CL| kernel package to the kernel source
   in the working directory.

   .. code-block:: bash

      git am ../*.patch


#. Make any of your desired code changes to the Linux source code files.


#. Track and commit your changes to the local git repo.

   .. code-block:: bash

      git add <FILENAME>
      git commit -m "My patch for driver A" <FILENAME>


#. Generate a patch file based on your git commits.
   <n> represents the number of local commits to create patch file.
   See the `git-format-patch`_ documentation for detailed information
   on using :command:`git format-patch`

   .. code-block:: bash

      git format-patch -<n>

#. Copy the patch files from the patches directory in the linux
   source tree to the RPM build directory.

   .. code-block:: bash

      cp *.patch ~/clearlinux/packages/linux/


#. Navigate back to the RPM build directory.

   .. code-block:: bash

      cd ~/clearlinux/packages/linux/

#. Open the Linux kernel package RPM SPEC file in an editor.

   .. code-block:: bash

      $EDITOR linux.spec

#. Locate the section of the SPEC file that contains existing patch
   variable definitions and append your patch file name. Ensure the
   patch number does not collide with an existing patch.
   In this example, the patch file is called
   :file:`2001-my-patch-for-driver-A.patch`

   .. code-block:: spec
      :linenos:
      :emphasize-lines: 13 

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
   In this example, patch2001 is added.

   .. code-block:: spec
      :linenos:
      :emphasize-lines: 11   

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

Modify kernel boot parameters
=============================
The kernel boot options are passed from the bootloader to the kernel with
command-line parameters.

While temporary changes can be made to kernel parameters on a running
system or on a during boot, you can also modify the default parameters that
are persistent and distributed with a customized kernel.


#. Open the kernel :file:`cmdline` file in an editor.

   .. code-block:: bash

      $EDITOR cmdline


#. Make any desired change to the kernel parameters.
   For example, you can remove the :command:`quiet` parameter to see more
   verbose output of kernel log messages during the boot process.

#. Commit and save the changes to the :file:`cmdline` file.

See the `kernel parameters`_  documentation for a list of available
parameters.

Build and install the kernel
****************************
After changes have been made to the kernel source and RPM SPEC file,
the kernel is ready to be compiled and packaged into an RPM.

The |CL| development tooling makes use of :command:`mock` environments to
isolate building of packages in a sanitized workspace.

#. Start the compilation process by issuing the :command:`make build`
   command. This process is typically resource intensive and will take a
   while.

   .. code-block:: bash

      make build

   .. note::
      The mock plugin `ccache`_ can be enabled to help speed up any future
      rebuilds of the kernel package by caching compiler outputs and reusing
      them.


#. The result will be multiple :file:`.rpm` files in the :file:`rpms`
   directory as output.

   .. code-block:: bash

      ls rpms/

   The kernel RPM will be named
   :file:`linux<NAME>-<VERSION>-<RELEASE>.x86_64.rpm`


#. The kernel RPM file can be input to the :ref:`mixer` to create a
   custom bundle and mix of |CL|.

Alternatively, the kernel RPM bundle can be installed manually on a local
machine for testing. This approach works well for individual development or
testing. For a more scalable and customizable approach, consider using the
:ref:`mixer` to provide a custom kernel with updates.

#. Install the kernel onto the local system by extracting the RPM with the
   :command:`rpm2cpio` command.

   .. code-block:: bash

      rpm2cpio linux<NAME>-<VERSION>-<RELEASE>.x86_64.rpm | (cd /; sudo cpio -i -d -u -v);


#. Update the |CL| boot manager using :command:`clr-boot-manager` and reboot.

   .. code-block:: bash

      sudo clr-boot-manager list-kernels
      sudo clr-boot-manager set-kernel org.clearlinux.<TARGET>.<VERSION>-<RELEASE>

      sudo reboot


#. After a reboot, verify the customized kernel is running.

   .. code-block:: bash

      uname -a

Related topics
**************

* :ref:`kernel-modules`
* :ref:`mixer`

.. _Distribution Project: https://github.com/clearlinux/distribution/issues/new/choose

.. _Source RPMs (SRPMS): https://cdn.download.clearlinux.org/current/source/SRPMS/

.. _Quilt: http://savannah.nongnu.org/projects/quilt

.. _clearlinux-pkgs: https://github.com/clearlinux-pkgs

.. _kernel.org: https://www.kernel.org/

.. _kernel parameters: https://www.kernel.org/doc/Documentation/admin-guide/kernel-parameters.txt

.. _ccache: https://fedoraproject.org/wiki/Mock/Plugin/CCache?rd=Subprojects/Mock/Plugin/CCache

.. _git-format-patch: https://git-scm.com/docs/git-format-patch
