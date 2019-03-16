.. _architect-lifecycle:

Architect the life-cycle of |CL-ATTR|
#####################################

This guide provides DevOps with a model to architect the life-cycle of a |CL|
derivative that integrates custom software and content using distinct
workflows.

Maintaining a |CL| derivative requires:

* Monitoring upstream |CL| for new releases
* Building software packages and staging
* Employing CI/CD automation for building releases
* Integrating Quality Assurance for testing and validation

This guide provides the foundation of the recommended infrastructure.

.. contents::
   :local:
   :depth: 1

Prerequisites
*************

* A repository with software RPM artifacts and a CI/CD system with a |CL|
  machine for building `mixes`

* Experience using :ref:`mixer <mixer>` to create a |CL|-based distro

* Experience using :ref:`swupd <swupd-guide>` for maintaining the |CL|
  build environment

* Familiarity with |CL| architecture and reuse of its content in releases

Description
***********

Coordinated infrastructure is deployed to automate the life-cycle
of your |CL| derivative. We divide deployment of this infrastucture in two
parts: *Content Workflow*; and *Release Workflow*, shown in Figure 1. Distro Factory manages the *Release Workflow* while capturing the requirements for
maintaining a long-term release cadence.

.. figure:: figures/architect-lifecycle-1.png
   :scale: 100%
   :alt: Architect the life-cycle

   Figure 1: Architect the life-cycle

Content workflow
****************

The *Content Workflow* (Figure 1) orchestrates the processes used to manage
the creation of content for the distribution. This includes everything from detecting a new release in a custom software repository to generating RPM package files. The RPM files serve as intermediary artifacts that track software dependencies and provide file-level data consumed in a *Release Workflow*.  The `Watcher Pipeline`_ checks |CL| and a content provider, such as Koji, to determine if a new release is necessary.

Release workflow
****************

The *Release Workflow* (Figure 1) gathers the content of the RPMs and
ensures it can be consumed by :ref:`mixer <mixer>`. A content web server
hosts the |CL| derivative, to which targets connect for updating their OSes.
As an integral part of this toolchain, the *Release Pipeline* enables these
derivatives to incorporate |CL| content into their own custom
content. The *Watcher Pipeline* triggers the `Release Pipeline`_ to create
new releases.

Implementation
**************

Distro factory implements the *Release workflow*. To get started on a full implementation, visit |CL| `Distro factory documentation`_.

.. _Distro factory documentation: https://github.com/clearlinux/clr-distro-factory/wiki#clear-linux-distro-factory

.. _Release Pipeline: https://github.com/clearlinux/clr-distro-factory/wiki/Release

.. _Watcher Pipeline: https://github.com/clearlinux/clr-distro-factory/wiki/Watcher
