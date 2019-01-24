.. _linux-kernel:

Linux Kernel Development Guide for |CL-ATTR|
############################################

This tutorial shows you how to run kernel development in |CL-ATTR| using |CL| tooling framework.

Prerequisites
*************

This guide requires that you:

* Have installed |CL| on a host machine or virtual environment. For detailed
  instructions on installing |CL|, visit the :ref:`get-started` section.

* :ref:`install-tooling`

.. _install-tooling:

Install the |CL| tooling framework
==================================

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

Modifying Linux Kernel Configurations
*************************************

Choose one of the following Linux kernel variants to start with:

* linux

* linux-kvm

* linux-hyperv

* linux-lts

Search for all kinds of Linux kernel variants supported by |CL| here: `Clear Linux Packages`_
This tutorial will continue with |CL| package with default Linux kernel named "linux".

Use this method to configure Linux kernel configurations without changing the package spec file.

#. Navigate to the |CL| tooling workspace.

   .. code-block:: bash

      cd ~/clearlinux

#. Use the command to clone the package:

   .. code-block:: bash

      make clone_<PACKAGE_NAME>
      make clone_linux

#. Navigate to the package workspace.

   .. code-block:: bash

      cd ~/packages/linux

#. Edit the kernel configuration file in the workspace.

   .. code-block:: bash

      vim config

#. Build the package into RPM.

   .. code-block:: bash

      make build

.. _Clear Linux Packages https://github.com/clearlinux-pkgs
