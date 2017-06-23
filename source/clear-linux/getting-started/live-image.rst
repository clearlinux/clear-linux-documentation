.. _live-image-gs:

Live Image Installation
#######################

The live image can be used to boot the OS in a VM, or you
can lay the image down on a USB drive with a tool like ``dd`` and boot from
USB.

This option is a great way to kick the tires with a minimal amount of
effort. Be aware, however, that if you do **not** manually configure the
install and instead use the auto-install, it will repartition ``/dev/sda``.
This image also enables telemetry by default; see the `telemetry`_ feature
page for more details.

To select this option, download the ``clear-[version_number]-live.img.xz``
image in the `current`_ version's download directory.

For older versions, see our `releases`_ page.

.. _telemetry: https://clearlinux.org/features/telemetry
.. _releases: https://download.clearlinux.org/releases
.. _current: http://download.clearlinux.org/current