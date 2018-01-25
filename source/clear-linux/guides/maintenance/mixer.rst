.. _mixer:

Use mixer tool
##############

*Mixing* refers to composing an operating system for specific use cases. While
the default Clear Linux\* OS for Intel® Architecture provides options to
install bundles for various server capabilities, some developers may wish to 1)
augment the operating system itself with functionality from their own packages
or 2) modify the structure of current bundles to cater to their particular
needs.

Prerequisites
=============

To start working with the Mixer tools, you'll need a recent image of Clear
Linux OS for Intel Architecture with the following bundle installed. If you
don't have it already, you can add it with the :command:`swupd bundle-add`
command like so::

  # swupd bundle-add mixer

Current Workflow
================

Mixing
------

#. **Create a workspace**. Create an empty directory in your Clear image to
   use as a "workspace" for mixing. For these steps, we assume your workspace
   location is :file:`/home/clr/mix`.

#. **Generate the starting point for your Mix**. In your workspace, run::

      # sudo mixer init --clear-version 13180 --mix-version 10

   This will initialize your workspace so that you can make a mix at version 10
   based on upstream Clear Linux version 13180. A default :file:`builder.conf` file
   will be created (if one doesn't already exist in your workspace), and a 
   :file:`mix-bundles` directory will be created.

   If you intend to build a mix with your own custom RPMs, run::

      # sudo mixer init --clear-version 13180 --mix-version 10 --local-rpms

   This will create :file:`local` and :file:`rpms` directories in your mix, and
   add their paths to the generated :file:`builder.conf`. (For more information
   on using these directories, or setting them up manually, see Step 4 below.)

   If you know you want to build a mix that includes all Clear bundles with no
   modifications, you can easily do so by running::

      # sudo mixer init --clear-version 13180 --mix-version 10 --all

#. **Configure builder.conf**. Edit the :file:`builder.conf` as needed.

   The :file:`builder.conf` file will be read automatically from the current
   workspace directory, but the ``--config`` option exists to specify where the
   file is if you want to store it elsewhere.

   Note there are different sections to the :file:`builder.conf`. The ``[Builder]``
   section provides the mixer tools with the required configuration options,
   defining where generated bundles and update metadata should get published.
   The ``[swupd]`` section is used by swupd-server to create an update with
   specific update parameters.

   Edit the template configuration file according to your needs. For this
   example, your :file:`builder.conf` should look like this, with both URL
   variables set to the domain or IP of the update server::

      # vim /etc/bundle-chroot-builder/builder.conf:

      [Builder]
      SERVER_STATE_DIR=/home/clr/mix/update
      BUNDLE_DIR=/home/clr/mix/mix-bundles
      YUM_CONF=/home/clr/mix/.yum-mix.conf
      CERT=/home/clr/mix/Swupd_Root.pem
      VERSIONS_PATH=/home/clr/mix/

      [swupd]
      BUNDLE=os-core-update
      CONTENTURL=<URL where the content will be hosted>
      VERSIONURL=<URL where the version of the mix will be hosted>
      FORMAT=1

   The ``SERVER_STATE_DIR`` is where the mix content will be output, and it
   is automatically created for you by the mixer. This can be set to any
   location, but for this example let's use the workspace directory. The same
   applies for ``BUNDLE_DIR``; it will be generated for you in the location
   specified in the :file:`builder.conf`, in this case 
   ``/home/clr/mix/mix-bundles``. This is where the bundle definitions are
   stored for your mix, and it's where the chroot-builder looks to know what
   bundles must be installed.

   The :file:`.yum-mix.conf` file defined in ``YUM_CONF`` will be auto-generated
   for you, as will the ``CERT`` file, :file:`Swupd_Root.pem`. A yum
   configuration is needed for the chroot-builder to know where the RPMs are
   hosted, and the certificate file is needed to sign the root Manifest to
   provide security for content verification.

   You may change the ``CERT=/path/to/cert`` line to point to a different
   certificate.  The chroot builder will insert the certificate specified here
   in ``/os-core-update/usr/share/clear/update-ca/``. This is the certificate
   used by the software update client to verify the :file:`Manifest.MoM`
   signature. For now, it is **HIGHLY** recommended that you do not modify this
   line, as the certificate swupd expects needs a very specific configuration to
   sign and verify properly. The certificate will be automatically generated for
   you, and the Manifest.MoM will be signed automatically as well, providing
   security for the update content you create.

   The ``CONTENTURL`` and ``VERSIONURL`` should be set to the domain or IP
   address where your update content will be served. This is the location that
   hosts the :file:`/home/clr/mix/update/www` (``SERVER_STATE_DIR``) directory.
   Creating a symlink to the directory in your server webdir is an easy way to
   host the content. These URLs are embeded in images created for your mix. They
   are where ``swupd-client`` will look to figure out if there is a new version
   available, and the location from which to download the update content. Think
   of these as the equivalent of https://cdn.download.clearlinux.org/update/
   used by Clear Linux, but for your derivative mix.

   To learn more about the ``FORMAT`` option, please refer to the "Format
   Version" section at the bottom of this document, and 
   https://github.com/clearlinux/swupd-server/wiki/Format-Bumps. For now, leave
   the ``FORMAT`` value alone and do not increment it.

   The mix version and Clear version will come from two state files:
   :file:`.mixversion` and :file:`.clearversion`, both of which will be created
   for you when you set-up the workspace. They will be created in the directory
   defined by the ``VERSIONS_PATH``.

#. **Create/locate RPMs for mix.**. (Steps 4-6 are necessary only if you
   want to add your own RPMs to the Mix. If you are working only with Clear
   bundles, then skip to Step 7.)

   If you are creating RPMs from scratch, you may use ``autospec``,
   ``mock``, ``rpmbuild``, etc. to build them. If they are not built on Clear,
   make sure your configuration and toolchain builds them correctly for Clear,
   or there is no guarantee they will be compatible.

#. **Import RPMs into workspace**. Create an :file:`rpms` directory in your
   workspace (for example :file:`/home/clr/mix/rpms`), and copy the RPMs you
   want into that directory. Next, add the following to your
   :file:`builder.conf`::

      RPMDIR=/home/clr/mix/rpms

   Mixer will look here for RPMs in order to build a local RPM repo for yum to
   use.

#. **Create a local RPM repo**. Create an empty directory in your workspace
   named :file:`local` and add the path in your :file:`builder.conf`::

      REPODIR=/home/clr/mix/local

   Once these values are configured, you can generate the yum repo by running::

      # sudo mixer add-rpms

   After the tool exits, you should see your RPMs and a repodata directory in
   :file:`/home/clr/mix/local`. If the RPMs are not all in this :file:`local`
   directory, check to make sure that they are indeed valid RPM files and not
   corrupt.

#. **Update/Add bundle definitions**. You can easily add bundles to your mix by
   running::

      # sudo mixer bundle add bundle1,bundle2,...

   This command will copy the specified bundle defintion files from your
   configured upstream version of Clear Linux (:file:`.clearversion`) into your
   :file:`mix-bundles` directory.

   Behind the scenes, mixer uses a local cache of the upstream Clear Linux
   bundle definitions. These are stored in the 
   :file:`.mixer/upstream-bundles/clr-bundles-{VER}/bundles/` directory in your
   workspace. Do *not* modify things in this directory; it is simply a mirror
   for the tool to use. However, you can refer to the files in this directory
   to see what bundles are available, or the format these files should have.

   To define your bundles:

      #. Navigate to the :file:`mix-bundles/` directory.
      #. Make any needed modifications to the bundle set.
      #. Commit the result::

         $ git add .
         $ git commit -s -m 'Update bundles for mix #<VER>'


   While using Git is optional, with Git history, mixes are easy to revert to or
   refer to in the future if something were to go wrong with a new mix. If
   you're just testing this out, or if you really do not want to mess with Git,
   you can ignore committing for now.

   To add your own bundle, create a bundle definition file in the correct format
   in the :file:`mix-bundles` directory (you can refer to an existing bundle,
   like :file:`mix-bundles/os-core-update`, for formatting). Be sure that the 
   bundle name you choose does not conflict with another bundle. Add your 
   package name(s) in the bundle definition file to tell it what package(s) 
   must be installed as part of that bundle.

#. **Build the bundle chroots** To build all of the ``chroots``
   that are based on the bundles you defined, in your workspace run::

    # sudo mixer build chroots

   If you have many bundles defined for your mix, this step may take some time.

#. **Create update**. In the workspace, run::

    # sudo mixer build update

   When the build completes, you'll find your mix update content under
   :file:`/home/clr/mix/update/www/VER`. In this example, it will be located in
   :file:`/home/clr/mix/update/www/{<MIXVERSION>}`, where ``<MIXVERSION>`` is
   the mix version you defined, or 10 by default.

   All content to make a fully usable mix will be created by this step, but note
   that only "zero packs" are automatically generated. Zero packs are the 
   content needed to go from nothing to the mix version you just built content
   for. To create optional "delta packs", which allow for transitioning from
   one mix version to another, run the pack-maker as follows::

      # sudo mixer-pack-maker.sh --to <MIX_VERSION> --from <PAST_VERSION> -S /home/clr/mix/update

   The pack-maker will generate all delta packs for changed bundles from
   ``PAST_VERSION`` to ``MIX_VERSION``. If your ``STATE_DIR`` is in a different
   location, be sure to specify where with the ``-S`` option. For the first
   build, no delta packs can be created because the "update" is from version 0, 
   which impicitly has no content, thus no deltas can be generated. For
   subsequent builds, :file:`mixer-pack-maker.sh` can be run to generate delta
   content between them (i.e
   10 to 20).

#. **Creating an image** Mixer uses the ``ister`` tool to create a bootable
   image from your update content. To configure the image ``ister`` creates,
   you'll need the ``ister`` config file. A default value can be obtained from
   the ``ister`` package::

      # cp /usr/share/defaults/ister/ister.json relase-image-config.json

   Feel free to inspect the config Clear Linux uses for its releases, which can
   be found here: https://raw.githubusercontent.com/bryteise/ister/master/release-image-config.json

   Note that mixer will automatically look for a file named ``release-image-
   config.json``, but you can choose whatever name you want. To use a different
   name, simply pass the ``--template path/to/file.config`` flag when creating
   your image.

   Edit the config to include all the bundles you want **pre-installed** into 
   your image. The rest of the bundles in your mix will be available to your
   users via ``swupd bundle add``. Keeping this list small allows for a smaller
   image size. For a minimal, base image this would be::

      "Bundles": ["os-core", "os-core-update", "kernel-native"]

   Next, set the "Version" field to say which mix version content the image
   should be built from. ``ister`` allows you to build an image from any mix
   version you've built, not just the current one. For the first build example
   we've been using, "Version" would be set to 10.

   Finally, to build the image, run::

      # sudo mixer build image --format 1

   The output from this should be an image that is bootable as a VM or
   installable to baremetal.

   .. note::
      By default, ``ister`` uses the format version of the build machine it is
      running on. As such, you need to pass in ``--format <FORMAT_NUMBER>`` if
      the format you are building is different than the format of Clear Linux OS
      you are currently building on. Your current format version can be found by
      running

      .. code-block:: console

         # cat /usr/share/defaults/swupd/format

Creating your next Mix version
------------------------------

**Update the next Mix version info**. Update the :file:`.mixversion` file to the
next version number you want to build.

From this point you can iterate through, starting again at step 4 and doing
modifications as needed. For example:

- Add/Remove/Modify Bundles
- ``sudo mixer build chroots``
- ``sudo mixer build update``
- (Optionally) ``sudo mixer-pack-maker.sh --to <NEWVERSION> --from <PREV_VERSION> -S /home/clr/mix/update``


Format Version
--------------

The "format" used in :file:`builder.conf` might be more precisely referred to as
an OS "compatibility epoch". Versions of the OS within a given epoch are fully
compatible with themselves and can update to any version in that epoch. Across
the format boundary *something* has changed in the OS, such that updating from
build M in format X, to build N in format Y will not work. Generally this
occurs when the software updater or manifests changed in a way that is no
longer compatible with the previous update scheme.

A format increment is the way we insure pre- and co-requisite changes flow out
with proper ordering. The update client will only ever update to the latest
release in its respective format version (unless overridden by command line
flags), thus we can guarantee all clients will update to the final version in
their given format, which *must* contain all the changes needed to understand
the content built in the following format. Only after reaching the final
release in the old format will a client be able to continue to update to
releases in the new format.

For the creation of a custom mix, the format version should start at '1', or
some known number, and increment only when a compatibility breakage is
introduced. Normal updates (updating a software package for example) do not
require a format increment.
