.. _mixin:

Create and add custom bundles to your upstream Clear Linux system
#################################################################

|CLOSIA| offers many curated bundles that you can install on your system to
create your desired capabilities. If the available upstream bundles do not
meet your needs, you can create and add your own custom bundles to your
system using one of two methods. Note: Upstream refers to the official
version of |CL|.

The first method is to use the :ref:`mixer tool<mixer>` to create your own
|CL| image and add your bundles to it.  Mixing your own |CL| image can
give you great control and flexibility; however, you must act as an
:abbr:`OSV (Operating System Vendor)` and maintain your releases and
updates because you have forked from upstream.

The second method is to use the :command:`mixin` tool, which also
makes use of mixer to create custom bundles that you can add to your
upstream |CL| system.  This  simpler method provides a “light” forking from
upstream, which means you can continue to get upstream bundles and updates.
If needed, you can easily revert your system back to the upstream version.

This guide shows you how to accomplish the second method by following these
steps:

#. Set up the workspace.
#. Copy your custom RPM package to the workspace.
#. Create a bundle with your custom RPM package.
#. Migrate your |CL| system to your custom mix.
#. Add your custom bundle to your system.
#. Optional: Revert your system back to 100% upstream.

Set up the workspace
********************

#. Install the mixer bundle to enable mixer.

   .. code-block:: console

      $ sudo swupd bundle-add mixer

#. Create the workspace.

   .. code-block:: console

      $ sudo mkdir -p /usr/share/mix/local-rpms

Copy your custom RPM package to the workspace
*********************************************

.. note::

   You cannot simply use RPMs from other Linux distros on |CL|. You must
   build RPMs specifically for |CL| in order for them to work properly.
   Follow the instructions on how to build RPMs found at the
   `Developer tooling framework for Clear Linux`_.  

If you have a local RPM you want to add to your mix you can do so by copying
your RPM package to the workspace.

.. code-block:: console

   $ sudo cp [RPM] /usr/share/mix/local-rpms

Alternatively, you can add a remote RPM repository by running the following
command.

.. code-block:: console

   $ sudo mixin repo add [repo-name] [repo-url]

Create a bundle with your custom RPM package
********************************************

Use the :command:`mixin` command to create a bundle with the RPM
package.

.. code-block:: console

   $ sudo mixin package add [package-name] [--build]

This command will add package-name to a bundle that is named after its parent
repository. For example, if the RPM was provided locally, it will be added to
the 'local' bundle. If it came from a repo that was added with :command:`mixin
repo add` it will be added to a bundle named after the repo-name. The `--build`
flag tells :command:`mixin` to run a `mixer` build after adding the package.

To add more than one RPM to your previously-created bundle, repeat
the :command:`mixin package add` command and change the package name. Do not add
the `--build` flag until all packages have been added. Once done adding packages
run the following to create your local mix.

.. code-block:: console

   $ sudo mixin build

.. note::

   * The first time you run the :command:`mixin build` command, mixer
     creates a new OS version by taking your current upstream |CL| version
     and multiplying it by 1000.  For example, if your upstream version is
     21530, your custom version will be 21530000.  For each subsequent call
     to mixin, mixer will increment the version by 10.  For example,
     21530010, 21530020, etc. 

Migrate your Clear Linux system to your custom mix
**************************************************

Before you can use your custom bundle, you must migrate your |CL| system
to your custom mix to make the bundle accessible.

.. code-block:: console

   $ sudo swupd update --migrate

After you migrate, the version of your |CL| system switches over to your
last custom version number as noted in the previous section. 

You can continue to create new bundles with :command:`mixin` 
while you are in your custom version of |CL|.  You do not need to migrate
again. However, you must run :command:`swupd update` again to update your
system in order to make those bundles visible. 

Add your custom bundle to your system
*************************************

#. Get a listing of your newly-created bundle.

   .. code-block:: console

      $ sudo swupd bundle-list -a

   The listing includes all upstream bundles.

#. Add your bundle.

   .. code-block:: console

      $ sudo swupd bundle-add [bundle-name]

.. note:: 

   You can also update your system to the latest upstream version using
   this command:   
   
   .. code-block:: console

      $ sudo swupd update

Optional: Revert your system back to 100% upstream
**************************************************

If you want to revert your |CL| system back to the official upstream
version, use this command:

.. code-block:: console
   
   $ sudo swupd verify --fix --force --picky -m [upstream-version-number] -C /usr/share/clear/update-ca/Swupd_Root.pem

After the command completes, all custom RPMs and bundles are unavailable
because :file:`/usr/share/mix` is deleted as part of the reversion process.  

.. _Developer tooling framework for Clear Linux:
   https://github.com/clearlinux/common
