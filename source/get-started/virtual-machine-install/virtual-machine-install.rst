.. _virtual-machine-install:

Install |CL-ATTR| in a virtual machine
######################################

When installing |CL-ATTR| in a VM, consider which kernel to use. This
document walks you through the available kernel options to help this
decision. At the end of this document, select the type of installation most
suitable to your use case.

Compatible kernels
******************

The |CL| provides the following Linux kernels with a respective
:ref:`bundle <bundles-about>` for VMs. Specific use cases these bundles serve
are provided along with links to their source code.

.. include:: ../../reference/compatible-kernels.rst
   :Start-after: vm-kernels:

Next steps
**********

Now that you have read about the |CL| compatible kernels, choose the
appropriate set of step-by-step instructions to proceed.

.. toctree::
   :maxdepth: 1

   gce
   kvm
   virtualbox-cl-installer
   vmware-esxi-install-cl
   vmware-esxi-preconfigured-cl-image
   vmw-player
   vmw-player-preconf
   hyper-v
   ../../guides/maintenance/increase-virtual-disk-size.rst
