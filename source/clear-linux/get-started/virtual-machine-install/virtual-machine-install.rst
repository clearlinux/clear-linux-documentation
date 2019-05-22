.. _virtual-machine-install:

Install |CL-ATTR| in a virtual machine
######################################

There are some considerations to make when installing |CL-ATTR| in a VM.
First, you need to decide which kernel to use. This document
will walk you through the available kernel options to help this decision. At
the end of this document, you will be able to select the set of installation
steps most suitable to you and install |CL| under a VM.

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

   kvm
   virtualbox-cl-installer
   vmware-esxi-install-cl
   vmware-esxi-preconfigured-cl-image
   vmw-player
   vmw-player-preconf
   hyper-v
   ../../guides/maintenance/increase-virtual-disk-size.rst
   gce
