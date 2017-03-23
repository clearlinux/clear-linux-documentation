.. _gs_clear-linux-kernels:

|CL| kernels
############

|CLOSIA| has several Linux kernels distributed over several bundles. This
`bundles`_ has specific use case which are explained below.

Kernel native
=============

This bundle is focuses in the bare metal platform. It is optimized for
fast boot, and best performance in Intel architecture as described in the
:ref:`gs_supported_hardware`. You can find the optimization patches 
in our `linux`_ GitHub* repo.

Kernel LTS
==========

This bundle is focuses in the bare metal platform and use the lattes
:abbr:`LTS (Long Term Support)` Linux kernel. It is optimized for
fast boot, and best performance in Intel architecture as described in the
:ref:`gs_supported_hardware`. Also it includes the VirtualBox* kernel
modules (see :ref:`vm-virtualbox`). You can find the optimization patches 
in our `linux-lts`_ GitHub* repo.

Kernel KVM
=============

This bundle is focuses on Linux :abbr:`KVM (Kernel-based Virtual Machine)`.
It is optimized for fast boot, and best performance in Virtual Machines
running on the :ref:`gs_supported_hardware`.
It is the preferred kernel when running |CL| as the guest OS
on top of *qemu/kvm* or through **cloud orchestrators** which
internally use *qemu/kvm* as the **hypervisor**.
Also it can be used as a
stand alone Linux VM (see :ref:`vm-kvm`). You can find the
optimization patches in our `linux-kvm`_ GitHub* repo.

Kernel Hyper-V*
===============

This bundle is focuses on running Linux on Microsoft* Hyper-V*.
It is optimized for fast boot, and best performance in Virtual Machines
running on the :ref:`gs_supported_hardware`.
It is the preferred kernel when running |CL| as the guest OS
from **Cloud Instances** in projects as Microsoft `Azure`_\*, and as a
stand alone Linux VM (see :ref:`vm-hyper-v`). You can find the
optimization patches in our `linux-hyperv`_ GitHub* repo.

Kernel Hyper-V* LTS
===================

This bundle is focuses on running Linux on Microsoft* Hyper-V* and use the
lattes :abbr:`LTS (Long Term Support)` Linux kernel.
It is optimized for fast boot, and best performance in Virtual Machines
running on the :ref:`gs_supported_hardware`.
It is the preferred kernel when running |CL| as the guest OS
from **Cloud Instances** in projects as Microsoft `Azure`_\*, and as a
stand alone Linux VM (see :ref:`vm-hyper-v`). You can find the
optimization patches in our `linux-hyperv-lts`_ GitHub* repo.

.. _linux: https://github.com/clearlinux-pkgs/linux
.. _linux-lts: https://github.com/clearlinux-pkgs/linux-lts
.. _linux-kvm: https://github.com/clearlinux-pkgs/linux-kvm
.. _linux-hyperv: https://github.com/clearlinux-pkgs/linux-hyperv
.. _linux-hyperv-lts: https://github.com/clearlinux-pkgs/linux-hyperv-lts
.. _bundles: https://github.com/clearlinux/clr-bundles
.. _CIAO: https://github.com/01org/ciao
.. _Azure: https://azuremarketplace.microsoft.com/en-us/marketplace/apps/clear-linux-project.clear-linux-os

