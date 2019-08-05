.. _kubernetes-bp:

Kubernetes\* Best Practices
###########################

Use swupd to update clusters
****************************

This tutorial shows you how to manage your Kubernetes cluster while using
:command:`swupd` to update |CL-ATTR|.

In our tutorial :ref:`kubernetes`, we explain how to set up a Kubernetes
cluster on |CL| using `kubeadm`. `Kubeadm documentation`_ often builds on the
assumption that the distribution uses a traditional package manager (e.g.,
RPM/DEB).

In contrast, |CL| uses `swupd` to update the OS, which in this case updates
all of the kubernetes node and client binaries simultaneously, as part of
the `cloud-native-basic` bundle (e.g., kubectl, kubeadm, kubelet). Running
:command:`sudo swupd update` requires special care to ensure the OS
incorporates the latest Kubernetes upgrades.

This document describes best practices to manage cluster upgrades with
`kubeadm` on a |CL|-based cluster.

Prerequisites
*************

Assure that you:

* Completed :ref:`kubernetes`
* Installed the bundle `cloud-native-basic`

.. note::

   Other Linux\* distros shown in Kubernetes upgrade documentation reflect
   `apt-get update`, `apt-mark hold kubeadm`, and similar commands; however, such commands **are not valid** on |CL|.

Update the control plane
************************

#. Read kubernetes documentation `before you begin`_.

#. On your master node, run the command:

   .. code-block:: bash

      sudo swupd update

   .. note::

      If the minor version of Kubernetes changes, |CL| shows a message-of-the-day, or `motd`. When the `motd` appears, you **must postpone** a kubelet restart on master and nodes until the control plane is properly updated. :command:`swupd update` does not restart services automatically unless explicitly configured to do so.

#. Now follow these instructions in kubernetes documentation.

   * `Upgrade control plane`_
   * `Drain control plane node`_
   * `Restart Kubelet and undrain node`_

Update worker nodes
*******************

#. On each worker node, run the command:

   .. code-block:: bash

      sudo swupd update

#. Now follow these instructions in kubernetes documentation:

   * `Drain node`_
   * `Update kubelet configuration`_
   * `Restart Kubelet and undrain node`_

.. _Kubeadm documentation: https://kubernetes.io/docs/reference/setup-tools/kubeadm/kubeadm-upgrade/

.. _Restart Kubelet and undrain node: https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade-1-13/#restart-the-kubelet-for-all-nodes

.. _Update kubelet configuration: https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade-1-13/#upgrade-the-kubelet-config-on-worker-nodes

.. _Drain node: https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade-1-13/#drain-control-plane-and-worker-nodes

 .. _Restart kubelet and undrain node: https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade-1-13/#restart-the-kubelet-for-all-nodes

.. _Upgrade control plane: https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade-1-13/#upgrade-the-control-plane-node

.. _Drain control plane node: https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade-1-13/#drain-control-plane-and-worker-nodes

.. _Kubeadmn documentation: https://kubernetes.io/docs/reference/setup-tools/kubeadm/kubeadm/

.. _before you begin: https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade-1-13/#before-you-begin

