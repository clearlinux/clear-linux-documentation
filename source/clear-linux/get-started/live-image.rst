.. _live-image:

Install Clear Linux as a live image
###################################

This option is a great way to try a live |CL| environment without writing
to your computer's hard disk.

Follow these instructions to create a bootable USB drive and boot from USB.
You can also use the live image to boot the OS in a VM.

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
