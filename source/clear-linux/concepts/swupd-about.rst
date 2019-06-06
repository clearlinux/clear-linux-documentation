.. _swupd-about:

swupd: software updater
#######################

:command:`swupd` is an operating system software manager and update program
that operates at a file-level to enable verifiable integrity and update
efficiency.

Visit the `swupd man page`_ for more details.

Versioning
==========

Using package managers to keep track of software version compatibility or compare multiple systems on many Linux distributions can be cumbersome.

With |CL| :command:`swupd`, versioning happens at the individual
file-level. This means |CL| generates an entirely new OS version with any set
of software changes to the system (including software downgrades or removals). This rolling release versioning model is similar to
:command:`git` internal version tracking, where any of the individual file
commits are tracked and move the pointer forward when changed.

While administrators can pick and choose which `bundles`_ a system has
installed, a single |CL| version number strictly represents one combination
of all software versions that can be installed onto a system of that |CL|
version. This method of whole OS versioning offers unique advantages.
Namely, system administrators can quickly compare multiple |CL| systems that share the same version for important software and security fixes.


Updating
========

|CL| promotes regular and automated updating of software to ensure
integration of new enhancements and security fixes. Refer to :ref:`security`
documentation for more information.

Learn how to update your system using :ref:`swupd <swupd-guide>`.

Update efficiency
-----------------

Because :command:`swupd` operates at the individual file-level instead of a
package-level, |CL| updates are small and fast.

On many Linux\* distributions, updates to a particular software package
require the whole software package to be downloaded and replaced
--even for one line of code.

In |CL|, updates are generated using the :ref:`mixer <mixer-about>` tool. Mixer calculates the difference between two |CL| versions and makes available
*binary deltas*, which contain only the changed portion of files. This
*binary delta technology* [1]_ means :command:`swupd` on |CL| systems only
needs to download and apply a small fraction of a package in order to
receive an update.

The :ref:`mixer <mixer-about>` tool additionally computes updates files in
multiple compression formats, allowing :command:`swupd` to utilize the most
efficiently compressed format for a |CL| system to minimize the cost
to update.

Update integrity
----------------

:command:`swupd` operates against a published manifest of files for a
particular |CL| version that contains the unique hash of each file. This is
the basis of the :command:`swupd diagnose` subcommand, which allows a |CL|
system to check for and remediate any discrepancies to system files. As
necessary, :command:`swupd diagnose` provides a useful way for software
developers to return to a known filesystem state.

Bundles
=======

|CL-ATTR| approaches software management differently than many other
Linux-based operating systems.

Instead of deploying granular software packages, |CL| uses the concept of
bundles with pre-associated software. Each bundle encapsulates a particular
use-case, which is enabled by composing all the required upstream open-source
projects and packages into one logical unit.

This bundle-based approach offers some unique advantages:

* Bundles provide a particular functionality, or stack, which
  include all associated runtime dependencies.

* Software package dependencies are resolved on the server, so file-level
  conflicts do not occur on the target system after an update.

* All combinations of bundles are able to co-exist on a |CL| system.

For more information on bundles, visit:

* :ref:`bundles`
* :ref:`bundles-about`
* :ref:`bundle-commands`
* :ref:`compatible-kernels`

.. [1] The software update technology for |CL-ATTR| was first presented at the Linux Plumbers conference in 2012.

.. _swupd man page: https://github.com/clearlinux/swupd-client/blob/master/docs/swupd.1.rst

