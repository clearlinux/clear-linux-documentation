.. _developer-workstation:

Developer Workstation
#####################

Overview
********

*Developer Workstation* helps you find the :ref:`bundles-about` you need to 
start your |CL| development project. 

Before continuing, we recommend that you learn how to use :ref:`swupd <swupd-guide>`. Visit our :ref:`swupd-about` page to understand how |CL|
simplifies software versioning in contrast to other Linux\* distributions. 

Workstation Setup
=================

This guide helps you understand the minimum bundles required to get started. 
After installing them, you can add more bundles relevant to your use case. 
To run any process required for Clear Linux development, you may choose to 
add the large bundle :ref:`*os-clr-on-clr* <enable-user-space>`. However, 
given how many packages this bundle contains, you may instead want to deploy 
a leaner OS with only those bundles relevant to your project. Developer 
Workstation responds to this need. 

Use Table 1, *Clear Linux Developer Profiles*, to identify the *minimum 
required bundles* to get started developing based on your role or project. 
While your role may not neatly fit in one of these categories, consider using Table 1 as a starting point. 

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

`swupd` search
==============

We recommend trying out :ref:`swupd search <swupd-search>`, to learn the
commands to search for and add bundles relevant to your project. 

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
