.. _live-image:

Install Clear Linux as a live image
###################################

A live image contains the complete |CLOSIA| operating system and resides
on a bootable media such as a USB drive or in a virtual machine
(see :ref:`virtual-machine-install`). This is a
great way to use |CL| without modifying your computer's hard disk.

.. include:: bootable-usb/bootable-usb-linux.rst
   :Start-after: bootable-usb-linux:
   :end-before: end-bootable-usb-linux-intro

.. include:: ../guides/maintenance/types-of-cl-images.rst
  :start-after: types-of-cl-images:
  
Download the latest Clear Linux live image
******************************************

Get the latest |CL| live image from the `image`_ directory.  
Look for :file:`clear-[version number]-live.img.xz`.

.. include:: ../guides/maintenance/download-verify-uncompress-linux.rst
   :Start-after: verify-image-checksum-on-linux:
   :end-before: uncompress-image-on-linux

.. include:: ../guides/maintenance/download-verify-uncompress-linux.rst
   :Start-after: uncompress-image-on-linux:
   :end-before: uncompress-gz-on-linux

.. include:: bootable-usb/bootable-usb-linux.rst
   :Start-after: copy-usb-linux:
   :end-before: usb-next

.. _boot-live-image:

Boot the Clear Linux live image
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

