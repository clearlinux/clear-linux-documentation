.. _live-image:

Install Clear Linux as a live image
###################################

A live image contains the complete Clear Linux operating system that resides on a bootable media such as a USB drive or in a virtual machine.  This is a great way to use |CL| without modifying your computer's existing hard disk.

Follow these instructions to create a bootable USB drive and boot from USB.  To boot |CL| in a virtual environment, see `Install Clear Linux in a virtual machine`_.

.. include:: bootable-usb/bootable-usb-linux.rst
   :Start-after: bootable-usb-linux:
   :end-before: download-cl-image

Download the latest Clear Linux Live Image
------------------------------------------

Download the ``clear-[version_number]-live.img.xz``
image in the `current`_ version's download directory.

For older versions, see our `releases`_ page.

.. include:: bootable-usb/bootable-usb-linux.rst
   :Start-after: copy-usb-linux:
   :end-before: usb-next

Boot your Clear Linux live image
================================

#. Plug the imaged USB drive into the target system and boot it up.

#. Log in as `root` and set a password.

.. _releases: https://download.clearlinux.org/releases
.. _current: http://download.clearlinux.org/current
.. _Install Clear Linux in a virtual machine: https://clearlinux.org/documentation/clear-linux/get-started/virtual-machine-install/virtual-machine-install.html
