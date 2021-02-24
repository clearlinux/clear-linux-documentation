.. _kubernetes-migration:

Kubernetes\* migration
######################

This guide describes how to migrate `Kubernetes container orchestration system`_ on |CL-ATTR| from 1.17.x to 1.19.x.

.. contents::
   :local:
   :depth: 1

Background
**********

The version of Kubernetes\* was bumped from 1.17.7 to 1.19.4 in |CL-ATTR|
release 34090. This guide and the |CL| bundle `k8s-migration` were created
to help facilitate migration of a cluster from 1.17.x to the latest 1.19.x .

The new |CL| bundle `k8s-migration` was added in |CL-ATTR| release 34270.

Prerequisites
*************

* Make sure you check any updates to kubernetes upgrade doc for caveats related to the version that is running in the cluster.
* Make sure ALL the nodes are in Ready state. Without that, the cluster cannot be upgraded.
  Either fix the broken nodes or remove them from the cluster.

.. contents::
   :local:
   :depth: 1

Upgrade 1.17.x ---> 1.18.15
***************************

#. Upgrade Control Node to 1.18.15 first

   First step would be to upgrade one of the main control node and
   update kubernetes components on them. You will need to have a newer
   version of :command:`kubeadm` for the upgrade to work. Please consult
   `kubeadm upgrade guide`_
   for any caveats from your current version to the new one.

   Update |CL| to the latest release to update the kubernetes version.

   .. code-block:: bash

      sudo -E swupd update

   .. note::
      Note: PLEASE DO NOT REBOOT YOUR SYSTEM AT THIS TIME. |CL| is awesome and
      your stuff will work just fine.

#. Add the new Kubernetes migration bundle which contains the 1.18.15 binaries.

   .. code-block:: bash

      sudo -E swupd bundle-add k8s-migration

#. Find the upgrade version of kubeadm that can used. This should be 1.18.15.

   This command will show the command and possible jumps that can be made from the current kubernetes version.

   .. code-block:: bash

      sudo -E /usr/k8s-migration/bin/kubeadm upgrade plan

   Sample output:

   .. code-block:: console

      [upgrade/config] Making sure the configuration is correct:
      [upgrade/config] Reading configuration from the cluster...
      [upgrade/config] FYI: You can look at this config file with 'kubectl -n kube-system get cm kubeadm-config -oyaml'
      [preflight] Running pre-flight checks.
      [upgrade] Running cluster health checks
      [upgrade] Fetching available versions to upgrade to
      [upgrade/versions] Cluster version: v1.17.17
      [upgrade/versions] kubeadm version: v1.18.15
      I0209 21:12:49.868786  832739 version.go:252] remote version is much newer: v1.20.2; falling back to: stable-1.18
      [upgrade/versions] Latest stable version: v1.18.15
      [upgrade/versions] Latest stable version: v1.18.15
      [upgrade/versions] Latest version in the v1.17 series: v1.17.17
      [upgrade/versions] Latest version in the v1.17 series: v1.17.17

      Components that must be upgraded manually after you have upgraded the control plane with 'kubeadm upgrade apply':
      COMPONENT   CURRENT       AVAILABLE
      Kubelet     3 x v1.17.7   v1.18.15

      Upgrade to the latest stable version:

      COMPONENT            CURRENT    AVAILABLE
      API Server           v1.17.17   v1.18.15
      Controller Manager   v1.17.17   v1.18.15
      Scheduler            v1.17.17   v1.18.15
      Kube Proxy           v1.17.17   v1.18.15
      CoreDNS              1.6.5      1.6.7
      Etcd                 3.4.3      3.4.3-0

      You can now apply the upgrade by executing the following command:

        kubeadm upgrade apply v1.18.15

#. Upgrade the node to the intermediate 1.18.15 version of Kubernetes.

   .. code-block:: bash

      sudo -E /usr/k8s-migration/bin/kubeadm upgrade apply v1.18.15

   .. note::
      Note: Do **not** reboot the system yet.

#. Upgrade Additional Control Nodes to 1.18.15

   In multi-node control plane, verify all the control plane nodes are updated prior to upgrading the worker nodes/SUTs.

#. Upgrade Other Nodes to 1.18.15

   For each of the other nodes:

   a. Update |CL| to the latest release to update the kubernetes version.

      .. code-block:: bash

         sudo -E swupd update

   #. Add the new Kubernetes migration bundle which contains the 1.18.15 binaries.

      .. code-block:: bash

         sudo -E swupd bundle-add k8s-migration

   #. On the **Admin node**, drain the Client node *FIRST*

      .. code-block:: bash

         /usr/k8s-migration/bin/kubectl drain <CLIENT_NODE_NAME> --ignore-daemonsets --delete-local-data

   #. Back on the **Client node**, upgrade Kubernetes on the Client

      .. code-block:: bash

         sudo -E /usr/k8s-migration/bin/kubeadm upgrade node

   #. On the **Admin node**, re-enable the Client

      .. code-block:: bash

         /usr/k8s-migration/bin/kubectl uncordon <CLIENT_NODE_NAME>


   #. Back on the **Client node**, restart Kubernetes on the Client

      .. code-block:: bash

         sudo -E systemctl restart kubelet

#. Restart Kubernetes on the Admin node(s) to finish the 1.18.x upgrade

   .. code-block:: bash

      sudo -E systemctl restart kubelet

   .. note::
      Note: Wait for all nodes to be Ready and showing the 1.19.x version.
      This version will now show as it is the released version the
      service files will see and use, but the Nodes are *not* upgraded yet.

Upgrade 1.18.15 ---> 1.19.x
***************************

#. Upgrade Control Node to 1.19.x

   Now that systems are upgraded to the intermediate release of 1.18.15
   each of the nodes can be upgraded to the latest 1.19.x release.

#. Find the upgrade version of kubeadm that can used. This should be 1.19.x.

   This command will show the command and possible jumps that can be made from the current kubernetes version.

   .. code-block:: bash

      sudo -E kubeadm upgrade plan

   Sample output:

   .. code-block:: console

      [upgrade/config] Making sure the configuration is correct:
      [upgrade/config] Reading configuration from the cluster...
      [upgrade/config] FYI: You can look at this config file with 'kubectl -n kube-system get cm kubeadm-config -oyaml'
      [preflight] Running pre-flight checks.
      [upgrade] Running cluster health checks
      [upgrade] Fetching available versions to upgrade to
      [upgrade/versions] Cluster version: v1.18.15
      [upgrade/versions] kubeadm version: v1.19.7
      I0209 23:08:23.810900  925910 version.go:252] remote version is much newer: v1.20.2; falling back to: stable-1.19
      [upgrade/versions] Latest stable version: v1.19.7
      [upgrade/versions] Latest stable version: v1.19.7
      [upgrade/versions] Latest version in the v1.18 series: v1.18.15
      [upgrade/versions] Latest version in the v1.18 series: v1.18.15

      Components that must be upgraded manually after you have upgraded the control plane with 'kubeadm upgrade apply':
      COMPONENT   CURRENT       AVAILABLE
      kubelet     3 x v1.17.7   v1.19.7

      Upgrade to the latest stable version:

      COMPONENT                 CURRENT    AVAILABLE
      kube-apiserver            v1.18.15   v1.19.7
      kube-controller-manager   v1.18.15   v1.19.7
      kube-scheduler            v1.18.15   v1.19.7
      kube-proxy                v1.18.15   v1.19.7
      CoreDNS                   1.6.7      1.7.0
      etcd                      3.4.3-0    3.4.13-0

      You can now apply the upgrade by executing the following command:

        kubeadm upgrade apply v1.19.7

      The table below shows the current state of component configs as understood by this version of kubeadm.
      Configs that have a "yes" mark in the "MANUAL UPGRADE REQUIRED" column require manual config upgrade or
      resetting to kubeadm defaults before a successful upgrade can be performed. The version to manually
      upgrade to is denoted in the "PREFERRED VERSION" column.

      API GROUP                 CURRENT VERSION   PREFERRED VERSION   MANUAL UPGRADE REQUIRED
      kubeproxy.config.k8s.io   v1alpha1          v1alpha1            no
      kubelet.config.k8s.io     v1beta1           v1beta1             no

#. Upgrade the node to the latest 1.19.x version of Kubernetes.

   .. code-block:: bash

      sudo -E /usr/bin/kubeadm upgrade apply v1.19.7

   .. note::

      Note: Do **not** reboot the system yet.

#. Upgrade Additional Control Nodes to 1.19.x

   In multi-node control plane, verify all the control plane nodes are updated prior to upgrading the worker nodes/SUTs.

#. Upgrade Other Nodes to 1.19.x

   For each of the other nodes:

   a. On the **Admin node**, drain the Client *FIRST*

      .. code-block:: bash

         kubectl drain <CLIENT_NODE_NAME> --ignore-daemonsets

   #. Back on the **Client node**, upgrade Kubernetes on the Client

      .. code-block:: bash

         sudo -E kubeadm upgrade node

   #. On the **Admin node**, re-enable the Client

      .. code-block:: bash

         kubectl uncordon <CLIENT_NODE_NAME>

   #. Back on the **Client node**, if you wish reboot the Client, it is now safe to do so.

      .. code-block:: bash

         sudo reboot

#. Reboot the Control Node (optional)

  *If you wish reboot the nodes, it is now safe to do so.*

   .. code-block:: bash

      sudo reboot

**Congratulations!**

You've successfully installed and set up Kubernetes in |CL| using CRI-O and kata-runtime. You are now ready to follow on-screen instructions to deploy a pod network to the cluster and join worker nodes with the displayed token and IP information.

Clean up: Remove the migration bundle for each node

.. code-block:: bash

   sudo -E swupd bundle-remove k8s-migration

Related topics
**************

Read the Kubernetes documentation to learn more about:

*  `Kubernetes tutorial <tutorials/kubernetes>`_

*  `Kubernetes best practices <tutorials/kubernetes-bp>`_

*  Deploying Kubernetes with a `cloud-native-setup`_

* `Understanding basic Kubernetes architecture`_

* `Deploying an application to your cluster`_

* Installing a `pod network add-on`_

* `Joining your nodes`_


.. _kubeadm upgrade guide: https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade/

.. _Kubernetes container orchestration system: https://kubernetes.io/

.. _Understanding basic Kubernetes architecture: https://kubernetes.io/docs/user-journeys/users/application-developer/foundational/#section-3

.. _Deploying an application to your cluster: https://kubernetes.io/docs/user-journeys/users/application-developer/foundational/#section-2

.. _pod network add-on: https://kubernetes.io/docs/setup/independent/create-cluster-kubeadm/#pod-network

.. _Joining your nodes: https://kubernetes.io/docs/setup/independent/create-cluster-kubeadm/#join-nodes

.. _cloud-native-setup: https://github.com/clearlinux/cloud-native-setup/tree/master/clr-k8s-examples
