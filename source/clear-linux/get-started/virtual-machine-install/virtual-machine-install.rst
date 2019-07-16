.. _virtual-machine-install:

Install |CL-ATTR| in a virtual machine
######################################

This page explains the available kernel options to help you decide which
kernel to use when installing |CL-ATTR| in a VM.

.. contents::
   :local:
   :depth: 1

Compatible kernels
******************

The |CL| provides the following Linux kernels with a respective
:ref:`bundle <bundles-about>` for VMs. Specific use cases these bundles serve
are provided along with links to their source code.

.. include:: ../../reference/compatible-kernels.rst
   :Start-after: vm-kernels:

Next steps
**********

After making a kernel selection, install using the appropriate set of
installation instructions for your kernel selection.

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
