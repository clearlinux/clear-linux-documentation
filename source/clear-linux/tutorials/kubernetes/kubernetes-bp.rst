.. _kubernetes-bp:

Kubernetes Best Practices on |CL|
#################################

Update Kubernetes clusters
**************************

This tutorial shows you how to manage your Kubernetes cluster while using
:command:`swupd` to update |CL-ATTR|.

In our tutorial :ref:`kubernetes`, we explain how to set up a Kubernetes
cluster on |CL| using `kubeadm`. `Kubeadm documentation`_ often builds on the
assumption that the distribution uses a traditional package manager (e.g.,
RPM/DEB). In contrast, |CL| manages packages in bundles. This document
describes best practices to manage cluster upgrades with kubeadm on a |CL|-based cluster.

Prerequisites
*************

Let's review some basic assumptions:

* |CL| includes Kubernetes support with the `cloud-native-basic` bundle.

* Ensure `autoupdate` is enabled. See :ref:`swupd-guide`.
  To enable, run:

  .. code-block:: bash

     sudo swupd autoupdate

* Execute :command:`sudo swupd update` **on each node** to do the update.

* Repeat the above command for both master and worker nodes.

Executing this command updates all of the kubernetes node and client
binaries simultaneously, which are part of `cloud-native-basic` bundle
(including kubectl, kubeadm, kubelet).

.. note::

   Other Linux\* distros shown in Kubernetes upgrade documentation reflect
   `apt-get update`, `apt-mark hold kubeadm`, and similar commands; however, such commands **aren not valid** on |CL|.


Update the cluster
******************
#. Read kubernetes documentation `before you begin`_.

#. On your master node, run the command:

   .. code-block:: bash

      sudo swupd update

#. Run this command to check the message-of-the-day, or `motd`:

   .. code-block:: bash

      cat /run/motd

.. TODO: As of 01/29/19 the motd is only available if the k8s minor version changes. Under consideration that the motd will ALWAYS show when k8s changes.

#. If the 'motd' indicates a change...., follow instructions below to update.

   .. note::

      Do not restart the kubelet before the control plane is updated.

      If the `motd` appears, a kubelet restart on master and nodes
      **must be postponed** until the control plane is properly updated.
      :command:`swupd update` does not restart services automatically unless
      explicitly configured to do so.

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


.. _Restart Kubelet and undrain node: https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade-1-13/#restart-the-kubelet-for-all-nodes

.. _Update kubelet configuration: https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade-1-13/#upgrade-the-kubelet-config-on-worker-nodes

.. _Drain node: https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade-1-13/#drain-control-plane-and-worker-nodes

 .. _Restart kubelet and undrain node: https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade-1-13/#restart-the-kubelet-for-all-nodes

.. _Upgrade control plane: https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade-1-13/#upgrade-the-control-plane-node

.. _Drain control plane node: https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade-1-13/#drain-control-plane-and-worker-nodes

.. _Kubeadmn documentation: https://kubernetes.io/docs/reference/setup-tools/kubeadm/kubeadm/

.. _before you begin: https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade-1-13/#before-you-begin