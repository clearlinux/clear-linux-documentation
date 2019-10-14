.. _dars:

Data Analytics Reference Stack
##############################

This guide explains how to use the :abbr:`DARS (Data Analytics Reference Stack)`, and to optionally build your own DARS container image.

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
:file:`releasenote` found in the `Data Analytics Reference Stack`_ GitHub\*
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


#. Once you have downloaded the image, you can run it with this command, which will launch the image and drop you into a bash shell inside the container.

   .. code-block:: bash

      docker run -it --ulimit nofile=1000000:1000000 --name mkl --network host --rm -i -t <name-of-image>


   Command Flags

   :command:`--ulimit nofile=` is required in order to increase the allowed number of open files for the Apache Spark\* engine.

   :command:`--name` can be any name of your choice.  This guide is using `mkl`

   :command:`--network host` flag is for simplicity, so the host machine's IP address can be used to access the container.

   If you need to verify the name of the DARS image for the <name-of-image> flag, you can use the :command:`docker image ls` command to see which images reside on your system.

   .. code-block:: bash

      docker image ls


   .. code-block:: console

      REPOSITORY                                                   TAG                 IMAGE ID            CREATED             SIZE
      clearlinux/stacks-dars-mkl                                   test-img            49a70a22231f        23 hours ago        2.66GB
      ubuntu                                                       latest              2ca708c1c9cc        7 days ago          64.2MB
      katadocker/kata-deploy                                       latest              bd6dc92f8060        7 days ago          673MB
      clearlinux/stacks-dars-mkl                                   latest              2c9555536d5f        4 weeks ago         2.62GB




.. note::

   All of the DARS components are compiled on Open JDK11\*. The container will have preinstalled JDK11 at :file:`/usr/lib/jvm/java-1.11.0-openjdk/` and it has been set as the default Java version. It is worth mentioning that the containers also contain Open JDK8, but we won't be using it in this guide.


Building DARS images
====================

If you choose to build your own DARS container images, you can customize them as needed. Use the :file:`Dockerfile` included in the Github\* repository as your baseline.

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

.. note::

   The environment variables for Apache Hadoop* and Apache Spark have been configured in the Dockerfile for the DARS container. For Apache Hadoop\* use :file:`/etc/hadoop` as `HADOOP_CONF_DIR` folder. For Apache Spark use :file:`/etc/spark` as `SPARK_CONF_DIR` folder.


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


Using Apache Hadoop in DARS
***************************

Apache Hadoop is an open source framework allowing for distributed processing of large data sets across clusters of computers using simple programming models. This framework is designed to scale up from a few servers to thousands of machines, each offering local computation and storage.

Single Node Hadoop Cluster Setup
================================

In this mode, all the daemons involved i.e. the DataNode, NameNode, TaskTracker and JobTracker run as Java processes on the same machine. This setup is useful for developing and testing Apache Hadoop applications.

The components of an Apache Hadoop Cluster are described below:

* NameNode manages HDFS storage. HDFS exposes a filesystem namespace and allows user data to be stored in files. Internally a file is split into one or more blocks and these blocks are stored in a set of DataNodes.
* DataNode is also known as Slave node, it is responsible for storing and managing the data in that node and responds to the NameNode for all filesystem operations.
* JobTracker is a master which creates and runs the job through tasktrackers. It also tracks resource availability and task lifecycle management.
* TaskTracker manages the processing resources on each worker node and send status updates to the JobTracker periodically.


Configuration
=============

#. To setup a single node cluster we need to run a DARS container with the following flags:

   .. code-block:: bash

      docker run --ulimit nofile=1000000:1000000 -ti --rm --network host clearlinux/stacks-dars-mkl cp -r -n /usr/share/defaults/hadoop/* /etc/hadoop

#. In the running container, set configuration in the :file:`/etc/hadoop/mapred-site.xml` file

   .. code-block:: xml

      <configuration>
          <property>
              <name>mapreduce.framework.name</name>
              <value>yarn</value>
          </property>

          <property>
              <name>yarn.app.mapreduce.am.env</name>
              <value>HADOOP_MAPRED_HOME=${HADOOP_HOME}</value>
          </property>

          <property>
              <name>mapreduce.map.env</name>
              <value>HADOOP_MAPRED_HOME=${HADOOP_HOME}</value>
          </property>

          <property>
              <name>mapreduce.reduce.env</name>
              <value>HADOOP_MAPRED_HOME=${HADOOP_HOME}</value>
          </property>
       </configuration>

#. Set up the :file:`/etc/hadoop/yarn-site.xml` as follows

   .. code-block:: xml

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

Start the Apache Hadoop daemons
===============================

#. Format the NameNode server using this command:

   .. code-block:: bash

      hdfs namenode -format

#. Start the Apache Hadoop services

   HDFS Namenode service :

   .. code-block:: bash

      hdfs --daemon start namenode


   HDFS Datanode service :

   .. code-block:: bash

      hdfs --daemon start datanode


   Yarn ResourceManager :

   .. code-block:: bash

      yarn --daemon start resourcemanager


   Yarn NodeManager :

   .. code-block:: bash

      yarn --daemon start nodemanager


   jobhistory service :

   .. code-block:: bash

      mapred --daemon start historyserver

#. Verify the nodes are alive with this command:


   .. code-block:: bash

      yarn node -list 2

   Your output will look similar to:

   .. code-block:: console

      Total Nodes:1
         Node-Id             Node-State Node-Http-Address       Number-of-Running-Containers
      <hostname>:43489            RUNNING <hostname>:8042                      0


Run an example
==============

Apache Hadoop comes packages with a set of example  applications. In this example we will show how to use the cluster to calculate Pi. The JAR file containing the compiled class can be found on your running DARS container at :file:`/usr/share/hadoop/mapreduce/hadoop-mapreduce-examples-3.2.0.jar`


.. code-block:: bash

   hadoop jar /usr/share/hadoop/mapreduce/hadoop-mapreduce-examples-$(hadoop version | grep Hadoop | cut -d ' ' -f2).jar pi 16 100


Deploy DARS on Kubernetes\*
***************************

Many containerized workloads are deployed in clusters managed by orchestration software like Kubernetes.

Prerequisites
=============

* A running Kubernetes cluster at version >= 1.6 with access configured to it using kubectl.
* You must have appropriate permissions to list, create, edit and delete pods in your cluster.
* The service account credentials used by the driver pods must be allowed to create pods, services and configmaps.
* You must have Kubernetes DNS configured in your cluster.

.. note::

  To ensure that Kubernetes is correctly installed and configured for |CL|, follow the instructions in :ref:`kubernetes`.


#. For this example we will create the following Dockerfile

   .. code-block:: bash

        cat > $(pwd)/Dockerfile << 'EOF'
        ARG DERIVED_IMAGE
        FROM ${DERIVED_IMAGE}

        RUN mkdir -p /etc/passwd /etc/pam.d /opt/spark/conf /opt/spark/work-dir

        RUN set -ex && \
            rm /bin/sh && \
            ln -sv /bin/bash /bin/sh && \
            touch /etc/pam.d/su \
            echo "auth required pam_wheel.so use_uid" >> /etc/pam.d/su && \
            chgrp root /etc/passwd && chmod ug+rw /etc/passwd

        RUN ln -s /usr/share/apache-spark/jars/ /opt/spark/ && \
            ln -s /usr/share/apache-spark/bin/ /opt/spark/ && \
            ln -s /usr/share/apache-spark/sbin/ /opt/spark/ && \
            ln -s /usr/share/apache-spark/examples/ /opt/spark/ && \
            ln -s /usr/share/apache-spark/kubernetes/tests/ /opt/spark/ && \
            ln -s /usr/share/apache-spark/data/ /opt/spark/ && \
            ln -s /etc/spark/* /opt/spark/conf/

        COPY entrypoint.sh /opt/
        ENV JAVA_HOME=/usr/lib/jvm/java-1.11.0-openjdk
        ENV PATH="${JAVA_HOME}/bin:${PATH}"
        ENV SPARK_HOME /opt/spark
        WORKDIR /opt/spark/work-dir
        ENTRYPOINT [ "/opt/entrypoint.sh" ]
        EOF


#. The Dockerfile requires an entrypoint script, to allow spark-submit to interact with the container using the given arguments. Create the :file:`entrypoint.sh` file:

   .. code-block:: bash

        cat > $(pwd)/entrypoint.sh << 'EOF'
        #!/bin/bash
        #
        # Licensed to the Apache Software Foundation (ASF) under one or more
        # contributor license agreements.  See the NOTICE file distributed with
        # this work for additional information regarding copyright ownership.
        # The ASF licenses this file to You under the Apache License, Version 2.0
        # (the "License"); you may not use this file except in compliance with
        # the License.  You may obtain a copy of the License at
        #
        #    http://www.apache.org/licenses/LICENSE-2.0
        #
        # Unless required by applicable law or agreed to in writing, software
        # distributed under the License is distributed on an "AS IS" BASIS,
        # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
        # See the License for the specific language governing permissions and
        # limitations under the License.
        #

        # echo commands to the terminal output
        set -ex

        # Check whether there is a passwd entry for the container UID
        myuid=$(id -u)
        mygid=$(id -g)
        # turn off -e for getent because it will return error code in anonymous uid case
        set +e
        uidentry=$(getent passwd $myuid)
        set -e

        # If there is no passwd entry for the container UID, attempt to create one
        if [ -z "$uidentry" ] ; then
            if [ -w /etc/passwd ] ; then
                echo "$myuid:x:$myuid:$mygid:anonymous uid:$SPARK_HOME:/bin/false" >> /etc/passwd
            else
                echo "Container ENTRYPOINT failed to add passwd entry for anonymous UID"
            fi
        fi

        SPARK_K8S_CMD="$1"
        case "$SPARK_K8S_CMD" in
            driver | driver-py | driver-r | executor)
              shift 1
              ;;
            "")
              ;;
            *)
              echo "Non-spark-on-k8s command provided, proceeding in pass-through mode..."
              exec /sbin/tini -s -- "$@"
              ;;
        esac

        SPARK_CLASSPATH="$SPARK_CLASSPATH:${SPARK_HOME}/jars/*"
        env | grep SPARK_JAVA_OPT_ | sort -t_ -k4 -n | sed 's/[^=]*=\(.*\)/\1/g' > /tmp/java_opts.txt
        readarray -t SPARK_EXECUTOR_JAVA_OPTS < /tmp/java_opts.txt

        if [ -n "$SPARK_EXTRA_CLASSPATH" ]; then
          SPARK_CLASSPATH="$SPARK_CLASSPATH:$SPARK_EXTRA_CLASSPATH"
        fi

        if [ -n "$PYSPARK_FILES" ]; then
            PYTHONPATH="$PYTHONPATH:$PYSPARK_FILES"
        fi

        PYSPARK_ARGS=""
        if [ -n "$PYSPARK_APP_ARGS" ]; then
            PYSPARK_ARGS="$PYSPARK_APP_ARGS"
        fi

        R_ARGS=""
        if [ -n "$R_APP_ARGS" ]; then
            R_ARGS="$R_APP_ARGS"
        fi

        if [ "$PYSPARK_MAJOR_PYTHON_VERSION" == "2" ]; then
            pyv="$(python -V 2>&1)"
            export PYTHON_VERSION="${pyv:7}"
            export PYSPARK_PYTHON="python"
            export PYSPARK_DRIVER_PYTHON="python"
        elif [ "$PYSPARK_MAJOR_PYTHON_VERSION" == "3" ]; then
            pyv3="$(python3 -V 2>&1)"
            export PYTHON_VERSION="${pyv3:7}"
            export PYSPARK_PYTHON="python3"
            export PYSPARK_DRIVER_PYTHON="python3"
        fi

        case "$SPARK_K8S_CMD" in
          driver)
            CMD=(
              "$SPARK_HOME/bin/spark-submit"
              --conf "spark.driver.bindAddress=$SPARK_DRIVER_BIND_ADDRESS"
              --deploy-mode client
              "$@"
            )
            ;;
          driver-py)
            CMD=(
              "$SPARK_HOME/bin/spark-submit"
              --conf "spark.driver.bindAddress=$SPARK_DRIVER_BIND_ADDRESS"
              --deploy-mode client
              "$@" $PYSPARK_PRIMARY $PYSPARK_ARGS
            )
            ;;
            driver-r)
            CMD=(
              "$SPARK_HOME/bin/spark-submit"
              --conf "spark.driver.bindAddress=$SPARK_DRIVER_BIND_ADDRESS"
              --deploy-mode client
              "$@" $R_PRIMARY $R_ARGS
            )
            ;;
          executor)
            CMD=(
              ${JAVA_HOME}/bin/java
              "${SPARK_EXECUTOR_JAVA_OPTS[@]}"
              -Xms$SPARK_EXECUTOR_MEMORY
              -Xmx$SPARK_EXECUTOR_MEMORY
              -cp "$SPARK_CLASSPATH"
              org.apache.spark.executor.CoarseGrainedExecutorBackend
              --driver-url $SPARK_DRIVER_URL
              --executor-id $SPARK_EXECUTOR_ID
              --cores $SPARK_EXECUTOR_CORES
              --app-id $SPARK_APPLICATION_ID
              --hostname $SPARK_EXECUTOR_POD_IP
            )
            ;;

          *)
            echo "Unknown command: $SPARK_K8S_CMD" 1>&2
            exit 1
        esac

        # Execute the container CMD
        exec "${CMD[@]}"
        EOF


#. Make :file:`entrypoint.sh` executable

   .. code-block:: bash

      sudo chmod +x $(pwd)/entrypoint.sh

#. Build the Docker image, for this example we will use dars_k8s_spark for the name of the image.

   .. code-block:: bash

      docker build . --build-arg DERIVED_IMAGE=clearlinux/stacks-dars-mkl -t dars_k8s_spark


#. Verify your built image. Execute the following command looking for the given name dars_k8s_spark

   .. code-block:: bash

     docker images | grep "dars_k8s_spark"

   You should see something like:

   .. code-block:: console

     dars_k8s_spark                               latest              1fa3278a3421        1 minutes ago       6.56GB

#. Use a variable to store the image's given name:

   .. code-block:: bash

     DARS_K8S_IMAGE=dars_k8s_spark


Configure RBAC
==============

Create the Spark service account and cluster role binding to allow Spark on Kubernetes to create Executors as required. For this example use the default namespace.

.. code-block:: bash

   kubectl create serviceaccount spark-serviceaccount --namespace default
   kubectl create clusterrolebinding spark-rolebinding --clusterrole=edit --serviceaccount=default:spark-serviceaccount --namespace=default


Prepare to Submit the Spark Job
===============================

#. Determine the Kubernetes master address:

   .. code-block:: bash

      kubectl cluster-info

   You should see something like:

   .. code-block:: console

      Kubernetes master is running at https://192.168.39.127:8443

#. Use a variable to store the master address:

   .. code-block:: bash

      MASTER_ADDRESS='https://192.168.39.127:8443'

#. Submit the Spark Job on Minikube using the MASTER_ADDRESS and DARS_K8S variables. The driver pod will be called spark-pi-driver.

   .. code-block:: bash

      spark-submit \
      --master k8s://${MASTER_ADDRESS} \
      --deploy-mode cluster \
      --name spark-pi \
      --class org.apache.spark.examples.SparkPi \
      --conf spark.executor.instances=2 \
      --conf spark.kubernetes.container.image=${DARS_K8S_IMAGE} \
      --conf spark.kubernetes.driver.pod.name=spark-pi-driver \
      --conf spark.kubernetes.namespace=default \
      --conf spark.kubernetes.authenticate.driver.serviceAccountName=spark-serviceaccount \
      local:///usr/share/apache-spark/examples/jars/spark-examples_2.12-2.4.0.jar


#. Check the Job. Read the logs and look for the Pi result:

   .. code-block:: bash

      kubectl logs spark-pi-driver | grep "Pi is roughly"

   You should see something like:

   .. code-block:: console

      Pi is roughly 3.1418957094785473

More information about spark-submit configuration is available in the  `running-on-kubernetes`_ documentation.


Troubleshooting
***************

Dropped or refused connection
=============================

If Pyspark / Spark-shell warns of a dropped connection exception or Connection refused, check if the `HADOOP_CONF_DIR` environment variable is set. These APIs assume they will use Hadoop Distributed File System.
You can unset `HADOOP_CONF_DIR` and use Spark RDDs, or start Hadoop services and then create your directories and files as required using hdfs.

It is also possible to change the file system to local without unsetting `HADOOP_CONF_DIR` as is further described here:

.. code-block:: bash

   pyspark --conf "spark.hadoop.fs.defaultFS=file:///"

.. code-block:: bash

   spark-shell --conf "spark.hadoop.fs.defaultFS=file:///"

Using Spark with proxy settings
===============================

There are two ways to work with proxies:

#. Add the following line to  :file:`$SPARK_CONF_DIR/spark-defaults.conf` for both `spark.executor.extraJavaOptions` and `spark.driver.extraJavaOptions` variables:

.. code-block:: console

   -Dhttp.proxyHost=<URL> -Dhttp.proxyPort=<PORT> -Dhttps.proxyHost=<URL> -Dhttps.proxyPort=<PORT>



#. Give the proxies URL and Port as a configuration parameter

.. code-block:: bash

   pyspark --conf "spark.hadoop.fs.defaultFS=file:///" --conf "spark.driver.extraJavaOptions=-Dhttp.proxyHost=example.proxy -Dhttp.proxyPort=111 -Dhttps.proxyHost=example.proxy -Dhttps.proxyPort=112"

.. code-block:: bash

   spark-shell --conf "spark.hadoop.fs.defaultFS=file:///" --conf "spark.driver.extraJavaOptions=-Dhttp.proxyHost=example.proxy -Dhttp.proxyPort=111 -Dhttps.proxyHost=example.proxy -Dhttps.proxyPort=112"


Known issues
============

#. There is an exception message `Unrecognized Hadoop major version number: 3.2.0 at org.apache.hadoop.hive.shims.ShimLoader.getMajorVersion.`

This exception can be disregarded because DARS does not use hadoop.hive.shims. Hive binaries installed from Apache on |CL| with JDK11 does not work, this is an issue reported on Hive's Jira.

#. There is an exception message `Exception in thread "Thread-3" java.lang.ExceptionInInitializerError at org.apache.hadoop.hive.conf.HiveConf` This is related to the same issue with |CL| and JDK11 noted above, and does not affect DARS for the same reason.


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

.. _running-on-kubernetes: https://spark.apache.org/docs/latest/running-on-kubernetes.html#configuration
