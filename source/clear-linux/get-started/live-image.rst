.. _live-image:

Install Clear Linux as a live image
###################################

A live image contains the complete |CLOSIA| operating system and resides
on a bootable media such as a USB drive or in a virtual machine
(see :ref:`virtual-machine-install`). This is a
great way to use |CL| without modifying your computer's hard disk.

To create a bootable USB drive with a live image, follow
:ref:`our step-by-step instructions<bootable-usb>` and use the latest |CL|
live image from the `image`_ directory. Look for the
:file:`clear-[version number]-live.img.xz` file.

.. _boot-live-image:

Boot the Clear Linux live image
*******************************

#. Configure the BIOS/UEFI firmware settings of the target system:

   * Enable `Intel® Virtualization Technology (Intel® VT)`_.
   * Enable `Intel® Virtualization Technology for Directed I/O (Intel® VT-d)`_.
   * Disable `Secure Boot`.

#. Plug the imaged USB drive in and boot it up.
#. Log in as `root` and set a password.
   
.. _create and enable user space: https://clearlinux.org/documentation/clear-linux/guides/maintenance/enable-user-space 

.. _`image`: https://download.clearlinux.org/image

.. _`Intel® Virtualization Technology (Intel® VT)`: http://www.intel.com/content/www/us/en/virtualization/virtualization-technology/intel-virtualization-technology.html

.. _`Intel® Virtualization Technology for Directed I/O (Intel® VT-d)`: https://software.intel.com/en-us/articles/intel-virtualization-technology-for-directed-io-vt-d-enhancing-intel-platforms-for-efficient-virtualization-of-io-devices>`

