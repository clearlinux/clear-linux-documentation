.. _types-of-cl-images:

Types of Clear Linux images
###########################

|CL| offers many types of `images`_ for different platforms and environments.

The naming convention of a |CL| image filename is: 

  .. code-block:: console
   
    clear-[version number]-[image type].[compression type]

The `[version number]` field specifies the version number.

The `[image type]` field specifies the type of image and its corresponding file 
format.  The current list of images available are:

.. list-table:: Table 1: Types of Clear Linux images
   :widths: 20, 60
   :header-rows: 1

   * - Image Type
     - Description
   * - azure.vhd
     - Image for Microsoft Azure
   * - azure-docker.vhd
     - Image with the Docker installed for Microsoft Azure
   * - azure-machine-learning.vhd
     - Image with the `machine-learning-basic` bundle installed for Microsoft Azure
   * - cloud.img
     - Image for cloud deployment such as OpenStack, etc.
   * - containers.img
     - An optimized image utilized by Clear Containers runtime
   * - hyperv.vhdx
     - Image for Microsoft HyperV
   * - hyperv-mini.vhdx
     - A minimal image with fewer bundles for Microsoft HyperV
   * - installer.img
     - An interactive installer image for installing Clear Linux
   * - installer.iso
     - An ISO of the interactive installer image for installing Clear Linux
   * - kvm.img
     - Image for booting in a simple VM with start_qemu.sh
   * - live.img
     - A live boot image of Clear Linux
   * - vmware.vmdk
     - Image for VMware

The `[compression type]` field specifies the compression type. Two types of 
compressions are used, namely GNU zip (`.gz`) and XZ (`.xz`).

.. _images: https://download.clearlinux.org/image
