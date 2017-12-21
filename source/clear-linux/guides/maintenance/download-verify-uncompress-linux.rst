.. _download-verify-uncompress-linux:

Download, verify, and uncompress a Clear Linux image on Linux
#############################################################

This section explains the types of |CLOSIA| images available, where to download
them, how to verify the integrity of an image, and how to uncompress it.

Alternative instructions for other operating systems are available:

* :ref:`download-verify-uncompress-mac`
* :ref:`download-verify-uncompress-windows`

.. include:: types-of-cl-images.rst
  :start-after: types-of-cl-images:

Download the latest Clear Linux image
*************************************

Go to the Clear Linux `image`_ repository and download the image you want to use.  

.. _verify-image-checksum-on-linux:

Verify the integrity of the Clear Linux image on Linux
******************************************************

Before you use a downloaded |CL| image, verify its integrity. Thus, you 
eliminate the small chance of a corrupted image due to download issues.
To support verification, we accompany each released |CL| image with an official 
SHA512 checksum file, which is designated with the suffix `-SHA512SUMS`.  

#.  Download the official corresponding SHA512 checksum file of your downloaded |CL| image.  
#.  Start a terminal emulator.
#.  Go to the directory with the downloaded image and checksum files.
#.  Verify the integrity of the image and compare it to its original checksum by entering:

    .. code-block:: console

      $ sha512sum ./clear-[version number]-[image type].[compression type] | diff ./clear-[version number]-[image type].[compression type]-SHA512SUMS -

If the checksum of the downloaded image is different than the original
checksum, the differences will displayed. Otherwise, an empty output indicates 
a match and your downloaded image is good.

.. _uncompress-image-on-linux:

Uncompress the Clear Linux image on Linux
*****************************************

We compress all released |CL| images by default with either GNU zip 
(`.gz`) or XZ (`.xz`). The compression type we use depends on the target 
platform or environment of the image. To uncompress the image, follow these steps:

#.  Start a terminal emulator.
#.  Go to the directory with the downloaded image.

.. _uncompress-xz-on-linux:

  To uncompress an XZ image, enter:

    .. code-block:: console

      $ unxz clear-[version number]-[image type].xz

.. _uncompress-gz-on-linux:

  To uncompress a GZ image, enter:

    .. code-block:: console

      $ gunzip clear-[version number]-[image type].gz

.. _image: https://download.clearlinux.org/image
