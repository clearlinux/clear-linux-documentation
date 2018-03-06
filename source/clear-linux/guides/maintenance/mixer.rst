.. _mixer:

Use mixer tool
##############

*Mixing* refers to composing an operating system for specific use cases. While
the default |CLOSIA| provides options to install bundles for various server
capabilities, some developers may wish to either augment the operating system
itself with functionality from their own packages or modify the structure of
current bundles to cater to their particular needs.

Prerequisites
*************

To start working with the mixer tools, you need a recent image of |CL| with
the `mixer` bundle installed. If the bundle is not yet installed, you can add it
with the :command:`swupd bundle-add` command as follows:

   .. code-block:: bash

      sudo swupd bundle-add mixer

Current mixing workflow
***********************

There are two different workflows to create your own mix.

The following workflow applies if the mix includes your own
:abbr:`RPMs (RPM Package Manager files)`:

#. `Create a workspace`_
#. `Generate the starting point for your mix`_
#. `Edit builder.conf`_
#. `Create or locate RPMs for the mix`_
#. `Import RPMs into workspace`_
#. `Create a local RPM repo`_
#. `List, edit, create, add, remove, or validate bundles`_
#. `Build the bundle chroots`_
#. `Create an update`_
#. `Create an image`_

Alternatively, the following workflow applies if the mix only uses |CL|
bundles.

#. `Create a workspace`_
#. `Generate the starting point for your mix`_
#. `Edit builder.conf`_
#. `List, edit, create, add, remove, or validate bundles`_
#. `Build the bundle chroots`_
#. `Create an update`_
#. `Create an image`_

The following sections contain detailed information on every step of
these workflows.

Create a workspace
******************

Create an empty directory in your |CL| image to use as a **workspace** for
mixing with the following command:

.. code-block:: bash

    mkdir /home/clr/mix

This guide assumes your workspace location is :file:`/home/clr/mix`.

Generate the starting point for your mix
****************************************

In your workspace, initialize mixer with the following command:

.. code-block:: bash

   sudo mixer init

This command initializes your workspace for you to make a mix at version 10
based on the latest released upstream |CL| version. If a :file:`builder.conf`
file is not already present in your workspace, mixer creates a default configuration
file along with several version and tracking files and two bundle directories:
:file:`local-bundles` and :file:`upstream-bundles`.

If you wish to start with a different version of upstream |CL| or a
different initial mix version, these options can be specified as flags, for example:

.. code-block:: bash

   sudo mixer init --clear-version 21060 --mix-version 100


Additionally, to build a mix with your own custom RPMs, use the optional
 :option:`--local-rpms` flag, for example:

.. code-block:: bash

   sudo mixer init --local-rpms

This command creates the :file:`local-yum` and :file:`local-rpms` directories in your
mix workspace and adds their paths to the generated :file:`builder.conf`. For more
information on using these directories or setting them up manually, see
`Create or locate RPMs for the mix`_.

If all upstream |CL| bundles are part of the mix, you can easily add them all
during initialization with the optional :option:`--all-upstream` flag, for
example:

.. code-block:: bash

   sudo mixer init --all-upstream

Finally, you may want to track the contents of your mixer workspace with a Git
repository. This is a great way to track changes to your mix's content or to
revert to earlier versions if something goes wrong. Mixer can set this up
automatically with the optional :option:`--git` flag, for example:

.. code-block:: bash

   sudo mixer init --git

.. note::
   You can use any or all of the above optional flags at the same time, for example:

   .. code-block:: bash

      sudo mixer init --clear-version 21060 --mix-version 100 --local-rpms --all-upstream --git

Edit builder.conf
*****************

To configure the mixer tool, you must edit the :file:`builder.conf` as needed.

The file :file:`builder.conf` is read automatically from the current workspace
directory. Use the :option:`--config` flag during initialization to specify a
alternate path to the file as needed.

The :file:`builder.conf` file has different sections, for example:

* The `[Builder]` section provides the mixer tools with the required
  configuration options. This section defines the path where the generated
  bundles and update metadata are published.

* The `[swupd]` section contains specific update parameters. The
  :abbr:`swupd-server (software update server)` creates an update using
  said specific update parameters.

Edit the configuration file according to your needs with the command:

.. code-block:: bash

   sudo vim /etc/bundle-chroot-builder/builder.conf

Your version of the :file:`builder.conf` file should resemble the
following example:

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

The following variables require further explanation:

* The `LOCAL_BUNDLE_DIR` variable sets the path where mixer stores the local
  bundle definition files. These bundle definition files include any new,
  original bundles you create and edited versions of upstream |CL| bundles.

* The `SERVER_STATE_DIR` variable sets the path for the output of the mix
  content. Mixer automatically creates the path for you but the path can be
  set to any location. In this example, we use the workspace directory.

* The `BUNDLE_DIR` sets the path where mixer temporarily stores the bundle
  definition files while building chroots. Only the legacy chroot-builder uses
  this path. By default, mixer does not generate this directory until needed.
  In our example, the path is set to :file:`/home/clr/mix/mix-bundles`. The
  new chroot-builder does not generate the folder at all.

* The `YUM_CONF` variable sets path where mixer automatically generates the
  :file:`.yum-mix.conf` yum configuration file. The yum configuration file
  points the chroot-builder to the path where the RPMs are stored.

* The `CERT` variable sets the path where mixer stores the
  :file:`Swupd_Root.pem` certificate file. The chroot-builder needs the
  certificate file to sign the root :file:`Manifest.MoM` file to provide
  security for content verification. The value of the `CERT` variable can
  point to a different certificate. The chroot-builder inserts the
  certificate specified here in the
  :file:`/os-core-update/usr/share/clear/update-ca/` path. The software
  update client uses this certificate to
  verify the :file:`Manifest.MoM` file's signature. For now, we **strongly**
  recommend not to modify this line as the certificate `swupd` expects needs
  a very specific configuration to sign and verify properly. Mixer
  automatically generates the certificate and signs the
  :file:`Manifest.MoM` file providing security for your created update
  content.

* The `CONTENTURL` and `VERSIONURL` variables set the domain or IP address
  where mixer serves your updated content and the corresponding version. You
  can set the `CONTENTURL` and `VERSIONURL` URL variables to the domain or IP-
  address of the update server. The `SERVER_STATE_DIR` directory is hosted
  here: :file:`/home/clr/mix/update/www`. Creating a symlink to the directory
  in your server webdir is an easy way to host the content. These URLs are
  embedded in images created for your mix. The `swupd-client` looks at these
  URLs to figure out if there is a new version available and the location from
  which to download the updated content. Think of these links as the
  equivalent to the |CL| `update page`_ but for your mix.

* The `FORMAT` variable relates to the format bump. To learn more about the
  `FORMAT` option, see :ref:`mixer-format` and the `format bumps wiki`_. For
  now, leave the `FORMAT` value unchanged.

* The `VERSIONS_PATH` variable set the path for the mix version and upstream
  |CL| version two state files: :file:`mixversion` and
  :file:`upstreamversion`. Mixer creates both files for you when you set up
  the workspace.

.. note:: If you are working only with |CL| bundles, then
   skip to `List, edit, create, add, remove, or validate bundles`_.

Create or locate RPMs for the mix
*********************************

If you create RPMs from scratch, you can use `autospec`, `mock`, `rpmbuild`,
or similar tools to build them. If the RPMs are not built on |CL|, ensure your
configuration and tool-chain builds them correctly for Clear or there is no
guarantee they will be compatible. For more information on building the RPMs
properly visit our `build RPMs instructions`_.

Import RPMs into workspace
**************************

#. Create a :file:`local-rpms` directory in your workspace, for example
   :file:`/home/clr/mix/local-rpms`.

#. Copy the RPMs into the created directory.

#. Add the following line to your :file:`builder.conf` file:

   .. code-block:: console

      LOCAL_RPM_DIR=/home/clr/mix/local-rpms

Mixer uses this directory to find the RPMs to build a local RPM repo for
yum to use.

Create a local RPM repo
***********************

#. Create an empty directory in your workspace named :file:`local-yum`.
#. Add the path to your :file:`builder.conf` file:

   .. code-block:: console

      LOCAL_REPO_DIR=/home/clr/mix/local-yum

#. With these values configured, generate the yum repo with the following command:

   .. code-block:: bash

      sudo mixer add-rpms

After the tool exits, you should see the RPMs and a repository data directory in
:file:`/home/clr/mix/local-yum`. If the RPMs are not all in this
:file:`local-yum` directory, check to ensure they are valid RPM files and not
corrupt.

List, edit, create, add, remove, or validate bundles
****************************************************

The bundles in the mix are specified in the mix bundle list. Mixer stores
this list as a flat file called :file:`mixbundles` in the path set in the
`VERSIONS_PATH` variable of the :file:`builder.conf` file. Mixer generates
the mix bundle list file automatically during initialization. Mixer reads
and writes the bundle list file when you change the bundles of the mix.

List the bundles in the mix
===========================

To view the bundles already in the mix, enter the following command:

.. code-block:: bash

   sudo mixer bundle list

The command shows a list of every bundle in the mix. Bundles can include other
bundles and those bundles can themselves include other bundles. When listing
the bundles with this command, mixer automatically recurses through the
includes to show every single bundle in the mix.

If you see an unexpected bundle in the list, the bundle probably is included
in another bundle. Use the :option:`--tree` flag to get a better view of how a
bundle ended up in the mix, for example:

.. code-block:: bash

   sudo mixer bundle list --tree

This command prints a tree view of the mix bundle list explicitly showing each
included bundle.

Bundles fall into two categories: **upstream** and **local**.

Upstream bundles are those provided by |CL|.

Mixer automatically downloads and caches upstream bundle definition files. The
definition files are stored in the :file:`upstream-bundles` directory in the
workspace. Do **not** modify the files in this directory. The directory is
simply a mirror for mixer to use.

The mixer tool automatically caches the bundles for the |CL| version configured in the
:file:`upstreamversion` file. Mixer also cleans up old versions once they are no
longer needed. See the available upstream bundles with the following command:

.. code-block:: bash

   sudo mixer bundle list upstream

Local bundles are bundles you create or edited versions of upstream bundles.

Local bundle definition files live in the :file:`local-bundles` directory.
The `LOCAL_BUNDLE_DIR` variable sets the path of this directory in your
:file:`builder.conf` configuration file. For this example, the path is
:file:`/home/clr/mix/local-bundles`. See the available local bundles with the
following command:

.. code-block:: bash

   sudo mixer bundle list local

Both the local or upstream :command:`bundle list` commands accept the
:option:`--tree` flag to print a tree view explicitly showing each included
bundle.

Edit the bundles in the mix
===========================

**Mixer always checks local bundles first and the upstream bundles second.**

Therefore, bundles in the :file:`local-bundles` directory always take
precedence over the upstream bundles of the same name.

This precedence enables the editing of upstream bundles. The local, edited
version of the bundle overrides the bundle version found upstream.

For example, to edit the `bundle1` definition file, we use the following
command:

.. code-block:: bash

   sudo mixer bundle edit bundle1

If `bundle1` is found in your local bundles, mixer edits the bundle definition
file. If instead `bundle1` is only found upstream, mixer copies the bundle
definition file from upstream into your :file:`local-bundles` directory first.

In both cases, mixer launches your default editor to edit the file. When the
editor closes, mixer automatically validates the edited bundle file and
reports any errors found. If mixer finds an error, you can edit the file as-
is, revert and edit, or skip and move on to the next bundle. If you skip a
file, mixer saves a backup of the original file with the ``.orig`` suffix.
Because mixer always checks your local bundles first, edited copies of an
upstream bundle always take precedence over their upstream counterpart. You
can edit multiple bundles with the following command:

.. code-block:: bash

   sudo mixer bundle edit bundle1 bundle2 [bundle3 ...]

Create bundles for the mix
==========================

To create a totally **new bundle**, the bundle name you specify cannot exist
upstream. If that is the case, create a `new-bundle` with the following
command:

.. code-block:: bash

   sudo mixer bundle edit new-bundle

This command generates a blank template in :file:`local-bundles` with the
:file:`new-bundle` filename. Mixer launches the editor for you to fill out the
bundle and performs validation on exiting. Add your package or packages in the
bundle definition file to define the packages to install as part of the bundle.

.. note::

   The :command:`mixer bundle edit` accepts multiple bundles at once. Thus,
   you can create multiple new bundles in a single command, for example:

   .. code-block:: bash

      sudo mixer bundle edit new-bundle1 new-bundle2 [new-bundle3 ...]

Add bundles to the mix
======================

Add `bundle1` to your mix easily with the following command:

.. code-block:: bash

   sudo mixer bundle add bundle1

This command adds the bundles you specify to your mix bundles list stored in
the :file:`mixbundles` file. For each bundle you add, mixer checks your local
and upstream bundles to ensure the added bundle actually exists. If mixer
cannot find the bundle, it reports back an error. Additionally, when mixer
adds a bundle, it tells you whether the bundle is local or upstream.
Alternatively, you can learn this information with the
:command:`mixer bundle list` command, see `List the bundles in the mix`_.

To add multiple bundles at once, use the following command:

.. code-block:: bash

   sudo mixer bundle add bundle1 bundle2 [bundle3 ...]

Remove bundles from the mix
===========================

Remove `bundle1` from your mix with the following command:

.. code-block:: bash

   sudo mixer bundle remove bundle1

This command remove the `bundle1` from the mix bundle list stored in the
:file:`mixbundles` file. By default, the command does not remove the bundle
definition file from your local bundles. To completely remove a bundle,
including its local bundle definition file, use the following command with the
:option:`--local` flag:

.. code-block:: bash

   sudo mixer bundle remove --local bundle1

By default, removing a local bundle file with this command removes the bundle
from the mix as well. To only remove the local bundle definition file, use the
following command with the :option:`--mix=false` flag:

.. code-block:: bash

   sudo mixer bundle remove --local --mix=false bundle1

If you remove a local edited version of an upstream bundle and keep the bundle
in the mix, the mix then references the original upstream version of the
bundle.

On the other hand, if you remove a bundle only found locally but keep the
bundle in the mix bundles list, mixer will no longer find a valid bundle
definition file and will produce an error.

Validate the bundles in the mix
===============================

Mixer performs basic **validation** on all bundles when used
throughout the system.

Mixer checks the validity of the bundle's syntax and name. Mixer also ensures
the bundle can be parsed. Run this validation manually on bundle1 with the
following command:

.. code-block:: bash

   sudo mixer bundle validate bundle1

With the optional :option:`--strict` flag, the command additionally
checks if the rest of the bundle header fields can be parsed, if they are
non-empty, and if the bundle header ``Title`` field and the bundle filename
match. Perform a strict validation of `bundle1` with the following command:

.. code-block:: bash

   sudo mixer bundle validate --strict bundle1

Validate multiple bundles with the following command:

.. code-block:: bash

   sudo mixer bundle validate bundle1 bundle2 [bundle3 ...]

Managing bundles with Git
=========================

If you initialized your workspace to be tracked as a Git repository
with the :command:`mixer init --git` command, it might be useful to apply a git
commit after modifying the mix bundle list or editing a bundle definition file.

All the :command:`mixer bundle` commands on the previous sections support an
optional :option:`--git` flag. The flag automatically applies a git commit
when the command completes, for example:

.. code-block:: bash

   sudo mixer bundle remove --git bundle1

Build the bundle chroots
************************

To build all the ``chroots`` based on the defined bundles, use the following
command in your workspace:

.. code-block:: bash

   sudo mixer build chroots

If the mix has many bundles, this step might take some time.

By default, mixer uses the legacy chroot-builder. In this mode, mixer
automatically gathers the bundle definition files for the bundles in the mix
into a :file:`mix-bundles` directory. The directory's path is set in the
`BUNDLE_DIR` variable in the :file:`builder.conf`. **Do not edit these
files.** Mixer automatically clears out any contents in this directory before
populating it on-the-fly as mixer builds the chroots.

We have build a new chroot-builder into the mixer tool itself. While this is
currently an experimental feature, you should use the new chroot-builder. To use
the new chroot-builder, use the following command with the
:option:`--new-chroots` flag:

.. code-block:: bash

   sudo mixer build chroots --new-chroots

We will soon deprecate the legacy chroot-builder and mixer will use the new version
automatically.

Create an update
****************

Create an update with the following command:

.. code-block:: bash

   sudo mixer build update

When the build completes, you can find the mix update content under
:file:`/home/clr/mix/update/www/VER`. In our example, the update content is
found in :file:`/home/clr/mix/update/www/{<MIXVERSION>}`. `<MIXVERSION>`
is the mix version defined, 10 by default.

By default, mixer uses the legacy `swupd-server` to generate the update
content. We have built a new implementation into the mixer tool itself. While
this is currently an experimental feature, you should use the new swupd-
server. To use the the new swupd-server, use the following command with the
:option:`--new-swupd` flag:

.. code-block:: bash

   sudo mixer build update --new-swupd

We will soon deprecate the legacy swupd-server and mixer will use the new version
automatically.

Mixer creates all the content needed to make a fully usable mix with this
step. However, only *zero packs* are automatically generated. Zero packs are
the content needed to go from nothing to the mix version for which you just
built the content.

Create optional *delta packs*, which allow the transition from one mix version
to another, with the following command:

.. code-block:: bash

   sudo mixer-pack-maker.sh --to <MIX_VERSION> --from <PAST_VERSION> -S /home/clr/mix/update

The pack-maker generates all delta packs for the bundles changed from
`PAST_VERSION` to `MIX_VERSION`. If your `STATE_DIR` is in a different
location, specify the location with the :option:`-S` flag. Mixer cannot create
delta packs for the first build because the update is from version 0. Version
0 implicitly has no content, thus, mixer can generate no deltas.

For subsequent builds, you can run :file:`mixer-pack-maker.sh`  to generate
delta content between them, for example: 10 to 20.

Create an image
*****************

Since mixer uses the `ister` tool to create a bootable image from your updated
content, we must first configure the `ister` tool. To configure the image
`ister` creates, we need the `ister` configuration file. Obtain a copy with
the default values from the `ister` package with the following command:

.. code-block:: bash

   sudo cp /usr/share/defaults/ister/ister.json relase-image-config.json

For reference, you can inspect the `Clear Linux ister configuration file`_
used for releases.

Edit the configuration file to include all bundles you want *preinstalled* in
the image. Users can install the bundles in the mix not included in the
configuration file with the following command:

.. code-block:: bash

   sudo swupd bundle add

Keeping the list of bundles in the configuration file small allows for a
smaller image size. For the minimal base image, the list is:

.. code-block:: console

   "Bundles": ["os-core", "os-core-update", "kernel-native"]

Next, set the `Version` field to the mix version content mixer should use to
build image. `ister` allows you to build an image from any mix version you
have built, not just the current one. In our example so far, `Version` is set
to 10.

With the `ister` tool configured, build the image with with the following command:

.. code-block:: bash

   sudo mixer build image --format 1

This command outputs an image bootable as a virtual machine and which can be
installed on bare metal.

Mixer automatically looks for the :file:`release-image-config.json` file but
you can freely choose the filename. To use a different name, simply pass the
:option:`--template` flag when creating your image, for example:

.. code-block:: bash

   sudo mixer build image --format 1 --template path/to/file.config

By default, `ister` uses the format version of the build machine it runs on.
Therefore, if the format you are building differs from the format of the |CL|
OS you are building on, you must use the :option:`--format <FORMAT_NUMBER>`
flag. Find the current format version of your OS with the following command:

.. code-block:: bash

   sudo cat /usr/share/defaults/swupd/format

Update the next mix version information
***************************************

Increment the mix version number for the next mix with the following command:

.. code-block:: bash

   sudo mixer versions update

This command automatically updates the mix version stored in the
:file:`mixversion` file incrementing it by 10. To increment by a different
amount, use the :option:`--increment` flag, for example:

.. code-block:: bash

   sudo mixer versions update --increment 100

Alternatively, to set the mix version to a specific value, use the
:option:`--mix-version` flag, for example:

.. code-block:: bash

   sudo mixer versions update --mix-version 200

The :command:`mixer versions update` command does not allow you to set the mix
version to a value lower than its current value. The mix version is expected
to always increase, even if the new mix is undoing an earlier change.

If you have been tracking your workspace with Git, you can restore the mix to
an earlier state but be careful of "rewriting history" if you are publishing
the mix content to users already.

Update the upstream version of |CL| used as a base for the mix, with the
following command using the :option:`--upstream-version` flag:

.. code-block:: bash

   sudo mixer versions update --upstream-version 21070

This command also accepts the keyword "latest":

.. code-block:: bash

   sudo mixer versions update --upstream-version latest

This command sets the upstream version to the latest released version of
upstream |CL| within the same format version. The :command:`mixer
versions update` command does not allow to set an upstream version to a
value crossing an upstream format boundary. Such values require a
"format bump" build, which is currently a manual process. See :ref:`mixer-format`
for more information.

Learn which mix version or upstream version you currently are on with the
following command:

.. code-block:: bash

   sudo mixer versions

At this point, you can continue to iterate through the workflows and make
modifications as needed. For example:

#. Add, remove, or modify bundles.
#. Build the chroots with:

   .. code-block:: bash

      sudo mixer build chroots

#. Build and update with:

   .. code-block:: bash

      sudo mixer build update

#. Optionally,create delta packs with:

   .. code-block:: bash

      sudo mixer-pack-maker.sh --to <NEWVERSION> --from <PREV_VERSION> -S /home/clr/mix/update

.. _mixer-format:

Format version
**************

The `Format` variable set in the :file:`builder.conf` can be more precisely
referred to as an OS *compatibility epoch*. Versions of the OS within a given
epoch are fully compatible and can update to any version in that epoch. Across
the `Format` boundary, the OS has changed in such a way, that updating from
build M in format X, to build N in format Y will not work. Generally, this
scenario occurs when the software updater or manifests change in a way no
longer compatible with the previous update scheme.

Using a format increment, we insure pre- and co-requisite changes flow out
with proper ordering. The updated client only ever updates to the latest
release in its respective format version, unless overridden by command line
flags. Thus, we can guarantee all clients update to the final version in their
given format. The given format *must* contain all the changes needed to
understand the content built in the subsequent format. Only after reaching the
final release in the old format, can a client continue to update to releases
in the new format.

When creating a custom mix, the format version should start at '1' or some
known number. The format version should increment only when a compatibility
breakage is introduced. Normal updates, like updating a software package for
example, do not require a format increment.

.. _update page: https://cdn.download.clearlinux.org/update/

.. _format bumps wiki: https://github.com/clearlinux/swupd-server/wiki/Format-Bumps

.. _build RPMs instructions: https://github.com/clearlinux/common#build-rpms-for-a-package

.. _Clear Linux ister configuration file:
   https://raw.githubusercontent.com/bryteise/ister/master/release-image-config.json
