.. _dars:

Data Analytics Reference Stack
##############################

This tutorial shows you how to use the Data Analytics Reference Stack
(DARS), and to optionally build your own images with the baseline Dockerfiles
provided in the `DARS repository`_. Our assumption is that |CL-ATTR| is the
host. However, any system that supports Docker\* containers can be used to
follow these steps.

.. contents::
   :local:
   :depth: 1

The Data Analytics Reference Stack release
******************************************

The Data Analytics Reference Stack provides two pre-built Docker images, available on `Docker Hub`_:

* A |CL|-derived `DARS with OpenBlas`_ stack optimized for `OpenBLAS`_
* A |CL|-derived  `DARS with MKL`_ stack optimized for `MKL`_

We recommend you view the latest component versions for each image in the
:file:`README` found in the `DARS repository`_.  Because |CL| is a rolling
distribution, the package version numbers in the |CL|-based containers may
not be the latest released by |CL|.

Using the Docker Images
***********************

To immediately start using the latest stable DARS images, pull directly
from `Docker Hub`_. For this tutorial we'll use the `Dars with MKL`_ version of the stack.

Once you have downloaded the image, you can run it with

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

Building DARS Images
********************

If you choose to build your own DARS container images, you can customize
them as needed. Use the provided Dockerfile as a baseline. To construct
images with |CL|, start with a |CL| development platform that
has the :command:`containers-basic-dev` bundle installed. Learn more about
bundles and installing them by using :ref:`swupd-guide`.

First, clone the `DARS repository`_ from GitHub.

.. code-block:: bash

   git clone https://github.com/clearlinux/dockerfiles/tree/master/stacks/dars -b master

Then, inside the DARS directory, run :command:`make` to build OpenBLAS and
MKL images, and run :command:`make baseline` to build the baseline CentOS
image. Depending on the system, it may take a while to finish building.
Once completed, check the resulting images with :command:`Docker`

.. code-block:: bash

   docker images | grep dars

You can use any of the resulting images to launch fully functional
containers.  If you need to customize the containers, you can edit the
provided :file:`Dockerfile`.


.. _DARS repository:  https://github.com/clearlinux/dockerfiles/tree/master/stacks/dars
.. _Docker Hub: https://hub.docker.com/
.. _OpenBLAS: http://www.openblas.net/
.. _MKL: https://software.intel.com/en-us/mkl
.. _CentOS: https://www.centos.org/
.. _DARS with OpenBLAS: https://hub.docker.com/r/clearlinux/stacks-dars-openblas/
.. _DARS with MKL: https://hub.docker.com/r/clearlinux/stacks-dars-mkl/
.. _DARS on CentOS: https://hub.docker.com/r/clearlinux.......
