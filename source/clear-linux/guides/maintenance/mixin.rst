.. _mixin:

mixin
#####

mixin is a tool provided in the |CL-ATTR| that allows users to add custom
content to their client systems and still receive updates from their upstream OS
vendor.

.. contents::
   :local:
   :depth: 1

Description
***********

mixin uses the mixer tool to generate a local update for client systems. With
the mixin tool, a user can add remote RPM repositories or local RPMs and mix
them into their update stream, while continuing to get upstream bundles and
updates. The metadata generated from the mixin tool is merged with the upstream
metadata to provide a single source of update content, which swupd uses to
perform updates.

How to use
**********

Learn the mixin tool set up and workflow.

.. contents::
   :local:
   :depth: 1

Prerequisites
=============

#. **OS installed**

   The |CL| must be installed to use the mixer tool.

#. **Required bundles**

   The mixin tool requires that the :command:`mixer` bundle is installed.

Workflow
========

The following steps show how to create and add a custom bundle with the mixin
tool:

#. **Add or create a new repo(s)**

   mixin pulls packages to build your custom bundle from locations referred to
   as repos. There are two default repos for mixin:

   * upstream
   * local

   Additional repos can be added, such as other locations on your local system
   or remote repos.

   RPMs must be built specifically for |CL| in order for them to work properly.
   Refer to :ref:`autospec` for instruction on creating RPMs for |CL|.

#. **Create a custom bundle with desired RPMs**

   Add the desired packages to your new bundle and build the bundle. By default,
   the bundle will be named after its parent repo.

   The first time you build the bundle, mixer will create a new OS version by
   taking your current upstream |CL| version and multiplying it by 1000. For
   example, if your upstream version is 27650, your custom version will be
   27650000. For each subsequent call to mixin, mixer will increment the version
   by 10.

   View the `mixin man page`_ for more information on mixin commands.

#. **Update system to make custom bundle available**

   Update your system using swupd to make your custom bundle accessible.

   When you first create your mix, you will have to do a one-time migration to
   your custom mix as part of the update. After you migrate, the system version
   switches over to your last custom version number as noted in the previous
   step. As long as you remain on your custom version of |CL| you can continue
   to create and add new bundles to your mix with no extra migration step.

#. **Install custom bundles**

   Install your custom bundle using the normal swupd :command:`bundle-add`
   command.

   View the `swupd man page`_ for more information on swupd commands.

Examples
********

The following examples use:

* A stock installation of |CL| with all `Prerequisites`_.

Example 1: Add custom helloclear bundle
=======================================

This example shows the basic steps of adding a custom bundle from a local repo.

#. Check that :command:`helloclear` does not exist on your system:

   .. code-block:: bash

      helloclear

   .. code-block:: console

      helloclear: command not found

#. Follow the "Build a new RPM" example from :ref:`autospec` to create a new
   `helloclear` RPM.

   The resulting RPMs are in `~/clearlinux/packages/helloclear/rpms`.

#. Create a new repo.

   #. Create a local repo folder and copy the new `helloclear` RPM files into
      the repo:

      .. code-block:: bash

         mkdir ~/mixin-repo
         cp ~/clearlinux/packages/helloclear/rpms/helloclear-v1.0-1.x86_64.rpm ~/mixin-repo
         cp ~/clearlinux/packages/helloclear/rpms/helloclear-bin-v1.0-1.x86_64.rpm ~/mixin-repo

   #. Create the repo data:

      .. code-block:: bash

         cd ~/mixin-repo
         createrepo_c .

   #. Add the repo name:

      .. code-block:: bash

         sudo mixin repo add mylocalrepo file:///$HOME/mixin-repo/

#. Create custom bundle with the new `helloclear` RPM. Add `helloclear` to the
   :command:`helloclear-bundle` bundle and build the bundle:

   .. code-block:: bash

      sudo mixin package add helloclear --bundle helloclear-bundle
      sudo mixin build

#. Migrate your |CL| to your custom mix. Check your version before and after the
   update to see the switch to your custom mix:

   .. code-block:: bash

      sudo swupd check-update
      sudo swupd update --migrate
      sudo swupd check-update

#. Install your custom bundle. Check that the `helloclear-bundle` is now
   available and install it to your system:

   .. code-block:: bash

      sudo swupd bundle-list -a | grep helloclear-bundle
      sudo swupd bundle-add helloclear-bundle

#. Test for `helloclear` again to see that it is installed:

   .. code-block:: bash

      helloclear

#. Revert your system back to upstream (optional). This example reverts back to
   upstream version 27650:

   .. code-block:: console

      sudo swupd verify --fix --picky --force -m 27650 -C /usr/share/clear/update-ca/Swupd_Root.pem
      sudo swupd clean --all
      sudo swupd check-update

Related topics
**************

* :ref:`About mixer <mixer-about>`
* :ref:`mixer`
* :ref:`autospec-about`
* :ref:`bundles-about`
* :ref:`swupd-about`

.. _mixin man page: https://github.com/clearlinux/mixer-tools/blob/master/docs/mixin.1.rst
.. _swupd man page: https://github.com/clearlinux/swupd-client/blob/master/docs/swupd.1.rst
