.. _dlaas-benchmarks:

Deep Learning as a Service Benchmarking
#######################################

This tutorial details the steps needed to run benchmarking workloads in |CL-ATTR| using TensorFlow and on Kubeflow with the |CL| Deep Learning as a Service Stack.

Prerequisites
=============

For this tutorial, we'll be using a system that has |CL| installed using the :ref:`bare-metal-install` getting started guide.  It is possible to follow these instructions on other OS systems but we're limiting the scope of this document to |CL|.

Ensure you have the "containers-basic" bundle installed, this will provide Docker, which is required for TensorFlow benchmarking. Use the :command:`swupd` utility with the `bundle-list` option and check for "containers-basic" in the list:

.. code-block:: bash

  sudo swupd bundle-list

If you need to install the containers-basic bundle, use :command:`swupd` to do so.

.. code-block:: bash

  sudo swupd bundle-add containers-basic


To run Kubernetes on |CL|, please refer to the :ref:`kubernetes` tutorial to ensure it is correctly installed and configured.

We have validated these steps against the following software package versions

  * |CL| 26240
  * Docker 18.06.1
  * Kubernetes 1.11.3
  * Go 1.11.12


TensorFlow Benchmarks
=====================

This section describes running the `TensorFlow benchmarks`_ as run by the TensorFlow community. These steps provide a template to run other benchmarks, providing they can invoke TensorFlow.

Download and run the docker image from hub.docker.com. The next commands will take place in the running container. Replace <docker_name> with the name of the image.

First, clone the benchmark repository

.. code-block:: bash

  docker exec -t <docker_name> bash -c ‘git clone http://github.com/tensorflow/benchmarks -b cnn_tf_v1.11_compatible’

Next, execute the benchmark script to run the benchmark

.. code-block:: bash

  docker exec -i <docker_name> bash -c ‘python benchmarks/scripts/tf_cnn_benchmarks/tf_cnn_benchmarks.py --device=cpu --model=resnet50 --data_format=NWHC ’.

You can replace the model with one of your choice supported by the TensorFlow benchmarks.



Kubeflow Benchmarks
===================

The benchmark workload will run in a Kubernetes (k8s) container. We will use Kubeflow and deploy three nodes for this tutorial, to get a decent return.

k8s setup
+++++++++

Please follow the instructions in the :ref:`kubernetes` tutorial to get set up on |CL|.  The k8s community also has `instructions`_ if you are using Ubuntu instead of |CL|.


k8s networking
++++++++++++++

We have used `flannel`_ as the network provider for these tests. If you are comfortable with another network layer, there is nothing that will prevent you from using that.
Refer to the Kubernetes `networking documentation`_ for setup.


Images
++++++

We will need to create a docker image that will include launcher.py to include the |CL| Deep Learning Stack, and put the benchmarks repo in the right location. From the docker image, run the following

.. code-block:: bash

  mkdir -p /opt
  git clone https://github.com/tensorflow/benchmarks.git /opt/tf-benchmarks
  cp launcher.py /opt
  chmod u+x /opt/*

Your entry point then becomes "/opt/launcher.py".


This will build an image which can be consumed directly by TFJob from kubeflow.  We are working to create these images as part of our release cycle.


Ksonnet
+++++++

Kubeflow uses Ksonnet to manage deployments, so we need to install that before setting up Kubeflow. On |CL|, follow these steps:

.. code-block:: bash

  swupd bundle-add go-basic-dev
  export GOPATH=$HOME/go
  export PATH=$PATH:$GOPATH/bin
  go get github.com/ksonnet/ksonnet
  cd $GOPATH/src/github.com/ksonnet/ksonnet
  make install


.. For other OS, follow steps in: https://www.kubeflow.org/docs/guides/components/ksonnet/ .

After the ksonnet installation is complete, ensure that binary `ks` is accessible across the environment.


Kubeflow
========
Once you have k8s running on your nodes, you can setup Kubeflow by following these instructions from their `quick start guide`_.

.. code-block:: bash

  export KUBEFLOW_SRC=$HOME/kflow
  export KUBEFLOW_TAG=”v0.3.2”
  export KFAPP=”kflow_app”
  export K8S_NAMESPACE=”kubeflow”
  mkdir ${KUBEFLOW_SRC}
  cd ${KUBEFLOW_SRC}
  curl https://raw.githubusercontent.com/kubeflow/kubeflow/${KUBEFLOW_TAG}/scripts/download.sh | bash
  ${KUBEFLOW_SRC}/scripts/kfctl.sh init ${KFAPP} --platform none
  cd ${KFAPP}
  ${KUBEFLOW_SRC}/scripts/kfctl.sh generate k8s

Now you have all the required kubeflow packages, and you can deploy the primary one for our purposes: tf-job-operator.

.. code-block:: bash

  kubectl create namespace ${K8S_NAMESPACE}
  ks env add default --namespace "${K8S_NAMESPACE}"
  ks apply default -c tf-job-operator

This creates the CustomResourceDefinition(CRD) endpoint to launch a TFJob.

Running the Deep Learning as a Service TFJob
++++++++++++++++++++++++++++++++++++++++++++

The jsonnet template files for ResNet50 and Alexnet are available in the |CL| Deep Learning Stack repository. Download and copy these files into

.. code-block:: console

  ${KUBEFLOW_SRC}/${KFAPP}/vendor/kubeflow/examples/prototypes/

Next, generate Kubernetes manifests for the workloads and apply them to create and run them using these commands

.. code-block:: bash

  ks generate dlaas-resnet50 dlaasresnet50 --name=dlaasresnet50
  ks generate dlaas-alexnet dlaasalexnet --name=dlaasalexnet
  ks apply default -c dlaasresnet50
  ks apply default -c dlaasalexnet

This will replicate and deploy three test setups in your k8s cluster.


Results
=======
You will need to parse the logs of the k8s pod to get the performance numbers. The pods will still be around post completion and will be in ‘Completed’ state. You can get the logs from any of the pods to inpsect the benchmark results.

.. To-Dos
.. This is a list of to-do’s to the engineering team to get this moving in the right direction.
.. Make kubeflow docker images along with release images.
.. Second downstream docker file for MKL.
.. Another set of jsonnet files for MKL.
.. Trim down the base DLaaS image to contain tensorflow bundle and nothing else.
.. CI will throw benchmarks into the repo and be able to test it.
.. The downstream dockerfile will generate another image with benchmarks repo and launcher.py file in the right locations.
.. Dynamic generation of ksonnet template files for a matrix of batch_size, model and replicas.



.. _TensorFlow benchmarks: https://www.tensorflow.org/guide/performance/benchmarks
.. _instructions: https://kubernetes.io/docs/setup/independent/create-cluster-kubeadm/
.. _flannel: https://github.com/coreos/flannel
.. _networking documentation: https://kubernetes.io/docs/setup/independent/create-cluster-kubeadm/#pod-network
.. _quick start guide: https://www.kubeflow.org/docs/started/getting-started/
