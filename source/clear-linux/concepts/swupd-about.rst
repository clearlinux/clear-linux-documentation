.. _swupd-about:

Software update
###############

|CLOSIA| does software updates differently than traditional Linux-based 
operating systems. Where traditional distributions rely on packages for 
software deployment, |CL| uses the concept of a "bundle" for 
deployment. Traditional Linux packages provide a particular utility or 
library; |CL| bundles provide all necessary packages to enable a 
specific function.

With |CL|, updating equates to an entirely new OS version with a 
specific set of bundles, as compared to a package-based distribution in 
which packages may be updated individually. |CL| updates are 
efficient, updating only changed files instead of entire packages.

System administrators can customize or add bundles to the OS, while still 
taking advantage of a controlled update stream. This enables system 
administrators to focus on the pieces that make their deployment unique.


Bundles
=======

While we use packages to manage compiling source code into installable 
binaries, we do not deploy software through packages. Instead, we use bundles 
to deploy software, where each bundle encapsulates a particular functionality 
-- functionality that is enabled by composing all the required upstream 
open-source projects and packages into one logical unit: a bundle. This 
simplifies installing features on |CL|.

For additional resources regarding available bundles, useful bundle commands, 
and compatible |CL| kernels, visit our :ref:`bundles-about` 
page.


Versioning
==========

In a traditional distribution, the process of describing current software
versioning usually involves:

-  Listing and keeping track of the current OS release (generally
   uninformative about any singular packages or functionality).

-  Keeping track of packages and repositories being used, and updating them
   individually.

-  Listing and tracking every package available and installed on the
   system, none of which are directly tied to the current OS release.

This can be done effectively, but given the nearly endless combinations of
packages and versions of packages a server may have, it quickly becomes
non-trivial to define what "version" the system is and what software it
is running without explicitly going through each system and inspecting
every package.

With |CL|, we need only track:

-  One single number

A number representing the **current** release of the OS is sufficient to
describe the versions of all the software on the OS. Each build is
composed of a specific set of bundles made from a particular version of
packages. This matters on a daily basis to system administrators, who
need to determine which of their systems do not have the latest security
fixes, or which combinations of software have been tested. Every release 
of the same number is guaranteed to contain the same versions of software, 
so there's no ambiguity between two systems running the same version of |CL|.


Updating
========

Another notable difference between package-based distributions and |CL|
is how updates are managed. On a package-based OS, system administrators update
each individual package or piece of software to a newer (or older!) version. With
|CL|, an update translates to an entirely new OS version, containing one 
or many updates.  It is not possible to update a piece of the system while 
remaining on the same version of |CL|.

How is this useful? Although it seems, at first, like a huge restriction
or limitation, this method has many non-obvious benefits. Imagine a
cloud environment composed of numerous machines.  Here, a homogeneous set of
software makes sense -- from the system administrator's level down to the
user level. Homogeneous systems allow users to focus on their contributions 
and/or code, rather than configuring environments or worrying about 
synchronizing versions and updates.  At the system admin level, it ensures 
security is tighter and makes it far easier to monitor and update patches.

|CL| promotes regular updating of the OS and will automatically check 
for updates and apply them by default.

To learn how to run an update of your system, visit our :ref:`swupd-guide` page.


Update speed
============

Software updates with |CL| are also efficient. Bundles simply describe 
a set of files, and the update technology updates *only* files that actually 
changed by using binary-delta technology for efficiency [1]_. Operating systems 
that use packages as the unit of deployment require full package updates (thus
hogging resources), even when one small file in that package has changed.

It is quite common for a full OS update fixing a security hole to be
only 15 kilobytes in total update size. If only several kilobytes need
to be changed, it does not make sense to re-download and reinstall an
entire package or suite of programs just to incorporate a minuscule (yet
important) update. Through binary deltas, the OS is able to update only
those bits that changed, yielding very small update content (deltas)
that can be applied exceedingly fast.  As a result, major security patches
and core update take merely seconds.


Customize the OS
================

While we realize our definition of bundles makes sense to us, data center
operators may have special needs and ideas. Therefore, we provide a
:ref:`mixer tool <mixer>`. This tool allows users to customize and add bundles
or even add their own software, while keeping the operating
system and its updates as the basis. Using this tool, system administrators
can focus on the customization their deployments require while staying on
a controlled update stream.

To learn more about mixing, visit our :ref:`mixer-about` page.


.. [1] The software update technology for |CLOSIA| was first presented at the 
   Linux Plumbers conference in 2012.
