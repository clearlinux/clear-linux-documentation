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
with the following bundle installed. If you don't have it already,
you can add it with the :command:`swupd bundle-add` command like so::

  # swupd bundle-add mixer

Mixing
------

#. **Create a workspace**. Create an empty directory in your Clear image to
   use as a "workspace" for mixing. For these steps, we assume your workspace
   location is :file:`/home/clr/mix`.

#. **Configure builder.conf**. Copy the template conf file::

    # cp /usr/share/defaults/bundle-chroot-builder/builder.conf /home/clr/mix/

   The file ``builder.conf`` will be read automatically from the current workspace directory,
   but all of the scripts accept a ``-c/--config`` option to specify where
   the file is if you want to store it elsewhere. To use one in your current workspace,
   copy the template to /home/clr/mix.
   The :file:``.yum-mix.conf`` file will be auto-generated for you.

   Note there are different sections to the builder.conf. The ``[Builder]`` section
   provides the mixer tools with required configuration options, defining where
   generated bundles and update metadata should get published. The ``[swupd]`` section
   is used by swupd-server to create an update with the newly mixed content.

   Edit the template configuration file according to your needs, for example like so::

      # vim /etc/bundle-chroot-builder/builder.conf:

      [Builder]
      SERVER_STATE_DIR=/home/clr/mix/update
      BUNDLE_DIR=/home/clr/mix/bundles
      YUM_CONF=/home/clr/mix/.yum-mix.conf
      CERT=/home/clr/mix/ClearLinuxRoot.pem
      CLEAR_VERSION=VER
      MIX_VERSION=VER

      [swupd]
      BUNDLE=os-core-update
      CONTENTURL=<URL where the content will be hosted>
      VERSIONURL=<URL where the version of the mix will be hosted>
      FORMAT=1


   You may change the ``CERT=/path/to/cert`` line which tells the chroot builder to insert the certificate
   specified for the mix in ``/os-core-update/usr/share/clear/update-ca/``. This is the certificate used by the software update client to verify the Manifest.MoM signature. For now, it is HIGHLY recommended that you do not modify this line, as the certificate swupd expects needs a very specific configuration to sign and verify properly. The certificate will be automatically generated for you, and the Manifest.MoM will be signed automatically as well, providing security for the update content you create.

   The CLEAR_VERSION is the upstream Clear Linux* OS for Intel® Architecture version the mix will be based off of, and all required content (RPMs) not provided by the mixer will be downloaded from that release.
   The MIX_VERSION is the version you want your mix to be.

   For this example, set CLEAR_VERSION=11230 and MIX_VERSION=10. You can of course choose any numbers you like for the MIX_VERSION, but it is recommended to use the current latest version of upstream for the CLEAR_VERSION. The CLEAR_VERSION can be updated as new upstream versions are released if needed.

   The CONTENTURL and VERSIONURL may be an IP address, or a domain name, which hosts the /home/clr/mix/update/www directory. A client running the mix will look to that URL to figure out if there is a new version available, and where to download update content from.

   To learn more about the FORMAT option, please refer to the bottom of this document "Format Version" and https://github.com/clearlinux/swupd-server/wiki/Format-Bumps for more information. For now leave the FORMAT value alone and do not increment it.

#. **Generate the starting point for your Mix**. In your workspace, run::
   
     # sudo mixer-init-mix.sh

   *If you wish to just build a mix that includes all Clear bundles with no modifications, run*::

    # sudo mixer-init-mix.sh --all-bundles
   And skip to ``Creating an image``. All the required content will be automatically built, and this mix
   will be identical to the version of Clear it is being composed from.

#. **Create/locate RPMs for mix.**. (Steps 4-6 are necessary only if you
   want to add your own RPMs to the Mix. If you are working only with Clear
   bundles, then skip to Step 7.)

   If you are creating RPMs from scratch, you may use ``autospec``,
   ``mock``, ``rpmbuild``, etc. to build them. If they are not
   built on Clear, make sure your configuration and toolchain builds them correctly for Clear.

#. **Import RPMs into workspace**. The way to do this is to create an
   ``rpms`` directory in your workspace (for example ``/home/clr/mix/rpms``),
   and to copy the RPMs you want into that directory. The mixer script will
   look here for RPMs in order to build a local RPM repo for yum to use.

#. **Create a local RPM repo**. Create an empty directory in your workspace
   named ``local`` and add the paths in your builder.conf::

    RPMDIR=/home/clr/mix/rpms
    REPODIR=/home/clr/mix/local

    These variables are automatically read; you simply need to run::

    # sudo mixer-add-rpms.sh

   After the script exits, you should see your RPMs and a repodata directory in
   ``/home/clr/mix/local``. If the RPMs are not all in the local directory, check
   to make sure that they are indeed valid RPM files and not corrupt.

#. **Update/Add bundle definitions**. The mixer uses a local clone of the
   ``clr-bundles`` repo to define bundles for the mix.

   To define your bundles:
      #. Navigate to the ``mix-bundles/`` directory.
      #. Make any needed modifications to the bundle set.
      #. Commit the result::
         
         $ git add .
         $ git commit -s -m 'Update bundles for mix #<VER>'

   You can easily copy bundles over from the ``clr-bundles/bundles`` directory in
   the case that you want to simply use existing bundle sets. Note that
   ``mix-bundles`` should not have any folders inside of it, only bundle definitions.
   Do *not* modify things in the clr-bundles dir, this is simply a mirror for you to
   use or refer to the Clear Linux OS bundle definitions.

   Why do this? With Git history, mixes are easy to revert to or refer
   to in the future if something were to go wrong with a new mix. If
   you're just testing this out, or if you really do not want to mess with Git,
   you can ignore committing for now.

   To add your own bundle, create a bundle definition file in ``mix-bundles/``
   and refer to :file:`mix-bundles/os-core-update` for formatting, but be sure that
   the name does not conflict with another bundle. Add your package
   name(s) in that  bundle definition file to tell it what package(s)
   must be installed as part of that bundle.

#. **Build the bundle chroots** To build all of the ``chroots``
   that are based on the bundles you defined, in your workspace run::
   
    # sudo mixer-build-chroots.sh

   If you have many bundles defined for your mix, this step may take some time.

#. **Create update**. In the workspace, run::

    # sudo mixer-create-update.sh

   When the script completes, you'll find your mix update content under
   ``/var/lib/update/www/VER``, in this example, it will be located in
   ``/var/lib/update/www/<MIXVERSION>``, where <MIXVERSION> is the mix version you
   defined, or 10 by default.

   All content to make a fully usable mix will be created by this step, but note that only zero packs are automatically generated. To create optional delta packs, run the pack-maker as follows::

    # sudo mixer-pack-maker.sh --to <MIX_VERSION> --from <PAST_VERSION> -S /home/clr/mix/update

   The pack-maker will generate all delta packs for changed bundles from PAST_VERSION to MIX_VERSION. If your STATE_DIR is in a different location be sure to specify where with the -S option.

#. **Initialize next Mix version info**. To update the versions and prep for your
   next mix::

   Update the MIX_VERSION in your builder.conf to the next version number you want to build. From this point you can iterate through, starting again at step 4 and doing modifications as needed, i.e.
   - Add/Remove/Modify Bundles
   - sudo mixer-build-chroots.sh
   - sudo mixer-create-update.sh
   - (Optionally) sudo mixer-pack-maker.sh --to <NEWVERSION> --from <PREV_VERSION> -S /home/clr/mix/update
   Next mix created.

#. **Update Bundles (Optional)**.  Update ``clr-bundles``.  In the workspace,
   run::

    # sudo mixer-update-bundles.sh

   This step is optional because the script is already called by mixer-init-mix.sh,
   and only needs to be called again when you want to update the upstream clr-bundles
   folder in your workspace. It also does not need to be called unless you are updating
   the CLEAR_VERSION number as well to match the newest upstream release.

**Creating an image**
To create a bootable image from your update content, you will need the configuration file for
ister to create images::

    # curl -O https://raw.githubusercontent.com/clearlinux/ister/master/release-image-config.json

Edit this to include  all the bundles you want pre-installed into your image. For a minimal, base
image this would be::

    "Bundles": ["os-core", "os-core-update", "kernel-native"]

And lastly, set the "Version:" to say which mix version content the image should be built from,
i.e. 10 for your first build. To build the image, run::

    # sudo ister.py -t release-image-config.json -V file:///home/clr/mix/update/www/ -C file:///home/clr/mix/update/www/ -f 1

The output from this should be an image that is bootable as a VM or installable to baremetal. *Note* that 
you may need to pass in -f/--format <FORMAT_NUMBER> if the format you are building is different than the
format of Clear Linux OS you are currently building on. Format version can be found via::
    # cat /usr/share/defaults/swupd/format

Format Version
--------------------------

The "format" used in ``builder.conf`` might be more precisely referred to as an
OS "compatibility epoch". Versions of the OS within a given epoch are fully
compatible with themselves and can update to any version in that epoch. Across
the format boundary *something* has changed in the OS, such that updating from
build M in format X, to build N in format Y will not work. Generally this occurs
when the software updater or manifests changed in a way that is no longer
compatible with the previous update scheme.

A format increment is the way we insure pre- and co-requisite
changes flow out with proper ordering. The update client will only ever update
to the latest release in its respective format version (unless overridden by
command line flags), thus we can guarantee all clients will update to the final
version in their given format, which *must* contain all the changes needed
to understand the content built in the following format. Only after reaching the
final release in the old format will a client be able to continue to update to
releases in the new format.

For the creation of a custom mix, the format version should start at '1',
or some known number, and increment only when a compatibility breakage is
introduced. Normal updates (updating a software package for example)
do not require a format increment.
