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

After installing the minimum set of bundles required to get started, you can 
add more bundles relevant to your specific use case.

To run any process required for |CL| development, you can add the large 
bundle :ref:`*os-clr-on-clr* <enable-user-space>`. However, given how many 
packages this bundle contains, you may want to deploy a leaner OS with only 
bundles relevant to your project.

Use Table 1, *Developer Profiles*, to identify the *minimum
required bundles* to get started developing based on your developer role or project. Consider using a profile as a starting point.


.. tabs::

   .. tab:: AI Developer

      .. list-table:: 
         :widths: 20, 20
         :header-rows: 1

         * - Function
           - Bundles

         * - Build and run C/C++ language programs.
           - `c-basic <https://clearlinux.org/software/bundle/c-basic/>`_

         * - API helper for cloud access.
           - `cloud-api <https://clearlinux.org/software/bundle/cloud-api/>`_

         * - Pre-built Python libraries for Data Science.
           - `python-extras <https://clearlinux.org/software/bundle/python-extras>`_

   .. tab:: Computer Vision Engineer

      .. list-table:: 
         :widths: 20, 20
         :header-rows: 1

         * - Function
           - Bundles

         * - API helper for cloud access.
           - `cloud-api <https://clearlinux.org/software/bundle/cloud-api/>`_

         * - Build computer vision applications.
           - `computer-vision-basic <https://clearlinux.org/software/bundle/computer-vision-basic/>`_

         * - Work with deep learning and edge-optimized models.
           - `computer-vision-models <https://clearlinux.org/software/bundle/computer-vision-models/>`_

         * - Basic OpenVINO™ toolkit.
           - `computer-vision-openvino <https://clearlinux.org/software/bundle/computer-vision-openvino/>`_

         * - All content for pkgconfig file opencv.pc.
           - `devpkg-opencv <https://clearlinux.org/software/bundle/devpkg-opencv/>`_

   .. tab:: Cloud/Container Developer

      .. list-table:: 
         :widths: 20, 20
         :header-rows: 1

         * - Function
           - Bundles

         * - Contains Clear Linux\* OS native software for cloud.
           - `ethtool <https://clearlinux.org/software/bundle/ethtool/>`_

         * - Utilities for controlling TCP/IP networking and traffic control.
           - `iproute2 <https://clearlinux.org/software/bundle/iproute2/>`_

         * - C++ runtime support.
           - `libstdcpp <https://clearlinux.org/software/bundle/libstdcpp/>`_

         * - Load and enumerate PKCS#11 modules.
           - `p11-kit <https://clearlinux.org/software/bundle/p11-kit/>`_

         * - API helper for cloud access.
           - `cloud-api <https://clearlinux.org/software/bundle/cloud-api/>`_

   .. tab:: Game Developer

      .. list-table:: 
         :widths: 20, 20
         :header-rows: 1

         * - Function
           - `Unity Hub <https://clearlinux.org/software/flathub/unity-hub/>`_

         * - Godot game engine editor
           - `Godot <https://clearlinux.org/software/flathub/godot/>`_
   
         * - Classic point and click adventure game engine and (Flatpak)
           - `adventure editor <https://clearlinux.org/software/flathub/adventure-editor/>`_

         * - Example
           - Example

   .. tab:: Kernel Developer

      .. list-table:: 
         :widths: 20, 20
         :header-rows: 1

         * - Function
           - Bundles

         * - Example
           - Example

   .. tab:: Embedded Systems Developer

      .. list-table:: 
         :widths: 20, 20
         :header-rows: 1

         * - Function
           - Bundles

         * - Example
           - Example

   .. tab:: System Administrator

      .. list-table:: 
         :widths: 20, 20
         :header-rows: 1

         * - Function
           - Bundles

         * - Example
           - Example

"""

  .. .. list-table:: **Table 1. Developer Profiles**
  ..    :widths: 20, 20, 20, 20
  ..    :header-rows: 1

  ..    * - |CL| Bundle
  ..      - *Internet of Things (IoT)*
  ..      - *System Administrator*
  ..      - *Client/Cloud/Web Developer*

  ..    * - :command:`editors`
  ..      - ✓
  ..      - ✓
  ..      - ✓

  ..    * - :command:`network-basic`
  ..      - ✓
  ..      - ✓
  ..      - ✓

  ..    * - :command:`openssh-server`
  ..      - ✓
  ..      - ✓
  ..      - ✓

  ..    * - :command:`webserver-basic`
  ..      -
  ..      - ✓
  ..      - ✓

  ..    * - :command:`application-server`
  ..      -
  ..      - ✓
  ..      - ✓

  ..    * - :command:`database-basic`
  ..      -
  ..      - ✓
  ..      - ✓

  ..    * - :command:`desktop-autostart`
  ..      - ✓
  ..      - ✓
  ..      - ✓

  ..    * - :command:`dev-utils`
  ..      -
  ..    -
  ..    - ✓

"""

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
