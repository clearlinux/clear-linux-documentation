.. _developer-workstation:

Developer Workstation
#####################

Overview
********

*Developer Workstation* helps you find the bundles you need to 
start your |CL| development project. 

First, we recommend learning how to use :ref:`swupd <swupd-guide>`. 

How to use this document
========================

This guide helps you understand the minimum bundles required to get started. 
After installing them, you can add more bundles relevant to your use case. 
To run any process required for Clear Linux developement, you may want to 
add the large bundle :ref:`*os-clr-on-clr* <enable-user-space>`. However, 
given how many packages this bundle contains, you may prefer instead to 
deploy a leaner OS with only bundles relevant to your project. Developer 
Workstation responds to this need. 

Use Table 1, *Clear Linux Developer Profiles*, to identify the *minimum 
required bundles* to get started developing based on your role or project. 
While your role may not fit neatly into one of these categories, use Table 1 
as a starting point. 

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


Second, try out :ref:`swupd search <swupd-search>`, to learn the commands to
search for and add bundles relevant to your project. 

:ref:`swupd-search` shows you how to: 

* Use `swupd` to search for bundles 
* Use `swupd` to add bundles

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
