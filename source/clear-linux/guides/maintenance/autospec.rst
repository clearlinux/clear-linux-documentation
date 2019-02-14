.. _autospec:

autospec
########

autospec is a tool to assist in the automated creation and maintenance of RPM
packaging in |CL-ATTR|. Where a standard RPM build process using rpmbuild
requires a tarball and :file:`.spec` file to start, autospec requires only a
tarball and package name to start.

.. contents::
   :local:
   :depth: 1

.. Todo: this should be the concept content

.. This guide shows you how to create RPMs with :ref:`autospec <autospec-about>`, a tool that assists in automated creation and maintenance of RPM packaging on |CL-ATTR|.

.. See our :ref:`autospec concept page <autospec-about>` for a detailed explaination of how ``autospec`` works on |CL|. For a general understanding of how RPMs work, we recommend visiting the `rpm website`_ or the `RPM Packaging Guide`_ .

Description
***********

.. TODO

How to use autospec
*******************

Learn the autospec tool set up and workflow.

.. contents::
   :local:
   :depth: 1

Prerequisites
=============

#. **OS installed**

   The |CL| must be installed to use the autospec tool.

#. **Required bundles**

   The autospec tool requires that the :command:`os-clr-on-clr` bundle is
   installed.

Workflow
========

First time setup
----------------

Before you use autospec, you will need to set up the autospec environment and
tools. This is mostly automated for you by using the provided
:file:`user_setup.sh` script.

The `user-setup script`_ creates the autospec workspace in the
:file:`clearlinux` folder. The workspace contains the :file:`Makefile`, :file:`packages`, and :file:`projects` subfolders. The :file:`projects` folder contains
the main tools, `autospec` and `common`, used for making packages in |CL|.

Create a RPM
------------

autospec helps build RPMs following these basic steps:

#. Run autospec, passing in the tarball URL and package name.

#. If there are build failures or dependency issues, supply the necessary
   dependency, ban, or exclusion information via control files to autospec.

   View the `autospec README`_ for more information on control files.

   If a binary dependency doesn't exist in |CL|, you will need to build it
   before running autospec again.

#. Run autospec again.

#. Repeat steps 2-3 until all errors are resolved, resulting in a successful
   build.

Examples
********

Example 1: First time setup
===========================

This example shows the basic steps for first time setup of autospec.

#. Download the :file:`user-setup.sh` script.

   .. code-block:: bash

      curl -O https://raw.githubusercontent.com/clearlinux/common/master/user-setup.sh

#. Make :file:`user-setup.sh` executable.

   .. code-block:: bash

      chmod +x user-setup.sh

#. Run the script as an unprivileged user.

   .. code-block:: bash

      ./user-setup.sh

#. After the script completes, log out and log in again to complete the setup
   process.

#. Set your Git user email and username for the repos on your system

   .. code-block:: bash

      git config --global user.email "you@example.com"
      git config --global user.name "Your Name"

.. TODO this last step (for GIT) - required? what is it doing?

Example 2: Build RPM with existing spec file
============================================

This example shows how to build a RPM from a pre-packaged upstream package with
an existing spec file.

#. If you do not already have them locally, clone the |CL| package repos:

   .. code-block:: bash

      cd clearlinux
      make [-j NUM] clone-packages

   Alternately, you can clone a single package using:

   .. code-block:: bash

      make clone_<package-name>

#. Navigate to the ``dmidecode`` package and build it:

   .. code-block:: bash

      cd ~/clearlinux/packages/dmidecode/
      make build

#. The resulting RPMs are in :file:`./rpms`. Logs are in :file:`./results`.

.. _autospec-build-new-pack:

Example 3: Build a new package
==============================

This example shows how to build a new RPM with no spec file.

#. Navigate to the autospec workspace and build the helloclear RPM:

   .. code-block:: bash

      cd ~/clearlinux
      make autospecnew URL="https://github.com/clearlinux/helloclear/archive/helloclear-v1.0.tar.gz" NAME="helloclear"

#. The resulting RPMs are in :file:`~/clearlinux/packages/helloclear/rpms`.
   Logs are in :file:`~/clearlinux/packages/helloclear/results`.

#. If build failures or dependency issues occur, provide the necessary
   dependency, ban, or exclusion information via control files to autospec:

   #. Navigate to the specific package.

      .. code-block:: bash

         cd ~/clearlinux/packages/<package-name>

   #. Respond to the build process output by editing control files to resolve
      issues, which may include dependencies or exclusions. See
      `autospec README`_ for more information on control files.

   #. Run autospec again:

      .. code-block:: bash

         make autospec

   Repeat the last two steps above until all errors are resolved and you
   complete a successful build.


Example 4: Generate a new spec file with a pre-defined package
==============================================================

This example shows how to modify an existing package to create a custom RPM. In
this example you will make a simple change to the ``dmidecode`` package, change
the revision to a new number higher than the |CL| OS version, and rebuild the
package.

#. Navigate to the autospec workspace and copy the ``dmidecode`` package:

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

   When the process completes, you will see new RPM packages in the
   :file:`results/` folder.

#. View the new RPM packages in :file:`/clearlinux/packages/dmidecode/results/`

Next steps
**********

Create a custom bundle and use it with |CL|:

* Use the :ref:`Mixer tool <mixer>` to add a new bundle to your derivative of
  |CL|.
* Use the :ref:`Mixin tool <mixin>` to customize your upstream |CL| installation
  with a new bundle.

Related topics
**************

* :ref:`Mixer tool <mixer>`
* :ref:`Mixin tool <mixin>`
* :ref:`autospec <autospec-about>`
* :ref:`Bundles <bundles-about>`

.. _user-setup script: https://github.com/clearlinux/common/blob/master/user-setup.sh
.. _autospec README: https://github.com/clearlinux/autospec

.. _rpm website: http://rpm.org
.. _RPM Packaging Guide: https://rpm-packaging-guide.github.io/
