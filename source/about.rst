.. _about:

About
#####

|CL| is designed to deliver a secure, hardware optimized OS that is easy to
keep up to date while ensuring that software dependencies remain mutually
compatible.

This is accomplished through a number of custom infrastructure components and process innovations that make |CL| unique. 

.. contents::
   :local:
   :depth: 1

Release Cadence
***************

|CL| updates are based on a rolling release that can occur daily but usually occur a few times per week. Each release has a unique version number that identifies every component in the OS from kernel, to driver, to tool, to GUI application. Most components are included in entities called :ref:`bundles-about`.

Updates
*******

Updates are made to ensure that the latest performance and security fixes are installed as soon as they are available. :ref:`swupd-guide` is the custom tool designed to manage updates and bundles. 

|CL| is :ref:`stateless` to make sure that system components can be updated without impacting user settings. 
 
Ease of Use
***********

|CL| is designed to make a number of difficult problems easier to manage.
:ref:`autoproxy` makes it possible for |CL| tools to operate in some proxy
environments without needing to be configured.

Being :ref:`stateless` means that configuration settings are easier to manage and remain untouched when system sofware is updated.

:ref:`swupd-guide` also makes it easy to manage software and maintain compatibility.

Custom Derivatives
******************

The same tooling that the |CL| team uses can be used to create a custom distribution that continues to benefit from rolling releases.

.. figure:: /_figures/clear-lifecycle.png
   :scale: 75%
   :align: center
   :alt: Creating and Managing a Clear Linux* OS (or derivative) Version

   Figure 1: Creating and managing a Clear Linux\* OS (or derivative) version


Create
======

You will need to understand how to use :ref:`autospec` and :ref:`mixer`
to create a custom distribution. 

Additional training materials are available in the `how-to-clear`_ GitHub\*
project to help you get started with |CL| tools.

To complete the training, you will need a clean |CL| installation and a
network connection. The project includes all files needed to complete the
exercises.

Deploy
======

We also provide training on how to :ref:`deploy-at-scale`.
 
Administrate
============

:ref:`telem-guide` provides a method of collecting useful information about a |CL| deployment, and  there are also :ref:`debug` capabilities.



.. _how-to-clear: https://github.com/clearlinux/how-to-clear
