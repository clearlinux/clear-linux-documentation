.. _download-image:

Download, verify, and uncompress a Clear Linux image
####################################################

.. _types-of-cl-images:

Types of Clear Linux images
===========================

|CL| offers many types of `images`_ for different platforms and environments.

The naming convention of a |CL| image filename is: 

  .. code-block:: console
   
    clear-<version number>-<image type>.<compression type>

The *<version number>* field specifies the version number.

The *<image type>* field specifies the type of image and its corresponding file format.  The current list of images available are:

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

The *<compression type>* field specifies the compression type. Two types of 
compressions are used, namely GNU zip (*.gz*) and XZ (*.xz*).

.. _images: https://download.clearlinux.org/image

.. _verify-image-checksum:

Verify the integrity of the Clear Linux image
=============================================

Before using a downloaded |CL| image, it is recommended to verify its integrity
to eliminate the chance, albeit small, that it might be corrupted due to any 
download issues.  To support this, each released |CL| image is accompanied by an 
official SHA512 checksum file, which is designated with the suffix `-SHA512SUMS`.  

#.  Download the corresponding checksum file so it can be used to verify the 
    SHA512 checksum result of the downloaded image.  
#.  Verify the integrity of the image using these steps:

.. _verify-image-checksum-on-linux:

  *On Linux distros:*

  #.  Start a terminal emulator.
  #.  Go to the directory with the downloaded image and checksum files.
  #.  Verify the integrity of the image and compare it to its original checksum by entering:

      .. code-block:: console

        $ sha512sum ./clear-<version number>-<image type>.<compression type> | diff ./clear-<version number>-<image type>.<compression type>-SHA512SUMS -

      If the checksum of the downloaded image is different than the original
      checksum, the differences will displayed. Otherwise, an empty output indicates a match.

.. _verify-image-checksum-on-macos:

  *On macOS:*

  #.  Start Terminal app.
  #.  Go to the directory with the downloaded image and checksum files.
  #.  Verify the integrity of the image and compare it to its original checksum by entering:

      .. code-block:: console

        $ shasum -a512 ./clear-<version number>-<image type>.<compression type> | diff ./clear-<version number>-<image type>.<compression type>-SHA512SUMS -

      If the checksum of the downloaded image is different than the original
      checksum, the differences will displayed. Otherwise, an empty output indicates a match.

.. _verify-image-checksum-on-windows:

  *On Windows:*

  #.  Start Command-Prompt.
  #.  Go to the directory with the downloaded image and checksum files.
  #.  Get the SHA512 checksum of the image by entering: 

      .. code-block:: console

        C:\> CertUtil -hashfile ./clear-<version number>-<image type>.<compression type> sha512

  #.  Manually compare the output with the original checksum value shown in 
      the downloaded checksum file and make sure they match.

.. _uncompress-image:

Uncompress the Clear Linux image
================================

All released |CL| images are compressed by default.  Two types of 
compressions are used, namely GNU zip (`.gz`) and XZ (`.xz`).  

Uncompress the image using these steps:

.. _uncompress-image-on-linux:

*On Linux distros:*

#.  Start a terminal emulator.
#.  Go to the directory with the downloaded image.

.. _uncompress-xz-on-linux:

  To uncompress an XZ image, enter:

    .. code-block:: console

      $ unxz clear-<version number>-<image type>.xz

.. _uncompress-gz-on-linux:

  To uncompress a GZ image, enter:

    .. code-block:: console

      $ gunzip clear-<version number>-<image type>.gz

.. _uncompress-image-on-mac:

*On macOS:*

#.  Start Terminal app.
#.  Go to the directory with the downloaded image.

.. _uncompress-xz-on-mac:

  To uncompress an XZ image, enter:

    .. code-block:: console

      $ gunzip clear-<version number>-<image type>.xz

.. _uncompress-gz-on-mac:

  To uncompress a GZ image, enter:

      $ gunzip clear-<version number>-<image type>.gz

.. _uncompress-image-on-windows:

*On Windows:*

#. Download and install `7zip`_.
#. Locate the |CL| image and right-click it.
#. From the pop-up menu, select :guilabel:`7-Zip` and select :guilabel:`Extract here`.

  .. figure:: figures/7zipwin.png
    :scale: 80 %
    :alt: 7-Zip extract file

  Figure 1: Windows - 7-Zip extract file

.. _7zip: http://www.7-zip.org/