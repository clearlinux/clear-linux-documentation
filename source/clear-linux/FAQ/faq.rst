.. _faq:

Frequently Asked Questions (FAQ)
################################

Below is a list of commonly asked questions with answers sourced from the
|CL-ATTR| team and community.

.. contents:: :local:
    :depth: 2


General
*******

Why are you making another distro?
==================================

The |CL| team felt there was performance being left on the table with Linux
software. |CL| takes a wholistic approach to improving performance across the
stack. 

We also felt there were more modern approaches to take with OS update and
tooling.

|

Can other distros copy |CL| improvements?
=========================================

Yes, we absolutely love open source reuse and upstreaming improvements. 

|

How frequently does |CL| update?
================================

The |CL| team puts out multiple releases a week. Often that means 2 or more
releases a day. This rolling release approach allows |CL| to remain agile to
upstream changes and security patches.

|

Is telemetry required?
======================

The telemetry solution provided by |CL| is entirely optional and customizable.
It is disabled by default.

When you do choose to enable telemetry, the data goes towards helping the |CL|
team proactively identify and resolve bugs. 

See the :ref:`telemetry <telemetry-about>` page for more information.

|

What is the default firewall?
=============================

|CL| packages iptables as a bundle however, there are no default firewall
rules; all network traffic is allowed by default.

|

Where are files that I usually see under /etc like fstab?
=========================================================

|CL| has a stateless design that maintains a separation between system files
and user files. Default values are stored under :file:`/usr/share/defaults/`.
Files under :file:`/etc/` are not created unless the user creates one.


A blog post explaining how this is accomplished with :file:`/etc/fstab/`
specifically is available here:
https://clearlinux.org/news-blogs/where-etcfstab-clear-linux

|

Software packages
*****************

How is software installed and updated?
======================================

|CL| provides software in the form of :ref:`bundles <bundles-about>` and
updated with :ref:`swupd <swupd-about>`.

:ref:`FlatPak <flatpak>` is an application virtualization solution that allows
more software to be available to |CL| users by augment the software |CL|
packages natively with software available through FlatPak.

Our goal is to have software packaged natively and made available through
bundles wherever it is possible.

|

Does |CL| use RPMS like RedHat?
===============================

|CL| provides software in the form of :ref:`bundles <bundles-about>`. The RPM
format is used as an intermediary step for packaging and determining software
dependencies at OS build time. 

Individual RPMs can sometimes be manually installed on a |CL| system with the
right tools, but that is not the intended use case. 

|

Can I install a software package from another OS on |CL|?
=========================================================

|CL| provides software in the forum of :ref:`bundles <bundles-about>`.

Software that is packaged in other formats for other Linux distributions is
not guaranteed to work on |CL| and may be impacted by |CL| updates.

If the software you're seeking is open source, please submit a request for it
be considered for adding on GitHub:
https://github.com/clearlinux/distribution/issues

|

Software availability
*********************

What software is available on |CL|?
===================================

Software that is available can be found in the `Software Store
<https://clearlinux.org/software>`_, through the GNOME Software application
on the desktop, or using :ref:`swupd search <bundle-commands>`.

|

Is the Google Chrome available?
===============================

The Google Chrome web browser is not distributed as a bundle in |CL| due to
copyright and licensing complexities. 

A discussion on manually installing and maintaining Google Chrome can be found
on GitHub: https://github.com/clearlinux/distribution/issues/422 

|

Is FFmpeg available?
====================

`FFmpeg <https://ffmpeg.org/>`_ is a multimedia framework and tools commonly
used for various media encoding/decoding, streaming, and playback. 

|CL| does not distribute FFmpeg due to well-known licensing and legal
complexities (See https://www.ffmpeg.org/legal.html and
http://blog.pkh.me/p/13-the-ffmpeg-libav-situation.html ).

Discussion about this and an alternative hardware-based solution can be found
on GitHub: https://github.com/clearlinux/distribution/issues/429. 

While |CL| cannot distribute FFmpeg, a manual solution to build and install
FFmpeg under :file:`/usr/local` has been shared on the community forums:
https://community.clearlinux.org/t/how-to-h264-etc-support-for-firefox-including-ffmpeg-install.

|

Is ZFS available?
=================

ZFS is not available with |CL| because of copyright and licensing
complexities. BTRFS is an alternative filesystem that is available in |CL|
natively.

A user on GitHub notes that the kernel module can be compiled built and
installed manually: https://github.com/clearlinux/distribution/issues/631

|

Can a driver that I need be added?
==================================

If a kernel module is available as part of the Linux kernel source tree but
not enabled in the |CL| kernels, the |CL| will enable it upon request in many
cases

The |CL| team does not typically add out-of-tree kernel modules as a matter of
practice because it is a maintenance overhead. If the driver was unable to be
merged upstream there is a good chance we may be unable to for similar
reasons.

Kernel modules can be individually built and installed on |CL|. See the
:ref:`kernel modules <kernel-modules>` page for more information.

|







.. _`Clear Linux community forums`: https://community.clearlinux.org
