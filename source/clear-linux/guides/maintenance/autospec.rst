.. _autospec:

Build RPMs with autospec
########################

This guide shows you how to create RPMs with :ref:`autospec <autospec-about>`
, a tool that assists in automated creation and maintenance of RPM packaging 
on |CLOSIA|.  Additionally, you learn how to use these RPMs to create bundles
with :ref:`mixer <mixer>`. 

Prerequisites
*************
This guide assumes that you have:

* Created :ref:`a custom mix <mixer>` of |CL| and deployed it to a
  to a target device

* |CL| running on a host machine or virtual environment
  
  .. note:: 

     To install |CL|, see: 

     * :ref:`bare-metal-install`
     * :ref:`virtual-machine-install`
   
Install Clear Linux tooling framework
=====================================

Our GitHub\* repository provides you with the resources you need
to create and maintain packages.

#. On your host system, install this developer bundle. 
   
   .. code-block:: bash

      sudo swupd bundle-add os-clr-on-clr

#. Run this command to download the :file:`user-setup.sh` script.

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

Create a RPM with autospec
**************************

.. include:: ../../concepts/autospec-about.rst
   :start-after: incl-autospec-overview:
   :end-before: incl-autospec-overview-end:
 
For a detailed explanation of how ``autospec`` works on |CL|, visit our 
:ref:`autospec-about` about page.  For a general understanding of how RPMs 
work, we recommend visiting the `rpm website`_ or the 
`RPM Packaging Guide`_ . 

Building RPMs 
=============

Choose one of the following options to build RPMs and manage source
code: 

* :ref:`build-a-new-rpm` and spec file using ``make autospecnew``. 

* :ref:`build-source-code-with-existing-spec-file` (without changing the
  spec file) using ``make build``.  

* :ref:`generate-a-new-spec-file` based on changes in the control files with
  ``make autospec``. 

.. _build-a-new-rpm:

Build a new RPM
===============

#. Navigate to the autospec workspace.

   .. code-block:: bash

      cd ~/clearlinux

#. Enter the command: 

   .. code-block:: bash

      make autospecnew URL="https://github.com/clearlinux/helloclear/archive/helloclear-v1.0.tar.gz" 
      NAME="helloclear"

   .. note:: 

      For a local tarball, use for the *URL*: 
      file://<absolute-path-to-tarball>
   
#. If build failures or dependency issues occur, continue below.
   Otherwise, skip directly to `copy-rpm-packages-to-mixer`_.    
   
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

   Skip to `copy-rpm-packages-to-mixer`_ to add the new RPM to your mix.

.. _build-source-code-with-existing-spec-file:

Build source code with an existing spec file 
============================================

If you only want to build the RPM using the spec file, use this method. This 
method assumes that a spec file already exists. In this example, we run a 
``make build`` on the ``dmidecode`` package. 

#. Navigate to the ``dmidecode`` package in clearlinux:  

   .. code-block:: bash

      cd ~/clearlinux/packages/dmidecode/   

#. To download the tarball and build, run the command: 

   .. code-block:: bash 

      make build

   Skip to `copy-rpm-packages-to-mixer`_ to add the new RPM to your mix.

.. _generate-a-new-spec-file:

Generate a new spec file with a pre-defined package
===================================================

In this method, you will modify an existing |CL| package called ``dmidecode``
to create a custom RPM. You will make a simple change to this package, 
change the revision to a new number that is higher than the |CL| OS version, 
and rebuild the package.

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

Add a custom RPM to a mix and deploy to target
**********************************************

We need a RPM repository to store our custom RPMs. This repository also 
includes some metadata that allows programs such as ``yum`` and ``dnf`` to 
follow and include any specified dependencies. This architecture enables us
to test custom RPMs before we integrate them in a mix. 

.. note:: 

   Assure that you followed the :ref:`mixer` instruction and created
   a location for **local RPM packages** using the *--local-rpms* flag
   with the command: :command:`mixer init --local-rpms`. If you skipped 
   this step, return and complete it in :ref:`mixer` before proceeding.  

.. _copy-rpm-packages-to-mixer:

Copy RPM packages to mixer and build bundle
============================================

Transfer the newly generated RPM packages to the ``mixer`` folder so
that it can include them as needed. 

.. note:: 

   This guide assumes that you have a web server that hosts ``swupd`` update 
   content. 

#. Change directory into the mix workspace: 

   .. code-block:: bash

      cd ~/mix

#. Copy the contents from the results folder in the RPM packages to the 
   :file:`local-rpms` folder in the :file:`mix` folder: 

   .. code-block:: bash

      cp ~/clearlinux/packages/dmidecode/results/*x86_64*rpm ~/mix/local-rpms/

#. Remove the debuginfo: 
   
   .. code-block:: bash

      rm ~/mix/local-rpms/*debuginfo*x86_64*

#. Generate the yum repo: 

   .. code-block:: bash

      sudo mixer add-rpms

#. Create a local bundle definition file to include the newly generated RPM 
   package in your mix. In our example, the ``[bundle-name]`` is 
   either ``dmidecode`` or  ``helloclear``. 

   .. code-block:: bash

      mixer bundle edit [bundle-name]

#. Then add the new bundle to the mix.
       
   .. code-block:: bash 
  
      mixer bundle add [bundle-name]

#. Build the bundle and update content.

   .. code-block:: bash

      sudo mixer build all
  
#. Log into the target device.     
  
#. On the target device, update and install the new bundle.

   .. code-block:: bash

      sudo swupd update

      sudo swupd bundle-add [bundle-name]
            
**Congratulations!**

You successfully built a RPM and created a mix with it. 

.. _rpm website: http://rpm.org

.. _RPM Packaging Guide: https://rpm-packaging-guide.github.io/

.. _user-setup script: https://github.com/clearlinux/common/blob/master/user-setup.sh

.. _autospec readme: https://github.com/clearlinux/autospec
