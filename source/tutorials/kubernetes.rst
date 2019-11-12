.. _kubernetes:

Kubernetes\*
############

This tutorial describes how to install, configure, and start the `Kubernetes
container orchestration system`_ on |CL-ATTR| using a variety of `container
runtimes
<https://kubernetes.io/docs/setup/production-environment/container-runtimes/>`_.

Alternatively, you can get a Kubernetes cluster up and running quickly with
our `cloud-native-setup repository`_ which includes scripts to automates
cluster initialization.

.. contents::
   :local:
   :depth: 1

Background
***********

|CL| has builtin integrations to make setting up Kubernetes using a variety of
container runtimes.

For more background information see:

* `What is Kubernetes?`_
* `What is Docker?`_
* `What is containerd?`_
* `What is CRI+O?`_
* `What is Kata Containers?`_

Prerequisites
*************

This tutorial assumes you have already installed |CL|. For detailed
instructions on installing |CL| on a bare metal system, follow the :ref:`bare
metal installation tutorial<bare-metal-install-desktop>`.

Before you continue, update your |CL| installation with the following command:

.. code-block:: bash

   sudo swupd update

Learn about the benefits of having an up-to-date system for cloud
orchestration on the :ref:`swupd-guide` page.


Install Kubernetes
******************

Kubernetes, a set of supported :abbr:`CRI (Container Runtime Interface)`
runtimes and :abbr:`CNI (Container Network Interface)` are included in the
`cloud-native-basic`_ bundle.

#. Install the cloud-native-basic bundle to get these components:

.. code-block:: bash

   sudo swupd bundle-add cloud-native-basic


Configure host system
=====================

This tutorial uses the basic default Kubernetes configuration for to get
started. You can customize your Kubernetes configuration according to your
specific deployment and security needs.

The Kubernetes administration tool, :command:`kubeadm`, performs some
"`preflight checks`_" when initializing and starting a cluster. The steps
below are necessary to ensure those `preflight checks`_ pass successfully.


#. Enable IP forwarding:

   - Create the file :file:`/etc/sysctl.d/60-k8s.conf` to set the
     :command:`net.ipv4.ip_forward` parameter

     .. code-block:: bash

        sudo mkdir -p /etc/sysctl.d/

        sudo tee /etc/sysctl.d/99-kubernetes-cri.conf > /dev/null <<EOF
        net.bridge.bridge-nf-call-iptables  = 1
        net.ipv4.ip_forward                 = 1
        net.bridge.bridge-nf-call-ip6tables = 1
        EOF

   - Apply the change:

     .. code-block:: bash

        sudo sysctl --system


#. Disable swap:

   .. code-block:: bash

      sudo systemctl mask $(sed -n -e 's#^/dev/\([0-9a-z]*\).*#dev-\1.swap#p' /proc/swaps) 2>/dev/null
      sudo swapoff -a

   .. warning::

      Kubernetes is designed to work without swap. Performance degradation of other workloads can occur
      with swap disabled on systems with constrained memory resources.

#. Add the the system's hostname to the :file:`/etc/hosts` file. Kubernetes
   will read this file to locate the master host.

    .. code-block:: bash

       echo "127.0.0.1 localhost `hostname`" | sudo tee --append /etc/hosts


#. Enable the kubelet agent service to start at boot automatically:

   .. code-block:: bash

      sudo systemctl enable kubelet.service


Initialize the master node
**************************

In Kubernetes, a master node is part of the `Kubernetes Control Plane
<https://kubernetes.io/docs/concepts/#kubernetes-control-plane>`_. 

Initializing a new Kubernetes cluster involves crafting a :command:`kubeadm
init` command. Adding parameters to this command can control the fundamental
operating components of the cluster. This means it is important to understand
and choose network and runtime options before running a :command:`kubeadm
init` command.


Choose a pod network add-on
===========================

In Kubernetes, a `pod
<https://kubernetes.io/docs/concepts/workloads/pods/pod/>`_ is a group of one
or more containers and is the smallest deployable unit of computing in a
Kubernetes cluster. Pods have shared storage/network internally but
communication between pods requires additional configuration. If you want your
pods to be able to communicate with each other you must choose and install a
`pod network add-on`_. Otherwise, this section can be skipped. 

This is important to decide early because some pod network add-ons require
configuration during cluster initialization. Check whether or not your add-on
requires special flags when you initialize the master control plane.

If your chosen network add-on requires appending to the :command:`kubeadm
init` command, make note of it before continuing. 

For example, if you choose the *flannel* pod network add-on, then in later
steps you must add the following to the :command:`kubeadm init` command:

.. code-block:: console

   --pod-network-cidr 10.244.0.0/16



Choose a container runtime
==========================

Container runtimes are the underlying fabric that pod workloads execute inside
of. Different container runtimes offer different balances between features,
performance, and security. 

Kubernetes allows integration various container runtimes via a container
runtime interface (CRI). |CL| supports Kubernetes with the various runtimes
below:

* `Docker`_ with or without `Kata Containers`_
* `containerd`_ with or without `Kata Containers`_
* `CRI+O`_ with or without `Kata Containers`_

The container runtime that you choose will dictate the steps necessary to
initialize the master cluster with :command:`kubeadm init`.


Docker
------

For information on Docker, see `What is Docker?`_. To use Docker as the
Kubernetes container runtime:

#. Make sure Docker is installed:

   .. code:: bash

      sudo swupd bundle-add containers-basic

#. Start the Docker service and enable it to start automatically at boot:

   .. code::

      sudo systemctl enable --now docker.service


#. Run the kubeadm command to initialize the master node:

   .. important:: 

      You may need to add additional parameters to the command below,
      depending the pod network addon in use. In this example, *flannel* is
      being used for the pod networking. See `Choose a pod network add-on`_
      for more information.

   .. code:: bash

      sudo kubeadm init \
      --pod-network-cidr 10.244.0.0/16 #required for flannel


.. warning:: 

   Docker on |CL| will automatically use kata-runtime as the default Docker
   runtime if it is available.

   If you do not want to use the kata runtime or experience problems with
   cluster initialization, you can disable Docker from setting kata as the
   default runtime by running these commands:

   .. code:: bash 

      sudo rm /etc/systemd/system/docker.service.d/50-runtime.conf
      sudo systemctl mask docker-set-default-runtime.service

#. Once the cluster initialization is complete, continue reading about how to
   `Use your cluster`_.

containerd
----------

For information on containerd as as Kubernetes runtime, see `What is
containerd?`_. To use containerd as the Kubernetes container runtime:

#. Start the containerd service and enable it to run at boot automatically:

   .. code-block:: bash

      sudo systemctl enable --now containerd.service


#. Configure kubelet to use containerd and reload the service.

   .. code-block:: bash

      sudo mkdir -p  /etc/systemd/system/kubelet.service.d/

      cat << EOF | sudo tee  /etc/systemd/system/kubelet.service.d/0-containerd.conf
      [Service]                                                 
      Environment="KUBELET_EXTRA_ARGS=--container-runtime=remote --runtime-request-timeout=15m --container-runtime-endpoint=unix:///run/containerd/containerd.sock"
      EOF

   .. code:: bash

      systemctl daemon-reload

#. Run the kubeadm command to initialize the master node with the
   :command:`--cri-socket` parameter:

   .. important:: 

      You may need to add additional parameters to the command below,
      depending the pod network addon in use. In this example, *flannel* is
      being used for the pod networking. See `Choose a pod network add-on`_
      for more information.

   .. code-block:: bash

      sudo kubeadm init \
      --cri-socket=/run/containerd/containerd.sock \ #required for containerd
      --pod-network-cidr 10.244.0.0/16               #required for flannel


#. (Optional) By default, containerd will use the default runc as the default
   runtime. `Kata Containers`_ runtime can be set as the runtime on a per-pod
   basis. See the Kata Containers documentation on `creating an untrusted pod
   <https://github.com/kata-containers/documentation/blob/master/how-to/how-to-use-k8s-with-cri-containerd-and-kata.md#create-an-untrusted-pod-using-kata-containers>`_
   for more information.

#. Once the cluster initialization is complete, continue reading about how to
   `Use your cluster`_.


CRI+O
-----

For information on CRI+O as a Kubernetes container runtime, see `What is
CRI+O?`_. To use CRI+O as the Kubernetes container runtime:

#. Start the CRI-O service and enable it to run at boot automatically:

   .. code-block:: bash

      sudo systemctl enable --now crio.service

   When the crio service starts for the first time, it will create a
   configuration file for crio at :file:`/etc/crio/crio.conf`.

#. Run the kubeadm command to initialize the master node with the
   :command:`--cri-socket` parameter:

   .. important:: 

      You may need to add additional parameters to the command below,
      depending the pod network addon in use. In this example, *flannel* is
      being used for the pod networking. See `Choose a pod network add-on`_
      for more information.

   .. code-block:: bash

      sudo kubeadm init \
      --cri-socket=/run/crio/crio.sock \ #required for CRI+O
      --pod-network-cidr 10.244.0.0/16   #required for flannel


#. (Optional) CRI+O can provide Kata Containers as a runtime. If
   you want to use kata containers with CRI+O, register kata-runtime as a
   `RuntimeClass handler`_:

    .. code-block:: bash

       cat << EOF | sudo kubectl apply -f -
       kind: RuntimeClass
       apiVersion: node.k8s.io/v1beta1
       metadata:
           name: native
       handler: runc
       ---
       kind: RuntimeClass
       apiVersion: node.k8s.io/v1beta1
       metadata:
           name: kata-containers
       handler: kata
       EOF

   If you are using the *flannel* for pod networking (see `Choose a pod
   network add-on`_), with CRI-O + Kata Containers as the runtime, the
   :file:`/etc/crio/crio.conf` file needs to include the value below. On |CL|
   this is done automatically. 

   .. code-block:: console

      [crio.runtime]
      manage_network_ns_lifecycle = true



#. Once the cluster initialization is complete, continue reading about how to
   `Use your cluster`_.

Use your cluster
****************

Once your master control plane is successfully initialized, follow the
instructions presented about how to use your cluster and its *IP*, *token*,
and *hash* values are displayed. It is important that you record this
information because it is required to join additional nodes to the cluster.

A successful initialization looks like this:

.. code-block:: console

   Your Kubernetes control-plane has initialized successfully!

   To start using your cluster, you need to run the following as a regular user:

   mkdir -p $HOME/.kube
   sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
   sudo chown $(id -u):$(id -g) $HOME/.kube/config

   ...

   You can now join any number of machines by running the following on each node
   as root:

   kubeadm join <control-plane-host>:<control-plane-port> --token <token> --discovery-token-ca-cert-hash sha256:<hash>


With the first node of the cluster setup, you can continue expanding the
cluster with additional nodes and start deploying containerized applications.
For further information on using Kubernetes, see `Related topics`_. 

.. note:: 

   By default, the master node does not run any pods for security reasons. To
   setup a single-node cluster and allow the master node to also run pods, the
   master node will need to be untained. See the Kubernetes documentation on
   `control plane node isolation
   <https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/#control-plane-node-isolation>`_.


Reference
*********

What is Kubernetes?
===================

Kubernetes (K8s) is an open source system for automating deployment, scaling,
and management of containerized applications. It groups containers that make
up an application into logical units for easy management and discovery.

Kubernetes supports using a variety of `container runtimes
<https://kubernetes.io/docs/setup/production-environment/container-runtimes/>`_.

What is Docker?
===============

`Docker <https://www.docker.com/>`_ is an engine for running software packaged
as functionally complete units, called containers, using the same operating
system kernel.

The default built-in runtime provided by Kubernetes is using the system Docker
installation via Dockershim and as a result is one of the simplest to use. One
limitation of using Dockershim is that all pods on the Kubernetes node will
inherit and use the default runtime that Docker is set to use. To be able to
specify a container runtime per-Kerbernetes service, use CRI+O or containerd. 


What is containerd?
===================

`containerd <https://containerd.io/>`_ is the runtime that the Docker engine
is built on top of. 

Kubernetes can use containerd directly instead of going through the Docker
engine for increased robustness and performance. See the `blog post on
kubernetes containerd integration
<https://kubernetes.io/blog/2018/05/24/kubernetes-containerd-integration-goes-ga/>`_
for more details.

containerd allows setting a different runtime per-pod.

What is CRI+O?
==============

`CRI+O <https://cri-o.io/>`_ is a lightweight alternative to using Docker as
the runtime for kubernetes. It allows Kubernetes to use any OCI-compliant
runtime as the container runtime for running pods, such as runc and
Kata Containers as the container runtimes.

CRI+O allows setting a different runtime per-pod.


What is Kata Containers?
========================

`Kata Containers`_ is an alternative OCI compatible runtime that secures
container workloads in a lightweight virtual machine. It provides stronger
workloads isolation using hardware virtualization technology as a second layer
of defense for untrusted workloads or multi-tenant scenarios.

The Kata Containers\* (kata-runtime) adheres to :abbr:`OCI (Open Container
Initiative*)` guidelines and works seamlessly with Kubernetes through Docker,
containerd, or CRI+O.


cloud-native-setup automation
=============================

Instead of manually installing a Kubernetes cluster as described in this
tutorial, you can clone the `cloud-native-setup repository`_  on your system
and follow the instructions. 

It includes helper scripts to automate configuration.


Related topics
==============

* `Understanding basic Kubernetes architecture`_

* Installing a `pod network add-on`_

* `Joining your nodes`_

* `Deploying an application to your cluster`_

*  See our document on :ref:`Kubernetes best practices <kubernetes-bp>`


Troubleshooting
***************

Package configuration customization
===================================

|CL| is a stateless system that looks for user-defined package configuration
files in the :file:`/etc/<package-name>` directory to be used as default. If
user-defined files are not found, |CL| uses the distribution-provided
configuration files for each package.

If you customize any of the default package configuration files, you **must**
store the customized files in the :file:`/etc/` directory. If you edit any of
the distribution-provided default files, your changes will be lost in the next
system update as the default files will be overwritten with the updated files.

Learn more about :ref:`stateless` in |CL|.


Proxy issues
============

If you receive any of the messages below, check outbound Internet access. You
may be behind a proxy server. Try configuring your :ref:`proxy settings
<tutorial-proxy>`, using the environment variables *HTTP_PROXY*,
*HTTPS_PROXY*, and *NO_PROXY* as required in your environment.:

   * Images cannot be pulled.
   * Connection refused error.
   * Connection timed-out or Access Refused errors.

If you use an outbound proxy server, you must set your proxy environment
variables and create an appropriate proxy configuration file for kubectl and
container runtime services. Ensure that your local IP address is **explicitly
included** in the environment variable *NO_PROXY*. (Setting *localhost* is not
enough.)

If you have already set your proxy environment variables, run the following
commands as a shell script to configure proxies for all services in one step:

.. code-block:: bash

   services=(kubelet docker crio containerd)
   for s in "${services[@]}"; do
   sudo mkdir -p "/etc/systemd/system/${s}.service.d/"
   cat << EOF | sudo tee "/etc/systemd/system/${s}.service.d/proxy.conf"
   [Service]
   Environment="HTTP_PROXY=${http_proxy}"
   Environment="HTTPS_PROXY=${https_proxy}"
   Environment="SOCKS_PROXY=${socks_proxy}"
   Environment="NO_PROXY=${no_proxy}"
   EOF
   done




DNS issues
==========

* <HOSTNAME> not found in <IP> message.

   Your DNS server may not be appropriately configured. Try adding an entry
   to the :file:`/etc/hosts` file with your host's IP and Name.

   For example: 100.200.50.20 myhost

   Use the commands :command:`hostname` and :command:`hostname -I` to
   retrieve them.



.. _Kubernetes container orchestration system: https://kubernetes.io/

.. _Kata Containers: https://katacontainers.io/

.. _cloud-native-basic: https://github.com/clearlinux/clr-bundles/blob/master/bundles/cloud-native-basic

.. _preflight checks: https://kubernetes.io/docs/reference/setup-tools/kubeadm/implementation-details/#preflight-checks

.. _Understanding basic Kubernetes architecture: https://kubernetes.io/docs/user-journeys/users/application-developer/foundational/#section-3

.. _Deploying an application to your cluster: https://kubernetes.io/docs/user-journeys/users/application-developer/foundational/#section-2

.. _pod network add-on: https://kubernetes.io/docs/setup/independent/create-cluster-kubeadm/#pod-network

.. _Joining your nodes: https://kubernetes.io/docs/setup/independent/create-cluster-kubeadm/#join-nodes

.. _cloud-native-setup repository: https://github.com/clearlinux/cloud-native-setup/tree/master/clr-k8s-examples

.. _control-plane node: https://kubernetes.io/docs/concepts/#kubernetes-control-plane

.. _RuntimeClass handler: https://kubernetes.io/docs/concepts/containers/runtime-class/
