.. _mixer_tool:

Mixer Tool
##########

*Mixing* refers to composing an operating system for very specific use cases.
While the default ClearLinux provides options to install bundles for various
server capabilities, some developers may wish to augment the operating system
itself with functionality from other distributions.


Current Workflow
================

Prerequisites
-------------

To start working with the Mixer tool, you'll need a recent Clear Linux* image,
and to have the following bundles installed. If you don't have them already,
you can add them with the :command:`swupd bundle-add` command::

# swupd bundle-add mixer-tools bundle-chroot-builder swupd-server

To satisfy all dependencies, you'll need the following additional bundles::

# swupd bundle-add os-clr-on-clr os-core-dev

Mixing
------

#. **Create a workspace**. Create an empty directory in your Clear image to
   use as a "workspace" for mixing. For these steps, assume that the workspace
   location is :file:`/home/clr/mix`.

#. **Configure builder.conf**. The :command:`bundle-chroot-builder` uses a specific
   configuration file, located in ``/usr/share/defaults/bundle-chroot-builder``. You
   must edit the :file:`builder.conf` in this directory to point to the correct path
   for ``BUNDLE_REPO``. Optionally, you may set a different ``YUM_CONF`` path to use
   if you do not wish to use the provided default. In this case, edit :file:`builder.conf`
   such that::

      BUNDLE_DIR = /home/clr/mix/.repos/clr-bundles/bundles
      YUM_DIR = /home/clr/mix/.yum-mix.conf

   reflects the path of the current workspace we are working in. The
   :file:`.yum-mix.conf` file will be auto-generated for you.

#. **Generate the starting point for your Mixer**. In your workspace, run::
   
     # ./mixer-init-mix.sh

   Currently, the only correct way to update an existing Clear image to a
   mixer-created update is to create an initial update that contains the same
   bundles and content as the VM. Then you can verify ``--fix`` the
   Clear image to it.  Lastly, update the Clear image as it normally would. 
   This step auto-generates that first version 10 for you, so you can focus
   on just your custom mix.

#. **Create/locate RPMs for mix.**. (Steps 3 and 4 are necessary only if you
   want to add your own RPMs to the Mix. If you are simply working with Clear
   only bundles, then skip to Step 5.)

   If you are creating RPMs from scratch, you may use :command:`autospec`,
   :command:`mock`, :command:`rpmbuild`, etc. to build them. If they are not
   built on Clear, make sure your configuration builds them correctly for Clear.

#. **Import RPMs into workspace**. The easiest way to do this is to create a
   ``results`` directory in your workspace *ala* ``/home/clr/mix/results``,
   and to copy the RPMs you want into that directory. The mixer script will
   look here for RPMs needed to build a local RPM repo for yum to use.

#. **Create a local RPM repo**. Create an empty directory in your workspace,
   and run::

   # mixer-add-rpms.sh --rpmdir results --repodir local

   After the script exits, you should see your RPMs and a repodata directory in
   ``/home/clr/mix/local``. If the RPMs are not all in the local directory, check
   to make sure that they are indeed valid files and not corrupt.

#. **Initialize Clear/mix version info**. In the workspace, run::

   # mixer-init-versions.sh -m 20

   This takes the Clear version from your image (or override with
   ``-c/--clear-version`` to use another Clear build's content), and use
   "20" for the mix version.

#. **Download**.  Download ``clr-bundles`` and other dependencies.  In the workspace,
   run::

   # mixer-update-bundles.sh

   This creates a ``.repos`` directory with git repos that are needed for
   later steps; it also creates a ``bundles/`` directory in your workspace,
   which contains the bundle definitions for the mix.

#. **Update bundle definitions**. The mixer uses a local clone of the
   ``clr-bundles`` repo to define bundles for the mix.

   To define your bundles:
      #. Navigate to the ``bundles/`` directory.
      #. Make any needed modifications to the bundle set.
      #. Commit the result::
         
         $ git add .
         $ git commit -s -m 'Update bundles for mix'

   Why do this? With git history, mixes are easy to revert to or refer
   to in the future if something were to go wrong with a new mix. If
   you're just testing this out, or really do not want to mess with git,
   you can ignore committing for now. The next feature will be to
   implement an interactive way to modify/add/delete bundles, so much of
   this work can be abstracted out and git work will be more automated.

   To add your own bundle, create a bundle definition file in ``bundles/``
   refer to :file:`os-core-update` for formatting), but be sure that the name
   does not conflict with another bundle. Add your package name(s) in that
   bundle definition file to tell it what packages must be installed as part
   of that bundle.

#. **Build**.  Build the bundle ``chroots``. To build all of the ``chroots``
   that are based on the bundles you defined, in your workspace run::
   
   # mixer-build-chroots.sh

   If you have many bundles defined for your mix, this step may take some time.

#. **Create update**. In the workspace, run::

   # mixer-create-update.sh

   When the script completes, you'll find your mix update content under
   ``/var/lib/update/www/VER`` (in this example, ``/var/lib/update/www/20``).
