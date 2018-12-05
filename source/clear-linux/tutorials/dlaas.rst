.. _dlaas:

Deep Learning as a Service
##########################

This tutorial explains how to run benchmarking workloads in |CL-ATTR| using
TensorFlow* and Kubeflow with the Clear Linux* Deep Learning Stack.

Release notes
=============

View current `release notes for the Clear Linux Deep Learning Stack`_.

Prerequisites
=============

* |CL| is installed on host system. If not, :ref:`bare-metal-install`
* `containers-basic` bundle is installed
* `cloud-native-basic` bundle is installed (includes kubernetes)

In |CL|, `containers-basic` provides Docker*, which is required for
TensorFlow benchmarking. Use the :command:`swupd` utility to check if
`containers-basic` and `cloud-native-basic` are present:

.. code-block:: bash

   sudo swupd bundle-list

If you need to install the `containers-basic` or `cloud-native-basic`, enter:

.. code-block:: bash

   sudo swupd bundle-add containers-basic

To ensure that kubernetes is correctly installed and configured,
:ref:`kubernetes`.

We have validated these steps against the following software package versions

* |CL| 26240--lowest version permissible.
* Docker 18.06.1
* Kubernetes 1.11.3
* Go 1.11.12

The |CL| Deep Learning Stack is available in two versions.  First, a version that includes TensorFlow* optimized for Intel Architecture, the `Eigen`_ version, and a version that includes the TensorFlow* framework optimized using Intel® Math Kernel Library for Deep Neural Networks (Intel® MKL-DNN) primitives, the `Intel MKL`_ version.

TensorFlow* Single and Multi Node Benchmarks
============================================

This section describes running the `TensorFlow benchmarks`_ in single node. For multi node testing replicate these steps for each node. These steps provide a template to run other benchmarks, providing they can invoke TensorFlow.

Download and run either the `Eigen`_ or the `Intel MKL-DNN`_  docker image from hub.docker.com. The next commands will take place in the running container. Replace <docker_name> with the name of the image.


.. note::

   Replace <docker_name> with the name of the image.

#. First, clone the benchmark repository:

   .. code-block:: bash

      docker exec -t <docker_name> bash -c ‘git clone http://github.com/tensorflow/benchmarks -b cnn_tf_v1.11_compatible’

#. Next, execute the benchmark script to run the benchmark

   .. code-block:: bash

      docker exec -i <docker_name> bash -c ‘python benchmarks/scripts/tf_cnn_benchmarks/tf_cnn_benchmarks.py --device=cpu --model=resnet50 --data_format=NWHC ’.

      .. note::

         You can replace the model with one of your choice supported by the
         TensorFlow benchmarks.

Kubeflow Multinode benchmarks
=============================

The benchmark workload will run in a Kubernetes container. We will use Kubeflow and deploy three nodes for this tutorial to show resource management and get sufficient output data for evaluation.

Kubernetes setup
****************

Follow the instructions in the :ref:`kubernetes` tutorial to get set up on
|CL|. The kubernetes community also has `instructions for creating a cluster`_.

Kubernetes networking
*********************

We have used `flannel`_ as the network provider for these tests. If you are
comfortable with another network layer, refer to the Kubernetes
`networking documentation`_ for setup.


Images
******

We need to add `launcher.py` to our docker image to
include the |CL| Deep Learning Stack, and put the benchmarks repo in the
right location. From the docker image, run the following:

.. code-block:: bash

   mkdir -p /opt
   git clone https://github.com/tensorflow/benchmarks.git /opt/tf-benchmarks
   cp launcher.py /opt
   chmod u+x /opt/*

Your entry point now becomes "/opt/launcher.py".

This will build an image which can be consumed directly by TFJob from
kubeflow.  We are working to create these images as part of our release
cycle.


ksonnet*
********

Kubeflow uses ksonnet* to manage deployments, so we need to install that before setting up Kubeflow. On |CL|, follow these steps:

.. code-block:: bash

   swupd bundle-add go-basic-dev
   export GOPATH=$HOME/go
   export PATH=$PATH:$GOPATH/bin
   go get github.com/ksonnet/ksonnet
   cd $GOPATH/src/github.com/ksonnet/ksonnet
   make install

After the ksonnet installation is complete, ensure that binary `ks` is
accessible across the environment.

Kubeflow
********

Once you have Kubernetes running on your nodes, you can setup Kubeflow by following these instructions from their `quick start guide`_.

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
============================================

The `jsonnet template files`_ for ResNet50 and Alexnet are available in the |CL|
Deep Learning Stack repository. Download and copy these files into:

.. code-block:: console

   ${KUBEFLOW_SRC}/${KFAPP}/vendor/kubeflow/examples/prototypes/

Next, generate Kubernetes manifests for the workloads and apply them to create and run them using these commands

.. code-block:: bash

   ks generate dlaas-resnet50 dlaasresnet50 --name=dlaasresnet50
   ks generate dlaas-alexnet dlaasalexnet --name=dlaasalexnet
   ks apply default -c dlaasresnet50
   ks apply default -c dlaasalexnet

This will replicate and deploy three test setups in your Kubernetes cluster.


Results
=======
You need to parse the logs of the Kubernetes pod to get the performance
numbers. The pods will still be around post completion and will be in
‘Completed’ state. You can get the logs from any of the pods to inspect the
benchmark results. More information about `Kubernetes logging`_ is available from the Kubernetes community.

.. To-Dos

.. Make kubeflow docker images along with release images.
.. Another set of jsonnet files for MKL.
.. Trim down the base DLaaS image to contain tensorflow bundle and nothing else.
.. CI will throw benchmarks into the repo and be able to test it.
.. The downstream dockerfile will generate another image with benchmarks repo and launcher.py file in the right locations.
.. Dynamic generation of ksonnet template files for a matrix of batch_size, model and replicas.



.. _TensorFlow benchmarks: https://www.tensorflow.org/guide/performance/benchmarks
.. _instructions for creating a cluster: https://kubernetes.io/docs/setup/independent/create-cluster-kubeadm/
.. _flannel: https://github.com/coreos/flannel
.. _networking documentation: https://kubernetes.io/docs/setup/independent/create-cluster-kubeadm/#pod-network
.. _quick start guide: https://www.kubeflow.org/docs/started/getting-started/

.. _Eigen: https://hub.docker.com/r/clearlinux/stacks-dlaas-oss/
.. _Intel MKL-DNN: https://hub.docker.com/r/clearlinux/stacks-dlaas-mkl/

.. _release notes for the Clear Linux Deep Learning Stack: https://github.com/clearlinux/dockerfiles/tree/master/stacks/dlaas

.. _Clear Linux Docker Hub page: https://hub.docker.com/u/clearlinux/

.. _jsonnet template files: https://github.com/clearlinux/dockerfiles/tree/master/stacks/dlaas/kubeflow/dlaas-tfjob/dlaas-bench/prototypes

.. _Kubernetes logging: https://kubernetes.io/docs/concepts/cluster-administration/logging/
