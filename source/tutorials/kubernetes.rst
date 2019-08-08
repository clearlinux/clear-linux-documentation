.. _kubernetes:

Kubernetes\*
############

This tutorial describes how to install, configure, and run the
`Kubernetes container orchestration system`_ on |CL-ATTR| using CRI+O and
kata-runtime.

.. contents::
   :local:
   :depth: 1

Description
***********

Kubernetes is an open source system for automating deployment, scaling, and
management of containerized applications. It groups containers that make up
an application into logical units for easy management and discovery. Get up
and running quickly with our `Cloud native setup automation`_.

Kata Containers\* kata-runtime adheres to
:abbr:`OCI (Open Container Initiative*)` guidelines and works seamlessly with
Kubernetes. `Kata Containers`_ provides strong isolation for untrusted
workloads or  multi-tenant scenarios. Kata Containers can be
allocated on a per-pod basis, so you can mix and match both on the same host
to suit your needs.

Prerequisites
*************

This tutorial assumes you have already installed |CL|. For detailed
instructions on installing |CL| on a bare metal system, follow the
:ref:`bare metal installation tutorial<bare-metal-install-desktop>`.
Learn about the benefits of having an up-to-date system for cloud
orchestration on the :ref:`swupd-guide` page.

Before you install any new packages, update |CL| with the following command:

.. code-block:: bash

   sudo swupd update

Install Kubernetes and CRI runtimes
***********************************

Kubernetes, a set of supported :abbr:`CRI (Container Runtime Interface)`
runtimes, and networking plugins, are included in the `cloud-native-basic`_
bundle.

To install this framework, enter the following command:

.. code-block:: bash

   sudo swupd bundle-add cloud-native-basic

.. note::

   For more on networking plugins, see `Install pod network add-on`_.

Configure Kubernetes
********************

This tutorial uses the basic default Kubernetes configuration for simplicity.
You must define your Kubernetes configuration according to your specific
deployment and your security needs.

#. Enable IP forwarding to avoid kubeadm `preflight check`_ errors:

   Create (or edit if it exists) the file :file:`/etc/sysctl.d/60-k8s.conf`
   and include the following line:

   .. code-block:: bash

      net.ipv4.ip_forward = 1

   Apply the change:

   .. code-block:: bash

      sudo systemctl restart systemd-sysctl

#. Enable the kubelet service:

   .. code-block:: bash

      sudo systemctl enable kubelet.service

#. Disable swap using one of the following methods, either:

   a) Temporarily:

      .. code-block:: bash

         sudo swapoff -a

      .. note::

         Swap will be enabled at next reboot, causing failures in
         your cluster.

   or:

   b) Permanently:

      Mask the swap partition:

      .. code-block:: bash

         sudo systemctl mask $(sed -n -e 's#^/dev/\([0-9a-z]*\).*#dev-\1.swap#p' /proc/swaps) 2>/dev/null
         sudo swapoff -a

      .. note::

         On systems with limited resources, some performance degradation may
         be observed while swap is disabled.

#. Switch to root to modify the `hosts` file:

   .. code-block:: bash

      sudo -s

#.  Create (or edit if it exists) the hosts file that Kubernetes will read to
    locate the master's host:

    .. code-block:: bash

       echo "127.0.0.1 localhost `hostname`" >> /etc/hosts

#.  Exit root:

    .. code-block:: bash

       exit

Configure and run Kubernetes
****************************

This section describes how to configure and run Kubernetes with CRI-O and
kata-runtime.

Configure and run CRI-O + kata-runtime
======================================

#.  Enable the CRI-O service:

    .. code-block:: bash

       sudo systemctl enable crio.service

#.  Enter the commands:

    .. code-block:: bash

       sudo systemctl daemon-reload
       sudo systemctl restart crio

#.  Initialize the master control plane with the command below and follow the
    displayed instructions to set up `kubectl`:

    .. code-block:: bash

       sudo kubeadm init --cri-socket=/run/crio/crio.sock

#.  Register kata-runtime as a RuntimeClass handler:

    .. code-block:: bash

       cat << EOF | kubectl apply -f -
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

Install pod network add-on
**************************

You must choose and install a `pod network add-on`_ to allow your pods to
communicate. Check whether or not your add-on requires special flags when you
initialize the master control plane.

**Notes about flannel add-on**

If you choose the `flannel` add-on, then you must add the following to the
`kubeadm init` command:

.. code-block:: bash

   --pod-network-cidr 10.244.0.0/16

Furthermore, if you are using CRI-O and `flannel` and you want to use
Kata Containers, edit the :file:`/etc/crio/crio.conf` file to add:

..  code-block:: bash

    [crio.runtime]
    manage_network_ns_lifecycle = true

Use your cluster
****************

Once your master control plane is successfully initialized, instructions on
how to use your cluster and its *IP*, *token*, and *hash* values are
displayed. It is important that you record the cluster values because they
are needed when joining worker nodes to the cluster. Some values have a valid
period. The values are presented in a format similar to:

.. code-block:: bash

   kubeadm join <master-ip>:<master-port> --token <token> --discovery-token-ca-cert-hash <hash>

**Congratulations!**

You've successfully installed and set up Kubernetes in |CL| using CRI-O and
kata-runtime. You are now ready to follow on-screen instructions to deploy a
pod network to the cluster and join worker nodes with the displayed token
and IP information.

Related topics
**************

Read the Kubernetes documentation to learn more about:

*  Deploying Kubernetes with a `cloud-native-setup`_

*  :ref:`Kubernetes best practices <kubernetes-bp>`

* `Understanding basic Kubernetes architecture`_

* `Deploying an application to your cluster`_

* Installing a `pod network add-on`_

* `Joining your nodes`_

Cloud native setup automation
*****************************

Optional: Clone the `cloud-native-setup`_ repository on your system and
follow the instructions. This repository includes helper scripts to automate
configuration.

Package configuration customization (optional)
**********************************************

|CL| is a stateless system that looks for user-defined package configuration
files in the :file:`/etc/<package-name>` directory to be used as default. If
user-defined files are not found, |CL| uses the distribution-provided
configuration files for each package.

If you customize any of the default package configuration files, you **must**
store the customized files in the :file:`/etc/` directory. If you edit any of
the distribution-provided default files, your changes will be lost in the
next system update.

For example, to customize CRI-O configuration in your system, run the
following commands:

.. code-block:: bash

   sudo mkdir /etc/crio
   sudo cp /usr/share/defaults/crio/crio.conf /etc/crio/
   sudo $EDITOR /etc/crio/crio.conf

Learn more about :ref:`stateless` in |CL|.

Proxy configuration (optional)
******************************

If you use a proxy server, you must set your proxy environment variables and
create an appropriate proxy configuration file for both CRI-O services. Consult
your IT department if you are behind a corporate proxy for the appropriate
values. Ensure that your local IP is **explicitly included** in the environment
variable *NO_PROXY*. (Setting *localhost* is not enough.)

If you have already set your proxy environment variables, run the following
commands as a shell script to configure all of these services in one step:

.. code-block:: bash

   services=('crio')
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

Troubleshooting
***************

* <HOSTNAME> not found in <IP> message.

  Your DNS server may not be appropriately configured. Try adding an
  entry to the :file:`/etc/hosts` file with your host's IP and Name.

  For example: 100.200.50.20 myhost

  Use the commands :command:`hostname` and :command:`hostname -I`
  to retrieve them.

* Images cannot be pulled.

  You may be behind a proxy server. Try configuring your proxy settings,
  using the environment variables *HTTP_PROXY*, *HTTPS_PROXY*, and *NO_PROXY*
  as required in your environment.

* Connection refused error.

  If you are behind a proxy server, you may need to add the master's IP to
  the environment variable *NO_PROXY*.

* Connection timed-out or Access Refused errors.

  You must ensure that the appropriate proxy settings are available from the
  same terminal where you will initialize the control plane. To verify the
  proxy settings that Kubernetes will actually use, run the commands:

  .. code-block:: bash

    echo $HTTP_PROXY
    echo $HTTPS_PROXY
    echo $NO_PROXY

  If the displayed proxy values are different from your assigned values, the
  cluster initialization will fail. Contact your IT support team to learn how
  to set the proxy variables permanently, and how to make them available for
  all the types of access that you will use, such as remote SSH access.

  If the result of the above commands is blank, you may need to add a
  ``profile`` to the :file:`/etc` directory. To do so, follow these steps.

  #. Create a `profile` in :file:`/etc`

     .. code-block:: bash

        sudo touch profile

  #. With your preferred editor, open `profile`, and enter your proxy settings.
     An example is shown below.

     .. code-block:: bash

        export "HTTP_PROXY=http://proxy.example.com:443"
        export "HTTPS_PROXY=http://proxy.example.com:445"
        export "SOCKS_PROXY=http://proxy.example.com:1080"
        export "NO_PROXY= site.com,.site.com,localhost,127.0.0.1,<master IP>

     .. note::

        <master IP> can be obtained by running :command:`ifconfig`.

  #. Save and exit the `profile`.

  #. Update your system's environment settings by executing the following
     command:

     .. code-block:: bash

        sudo source profile

  #. To ensure your system isn't running previous session variables, run:

     .. code-block:: bash

        sudo kubeadm reset --cri-socket=/run/crio/crio.sock

  #. Continue below while passing `-E` in the command as shown.

* Missing environment variables.

  If you are behind a proxy server, pass environment variables by adding *-E*
  to the command that initializes the master control plane.

  .. code-block:: bash

     /* Kubernetes with CRI-O + kata-runtime */
     sudo -E kubeadm init --cri-socket=/run/crio/crio.sock



.. _Kubernetes container orchestration system: https://kubernetes.io/

.. _Kata Containers: https://katacontainers.io/

.. _cloud-native-basic: https://github.com/clearlinux/clr-bundles/blob/master/bundles/cloud-native-basic

.. _preflight check: https://kubernetes.io/docs/reference/setup-tools/kubeadm/implementation-details/#preflight-checks

.. _Understanding basic Kubernetes architecture: https://kubernetes.io/docs/user-journeys/users/application-developer/foundational/#section-3

.. _Deploying an application to your cluster: https://kubernetes.io/docs/user-journeys/users/application-developer/foundational/#section-2

.. _pod network add-on: https://kubernetes.io/docs/setup/independent/create-cluster-kubeadm/#pod-network

.. _Joining your nodes: https://kubernetes.io/docs/setup/independent/create-cluster-kubeadm/#join-nodes

.. _cloud-native-setup: https://github.com/clearlinux/cloud-native-setup/tree/master/clr-k8s-examples
