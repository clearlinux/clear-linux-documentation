.. _autospec:

autospec
########

**autospec** is a tool to assist in the automated creation and maintenance of
RPM packaging in |CL-ATTR|. Where a standard RPM build process using
:command:`rpmbuild` requires a tarball and :file:`.spec` file to start, autospec
requires only a tarball and package name to start.

.. contents::
   :local:
   :depth: 1

Description
***********

The autospec tool attempts to infer the requirements of the :file:`.spec` file
by analyzing the source code and :file:`Makefile` information. It will
continuously run updated builds based on new information discovered from build
failures until it has a complete and valid :file:`.spec` file. If needed, you
can influence the behavior of autospec and customize the build by providing
optional `control files`_ to the autospec tool.

autospec uses mock as a sandbox to run the builds. Visit the `mock wiki`_ for
additional information on using mock.

For a general understanding of how RPMs work, visit the `rpm website`_ or the
`RPM Packaging Guide`_ .

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
setup.

Create an RPM
=============

The basic autospec process is described in the following steps:

#. The :command:`make autospec` command generates a :file:`.spec` file based on
   analysis of code and existing control files.

   Any control files should be located in the same directory as the resulting
   :file:`.spec` file.

   View the `autospec README`_ for more information on `control files`_.

#. autospec creates a build root with mock config.

#. autospec attempts to build an RPM from the generated :file:`.spec`.

#. autospec detects any missed declarations in the :file:`.spec`.

#. If build errors occur, autospec will scan the build log to try and detect
   the root cause.

#. If autospec detects the root cause and knows how to continue, it will restart
   the build automatically at step 1 with updated build instructions.

#. Otherwise, autospec will stop the build for user inspection to resolve the
   errors. Respond to the build process output by fixing source code issues
   and/or editing control files to resolve issues, which may include
   dependencies or exclusions. See `autospec README`_ for more information on
   control files.

   The user resumes the process at step 1 after errors are resolved.

   If a binary dependency doesn't exist in |CL|, you will need to build it
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

Example 1: Build RPM with existing spec file
============================================

This example shows how to build a RPM from a pre-packaged upstream package, with
an existing spec file. The example uses the ``dmidecode`` package.

#. Navigate to the autospec workspace and clone the ``dmidecode`` package:

   .. code-block:: bash

      cd ~/clearlinux
      make clone_dmidecode

   .. note::

      You can clone all package repos at once using:

      .. code-block:: bash

         make [-j NUM] clone-packages

      The optional NUM is the number of threads to use.

      For a list of available packages, view the
      :file:`~/clearlinux/projects/common/packages` file.

#. Navigate to the local copy of the ``dmidecode`` package and build it:

   .. code-block:: bash

      cd ~/clearlinux/packages/dmidecode/
      make build

#. The resulting RPMs are in :file:`./rpms`. Build logs and additional RPMs are
   in :file:`./results`.

Example 2: Build a new RPM
==========================

This example shows how to build a new RPM with no spec file. The example will
create a simple helloclear RPM.

#. Navigate to the autospec workspace and build the helloclear RPM. The
   :file:`Makefile` provides a :command:`make autospecnew` that can
   automatically generate an RPM package using the autospec tool. You must pass
   the URL to the source tarball and the NAME of the RPM you wish to create:

   .. code-block:: bash

      cd ~/clearlinux
      make autospecnew URL="https://github.com/clearlinux/helloclear/archive/helloclear-v1.0.tar.gz" NAME="helloclear"

   The resulting RPMs are in :file:`./packages/helloclear/rpms`. Builde logs and
   additional RPMs are in :file:`./packages/helloclear/results`.

Example 3: Generate a new spec file with a pre-defined package
==============================================================

This example shows how to modify an existing package to create a custom RPM. In
this example you will make a simple change to the ``dmidecode`` package and
rebuild the package.

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

#. In the :file:`dmidecode` directory, build the modified ``dmidecode`` package:

   .. code-block:: bash

      make autospec

#. The resulting RPMs are in :file:`./rpms`. Logs are in :file:`./results`.

Example 4: Provide control files to autospec
============================================

This example shows how to modify control files to correct build failures that
autospec is unable to resolve. In this example you will add a missing license
and dependencies in order for autospec to complete a successful build.

#. Navigate to the autospec workspace:

   .. code-block:: bash

      cd ~/clearlinux

#. If you have not already, clone all upstream package repos:

   .. code-block:: bash

      make [-j NUM] clone-packages

   The optional NUM is the number of threads to use.

   .. note::

      In a later step of this example, we will search the cloned package repos
      for a missing dependency.

#. Build the opae-sdk RPM:

   .. code-block:: bash

      make autospecnew URL="https://github.com/OPAE/opae-sdk/archive/0.13.0.tar.gz" NAME="opae-sdk"

   This will give an error for a missing license file:

   .. code-block:: console

      [FATAL]    Cannot find any license or opae-sdk.license file!

#. Navigate to the package with build failures:

   .. code-block:: bash

      cd packages/opae-sdk

#. Add a license:

   .. code-block:: bash

      echo "Intel Corporation" > opae-sdk.license

#. Run autospec again:

   .. code-block:: bash

      make autospec

   This will result in a generic error:

   .. code-block:: console

      [FATAL]    Build failed, aborting

#. Open the build log to view the error details:

   .. code-block:: bash

      cat ./results/build.log

   In the build log, you will find details for the specific failures. In this
   instance, there are missing dependencies:

   .. code-block:: console

      CMake Error: The following variables are used in this project, but they are set to NOTFOUND.  Please set them or make sure they are set and tested correctly in the CMake files:
      CJSON_LIBRARY
         linked by target "opae-c++-utils" in directory /builddir/build/BUILD/opae-sdk-0.13.0/tools/c++utilslib
      json-c_LIBRARIES
         linked by target "opae-c" in directory /builddir/build/BUILD/opae-sdk-0.13.0/libopae
      libuuid_LIBRARIES
         linked by target "opae-c" in directory /builddir/build/BUILD/opae-sdk-0.13.0/libopae

#. Search the spec files of upstream |CL| packages to see if the json-c library
   is availabe. In this case, it does exist and we'll add the json-c 'dev'
   package into the buildreq_add:

   .. code-block:: bash

      grep 'json-c\.so$' ~/clearlinux/packages/*/*.spec
      echo "json-c-dev" >> buildreq_add

   .. note::

      This search step works only if the user cloned all of the upstream package
      repos. In this example, upstream package repos were cloned in a previous
      step.

#. Search the spec files of upstream |CL| packages to see if the libuuid library
   is available. In this case, it exists in the util-linux package, so we'll add
   util-linux-dev package into the buildreq_add:

   .. code-block:: bash

      grep 'libuuid\.so$' ~/clearlinux/packages/*/*.spec
      echo "util-linux-dev" >> buildreq_add

#. Run autospec again and find the successfully-generated RPMs in the rpms
   directory:

   .. code-block:: bash

      make autospec

.. note::

   If you need a dependency that does not exist in the |CL| repo, you must first
   build it manually (see `Example 2: Build a new RPM`_), then add the repo so
   that autospec knows the package exists. For example:

   .. code-block:: bash

      cd ~/clearlinux/packages/<package-name>
      make repoadd
      make repostatus

   You only need to add the dependency to the :file:`buildreq_add` control file
   if autospec is not able to automatically find the correct dependency on its
   own.

References
**********

Reference the `autospec README`_ for details regarding autospec commands and
options.

Setup environment to build source
=================================

.. _install-tooling-after-header:

Setup of the workspace and tooling used for building source in |CL| is mostly
automated for you with a setup script. It uses tools from the
:command:`os-clr-on-clr` bundle.

The setup script creates a workspace in the :file:`clearlinux` folder, with the
subfolders :file:`Makefile`, :file:`packages`, and :file:`projects`. The
:file:`projects` folder contains the main tools used for making packages in
|CL|: `autospec` and `common`.

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
* :ref:`Mixin tool <mixin>`

.. _user-setup script: https://github.com/clearlinux/common/blob/master/user-setup.sh
.. _autospec README: https://github.com/clearlinux/autospec
.. _control files: https://github.com/clearlinux/autospec#control-files
.. _mock wiki: https://github.com/rpm-software-management/mock/wiki
.. _rpm website: http://rpm.org
.. _RPM Packaging Guide: https://rpm-packaging-guide.github.io/
