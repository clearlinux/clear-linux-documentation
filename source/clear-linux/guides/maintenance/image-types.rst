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
     - Virtual Hard Disk for use on Microsoft\* Azure\* cloud platform

   * - azure-docker.vhd
     - Virtual Hard Disk for use on Microsoft\* Azure\* cloud platform with Docker\* pre-installed

   * - azure-machine-learning.vhd
     - Virtual Hard Disk for use on Microsoft\* Azure\* cloud platform with the `machine-learning-basic` bundle installed

   * - cloud.img
     - Image for use by cloud deployments such as OpenStack\*

   * - containers.img
     - Image for use by Clear Containers runtime. Includes `optimized kernel`_ for Clear Containers.

   * - hyperv.vhdx
     - Virtual Hard Disk for use with Microsoft Hyper-V\* hypervisor. Includes `optimized kernel`_ for Hyper-V.

   * - installer.img 
     - Preferred image of Clear Linux with interactive installer. 

   * - installer.iso
     - ISO of Clear Linux with interactive installer. Only for special cases where ISO image format is required (not for use with a USB key)

   * - kvm.img
     - Image for booting in a simple VM with start_qemu.sh. Includes `optimized kernel`_ for KVM.

   * - live.img
     - image for live booting into memory, without requiring installaton. 

   * - vmware.vmdk
     - Virtual Machine Disk for VMware\* platforms inclduing Player, Workstation, and ESXi.

.. _images: https://download.clearlinux.org/image
.. _`optimized kernel`: https://clearlinux.org/documentation/clear-linux/reference/compatible-kernels

