.. _installation-options:

Installation options
####################

You can check your system hardware
capabilities against the list of
:ref:`supported processors <supported-hardware>`; alternatively,
download and run the `clear-linux-check-config`_ script to check the hardware
compatibility of your system from the command line.


Virtualized images
==================

Images are also available to run under Virtual Machines or containers.

To test whether your host contains the necessary components to run the OS in
a container, download the `clear-linux-check-config`_ script and run::

   $ ./clear-linux-check-config.sh container

* **KVM Image** -- Download a recent KVM image, along with the UEFI firmware
  helper, ``OVMF.fd`` and the KVM start helper script ``start_qemu.sh.`` Find
  the ``clear-[version_number]-kvm.img.xz`` image in the `current`_ directory
  and see
  :ref:`kvm` for further detail.

* **Docker Image** -- A Clear Linux* Docker* image can be downloaded
  directly from the Docker hub and executed within the Docker environment.
  Details were posted in the blog post `Clear Linux Highlights 3`_, and
  on a Docker* enabled system you can execute::

    docker pull clearlinux
    docker run -it clearlinux

  and then follow the normal Clear Linux* instuctions to add bundles etc.


Bare metal installer images
===========================

To test whether your system contains the necessary components to run the OS
natively, download the `clear-linux-check-config`_ script and run::

   $ ./clear-linux-check-config.sh host


* **Installer Image** -- The installer image allows you to manipulate and
  target partitions, and to set other OS configuration features (hostname,
  administrative user) commonly found in Linux installers. Find the
  ``clear-[version_number]-installer.img.xz`` in our `current`_ directory and
  see :ref:`clear-host`. This `blog post`_ contains more detail
  about the evolution of our installer.

* **Provisioning Image** -- This image is intended to be used in a provioning
  environment. Find the ``clear-[version_number]-provision.img.xz`` image in
  our `current`_ directory. *Warning*: This installer repartitions
  ``/dev/sda`` and installs the OS to the new partition. Don't use this image
  on a system where you care about existing data on ``/dev/sda``.


Other installation options
==========================

* **Live Image** -- The live image can be used to boot the OS in a VM, or you
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

.. _clear-linux-check-config: http://download.clearlinux.org/current/clear-linux-check-config.sh
.. _current: http://download.clearlinux.org/current
.. _blog post: https://clearlinux.org/blogs/clear-linux-installer-v20
.. _Clear Linux Highlights 3: https://clearlinux.org/blogs/clear-linux-highlights-3
.. _telemetry: https://clearlinux.org/features/telemetry
.. _releases: https://download.clearlinux.org/releases
