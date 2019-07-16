.. _compatible-kernels:

Compatible kernels
##################

The |CL-ATTR| provides the following Linux kernels with a respective bundle.
This document describes the specific use cases these `bundles`_ serve
and provides links to their source code.

Kernel native
=============

The *kernel-native* bundle focuses on the bare metal platforms. It is optimized
for fast booting and performs best on the Intel® architectures described on the
:ref:`supported hardware list<system-requirements>`.

The optimization patches are found in the `Linux`_ GitHub\* repo.

Kernel Container
================

The *kernel-container* bundle contains the kernel used by the Intel® Clear
Containers project. This kernel is optimized for fast booting and performs best
on |CC| running on the Intel® architectures described on the
:ref:`supported hardware list<system-requirements>`.

The optimization patches are found in the `Linux-Container`_ GitHub repo.

.. _vm-kernels:

Kernel LTS
==========

The *kernel-lts* bundle focuses on the bare metal platforms but uses the latest
:abbr:`LTS (Long Term Support)` Linux kernel. It is optimized for fast booting
and performs best on the Intel® architectures described on the
:ref:`supported hardware list<system-requirements>`. This kernel also includes
the VirtualBox\* kernel modules. See the
:ref:`instructions on using Virtualbox<virtualbox-cl-installer>` for more
information.

The optimization patches are found in the `Linux-LTS`_ GitHub repo.

Kernel KVM
==========

The *kernel-kvm* bundle focuses on the Linux
:abbr:`KVM (Kernel-based Virtual Machine)`. It is optimized for fast booting
and performs best on virtual machines running on the Intel® architectures
described in the :ref:`supported hardware list<system-requirements>`.
Use this kernel when running |CL| as the guest OS on top of *qemu/kvm* or with
**cloud orchestrators** using *qemu/kvm* internally as
their **hypervisor**. This kernel can be used as a standalone |CL| VM. See
the :ref:`instructions on using KVM<kvm>` for more information.

The optimization patches are found in the `Linux-KVM`_ GitHub repo.

Kernel Hyper-V\*
================

The *kernel-hyperv* bundle focuses on running Linux on Microsoft\*
Hyper-V. It is optimized for fast booting and performs best on Virtual
Machines running on the Intel® architectures described on the
:ref:`supported hardware list<system-requirements>`.
Use this kernel when running |CL| as the guest OS of **Cloud Instances** in
projects such as Microsoft `Azure`_\*. This kernel can be used in a
standalone |CL| VM. See the :ref:`instructions on using Hyper-V<hyper-v>` for
more information.

The optimization patches are found in the `Linux-HyperV`_ GitHub repo.

Kernel Hyper-V LTS
==================

The *kernel-hyperv-lts* bundle focuses on running Linux on Microsoft
Hyper-V but uses the latest :abbr:`LTS (Long Term Support)` Linux kernel. It
is optimized for fast booting and performs best on virtual machines running on
the Intel® architectures described on the
:ref:`supported hardware list<system-requirements>`. Use this kernel when
running |CL| as the guest OS of **Cloud Instances** in projects such as
Microsoft `Azure`_. This kernel can be used in a standalone |CL| VM. See our
:ref:`instructions on using Hyper-V<hyper-v>` for more information.

The optimization patches are found in the `Linux-HyperV-LTS`_ GitHub repo.


.. _Linux: https://github.com/clearlinux-pkgs/linux
.. _Linux-LTS: https://github.com/clearlinux-pkgs/linux-lts
.. _Linux-KVM: https://github.com/clearlinux-pkgs/linux-kvm
.. _Linux-HyperV: https://github.com/clearlinux-pkgs/linux-hyperv
.. _Linux-HyperV-LTS: https://github.com/clearlinux-pkgs/linux-hyperv-lts
.. _Linux-Container: https://github.com/clearlinux-pkgs/linux-container
.. _bundles: https://github.com/clearlinux/clr-bundles
.. _CIAO: https://github.com/01org/ciao
.. _Azure:
   https://azuremarketplace.microsoft.com/en-us/marketplace/apps/clear-linux-project.clear-linux-os

