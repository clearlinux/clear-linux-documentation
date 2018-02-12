.. _spark:

Set up a standalone cluster system using Spark*\
################################################

This tutorial walks you through the process of installing, configuring, and running Apache* Spark on Clear Linux OS for Intel(r) Architecture. Apache Spark is a fast and general-purpose cluster computing system. It provides high-level APIs in Java, Scala, Python and R, and an optimized engine that supports general execution graphs. It also supports a rich set of higher-level tools including Spark SQL for SQL and structured data processing, MLlib for machine learning, GraphX for graph processing, and Spark Streaming.

Prerequisites
*************

Before following this tutorial, you should follow the :ref:`bare-metal-install` to ensure you have installed |CLOSIA|.

Before you install any new packages, update |CL| with the following command:

.. code-block:: bash

   $ sudo swupd update

For the purposes of this tutorial, we will install Spark in a single machine running both the master and a worker daemons.

Install Apache Spark
********************

Apache Spark is included in the *big-data-basic* bundle. To install the framework, enter the following command:

.. code-block:: bash

   $ sudo swupd bundle-add big-data-basic

Configure Apache Spark
**********************

#. To create the configuration directory, enter the following command:

   .. code-block:: bash

      $ sudo mkdir /etc/spark

#. Copy the default templates from */usr/share/defaults/spark* to */etc/spark* with the following command:

   .. code-block:: bash

      $ sudo cp /usr/share/defaults/spark/* /etc/spark

   .. note:: Since |CL| is a stateless system, you should never modify the files under the */usr/share/defaults* directory. The software updater will overwrite those files.

Once all the configuration templates are in */etc/spark*, we must edit them to fit our needs.

#. Create the basic configuration files from the default templates with the following commands:

   .. code-block:: bash

      $ sudo cp /etc/spark/spark-defaults.conf.template /etc/spark/spark-defaults.conf
      $ sudo cp /etc/spark/spark-env.sh.template /etc/spark/spark-env.sh
      $ sudo cp /etc/spark/log4j.properties.template /etc/spark/log4j.properties

#. Open the */etc/spark/spark-env.sh* file using the editor of your choice and add the *SPARK_MASTER_HOST* variable with your localhost IP address as follows (substitute the address with your actual value. You can view this with the command *hostname -I*):

   .. code-block:: xml

      SPARK_MASTER_HOST="10.300.200.100"
    
   .. note:: Although setting the *SPARK_MASTER_HOST* variable to an IP address
      is not required to run Spark in standalone mode, by doing so now you
      will be able to navigate through the master's web UI pages without
      issues and view information there from both the worker and the
      application that will be started in next steps of this tutorial.
    
#. Open the */etc/spark/spark-defaults.conf* file using the editor of your choice and add the master host's IP Address and port *7077* to the variable *spark.master* (substitute the address with the value you entered in previous step):

   .. code-block:: xml

      spark.master    spark://10.300.200.100:7077
    
Start the master server and a worker
************************************
    
#. Start the master server by executing:

   .. code-block:: bash

      $ sudo /usr/share/apache-spark/sbin/./start-master.sh
    
#. Start one worker and connect it to the master through port *7077* via the following command (substitute the IP address with the one you entered in step 2 from the previous section):

   .. code-block:: bash

      $ sudo /usr/share/apache-spark/sbin/./start-slave.sh spark://10.300.200.100:7077


You should now be able to view the worker information in the master's web UI by using the internet browser of your choice and entering the master's IP address, followed by the port *8080* in the address bar (substitute the address with the value entered in step 4 from previous section):

   .. code-block:: xml

      http://10.300.200.100:8080
    
Run the Spark worcount example
******************************

#. Run the wordcount example using a file in your local host and output the results to a new file by using the following command (substitute the file path and name with actual values in your host):

   .. code-block:: bash

      $ sudo spark-submit /usr/share/apache-spark/examples/src/main/python/wordcount.py ~/Documents/example_file > ~/Documents/results
    
You should now be able to view the application information in the master's web UI by using the internet browser of your choice and entering the master's IP address, followed by the port *8080* in the address bar (substitute the address with the value entered in previous sections). The results of the *wordcount* application on the input file can be viewed in the output file.
    
Congratulations!

You successfully installed and setup a standalone Apache Spark cluster. Additionally, you ran a simple wordcount example.
