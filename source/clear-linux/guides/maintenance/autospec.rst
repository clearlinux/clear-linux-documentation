.. _autospec:

Build RPMs with autospec
########################

This guide shows you how to create RPMs with :ref:`autospec <autospec-about>`,
a tool that assists in automated creation and maintenance of RPM packaging
on |CL-ATTR|.

See our :ref:`autospec concept page <autospec-about>` for a detailed explaination
of how ``autospec`` works on |CL|. For a general understanding of how RPMs work,
we recommend visiting the `rpm website`_ or the `RPM Packaging Guide`_ .

Prerequisites
*************

This guide requires that you:

* Have installed |CL| on a host machine or virtual environment. For detailed
  instructions on installing |CL|, visit the :ref:`get-started` section.

* :ref:`install-tooling`

.. _install-tooling:

Install the |CL| development tooling framework
==============================================

.. _install-tooling-after-header:

#. Install the `os-clr-on-clr` developer bundle on your host system.

   .. code-block:: bash

      sudo swupd bundle-add os-clr-on-clr

#. Download the :file:`user-setup.sh` script.

   .. code-block:: bash

      curl -O https://raw.githubusercontent.com/clearlinux/common/master/user-setup.sh

#. Make :file:`user-setup.sh` executable.

   .. code-block:: bash

      chmod +x user-setup.sh

#. Run the script as an unprivileged user.

   .. code-block:: bash

      ./user-setup.sh

#. After the script completes, log out and log in again to complete
   the setup process.

   The `user-setup script`_ creates a folder called :file:`clearlinux`, which
   contains the :file:`Makefile`, :file:`packages`, and :file:`projects`
   subfolders.

   The :file:`projects` folder contains the main tools, `autospec`
   and `common`, used for making packages in |CL|.

.. _install-tooling-end:

Create a RPM with autospec
**************************

Choose one of the following options to build RPMs and manage source
code:

* :ref:`build-a-new-rpm` and spec file using ``make autospecnew``.

* :ref:`build-source-code-with-existing-spec-file` using ``make build``, without changing the
  spec file.

* :ref:`generate-a-new-spec-file` using ``make autospec``, based on changes in the control files.

.. _build-a-new-rpm:

Option 1: Build a new RPM
=========================

Use this method to build a new RPM with no spec file. In this example,
we build a new helloclear RPM.

#. Navigate to the autospec workspace.

   .. code-block:: bash

      cd ~/clearlinux

#. Enter the command:

   .. code-block:: bash

      make autospecnew URL="https://github.com/clearlinux/helloclear/archive/helloclear-v1.0.tar.gz"
      NAME="helloclear"

   .. note::

      For a local tarball, use this type of *URL*: \file://<absolute-path-to-tarball>

#. If build failures or dependency issues occur, continue below.
   Otherwise, skip directly to `Next steps`_.

   #. Navigate to the specific package.

      .. code-block:: bash

         cd ~/clearlinux/packages/[package-name]

   #. Respond to the build process output by editing control files to resolve
      issues, which may include dependencies or exclusions.
      See `autospec readme`_

   #. Run this command:

      .. code-block:: bash

         make autospec

   Repeat the last two steps above until all errors are resolved and you
   complete a successful build.

**Congratulations!**

You've successfully created a RPM.

Skip to `Next steps`_.

.. _build-source-code-with-existing-spec-file:

Option 2: Build source code with an existing spec file
======================================================

Use this method if you only want to build the RPM using the spec file. This
method assumes that a spec file already exists. In this example, we run a
``make build`` on the ``dmidecode`` package.

#. Navigate to the ``dmidecode`` package in clearlinux:

   .. code-block:: bash

      cd ~/clearlinux/packages/dmidecode/

#. To download the tarball and build, run the command:

   .. code-block:: bash

      make build

**Congratulations!**

You've successfully created a RPM.

Skip to `Next steps`_.

.. _generate-a-new-spec-file:

Option 3: Generate a new spec file with a pre-defined package
=============================================================

Use this method to modify an existing package. In this example, you will
modify an existing |CL| package called ``dmidecode`` to create a custom
RPM. You will make a simple change to this package, change the revision to
a new number that is higher than the |CL| OS version, and rebuild the package.

#. Navigate to clearlinux:

   .. code-block:: bash

      cd ~/clearlinux

#. Copy the ``dmidecode`` package.

   .. code-block:: bash

      make clone_dmidecode

#. Navigate into the *dmidecode* directory:

   .. code-block:: bash

      cd packages/dmidecode

#. With an editor, open the :file:`excludes` file and add these lines:

   .. code-block:: bash

      /usr/bin/biosdecode
      /usr/bin/ownership
      /usr/bin/vpddecode
      /usr/share/man/man8/biosdecode.8
      /usr/share/man/man8/ownership.8
      /usr/share/man/man8/vpddecode.8

   .. note::

      These files aren't needed by dmidecode, so we can remove them without
      any issues.

#. Save the file and exit.

#. At :file:`~/clearlinux/packages/dmidecode`, build the modified
   ``dmidecode`` package:

   .. code-block:: bash

      make autospec

   When the process completes, you will see new RPM packages in the
   :file:`results/` folder.

#. To view the new RPM packages, enter:

   .. code-block:: bash

      ls /clearlinux/packages/dmidecode/results/

**Congratulations!**

You've successfully created a RPM.

Next steps
**********

Now you can create a custom bundle with your new RPM and use it with |CL|:

* Use the :ref:`Mixer tool <mixer>` to add a new bundle to your derivative of |CL|.
* Use the :ref:`Mixin tool <mixin>` to customize your upstream |CL| installation with a new bundle.

Related topics
**************

* :ref:`Mixer tool <mixer>`
* :ref:`Mixin tool <mixin>`
* :ref:`autospec <autospec-about>`
* :ref:`Bundles <bundles-about>`


.. _rpm website: http://rpm.org

.. _RPM Packaging Guide: https://rpm-packaging-guide.github.io/

.. _user-setup script: https://github.com/clearlinux/common/blob/master/user-setup.sh

.. _autospec readme: https://github.com/clearlinux/autospec
