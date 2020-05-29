.. _autospec:

autospec
########

**autospec** is a tool used to assist with the automated creation and
maintenance of RPM packaging in |CL-ATTR|. Where a standard
:abbr:`RPM (RPM Package Manager)` build process using :command:`rpmbuild`
requires a tarball and :file:`.spec` file to start, autospec requires only a
tarball and package name to start.

.. contents::
   :local:
   :depth: 1

Description
***********

The autospec tool attempts to infer the requirements of the :file:`.spec`
file by analyzing the source code and :file:`Makefile` information. It
continuously runs updated builds based on new information discovered from
build failures until it has a complete and valid :file:`.spec` file. If
needed, you can influence the behavior of autospec and customize the build by providing optional `control files`_ to the autospec tool.

autospec uses **mock** as a sandbox to run the builds. Visit the `mock wiki`_
for additional information on using mock.

For a general understanding of how an RPM works, visit
the `rpm website`_ or the `RPM Packaging Guide`_.

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/qrUpt1D1YAw" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="padding:10px; background-color: #fff;"></iframe>

How it works
************

Learn the autospec tool set up and process.

.. contents::
   :local:
   :depth: 1

Prerequisites
=============

The setup for building source in |CL| must be completed before using the
autospec tool.

Refer to `Setup environment to build source`_ for instructions on completing
the setup.

Create an RPM
=============

The basic autospec process is described in the following steps:

#. The :command:`make autospec` command generates a :file:`.spec` file based
   on the analysis of code and existing control files.

   Any control files should be located in the same directory as the resulting
   :file:`.spec` file. View the `autospec README`_ for more information on `control files`_.

#. autospec creates a build root with mock config.

#. autospec attempts to build an RPM from the generated :file:`.spec`.

#. autospec detects any missed declarations in the :file:`.spec`.

#. If build errors occur, autospec scans the build log to try to detect
   the root cause.

#. If autospec detects the root cause and knows how to continue, it restarts
   the build automatically at step 1 with updated build instructions.

#. Otherwise, autospec stops the build for user inspection to resolve the
   errors. Respond to the build process output by fixing source code issues
   and/or editing control files to resolve issues, which may include
   dependencies or exclusions. See `autospec README`_ for more information on
   control files.

   The user resumes the process at step 1 after errors are resolved.

   If a binary dependency doesn't exist in |CL|, you must build it
   before running autospec again.

Following these steps, autospec continues to rebuild the package, based on
new information discovered from build failures, until it has a valid
:file:`.spec`. If no build errors occur, RPM packages are successfully built.

Examples
********

Complete `Setup environment to build source`_ before using these examples.

.. contents::
   :local:
   :depth: 1

Example 1: Build RPM with an existing spec file
===============================================

This example shows how to build a RPM from a pre-packaged upstream package
with an existing spec file. The example uses the ``dmidecode`` package.

#. Navigate to the autospec workspace and clone the ``dmidecode`` package:

   .. code-block:: bash

      cd ~/clearlinux
      make clone_dmidecode

   .. note::

      You can clone all package repos at once using the following command:

      .. code-block:: bash

         make [-j NUM] clone-packages

      The optional NUM is the number of threads to use.

      For a list of available packages, view the
      :file:`~/clearlinux/projects/common/packages` file.

#. Navigate to the local copy of the ``dmidecode`` package and build it:

   .. code-block:: bash

      cd ~/clearlinux/packages/dmidecode/
      make build

#. The resulting RPMs are in :file:`./rpms`. Build logs and additional RPMs
   are in :file:`./results`.

Example 2: Build a new RPM
==========================

This example shows how to build a new RPM with no spec file. The example will
create a simple helloclear RPM.

#. Navigate to the autospec workspace and build the helloclear RPM. The
   :file:`Makefile` provides a :command:`make autospecnew` that can
   automatically generate an RPM package using the autospec tool. You must
   pass the URL to the source tarball and the NAME of the RPM you wish to
   create:

   .. code-block:: bash

      cd ~/clearlinux
      make autospecnew URL="https://github.com/clearlinux/helloclear/archive/helloclear-v1.0.tar.gz" NAME="helloclear"

   The resulting RPMs are in :file:`./packages/helloclear/rpms`. Build logs and additional RPMs are in :file:`./packages/helloclear/results`.

Example 3: Generate a new spec file with a pre-defined package
==============================================================

This example shows how to modify an existing package to create a custom RPM.
In this example you will make a simple change to the ``dmidecode`` package
and rebuild the package.

#. Navigate to the autospec workspace and clone the ``dmidecode`` package:

   .. code-block:: bash

      cd ~/clearlinux
      make clone_dmidecode

#. Navigate into the *dmidecode* directory:

   .. code-block:: bash

      cd packages/dmidecode

#. Open the :file:`excludes` file with an editor and add these lines:

   .. code-block:: console

      /usr/bin/biosdecode
      /usr/bin/ownership
      /usr/bin/vpddecode
      /usr/share/man/man8/biosdecode.8
      /usr/share/man/man8/ownership.8
      /usr/share/man/man8/vpddecode.8

   .. note::

      These files aren't needed by dmidecode, so we can remove them without
      any issues.

#. In the :file:`dmidecode` directory, build the modified ``dmidecode``
   package:

   .. code-block:: bash

      make autospec

#. The resulting RPMs are in :file:`./rpms`. Logs are in :file:`./results`.

Example 4: Provide control files to autospec
============================================

This example shows how to modify control files to correct build failures that
autospec is unable to resolve. In this example, you will add a missing
license and dependencies so autospec can complete a successful build.

#. Navigate to the autospec workspace:

   .. code-block:: bash

      cd ~/clearlinux

#. If you have not already, clone all upstream package repos:

   .. code-block:: bash

      make [-j NUM] clone-packages

   The optional NUM is the number of threads to use.

   .. note::

      In a later step of this example, we will search the cloned package
      repos for a missing dependency.

#. Build the opae-sdk RPM:

   .. code-block:: bash

      make autospecnew URL="https://github.com/OPAE/opae-sdk/archive/0.13.0.tar.gz" NAME="opae-sdk"

   This results in an error for a missing license file:

   .. code-block:: console

      [FATAL]    Cannot find any license or opae-sdk.license file!

#. Navigate to the package with build failures:

   .. code-block:: bash

      cd packages/opae-sdk

#. Add one or more valid license identifiers from the
   `SPDX License List <https://spdx.org/licenses/>`_.
   In the example below, two different licenses are appropriate based on the
   opae-sdk project licensing:

   .. code-block:: bash

      echo "BSD-3-Clause MIT" > opae-sdk.license

#. Run autospec again:

   .. code-block:: bash

      make autospec

   This results in a generic error:

   .. code-block:: console

      [FATAL]    Build failed, aborting

#. Open the build log to view the error details:

   .. code-block:: bash

      cat ./results/build.log

   The build log contains details for the specific failures. In this
   instance, there are missing dependencies:

   .. code-block:: console

      CMake Error: The following variables are used in this project, but
      they are set to NOTFOUND.  Please set them or make sure they are set and tested correctly in the CMake files:

      CJSON_LIBRARY
         linked by target "opae-c++-utils" in directory /builddir/build/BUILD/opae-sdk-0.13.0/tools/c++utilslib
      json-c_LIBRARIES
         linked by target "opae-c" in directory /builddir/build/BUILD/opae-sdk-0.13.0/libopae
      libuuid_LIBRARIES
         linked by target "opae-c" in directory /builddir/build/BUILD/opae-sdk-0.13.0/libopae

#. Search the spec files of upstream |CL| packages to see if the json-c
   library is available. In this case, it does exist and we'll add the json-c 'dev' package into the buildreq_add:

   .. code-block:: bash

      grep 'json-c\.so$' ~/clearlinux/packages/*/*.spec
      echo "json-c-dev" >> buildreq_add

   .. note::

      This search step works only if the user cloned all of the upstream package repos. In this example, upstream package repos were cloned in a previous step.

#. Search the spec files of upstream |CL| packages to see if the libuuid
   library is available. In this case, it exists in the util-linux package, so we'll add util-linux-dev package into the buildreq_add:

   .. code-block:: bash

      grep 'libuuid\.so$' ~/clearlinux/packages/*/*.spec
      echo "util-linux-dev" >> buildreq_add

#. Run autospec again and find the successfully-generated RPMs in the
   :file:`rpms` directory:

   .. code-block:: bash

      make autospec

   .. note::

      If you need a dependency that does not exist in the |CL| repo, you must first build it manually (see `Example 2: Build a new RPM`_), then add the repo so that autospec knows the package exists. For example:

   .. code-block:: bash

      cd ~/clearlinux/packages/<package-name>
      make repoadd
      make repostatus

   You only need to add the dependency to the :file:`buildreq_add` control
   file if autospec is not able to automatically find the correct dependency
   on its own.

.. TODO: Document how to set up a license server for use with autospec.
.. TODO: Demonstrate control file management. Establish specific use cases.

Example 5: Update an existing package
=====================================

The |CL| team prefers to carry no patches and seeks to make the latest
releases work. If we do need patches, we use :command:`autospec` to add,
remove, or manage patches. The :command:`autospec` control files are
integral to the patch management process. Developers can expect a more
streamlined approach to managing a large collection of packages with
:command:`autospec`.

Adding and submitting patches
-----------------------------

* To add patches to |CL| upstream, follow `patching source code`_.

* To submit a patch to upstream, follow
  `contributing to an existing software package`_.

If you maintain a downstream derivative of |CL| and you want to integrate
new or patched packages into your mix, follow the process in :ref:`mixer`.

Assuming you have followed the above process, :command:`autospec` has
generated a new spec file.

Refresh a package and inspect
-----------------------------

In this example, we use autospec to refresh the :command:`m4` package and
recreate RPM files.

#. Navigate to the top-level directory of the workspace

   .. code-block:: bash

      cd clearlinux

   - where :command:`clearlinux` is the top level of the tooling workspace

#. Run the make_clone command and then navigate to the package.

   .. code-block:: bash

      make clone_m4

      cd packages/m4

#. Make desired changes to the package, its control files, or
   other files.

#. Finally, run:

   .. code-block:: bash

      make autospec

#. To view spec file changes, run:

   .. code-block:: bash

      git show m4.spec

   The output shows:

   .. code-block:: console

      m4: Autospec creation for version 1.4.18

      diff --git a/m4.spec b/m4.spec
      index f76c78d..97b846a 100644
      --- a/m4.spec
      +++ b/m4.spec
      @@ -6,15 +6,14 @@
      #
      Name     : m4
      Version  : 1.4.18
      -Release  : 88
      +Release  : 89
      URL      : http://mirrors.kernel.org/gnu/m4/m4-1.4.18.tar.xz
      Source0  : http://mirrors.kernel.org/gnu/m4/m4-1.4.18.tar.xz
      -Source99 : http://mirrors.kernel.org/gnu/m4/m4-1.4.18.tar.xz.sig
      +Source1 : http://mirrors.kernel.org/gnu/m4/m4-1.4.18.tar.xz.sig
      Summary  : No detailed summary available
      Group    : Development/Tools
      ...

#. The following commands provide a more complete view of the changes.

   * :command:`git log -p`
   * :command:`gitk`

Test packaged software
**********************

After software has been packaged with autospec, the resulting RPMs can be
tested for functionality before being integrated and deployed into a |CL|
image with the :ref:`Mixer tool <mixer>`.

The |CL| development tooling offers two ways to quickly test autospec
generated RPMs.

.. note::
   The methods outlined below should only be used for temporary testing on
   development systems.


Test in a |CL| virtual machine
==============================

The |CL| development tooling includes a method to install RPMs into a |CL|
virtual machine running on the KVM hypervisor. Using a :abbr:`VM (Virtual
Machine)` allows testing in a completely isolated environment.

To test an autospec-created package inside a VM:

#. Download the |CL| KVM image into the :file:`~/clearlinux` directory as
   :file:`clear.img`. The location and name :file:`clear.img.xz` is important
   for the tooling to work:

   .. code-block:: bash

      cd ~/clearlinux
      curl -o clear.img.xz https://download.clearlinux.org/image/$(curl https://download.clearlinux.org/image/latest-images | grep '[0-9]'-kvm)

#. Extract the downloaded |CL| KVM image:

   .. code-block:: bash

      unxz -v clear.img.xz

#. Copy the QEMU start script and virtual firmware needed for KVM into the
   :file:`~/clearlinux` directory:

   .. code-block:: bash

      cp ~/clearlinux/projects/common/start_qemu.sh .
      cp /usr/share/qemu/OVMF.fd .

#. Run :command:`make install` from the package's autospec directory. The
   :command:`make install` command mounts the downloaded |CL| KVM image and
   installs the autospec-created RPM into it:

   .. code-block:: bash

      cd ~/clearlinux/packages/<package-name>
      make install

   The code that makes this possible can be viewed by searching for the
   *install:*  target in the `Makefile.common`_ file on GitHub.

#. Return to the :file:`~/clearlinux` directory and start the |CL| VM:

   .. code-block:: bash

      cd ~/clearlinux/
      sudo ./start_qemu.sh clear.img

#. A new |CL| VM will launch in the console. Log into the VM as *root* and set
   a new password for the VM.

#. Check that the software is installed in the |CL| VM as expected and perform
   any relevant tests.

#. After testing has been completed, the |CL| VM can be powered off and
   deleted:

   .. code-block:: bash

      poweroff
      rm clear.img


Test directly on a development machine
======================================

The |CL| development tooling also includes a method to extract
autospec-created RPMs locally onto a |CL| development system for testing.
Extracting an RPM directly onto a system  offers quicker testing; however
conflicts may occur and responsibility to remove the software after testing is
up to the developer.

To test an autospec created package directly on the |CL| development system:

#. Run :command:`make install-local` from the package's autospec directory.
   The :command:`make install-local` command extracts the RPM directly onto
   the filesystem of the running |CL| system:

   .. code-block:: bash

      cd ~/clearlinux/packages/<package-name>
      make install-local

   The code that makes this possible can be viewed by searching for the
   *install-local:*  target in the `Makefile.common`_  file on GitHub.

#. Check that the software is installed as expected and perform any relevant
   tests.

#. After testing has been completed, the software and any related files must
   be identified and deleted. The :command:`swupd repair --picky`
   command can help restore the state of the :file:`/usr` directory (see
   :ref:`swupd <swupd-guide>`) however any other files must be cleaned up
   manually.


References
**********

Reference the `autospec README`_ for details regarding `autospec` commands and options.

Setup environment to build source
=================================

.. _install-tooling-after-header:

Setup of the workspace and tooling used for building source in |CL| is mostly
automated for you with a setup script. It uses tools from the
:command:`os-clr-on-clr` bundle.

The setup script creates a workspace in the :file:`clearlinux` folder, with the
subfolders :file:`Makefile`, :file:`packages`, and :file:`projects`. The
:file:`projects` folder contains the main tools used for making packages in
|CL| :file:`autospec` and :file:`common`.

Follow these steps to setup the workspace and tooling for building source:

#. Install the :command:`os-clr-on-clr` bundle:

   .. code-block:: bash

        sudo swupd bundle-add os-clr-on-clr

#. Download the :file:`user-setup.sh` script:

   .. code-block:: bash

      curl -O https://raw.githubusercontent.com/clearlinux/common/master/user-setup.sh

#. Make :file:`user-setup.sh` executable:

   .. code-block:: bash

      chmod +x user-setup.sh

#. Run the script as an unprivileged user:

   .. code-block:: bash

      ./user-setup.sh

#. After the script completes, log out and log in again to complete the setup
   process.

#. Set your Git user email and username for the repos on your system:

   .. code-block:: bash

      git config --global user.email "you@example.com"
      git config --global user.name "Your Name"

   This global setting is used by |CL| tools that make use of Git.

.. _install-tooling-end:

Related topics
**************

* :ref:`Mixer tool <mixer>`
* :ref:`Proxy Configuration <proxy>`

.. _contributing to an existing software package: https://github.com/clearlinux/distribution/blob/master/contributing.md#contributing-to-an-existing-software-package

.. _patching source code: https://github.com/clearlinux/distribution/blob/master/contributing.md#patching-source-code

.. _`Makefile.common`: https://github.com/clearlinux/common/blob/master/Makefile.common
.. _autospec README: https://github.com/clearlinux/autospec
.. _control files: https://github.com/clearlinux/autospec#control-files
.. _mock wiki: https://github.com/rpm-software-management/mock/wiki
.. _rpm website: http://rpm.org
.. _RPM Packaging Guide: https://rpm-packaging-guide.github.io/


.. TODO:  Add link to how to submit a new package: https://github.com/clearlinux/distribution/blob/master/contributing.md#contributing-a-new-software-package
