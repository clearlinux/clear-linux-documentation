.. _hadoop:

Set up a single node cluster with Hadoop\*
##########################################

This tutorial walks you through the process of installing, configuring, and
running Apache\* Hadoop on |CLOSIA|. The Apache Hadoop software library is a
framework for distributed processing of large data sets across clusters of
computers using simple programming models. It is designed to scale up from
single servers to thousands of machines, with each machine offering local
computation and storage.

Prerequisites
*************

Before following this tutorial, you should follow the
:ref:`bare-metal-install` to ensure you have installed |CLOSIA|.

Before you install any new packages, update |CL| with the following command:

.. code-block:: bash

   sudo swupd update

For the purposes of this tutorial, we will install Hadoop in a single machine
running both the master and slave daemons.

Install Apache Hadoop
*********************

Apache Hadoop is included in the `big-data-basic` bundle. To install the
framework, enter the following command:

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

   .. note:: Remember, you should never modify the files under the
      :file:`/usr/share/defaults` directory since swupd will overwrite them.

Once all configuration files are in :file:`/etc/hadoop`, we must edit them
according to our needs. The first file, :file:`/etc/hadoop/core-site.xml`, is
responsible to inform the Hadoop daemon of where `NameNode` running. The
`NameNode` server is the master server managing the files system namespace
and regulating the clients' access to files.

In this tutorial, our `NameNode` runs in our `localhost`. Follow these steps
to set it up correctly:

#. Open the :file:`/etc/hadoop/core-site.xml` using the editor of your
   choice and modify the file as follows:

   .. code-block:: xml

      <?xml version="1.0" encoding="UTF-8"?>
      <?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
      <configuration>
      <property>
      <name>fs.default.name</name>
      <value>hdfs://localhost:9000</value>
      </property>
      </configuration>

#. Edit :file:`/etc/hadoop/hdfs-site.xml`. This file configures the
   :abbr:`HDFS (Hadoop Distributed File System)` daemons. This includes
   things like the list of permitted and excluded data nodes or the size of
   the blocks. In this example, we are setting the number of block
   replication to 1 from the default of 3 as follows:

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

#. Edit :file:`/etc/hadoop/mapred-site.xml`. This file configures all daemons
   related to MapReduce: `JobTracker` and `TaskTrackers`. With MapReduce,
   Hadoop can process big amounts of data in multiple systems. In our
   example, we set :abbr:`YARN (Yet Another Resource Manager)` as our runtime
   framework for executing MapReduce jobs as follows:

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

#. Edit :file:`/etc/hadoop/yarn-site.xml`. This file configures all daemons
   related to YARN: `ResourceManager` and `NodeManager`. In our example, we
   implement the `mapreduce_shuffle` service, which is the default as follows:

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

Run the Hadoop daemons
**********************

With all the configuration files properly edited, we are ready to start the
daemons.

When we format `NameNode`, it formats the meta-data related to data-nodes.
Thus, all the information on the data nodes is lost and the nodes can be
reused for new data.

#. Format `NameNode` with the following command:

   .. code-block:: bash

      hdfs namenode -format

#. Start the DFS daemons `NameNode` and `DataNodes` with the following command:

   .. code-block:: bash

      start-dfs.sh

#. Start the YARN daemons `ResourceManager` and `NodeManager` with the
   following command:

   .. code-block:: bash

      start-yarn.sh

#. Ensure everything is running as expected with the following command:

   .. code-block:: bash

      jps

**Congratulations!**

Your single node Hadoop cluster is up and running!

