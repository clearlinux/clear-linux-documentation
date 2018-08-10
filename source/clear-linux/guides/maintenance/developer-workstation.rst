.. _developer-workstation:

Developer Workstation
#####################

Workstation Setup
*****************

*Workstation Setup* helps you, the developer, find the tools you need. Use 
the *Clear Linux Developer Profiles* (Table 1) to help you decide which bundles, at minimum, you need to set up your developer workstation. 

We recommend using :ref:`swupd-search` to jump-start your skills using 
core |CL| features like `swupd`.

:ref:`swupd search <swupd-search>` shows: 

* How to use `swupd` commands
* How to search for bundles (that contain packages)
* How to add bundles

How to use this document
========================

As a Developer, you could add the bundle `os-clr-on-clr` found in 
:ref:`enable-user-space`. However, you may want to deploy a leaner OS with
only the bundles you need. This guide helps you get started. 

Use Table 1 to identify the *minimum required bundles* you need to get 
started developing based on your role. While your role may not 
neatly fit into one of these categories, use Table 1 as a starting point. 

.. list-table:: **Table 1. Clear Linux Developer Profiles**
   :widths: 20, 20, 20, 20
   :header-rows: 1

   * - Clear Linux Bundle
     - *Internet of Things (IoT)* 
     - *System Administrator*
     - *Client/Cloud/Web Developer*
   * - `editors` 
     - ✓
     - ✓
     - ✓

   * - `network-basic`
     - ✓
     - ✓
     - ✓

   * - `openssh-server`
     - ✓
     - ✓
     - ✓
   
   * - `webserver-basic`
     - 
     - ✓
     - ✓   
   
   * - `application-server`
     - 
     - ✓
     - ✓
   
   * - `database-basic`
     - 
     - ✓
     - ✓
   
   * - `desktop-autostart`
     - 
     - ✓
     - ✓

   * - `dev-utils`
     - 
     - 
     - ✓

Core Concepts
=============

We recommend that you understand these core concepts in |CL| *before* 
developing your project. 

* :ref:`Bundles <bundles-about>`
* :ref:`Software update <swupd-about>`
* :ref:`Mixer <mixer-about>`
* :ref:`Autospec <autospec-about>` 

Resources for |CL| developers: 

* `Developer Tooling Framework for Clear Linux`_
* `Clear Linux Bundles`_

.. _Clear Linux Bundles: https://github.com/clearlinux/clr-bundles

.. _Developer Tooling Framework for Clear Linux: https://github.com/clearlinux/common
