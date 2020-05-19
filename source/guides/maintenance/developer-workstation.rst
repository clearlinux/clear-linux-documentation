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
bundle :ref:`*os-clr-on-clr* <enable-user-space>`. However, you may want to deploy a leaner OS with only bundles relevant to your project.

Use the **Developer Profiles** tabs to start installing *suggested bundles*
based on your role or project. Installing any ``dkms`` bundle gives all the
tools you need to start. Consider these profiles as a starting point.

.. tip:: 
   
   Click on a bundle to learn how to install it using :command:`swupd`. 

.. tabs::

   .. tab:: AI/ML Engineer

      .. list-table:: 
         :widths: 50, 50
         :header-rows: 1

         * - Function
           - Bundle

         * - Build machine learning applications with a full suite of libraries.
           - `machine-learning-basic <https://clearlinux.org/software/bundle/machine-learning-basic/>`_

         * - Build machine learning applications with PyTorch, an optimized tensor library for deep learning.
           - `machine-learning-pytorch <https://clearlinux.org/software/bundle/machine-learning-pytorch/>`_

         * - Build machine learning applications using Tensorflow, a library for numerical computation using deep neural networks.
           - `machine-learning-tensorflow <https://clearlinux.org/software/bundle/machine-learning-tensorflow/>`_

         * - Web-based, interactive tools for machine learning.
           - `machine-learning-web-ui <https://clearlinux.org/software/bundle/machine-learning-web-ui/>`_

         * - Machine learning Docker container.
           - `machine-learning <https://clearlinux.org/software/docker/machine-learning-ui/>`_

         * - Pre-built Python libraries for Data Science.
           - `python-extras <https://clearlinux.org/software/bundle/python-extras>`_

         * - API helper for cloud access.
           - `cloud-api <https://clearlinux.org/software/bundle/cloud-api/>`_

   .. tab:: Computer Vision Engineer

      .. list-table:: 
         :widths: 50, 50
         :header-rows: 1

         * - Function
           - Bundle

         * - Build computer vision applications.
           - `computer-vision-basic <https://clearlinux.org/software/bundle/computer-vision-basic/>`_

         * - Work with deep learning and edge-optimized models.
           - `computer-vision-models <https://clearlinux.org/software/bundle/computer-vision-models/>`_

         * - API helper for cloud access.
           - `cloud-api <https://clearlinux.org/software/bundle/cloud-api/>`_

         * - Run container applications from Dockerhub in lightweight virtual machines.
           - `containers-virt <https://clearlinux.org/software/bundle/containers-virt>`_

         * - All content for pkgconfig file opencv.pc.
           - `devpkg-opencv <https://clearlinux.org/software/bundle/devpkg-opencv/>`_

         * - *Refer also to Cloud Orchestration Engineer*
           - 

   .. tab:: Cloud Orchestration Engineer

      .. list-table:: 
         :widths: 50, 50
         :header-rows: 1

         * - Function
           - Bundle

         * - Contains Clear Linux\* OS native software for cloud.
           - `ethtool <https://clearlinux.org/software/bundle/ethtool/>`_

         * - Utilities for controlling TCP/IP networking and traffic control.
           - `iproute2 <https://clearlinux.org/software/bundle/iproute2/>`_

         * - API helper for cloud access.
           - `cloud-api <https://clearlinux.org/software/bundle/cloud-api/>`_

         * - C++ runtime support.
           - `libstdcpp <https://clearlinux.org/software/bundle/libstdcpp/>`_

         * - Load and enumerate PKCS#11 modules.
           - `p11-kit <https://clearlinux.org/software/bundle/p11-kit/>`_

   .. tab:: Kernel Developer

      .. list-table:: 
         :widths: 50, 50
         :header-rows: 1

         * - Function
           - Bundle

         * - Installs kernel, initrd, kernel config, system map; creates a bootloader entry.
           - `kernel-install <https://clearlinux.org/software/bundle/kernel-install/>`_

         * - Support module for building/loading via Dynamic Kernel Module System (DKMS) in LTS kernel.
           - `kernel-lts-dkms <https://clearlinux.org/software/bundle/kernel-lts-dkms/>`_

         * - Support module for building/loading via Dynamic Kernel Module System (DKMS) in native kernel.
           - `kernel-native-dkms <https://clearlinux.org/software/bundle/kernel-native-dkms/>`_

         * - Support module for building/loading via Dynamic Kernel Module System (DKMS) in AWS kernel.
           - `kernel-aws-dkms <https://clearlinux.org/software/bundle/kernel-aws-dkms/>`_

         * - Run the Kernel-based Virtual Machine (KVM) with |CL| as a guest under KVM.
           - `kernel-kvm <https://clearlinux.org/software/bundle/kernel-kvm/>`_
      
         * - Linux Test Project.
           - `ltp <https://clearlinux.org/software/bundle/ltp/>`_

   .. tab:: Maker Developer

      .. list-table:: 
         :widths: 50, 50
         :header-rows: 1

         * - Function
           - Bundle

         * - Basic tools for makers and experimenters.
           - `maker-basic <https://clearlinux.org/software/bundle/maker-basic/>`_

         * - GIS/Mapping tools for makers.
           - `maker-gis <https://clearlinux.org/software/bundle/maker-gis/>`_

         * - Electronic Design Tool.
           - `Fritzing <https://clearlinux.org/software/flathub/fritzing>`_

         * -  Open-source electronics prototyping platform.
           - `arduino-ide <https://clearlinux.org/software/flathub/arduino-ide/>`_

   .. tab:: System Administrator

      .. list-table:: 
         :widths: 50, 50
         :header-rows: 1

         * - Function
           - Bundle

         * - Run popular terminal text editors.
           - `editors <https://clearlinux.org/software/bundle/editors/>`_

         * - Run network utilities and modify network settings.
           - `network-basic <https://clearlinux.org/software/bundle/network-basic/>`_

         * - Run a secure shell (SSH) server for access from remote machines.
           - `openssh-server <https://clearlinux.org/software/bundle/openssh-server/>`_

         * - Run an HTTP server.
           - `nginx <https://clearlinux.org/software/bundle/nginx>`_

         * - Run an application server via HTTP.
           - `application-server <https://clearlinux.org/software/bundle/application-server/>`_

         * - Run a SQLite database.
           - `sqlite <https://clearlinux.org/software/bundle/sqlite>`_

         * - Bundle to automatically launch the GUI upon boot.
           - `desktop-autostart <https://clearlinux.org/software/bundle/desktop-autostart/>`_

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

Related topics
--------------

* `Developer Tooling Framework`_ for |CL|
* `Bundle Definition Files`_

.. _Bundle Definition Files: https://github.com/clearlinux/clr-bundles

.. _Developer Tooling Framework: https://github.com/clearlinux/common
