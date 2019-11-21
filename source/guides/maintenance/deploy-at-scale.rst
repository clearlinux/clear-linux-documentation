.. _deploy-at-scale:

Deploy at Scale
###############

This guide describes deployment considerations and strategies when deploying
|CL-ATTR| at scale in your environment.

.. contents::
    :local:
    :depth: 1

Overview
********

In this guide the term *endpoint* refers to a system targeted for |CL|
installation, whether that is a datacenter system or unit deployed in field.

.. note::

    This guide is not a replacement or blueprint for designing your own IT
    operating environment.

    Implementation details for a scale deployment are beyond the scope of this
    guide.

    Your |CL| deployment should complement your existing environment and
    available tools. It is assumed core IT dependencies of your environment,
    such as your network, are healthy and scaled to suit the deployment.

Pick a usage and update strategy
********************************

Different business scenarios call for different deployment methodologies.
|CL| offers the flexibility to continue consuming the upstream |CL|
distribution or the option to fork away from the |CL| distribution and
act as your own :abbr:`OSV (Operating System Vendor)`.

Below is an overview of some considerations.

Create your own Linux distribution (mix)
========================================

This approach forks away from the |CL| upstream and has you act as your own
:abbr:`OSV (Operating System Vendor)` by leveraging the :ref:`mixer` process to
create customized images based on |CL|. This is a level of responsibility
that requires having more infrastructure and processes to adopt. In return,
this approach *offers you a high degree of control and customization*. Consider:

* Development systems that generate bundles and updates should have
  sufficient performance for the task and be separate from the swupd update
  webservers that serve update content to production machines.

* swupd update webservers that serve update content to production machines
  should be appropriately scaled. Specific implementation details for a scalable,
  resilient web server are beyond the scope of this document.

  (See :ref:`mixer` for more information about update servers.)

Adopt an agile methodology
==========================

The cloud, and other scaled deployments, are all about flexibility and speed.
It only makes sense that any |CL| deployment strategy should follow suit.

Manually rebuilding your own bundles or mix for every release is not
sustainable at a large scale. A |CL| deployment pipeline should be agile
enough to validate and produce new versions with speed. Whether or not those
updates actually make their way to your production can be separate
business decision. However this *ability to frequently roll new versions* of
software to your endpoints is an important prerequisite.

You own the validation and lifecycle of the OS and should treat it like any
other software development lifecycle. Below are some pointers:

* Thoroughly understand the custom software packages that you will need to
  integrate with |CL| and maintain along with their dependencies.

* Setup a path to production for building |CL| based images. At minimum this
  should include:

  * A development clr-on-clr environment to test building packages and
    bundles for |CL| systems.

  * A pre-production environment to deploy |CL| versions to before
    production

* Employ a continuous integration and continuous deployment (CI/CD)
  philosophy in order to:

  - Automatically pull custom packages as they are updated from their
    upstream projects or vendors.

  - Generate |CL| bundles and potentially bootable images with your
    customizations, if any.

  - Measure against metrics and indicators which are relevant to your
    business (e.g. performance, power, etc) from release to release.

  - Integrate with your organization's governance processes, such as change
    control.

Versioning infrastructure
=========================

|CL| version numbers are very important as they apply to the whole
infrastructure stack from OS components to libraries and applications.

Good record keeping is important, so you should keep a detailed registry and
history of previously deployed versions and their contents.

With a glance at the |CL| version numbers deployed, you should be able to
tell if your Clear systems are patched against a particular security
vulnerability or incorporate a critical new feature.

Pick an image distribution strategy
***********************************

Once you have decided on a usage and update strategy, you should understand
*how* |CL| will be deployed to your endpoints. In a large scale deployment,
interactive installers should be avoided in favor of automated installations
or prebuilt images.

There are many well-known ways to install an operating system at scale. Each
have their own benefits, and one may lend itself easier in your environment
depending on the resources available to you.

See the available :ref:`image-types`.

Below are some common ways to install |CL| to systems at scale:

Bare metal
==========

Preboot Execution Environments (PXE) or other out-of-band booting options are
one way to distribute |CL| to physical bare metal systems on a LAN.

This option works well if your customizations are fairly small in size
and infrastructure can be stateless.

The |CL| `Downloads`_ page offers a live image that can be deployed as
a PXE boot server if one doesn't already exist in your environment. Also see
documentation on how to :ref:`bare-metal-install-server`.

Cloud instances or virtual machines
===================================

Image templates in the form of cloneable disks are an effective way to
distribute |CL| for virtual machine environments, whether on-premises or
hosted by a Cloud Solution Provider (CSP).

When used in concert with cloud VM migration features, this can be a good option
for allowing your applications a degree of high availability and workload
mobility; VMs can be restarted on a cluster of hypervisor host or moved between
datacenters transparently.

The |CL| `Downloads`_ page offers example prebuilt VM images and is readily
available on popular CSPs. Also see documentation on how to
:ref:`virtual-machine-install`.

Containers
==========

Containerization platforms allow images to be pulled from a repository and
deployed repeatedly as isolated containers.

Containers with a |CL| image can be a good option to blueprint and ship
your application, including all its dependencies, as an artifact while
allowing you or your customers to dynamically orchestrate and scale
applications.

|CL| is capable of running a Docker host, has a container image which can
be pulled from DockerHub, or can be built as a customized container.
For more information visit the `Containers`_ page.

Considerations with stateless systems
*************************************

An important |CL| concept is statelessness and partitioning of system data
from user data. This concept can change the way you think about an at scale
deployment.

Backup strategy
===============

A |CL| system and its infrastructure should be considered a commodity and
be easily reproducible. Avoid focusing on backing up the operating system
itself or default values.

Instead, focus on backing up what's important and unique - the application
and data.  In other words, only focus on backing up critical areas like
:file:`/home`, :file:`/etc`, and :file:`/var`.

Meaningful logging & telemetry
==============================

Offload logging and telemetry from endpoints to external servers, so it is
persistent and can be accessed on another server when an issue occurs.

* Remote syslogging in |CL| is available through the
  `systemd-journal-remote.service`_

* |CL| offers a :ref:`telem-guide`, which can be a powerful tool
  for a large deployment to quickly crowdsource issues of interest. Take
  advantage of this feature with careful consideration of the target audience
  and the kind of data that would be valuable, and expose events
  appropriately.

  Like any web server, the telemetry server should be appropriately scaled and
  resilient. Specific implementation details for a scalable, resilient web
  server are beyond the scope of this document.

Orchestration and configuration management
==========================================

In cloud environments, where systems can be ephemeral, being able to
configure and maintain generic instances is valuable.

|CL| offers an efficient cloud-init style solution, `micro-config-drive`_,
through the *os-cloudguest* bundles which allow you to configure many Day 1
tasks such as setting hostname, creating users, or placing
SSH keys in an automated way at boot. For more information on
automating configuration during deployment of |CL| endpoints see the
:ref:`ipxe-install` guide.

A configuration management tool is useful for maintaining consistent system
and application-level configuration. Ansible\* is offered through the
*sysadmin-hostmgmt* bundle as a configuration management and automation
tool.

Cloud-native applications
=========================

An Infrastructure OS can design for good behavior, but it is ultimately up
to applications to make agile design choices. Applications deployed
on |CL| should aim to be host-aware but not depend on any specific host to
run. References should be relative and dynamic when possible.

The application architecture should incorporate an appropriate tolerance for
infrastructure outages. Don't just keep stateless design as a noted feature.
Continuously test its use; Automate its use by redeploying |CL| and
application on new hosts. This naturally minimizes configuration drift,
challenges your monitoring systems, and business continuity plans.

.. _`Downloads`: https://clearlinux.org/downloads/
.. _`Containers`: https://clearlinux.org/downloads/containers
.. _`systemd-journal-remote.service`: https://www.freedesktop.org/software/systemd/man/systemd-journal-remote.service.html
.. _`micro-config-drive`: https://github.com/clearlinux/micro-config-drive

.. |WEB-SERVER-SCALE| replace::
   There are many well-known ways to achieve a scalable and resilient web
   server for this purpose, however implementation details are not in the
   scope of this document. In general, they should be close to your
   endpoints, highly available, and easy to scale with a load balancer when
   necessary.
