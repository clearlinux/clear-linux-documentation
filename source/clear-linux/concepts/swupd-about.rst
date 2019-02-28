.. _swupd-about:

Software update
###############

swupd is an OS-level software update program that applies updates to a
|CL-ATTR| or derivative.

While traditional Linux\*-based distributions rely on packages for software
deployment, |CL-ATTR| uses bundles. In a traditional Linux\* distro,
packages provide a particular utility or library and are updated
individually. In contrast, the |CL| update process equates to installing an
entirely new OS version with a specific set of bundles. Extremely efficient,
updates only change files instead of entire packages.

Visit the `swupd man page`_ for more details.

Bundles
=======

While |CL| uses packages to manage compiling source code into installable binaries, it does not deploy software through packages. Instead, |CL| uses bundles to deploy software. Each bundle encapsulates a particular functionality, which is enabled by composing all the required upstream open-source projects and packages into one logical unit. This simplifies installing features on the OS. For more resources, visit:

* :ref:`bundles`
* :ref:`bundles-about`
* :ref:`bundle commands`
* :ref:`compatible-kernels`


Versioning
==========

In a traditional Linux\* distro, describing current software versioning
involves keeping track of the current OS release and keeping track of the
packages while individually updating them. Packages are not directly tied
to the current OS release.

In |CL|, one single number represents the **current** release of the OS.
This number describes the versions of **all** the software on the OS. Each
release is composed of a specific set of bundles made from a particular
version of packages. This process offers other distinct advantages. System
administrators can be assured that all systems benefit from the latest
security fixes, all combinations of software have been tested, and all
package conflicts are resolved at build time. Further, every release--and by extension every target OS--that shares the same number is guaranteed to have the same versions of software.

Updating
========

|CL| promotes regular updating of the OS, automatically checking
for updates, and applying them by default. On a package-based OS, system
administrators update each individual package or piece of software. In |CL|
an update translates to an entirely new OS version, containing one or many
updates. It is not possible to update a piece of the system while remaining
on the same version of |CL|.

While this may seem like a limitation, the method has several benefits:

* In a cloud environment, |CL| allows you to run the exact same software
  for all container hosts in a cluster.

* |CL| intends to help developers create custom |CL| derivatives. Using
  :ref:`mixer <mixer>`, system administrators can focus on customizing their deployments while staying on a controlled update stream.

* Regular updates ensure :ref:`security` is tighter, so it is
  much easier to monitor and update patches.

Learn how to update your system using :ref:`swupd <swupd-guide>`.

Update speed
------------

Software updates with |CL| are also efficient. Whereas an OS that uses
packages requires full package updates, bundles simply describe
a set of files, and updates are made *only* to files that actually
changed by using binary-delta technology [1]_. With this method, the OS
updates only those bits that changed, yielding very small update content (
deltas) that are applied exceedingly fast. Major security patches and core update take merely seconds.

.. [1] The software update technology for |CL-ATTR| was first presented at the Linux Plumbers conference in 2012.

.. _swupd man page: https://github.com/clearlinux/swupd-client/blob/master/docs/swupd.1.rst