.. _gs_getting_started:

Getting started with Clear Linux* OS for Intel® Architecture
############################################################

**Note:** To improve quality, the Telemetry service is enabled by default. See the `Telemetry feature page <https://clearlinux.org/features/telemetry>`_ for more details. Use the ``telemctl`` command to manage this service.

There are a number of ways to download and run Clear Linux OS for Intel Architecture. 
All of the images are in our `image directory <http://download.clearlinux.org/image/>`_. 

KVM Image
=========

Download a recent KVM image along with the UEFI firmware
helper ``OVMF.fd`` and the KVM start helper script ``start_qemu.sh.`` 
See :ref:`gs_running_clr_virtual` for details.

Live Image
==========
With the live image you can boot right into Clear in a VM, or you can lay the image down 
on a USB drive with a tool like ``dd`` and boot from USB. This is a great 
way to kick the tires with a minimal amount of effort. 

Installer Image
===============
The installer image allows you to manipulate and target partitions, and to set 
other OS configuration features (hostname, administrative user) commonly found in 
Linux Installers. See :ref:`gs_installing_clr_as_host` on a target computer for more information.

**CAUTION** If you do not manually configure the install and 
instead use the auto-install, it will repartition ``/dev/sda``. 

Provisioning Image
==================
**CAUTION:** This image is intended to be used in a provioning environment. The installer will 
repartition ``/dev/sda`` and install Clear Linux OS for Intel Architecture into the new 
partition. Don't use this on a system where you care about the data on ``/dev/sda``.

Container Evaluation
====================
Clear Containers for Docker* Engine is now available on multiple
operating systems. This enables executing existing Docker applications
in the secure and fast Clear Containers environment. 
See :ref:`gs-clear-containers-gettting-started` for details.

