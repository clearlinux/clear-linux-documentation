.. _mixer:

Use mixer tool
##############

*Mixing* refers to composing an operating system for specific use cases.
While the default Clear Linux* OS for Intel® Architecture provides options
to install bundles for various server capabilities, some developers may wish
to either augment the operating system itself with functionality from their
own packages, or modify the structure of current bundles to cater to their
particular needs.

Prerequisites
*************

To start working with the mixer tools, you'll need a recent image of Clear
Linux OS for Intel Architecture with the following bundle installed. If you
don't have it already, you can add it with the :command:`swupd bundle-add`
command like so:

   .. code-block:: bash

      # swupd bundle-add mixer

Current mixing workflow
***********************

#. **Create a workspace**. Create an empty directory in your Clear image to
   use as a "workspace" for mixing. For these steps, we assume your workspace
   location is :file:`/home/clr/mix`.

#. **Generate the starting point for your mix**. In your workspace, run:

   .. code-block:: bash

      # mixer init

   This initializes your workspace so that you can make a mix at version 10
   based on the latest released upstream Clear Linux version. A default 
   :file:`builder.conf` file will be created (if one is not already present in
   your workspace), along with several version and tracking files, and two
   bundle directories: :file:`local-bundles` and :file:`upstream-bundles`.
   (We'll get to how these files and directories are used later.)

   If you wish to start with a different version of upstream Clear Linux, or a
   different initial mix version, these can be specified as optional flags.

   .. code-block:: bash

      # mixer init --clear-version 21060 --mix-version 100


   Additionally, if you intend to build a mix with your own custom RPMs, you can
   pass the optional :option:`--local-rpms` flag.

   .. code-block:: bash

      # mixer init --local-rpms

   This creates :file:`local-yum` and :file:`local-rpms` directories in your
   mix, and adds their paths to the generated :file:`builder.conf`. (For more
   information on using these directories, or setting them up manually, see
   Step 4 below.)

   If you know you want to include all upstream Clear bundles in your mix, you
   can easily add them all to your mix during initialization with the optional
   :option:`--all-upstream` flag.

   .. code-block:: bash

      # mixer init --all-upstream

   Finally, you may find it useful to track the contents of your mixer working
   directory with a Git repository. This can be a great way to track changes to
   your mix content, or revert to earlier versions should something go wrong.
   Mixer can set this up automatically by passing the optional :option:`--git`
   flag.

   .. code-block:: bash

      # mixer init --git

   .. note::
         Any or all of the above optional flags can be used at the same time.
         For example:

         .. code-block:: bash

            # mixer init --clear-version 21060 --mix-version 100 --local-rpms --all-upstream --git

#. **Configure builder.conf**. Edit the :file:`builder.conf` as needed.

   The :file:`builder.conf` file will be read automatically from the current
   workspace directory, but the :option:`--config` option exists to specify
   where the file is if you want to store it elsewhere.

   Note there are different sections of :file:`builder.conf`. The ``[Mixer]``
   section contains configuration values for how the mixer tool deals with
   bundles and keeps track of what is in your mix. The ``[Builder]`` section
   provides the mixer tools with the required configuration options for
   building your mix, and defines where generated update metadata should be
   published. The ``[swupd]`` section is used by swupd-server to create update
   content with specific update parameters.

   Edit the template configuration file according to your needs. For this
   example, your :file:`builder.conf` should look similar to the example
   below, with both URL variables set to the domain or IP of the update
   server:

   .. code-block:: console

      [Mixer]
      LOCAL_BUNDLE_DIR=/home/clr/mix/local-bundles

      [Builder]
      SERVER_STATE_DIR=/home/clr/mix/update
      BUNDLE_DIR=/home/clr/mix/mix-bundles
      YUM_CONF=/home/clr/mix/.yum-mix.conf
      CERT=/home/clr/mix/Swupd_Root.pem
      VERSIONS_PATH=/home/clr/mix

      [swupd]
      BUNDLE=os-core-update
      CONTENTURL=<URL where the content will be hosted>
      VERSIONURL=<URL where the version of the mix will be hosted>
      FORMAT=1

      [Server]
      debuginfo_banned=true
      debuginfo_lib=/usr/lib/debug/
      debuginfo_src=/usr/src/debug/

   The ``LOCAL_BUNDLE_DIR`` is where local bundle definition files are stored.
   These include any new, original bundles you create, as well as edited
   versions of upstream Clear bundles. (More on this in Step 4 below.)

   The ``SERVER_STATE_DIR`` is where the mixed content is output. This
   is automatically created for you by the mixer. You can set this
   directory to any location, but we will use the workspace directory for
   this example. The same applies for ``BUNDLE_DIR``. This directory is
   generated for you in the location specified in the :file:`builder.conf`, in
   this case ``/home/clr/mix/mix-bundles``. If you are using the legacy
   chroot-builder, this directory is where the bundle definition files are
   temporarily stored while building chroots. By default, this directory is not
   generated until it is needed, and is not generated at all if using the new
   chroot-builder built into mixer. (More on this below in Step 8.)

   The :file:`.yum-mix.conf` file defined in ``YUM_CONF`` is auto-generated,
   along with the ``CERT`` file, :file:`Swupd_Root.pem`. The yum configuration
   file is needed for the chroot-builder to know where the RPMs are hosted,
   and the certificate file is needed to sign the root Manifest to provide
   security for content verification.

   You can change the ``CERT=/path/to/cert`` line to point to a different
   certificate. The chroot builder inserts the certificate specified here
   in ``/os-core-update/usr/share/clear/update-ca/``. This is the certificate
   used by the software update client to verify the :file:`Manifest.MoM`
   signature. For now, we *highly* recommend that you do not modify this
   line, as the certificate that swupd expects needs a very specific
   configuration to sign and verify properly. The certificate is
   automatically generated, and the :file:`Manifest.MoM` is signed
   automatically as well, providing security for the updated content that
   you create.

   The ``CONTENTURL`` and ``VERSIONURL`` should be set to the domain or IP
   address where your updated content will be served. This is the location
   that hosts the :file:`/home/clr/mix/update/www` (``SERVER_STATE_DIR``)
   directory. Creating a symlink to the directory in your server webdir is
   an easy way to host the content. These URLs are embeded in images created
   for your mix. They are where ``swupd-client`` will look to figure out if
   there is a new version available, and the location from which to download
   the updated content. Think of these as the equivalent of the 
   `ClearLinux update page`_ used by Clear Linux, but for your derivative mix.

   To learn more about the ``FORMAT`` option, refer to the "Format Version"
   section at the bottom of this document, and `Format Bumps`_ on the Clear
   Linux wiki. For now, leave the ``FORMAT`` value alone and do not increment
   it.

   The mix version and upstream Clear version will come from two state files:
   :file:`mixversion` and :file:`upstreamversion`, both of which will be
   created for you when you set up the workspace. They will be created in the
   directory defined by the ``VERSIONS_PATH``.

#. **Create/locate RPMs for mix.**. (Steps 4 through 6 are necessary only
   if you want to add your own RPMs to the Mix. If you are working only with
   Clear bundles, then skip to Step 7.)

   If you are creating RPMs from scratch, you can use ``autospec``, ``mock``,
   ``rpmbuild``, etc. to build them. If they are not built on Clear,
   make sure your configuration and toolchain builds them correctly for Clear,
   or there is no guarantee they will be compatible.

#. **Import RPMs into workspace**. Create a :file:`local-rpms` directory in your
   workspace (for example :file:`/home/clr/mix/local-rpms`), and copy the RPMs
   you want into that directory. Next, add the following to your
   :file:`builder.conf`:

   .. code-block:: bash

      LOCAL_RPM_DIR=/home/clr/mix/local-rpms

   Mixer will look in this directory for RPMs to build a local RPM repo for
   yum to use.

#. **Create a local RPM repo**. Create an empty directory in your workspace
   named :file:`local-yum` and add the path in your :file:`builder.conf`:

   .. code-block:: bash

      LOCAL_REPO_DIR=/home/clr/mix/local-yum

   Once these values are configured, you can generate the yum repo by
   running the following command:

   .. code-block:: bash

      # sudo mixer add-rpms

   After the tool exits, you should see your RPMs and a repodata directory in
   :file:`/home/clr/mix/local-yum`. If the RPMs are not all in this 
   :file:`local-yum` directory, check to make sure that they are indeed valid
   RPM files and not corrupt.

#. **Add/remove/edit/list the bundles in your mix**. The bundles in your mix are
   specified in the Mix Bundle List. This list is stored as a flat file called
   :file:`mixbundles` in the directory defined by the ``VERSIONS_PATH`` variable
   in :file:`builder.conf`. This file is generated automatically during
   initialization, and is read from and written to by mixer when you use it to
   work with bundles.

   You can view what bundles are already in your mix by running:

   .. code-block:: bash

      # mixer bundle list

   This will show you a list of every bundle in your mix. Bundles are capable of
   including other bundles, and those bundles can themselves include other
   bundles. When you list the bundles in your mix this way, mixer will
   automatically recurse through these includes and show you every single bundle
   that will end up in your mix.

   If you see a bundle in the list that you weren't expecting, odds are it was
   included by something you added in. To get a better view at how a bundle
   ended up in your mix, you can pass the :option:`--tree` flag:

   .. code-block:: bash

      # mixer bundle list --tree

   This will print a tree view of your Mix Bundle List, visually showing what
   each bundle includes.

   Bundles fall into two categories: **upstream** and **local**. Upstream
   bundles are those provided by Clear Linux. Local bundles are bundles you've
   created yourself, or edited versions of upstream bundles.

   Upstream bundle definition files are downloaded and cached for you
   automatically by mixer, and are stored in the :file:`upstream-bundles`
   directory created in your working directory. Do *not* modify things in this
   directory; it is simply a mirror for the tool to use. The tool automatically
   caches the bundles for your configured version of Clear Linux (in your 
   :file:`upstreamversion` file), and cleans up old versions once they are no
   longer needed. You can see what upstream bundles are available by running:

   .. code-block:: bash

      # mixer bundle list upstream

   Local bundle definition files live in the :file:`local-bundles` directory.
   The location of this directory is specified by ``LOCAL_BUNDLE_DIR`` in your
   :file:`builder.conf`. For this example, this is
   :file:`/home/clr/mix/local-bundles`. You can see what local bundles are
   available by running:

   .. code-block:: bash

      # mixer bundle list local

   With either of the above commands, you can pass the :option:`--tree` flag to
   see a tree view of what other bundles each bundle includes.

   When looking for a bundle definition file, **mixer always checks local
   bundles first, then upstream**. As such, bundles found in
   :file:`local-bundles` will always take precedence to upstream bundles of the
   same name. This is how "editing" an upstream bundle works; the local, edited
   version overrides the version found upstream. (More on editing bundles in
   a moment.)

   You can easily **add bundles** to your mix by running:

   .. code-block:: bash

      # mixer bundle add bundle1 [bundle2...]

   This command adds the bundles you specify to your Mix Bundle List
   (:file:`mixbundles`). For each bundle you add, mixer checks your local and
   upstream bundles to make sure that the bundle you're adding actually exists.
   If any cannot be found, an error will be reported. When mixer adds a bundle,
   it will tell you whether it was found in local or upstream. You can also see
   this information when you run :command:`mixer bundle list`.

   To **remove a bundle** from your mix, run:

   .. code-block:: bash

      # mixer bundle remove bundle1 [bundle2...]

   This command will remove the bundles you specify from your Mix Bundle List
   (:file:`mixbundles`). By default, it does not remove the bundle definition
   file from your local bundles. If you would like to completely remove a
   bundle, including its local bundle definition file, the :option:`--local`
   flag can be passed. By default, removing a local bundle file this way will
   remove it from your mix as well. If you wish to *only* remove the local
   bundle definition file, you can also pass the :option:`--mix=false` flag.
   Please note that if you remove a local bundle that was an edited version of
   upstream, and that bundle is still in your mix, your mix will now be 
   referencing the original upstream version of the bundle. If you remove a 
   bundle that was *only* found locally and still leave the bundle in your Mix
   Bundles List, there will no longer be any valid bundle definition file to
   refer to, and mixer will produce an error.

   To **edit a bundle definition file**, run:

   .. code-block:: bash

      # mixer bundle edit bundle1 [bundle2...]

   If the bundle is found in your local bundles, mixer will edit this bundle
   definition file. If instead the bundle is only found upstream, mixer will
   copy the bundle definition file from upstream into your :file:`local-bundles`
   directory first. In either case, mixer will launch your default editor to
   edit the file. When the editor closes, mixer automatically validates the
   edited bundle file, and reports any errors it encounters. If it does find an
   error, you have the option of continuing to edit the file as-is, revert and
   edit, or skip and keep going to the next bundle. If you skip a file, a backup
   of the original file is saved with the ``.orig`` suffix. Because mixer always
   checks your local bundles first, edited copies of an upstream bundle will
   always take precedence over their upstream counterpart.

   This same command is used to create a totally **new bundle**: if the bundle
   name you specify is not found upstream, a blank template is generated in
   :file:`local-bundles` with the correct filename. The editor is again launched
   for you to fill out the bundle, and validation is performed on exiting. Add
   your package name(s) in the bundle definition file to tell it what package(s)
   must be installed as part of that bundle.

   Mixer will do basic **validation** on all bundles when they are used
   throughout the system: it will check that the bundle syntax is valid and can
   be parsed, and that the bundle file has a valid name. If you would like to
   manually run this validation on a bundle, you can run:

   .. code-block:: bash

      # mixer bundle validate bundle1 [bundle2...]

   This command has an optional :option:`--strict` flag, which additionally
   checks that the rest of the bundle header fields can be parsed and are
   non-empty, and that the bundle header ``Title`` field and the bundle filename
   match.

   .. note::
         If you initialized your workspace to be tracked as a Git repository
         (:command:`mixer init --git`), you may find it useful to apply a git
         commit after modifying what bundles are in your Mix Bundle List or
         editing a bundle definition file. All of the above :command:`mixer 
         bundle` commands support an optional :option:`--git` flag that will
         automatically apply a git commit when they are finished.

#. **Build the bundle chroots**. To build all of the ``chroots`` that are
   based on the bundles you defined, run the following command in your
   workspace:

   .. code-block:: bash

    # sudo mixer build chroots

   If you have many bundles in your mix, this step might take some
   time.

   By default, mixer will use the legacy chroot-builder. In this mode, the
   bundle definition files for the bundles in your mix will be automatically
   gathered into a :file:`mix-bundles` directory in the location specified by
   ``BUNDLE_DIR`` in your :file:`builder.conf`. **Do not edit these files**.
   Mixer will automatically clear out any contents of this directory before
   populating it on-the-fly as chroots are built.

   Mixer now has a new chroot-builder built into the mixer tool itself. While
   this is currently an experimental feature, you can (and should) use the new
   chroot-builder by passing the :option:`--new-chroots` flag. The legacy 
   chroot-builder will soon be deprecated, and mixer will use the new version
   automatically.

#. **Create update**. In the workspace, run:

   .. code-block:: bash

    # sudo mixer build update

   When the build completes, you will find your mix update content under
   :file:`/home/clr/mix/update/www/VER`. In our example, this will be
   located in :file:`/home/clr/mix/update/www/{<MIXVERSION>}`, where
   ``<MIXVERSION>`` is the mix version you defined (10 by default).

   By default, mixer will use the legacy swupd-server to generate the update
   content. Mixer now has a new implementation built into the mixer tool itself.
   While this is currently an experimental feature, you can (and should) use the
   new swupd-server by passing the :option:`--new-swupd` flag. The legacy
   swupd-server will soon be deprecated, and mixer will use the new version
   automatically.

   All content to make a fully usable mix will be created by this step, but
   note that only *zero packs* are automatically generated. Zero packs are
   the content needed to go from nothing to the mix version you just built
   content for. To create optional *delta packs*, which allow for
   transitioning from one mix version to another, run the pack-maker as
   follows:

   .. code-block:: bash

      # sudo mixer-pack-maker.sh --to <MIX_VERSION> --from <PAST_VERSION> -S /home/clr/mix/update

   The pack-maker will generate all delta packs for bundles that have changed
   from ``PAST_VERSION`` to ``MIX_VERSION``. If your ``STATE_DIR`` is in a
   different location, be sure to specify the location with the ``-S``
   option. For the first build, no delta packs can be created because the
   "update" is from version 0. Version 0 implicitly has no content, thus no
   deltas can be generated. For subsequent builds,
   :file:`mixer-pack-maker.sh` can be run to generate delta content between
   them (for example: 10 to 20).

#. **Creating an image**. Mixer uses the ``ister`` tool to create a bootable
   image from your updated content. To configure the image ``ister`` creates,
   you will need the ``ister`` config file. You can obtain a default value
   from the ``ister`` package:

   .. code-block:: bash

      # cp /usr/share/defaults/ister/ister.json relase-image-config.json

   For reference, you can inspect the ``ister`` config file that `Clear
   Linux uses`_ for its releases. 

   Note that mixer automatically looks for a file named 
   :file:`release-image-config.json`, but you can choose whatever name you want.
   To use a different name, simply pass the 
   :option:`--template path/to/file.config` flag when creating your image.

   Edit the config file to include all bundles that you want *preinstalled*
   into your image. The rest of the bundles in your mix will be available to your users via:

   .. code-block:: bash 

      # swupd bundle add 

   Keeping this list small allows for a smaller image size. For a minimal,
   base image, this list would be:

      .. code-block:: console

      "Bundles": ["os-core", "os-core-update", "kernel-native"]

   Next, set the ``Version`` field to the mix version content that the image
   should be built from. ``ister`` allows you to build an image from any mix
   version that you have built, not just the current one. For the first build
   example we've been using, ``Version`` would be set to 10.

   Finally, to build the image, run:

   .. code-block:: bash

      # sudo mixer build image --format 1

   The output from this should be an image that is bootable as a virtual
   machine and can be installed on bare metal.

   .. note::
      By default, ``ister`` uses the format version of the build machine it
      is running on. Therefore, if the format you are building is different
      than the format of the Clear Linux OS that you are building on, you
      need to pass :option:`--format <FORMAT_NUMBER>`. You can find your
      current format version by running:

      .. code-block:: bash

         # cat /usr/share/defaults/swupd/format

Creating your next mix version
==============================

**Update the next Mix version info**. To increment your mix version number for
your next mix, run:

   .. code-block:: bash

      # mixer versions update

This command will automatically update your mix version (stored in the 
:file:`mixversion` file), incrementing it by 10. If you'd like to increment by a
different amount, the :option:`--increment` flag can be used:

   .. code-block:: bash

      # mixer versions update --increment 100

Alternatively, if you want set your mix version to a specific value, you can
do so with the :option:`--mix-version` flag:

   .. code-block:: bash

      # mixer versions update --mix-version 200

Please note that the :command:`mixer versions update` command does not allow you
to set your mix version to something lower than its current value. This is
because your mix version is expected to always increase, even if the new mix is
undoing an earlier change. (If you've been tracking your working directory with
Git, it is possible to restore your mix to an earlier state, but be careful of
"rewriting history" if you are already publishing your mix content to users.)

From this point you can iterate through the instructions, starting again at
Step 4 and making modifications as needed. For example:

   - Add/remove/modify bundles
   - ``sudo mixer build chroots``
   - ``sudo mixer build update``
   - (Optionally) ``sudo mixer-pack-maker.sh --to <NEWVERSION> --from <PREV_VERSION> -S /home/clr/mix/update``

If you want to update the upstream version of Clear Linux on which your mix is
based, you can do so using the :option:`--upstream-version` flag:

   .. code-block:: bash

      # mixer versions update --upstream-version 21070

This command also accepts the keyword "latest": :option:`--upstream-version
latest`. This will set your upstream version to the latest released version of
upstream Clear Linux within the same format version. The :command:`mixer
versions update` command does not allow you to set your upstream version to a
value that would cross an upstream format boundary, as this would require a
"format bump" build, which is currently a manual process. You can read more
about format versions below.

If you simply wish to learn which mix version or upstream version you currently
are on, you can run:

   .. code-block:: bash

      # mixer versions


Format Version
**************

The ``format`` used in :file:`builder.conf` might be more precisely referred
to as an OS "compatibility epoch". Versions of the OS within a given epoch
are fully compatible with themselves and can update to any version in that
epoch. Across the ``format`` boundary *something* has changed in the OS,
such that updating from build M in format X, to build N in format Y will not
work. Generally this occurs when the software updater or manifests changed 
in a way that is no longer compatible with the previous update scheme.

A format increment is the way we insure pre- and co-requisite changes flow
out with proper ordering. The updated client will only ever update to the
latest release in its respective format version (unless overridden by
command line flags). Thus we can guarantee all clients will update to the
final version in their given format, which *must* contain all the changes
needed to understand the content built in the subsequent format. Only after
reaching the final release in the old format will a client be able to
continue to update to releases in the new format.

When creating a custom mix, the format version should start at '1', or
some known number, and should increment only when a compatibility breakage is
introduced. Normal updates (for example, updating a software package) do not
require a format increment.

.. _Clear Linux update page: https://cdn.download.clearlinux.org/update/
.. _Format Bumps: https://github.com/clearlinux/swupd-server/wiki/Format-Bumps
.. _Clear Linux uses: https://raw.githubusercontent.com/bryteise/ister/master/release-image-config.json
