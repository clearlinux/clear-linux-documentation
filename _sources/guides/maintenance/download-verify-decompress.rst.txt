.. _download-verify-decompress:

Download, verify, and decompress a |CL-ATTR| image
##################################################

This guide describes the available types of |CL| images, where to
download them, how to verify their integrity, and how to decompress them.
Follow the steps for your OS.

.. contents::
   :local:
   :depth: 1


.. include:: ../../reference/image-types.rst
   :start-after: image-types-content:
   :end-before: incl-image-filename-end:

.. _download-verify-decompress-linux:

Linux OS steps
**************

.. _verify-linux:

Verify the integrity of the |CL| image
======================================

Before you use a downloaded |CL| image, verify its integrity. This action
eliminates the small chance of a corrupted image due to download issues. To
support verification, each released |CL| image has a corresponding SHA512
checksum file designated with the suffix `-SHA512SUMS`.

#.  Download the corresponding SHA512 checksum file of your |CL| `image`_.
#.  Open a Terminal.
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

.. incl-decompress-image:

Decompress the |CL| image
=========================

Released |CL| images are compressed with either GNU zip (*.gz*) or XZ
(*.xz*). The compression type depends on the target platform or
environment. To decompress the image, follow these steps:

#.  Open a Terminal.
#.  Go to the directory with the downloaded image.

    To decompress an XZ image, enter:

    .. code-block:: bash

        unxz clear-[version number]-[image type].xz

    To decompress a GZ image, enter:

    .. code-block:: bash

        gunzip clear-[version number]-[image type].gz

.. incl-decompress-image-end:

.. _download-verify-decompress-mac:

macOS\* steps
*************

.. _verify-mac:

Verify the integrity of the |CL| image
======================================

Before you use a downloaded |CL| image, verify its integrity. This action
eliminates the small chance of a corrupted image due to download issues. To
support verification, each released |CL| image has a corresponding SHA512
checksum file designated with the suffix `-SHA512SUMS`.

#. Download the corresponding SHA512 checksum file of your |CL| `image`_.
#. Open a Terminal.
#. Go to the directory with the downloaded image and checksum files.
#. Verify the integrity of the image and compare it to its original checksum
   with the command:

   .. code-block:: bash

      shasum -a512 clear-[version number]-[image type].[compression type] | diff clear-[version number]-[image type].[compression type]-SHA512SUMS -

If the checksum of the downloaded image is different than the original
checksum, the differences will be displayed. Otherwise, an empty output indicates
a match and your downloaded image is good.

Decompress the |CL| image
=========================

We compress all released |CL| images by default with either GNU zip
(`.gz`) or xz (`.xz`). The compression type we use depends on the target
platform or environment. To decompress the image, follow these steps:

#. Open a Terminal.
#. Go to the directory with the downloaded image.
#. Use the :command:`gunzip` command to decompress either compression type. For example:

   .. code-block:: bash

      gunzip clear-[version number]-[image type].xz
      gunzip clear-[version number]-[image type].gz

.. _download-verify-decompress-windows:

Windows\* OS steps
******************

.. _verify-windows:

Verify the integrity of the |CL| image
======================================

Before you use a downloaded |CL| image, verify its integrity. This action
eliminates the small chance of a corrupted image due to download issues. To
support verification, each released |CL| image has a corresponding SHA512
checksum file designated with the suffix `-SHA512SUMS`.

#.  Download the corresponding SHA512 checksum file of your |CL| `image`_.
#.  Start Command Prompt.
#.  Go to the directory with the downloaded image and checksum files.
#.  Get the SHA512 checksum of the image with the command:

    .. code-block:: bash

        CertUtil -hashfile ./clear-[version number]-[image type].[compression type] SHA512

#.  Manually compare the output with the original checksum value shown in
    the downloaded checksum file and make sure they match.

Decompress the |CL| image
=========================

Released |CL| images are compressed with either GNU zip (*.gz*) or XZ
(*.xz*). The compression type depends on the target platform or
environment. To decompress the image, follow these steps:

#. Download and install `7-Zip`_.
#. Go to the directory with the downloaded image and right-click it.
#. From the pop-up menu, select :guilabel:`7-Zip` and select
   :guilabel:`Extract Here` as shown in Figure 1.

   .. figure:: figures/download-verify-decompress-windows-fig-1.png
      :scale: 80 %
      :alt: 7-Zip extract file

      Figure 1: Windows 7-Zip extract file.

.. _7-Zip: http://www.7-zip.org/

Image types
***********

.. include:: ../../reference/image-types.rst
   :start-after: incl-image-filename-end:

.. _image: https://clearlinux.org/downloads
