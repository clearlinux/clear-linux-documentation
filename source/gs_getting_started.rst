.. _gs_getting_started:

Getting started
###############

There are a number of options available for downloading and running Clear Linux*
OS for Intel® Architecture. Be sure to check your system hardware capabilities
against our list of `supported processors`_; alternatively, you can download and
run the `clear-linux-check-config`_ script to check the hardware compatibility of
your system from the command line.

Once you're ready to download an image, you can choose from these options:


KVM Image
=========
Download a recent KVM image along with the UEFI firmware helper ``OVMF.fd`` and
the KVM start helper script ``start_qemu.sh.`` See :ref:`vm-kvm` for details. Find
the ``clear-[version_number]-kvm.img.xz`` image in our `current`_ directory.


Installer Image
===============
The installer image allows you to manipulate and target partitions, and to set other
OS configuration features (hostname, administrative user) commonly found in Linux
installers. Find the ``clear-[version_number]-installer.img.xz`` in our `current`_
directory and see :ref:`gs_installing_clr_as_host` for more information.


Live Image
==========
With the live image you can boot right into Clear in a VM, or you can lay the image
down on a USB drive with a tool like ``dd`` and boot from USB. This is a great way
to kick the tires with a minimal amount of effort. Find the ``clear-[version_number]
-live.img.xz`` image in our `current`_ directory. **Warning** -- if you do not manually
configure the install and instead use the auto-install, it  will repartition ``/dev/sda``.

.. tip::
   To improve quality, the telemetry service is enabled by default. See the `Telemetry`
   feature page for more details. Use the ``telemctl`` command to manage this service.


Provisioning Image
==================
This image is intended to be used in a provioning environment. Find the
``clear-[version_number]-provision.img.xz`` image in our `current`_ directory.

.. warning::
   This installer repartitions ``/dev/sda`` and installs Clear Linux OS for Intel
   Architecture into the new partition. Don't use this image on a system where you
   care about existing data on ``/dev/sda``.


Container Evaluation
====================
Clear Containers for Docker* Engine is now available on multiple operating
systems. This enables executing existing Docker applications in the secure and
fast Clear Containers environment. Find the ``clear-[version_number]-containers.img.xz``
and see :ref:`gs-clear-containers-gettting-started` for further detail.

For older versions, see our `releases <https://download.clearlinux.org/releases>`_ page.

.. _clear-linux-check-config: http://download.clearlinux.org/current/clear-linux-check-config.sh
.. _current: http://download.clearlinux.org/current
.. _telemetry: https://clearlinux.org/features/telemetry
.. _supported processors: http://clearlinux.org/documentation/gs_supported_hardware.html
