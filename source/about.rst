.. _about:

About
#####

|CL-ATTR| does things differently. Our software architecture provides a 
unique and innovative platform for Linux* developers focused on
performance, security, and cutting-edge computation in the cloud. 

.. contents::
   :local:
   :depth: 1


What is |CL|?
*************

|CL| is an open source, rolling-release Linux* distribution, optimized for 
performance and security from the cloud to the Edge.  With an emphasis on 
customization and manageability, |CL| provides an industry blueprint on how 
to incorporate Intel® architecture, from leveraging instruction sets to 
optimizing kernel configurations and compiler flags, so tuning across the stack coalesces in a single, performance-driven development environment. 

What |CL| isn't?
****************

|CL| is not intended to be a general-purpose Linux distribution, suitable 
for novice end-users. While we ship common applications, our purpose isn’t 
to make an OS for routine desktop tasks and provide immunity from all 
security threats in all situations. Our unique focus means what we consider 
*essential* use cases, *optional* use cases, or even *unwanted* use cases, 
differs from other Linux distros.

Target audience
***************

Rather than making a standard Linux distribution, the |CL| team decided to
build its own. |CL| mainly targets professionals in IT, DevOps, Cloud/
Container deployments, and :abbr:`AI (Artifical Intelligence)`. 

One advantage of developing a distro in house is that our experiments help us
continually optimize performance and deliver security patches, several times
per week. Yet our experiments are only valuable if our software architecture 
gives you the freedom to innovate, too. To improve manageability, |CL| 
employs a :ref:`stateless` design, separating user and system management.  

Understanding what it takes to integrate features into our own Linux distro 
helps us collaborate with other distro owners and submit enhancements to 
upstream. We demonstrate the value of our distro by offering users the 
same tools we use. For example, :ref:`mixer`, a tool unique to |CL|, allows 
users to build custom derivatives and act as their own 
:abbr:`(OSV) OS Vendor`. 

For more details on |CL| features, refer to the :ref:`cl-guides` guides.

What makes |CL| different?
**************************

Release Cadence
===============

|CL| updates are based on a rolling release that can occur daily, up to a few
times per week. Each release has a unique version number that identifies
every component in the OS from kernel, to driver, to tool, to GUI
application. Most components are included in entities called :ref:`bundles<bundles>`.

Updates
=======

By default, |CL| automatically checks for updates, ensuring the latest
performance and security fixes are installed as soon as they are available.
|CL| stays in lockstep with upstream for current security upgrades and is 
designed to rapidly deliver security mitigations to customers.
:ref:`swupd-guide` is designed to manage updates and bundles.

Ease of Use
===========

|CL| makes it easier to manage a number of difficult problems.

* :ref:`autoproxy` makes it possible for |CL| tools to operate in some proxy
  environments without needing to be configured.

* :ref:`stateless` means that configuration settings are easier to manage
  and remain untouched when system software is updated.

* :ref:`swupd-guide` simplifies managing software and maintaining compatibility.

Custom Derivatives
==================

The same tools used to build the |CL| are available *in* the OS. These tools can be used to create a custom distribution that continues to benefit from upstream rolling releases.

.. figure:: /_figures/about/clear-lifecycle.png
   :scale: 75%
   :align: center
   :alt: Creating and managing a Clear Linux* OS  version (or derivative)

   Figure 1: Creating and managing a Clear Linux\* OS version (or derivative)

Create
======

To create a custom distribution you need to understand how to use the
:ref:`autospec` and :ref:`mixer` tools.

Additional training materials are available in the `how-to-clear`_ GitHub\*
project to help you get started with |CL| tools.

Deploy
======

We also provide training on how to :ref:`deploy-at-scale`.

Administrate
============

|CL| provides a :ref:`telem-guide` solution for collecting useful information
about a deployment, as well as :ref:`debug` capabilities.

Performance and security
------------------------

We apply the same strategy when it comes to performance. Our developers 
strive to optimize performance for *essential* use cases while we ignore 
*unwanted* or unsupported use cases.

For example, while |CL| does not enable antivirus by default, we provide
a bundle for it (`clamav`). We leave antivirus configuration to our users. 
In addition, firewalls are less important if the OS doesn’t expose services 
to the outside by default. In |CL|, we enforce this strategy by disabling 
network services by default - e.g. mariadb listens on a UNIX socket, nginx 
won’t listen at all, and other services similarly like that are restricted 
from being accessed over the network. This strategy alone makes firewall 
software much less urgent - there simply isn’t anything that a firewall 
could easily block.

If you want a general purpose Linux distro with little to no configuration, 
|CL| may not be the distro enough for you. 


Is |CL| completely Open Source?
*******************************

Wherever possible, |CL| aims to be completely open source.  Our 
`source code`_ is available on GitHub. When considering projects for inclusion, we check that they are in active development and are well maintained. We have a very strict requirement for not accepting proprietary packages and non-open source components.  For example, many Linux distros may not be able to include certain media codecs due to  
:ref:`licensing restrictions <licensing_restrict>`, but alternatives are available.

What’s the thinking around Command line v. Desktop?
***************************************************

|CL| focuses on performance for server and cloud use-cases first because
many design decisions associated with them are applicable to other use-cases, such as IoT and the desktop client. 

While our initial focus was on the command line, we realized that many people valued the ease-of-use of a desktop environment.  We've been trying to accommodate these people as much as we can, but there are clear limits to what a desktop environment can do. This is especially true, given our desire to deliver a highly performant and secure Linux distro, one that provides unique tools for customization, and one that enables several cloud use cases. |CL| has a strong bias toward servers and what developers use, 
rather than including "random stuff".

Why create new components rather than modifying existing projects?
******************************************************************

One question that's often asked: “Why did you develop your own solution 
instead of using <XYZ>?” (e.g. `swupd post`_).  We do evaluate existing 
projects for inclusion in |CL|, yet there are cases where our unique 
architecture and components would require too much customization to use 
off-the-shelf projects.  In other situations, we may feel that using a new 
language to develop the component would give us a performance advantage, 
ease code development and maintenance, and grow the skills of our engineers 
on new and upcoming programming languages.  And yes, sometimes there are 
personal biases for and against some projects by the architects and 
engineers.  We tend to move fast, and sometimes it’s easier to live with 
suboptimal choices until we have the time or incentive to re-architect them 
properly. 

Which Components are used in Clear Linux?
*****************************************

.. list-table::
   :widths: 33,33,33
   :header-rows: 1

   * - Component
     - Enabled in OS/Bundle
     - Optional

   * - OS Installer
     - `Clear Linux installer`_
     - 

   * - Bootloader
     - `systemd-boot`_ (UEFI) / `syslinux`_ (Legacy)
     - 

   * - Boot Manager
     - `Clear Linux Boot Manager`_
     - 

   * - Configuration initialization and management
     - 
     - `micro-config-drive`_ (minimal cloud-init), Ansible

   * - Software component installer, manager, updater
     - `swupd`_
     - 

   * - Software bundle generator - 
     - `mixer`_ and `clr-distro-factory`_
     - 

   * - Package builder
     - `autospec`_
     - 

   * - Software debugging
     - 
     - `clr-debug-info`_ 

   * - Unified TLS Trust Store Management
     - `clrtrust`_
     - 

   * - System and software telemetry
     - 
     - `Telemetrics`_ (disabled by default)

   * - File system
     - `EXT4`_ (default for rootfs)
     - `VFAT`_, `EXT2 and EXT3`_, `F2FS`_

   * - Disk encryption
     - 
     - `LUKS`_ 

   * - System /Service manager  
     - `systemd`_
     - 

   * - Display manager 
     - `Gnome`_
     - ``KDE``, ``i3``, ``XFCE`` ``LXQt`` (see`Clear Linux store`_)

   * - Display services (Desktop installed)
     - `X.Org`_
     - `Wayland`_ compositor

   * - Network services
     - `NetworkManager`_ by default*, `systemd-networkd`_
     - 

   * - SSH Port scanning blocker
     - `Tallow`_
     - 

   * - Firewall
     - None by default
     - iptables and `firewalld`_

   * - Antivirus
     - None by default
     - `ClamAV®`_

   * - Web browser
     - `Lynx`_ or `links`_ for text environments, `Firefox`_ for GUI
     - 

   * - Additional Software
     - `Supplied Bundles`_
     - Flatpak, 3rd-party software bundles

.. note::
   
   The |CL| OS images targeted for cloud deployments continue to use
   ``systemd-networkd`` to manage network connections.  In earlier |CL|, 
   ``systemd-networkd`` was used to manage Ethernet interfaces and NetworkManager was used for wireless interfaces.

.. _how-to-clear: https://github.com/clearlinux/how-to-clear
.. _Clear Linux store: https://clearlinux.org/software
.. _source code: https://github.com/clearlinux
.. _swupd post: https://community.clearlinux.org/t/why-does-clearlinux-use-swupd-and-not-apt-deb-rpm/
.. _swupd: https://github.com/clearlinux/swupd-client
.. _Clear Linux installer: https://github.com/clearlinux/clr-installer/
.. _systemd-boot: https://www.freedesktop.org/software/systemd/man/systemd-boot.html
.. _syslinux: https://wiki.syslinux.org/wiki/index.php?title=The_Syslinux_Project
.. _Clear Linux Boot Manager: https://github.com/clearlinux/clr-boot-manager
.. _mixer: https://github.com/clearlinux/mixer-tools
.. _clr-distro-factory: https://github.com/clearlinux/clr-distro-factory
.. _autospec: https://github.com/clearlinux/common
.. _clr-debug-info: https://github.com/clearlinux/clr-debug-info
.. _clrtrust: https://github.com/clearlinux/clrtrust
.. _EXT4: https://ext4.wiki.kernel.org/index.php/Main_Page
.. _VFAT: https://www.kernel.org/doc/html/latest/filesystems/vfat.html
.. _EXT2 and EXT3: https://ext4.wiki.kernel.org/index.php/Main_Page
.. _F2FS: https://www.kernel.org/doc/Documentation/filesystems/f2fs.txt
.. _LUKS: https://gitlab.com/cryptsetup/cryptsetup/
.. _systemd: https://www.freedesktop.org/wiki/Software/systemd/
.. _Gnome: https://www.gnome.org/
.. _X.Org: https://www.x.org/
.. _Wayland: https://wayland.freedesktop.org/
.. _NetworkManager: https://wiki.gnome.org/Projects/NetworkManager
.. _systemd-networkd: https://www.freedesktop.org/software/systemd/man/systemd.network.html
.. _Tallow: https://github.com/clearlinux/tallow
.. _firewalld: https://docs.01.org/clearlinux/latest/guides/network/firewall.html#firewalld
.. _ClamAV®: https://www.clamav.net/
.. _Lynx: https://lynx.invisible-island.net/
.. _links: http://links.twibright.com/
.. _Firefox: https://www.mozilla.org/en-US/firefox/
.. _Supplied Bundles: https://clearlinux.org/software
.. _micro-config-drive: https://github.com/clearlinux/micro-config-drive
.. _Telemetrics: https://github.com/clearlinux/telemetrics-backend