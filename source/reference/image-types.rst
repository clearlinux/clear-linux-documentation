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
  compression methods are used: GNU\* zip (*.gz*) and XZ (*.xz*).

.. _incl-image-filename-end:

Table 1 lists the currently available images that are platform independent.
Table 2 lists the currently available images that are platform specific.

.. list-table:: Table 1: Types of platform-independent |CL| images
   :widths: 15, 85
   :header-rows: 1

   * - Image Type
     - Description

   * - live-desktop.img or live-desktop.iso
     - Image for booting to GNOME\* desktop to preview or install the OS.

   * - live-server.img or live-server.iso
     - Image for booting to server command prompt to preview or install the OS.

.. list-table:: Table 2: Types of platform-specific |CL| images
   :widths: 15, 85
   :header-rows: 1

   * - Image Type
     - Description

   * - aws.img
     - Image suitable for use with Amazon\* AWS\*.

   * - cloudguest.img
     - Image with generic cloud guest virtual machine (VM) requirements
       installed.

   * - gce.tar
     - Image with the Google Compute Engine (GCE) specific kernel.

   * - azure-hyperv.vhd
     - Image for Microsoft* Azure and Hyper-V generation 1 VMs. Includes
       :ref:`optimized kernel <vm-kernels>` for Hyper-V.

   * - kvm.img
     - Image for booting in a simple VM with start_qemu.sh. Includes
       :ref:`optimized kernel <vm-kernels>` for KVM.

   * - kvm-legacy.img
     - Image for booting in a simple VM using legacy BIOS, if using
       start_qemu.sh make sure to remove -bios parameter.

   * - pxe.tar
     - Image suitable for use with PXE server.

   * - vmware.vmdk
     - Virtual Machine Disk for VMware\* platforms including Player,
       Workstation, and ESXi.

.. _images: https://clearlinux.org/downloads
