.. _image-types:

|CL-ATTR| image types
#########################

.. _image-types-content:

|CL-ATTR| offers many types of `images`_ for different platforms and environments.

.. _incl-image-filename:

The naming convention of a |CL| image filename is:

.. code-block:: console

   clear-[version number]-[image type].[compression type]

* The *[version number]* field specifies the version number.

* The *[image type]* field specifies the type of image and its corresponding
  file format.

* The *[compression type]* field specifies the compression type. Two types of
  compressions are used: GNU\* zip (*.gz*) and XZ (*.xz*).

.. _incl-image-filename-end:

Table 1 lists the currently available images that are platform independent.
Table 2 lists the currently available images that are platform specific.

.. list-table:: Table 1: Types of platform-independent |CL| images
   :widths: 15, 85
   :header-rows: 1

   * - Image Type
     - Description

   * - installer.img
     - Preferred image of |CL| with interactive installer.

   * - installer.iso
     - ISO of |CL| with interactive installer. Only for special cases where ISO image format is required (not for use with a USB key)

   * - live.img
     - Image for live booting into memory, without requiring installaton.

.. list-table:: Table 2: Types of platform-specific |CL| images
   :widths: 15, 85
   :header-rows: 1

   * - Image Type
     - Description

   * - azure.vhd
     - Virtual Hard Disk for use on Microsoft\* Azure\* cloud platform

   * - azure-docker.vhd
     - Virtual Hard Disk for use on Microsoft Azure cloud platform with Docker\* pre-installed

   * - azure-machine-learning.vhd
     - Virtual Hard Disk for use on Microsoft Azure cloud platform with the `machine-learning-basic` bundle installed

   * - cloud.img
     - Image for use by cloud deployments such as OpenStack\*

   * - containers.img
     - Image for use by Clear Containers runtime. Includes `optimized kernel`_ for Clear Containers.

   * - hyperv.vhdx
     - Virtual Hard Disk for use with Microsoft Hyper-V\* hypervisor. Includes `optimized kernel`_ for Hyper-V.

   * - kvm.img
     - Image for booting in a simple VM with start_qemu.sh. Includes
       `optimized kernel`_ for KVM.

   * - vmware.vmdk
     - Virtual Machine Disk for VMware\* platforms inclduing Player, Workstation, and ESXi.

.. _images: https://download.clearlinux.org/image
.. _`optimized kernel`: https://clearlinux.org/documentation/clear-linux/reference/compatible-kernels

