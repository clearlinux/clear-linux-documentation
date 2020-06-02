.. _dlrs-inference:

AI Inference with the Deep Learning Reference Stack
###################################################

In this guide walk through a solution for using the Deep Learning Reference Stack with a Seldon Core\* platform deployed on Kubernetes\*. Seldon Core simplifies deployment of the models we create and use with the Deep Learning Reference Stack. Use this guide to set up your infrastructure and deploy a benchmarking workload on your Kubernetes cluster.

.. contents::
   :local:
   :depth: 1

Overview
********

.. figure:: /_figures/stacks/kubeflow-seldon-dlrs-example-diagram.png
   :alt: Example diagram with DLRS deployed by Seldon
   :width:     800


The solution covered here requires the following software components:

* `Deep Learning Reference Stack`_ which is a |CL-ATTR| based Docker\* container providing deep learning frameworks and is optimized for Intel® Xeon® platforms.
* `Kubeflow`_ is the machine learning toolkit for Kubernetes that helps with deployment of Seldon Core and Istio components.
* `Seldon Core`_ is a software platform for deploying machine learning models. We use the DLRS container to serve the OpenVino\* framework for inference with the Seldon Core.
* The OpenVino Model Server is included in DLRS and provides the OpenVino framework for inference. From OpenVino, the `OpenVino Toolkit`_ provides improved neural network performance on a variety of Intel processors. For this guide, we converted pre-trained Caffe models into the `Intermediate Representation(IR)`_ of ResNet50 with the OpenVino toolkit.
* `Istio`_ is a traffic manager and performs the load balancing for service requests in the cluster.
* Pre-processing container converts jpeg content into NumPy array
* Post-processing container converts an array of classification probabilities to a human-readable class name.
* Pre and post-processing containers are created using the `Source-to-Image`_ (S2I)toolkit, which builds reproducible container images from source code/
* `Min.io`_ is used as the distributed object storage for models



Prerequisites
*************

Although this guide assumes a |CL| host system, it has also been validated with the following software components.

.. list-table:: **Table 1. Software Component Versions**
   :widths: 16,16
   :header-rows: 1

   * - Component
     - Version

   * - DLRS
     - 0.4.0

   * - Docker
     - 18.09

   * - Kubernetes
     - 1.15.3

   * - Source-to-Image
     - 1.1.14

   * - Helm
     - 2.14.3

   * - Kubeflow
     - 0.6.1

   * - Seldon
     - 0.3.2

   * - Rook
     - 1.0.5

   * - Ceph
     - 14.2.1-20190430

   * - Minio
     - RELEASE.2019-04-23T23-50-36Z

   * - CentOS
     - 7.6

   * - OpenVINO Toolkit
     - 2019 R1.0.1

   * - MKL-DNN
     - 0.19

Recommended Hardware
====================

We validated this guide on a server with a 2nd Generation Intel Xeon Scalable processor, formerly Cascade Lake, and this is recommended to get optimal performance and take advantage of the built in Intel® Deep Learning Boost (Intel® DL Boost) functionality.

Required Software
=================

#.  :ref:`Install <bare-metal-install-desktop>` |CL| on your host system


#. Install the :command:`containers-basic` and :command:`cloud-native-basic` bundles:

   .. code-block:: bash

      sudo swupd bundle-add containers-basic cloud-native-basic


#. Start Docker

   Docker is not started upon installation of the :command:`containers-basic` bundle. To start Docker, enter:

   .. code-block:: bash

      sudo systemctl start docker


#. Install and configure :ref:`kubernetes`.







.. note::

   The Deep Learning Reference Stack was developed to provide the best user experience when executed on a |CL| host.  However, as the stack runs in a container environment, you should be able to complete the following sections of this guide on other Linux* distributions, provided they comply with the Docker\* and Kubernetes\*  package versions listed above. Look for your distribution documentation on how to update packages and manage Docker services.

   For other systems, please install the following software

   * `Docker 18.09`_
   * `Kubernetes 1.15.3`_


Infrastructure Set-Up
*********************

Environment
===========

Throughout this guide we will refer to the DEPLOY_DIR environment variable.  DEPLOY_DIR is a pointer to the current directory with all resources used as the installation directory. Set it as follows

.. code-block:: bash

   DEPLOY_DIR=`pwd`

Deployment Tools
================

Source-to-Image (S2i)
---------------------

S2i is a tool for building artifacts from source and injecting them into Docker images.  We use S2i to build the Imagenet transformer. Install it:

.. code-block:: bash

   wget https://github.com/openshift/source-to-image/releases/download/v1.1.14/source-to-image-v1.1.14-874754de-linux-amd64.tar.gz
   tar -zxvf source-to-image-v1.1.14-874754de-linux-amd64.tar.gz
   mv -f -t /usr/local/bin/ sti s2i
   rm -f source-to-image-v1.1.14-874754de-linux-amd64.tar.gz
   chmod +x /usr/local/bin/sti
   chmod +x /usr/local/bin/s2i

kfctl
-----

`kfctl` is a client used to control and deploy the Kubeflow platform.  Install with:

.. code-block:: bash

   wget https://github.com/kubeflow/kubeflow/releases/download/v0.6.1/kfctl_v0.6.1_linux.tar.gz
   tar -zxvf kfctl_v0.6.1_linux.tar.gz
   rm -f kfctl_v0.6.1_linux.tar.gz
   mv -f kfctl /usr/local/bin/
   chmod +x /usr/local/bin/kfctl

Minio
-----

The Minio client is compatible with object cloud storage services.  We use it to manage buckets and files stored in Minio storage. Install with:

.. code-block:: bash

   wget https://dl.min.io/client/mc/release/linux-amd64/mc
   mv mc /usr/local/bin/
   chmod +x /usr/local/bin/mc


Helm
----

Helm is used to deploy components on Kubernetes clusters. Helm is included in the :file:`cloud-native-basic` bundle in |CL| and can be installed with

.. code-block:: bash

   sudo swupd bundle-add cloud-native-basic

If you are not using a |CL| host, install with:

.. code-block:: bash

   wget https://get.helm.sh/helm-v2.14.3-linux-amd64.tar.gz
   tar -zxvf helm-v2.14.3-linux-amd64.tar.gz
   rm -f helm-v2.14.3-linux-amd64.tar.gz
   mv linux-amd64/helm /usr/local/bin/helm

Regardless of your host OS, initialize Helm as follows:

.. code-block:: bash

   helm init
   kubectl create serviceaccount --namespace kube-system tiller
   kubectl create clusterrolebinding tiller-cluster-rule --clusterrole=cluster-admin --serviceaccount=kube-system:tiller
   kubectl patch deploy --namespace kube-system tiller-deploy -p '{"spec":{"template":{"spec":{"serviceAccount":"tiller"}}}}'


gsutil
------

:file:`gsutil` is a client utility to work with Google Cloud\* storage.  Follow the instructions to install `gsutil`_ . With the initialized Google Cloud storage command line interface, we will be able to download ResNet50 models, which we will use for model serving.


Rook
----

Rook.io is used to deploy Minio and Ceph.  Clone the GitHub\* repository:

.. code-block:: bash

   git clone -b release-1.0 https://github.com/rook/rook.git


.. todo:  ADD CORRECT GITHUB LINK FOR ai-inferencing REPO

AI Inferencing
--------------

This guide is based on the code in the IntelSolutionDev Ai Inferencing repository.  Clone the repository

.. code-block:: bash

   git clone https://<need github URL>




Platform Backends
=================

Ceph
----

#. Deploy Ceph Rook Operator


   The Rook Operator is used to deploy the remaining Rook Ceph components.  Deploy it:

   .. code-block:: bash

      cd $DEPLOY_DIR
      cd rook/cluster/examples/kubernetes/ceph
      kubectl create -f common.yaml
      kubectl create -f operator.yaml
      kubectl -n rook-ceph get pods # wait for rook-ceph-operator pod

#. Deploy Rook Ceph Cluster


   The Rook Ceph cluster is used for block storage for all platform components. You will need to modify the :file:`cluster.yaml` for your requirements. For this guide, we will prepare a cluster with 3 mons, and we will store data in :file:`/var/lib/rook` on all nodes.  Modify the file:

   .. code-block:: yaml

      apiVersion: ceph.rook.io/v1
      kind: CephCluster
      metadata:
      name: rook-ceph
      namespace: rook-ceph
      spec:
      cephVersion:
       image: ceph/ceph:v14.2.1-20190430
       allowUnsupported: false
      dataDirHostPath: /var/lib/rook
      mon:
       count: 3
       allowMultiplePerNode: false
      dashboard:
       enabled: true
      network:
       hostNetwork: false
      rbdMirroring:
       workers: 0
      annotations:
      resources:
      storage:
       useAllNodes: true
       useAllDevices: false
       deviceFilter:
       location:
       config:
       directories:
       - path: /var/lib/rook

   After modifying the :file:`cluster.yaml`, run:

   .. code-block:: bash

      kubectl create -f cluster.yaml
      kubectl -n rook-ceph get pods #wait for osd pods
      kubectl create -f toolbox.yaml
      kubectl -n rook-ceph get pod -l "app=rook-ceph-tools"
      kubectl create -f storageclass.yaml
      kubectl patch storageclass rook-ceph-block -p '{"metadata": {"annotations":{"storageclass.kubernetes.io/is-default-class":"true"}}}'

   To verify the setup is correct, run:

   .. code-block:: bash

      kubectl -n rook-ceph exec -it $(kubectl -n rook-ceph get pod -l "app=rook-ceph-tools" -o jsonpath='{.items[0].metadata.name}') ceph status

   The command should return:

   .. code-block:: console

      HEALTH_OK

#. Troubleshooting

   If you see a warning related to undersized PGs you need to increase the number of PGs using these commands:

   First get number of PGs:

   .. code-block:: bash

      ceph osd pool get replicapool pg_num

   Then double the number of pgs (for example from 300 to 600):

   .. code-block:: bash

      ceph osd pool set replicapool pg_num 600
      ceph osd pool set replicapool pgp_num 600

Minio
-----

The Minio cluster is used as object storage for all components in the platform. Deploy it:

.. code-block:: bash

   cd $DEPLOY_DIR
   cd rook/cluster/examples/kubernetes/minio
   kubectl create -f operator.yaml
   kubectl -n rook-minio-system get pods # wait for rook-minio-operator pod
   kubectl create -f object-store.yaml

.. note::

   Minio pods will not start if you are using a proxy in your environment. Please check the proxy settings in the :file:`/etc/kubernetes/manifests/kube-apiserver.yaml`. The `.local,.svc,.nip.io` line should be set to `no_proxy`.

Docker registry
---------------

This Docker registry will be used for all platform components.  We will use helm to set up the registry as shown:

.. code-block:: bash

   cd $DEPLOY_DIR
   cd ai-inferencing/infra
   helm install --namespace registry --name registry stable/docker-registry -f registry-values.yaml

Verify the registry setup

.. code-block:: bash

   REGISTRY_URL=`kubectl get svc -n registry | grep NodePort | awk '{ print $3; }'`.nip.io:5000


Create the Machine Learning Platform
====================================

The machine learning platform for this guide is built using the Kubeflow Toolkit from which we use the Seldon-core and Istio components.

#. Prepare the definition files

   First we will get the configuration file for Istio

   .. code-block:: bash

      cd $DEPLOY_DIR
      wget https://raw.githubusercontent.com/kubeflow/kubeflow/v0.6.1/bootstrap/config/kfctl_k8s_istio.yaml
      sed -i 's/master.tar.gz/v0.6.1.tar.gz/g' kfctl_k8s_istio.yaml
      kfctl init kubeflow --config=$(pwd)/kfctl_k8s_istio.yaml -V
      cd kubeflow
      kfctl generate all -V

#. Edit :file:`kustomize/seldon-core-operator/base/statefulset.yaml` to change the version to `0.3.2-SNAPSHOT`.

#. Edit :file:`kustomize/istio-install/base/istio-noauth.yaml` to change limits for the istio-pilot deployment as shown:

   .. code-block:: yaml

      resources:
        limits:
          cpu: 1000m
          memory: 1000Mi

   This will correct a performance issue which results in istio-pilot causing crashes with multiple Seldon deployments start simultaneously.

   .. note::

      If istio cannot start because of an OOM (Out of Memory) error, change the limits of all istio-system deployments.  The Default settings should be enough for a small cluster (32GB RAM and less).



#. Install the Kubeflow components and wait for all pods in the Kubeflow and istio-system namespace to start.

   .. code-block:: bash

      kfctl apply all -V

#. Run

   .. code-block:: bash

      kubectl label namespace kubeflow istio-injection=enabled

      kubectl apply -f - <<EOF
      apiVersion: "rbac.istio.io/v1alpha1"
      kind: ClusterRbacConfig
      metadata:
        name: default
      spec:
        mode: 'OFF'
      EOF

      kubectl delete meshpolicy default

Getting Models
==============

#. Download models from the Public Google Storage Bucket:

   .. code-block:: bash

      cd $DEPLOY_DIR
      mkdir -p models/resnet50/1
      gsutil cp gs://intelai_public_models/resnet_50_i8/1/resnet_50_i8.bin models/resnet50/1/
      gsutil cp gs://intelai_public_models/resnet_50_i8/1/resnet_50_i8.xml models/resnet50/1/
      mv models/resnet50/1/resnet_50_i8.bin models/resnet50/1/model.bin
      mv models/resnet50/1/resnet_50_i8.xml models/resnet50/1/model.xml

#. Upload models to Minio

   .. code-block:: bash

      MINIO_URL=http://`kubectl get svc --all-namespaces | grep minio | grep NodePort | awk '{ print $4; }'`:9000
      mc config host add minio $MINIO_URL TEMP_DEMO_ACCESS_KEY TEMP_DEMO_SECRET_KEY --api S3v4
      mc mb minio/models
      mc cp --recursive models/* minio/models

Transformer Image
=================

#. Build the transformer image:

   .. code-block:: bash

      cd $DEPLOY_DIR
      REGISTRY_URL=`kubectl get svc -n registry | grep NodePort | awk '{ print $3; }'`.nip.io:5000
      s2i build -E ai-inferencing/infra/s2i-transformer/environment_grpc ai-inferencing/infra/s2i-transformer docker.io/seldonio/seldon-core-s2i-openvino:0.1 $REGISTRY_URL/imagenet_transformer:0.1 --network=host

#. Reset docker on all workers:

   The local Docker registry should be set as an insecure registry.  On all workers, edit the :file:`/etc/docker/daemon.json` file to set these lines:

   .. code-block:: console

      systemctl daemon-reload
      systemctl restart-docker

#. Push the image to the registry:

   .. code-block:: bash

      docker push $REGISTRY_URL/imagenet_transformer:0.1

.. note::

   If you are working behind a proxy in your network, use the `no-proxy` settings shown above.


OpenVINO Model Server Images
============================

There are a few OVMS images that could be used, but each of them have a different path to be used in a Seldon deployment, as seen in this table.

.. list-table:: **Table 2. Seldon server script path**
   :widths: 16,16
   :header-rows: 1

   * - Docker Image name
     - Command

   * - intelaipg/openvino-model-server:latest
     - \- /ie-serving-py/start_server.sh

   * - clearlinux/stacks-dlrs-mkl:v0.4.0
     - \- /workspace/scripts/serve.sh


DLRS Images
-----------

There is a |CL| based image with the OpenVINO Model Server in DLRS v0.4.0, but there is a known issue which prevents running successfully. The workaround until this issue is resolved is to prepare a modified version of the DLRS container.

#. Create a new Dockerfile

   .. code-block:: bash

      cat  <<EOF > Dockerfile
      FROM clearlinux/stacks-dlrs-mkl:v0.4.0
      COPY serve.sh /workspace/scripts/serve.sh
      EOF

#. Create the :file:`serve.sh` file

   .. code-block:: bash

      cat  <<EOF > serve.sh
      #!/bin/bash
      # temporary workaround
      PY_PATH="/usr/local/lib/openvino/inference_engine/:/usr/local/lib"
      echo "export PYTHONPATH=\${PY_PATH}" >>/.bashrc
      source ~/.bashrc

      # start the model server
      cd /ie_serving_py
      exec "\$@"
      EOF

#. Make :file:`serve.sh` executable

   .. code-block:: bash

      chmod +x serve.sh

#. Build the new docker image

   .. code-block:: bash

      REGISTRY_URL=`kubectl get svc -n registry | grep NodePort | awk '{ print $3; }'`.nip.io:5000
      sudo docker build -t ${REGISTRY_URL}/dlrs-mkl-fixed:v0.4.0 .

#. Upload the image to the registry

   .. code-block:: bash

      sudo docker push ${REGISTRY_URL}/dlrs-mkl-fixed:v0.4.0


Deploy Using Helm with Seldon
=============================

At this point you are ready to go.  Use the Helm chart with Seldon for deployment:

.. code-block:: bash

   helm install \
   --namespace kubeflow \
   --name seldonovms-server-res \
   --set transformer.image=$REGISTRY_URL/imagenet_transformer:0.1 \
   --set openvino.image=$REGISTRY_URL/dlrs-mkl-fixed:v0.4.0 \
   ai-inferencing/seldon

Verify that all pods are in the `Running` state:

.. code-block:: bash

   kubectl -n kubeflow get pods -l version=openvino

You have now created the inference infrastructure!



Secure Communication
====================

You can optionally set up secure communication between the clients and the server.  This is not required for completing this guide, but we will walk through it for completeness.

For this example we will use `10.0.0.1.nip.io` for our domain name.

#. Clone the repository

   .. code-block:: bash

      git clone https://github.com/nicholasjackson/mtls-go-example

#. Generate the certificates.

   This script will generate four directories: 1_root, 2_intermediate, 3_application, and 4_client containing the client and server certificates that will be used in the following procedures. When prompted, select `y` for all questions.

   .. code-block:: bash

      cd mtls-go-example
      ./generate.sh 10.0.0.1.nip.io password
      mkdir 10.0.0.1.nip.io && mv 1_root 2_intermediate 3_application 4_client 10.0.0.1.nip.io

#. Create a Kubernetes secret to hold the server's certificate and private key.

   We'll use :command:`kubectl` to create the  secret istio-ingressgateway-certs in namespace istio-system. The Istio gateway will load the secret automatically.

   .. code-block:: bash

      kubectl create -n istio-system secret tls istio-ingressgateway-certs --key 10.0.0.1.nip.io/3_application/private/10.0.0.1.nip.io.key.pem --cert 10.0.0.1.nip.io/3_application/certs/10.0.0.1.nip.io.cert.pem

#. Verify that :file:`tls.crt` and :file:`tls.key` have been mounted in the ingress gateway pod

   .. code-block:: bash

      kubectl exec -it -n istio-system $(kubectl -n istio-system get pods -l istio=ingressgateway -o jsonpath='{.items[0].metadata.name}') -- ls -al /etc/istio/ingressgateway-certs

#. Edit the default kubeflow gateway

   .. code-block:: bash

      kubectl apply -f - <<EOF
      apiVersion: networking.istio.io/v1alpha3
      kind: Gateway
      metadata:
        name: kubeflow-gateway
        namespace: kubeflow
      spec:
        selector:
          istio: ingressgateway
        servers:
        - hosts:
          - '*'
          port:
            name: http
            number: 80
            protocol: HTTP
        - hosts:
          - '*'
          port:
            name: https
            number: 443
            protocol: HTTPS
          tls:
            mode: SIMPLE
            privateKey: /etc/istio/ingressgateway-certs/tls.key
            serverCertificate: /etc/istio/ingressgateway-certs/tls.crt
      EOF


Seldon autoscaling
==================

The :file:`ai-inferencing/seldon/templates/deployment.yaml` file includes options for horizontal pod auto-scaling (HPA) in the Seldon deployment.

Auto-scaling automatically increases the number of replicas when resource usage exceeds the given threshold, whic is currently set to 30% CPU utilization. As well, when utilization is low, it decreases the number of instances for efficiency.

Set resource requests in all containers to to enable HPA.  The metrics-server will measure if the targetAverageUtilization has been exceeded.

Metrics server
--------------

By default, HPA needs access to the metrics.k8s.io API which is provided by the metrics-server. It can be launched as a cluster addon:

.. code-block:: bash

   cd $DEPLOY_DIR
   cd ai-inferencing/infra
   helm install --namespace kube-system --name metricsserver -f metrics-server-values.yaml stable/metrics-server

Enable HPA
----------

Upgrade Helm  to enable HPA

.. code-block:: bash

   helm upgrade \
   --install \
   seldonovms-server-res \
   --namespace kubeflow \
   --set transformer.image=$REGISTRY_URL/imagenet_transformer:0.1 \
   --set openvino.image=$REGISTRY_URL/dlrs-mkl-fixed:v0.4.0 \
   --set seldon.resource_limiting=1 \
   --set seldon.average_utilization=50 \
   --set seldon.hpa_enabled=1 \
   ai-inferencing/seldon


In this example:

seldon.resource_limiting=1 - required for HPA
seldon.average_utilization - target utilization of pods (values between 50-100% is recommended)
seldon.hpa_enabled=1 - enable Horizontal Pod Autoscaler


Benchmarking
************

Prerequisites
=============

To run the following examples, you need:

* Clone the github repository with all scripts
* Complete the inference evironment setup shown above
* Use Python v3.6

Setting the INGRESS_ADDRESS
---------------------------

The `INGRESS_ADDRESS` environment variable is used in the following examples in this guide and should be set with the server IP or domain name and port where Istio is exposed. Here, 10.0.0.1.nip.io will be used as a domain name.

The default nodePort exposed by Istio is 31380. It may be checked on the server with this command:

.. code-block:: bash

   kubectl -n istio-system get service istio-ingressgateway -o jsonpath='{.spec.ports[?(@.name=="http2")].nodePort}'

Set the INGRESS_ADDRESS:

.. code-block:: bash

   export INGRESS_ADDRESS=10.0.0.1.nip.io:31380


Standalone Client
=================

The :file:`standalone clients` script is the simplest and the fastest way to run benchmarks. This python script creates multiple clients to generate the requests sending jpeg files for inference and returns the throughput and latency numbers.
The script allows you to run a benchmark using just a few dependencies, which are listed in the `ai-inferencing/clients/standalone/requirements.txt` file.

Install the dependencies, start from the ai-inferencing directory and run:

.. code-block:: bash

   pip3.6 install -f ./clients/standalone/requirements.txt


To make sure that clients are not affecting Seldon performance
the script should be run on a different machine than the inference itself.

Verification
------------

To verify the script is working, verify with a small images set as follows:

#. Download the basic images set

   .. code-block:: bash

      cd ai-inferencing/clients/standalone
      wget https://github.com/SeldonIO/seldon-core/raw/master/examples/models/openvino_imagenet_ensemble/{imagenet_classes.json,input_images.txt,dog.jpeg,pelican.jpeg,zebra.jpeg}`.




#. Run the script

   .. code-block:: bash

      python3.6 seldon_grpc_client.py --ingress ${INGRESS_ADDRESS}

#. Output

   The output from the script will be similar to:

   .. code-block:: console

      total: 0.213 seconds, throughput 14.07 imgs/s
      53.244
      94.234
      52.158

   The output shows:
   * total time that test lasted (time from the first client start to the end of the last client request)
   * throughput, calculated as `number of requests / total test time`
   * every single line, except the first line described above, contains latencies of all requests done by all clients



Optional parameters
-------------------
Common:

* `--clients-number [INT]` - how many parallel instances of the single client should be spawned
* `--repeats [INT]` - how many times the script should repeat the test
* `--warmup [INT]` - how many repeats of tests should be done before starting time measuring
* `--debug [true/false]` - used to enable additional logging

Seldon communication settings:

* `--ingress` - IP and port where Kubernetes ingress is serving, e.g. `10.54.8.228:31380`
* `--deployment` - the name of the Seldon helm deployment a.k.a. ingress service name,
  i.e. `seldonovms-server-res`
* `--namespace` - namespace in which Seldon is deployed, i.e. `kubeflow`

Security:

* `--certs-file` - certificate file used for requests, setting this option turns on secure communication,

  NOTE: when using SSL, it is necessary to use a domain name, so if it is set IP in ingress address,
  make sure to add `.nip.io` suffix after IP, e.g. `10.54.8.228.nip.io:31380`

Custom images set:

* `--input-images-list` - path to file containing the list of images with classification, e.g. `input_images.txt`
* `--classes-file` - file with the classes dictionary, e.g. `imagenet_classes.json`
* `--input-base-path` - path to directory where images mentioned in `input-images-list` are stored,
  e.g. `/path/to/imagenet/directory`
* `--images-limit [INT]` - as images set can contain high number of images,
  using this parameter user can set max number of images uploaded in single repeat of the test.



Locust
======

`Locust.io`_ is a performance testing tool that allows us to use a Python script that is executed by simulating multiple users. For our example, Docker and Kubernetes are used for the Locust client deployment. The Locust Python client sends inference requests to the test platform based on the ResNet50 model.  A separate Kubernetes cluster is recommended for the client deployment, so as to avoid interfering with the cluster containing the inferencing engine.

This example can be used to model a more "natural" user behavior.  The load is not steady, and can be distributed.  Follow these steps to set up.

#. From the :file:`ai-inferencing/clients/locust/docker` directory set the following environment variables:

   .. code-block:: bash

      export REGISTRY_URL=<DOCKER REGISTRY URL>
      export INGRESS_ADDRESS=<ISTIO URL>

#. Build the Docker image:

   .. code-block:: bash

      docker build -t ${REGISTRY_URL}/seldon-ovms-locust-client:0.1 --network=host .

#. Push the image to the Docker registry

   .. code-block:: bash

      docker push ${REGISTRY_URL}/seldon-ovms-locust-client:0.1

#. Change to the :file:`ai-inferencing/clients/locust/helm` directory and modify the number of Lucust slave nodes by editing the :file:`values.yaml` file. Change `slaves_replicas` to the desired number of slave nodes.

#. Run Locust, modifying this command as your environment requires:

   .. code-block:: bash

      helm helm install --name locust --namespace kubeflow
      --set client.image=${REGISTRY_URL}/seldon-ovms-locust-client:0.1
      --set client.ingress=${INGRESS_ADDRESS}
      --set client.mount_images_volume.enabled=false
      --set client.images_path=./
      ../helm

   Values can be adjusted in the helm command using `--set` as shown in this sample command.  Note that `.nip.io` may be necessary when using ingress.

#. Find the UI port in the output from the helm command:

   .. code-block:: console

      NAME           TYPE       CLUSTER-IP      EXTERNAL-IP  PORT(S)            AGE
      locust         NodePort   10.110.167.232  <none>       8089:XXXXX/TCP     0s
      locust-master  ClusterIP  10.107.78.16    <none>       5557/TCP,5558/TCP  0s



#. On the system running the Kubernetes cluster, open a browser and go to `localhost:XXXXX` where `XXXXX` is the port found above.

#. Run tests using the UI.

   * In the Locust's landing page you will see 2 fields - Number of users to simulate and Hatch rate. Fill them and press "start swarming"
   * Locust should start the test. You can track the number of requests and fails in the "statistics" tab.

     .. figure:: /_figures/stacks/Locust_statistics.png
      :alt: Locust statistics
      :width:     600

   * In the "Failures" section you should see the type of errors - there should be only classified errors while running the test. This means that the sent image was classified incorrectly. That's normal behavior - we expect <100% accuracy for this model.

     .. figure:: /_figures/stacks/Locust_failures.png
      :alt: Locust failures
      :width:     600

   * You can see some simple charts in the "charts" tab. In "Response Times (ms)" chart, the green line is "Median Response Time", yellow line is "95% percentile".

     .. figure:: /_figures/stacks/Locust_charts.png
      :alt: Locust charts
      :width:     600

   * In the Exceptions tab, there might be some exceptions shown. This might happen when tested environments reach their response limit and some requests start to fail.

     .. figure:: /_figures/stacks/Locust_exception.png
      :alt: Locust exception
      :width:     600



Performance Tuning
==================

If you need to maximize the usage of available resources,
it is worth to adjust the threading parameters of inference serving instances. It is not enough to set the OMP_NUM_THREADS environment parameter which defines the number of threads used for inference on the CPU. In this case, the instances will scale across the nodes, but won't scale properly across the available cores on one node. Using the :command:`numactl` program is the solution in this case. :command:`numactl` allows you to run the instance on defined cores and uses memory from the same socket.

To find out how to assign the cores and memory properly run :command:`numactl -H` which will produce output like this:

.. code-block:: console

   available: 2 nodes (0-1)
   node 0 cpus: 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
   node 0 size: 195279 MB
   node 0 free: 128270 MB
   node 1 cpus: 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47
   node 1 size: 196608 MB
   node 1 free: 119445 MB
   node distances:
   node   0   1
     0:  10  21
     1:  21  10


In this case, the tests are run on Intel® Xeon® Platinum 6260L processor with 2 sockets(nodes) and 24 cores (CPUs) on each socket.
Running the inference serving the application with :command:`numactl --membind=0 --cpubind=0-3` forces the system to use 0,1,2,3 cores and memory located on the same socket (0). To use all available cores there is a need to create more service deployments assigned to the remaining cores.

The `ai-inferencing` repository contains an example deployment script with 2 cores per instance assignment.

Automatic CPU and memory binds in Seldon deployment
===================================================

The Seldon deployment works by default using one deployment only, that is, only one Seldon deployment should be spawned on one cluster node. When there is only one instance of the deployment, it is not necessary to use :command:`numactl` as all resources can be used by this single deployment.

In most cases that is far too many resources being used, so this setting is not optimal. Instead, use a mechanism that allows creating more than one deployment per node, and equally spliting CPU and memory banks resources between them, using :command:`numactl`.

First, it is necessary to set the following Helm values in the :file:`ai-inferencing/seldon/values.yaml` file:

* `instances` is a number describing how many Seldon deployments and  different resources ranges should be prepared (each CPU bind range would be used by only single one deployment) to be used by :file:`numactl` on a single socket. When this variable is set to 1, :file:`numactl` is not used.
* `cpus` should be set to the number of physical CPUs on a single node (without HyperThreading)
* `sockets` should be equal to the number of sockets on a single node and to memory banks number

Run the benchmark
=================

There are 2 scripts prepared to automate finding the best configuration
by customizing  the number of clients and Seldon instances.

#. :file:`clients/standalone/scale.sh`

   This is a script created to automatically scale and adjust Seldon instances to the selected configuration (2 or 24 cores per instance).

   It takes the following arguments:
   * the number, how many replicas (pods) each Seldon deployment should contain, this number should be equal to the number of the nodes in the cluster
   * the number, how many deployments should be created (each node would divide resources between deployments)

   This script is called by :file:`clients/standalone/benchmark.sh` script.

#. :file:`clients/standalone/benchmark.sh`

   This script is used to run benchmarks with selected configuration.
   There are 3 benchmark options to set:

   * number of `nodes` - how many nodes are in the cluster, this will scale Seldon deployments, to have one pod replica for each resource slice on each node.
   * list of `instances` values - how many Seldon instances would be started for a particular benchmark
   * list of `clients` values - it represents the number of clients to be used in particular benchmark

   It is necessary to customize the file itself to use the selected setup, setting environment variables mentioned below:

   * `SSH_PASSWORD` - password to Kubernetes master host
   * `SSH_USER` - user to be used to connect Kubernetes master host
   * `SSH_IP` - IP of the Kubernetes master host
   * `SCALE_FILE_PATH` - path to downloaded this repository on the Kubernetes master host, for example :file:`/path/to/this/repository/clients/standalone`
   * `INGRESS_ADDRESS` - server IP or domain name and port where Istio is exposed

   ssh settings should be set to Kubernetes master host where kubectl is usable.

.. note::  Before starting :file:`benchmark.sh` script, make sure all standalone client requirements are fulfilled, including installed python requirements and downloaded small sample images set if it is used.

The output from this file is shown on stdout and saved to file named
:file:`log_n<# nodes>_i<# instances per node>_c<# clients>_<date>.txt`.

The simplest way to monitor the cores usage is to run `htop` program on each tested node.

.. figure:: /_figures/stacks/htop.png
 :alt: htop output
 :width:     600

Results
=======

The test performed on a 2 node cluster with 48 cores per node showed that there are 2 optimal scenarios:

#. Low latency
   2 instances with 24 cores per instance on each node (4 instances on 2 nodes):

   .. code-block:: console

      1 (Node 1, socket 0): 'numactl --membind=0 --cpubind=0-23
      2 (Node 1, socket 1): 'numactl --membind=1 --cpubind=24-46
      3 (Node 2, socket 0): 'numactl --membind=0 --cpubind=0-23
      4 (Node 2, socket 1): 'numactl --membind=1 --cpubind=46-47


   Inference engine configuration for this case

   .. code-block:: console

      OMP_NUM_THREADS=24
      KMP_SETTINGS=1
      KMP_AFFINITY=granularity=fine,verbose,compact,1,0
      KMP_BLOCKTIME=1


#. High throughput

   24 instances with 2 cores per instance on each node (48 instances on 2 nodes):

   .. code-block:: console

      1 (Node 1, socket 0): 'numactl --membind=0 --cpubind=0-1
      2 (Node 1, socket 0): 'numactl --membind=0 --cpubind=2-3
      ...
      48 (Node 2, socket 1): 'numactl --membind=1 --cpubind=46-47


   Inference engine configuration:

   .. code-block:: console

      OMP_NUM_THREADS=2
      KMP_SETTINGS=1
      KMP_AFFINITY=granularity=fine,verbose,compact,1,0
      KMP_BLOCKTIME=1


*Intel, Xeon, and the Intel logo are trademarks of Intel Corporation or its subsidiaries.*


.. _Deep Learning Reference Stack: https://clearlinux.org/stacks/deep-learning
.. _Kubeflow: https://www.kubeflow.org/
.. _Seldon Core: https://docs.seldon.io/projects/seldon-core/en/latest/
.. _OpenVino Toolkit: https://software.intel.com/en-us/openvino-toolkit
.. _Intermediate Representation(IR): https://docs.openvinotoolkit.org/latest/_docs_MO_DG_prepare_model_convert_model_Converting_Model.html
.. _Istio: https://istio.io/
.. _Source-to-Image: https://github.com/openshift/source-to-image
.. _Min.io: https://min.io/
.. _2nd Generation Intel® Xeon® Scalable processor: https://www.intel.com/content/www/us/en/design/products-and-solutions/processors-and-chipsets/cascade-lake/2nd-gen-intel-xeon-scalable-processors.html
.. _Docker 18.09: https://kubernetes.io/docs/setup/production-environment/container-runtimes/
.. _Kubernetes 1.15.3: https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/
.. _gsutil: https://cloud.google.com/storage/docs/gsutil_install#linux
.. _Locust.io: https://locust.io
