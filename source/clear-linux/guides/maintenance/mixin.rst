.. _mixin:

Mixin tool
##########

The mixin tool, a light wrapper for :ref:`mixer`, is used to customize your
installation of |CL-ATTR| by *side loading* a custom bundle. This is known
as a *mixin*. Creating a mixin is useful when you need to add custom or 3rd
party content but want to keep on the upstream update cycle. This guide covers
the workflow of creating your own mixin using the mixin tool.

If you need to customize beyond what the mixin tool provides, use the
:ref:`mixer tool<mixer>`.

Prerequisites
*************

To start working with the mixin tool, you will need a recent image of |CL| with
the `mixer` bundle installed. Before you install any new packages, update your
OS with the following command:

.. code-block:: bash

   sudo swupd update

If the bundle is not yet installed, you can add it with the :command:`swupd bundle-add`
command as follows:

.. code-block:: bash

   sudo swupd bundle-add mixer

Mixin workflow
**************

The workflow to create your own mixin is outlined below.

#. :ref:`create-workspace-mixin`
#. :ref:`create-rpm`
#. :ref:`copy-custom-rpm`
#. :ref:`create-bundle`
#. :ref:`migrate-mix`
#. :ref:`add-bundle-to-system`
#. :ref:`revert-to-upstream`

.. _create-workspace-mixin:

Create a workspace
******************

Use the following command to create an empty directory in your |CL| image to
use as a workspace for mixing:

.. code-block:: bash

   sudo mkdir -p /usr/share/mix/local-rpms

.. _create-rpm:

Create RPMs for mixin
***********************

Create a RPM for your mixin, using your content or 3rd party content.
Alternatively, you can use a remote RPM repository. In both cases, ensure
the RPM is built for |CL|.

.. include:: ../../guides/maintenance/mixer.rst
   :Start-after: incl-create-rpm:
   :end-before: incl-create-rpm-end:

.. _copy-custom-rpm:

Copy RPMs to workspace
**********************

If the RPM you want to add to your mix is local, copy the local
RPM package to the workspace:

.. code-block:: bash

   sudo cp [RPM] /usr/share/mix/local-rpms

If you are using a remote RPM repository, use the following
command:

.. code-block:: bash

   sudo mixin repo add [repo-name] [repo-url]

.. _create-bundle:

Create a bundle with your RPM
*****************************

Create a bundle using your custom RPM with the following steps:

#. Use the :command:`mixin package add` command to create a bundle with the RPM
   package:

   .. code-block:: bash

      sudo mixin package add [package-name] [--bundle bundle-name] [--build]

   This command will add package-name to a bundle that is named after its parent
   repository. For example, if the RPM was provided locally, it will be added to
   the 'local' bundle. If it came from a repo that was added with
   :command:`mixin repo add`, it will be added to a bundle named after the
   repo-name.

   If the `--bundle bundle-name` flag is provided, the package will
   be added to `bundle-name` instead.

   The `--build` flag tells :command:`mixin` to run a `mixer` build after adding
   the package.

#. To add more than one RPM to your previously created bundle, repeat
   the :command:`mixin package add` command and change the package name. Do not
   add the `--build` flag until all packages have been added.

#. Once done adding packages, run the following command to create your local mix:

   .. code-block:: bash

      sudo mixin build

   .. note::

      The first time you run the :command:`mixin build` command, mixer
      creates a new OS version by taking your current upstream |CL| version
      and multiplying it by 1000.  For example, if your upstream version is
      21530, your custom version will be 21530000.  For each subsequent call
      to mixin, mixer will increment the version by 10.  For example,
      21530010, 21530020, etc.

.. _migrate-mix:

Migrate to your custom mix
**************************

Before you can use your custom bundle, you must migrate your |CL| system
to your custom mix to make the bundle accessible:

.. code-block:: bash

   sudo swupd update --migrate

After you migrate, the version of your system will be your last custom
version number as noted in the previous section.

You can continue to create new bundles with :command:`mixin` while you are in
your custom version of |CL|.  You do not need to migrate again. However each
time you create new bundles with mixin, you must run :command:`swupd update`
to make the new bundles visible.

.. _add-bundle-to-system:

Add custom bundle to your system
********************************

Add your custom bundle to your system with the following steps:

#. Get a listing of your newly-created bundle:

   .. code-block:: bash

      sudo swupd bundle-list -a

   The listing includes all upstream bundles.

#. Add your bundle:

   .. code-block:: bash

      sudo swupd bundle-add [bundle-name]

.. note::

   You can also update your system to the latest upstream version using
   this command:

   .. code-block:: bash

      sudo swupd update

.. _revert-to-upstream:

Optional: Revert system back to 100% upstream
*********************************************

You can revert your |CL| system back to the official upstream version
with the following command:

.. code-block:: bash

   sudo swupd verify --fix --force --picky -m [upstream-version-number] -C /usr/share/clear/update-ca/Swupd_Root.pem

After the command completes, all custom RPMs and bundles are unavailable
because :file:`/usr/share/mix` is deleted as part of the reversion process.

Related topics
**************

* :ref:`About mixer <mixer-about>`
* :ref:`mixer`
* :ref:`autospec-about`
* :ref:`bundles-about`

.. _Developer tooling framework for Clear Linux:
   https://github.com/clearlinux/common