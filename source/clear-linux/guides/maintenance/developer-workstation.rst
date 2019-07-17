.. _developer-workstation:

Developer Workstation
#####################

*Developer Workstation* helps you find the :ref:`bundles-about` you need to
start your |CL-ATTR| development project.

Before continuing, we recommend that you learn how to use
:ref:`swupd <swupd-guide>`. Visit our :ref:`swupd-about` page to understand
how |CL| simplifies software versioning compared to other Linux\*
distributions.

Workstation Setup
*****************

This guide helps you understand the minimum bundles required to get started.
After installing them, you can add more bundles relevant to your use case.
To run any process required for |CL| development, you can add the
large bundle :ref:`*os-clr-on-clr* <enable-user-space>`. However, given how
many packages this bundle contains, you may want instead to deploy a leaner
OS with only those bundles relevant to your project. Developer Workstation
responds to this need.

Use Table 1, *Developer Profiles*, to identify the *minimum
required bundles* to get started developing based on your role or project.
While your role may not neatly fit in one of these categories, consider using
Table 1 as a starting point.

.. list-table:: **Table 1. Developer Profiles**
   :widths: 20, 20, 20, 20
   :header-rows: 1

   * - |CL| Bundle
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
     - ✓
     - ✓
     - ✓

   * - `dev-utils`
     -
     -
     - ✓

`swupd` search
**************

We recommend learning about :ref:`swupd <swupd-guide>`, to learn the
commands to search for and add bundles relevant to your project.

The guide provides an :ref:`example <swupd-guide-example-install-bundle>`
that shows you how to:

* Use `swupd` to search for bundles
* Use `swupd` to add bundles

Core Concepts
*************

We recommend that you understand these core concepts in |CL| *before*
developing your project.

* :ref:`Bundles <bundles-about>`
* :ref:`Software update <swupd-about>`
* :ref:`Mixer <mixer-about>`
* :ref:`Autospec <autospec-about>`

Other resources for developers
-----------------------------------

* `Developer Tooling Framework`_ for |CL|
* `Bundle Definition Files`_

.. _Bundle Definition Files: https://github.com/clearlinux/clr-bundles

.. _Developer Tooling Framework: https://github.com/clearlinux/common
