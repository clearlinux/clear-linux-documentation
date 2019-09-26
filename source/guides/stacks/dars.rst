.. _dars:

Data Analytics Reference Stack
##############################

This guide explains how to use the :abbr:`DARS (Data Analytics Reference Stack)`,
and to optionally build your own DARS container image.

Any system that supports Docker\* containers can be used with DARS. The steps
in this guide use |CL-ATTR| as the host system.

.. contents::
   :local:
   :depth: 1

Overview
********

The Data Analytics Reference Stack (DARS) provides developers and enterprises a straightforward, highly optimized software stack for storing and processing large amounts of data.  More detail is available on the `DARS architecture and performance benchmarks`_.

Stack Features
==============

The Data Analytics Reference Stack provides two pre-built Docker images,
available on `Docker Hub`_:

* A |CL|-derived `DARS with OpenBlas`_ stack optimized for `OpenBLAS`_
* A |CL|-derived  `DARS with Intel® MKL`_ stack optimized for `MKL`_ (Intel® Math Kernel Library)

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

Launching the Image
===================

#. To use the latest stable DARS images, pull an image
   directly from `Docker Hub`_. This example uses the
   `DARS with Intel® MKL`_ Docker image.

   .. code-block:: bash

      docker pull clearlinux/stacks-dars-mkl


#. Once you have downloaded the image, you can run it with

   .. code-block:: bash

      docker run -it --ulimit nofile=1000000:1000000 --name mkl <name of image>

   This will launch the image and drop you into a bash shell inside the container. The :command:`--ulimit nofile=` parameter is required in order to increase the allowed number of open files for the Apache Spark engine.

   If you need to verify the name of the DARS image, you can use the :command:`docker image ls` command to see which images reside on your system.

   .. code-block:: bash

      docker image ls


   .. code-block:: console

      REPOSITORY                                                   TAG                 IMAGE ID            CREATED             SIZE
      clearlinux/stacks-dars-mkl                                   test-img            49a70a22231f        23 hours ago        2.66GB
      ubuntu                                                       latest              2ca708c1c9cc        7 days ago          64.2MB
      katadocker/kata-deploy                                       latest              bd6dc92f8060        7 days ago          673MB
      clearlinux/stacks-dars-mkl                                   latest              2c9555536d5f        4 weeks ago         2.62GB



Building DARS images
====================

If you choose to build your own DARS container images, you can customize them as needed. Use the :file:`Dockerfile` included in the Github\* repository as your baseline. You can also follow :ref:`custom-app-container` for details on customizing containers on |CL|.

To construct images with |CL|, start with a |CL| development platform that has the :command:`containers-basic-dev` bundle installed. Learn more about bundles and installing them by using :ref:`swupd-guide`.

#. The `Data Analytics Reference Stack`_ is part of the |CL| Project GitHub\* repository. Clone the :file:`dockerfiles` repository.

   .. code-block:: bash

      git clone https://github.com/clearlinux/dockerfiles.git

#. Inside the :file:`stacks/dars/mkl` directory, use docker with the :file:`Dockerfile` to build the  MKL image.

   .. code-block:: bash

      cd ./dockerfiles/stacks/dlrs/mkl
      docker build --no-cache -t clearlinux/stacks-dars-mkl .


#. Once completed, check the resulting images with :command:`Docker`

   .. code-block:: bash

       docker images | grep dars

#. You can use any of the resulting images to launch fully functional containers. If you need to customize the containers, you can edit the provided :file:`Dockerfile`.

Using Apache Spark\* in DARS
****************************

After launching the container, you can start Apache Spark with either the Scala or PySpark environment.  For these examples we will use PySpark, which is the Python\* API for Apache Spark.

.. code-block:: bash

  pyspark


Launching is as simple as this.  Depending on your system configuration and capabilities, you may need to define proxy or memory allocation settings on the command line or in a config file for optimal performance. Refer to the `Apache Spark documentation`_ for more detail.

After executing :command:`pyspark`, you will see output similar to this.

.. code-block:: console

  root@fd5155b89857 /root # pyspark
    Welcome to
        ____              __
       / __/__  ___ _____/ /__
       _\ \/ _ \/ _ `/ __/  '_/
      /__ / .__/\_,_/_/ /_/\_\   version 2.4.0
         /_/

    Using Python version 3.7.4 (default, Jul 13 2019 06:59:17)
    SparkSession available as 'spark'.
    >>>


Execute code directly in PySpark
================================

A simple example for verifying that pyspark is working correctly is to run a small python function from a `PySpark getting started guide`_ to estimate the value of Pi. Run these lines in the PySpark shell.

.. code-block:: console

   import random
   NUM_SAMPLES = 100000000
   def inside(p):
    x, y = random.random(), random.random()
    return x*x + y*y < 1

   count = sc.parallelize(range(0, NUM_SAMPLES)).filter(inside).count()
   pi = 4 * count / NUM_SAMPLES
   print(“Pi is roughly”, pi)


Run Python programs with spark-submit
=====================================

You can also run python scripts in Apache Spark from the command line.  We'll use the Apache Spark example found in the :file:`/usr/share/apache-spark/examples/src/main/python/pi.py` file.  Note that we have turned off the INFO and WARN messages in Apache Spark for this example.

.. code-block:: console

   #spark-submit /usr/share/apache-spark/examples/src/main/python/pi.py
   Config directory: /usr/share/defaults/spark/
   Pi is roughly 3.134700

DARS Usecase example
====================

The DARS container is used in conjunction with the Deep Learning Reference Stack container to implement a real world use case.  Refer to the `Github Issue Classification`_ Usecase found in the `stacks-usecase`_ repository for a walkthrough.  This usecase is implemented using the Scala environment, rather than PySpark.




.. _Data Analytics Reference Stack: https://github.com/clearlinux/dockerfiles/tree/master/stacks/dars

.. _Docker Hub: https://hub.docker.com/

.. _OpenBLAS: http://www.openblas.net/

.. _MKL: https://software.intel.com/en-us/mkl

.. _CentOS: https://www.centos.org/

.. _DARS with OpenBLAS: https://hub.docker.com/r/clearlinux/stacks-dars-openblas/

.. _DARS with Intel® MKL: https://hub.docker.com/r/clearlinux/stacks-dars-mkl/

.. _DARS architecture and performance benchmarks: https://clearlinux.org/stacks/data-analytics-stack-v1

.. _DARS Terms of Use: https://clearlinux.org/stacks/data-analytics/terms-of-use

.. _PySpark getting started guide: https://towardsdatascience.com/how-to-get-started-with-pyspark-1adc142456ec

.. _Apache Spark documentation: https://spark.apache.org/docs/latest/

.. _stacks-usecase: https://github.com/intel/stacks-usecase

.. _Github Issue Classification: https://github.com/intel/stacks-usecase/tree/master/github-issue-classification
