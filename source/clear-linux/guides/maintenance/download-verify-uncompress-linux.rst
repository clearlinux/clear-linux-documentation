.. _download-verify-uncompress-linux:

Download, verify, and uncompress a Clear Linux image on Linux
#############################################################

This guide describes the types of |CLOSIA| images available, where to download
them, how to verify the integrity of an image, and how to uncompress it.

Instructions for other operating systems are available:

* :ref:`download-verify-uncompress-mac`
* :ref:`download-verify-uncompress-windows`

Image types
***********

.. include:: image-types.rst
   :start-after: image-types-content:

.. _verify-linux:

Verify the integrity of the Clear Linux image
*********************************************

Before you use a downloaded |CL| image, verify its integrity. This action
eliminates the small chance of a corrupted image due to download issues. To
support verification, each released |CL| image has a corresponding SHA512
checksum file designated with the suffix `-SHA512SUMS`.

#.  Download the corresponding SHA512 checksum file of your |CL| image.
#.  Start a terminal emulator.
#.  Go to the directory with the downloaded image and checksum files.
#.  Verify the integrity of the image and compare it to its original checksum
    with the command:

    .. code-block:: bash

        sha512sum -c ./clear-[version number]-[image type].[compression type]-SHA512SUMS

If the checksum of the downloaded image is different than the original
checksum, a warning is displayed with a message indicating the computed
checksum does **not** match. Otherwise, the name of the image is printed on
the screen followed by `OK`.

For a more in-depth discussion of image verification including checking the
certificate see :ref:`image-content-validation`.

Uncompress the Clear Linux image
********************************

Released |CL| images are compressed with either GNU zip (*.gz*) or XZ
(*.xz*). The compression type depends on the target platform or
environment. To uncompress the image, follow these steps:

#.  Start a terminal emulator.
#.  Go to the directory with the downloaded image.

    To uncompress an XZ image, enter:

    .. code-block:: bash

        unxz clear-[version number]-[image type].xz

    To uncompress a GZ image, enter:

    .. code-block:: bash

        gunzip clear-[version number]-[image type].gz
