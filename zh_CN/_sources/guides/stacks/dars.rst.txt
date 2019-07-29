.. _dars:

Data Analytics Reference Stack
##############################

This guide explains how to use the :abbr:`DARS (Data Analytics Reference Stack)`,
and to optionally build your own DARS container image.

Any system that supports Docker\* containers can be used with DARS. This steps
in this guide use |CL-ATTR| as the host system.

.. contents::
   :local:
   :depth: 1

The Data Analytics Reference Stack release
******************************************

The Data Analytics Reference Stack (DARS) provides developers and enterprises a straightforward, highly optimized software stack for storing and processing large
amounts of data.  More detail is available on the
`DARS architecture and performance benchmarks`_.

The Data Analytics Reference Stack provides two pre-built Docker images,
available on `Docker Hub`_:

* A |CL|-derived `DARS with OpenBlas`_ stack optimized for `OpenBLAS`_
* A |CL|-derived  `DARS with Intel® MKL`_ stack optimized for `MKL`_

We recommend you view the latest component versions for each image in the
:file:`README` found in the `Data Analytics Reference Stack`_ GitHub\*
repository. Because |CL| is a rolling distribution, the package version numbers
in the |CL|-based containers may not be the latest released by |CL|.

.. note::

   The Data Analytics Reference Stack is a collective work, and each piece
   of software within the work has its own license.  Please see the
   `DARS Terms of Use`_ for more details about licensing and usage of the Data
   Analytics Reference Stack.

Using the Docker images
***********************

#. To immediately start using the latest stable DARS images, pull an image
   directly from `Docker Hub`_. This example uses the
   `DARS with Intel® MKL`_ Docker image.

#. Once you have downloaded the image, you can run it with

   .. code-block:: bash

      docker run -it --ulimit nofile=1000000:1000000 --name mkl <name of image>

   This will launch the image and drop you into a bash shell inside the
   container.  You will see output similar to the following:

   .. code-block:: console

      root@fd5155b89857 /root # spark-shell
      spark-shell
      Config directory: /usr/share/defaults/spark/
      Welcome to
        ____              __
       / __/__  ___ _____/ /__
       _\ \/ _ \/ _ `/ __/  '_/
      /___/ .__/\_,_/_/ /_/\_\   version 2.4.0
         /_/

      Using Scala version 2.12.7 (OpenJDK 64-Bit Server VM, Java 1.8.0-internal)
      Type in expressions to have them evaluated.
      Type :help for more information.

      scala>

   The :command:`--ulimit nofile` parameter is currently required in order to
   increase the number of open files opened at certain point by the spark
   engine.

Building DARS images
********************

If you choose to build your own DARS container images, you can customize
them as needed. Use the provided Dockerfile as a baseline.

To construct images with |CL|, start with a |CL| development platform that
has the :command:`containers-basic-dev` bundle installed. Learn more about
bundles and installing them by using :ref:`swupd-guide`.

#. Clone the `Data Analytics Reference Stack`_ GitHub\* repository.

   .. code-block:: bash

      git clone https://github.com/clearlinux/dockerfiles/tree/master/stacks/dars -b master

#. Inside the DARS directory, run :command:`make` to build OpenBLAS and MKL images.

   .. code-block:: bash

      make

   Run :command:`make baseline` to build the baseline CentOS image. Depending on
   the system, it may take a while to finish building.

   .. code-block:: bash

      make baseline

#. Once completed, check the resulting images with :command:`Docker`

   .. code-block:: bash

      docker images | grep dars

#. You can use any of the resulting images to launch fully functional containers.
   If you need to customize the containers, you can edit the provided :file:`Dockerfile`.

.. _Data Analytics Reference Stack: https://github.com/clearlinux/dockerfiles/tree/master/stacks/dars

.. _Docker Hub: https://hub.docker.com/

.. _OpenBLAS: http://www.openblas.net/

.. _MKL: https://software.intel.com/en-us/mkl

.. _CentOS: https://www.centos.org/

.. _DARS with OpenBLAS: https://hub.docker.com/r/clearlinux/stacks-dars-openblas/

.. _DARS with Intel® MKL: https://hub.docker.com/r/clearlinux/stacks-dars-mkl/

.. _DARS architecture and performance benchmarks: https://clearlinux.org/stacks/data-analytics-stack-v1

.. _DARS Terms of Use: https://clearlinux.org/stacks/data-analytics/terms-of-use
