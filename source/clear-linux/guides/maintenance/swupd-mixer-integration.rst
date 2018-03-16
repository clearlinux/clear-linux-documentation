.. _swupd-mixer-integration:

Mixer tool enhancement
######################

Mixing means composing an operating system for a specific use case. The
default build of |CLOSIA| provides options to install bundles for various
server capabilities. If you want to supplement the default OS with
functionality from other OS distributions, you can manually compose an OS
using :ref:`the mixer tool <mixer>`.

Software updater release 19900 integrates the mixer tool with the
updater (:command:`swupd`) and provides a simpler way to mix your OS.

Process overview
****************

To add a package that does not exist in the current |CL| bundle, perform the following:

#. Create custom packages and bundles using the :file:`swupd-add-pkg` script.

#. Add your desired content with the commands:

   .. code-block:: bash

      sudo swupd update
      sudo swupd bundle-add <new_bundle>

The upstream content is pulled from the normal URL and local content is added
from a local update store.

.. note::

   The integrated mixer tool adds non-unique packages and replaces upstream
   content with a local version. However, the updater exits if it finds
   conflicts before creating the local content. You can override this behavior
   by passing the :command:`--allow-mix-collisions` option.


Prerequisites
*************

To use the integrated swupd mixer, you need a recent image of
|CLOSIA| with the mixer bundle installed. If you do not have it already,
add it with the :command:`swupd bundle-add` command as shown below:

.. code-block:: bash

   sudo swupd bundle-add mixer


Using the enhanced swupd mixer
******************************

Perform the following steps:

#. Create a folder :file:`/usr/share/mix/rpms` for the local update content
   and copy the desired RPM into the folder:

   .. note::

     The RPM must be formatted and built for |CL|.

   .. code-block:: bash

      sudo cp RPM /usr/share/mix/rpms/

#. Add RPM and create content.

   .. code-block:: bash

      sudo swupd-add-pkg RPM <bundle_name>

   The :file:`swupd-add-pkg` script creates the :command:`<bundle_name>`
   bundle if it does not exist, adds the RPM to it, and generates the
   required mixer content and manifests.

#. Use the new :command:`--migrate` flag to let :command:`swupd` know that
   local content exists.

   .. code-block:: bash

      sudo swupd update --migrate

   When complete, your system is in the mix-ready state using the new
   Manifest.MoM.

#. Add your bundle to your system:

   .. code-block:: bash

      sudo swupd bundle-add <bundle_name>


Reverting to the upstream version
*********************************

You can return your OS to an official upstream version with no user-added
content using the following command:

   .. code-block:: bash

      sudo swupd verify --fix --picky --force -m <upstreamversion> -C
      /usr/share/clear/update-ca/Swupd_Root.pem

   .. note::

      The options used in the example delete the :file:`/usr/share/mix` folder, and all other extraneous data on your system that is not part of <upstreamversion>.


swupd operational details
*************************

From a user perspective, swupd operates the same as before and now supports
multiple sources for content. The tasks described below are done without any
extra flags or configurations needed.

Software updater release 19900 checks for content in :file:`/usr/share/mix`.
If content exists, then the updater knows user content must be incorporated
into the updater commands.

Internally, :command:`swupd` performs the following operations:

*  Retrieves the upstream manifests and content.

   .. note::

      Upstream Manifest.MoMs are signature-verified for security and accuracy.

*  Retrieves local content.

The :command:`swupd-add-pkg` script performs the following:

*  Executes the necessary mixer commands and bookkeeping tasks to create a
   minimal mix. This mix contains only the new user bundle and os-core which
   tracks version and timestamp changes.

*  Verifies and merges the upstream Manifest.MoM with the local
   Manifest.MoM.

*  Signs the resulting merged Manifest.MoM with the user's certificate.

Ongoing updates
===============

To simplify tracking of the base OS version, :command:`swupd` modifies the OS
version by multiplying by 1000. For example, if the base OS version was 18220,
after running the :command:`swupd-add-pkg` script, the OS version is
identified as 18220000. If :command:`swupd` finds an OS version greater than
18220 during regular checks, :command:`swupd` automatically generates a new
Manifest.MoM in the next update operation.

Security updates are handled per the normal update schedule. For tracking, a
mixed file exists at :file:`/usr/share/defaults/swupd/mixed` signifying that
the system is on an augmented OS version.
