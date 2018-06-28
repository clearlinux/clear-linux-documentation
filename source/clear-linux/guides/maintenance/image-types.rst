.. _image-types:

Clear Linux image types
#######################

.. _image-types-content:

|CLOSIA| offers many types of `images`_ for different platforms and environments.

The naming convention of a |CL| image filename is:

  .. code-block:: console

      clear-[version number]-[image type].[compression type]

The *[version number]* field specifies the version number.

The *[image type]* field specifies the type of image and its corresponding
file format.

The *[compression type]* field specifies the compression type. Two types of
compressions are used: GNU\* zip (*.gz*) and XZ (*.xz*).

Table 1 lists the currently available images.

.. list-table:: Table 1: Types of Clear Linux images
   :widths: 20, 60
   :header-rows: 1

   * - Image Type
     - Description
   * - azure.vhd
     - Image for Microsoft\* Azure\*
   * - azure-docker.vhd
     - Image with Docker\* installed for Microsoft Azure
   * - azure-machine-learning.vhd
     - Image with the `machine-learning-basic` bundle installed for Microsoft
       Azure
   * - cloud.img
     - Image for cloud deployment such as OpenStack\*
   * - containers.img
     - Optimized image used by Clear Containers runtime
   * - hyperv.vhdx
     - Image for Microsoft Hyper-V\*
   * - installer.img 
     - Preferred interactive installer image
   * - installer.iso
     - ISO of the interactive installer image. Only on special cases where ISO image format is required (not for use with a USB key)
   * - kvm.img
     - Image for booting in a simple VM with start_qemu.sh
   * - live.img
     - Live boot image
   * - vmware.vmdk
     - Image for VMware\*

.. _images: https://download.clearlinux.org/image
