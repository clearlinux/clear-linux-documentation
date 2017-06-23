.. _live-image:

Live Image Installation
#######################

This option is a great way to try a live |CL| environment without writing
to your computer's hard disk.

The live image can be used to boot the OS in a VM, or you
can create a bootable USB drive and boot from USB. 

Be aware, however, that if you do **not** manually configure the install and
instead use the auto-install, it will repartition ``/dev/sda``.
This image also enables telemetry by default; see the `telemetry`_ feature
page for more details.

Download the latest Clear Linux Live Image
------------------------------------------

Download the ``clear-[version_number]-live.img.xz``
image in the `current`_ version's download directory.

For older versions, see our `releases`_ page.

.. include:: bare-metal-install/bare-metal-install.rst
   :Start-after: create-usb:
   :end-before: download-clear-linux-image

This example uses release 10980 so we will download the
:file:`clear-10980-installer.img.xz` image file.

.. include:: bare-metal-install/bare-metal-install.rst
   :Start-after: copy-image:
   :end-before: install-on-target

**Congratulations!**

You are now ready to boot from USB and kick the tires on your live |CL|
environment.

.. _telemetry: https://clearlinux.org/features/telemetry
.. _releases: https://download.clearlinux.org/releases
.. _current: http://download.clearlinux.org/current
