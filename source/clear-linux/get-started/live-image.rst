.. _live-image:

Install Clear Linux as a live image
###################################

A live image contains the complete |CLOSIA| operating system and resides
on a bootable media such as a USB drive or in a virtual machine
(see :ref:`virtual-machine-install`). This is a
great way to use |CL| without modifying your computer's hard disk.

.. include:: bootable-usb/bootable-usb-linux.rst
   :Start-after: bootable-usb-linux:
   :end-before: download-cl-image

.. include:: ../guides/maintenance/download-image.rst
   :Start-after: types-of-cl-images:
   :end-before: download-usb-suitable-images

.. Download the latest Clear Linux Live image
.. ******************************************

.. #. Get the latest |CL| Live image from the `image`_ page.  Look for
..   `clear-<version>-live.img.xz`.

..   For older versions, see the `releases`_ page.

Download the latest Clear Linux live image
==========================================

Get the latest |CL| installer image from the `image`_ directory.  
Look for **clear-<version number>-live.img.xz**.

.. _image: https://download.clearlinux.org/image

.. include:: ../guides/maintenance/download-image.rst
   :Start-after: verify-image-checksum:
   :end-before: verify-image-checksum-on-macos

.. #. Although not required, it is recommended to download the corresponding
..   checksum file (designated with `-SHA512SUMS` at the end of the filename) for
..   the image in order to verify its integrity.

.. include bootable-usb/bootable-usb-linux.rst
..   :Start-after: verify-checksum:
..   :end-before: verify-checksum-on-macos

.. include:: ../guides/maintenance/download-image.rst
   :Start-after: uncompress-image:
   :end-before: uncompress-gz-on-linux

.. include:: bootable-usb/bootable-usb-linux.rst
   :Start-after: copy-usb-linux:
   :end-before: usb-next

.. _boot-live-image:

Boot the Clear Linux Live image
*******************************

#. Configure the BIOS/UEFI firmware settings of the target system:
   
   * Enable `Intel® Virtualization Technology (Intel® VT)`_.
   * Enable `Intel® Virtualization Technology for Directed I/O (Intel® VT-d)`_.
   * Disable `Secure Boot`.
   
#.	Plug the imaged USB drive in and boot it up.
#. Log in as `root` and set a password.

.. _`releases`: https://download.clearlinux.org/releases
.. _`image`: https://download.clearlinux.org/image
.. _`Intel® Virtualization Technology (Intel® VT)`: http://www.intel.com/content/www/us/en/virtualization/virtualization-technology/intel-virtualization-technology.html
.. _`Intel® Virtualization Technology for Directed I/O (Intel® VT-d)`: https://software.intel.com/en-us/articles/intel-virtualization-technology-for-directed-io-vt-d-enhancing-intel-platforms-for-efficient-virtualization-of-io-devices>`

