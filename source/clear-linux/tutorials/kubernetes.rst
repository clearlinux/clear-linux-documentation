.. _kubernetes:

Run Kubernetes\* on |CL-ATTR|
#############################

This tutorial describes how to install, configure, and run the 
`Kubernetes container orchestration system`_ on |CL-ATTR| using different
container engines and runtimes.

Kubernetes\* is an open source system for automating deployment, scaling, and
management of containerized applications. It groups containers that make up
an application into logical units for easy management and discovery.

Runc and Kata Containers\* kata-runtime adhere to :abbr:`OCI (Open Container Initiative*)` guidelines and work seamlessly with Kubernetes.
`Kata Containers`_ provide strong isolation for untrusted workloads or 
multi-tenant scenarios.  Runc and Kata Containers can be allocated on a 
per-pod basis so you can mix and match both on the same host
to suit your needs.

Prerequisites
*************

This tutorial assumes you have installed |CL| and updated to the latest
release on your host system. You can learn about the benefits of having an 
up-to-date system for cloud orchestration in the :ref:`swupd-about`
page. For detailed instructions on installing |CL| on a bare metal system,
follow the :ref:`bare metal installation tutorial<bare-metal-install>`.

Before you install any new packages, update |CL| with the following command:

.. code-block:: bash

   sudo swupd update

Install Kubernetes and CRI runtimes
***********************************

Kubernetes and a set of supported :abbr:`CRI (Container Runtime Interface)` 
runtimes are included in the `cloud-native-basic`_ bundle. To install the 
framework, enter the following command:

.. code-block:: bash

   sudo swupd bundle-add cloud-native-basic

Configure Kubernetes
********************

This tutorial uses the basic default Kubernetes configuration for simplicity.
You must define your Kubernetes configuration according to your specific
deployment and your security needs.

#. Enable IP forwarding to avoid "preflight check" errors:

   Create (or edit if it exists) the file :file:`/etc/sysctl.d/60-k8s.conf`
   and include the following line:

   .. code-block:: bash

      net.ipv4.ip_forward = 1

   Apply the change:

   .. code-block:: bash

      sudo systemctl restart systemd-sysctl

#. Enable kubelet service:

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
         
#. Create (or edit if it exists) the hosts file that kubernetes will read to 
   locate master's host:

   .. code-block:: bash

      echo "127.0.0.1 localhost `hostname`" >> /etc/hosts

#. Configure the Kubernetes runtime interface, either:

   a) Run Kubernetes with Docker + runc:

      #. Enable docker.service:

         .. code-block:: bash

            sudo systemctl enable docker.service

      #. Create (or edit if it exists) the file 
         :file:`/etc/systemd/system/docker.service.d/51-runtime.conf` and include the following lines:

         .. code-block:: bash

            [Service]
            Environment="DOCKER_DEFAULT_RUNTIME=--default-runtime runc"

      #. Create (or edit if it exists) the file :file:`/etc/systemd/system/kubelet.service.d/10-kubeadm.conf` and include the following lines:

         .. code-block:: bash

            [Service]
            Environment="KUBELET_EXTRA_ARGS="

      #. Restart services:

         .. code-block:: bash

            sudo systemctl daemon-reload
            sudo systemctl restart docker
            sudo systemctl restart kubelet

   or:

   b) Run Kubernetes with CRI-O + your desired runtime. You can use multiple
      runtimes with CRI-O, including *runc* and *kata-runtime*. To use
      CRI-O + *kata-runtime*:

      #. Enable crio.service:

         .. code-block:: bash

            sudo systemctl enable crio.service

      #. Restart services:

         .. code-block:: bash

            sudo systemctl restart crio
            sudo systemctl restart kubelet

Run Kubernetes for the first time
*********************************

#. Prepare your system to run Kubernetes for the first time with the
   following commands, either:

   a) If you are running Kubernetes with Docker + runc:

      .. code-block:: bash

         sudo systemctl daemon-reload
         sudo systemctl restart docker
         sudo systemctl restart kubelet

   or:

   b) If you are running Kubernetes with CRI-O + kata-runtime:

      .. code-block:: bash

         sudo systemctl daemon-reload
         sudo systemctl restart crio
         sudo systemctl restart kubelet

#. Initialize the master control plane with the following command, either:

   a) If you are running Kubernetes with Docker + runc:

      .. code-block:: bash

         sudo -E kubeadm init --pod-network-cidr 10.244.0.0/16 --ignore-preflight-errors=SystemVerification

   or:

   b) If you are running Kubernetes with CRI-O + kata-runtime:

      .. code-block:: bash

         sudo -E kubeadm init --pod-network-cidr 10.244.0.0/16 --cri-socket=/run/crio/crio.sock

Once your master control is successfully initialized, instructions on how to
use your cluster and its *IP*, *token*, and *hash* values are displayed. It 
is important that you note these cluster values because they will be needed 
when joining worker nodes to the cluster and some of them have a valid
period. The values are presented in a format similar to:

.. code-block:: bash

   kubeadm join <master-ip>:<master-port> --token <token> --discovery-token-ca-cert-hash <hash>


**Congratulations!**

You've successfully installed and set up Kubernetes in |CL| using Docker and 
runc or CRI-O and kata-runtime. You are now ready to follow on-screen 
instructions to deploy a pod network to the cluster and join worker nodes 
with the displayed token and IP information.

Related Topics
**************

Read the Kubernetes documentation to learn more about: 

* `Understanding basic Kubernetes architecture`_

* `Deploying an application to your cluster`_

* `Installing a pod network add-on`_

* `Joining your nodes`_

Package configuration customization in |CL| (Optional)
******************************************************

|CL| is a stateless system that looks for user-defined package configuration
files in the :file:`/etc/<package-name>` directory to be used as default. If
user-defined files are not found, |CL| uses the distribution-provided
configuration files for each package.

If you customize any of the default package configuration files, you *must*
store the customized files in the :file:`/etc/` directory. If you edit any of
the distribution-provided default files, your changes will be lost in the
next system update.

For example, to customize CRI-O configuration in your system you can run the
following commands:

.. code-block:: bash

   sudo mkdir /etc/crio
   sudo cp /usr/share/defaults/crio/crio.conf /etc/crio/
   sudo $EDITOR /etc/crio/crio.conf

Learn more about `Stateless in Clear Linux`_ and view the `Clear Linux documentation`_.

Proxy configuration (optional)
******************************

If you use a proxy server, you must set your proxy environment variables and
create an appropriate proxy configuration file for both CRI-O and Docker
services. Consult your IT department if you are behind a corporate proxy for
the appropriate values. Ensure that your local IP is **explicitly included**
in the environment variable *NO_PROXY*. (Setting *localhost* is not enough.)

If you have already set your proxy environment variables, run the following
commands as a shell script to configure all of these services in one step:

.. code-block:: bash

      services=('crio' 'docker')
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

  Your DNS server may not be appropriately configured. You can try adding
  an entry to the :file:`/etc/hosts` file with your host's IP and Name. Use
  the commands *hostname* and *hostname -I* to retrieve them.
  For example: 100.200.50.20   myhost

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
  proxy settings that kubernetes will actually use, run the commands:

  * *"echo $HTTP_PROXY"* 
  * *"echo $HTTPS_PROXY"* 
  * *"echo $NO_PROXY"* 

  If the displayed proxy values are different from your assigned values, the cluster initialization will fail. Contact your IT support team to learn the appropriate procedure to set the proxy variables permanently, and make them available for all the access forms that you will use (for example: remote ssh access).

.. _Kubernetes container orchestration system: https://kubernetes.io/

.. _Kata Containers: https://katacontainers.io/

.. _Software Update documentation: https://clearlinux.org/documentation/clear-linux/concepts/swupd-about#updating

.. _cloud-native-basic: https://github.com/clearlinux/clr-bundles/blob/master/bundles/cloud-native-basic

.. _Understanding basic Kubernetes architecture: https://kubernetes.io/docs/user-journeys/users/application-developer/foundational/#section-3

.. _Deploying an application to your cluster: https://kubernetes.io/docs/user-journeys/users/application-developer/foundational/#section-2

.. _Installing a pod network add-on: https://kubernetes.io/docs/setup/independent/create-cluster-kubeadm/#pod-network

.. _Joining your nodes: https://kubernetes.io/docs/setup/independent/create-cluster-kubeadm/#join-nodes

.. _Stateless in Clear Linux: https://clearlinux.org/features/stateless

.. _Clear Linux documentation: https://clearlinux.org/documentation/clear-linux

