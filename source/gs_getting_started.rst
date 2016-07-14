.. _gs_getting_started:

Getting started
###############

There are a number of options available for downloading and running Clear Linux*
OS for Intel® Architecture. You can check your system hardware capabilities against
the list of `supported processors`_; alternatively, download and run the
`clear-linux-check-config`_ script to check the hardware compatibility of your
system from the command line.


Virtual machine installer images
================================

To test whether your host contains the necessary components to run the OS in
a container, download the `clear-linux-check-config`_ script and run::

   $ ./clear-linux-check-config.sh container

* **KVM Image** -- Download a recent KVM image, along with the UEFI firmware helper,
  ``OVMF.fd`` and the KVM start helper script ``start_qemu.sh.`` Find the
  ``clear-[version_number]-kvm.img.xz`` image in the `current`_ directory and see
  :ref:`vm-kvm` for further detail.

* **Container Evaluation** -- Intel® Clear Containers for Docker* Engine is available for
  numerous operating systems. This allows you to execute existing Docker applications in
  the secure and fast Intel Clear Containers environment. Find the
  ``clear-[version_number]-containers.img.xz`` in the `current`_ directory and see
  :ref:`gs-clear-containers-gettting-started` for more information.


Bare metal installer images
===========================

To test whether your system contains the necessary components to run the OS natively,
download the `clear-linux-check-config`_ script and run::

   $ ./clear-linux-check-config.sh host


* **Installer Image** -- The installer image allows you to manipulate and target
  partitions, and to set other OS configuration features (hostname, administrative user)
  commonly found in Linux installers. Find the ``clear-[version_number]-installer.img.xz``
  in our `current`_ directory and see :ref:`gs_installing_clr_as_host`. This `blog post`_
  contains more detail about the evolution of our installer.

* **Provisioning Image** -- This image is intended to be used in a provioning environment.
  Find the ``clear-[version_number]-provision.img.xz`` image in our `current`_ directory.
  *Warning*: This installer re-partitions ``/dev/sda`` and installs the OS to the new
  partition. Don't use this image on a system where you care about existing data on
  ``/dev/sda``.


Other installation options
==========================

* **Live Image** -- The live image can be used to boot the OS in a VM, or you can lay
  the image down on a USB drive with a tool like ``dd`` and boot from USB.

  This option is a great way to kick the tires with a minimal amount of effort.  Be
  aware, however, that if you do **not** manually configure the install and instead use
  the auto-install, it will repartition ``/dev/sda``.  This image also enables telemetry
  by default; see the `telemetry`_ feature page for more details.

  To select this option, download the ``clear-[version_number]-live.img.xz`` image in
  the `current`_ version's download directory.

For older versions, see our `releases`_ page.

.. _clear-linux-check-config: http://download.clearlinux.org/current/clear-linux-check-config.sh
.. _current: http://download.clearlinux.org/current
.. _blog post: https://clearlinux.org/blogs/clear-linux-installer-v20
.. _telemetry: https://clearlinux.org/features/telemetry
.. _supported processors: http://clearlinux.org/documentation/gs_supported_hardware.html
.. _releases: https://download.clearlinux.org/releases