.. _about:

About
#####

|CL-ATTR| does things differently. Our software architecture provides a
unique and innovative platform for Linux* developers focused on
performance and security for compute, server, and the cloud.

.. contents::
   :local:
   :depth: 1

What is |CL|?
*************

|CL| is an open source, rolling-release Linux distribution, optimized for
performance and security from the cloud to the Edge. Designed from the ground up,
|CL| provides an industry blueprint on how to incorporate Intel® architecture
features for a modern, modular Linux OS. |CL| is not based on any other Linux
distro.

What |CL| isn't?
****************

|CL| is not intended to be a general-purpose Linux distribution, suitable 
for novice end-users. While we ship common applications, our purpose isn’t 
to make an OS for routine desktop tasks and provide immunity from all 
security threats in all situations. Our unique focus means that what we consider *essential* use cases, *optional* use cases, or even *unsupported* use cases, differs from other Linux distros. See our :ref:`target audience <target-audience>` below. 

Is |CL| completely Open Source?
*******************************

|CL| aims to be completely open source. Our project `source code`_ and 
`packages source code`_ are available on GitHub\*. When considering projects 
for inclusion, we check that they are in active development and are well 
maintained. We have a very strict requirement for not accepting proprietary 
packages and non-open source components.  For example, many Linux distros 
may not be able to include certain media codecs due to 
:ref:`licensing restrictions <licensing_restrict>`, but manual installation and `third party alternatives`_ are available. 

.. _target-audience:

Who is the target audience?
***************************

|CL| mainly targets professionals in IT, DevOps, Cloud/Container deployments, and :abbr:`AI (Artificial Intelligence)`. 

Rather than making a standard Linux distribution, the |CL| team decided to
build a unique Linux distro. Developing a distro in house allows us to experiment and iterate faster, which means we continually optimize performance and deliver security patches, :ref:`several times per week <release-cadence>`. Yet our experiments are only valuable if our software architecture gives you the freedom to innovate, too. To improve manageability, |CL| employs a :ref:`stateless` design, separating user and system management.  

We leverage the pool of knowledge and skills at Intel to drive improvements to |CL|.

Intel has worked with the Linux community and other distros for many years.
Understanding what it takes to integrate features in our own Linux distro
helps us collaborate with other distro owners and submit enhancements to
upstream. We demonstrate the value of our distro by offering users the same
tools we use. For example, :ref:`mixer`, a tool unique to |CL|, allows users
to build custom derivatives and act as their own :abbr:`OSV (Operating System
Vendor)`. 

For more details on |CL| features, visit our :ref:`cl-guides` guides.

How does |CL| address security?
*******************************

Several :ref:`security features <security>` are designed to work 
out-of-the-box, yet they're not intended to be intrusive. We focus on 
*essential* use cases and ignore *unwanted* or *unsupported* use cases. 
For example, while |CL| does not enable antivirus by default, we provide a 
bundle for it (``clamav``). We leave antivirus configuration to our users.  
In addition, firewalls are less important if the OS doesn’t expose services 
to the outside by default. In |CL|, we enforce this strategy by disabling 
network services by default - e.g. ``mariadb`` listens on a UNIX socket; 
``nginx`` won’t listen at all; and other services similarly are restricted 
from being accessed over the network. This strategy alone makes firewall 
software much less urgent--there simply isn’t anything that a firewall could 
easily block.

What’s the thinking around Server vs. Desktop?
**********************************************

|CL| focuses on performance for server and cloud use-cases first because 
many design decisions associated with them are applicable to other 
use-cases, such as IoT and the desktop client. While our initial focus was 
on the command line, we realized that many people valued the ease-of-use of 
a desktop environment.  Whereas in the past we tried to accommodate those 
interested in a desktop version, we were forced to confront clear limits as
to how we could meet this need. |CL| minimizes the customizations and patches in support of the desktop and provides a generic GNOME implementation. Other window managers or desktops are available; however, testing in |CL| is focused on GNOME. 

What makes |CL| different?
**************************

.. _release-cadence:

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

* :ref:`swupd-guide` simplifies managing software and maintaining
  compatibility.

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
:ref:`autospec` and :ref:`mixer` tools. Additional training materials are available in the `how-to-clear`_ GitHub project to help you get started with |CL| tools.

Deploy
======

We also provide training on how to :ref:`deploy-at-scale`.

Administrate
============

|CL| provides a :ref:`telem-guide` solution for collecting useful information
about a deployment, as well as :ref:`debug` capabilities.

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
     - *NA*
     - `micro-config-drive`_ (minimal cloud-init), Ansible

   * - Software component installer, manager, updater
     - `swupd`_
     - 

   * - Software bundle generator - 
     - `mixer`_ and `Clear Linux Distro Factory`_
     - 

   * - Software package builder
     - `autospec`_
     - 

   * - Software debugging
     - *NA*
     - `clr-debug-info`_ 

   * - Unified TLS Trust Store Management
     - `clrtrust`_
     - 

   * - System and software telemetry
     - *NA*
     - `Telemetrics`_ (disabled by default)

   * - File system
     - `EXT4`_ (default for rootfs), `VFAT`_, `EXT2 and EXT3`_, `F2FS`_
     - 

   * - Disk encryption
     - *NA*
     - `LUKS`_ 

   * - System /Service manager  
     - `systemd`_
     - 

   * - Display manager 
     - `GNOME`_
     - ``KDE``, ``Xfce``, ``lightdm``, ``sddm``  (see `Clear Linux store`_)

   * - Display services (Desktop installed)
     - `X.Org`_
     - `Wayland`_ compositor

   * - Network services
     - `NetworkManager`_ by default, `systemd-networkd`_ See Note below.
     - 

   * - SSH Port scanning blocker
     - `Tallow`_
     - 

   * - Firewall
     - *NA*
     - iptables and `firewalld`_

   * - Antivirus
     - *NA*
     - `ClamAV*`_

   * - Web browser
     - `Lynx`_ or `links`_ for text environments, `Firefox*`_ for GUI
     - 

   * - Additional Software
     - `Supplied Bundles`_
     - Flatpak, 3rd-party software bundles

.. note::
   
   The |CL| OS images targeted for cloud deployments continue to use
   ``systemd-networkd`` to manage network connections.  In earlier |CL|, 
   ``systemd-networkd`` was used to manage Ethernet interfaces and NetworkManager was used for wireless interfaces.


*Intel and the Intel logo are trademarks of Intel Corporation or its subsidiaries.*

.. _third party alternatives: https://community.clearlinux.org/t/about-the-3rd-party-sw-category/4072
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
.. _Clear Linux Distro Factory: https://github.com/clearlinux/clr-distro-factory
.. _autospec: https://github.com/clearlinux/common
.. _clr-debug-info: https://github.com/clearlinux/clr-debug-info
.. _clrtrust: https://github.com/clearlinux/clrtrust
.. _EXT4: https://ext4.wiki.kernel.org/index.php/Main_Page
.. _VFAT: https://www.kernel.org/doc/html/latest/filesystems/vfat.html
.. _EXT2 and EXT3: https://ext4.wiki.kernel.org/index.php/Main_Page
.. _F2FS: https://www.kernel.org/doc/Documentation/filesystems/f2fs.txt
.. _LUKS: https://gitlab.com/cryptsetup/cryptsetup/
.. _systemd: https://www.freedesktop.org/wiki/Software/systemd/
.. _GNOME: https://www.gnome.org/
.. _X.Org: https://www.x.org/
.. _Wayland: https://wayland.freedesktop.org/
.. _NetworkManager: https://wiki.gnome.org/Projects/NetworkManager
.. _systemd-networkd: https://www.freedesktop.org/software/systemd/man/systemd.network.html
.. _Tallow: https://github.com/clearlinux/tallow
.. _firewalld: https://docs.01.org/clearlinux/latest/guides/network/firewall.html#firewalld
.. _ClamAV*: https://www.clamav.net/
.. _Lynx: https://lynx.invisible-island.net/
.. _links: http://links.twibright.com/
.. _Firefox*: https://www.mozilla.org/en-US/firefox/
.. _Supplied Bundles: https://clearlinux.org/software
.. _micro-config-drive: https://github.com/clearlinux/micro-config-drive
.. _Telemetrics: https://github.com/clearlinux/telemetrics-backend
.. _packages source code: https://github.com/clearlinux-pkgs/
