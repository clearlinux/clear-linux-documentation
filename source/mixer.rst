.. _mixer_tool:

Mixer Tool
##########

*Mixing* refers to composing an operating system for specific use cases.
While the default Clear Linux* OS for Intel® Architecture provides options to install 
bundles for various server capabilities, some developers may wish to 1) augment the 
operating system itself with functionality from their own packages or 2) modify the 
structure of current bundles to cater to their particular needs.


Current Workflow
================

Prerequisites
-------------

To start working with the Mixer tools, you'll need a recent image of Clear Linux OS for Intel Architecture
with the following bundles installed. If you don't have them already,
you can add them with the :command:`swupd bundle-add` command::

  # swupd bundle-add mixer

To satisfy all dependencies (until further development), you'll need the
following additional bundles::

  # swupd bundle-add os-clr-on-clr os-core-dev

Mixing
------

#. **Create a workspace**. Create an empty directory in your Clear image to
   use as a "workspace" for mixing. For these steps, we assume your workspace
   location is :file:`/home/clr/mix`.

#. **Configure builder.conf**. Copy the template conf file::

    # cp /usr/share/defaults/bundle-chroot-builder/builder.conf /etc/bundle-chroot-builder/`

   Note there are different sections to the builder.conf. The ``[Builder]`` section
   provides the mixer tools with required configuration options, defining where
   generated bundles and update metadata should get published. The ``[swupd]`` section
   is used by swupd-server to create an update with the newly mixed content.

   Edit the template configuration file according to your needs::

      # vim /etc/bundle-chroot-builder/builder.conf:

      [Builder]
      SERVER_STATE_DIR = /var/lib/update
      BUNDLE_DIR = /home/clr/mix/bundles
      YUM_CONF = /home/clr/mix/.yum-mix.conf

      [swupd]
      BUNDLE=os-core-update
      CONTENTURL=<URL where content will be hosted>   ### URL where swupd content is
                                                        #  published. Optional if not hosting updates
      VERSIONURL=<URL where version will be hosted>   ### Should be the same as CONTENTURL.
                                                        #  Optional if not hosting updates
      FORMAT=1                                        ### Can be any number.
                                                        # See 'OS Epoch' discussion for details

   The file ``builder.conf`` will be read automatically from ``/etc/bundle-chroot-builder``,
   but all of the scripts accept a ``-c/--config`` option to specify where
   the file is if you want to store it elsewhere. The :file:``.yum-mix.conf``
   file will be auto-generated for you.

#. **Generate the starting point for your Mixer**. In your workspace, run::
   
     # ./mixer-init-mix.sh -c /etc/bundle-chroot-builder/builder.conf
   Optionally, the ``-b/--buildver`` option can be passed to tell the script which
   Clear version to build the initial mix against. This may be needed if the build
   you are currently on is newer than the latest clr-bundles release tag.

   Currently, the only correct way to update an existing Clear image to a
   mixer-created update is to create an initial update that contains the same
   bundles and content as the image. Then you can verify ``--fix`` the
   Clear image to it. Lastly, update the Clear image as it normally would. 
   This step auto-generates that first version 10 for you, so you can focus
   on just your custom mix.

#. **Create/locate RPMs for mix.**. (Steps 4-6 are necessary only if you
   want to add your own RPMs to the Mix. If you are simply working with Clear
   only bundles, then skip to Step 7.)

   If you are creating RPMs from scratch, you may use ``autospec``,
   ``mock``, ``rpmbuild``, etc. to build them. If they are not
   built on Clear, make sure your configuration builds them correctly for Clear.

#. **Import RPMs into workspace**. The easiest way to do this is to create a
   ``results`` directory in your workspace (for example ``/home/clr/mix/results``),
   and to copy the RPMs you want into that directory. The mixer script will
   look here for RPMs needed to build a local RPM repo for yum to use.

#. **Create a local RPM repo**. Create an empty directory in your workspace
   named ``local`` and run::

    # mixer-add-rpms.sh --rpmdir results --repodir local

   After the script exits, you should see your RPMs and a repodata directory in
   ``/home/clr/mix/local``. If the RPMs are not all in the local directory, check
   to make sure that they are indeed valid RPM files and not corrupt.

#. **Initialize Clear/Mix version info**. In the workspace, run::

    # mixer-init-versions.sh -m 20

   This takes the Clear version from your image (or override it with
   ``-c/--clear-version`` to use another Clear build's content), and uses
   "20" for the mix version.

#. **Download Bundles (Optional)**.  Download ``clr-bundles``.  In the workspace,
   run::

    # mixer-update-bundles.sh

   This creates two folders: ``clr-bundles``, which contains all of the upstream
   bundles and should ``NOT`` be modified or touched, and ``mix-bundles``, which
   contains the bundle definitions the mixer will use.

   This step is optional because the script is already called by mixer-init-mix.sh,
   and only needs to be called again when you want to update the upstream clr-bundles
   folder in your workspace.

#. **Update bundle definitions**. The mixer uses a local clone of the
   ``clr-bundles`` repo to define bundles for the mix.

   To define your bundles:
      #. Navigate to the ``mix-bundles/`` directory.
      #. Make any needed modifications to the bundle set.
      #. Commit the result::
         
         $ git add .
         $ git commit -s -m 'Update bundles for mix'
   You can easily copy bundles over from the ``clr-bundles/bundles`` directory in
   the case that you want to simply use existing bundle sets. Note that
   ``mix-bundles`` should not have any folders inside of it, only bundle definitions.

   Why do this? With Git history, mixes are easy to revert to or refer
   to in the future if something were to go wrong with a new mix. If
   you're just testing this out, or if you really do not want to mess with Git,
   you can ignore committing for now. The next feature will be to
   implement an interactive way to modify/add/delete bundles, so much of
   this work can be abstracted out so Git work will be more automated.

   To add your own bundle, create a bundle definition file in ``mix-bundles/``
   and refer to :file:`os-core-update` for formatting, but be sure that
   the name does not conflict with another bundle. Add your package
   name(s) in that  bundle definition file to tell it what package(s)
   must be installed as part of that bundle.

#. **Build the bundle chroots** To build all of the ``chroots``
   that are based on the bundles you defined, in your workspace run::
   
    # mixer-build-chroots.sh

   If you have many bundles defined for your mix, this step may take some time.

#. **Create update**. In the workspace, run::

    # mixer-create-update.sh

   When the script completes, you'll find your mix update content under
   ``/var/lib/update/www/VER``, in this example, it will be located in
   ``/var/lib/update/www/20``.


OS Epoch or Format version
--------------------------

The "format" used in ``builder.conf`` might be more precisely referred to as an
OS "compatibility epoch". Versions of the OS within a given epoch are fully
compatible with themselves. Across the epoch boundary *something* has
changed in the OS. This change is impactful enough that the release where the
change has taken place must be visited to ensure operations occur in the
correct order. A format increment is the way we insure pre- and co-requisite
changes flow out with proper ordering.

From an update perspective, the format, or compatibility epoch, limits the
extent to which the client can be updated in a single step.

For the creation of a custom mix, the format version should start at '1',
or some known number, and increment only when a compatibility breakage is
introduced. Normal updates (updating a software package for example)
do not require a format increment.