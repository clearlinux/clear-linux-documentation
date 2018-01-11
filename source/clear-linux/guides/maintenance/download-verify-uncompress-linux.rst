.. _download-verify-uncompress-linux:

Download, verify, and uncompress a Clear Linux image on Linux
#############################################################

This section explains the types of |CLOSIA| images available, where to download
them, how to verify the integrity of an image, and how to uncompress it.

We also provide instructions for other operating systems:

* :ref:`download-verify-uncompress-mac`
* :ref:`download-verify-uncompress-windows`

.. include:: image-types.rst
   :start-after: image-types-content:

.. _verify-linux:

Verify the integrity of the Clear Linux image
*********************************************

Before you use a downloaded |CL| image, verify its integrity. Thus, you 
eliminate the small chance of a corrupted image due to download issues.
To support verification, we accompany each released |CL| image with an official 
SHA512 checksum file, which is designated with the suffix `-SHA512SUMS`.  

#.  Download the official corresponding SHA512 checksum file of your
    downloaded |CL| image.
#.  Start a terminal emulator.
#.  Go to the directory with the downloaded image and checksum files.
#.  Verify the integrity of the image and compare it to its original checksum
    by entering:

   .. code-block:: console

      $ sha512sum ./clear-[version number]-[image type].[compression type] | diff ./clear-[version number]-[image type].[compression type]-SHA512SUMS -

If the checksum of the downloaded image is different than the original
checksum, the differences will displayed. Otherwise, an empty output indicates
a match and your downloaded image is good.

Uncompress the Clear Linux image
********************************

We compress all released |CL| images by default with either GNU zip 
(`.gz`) or XZ (`.xz`). The compression type we use depends on the target 
platform or environment of the image. To uncompress the image, follow these steps:

#.  Start a terminal emulator.
#.  Go to the directory with the downloaded image.

   To uncompress an XZ image, enter:

      .. code-block:: console

         $ unxz clear-[version number]-[image type].xz

   To uncompress a GZ image, enter:

       .. code-block:: console

         $ gunzip clear-[version number]-[image type].gz
