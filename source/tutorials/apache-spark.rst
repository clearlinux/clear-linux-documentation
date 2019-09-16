  .. _spark:

Apache\* Spark\*
################

This tutorial describes how to install, configure, and run Apache Spark on
|CL-ATTR| on a single machine running the master daemon and a worker daemon.

.. contents::
   :local:
   :depth: 1

Description
***********

Apache Spark is a fast, general-purpose cluster computing system with
the following features:

*  Provides high-level APIs in Java\*, Scala\*, Python\*, and R\*.
*  Includes an optimized engine that supports general execution graphs.
*  Supports high-level tools including Spark SQL, MLlib, GraphX, and Spark
   Streaming.


Prerequisites
*************

* |CL| installed on your host system.

  For detailed instructions on installing |CL| on a bare metal system, visit
  the :ref:`bare metal installation guide <bare-metal-install-desktop>`.

* Before installing any new packages, update |CL| with the following command:

   .. code-block:: bash

      sudo swupd update

Install Apache Spark
********************

Apache Spark is included in the :command:`big-data-basic` bundle. To install the
framework, run the following command:

.. code-block:: bash

   sudo swupd bundle-add big-data-basic

Configure Apache Spark
**********************

#. Create the configuration directory:

   .. code-block:: bash

      sudo mkdir /etc/spark

#. Copy the default templates from :file:`/usr/share/defaults/spark` to
   :file:`/etc/spark`:

   .. code-block:: bash

      sudo cp /usr/share/defaults/spark/* /etc/spark

   .. note:: Since |CL| is a stateless system, you should never modify the
      files under the :file:`/usr/share/defaults` directory. The software
      updater overwrites those files.

#. Copy the template files shown below to create custom configuration files:

   .. code-block:: bash

      sudo cp /etc/spark/spark-defaults.conf.template /etc/spark/spark-defaults.conf
      sudo cp /etc/spark/spark-env.sh.template /etc/spark/spark-env.sh
      sudo cp /etc/spark/log4j.properties.template /etc/spark/log4j.properties

#. Edit the :file:`/etc/spark/spark-env.sh` file and add the
   :envvar:`SPARK_MASTER_HOST` variable. Replace the example address below
   with your localhost IP address. View your IP address using the
   :command:`hostname -I` command.

   .. code-block:: bash

      SPARK_MASTER_HOST="10.300.200.100"

   .. note:: This optional step enables the master's web user interface to
      view information needed later in this tutorial.

#. Edit the :file:`/etc/spark/spark-defaults.conf` file and update the
   :envvar:`spark.master` variable with the `SPARK_MASTER_HOST` address and port
   `7077`.

   .. code-block:: bash

      spark.master    spark://10.300.200.100:7077

Start the master server and a worker daemon
*******************************************

#. Start the master server:

   .. code-block:: bash

      sudo /usr/share/apache-spark/sbin/./start-master.sh

#. Start one worker daemon and connect it to the master using the
   :envvar:`spark.master` variable defined earlier:

   .. code-block:: bash

      sudo /usr/share/apache-spark/sbin/./start-slave.sh spark://10.300.200.100:7077

#. Open an internet browser and view the worker daemon information using
   the master's IP address and port `8080`:

   .. code-block:: bash

      http://10.300.200.100:8080

Run the Spark wordcount example
*******************************

#. Run the wordcount example using a file on your local host and output the
   results to a new file with the following command:

   .. code-block:: bash

      sudo spark-submit /usr/share/apache-spark/examples/src/main/python/wordcount.py ~/Documents/example_file > ~/Documents/results

#. Open an internet browser and view the application information using
   the master's IP address and port `8080`:

   .. code-block:: bash

      http://10.300.200.100:8080

#. View the results of the wordcount application in the :file:`~/Documents/results` file.

**Congratulations!**

You have successfully installed and set up a standalone Apache Spark cluster,
and ran a simple wordcount example.
