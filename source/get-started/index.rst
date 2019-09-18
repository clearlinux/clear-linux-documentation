.. _get-started:

Get started
###########

The Get Started section guides you through the requirements and installation of
|CL-ATTR|. Follow these step-by-step intructions to get started with |CL|, fast.

Pre-install
***********

There are a couple of things to take care of before you install.

* :ref:`system-requirements`
* :ref:`compatibility-check`
* :ref:`bootable-usb`

When installing |CL-ATTR| in a VM, consider which kernel to use. 

* :ref:`Compatible VM kernels <vm-kernels>`

.. toctree::
   :maxdepth: 1
   :hidden:

   compatibility-check
   bootable-usb

Install
*******

.. toctree::
   :maxdepth: 1

   bare-metal-install-desktop
   bare-metal-install-server
   install-configfile

.. _virtual-machine-install:

Install in a virtual machine
****************************

.. toctree::
   :maxdepth: 1
   :glob:

   virtual-machine-install/*
   ../../guides/maintenance/increase-virtual-disk-size.rst

Deploy to the cloud
********************

.. toctree::
   :maxdepth: 1
   :glob:

   cloud-install/*