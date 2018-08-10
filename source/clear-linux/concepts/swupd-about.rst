.. _swupd-about:

Software update
###############

Clear Linux OS for Intel® Architecture does software updates differently than traditional Linux-based operating systems. Where traditional distributions rely on packages for software deployment, Clear Linux uses the concept of a bundle for deployment. Traditional Linux packages provide a particular utility or library, whereas Clear Linux bundles provide a specific function and include all necessary dependencies and packages.

With Clear Linux, updating equates to an entirely new OS version with a specific set of bundles, as compared to a package-based distribution in which packages may be updated individually. Clear Linux updates are efficient, updating only changed files instead of entire packages.

System administrators can customize or add bundles to the OS, while still taking advantage of a controlled update stream. This enables system administrators to focus on the pieces that make their deployment unique.


Bundles
=======

While we use the concept of "packages" to manage compiling source code into
installable binaries, we do not deploy software through packages. Instead,
we provide "bundles" which operate as a self-contained set of functionality
for the system administrator -- functionality that gets enabled by composing
all the required upstream open-source projects into one logical unit: a
bundle.

For additional resources regarding available bundles, useful bundle commands, and compatible Clear Linux kernels, visit our :ref:`Bundles <bundles-about>` page.


Versioning
==========

In a traditional distribution, the process of describing current software
versioning usually involves:

-  Listing and keeping track of the current OS release (generally
   uninformative about any singular packages or functionality),

-  Keeping track of packages and repositories being used, updating them
   individually,

-  Listing and tracking every package available and installed on the
   system, none of which are directly tied to the current OS release

This can be done effectively, but given the nearly endless combinations of
packages and versions of packages a server may have, it quickly becomes
non-trivial to define what "version" the system is and what software it
is running without explicitly going through each system and inspecting
every package.

With the Clear Linux OS for Intel Architecture, we need only track:

-  One single number

A number representing the **current** release of the OS is sufficient to
describe the versions of all the software on the OS. Each build is
composed of a specific set of bundles made from a particular version of
packages. This matters on a daily basis to system administrators, who
need to determine which of their systems do not have the latest security
fixes, or which combinations of software have been tested, and on what
other pieces. Every release of the same number is guaranteed to contain
the same versions of software, so there's no ambiguity between two
systems running the same Clear Linux OS for Intel Architecture.


Updating
========

Another notable difference between package-based distributions and Clear Linux
is how updates are managed. On a package-based OS, system administrators update
each individual package or piece of software to a newer (or older!) version. With
Clear Linux OS for Intel Architecture, an update translates to an entirely new
OS version, containing one or many updates.  It is not possible to update a
piece of the system while remaining on the same version of Clear Linux.

How is this useful? Although it seems, at first, like a huge restriction
or limitation, this method has many non-obvious benefits. Imagine a
cloud environment composed of numerous machines.  Here, a homogeneous set of
software makes sense -- from the system administrator's level down to the
user level. Homogeneous systems allow users the ability to focus on their
contributions and/or code, rather than configuring environments or worrying
about synchronizing versions and updates.  At the system admin level, it
ensures security is tighter and makes it far easier to monitor and update
patches.

Clear Linux OS will automatically check for updates and apply them. This default
can be disabled by running::

    # swupd autoupdate --disable

And reenabled by running::

    # swupd autoupdate --enable

To learn how to run an update of your system, visit our :ref:`Use swupd <swupd-guide>` page.

Update speed
============

Software updates with Clear Linux OS for Intel Architecture are also
efficient. Bundles simply describe a set of files, and the update
technology updates *only* files that actually changed by using
binary-delta technology for efficiency [1]_. Operating systems that use
packages as the unit of deployment require full package updates (thus
hogging resources), even when one small file in that package has changed.

It is quite common for a full OS update fixing a security hole to be
only 15 kilobytes in total update size. If only several kilobytes need
to be changed, it does not make sense to re-download and reinstall an
entire package or suite of programs just to incorporate a minuscule (yet
important) update. Through binary deltas, the OS is able to update only
those bits that changed, yielding very small update content (deltas)
that can be applied exceedingly fast.  As a result, major security patches
and core update take merely seconds.

While we realize our definition of bundles makes sense to us, data center
operators may have special needs and ideas. Therefore, we provide a
:ref:`mixer tool <mixer>`. This tool allows users to customize and add bundles
or even add their own software, while keeping the operating
system and its updates as the basis. Using this tool, system administrators
can focus on the custom pieces their deployments require while staying on
a controlled update stream.



.. [1] The software update technology for Clear Linux* OS for Intel
   Architecture was first presented at the Linux Plumbers conference in 2012.
