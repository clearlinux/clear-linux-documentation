Linux\*-based operating systems contain the code of several hundred, if
not thousands, of open source projects. To make this manageable,
distributions use a concept called "packages" to configure and compile
the source code of these projects into binaries, which can then be
logically installed.

Many distributions then combine these compiled binaries into so-called
packages, resolving dependencies and providing everything needed to
install. This is the granularity at which typical distributions deploy
their software, enabling system administrators to install and update
each package individually or as a set, using tools such as "yum" and
"apt-get."

The Clear way
-------------

The Clear Linux OS for Intel(r) Architecture does things a bit
differently. While we use the concept of packages to manage compiling
source code into installable binaries, we do not deploy software through
packages as many distributions do. Instead, we provide "bundles" that
each contain a set of functionality for the system
administrator--functionality that is enabled by composing all the
required upstream open source projects into one logical unit: a bundle.

There is another notable difference between package-based distributions
and the Clear Linux OS for Intel Architecture. On a package-based OS, a
system administrator can update each individual package or piece of
software to a newer (or older!) version. In the Clear Linux OS for Intel
Architecture, an update translates to an entirely new OS version,
containing one or many updates; it is not possible to update a piece of
the system while remaining on the same version of Clear Linux.

Why would you want this? This may sound like a huge restriction or
limitation at first, but we consider this a great feature. Imagine a
cloud environment with many machines. In this case, it is desirable and
more advantageous to have a homogeneous set of software.

With traditional distributions, to describe what version of software a
server is running, one might need to:

-  List and keep track of the current OS release (generally
   uninformative about any singular packages or functionality)

-  Keep track of all packages and repositories used, updating those as
   required to keep up to date

-  List and keep track of every package available and installed on the
   system, none of which are directly tied to the current OS release

This is done very well, but given the nearly endless combinations of
packages and versions of packages a server may have, it quickly becomes
non-trivial to define what "version" the system is and what software it
is running without explicitly going through each system and inspecting
every package.

With the Clear Linux OS for Intel Architecture, we must keep track of:

-  One single number

That number represents the current OS release, and it is sufficient to
describe the versions of all the software on the OS. Each build is
composed of a specific set of bundles made from a particular version of
packages. This matters on a daily basis to system administrators, who
need to determine which of their systems do not have the latest security
fixes, or which combinations of software have been tested with which
other pieces. Every release of the same number is guaranteed to contain
the same versions of software, so there is no ambiguity between two
systems running the same Clear Linux OS for Intel Architecture.

Incredible update speeds
------------------------

Software updates with Clear Linux OS for Intel Architecture are also
efficient; bundles are only describing a set of files, and the update
technology only updates files that actually changed, using so-called
binary-delta technology for efficiency. Updating using this method is
different from operating systems that use packages as the unit of
deployment. In those operating systems, the entire package gets updated
when needed, even if only one small file in that package has changed.

It is quite common for a full OS update fixing a security hole to be
only 15 kilobytes in total update size. If only several kilobytes need
to be changed, it does not make sense to re-download and reinstall an
entire package or suite of programs just to incorporate a miniscule (yet
important) update. Through binary deltas, the OS is able to update only
those bits that changed, yielding very small update content (deltas)
that can be applied exceedingly fast. One can then expect a major
security patch or core update to take seconds.

We realize that while our definition of bundles makes sense to us, each
data center operator may have special needs and ideas. For that reason
we are working on completing a "mixer" tool, which would allow users of
Clear Linux OS for Intel Architecture to customize and add bundles and
their own software while still using the content of the operating
system, and its updates, as the base. This way system administrators can
focus on the pieces of their OS deployment that are custom to their
environment, while continuing to stay on a controlled update stream.

[The software update technology in Clear Linux OS for Intel Architecture
was first presented at the Linux Plumbers conference in 2012.]

 
