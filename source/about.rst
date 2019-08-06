.. _about:

About
#####

The |CL| delivers a secure, hardware optimized OS. Its easy updates ensure that
software dependencies remain mutually compatible.

|CL| does this via custom infrastructure components and process innovations.

.. contents::
   :local:
   :depth: 1


For detailed information on these topics, refer to the :ref:`cl-guides` guides.


Release Cadence
***************

|CL| updates are based on a rolling release that can occur daily, up to a few
times per week. Each release has a unique version number that
identifies every component in the OS from kernel, to driver, to tool, to GUI
application. Most components are included in entities called *bundles*.

Updates
*******

By default, |CL| automatically checks for updates, ensuring that the latest
performance and security fixes are installed as soon as they are available.
:ref:`swupd-guide` is the custom tool designed to manage updates and bundles.

|CL| is :ref:`stateless` to make sure that system components can be updated
without impacting user settings.


Ease of Use
***********

|CL| makes it easier to manage a number of difficult problems.

* :ref:`autoproxy` makes it possible for |CL| tools to operate in some proxy
  environments without needing to be configured.

* Being :ref:`stateless` means that configuration settings are easier to manage
  and remain untouched when system sofware is updated.

* :ref:`swupd-guide` simplifies managing software and maintaining compatibility.

Custom Derivatives
******************

The same tools used to build the |CL| are available *in* the OS. These tools can
be used to create a custom distribution that continues to benefit from upstream
rolling releases.

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

.. _how-to-clear: https://github.com/clearlinux/how-to-clear
