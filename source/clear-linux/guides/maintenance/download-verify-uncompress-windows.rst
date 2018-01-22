.. _download-verify-uncompress-windows:

Download, verify, and uncompress a Clear Linux image on Windows
###############################################################

This section explains the types of |CLOSIA| images available, where to download
them, how to verify the integrity of an image, and how to uncompress it.

We also provide instructions for other operating systems:

* :ref:`download-verify-uncompress-linux`
* :ref:`download-verify-uncompress-mac`

.. include:: image-types.rst
   :start-after: image-types-content:

.. _verify-windows:

Verify the integrity of the Clear Linux image
*********************************************

Before you use a downloaded |CL| image, verify its integrity. Thus, you 
eliminate the small chance of a corrupted image due to download issues.
To support verification, we accompany each released |CL| image with an official 
SHA512 checksum file, which is designated with the suffix `-SHA512SUMS`.  

#.  Download the official corresponding SHA512 checksum file of your
    downloaded |CL| image.
#.  Start Command-Prompt.
#.  Go to the directory with the downloaded image and checksum files.
#.  Get the SHA512 checksum of the image by entering:

    .. code-block:: console

        C:\> CertUtil -hashfile ./clear-[version number]-[image type].[compression type] sha512

#.  Manually compare the output with the original checksum value shown in
    the downloaded checksum file and make sure they match.

Uncompress the Clear Linux image
********************************

We compress all released |CL| images by default with either GNU zip 
(`.gz`) or XZ (`.xz`). The compression type we use depends on the target 
platform or environment of the image. To uncompress the image, follow these steps:

#. Download and install `7zip`_.
#. Locate the |CL| image and right-click it.
#. From the pop-up menu, select :guilabel:`7-Zip` and select
   :guilabel:`Extract here`.

   .. figure:: figures/download-verify-uncompress-windows-fig-1.png
      :scale: 80 %
      :alt: 7-Zip extract file

      Figure 1: Windows - 7-Zip extract file

.. _7zip: http://www.7-zip.org/
