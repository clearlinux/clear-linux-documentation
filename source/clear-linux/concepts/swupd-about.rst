.. _swupd-about:

swupd (Software Updater)
########################

:command:`swupd` is an operating system software manager and update program
that operates at a file-level. |CL| leverages :command:`swupd` to allow
software under :file:`/usr` (see `Stateless`_) to be installed with verifiable
integrity and updated efficiently. 

Visit the `swupd man page`_ for more details.



Versioning
==========

With |CL| and :command:`swupd`, versioning happens at the individual
file-level. This means |CL| generates an entirely new OS version with any set
of software changes to the system (including software downgrades or removals).
This type of rolling versioning can be thought of similar to the
:command:`git` internal version tracking, where any of the individual file
commits are tracked and move the pointer forward when changed.

While administrators can pick and choose which `bundles`_ a system has
installed, a single |CL| version number is powerful enough to represent
strictly one possible combination of all software versions that can be
installed onto a system of that |CL| version.This method of whole OS
versioning offers some unique advantages. Namely, system administrators can
quickly compare multiple |CL| systems for important software and security
fixes.

While the process of describing installed software on other Linux\*
distributions can be done with package managers, it can still be cumbersome to
keep track of dissociated software version compatibility or to compare
multiple systems. 



Updating
========

|CL| promotes regular and automated updating of software to reap the benefits
of new enhancements and security fixes. Refer to :ref:`security` documentation
for more information.

Learn how to update your system using :ref:`swupd <swupd-guide>`.


Update efficiency 
-----------------

Because :command:`swupd` operates at the individual file-level instead of a
package-level, |CL| updates are able to be small and fast. 

|CL| updates are generated using the :ref:`mixer <mixer-about>` tool. Mixer
calculates the difference between two |CL| versions and makes available
*binary deltas*, which contain only the changed portion of files. This *binary
delta technology* [1]_ means :command:`swupd` on |CL| systems only needs to
download and apply a small fraction of a package in order to receive an
update.


While similar update technologies exist, they are seldomly used in practice.
In other Linux\* distributions, updates to a particular software package
typically results in the whole software package being downloaded again and
replaced on the system - even when the net change is just one line of code. 

The :ref:`mixer <mixer-about>` tool additionally computes updates files in
multiple compression formats, allowing :command:`swupd` to utilize the most
efficiently compressed format for a |CL| system in order to minimize the cost
to update.


Update integrity 
----------------

:command:`swupd` operates against a published manifest of files for a
particular |CL| version that contains the unique hash of each file. This is
the basis of the :command:`swupd verify` subcommand which allows a |CL| system
to check for, and remediate, any discrepancies to system files. The
:command:`swupd verify` can be especially useful for software developers to
return to a known filesystem state.



Bundles
=======

|CL-ATTR| approaches software management differently than other distributions
of Linux-based operating systems. 

Instead of deploying granular software packages, |CL| uses the concept of
bundles with pre-associated software. Each bundle encapsulates a particular
use-case, which is enabled by composing all the required upstream open-source
projects and packages into one logical unit. 

This bundle-based approach offers some unique advantages.

- Installing software for a particular functionality will come "bundled" with 
  all of its runtime dependencies, avoiding a situation where you have to hunt
  them down.
- Software package dependencies are resolved before the updates comes to |CL| 
  systems, meaning file-level conflicts will not occur due to an update. 
- All combinations of bundles are able to co-exist on a |CL| system.

For more information on bundles, visit:

* :ref:`bundles`
* :ref:`bundles-about`
* :ref:`bundle-commands`
* :ref:`compatible-kernels`



.. [1] The software update technology for |CL-ATTR| was first presented at the Linux Plumbers conference in 2012.

.. _Stateless: https://clearlinux.org/features/stateless
.. _swupd man page: https://github.com/clearlinux/swupd-client/blob/master/docs/swupd.1.rst