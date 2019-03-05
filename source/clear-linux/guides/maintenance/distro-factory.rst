.. distro_factory:

Distro factory
##############

Distro factory gives DevOps teams the means to produce |CL-ATTR|
derivatives via pipeline jobs that support a release workflow with
continuous integration. This guide recommends setting up a standard
infrastructure before implementing the release workflow.

.. contents::
   :local:
   :depth: 1

Description
***********

As an operating system vendor (OSV) toolchain, Distro factory manages |CL|
derivatives while capturing the requirements used to maintain the release
cadence over time. Distro factory provides a wrapper around
:ref:`mixer <mixer>` that enables a DevOps team to publish rolling releases
that include the update content and metadata associated with each version.

Maintaining an OSV derivative of |CL| requires:

* Monitoring upstream |CL| for new releases
* Building software packages and staging
* Employing CI/CD automation for building releases
* Integrating Quality Assurance for testing and validation

How it works
************

Review the requirements and learn the basics of implementation.

.. contents::
   :local:
   :depth: 1

Prerequisites
=============

* A repository with software RPM artifacts and a CI/CD system with a |CL|
  machine for building `mixes`

* Experience using :ref:`mixer <mixer>` to create a |CL|-based distro

* Experience using :ref:`swupd <swupd-guide>`

Overview
========

We divide deployment of infrastucture in two parts: *Content Workflow*;
and *Release Workflow*. Distro Factory manages the *Release Workflow*.

We include the *Content Workflow* to give context for the entire process.

Content workflow
----------------
The *Content Workflow* (Figure 1) comprises all of the processes and
methodologies used to manage the content of the distribution. It includes
everything from detecting a new release in a custom software repository to
generating RPM package files. Used as intermediary artifacts to track
software dependencies, RPM files are fed into :ref:`mixer <mixer>`.

Release workflow
----------------
The *Release Workflow* allows DevOps to create a new release for the
targets/clients (Figure 1). As an integral part of the toolchain, the
*Release Pipeline* enables downstream derivatives to incorporate
|CL| content into their own custom content.


.. figure:: figures/distro-factory-1.png
   :scale: 100%
   :alt: Distro factory overview

   Figure 1: Distro factory overview

.. note::

   While Jenkins is used for CI/CD and Koji is used for content, these may
   be replaced with other solutions.

Pipelines
=========

Pipelines define the order in which a set of scripts is executed, and they
determine how processes interact. Pipelines can be customized to fit a
team's requirements. So what do pipelines do?

* `Watcher Pipeline`_ Checks if a new release is necessary by checking |CL| and a content provider, such as Koji.
* `Release Pipeline`_ Creates new releases when triggered by the Watcher Pipeline

Implementation
==============

To implement Distro Factory, you should follow a Distro Release Workflow
for multiple instances to share. First, pipelines must be established to
fetch from a `clr-distro-factory-config`, which is a git repository
containing all the data needed for this workflow to run. To get started on a
full implementation, visit |CL| `Distro factory documentation`_.

.. TODO: Add content here on: 1) Recommended file structure; 2) clr-distro-factory-config git repo; 3) using Jenkins to create jobs for each pipeline.

.. _Distro factory documentation: https://github.com/clearlinux/clr-distro-factory/wiki#clr-distro-factory

.. _Watcher Pipeline: https://github.com/clearlinux/clr-distro-factory/wiki/Watcher

.. _Koji Pipeline: https://github.com/clearlinux/clr-distro-factory/wiki/Koji

.. _Release Pipeline: https://github.com/clearlinux/clr-distro-factory/wiki/Release
