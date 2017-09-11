.. _bdl-kvm-host:

kvm-host
########

This bundle provides the software needed to run virtual machines.

QEMU
====

|CL| provides :abbr:`QEMU (Quick Emulator)` to perform hardware virtualization.
When possible, qemu would be used together with
:abbr:`KVM (Kernel-based Virtual Machine)` in order to run virtual machines at
near-native speed.

For more information about how to use qemu, please refer to `qemu.org`_

virsh
=====

|CL| provides the virsh program to manage `libvirt`_ guests and the hypervisor.
libvirtd management daemon is not enabled nor started by default. To enable
the hypervisor, perform the following commands as root.

#. Enable the service to start every time the machine boots.
   This step is optional

   .. code-block:: console

      # systemctl enable libvirtd.service

#. Start the libvirtd management daemon service

   .. code-block:: console

      # systemctl start libvirtd.service

Congratulations! The libvirtd management daemon is running and virsh is ready
to be used.

.. _qemu.org: http://www.qemu.org/
.. _libvirt: http://libvirt.org/
