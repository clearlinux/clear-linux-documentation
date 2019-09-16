.. _hadoop:

Apache\* Hadoop\*
#################

This tutorial explains the process of installing, configuring, and
running Apache Hadoop on |CL-ATTR|.

.. contents::
   :local:
   :depth: 1

Description
***********

For this tutorial, you will install Hadoop in a single machine
running both the master and slave daemons.

The Apache Hadoop software library is a framework for distributed processing
of large data sets across clusters of computers using simple programming
models. It is designed to scale up from single servers to thousands of
machines, with each machine offering local computation and storage.

Prerequisites
*************

* :ref:`bare-metal-install-desktop`

* In |CL|, run :command:`swupd update`


Install Apache Hadoop
*********************

Apache Hadoop is included in the :command:`big-data-basic` bundle. To install
the framework, enter the following command:

.. code-block:: bash

   sudo swupd bundle-add big-data-basic

Configure Apache Hadoop
***********************

#. To create the configuration directory, enter the following command:

   .. code-block:: bash

      sudo mkdir /etc/hadoop

#. Copy the defaults from :file:`/usr/share/defaults/hadoop` to
   :file:`/etc/hadoop` with the following command:

   .. code-block:: bash

      $ sudo cp /usr/share/defaults/hadoop/* /etc/hadoop

   .. note:: Since |CL| is a stateless system, never modify the
      files under the :file:`/usr/share/defaults` directory. The software
      updater will overwrite those files.

   Once all the configuration files are in :file:`/etc/hadoop`, edit them to
   fit your needs. The `NameNode` server is the master server that manages the
   namespace of the files' system and regulates the clients' access to files.
   The first file to be edited, :file:`/etc/hadoop/core-site.xml`, informs the
   Hadoop daemon where `NameNode` is running. In this tutorial, `NameNode` runs
   in the `localhost`.

#. Open the :file:`/etc/hadoop/core-site.xml` file using any editor and modify
   the file as follows:

   .. code-block:: xml

      <?xml version="1.0" encoding="UTF-8"?>
      <?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
      <configuration>
      <property>
      <name>fs.default.name</name>
      <value>hdfs://localhost:9000</value>
      </property>
      </configuration>

#. Edit the :file:`/etc/hadoop/hdfs-site.xml` file. This file configures the
   :abbr:`HDFS (Hadoop Distributed File System)` daemons. This configuration
   includes the list of permitted and excluded data nodes and the size of
   those blocks. For this example, set the number of block replication to 1
   from the default of 3 as follows:

   .. code-block:: xml
      :emphasize-lines: 6

      <?xml version="1.0" encoding="UTF-8"?>
      <?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
      <configuration>
      <property>
      <name>dfs.replication</name>
      <value>1</value>
      </property>
      <property>
      <name>dfs.permission</name>
      <value>false</value>
      </property>
      </configuration>

#. Edit the :file:`/etc/hadoop/mapred-site.xml` file. This file configures
   all daemons related to `MapReduce`: `JobTracker` and `TaskTrackers`. With
   `MapReduce`, Hadoop can process big amounts of data in multiple systems. In
   our example, we set :abbr:`YARN (Yet Another Resource Manager)` as our
   runtime framework for executing `MapReduce` jobs as follows:

   .. code-block:: xml
      :emphasize-lines: 5,6

      <?xml version="1.0" encoding="UTF-8"?>
      <?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
      <configuration>
      <property>
      <name>mapreduce.framework.name</name>
      <value>yarn</value>
      </property>
      </configuration>

#. Edit the :file:`/etc/hadoop/yarn-site.xml` file. This file configures all
   daemons related to `YARN`: `ResourceManager` and `NodeManager`. In our
   example, we implement the `mapreduce_shuffle` service, which is the
   default as follows:

   .. code-block:: xml
      :emphasize-lines: 4,5,8,9

      <?xml version="1.0"?>
      <configuration>
      <property>
      <name>yarn.nodemanager.aux-services</name>
      <value>mapreduce_shuffle</value>
      </property>
      <property>
      <name>yarn.nodemanager.auxservices.mapreduce.shuffle.class</name>
      <value>org.apache.hadoop.mapred.ShuffleHandler</value>
      </property>
      </configuration>

Configure your SSH key
**********************

#. Create a SSH key. If you already have one, skip this step.

   .. code-block:: bash

      sudo ssh-keygen -t rsa


#. Copy the key to your authorized keys.

   .. code-block:: bash

      sudo cat /root/.ssh/id_rsa.pub | sudo tee -a /root/.ssh/authorized_keys

#. Log into the localhost. If no password prompt appears, you are ready to
   run the Hadoop daemons.

   .. code-block:: bash

      sudo ssh localhost

Run the Hadoop daemons
**********************

With all the configuration files properly edited, you are ready to start the
daemons.

When you format the `NameNode` server, it formats the metadata related to
data nodes. Thus, all the information on the data nodes is lost and the nodes
can be reused for new data.

#. Format the `NameNode` server with the following command:

   .. code-block:: bash

      sudo hdfs namenode -format

#. Start the DFS in `NameNode` and `DataNodes` with the following command:

   .. code-block:: bash

      sudo start-dfs.sh

   The console output should be similar to:

   .. code-block:: console

      Starting namenodes on [localhost]
      The authenticity of host 'localhost (::1)' can't be established.
      ECDSA key fingerprint is
      SHA256:97e+7TnomsS9W7GjFPjzY75HGBp+f1y6sA+ZFcOPIPU.
      Are you sure you want to continue connecting (yes/no)?

#. Enter `yes` to continue.

#. Start the `YARN` daemons `ResourceManager` and `NodeManager` with the
   following command:

   .. code-block:: bash

      sudo start-yarn.sh

#. Ensure everything is running as expected with the following command:

   .. code-block:: bash

      sudo jps

   The console output should be similar to:

   .. code-block:: console

      22674 DataNode
      26228 Jps
      22533 NameNode
      23046 ResourceManager
      22854 SecondaryNameNode
      23150 NodeManager

Run the MapReduce wordcount example
***********************************

#. Create the input directory.

   .. code-block:: bash

      sudo hdfs dfs -mkdir -p /user/root/input

#. Copy a file from the local file system to the HDFS.

   .. code-block:: bash

      sudo hdfs dfs -copyFromLocal local-file /user/root/input

#. Run the `wordcount` example.

   .. code-block:: bash

      sudo hadoop jar /usr/share/hadoop/mapreduce/hadoop-mapreduce-examples-2.8.0.jar wordcount input output

#. Read the output file "part-r-00000". This file contains the number of times
   each word appears in the file.

   .. code-block:: bash

      sudo hdfs dfs -cat /user/root/output/part-r-00000

**Congratulations!**

You have successfully installed and setup a single node Hadoop cluster.
Additionally, you ran a simple wordcount example.

Your single node Hadoop cluster is up and running!