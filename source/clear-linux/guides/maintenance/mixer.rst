.. _mixer:

Use mixer tool
##############

*Mixing* refers to composing an operating system for specific use cases.
While the default |CLOSIA| provides options to install bundles for various
server capabilities, some developers may wish to either augment the
operating system itself with functionality from their own packages or modify
the structure of current bundles to cater to their particular needs.

Prerequisites
*************

To start working with the mixer tools, you need a recent image of |CL| with
the `mixer` bundle installed. If the bundle is not yet installed, you can
add it with the :command:`swupd bundle-add` command as follows:

.. code-block:: bash

   sudo swupd bundle-add mixer

Current mixing workflow
***********************
Mixer by default runs *all* build commands in a container to ensure the
correct version of the tooling is being used. This also allows custom mixes
to automatically perform downstream format bumps when upstream releases
a format bump. You can still run mixer natively by appending --native to
any of the commands. Note that you cannot run mixer if you are already in a
container, unless you pass --native to the command. Nested containerization
is not supported, nor is building images using the container mode.

There are two different workflows to create your own mix.
First, if your mix only uses |CL| content, *skip step 5* below. 
Second, if your mix includes your own 
:abbr:`RPMs (RPM Package Manager files)`, follow all these steps. 

#. `Create ngninx web server to host mixer updates`_
#. `Create a workspace`_
#. `Generate the starting point for your mix`_
#. `Edit builder.conf`_
#. `Create custom RPMs`_
    #. `Create or locate RPMs for the mix`_
    #. `Import RPMs into workspace`_
    #. `Create a local RPM repo`_
#. `List, edit, create, add, remove, or validate bundles`_
#. `Build the bundle chroots`_
#. `Create an update`_
#. `Create an image`_

The following sections contain detailed information on every step of
these workflows.

.. _create-nginx-web-server:

Create nginx web server to host mixer updates
**********************************************

Follow these steps to set up a HTTP service with ``nginx`` web 
server, where you can host custom |CL| mixes.  

#. Install ``web-server-basic``: 
   
   .. code-block:: bash

      sudo swupd bundle-add web-server-basic

#. Make the directory where mixer updates will reside.  

   .. code-block:: bash

      sudo mkdir -p /var/www

#. Create a symbolic link.

   .. code-block:: bash

      sudo ln -sf /home/clr/mix/update/www /var/www/mixer

   .. note::

      `/home/clr/mix` is the workspace for the mix (read `Create workspace`)


#. Set up ``nginx`` configuration. 

   .. code-block:: bash

      sudo mkdir -p  /etc/nginx/conf.d

#. Copy the default example configuration file. 

   .. code-block:: bash

      sudo cp -f /usr/share/nginx/conf/nginx.conf.example /etc/nginx/nginx.conf

#. Open ``mixer.conf`` with an editor.

   .. code-block:: bash
 
      sudo nano /etc/nginx/conf.d/mixer.conf 

#. Add the server configuration content below to ``mixer.conf``. 

   .. code-block:: console

      server {
           server_name localhost;
           location / {
                     root /var/www/mixer;
                     autoindex on; 
           }
      }

#. Restart the daemon, enable nginx on boot, and start the service.

   .. code-block:: bash

      sudo systemctl daemon-reload 

      sudo systemctl enable nginx 

      sudo systemctl start nginx 

#. To verify the web server is running, enter in an Internet browser:

   .. code-block:: bash

      http://localhost

#. Alternatively, verify the server is running by entering:

   .. code-block:: bash

      ps aux | grep nginx 

   .. note:: 

      If `nginx` is active, a list should appear showing one master process 
      and a few worker processes.

Connect the URL to mixer
========================

Add the URL of the `nginx` server to builder.conf. Your |CL| clients connect 
to this URL to find the update content.    

#. Get the IP address of your nginx server: 

   .. code-block:: bash

      networkctl status

#. In the mixer workspace, edit `builder.conf` to set the value for
   CONTENTURL and VERSIONURL to the IP `Address` of your `nginx` server.    

   .. code-block:: bash

      nano builder.conf

      .. note:: 
            
         For example: 
         CONTNENTURL=http://192.168.25.52
         VERSIONURL=http://192.168.25.52

Create a workspace
******************

Use the following command to create an empty directory in your |CL| image to
use as a **workspace** for mixing:

.. code-block:: bash

    mkdir /home/clr/mix

This guide assumes your workspace location is :file:`/home/clr/mix`.

Generate the starting point for your mix
****************************************

In your workspace, initialize mixer with the following command:

.. code-block:: bash

   mixer init

This command initializes your workspace so you can make a mix at version 10
based on the latest released upstream |CL| version. If a :file:`builder.conf`
file is not already present in your workspace, mixer creates a default
configuration file. Additionally, mixer creates several version and tracking
files, and two bundle directories: :file:`local-bundles` and
:file:`upstream-bundles`.

If you wish to start with a different version of upstream |CL| or a
different initial mix version, you can specify these options as flags.
For example:

.. code-block:: bash

   mixer init --upstream-version 21060 --mix-version 10


Additionally, to build a mix with your own custom RPMs, use the optional
*--local-rpms* flag, for example:

.. code-block:: bash

   mixer init --local-rpms

This command creates the :file:`local-yum` and :file:`local-rpms`
directories in your mix workspace and adds their paths to the generated
:file:`builder.conf`. If the configuration file already exists, you must add
the paths manually. For more information on using these directories or
setting them up manually, see `Create or locate RPMs for the mix`_.

If all upstream |CL| bundles will be part of the mix, you can easily add 
them all during initialization with the optional *--all-upstream* flag. For example:

.. code-block:: bash

   mixer init --all-upstream

Finally, you may want to track the contents of your mixer workspace with a
git repository. This is a great way to track changes to your mix's content
or to revert to earlier versions if something goes wrong. Mixer can set this
up automatically with the optional *--git* flag, for example:

.. code-block:: bash

   mixer init --git

.. note::
   You can use any or all of the above optional flags at the same time, for example:

   .. code-block:: bash

      mixer init --upstream-version 21060 --mix-version 10 --local-rpms --all-upstream --git

Edit builder.conf
*****************

To configure the mixer tool, edit the :file:`builder.conf` as needed.

The file :file:`builder.conf` is read automatically from the current
workspace directory. Use the *--config* flag during initialization
to specify an alternate path to the file as needed.

The :file:`builder.conf` file has different sections, for example:

* The `[Builder]` section provides the mixer tools with the required
  configuration options. This section defines the path where the generated
  bundles and update metadata are published.

* The `[swupd]` section contains specific update parameters. The
  :abbr:`swupd-server (software update server)` creates an update using
  said specific update parameters.

Edit the configuration file according to your needs with the command:

.. code-block:: bash

   vim /home/clr/mix/builder.conf

Your version of the :file:`builder.conf` file should resemble the
following example:

.. code-block:: console

   #VERSION 1.0

   [Builder]
     CERT = "/home/clr/mix/Swupd_Root.pem"
     SERVER_STATE_DIR = "/home/clr/mix/update"
     VERSIONS_PATH = "/home/clr/mix"
     YUM_CONF = "/home/clr/mix/.yum-mix.conf"

   [Swupd]
     BUNDLE = "os-core-update"
     CONTENTURL = "<URL where the content will be hosted>"
     VERSIONURL = "<URL where the version of the mix will be hosted>"

   [Server]
     DEBUG_INFO_BANNED = "true"
     DEBUG_INFO_LIB = "/usr/lib/debug"
     DEBUG_INFO_SRC = "/usr/src/debug"

   [Mixer]
     LOCAL_BUNDLE_DIR = "/home/clr/mix/local-bundles"
     LOCAL_REPO_DIR = ""
     LOCAL_RPM_DIR = ""
     DOCKER_IMAGE_PATH = "clearlinux/mixer"

The following variables require further explanation:

* The `LOCAL_BUNDLE_DIR` variable sets the path where mixer stores the local
  bundle definition files. These bundle definition files include any new,
  original bundles you create, along with any edited versions of upstream
  |CL| bundles.

* The `SERVER_STATE_DIR` variable sets the path for the output of the mix
  content. Mixer automatically creates the path for you, but the path can be
  set to any location. In this example, we use the workspace directory.

* The `YUM_CONF` variable sets the path where mixer automatically generates
  the :file:`.yum-mix.conf` yum configuration file. The yum configuration 
  file points the chroot-builder to the path where the RPMs are stored.

* The `CERT` variable sets the path where mixer stores the
  :file:`Swupd_Root.pem` certificate file. The chroot-builder needs the
  certificate file to sign the root :file:`Manifest.MoM` file to provide
  security for content verification. The value of the `CERT` variable can
  point to a different certificate. The chroot-builder inserts the
  certificate specified in this value into the
  :file:`/os-core-update/usr/share/clear/update-ca/` path. The software 
  update client uses this certificate to verify the :file:`Manifest.MoM` 
  file's signature. For now, we **strongly** recommend that you do not modify
  this line, as the certificate that :abbr:`swupd (Software Updater)`
  expects needs to have a very specific configuration to sign and verify
  properly. Mixer automatically generates the certificate, if you do not
  provide the path to an existing one, and signs the :file:`Manifest.MoM`
  file to provide security for the updated content you create.

* The `CONTENTURL` and `VERSIONURL` variables set the domain or IP address
  where swupd looks for your update content and the corresponding version. 
  You must set these variables to the domain or IP-address of the server 
  hosting the update content. You can use any web server to host your update 
  content. To learn how to install and configure web server using |CL|, see 
  :ref:`create-nginx-web-server`. For our example, the web update content 
  within the `SERVER_STATE_DIR` directory is located here:
  :file:`/home/clr/mix/update/www`. If the web server is on the same machine 
  as this directory, you can create a symlink to the directory in your web
  server's document root to easily host the content. These URLs are
  embedded in images created for your mix. The `swupd-client` looks at
  these URLs to determine if a new version is available and the location
  from where to download the updated content. These links are equivalent
  to the |CL| `update page`_ but for the mix.

* The `VERSIONS_PATH` variable sets the path for the mix version and upstream
  |CL| version's two state files: :file:`mixversion` and
  :file:`upstreamversion`. Mixer creates both files for you when you set up
  the workspace.

* The `DOCKER_IMAGE_PATH` variable sets the base name of the docker image
  mixer will pull down in order to run builds in the proper container.

.. note:: If you are working only with |CL| bundles, then
   skip to `List, edit, create, add, remove, or validate bundles`_.


Create custom RPMs
******************

Create or locate RPMs for the mix
=================================

If you create RPMs from scratch, you can use `autospec`, `mock`, `rpmbuild`,
or similar tools to build them. If the RPMs are not built on |CL|, ensure
your configuration and toolchain builds them correctly for |CL|, or else
there is no guarantee they will be compatible. For more information on
building the RPMs properly, refer to our `build RPMs instructions`_.

Import RPMs into workspace
==========================

#. Create a :file:`local-rpms` directory in your workspace, for example,
   :file:`/home/clr/mix/local-rpms`.

#. Copy the RPMs into the directory you created.

#. Add the following line to your :file:`builder.conf` file:

   .. code-block:: console

      LOCAL_RPM_DIR=/home/clr/mix/local-rpms

Mixer uses this directory to find the RPMs to build a local RPM repo for
yum to use.

Create a local RPM repo
=======================

#. Create an empty directory in your workspace named :file:`local-yum`.
#. Add the path to your :file:`builder.conf` file:

   .. code-block:: console

      LOCAL_REPO_DIR=/home/clr/mix/local-yum

#. With these values configured, generate the yum repo with the following
   command:

   .. code-block:: bash

      mixer add-rpms

After the tool exits, you should see the RPMs and a repository data
directory in :file:`/home/clr/mix/local-yum`. If the RPMs are not all in this
:file:`local-yum` directory, check to ensure that the RPM files are valid
and not corrupt.

List, edit, create, add, remove, or validate bundles
****************************************************

The bundles in the mix are specified in the mix bundle list. Mixer stores
this list as a flat file called :file:`mixbundles` in the path set by the
`VERSIONS_PATH` variable of the :file:`builder.conf` file. Mixer
automatically generates the :file:`mixbundles` list file during
initialization. Mixer reads and writes the bundle list file when you change
the bundles of the mix.

List the bundles in the mix
===========================

To view the bundles already in the mix, enter the following command:

.. code-block:: bash

   mixer bundle list

This command shows a list of every bundle in the mix. Bundles can include
other bundles. Those nested bundles can themselves include other
bundles. When listing bundles with this command, mixer automatically
recurses through the includes to show every single bundle in the mix.

If you see an unexpected bundle in the list, that bundle is probably included
in another bundle. Use the *--tree* flag to get a better view of how
a bundle ended up in the mix, for example:

.. code-block:: bash

   mixer bundle list --tree

This command shows a visual representation of the inclusion relationships
between the bundles in the mix.

Bundles fall into two categories: **upstream** and **local**.

Upstream bundles are those provided by |CL|.

Mixer automatically downloads and caches upstream bundle definition files.
These definition files are stored in the :file:`upstream-bundles` directory
in the workspace. Do **not** modify the files in this directory. This
directory is simply a mirror for mixer to use.

The mixer tool automatically caches the bundles for the |CL| version
configured in the :file:`upstreamversion` file. Mixer also cleans up old
versions once they are no longer needed. You can see the available upstream
bundles with the following command:

.. code-block:: bash

   mixer bundle list upstream

Local bundles are bundles that you create, or are edited versions of upstream
bundles.

Local bundle definition files live in the :file:`local-bundles` directory.
The `LOCAL_BUNDLE_DIR` variable sets the path of this directory in your
:file:`builder.conf` configuration file. For this example, the path is
:file:`/home/clr/mix/local-bundles`. You can see the available local bundles
with the following command:

.. code-block:: bash

   mixer bundle list local

Both the local and upstream :command:`bundle list` commands accept the
*--tree* flag to show a visual representation of the inclusion relationships
between the bundles in the mix.

Edit the bundles in the mix
===========================

**Mixer always checks local bundles first and the upstream bundles second.**

Therefore, bundles in the :file:`local-bundles` directory always take
precedence over any upstream bundles that have the same name.

This precedence enables you to edit upstream bundles. The local, edited
version of the bundle overrides the bundle version found upstream.

For example, to edit the `bundle1` definition file, we use the following
command:

.. code-block:: bash

   mixer bundle edit bundle1

If `bundle1` is found in your local bundles, mixer edits this bundle
definition file. If instead `bundle1` is only found upstream, mixer copies
the bundle definition file from upstream into your :file:`local-bundles`
directory first.

In both cases, mixer launches your default editor to edit the file. When the
editor closes, mixer automatically validates the edited bundle file and
reports any errors found. If mixer finds an error, you can edit the file
as-is, revert and edit, or skip and move on to the next bundle. If you skip a
file, mixer saves a backup of the original file with the ``.orig`` suffix.
Because mixer always checks your local bundles first, edited copies of an
upstream bundle always take precedence over their upstream counterpart. You
can edit multiple bundles with the following command:

.. code-block:: bash

   mixer bundle edit bundle1 bundle2 [bundle3 ...]

Create bundles for the mix
==========================

To create a totally **new bundle**, the bundle name you specify cannot exist
upstream. If that is the case, create a :file:`new-bundle` with the following
command:

.. code-block:: bash

   mixer bundle edit new-bundle

This command generates a blank template in :file:`local-bundles` with the
:file:`new-bundle` filename. Mixer launches the editor for you to fill out
the bundle and performs validation when you exit the editor. Add your package
or packages to the bundle definition file to define the packages to install
as part of the bundle.

.. note::

   The :command:`mixer bundle edit` command accepts multiple bundles at once.
   Thus, you can create multiple new bundles in a single command, for 
   example:

   .. code-block:: bash

      mixer bundle edit new-bundle1 new-bundle2 [new-bundle3 ...]

Add bundles to the mix
======================

Add `bundle1` to your mix with the following command:

.. code-block:: bash

   mixer bundle add bundle1

This command adds the specified bundles to the mix bundles list stored in
your :file:`mixbundles` file. For each bundle you add, mixer checks your
local and upstream bundles to ensure the added bundles actually exist. If
mixer cannot find the bundle, it reports back an error. Additionally, when
mixer adds a bundle, it tells you whether the bundle is local or upstream.
Alternatively, you can learn this information with the
:command:`mixer bundle list` command. Refer to `List the bundles in the mix`_.

To add multiple bundles at once, use the following command:

.. code-block:: bash

   mixer bundle add bundle1 bundle2 [bundle3 ...]

Remove bundles from the mix
===========================

Remove `bundle1` from your mix with the following command:

.. code-block:: bash

   mixer bundle remove bundle1

This command removes `bundle1` from the mix bundle list stored in your
:file:`mixbundles` file. By default, this command does not remove the bundle
definition file from your local bundles. To completely remove a bundle,
including its local bundle definition file, use the following command with
the *--local* flag:

.. code-block:: bash

   mixer bundle remove --local bundle1

By default, removing a local bundle file with this command removes the bundle
from the mix as well. To only remove the local bundle definition file, use
the following command with the *--mix=false* flag:

.. code-block:: bash

   mixer bundle remove --local --mix=false bundle1

If you remove a local, edited version of an upstream bundle and keep the
bundle in the mix, the mix then references the original upstream version of
the bundle.

On the other hand, if you remove a bundle that is only found locally but
keep the bundle in the mix bundles list, mixer will not find a valid
bundle definition file and will produce an error.

Validate the bundles in the mix
===============================

Mixer performs basic validation on all bundles when used throughout the
system.

Mixer checks the validity of the bundle's syntax and name. Optionally, you 
can run this validation manually on `bundle1` with the following command:

.. code-block:: bash

   mixer bundle validate bundle1

.. note:: This command can be useful in many circumstances. One example is
   when importing already-existing local bundles from other projects.

If you use the optional *--strict* flag, the command additionally
checks if the rest of the bundle header fields can be parsed, if the bundle
header fields are non-empty, and if the bundle header ``Title`` field and
the bundle filename match. Perform a strict validation of `bundle1` with the
following command:

.. code-block:: bash

   mixer bundle validate --strict bundle1

Validate multiple bundles with the following command:

.. code-block:: bash

   mixer bundle validate bundle1 bundle2 [bundle3 ...]

Managing bundles with Git
=========================

If you initialized your workspace to be tracked as a git repository
with the :command:`mixer init --git` command, it might be useful to apply a
git commit after you modify the mix bundle list or edit a bundle definition
file.

All the :command:`mixer bundle` commands in the previous sections support an
optional *--git* flag. This flag automatically applies a git commit
when the command completes, for example:

.. code-block:: bash

   mixer bundle remove --git bundle1

Build the bundle chroots
************************

To build all the ``chroots`` based on the defined bundles, use the following
command in your workspace:

.. code-block:: bash

   mixer build bundles 

If the mix has many bundles, this step might take some time.

Mixer automatically gathers the bundle definition files for the upstream
bundles into a :file:`upstream-bundles` directory, and user bundles should
be placed directly into :file:`local-bundles`. The local path is set in
the `LOCAL_BUNDLE_DIR` variable in the :file:`builder.conf`. **Do not edit
files in upstream-bundles.** Mixer automatically deletes the contents of
the :file:`upstream-bundles` directory before repopulating the directory
on-the-fly if a new version must be downloaded.


Create an update
****************

Create an update with the following command:

.. code-block:: bash

   mixer build update

When the build completes, you can find the mix update content under
:file:`/home/clr/mix/update/www/VER`. In our example, the update content is
found in :file:`/home/clr/mix/update/www/{<MIXVERSION>}`. `<MIXVERSION>`
is the defined mix version, which is 10 by default.

.. code-block:: bash

   mixer build update 

Mixer creates all the content needed to make a fully usable mix with this
step. However, only *zero packs* are automatically generated. Zero packs are
the content needed to go from nothing to the mix version for which you just
built the content.

You can create optional *delta packs*, which allow the transition from one
mix version to another, with the following command:

.. code-block:: bash

   mixer build delta-packs --to <MIX_VERSION> --from <PAST_VERSION>

This command generates all delta packs for the bundles changed from
`PAST_VERSION` to `MIX_VERSION`. Mixer cannot create delta packs for the
first build because the update is from version 0. Version 0 implicitly has
no content, thus mixer can generate no deltas.

For subsequent builds, you can run :file:`mixer-pack-maker.sh` to generate
delta content between them, for example: 10 to 20.

Create an image
*****************

Since mixer uses the `ister` tool to create a bootable image from your
updated content, we must first configure the `ister` tool. To configure the
image `ister` creates, we need the `ister` configuration file. Obtain a copy
with the default values from the `ister` package with the following command:

.. code-block:: bash

   sudo cp /usr/share/defaults/ister/ister.json release-image-config.json

For reference, you can inspect the `Clear Linux ister configuration file`_
used for releases.

Edit the configuration file to include all bundles you want *preinstalled* in
the image. Users can install the bundles in the mix that are not included in
the configuration file with the following command:

.. code-block:: bash

   sudo swupd bundle-add bundle1

Keeping the list of bundles in the configuration file small allows for a
smaller image size. For the minimal base image, the list is:

.. code-block:: console

   "Bundles": ["os-core", "os-core-update", "kernel-native"]

Next, set the `Version` field to the mix version that you want the content
mixer to use to build the image. `ister` allows you to build an image from
any mix version that you have built, not just from the current version. In
our example so far, `Version` is set to 10.

With the `ister` tool configured, build the image with the following command:

.. code-block:: bash

   sudo mixer build image

Mixer automatically looks for the :file:`release-image-config.json` file, but
you can freely choose the filename. To use a different name, simply pass the
*--template* flag when creating your image, for example:

.. code-block:: bash

   sudo mixer build image --template path/to/file.config

By default, `ister` uses the format version of the build machine it runs on.
Therefore, if the format you are building differs from the format of the |CL|
OS you are building on, you must use the *--format <FORMAT_NUMBER>*
flag. Find the current format version of your OS with the following command:

.. code-block:: bash

   sudo cat /usr/share/defaults/swupd/format

Update the next mix version information
***************************************

Increment the mix version number for the next mix with the following command:

.. code-block:: bash

   mixer versions update

This command automatically updates the mix version stored in the
:file:`mixversion` file, incrementing it by 10. To increment by a different
amount, use the *--increment* flag, for example:

.. code-block:: bash

   mixer versions update --increment 10

Alternatively, to set the mix version to a specific value, use the
*--mix-version* flag, for example:

.. code-block:: bash

   mixer versions update --mix-version 20

The :command:`mixer versions update` command does not allow you to set the
mix version to a value less than its current value. The mix version is
expected to always increase, even if the new mix is undoing an earlier
change.

If you have been tracking your workspace with git, you can restore the mix to
an earlier state. However, be careful when "rewriting history" if you have
published the mix content to users already.

Use the following command with the the *--upstream-version* flag to
update the upstream version of |CL| used as a base for the mix:

.. code-block:: bash

   mixer versions update --upstream-version 21070

This command also accepts the keyword "latest":

.. code-block:: bash

   mixer versions update --upstream-version latest

This command sets the upstream version to the latest released version of
upstream |CL| within the same format version. The
:command:`mixer versions update` command does not allow you to set an
upstream version to a value that crosses an upstream format boundary.
Such values require a "format bump" build, which is currently a
manual process. Refer to :ref:`mixer-format` for more information.

Optionally, you can learn which mix version or upstream version you are
currently using with the following command:

.. code-block:: bash

   mixer versions

At this point, you can continue to iterate through the workflows and make
modifications as needed, for example:

#. Add, remove, or modify bundles.
#. Build the chroots with:

   .. code-block:: bash

      mixer build chroots

#. Build and update with:

   .. code-block:: bash

      mixer build update

#. Optionally, you can create delta packs with:

   .. code-block:: bash

      mixer build delta-packs --to <NEWVERSION> --from <PREV_VERSION>

.. _mixer-format:

Format version
**************

The `Format` variable set in the :file:`builder.conf` file can be more
precisely referred to as an OS *compatibility epoch*. Versions of the OS
within a given epoch are fully compatible and can update to any other
version within that epoch. Across the `Format` boundary, the OS has changed
in such a way that updating from build M in format X, to build N in format Y
will not work. Generally, this scenario occurs when the software updater or
software manifests change in a way that they are no longer compatible with
the previous update scheme.

Using a format increment, we insure pre- and co-requisite changes flow out
with proper ordering. The updated client only ever updates to the latest
release in its respective format version, unless overridden by command line
flags. Thus, we can guarantee that all clients update to the final version
in their given format. The given format *must* contain all the changes
needed to understand the content built in the subsequent format. Only after
reaching the final release in the old format can a client continue to update
to releases in the new format.

When creating a custom mix, the format version should start at "1" or some
known number such as the host system format. The format version should
increment only when a compatibility breakage is introduced. Normal updates,
like updating a software package for example, do not require a format
increment.

.. _update page: https://cdn.download.clearlinux.org/update/

.. _format bumps wiki: https://github.com/clearlinux/swupd-server/wiki/Format-Bumps

.. _build RPMs instructions: https://github.com/clearlinux/common#build-rpms-for-a-package

.. _Clear Linux ister configuration file:
   https://raw.githubusercontent.com/bryteise/ister/master/release-image-config.json
