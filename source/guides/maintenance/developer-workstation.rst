.. _developer-workstation:

Developer Workstation
#####################

This guide helps you find the minimum set of bundles needed to start your
|CL-ATTR| development project.

Before continuing, review the :ref:`swupd <swupd-guide>` guide to learn more
about the swupd tool and how |CL| simplifies software versioning compared to
other Linux\* distributions.

.. contents::
   :local:
   :depth: 1

Workstation Setup
*****************

After installing the minimum set of bundles required to get started, you can add
more bundles relevant to your specific use case.

To run any process required for |CL| development, you can add the large bundle
:ref:`*os-clr-on-clr* <enable-user-space>`. However, given how many packages this
bundle contains, you may want to deploy a leaner OS with only bundles relevant to
your project.

Use Table 1, *Developer Profiles*, to identify the *minimum
required bundles* to get started developing based on your role or project.
While your role may not neatly fit in one of these categories, consider
Table 1 as a starting point.

.. list-table:: **Table 1. Developer Profiles**
   :widths: 20, 20, 20, 20
   :header-rows: 1

   * - |CL| Bundle
     - *Internet of Things (IoT)*
     - *System Administrator*
     - *Client/Cloud/Web Developer*

   * - :command:`editors`
     - ✓
     - ✓
     - ✓

   * - :command:`network-basic`
     - ✓
     - ✓
     - ✓

   * - :command:`openssh-server`
     - ✓
     - ✓
     - ✓

   * - :command:`webserver-basic`
     -
     - ✓
     - ✓

   * - :command:`application-server`
     -
     - ✓
     - ✓

   * - :command:`database-basic`
     -
     - ✓
     - ✓

   * - :command:`desktop-autostart`
     - ✓
     - ✓
     - ✓

   * - :command:`dev-utils`
     -
     -
     - ✓

swupd search
************

We recommend learning about :ref:`swupd <swupd-guide>`, to learn the
commands to search for and add bundles relevant to your project.

The guide provides an :ref:`example <swupd-guide-example-install-bundle>`
that shows you how to:

* Use swupd to search for bundles
* Use swupd to add bundles

Core Concepts
*************

We recommend that you understand these core concepts in |CL| *before*
developing your project.

* :ref:`Software update <swupd-guide>`
* :ref:`Mixer <mixer>`
* :ref:`Autospec <autospec>`

Other resources for developers
-----------------------------------

* `Developer Tooling Framework`_ for |CL|
* `Bundle Definition Files`_

.. _Bundle Definition Files: https://github.com/clearlinux/clr-bundles

.. _Developer Tooling Framework: https://github.com/clearlinux/common
