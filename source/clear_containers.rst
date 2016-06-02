.. _clear_containers.rst

Clear Containers
################

Introduction
============

Clear Containers is a collection of tools, configurations, and techniques
anchored on an implementation that leverages Intel Architecture to optimize
container launching and execution workflow. These optimizations improve
speed, size, and efficiency while offering a number of benefits that can
be derived only from hardware-backed virtual machines (hardware-enforced
isolation and security, for example) on Intel VT technology.

These methods are applied across all levels of the host/virtual machine
hierarchy, from the host side userland software stack down through the host
Linux kernel and into the client side kernel and userland. While a standalone
offering, Clear Containers leverage technology included as  part of the Clear
Linux distribution for many of their technology improvements.

Customers can integrate all or parts of Clear Containers into a container
infrastructure.

.. _architecture_overview.rst

Architecture Overview
=====================

Clear Containers are architected around the Linux* Kernel Virtual Machine
(KVM) virtualization infrastructure to make best use of Intel Architecture
VT features. Operational speed gets improved and overhead gets reduced by
optimizing existing code, removing redundant components, and implementing
new techniques for containers with KVM.

Version 1.0 of Clear Containers was designed as a lightweight container
system based around lkvm, KVM and Intel VT-x features; the initial version
was aimed primarily at Docker integration. Version 2.0 replaces ``lkvm``
with a lightweight version of ``qemu``. Version 1.0 also expands the
feature set to include key technologies, such as `SR-IOV`_, and the
:abbr:`Open Container Initiative (OCI)` runtime API.



V1.0
====

V1.0 of Clear Containers (also know as ‘Clear Containers for Docker*
Engine’) is based around ``kvmtool`` with example host integrations for
Docker and ``rkt``.

 .. figure:: _static/images/clear-containers-v1.png
   :align: center
   :alt: Clear Containers V1.0


Host kernel optimizations
-------------------------

Clear Containers operate better when a number of host kernel features and
optimizations are applied:

* Enabling Kernel Samepage Merging (KSM) in the host kernel is recommended
  to allow efficient page sharing of VM pages. Kernel documentation:
  Documentation/vm/ksm.txt  Config symbol: CONFIG_KSM
* Ensuring KVM VM startup times have been optimized by using a kernel
  version >= v4.0, or by backporting appropriate patches if your kernel
  version is v4.0 or lower.

.. note::

  Intel :abbr:`Extended Page Table (EPT)` acceleration will automatically be
  detected and used by your host kernel if supported by your hardware. You
  can check whether this feature is present by looking for the string ``ept``
  in the :file:`/proc/cpuinfo` of your system. See `mmu.txt`_ for more
  details.


Host user space
---------------

Clear Containers V1.0 host user space is based around ``kvmtool`` as a fast
and lightweight hypervisor. Optimiztions to ``kvmtool`` include:

* **File access**, enabling efficient *shmem* / *pci-bar* / DAX file
  access to client.
* **Less verbosity**.
* **Minimal UART scanning** to improve speed.
* **TSC timer functionality changes** passing the client apic timer
  calibration step speeds up container creation time.
* Adding ability to **skip unused features**, (such as creation of a
  custom rootfs).
* **Removing need for BIOS** saves boot time.
* **No bootloader required** speeds up initial booting of a machine.
* **Direct kernel boot** -- The hypervisor can boot the kernel directly as
  an uncompressed ELF binary. Although the kernel image is slightly larger
  than a compressed one, it ends up being faster to read and boot the larger
  file than it is to uncompress and boot the slightly smaller file.


Client mini-OS
--------------

Clear Containers V1.0 uses an optimized client user space (mini-OS) as its
primary launch vehicle to execute workload commands.The mini-OS is built
with a Clear Linux distribution that has an optimized configuration for
time and space efficiency. The mini-OS includes:

* Minimized ``systemd`` configuration
* Optimized ``libc``
* Custom AutoFDO settings
* Optimized multi-lib runtime support
* Optimized kernel config (speed and size)

The mini-OS configuration can be modified and rebuilt by customers for their
own use cases, which may preclude the need to load further client images.


Client customer images
----------------------

Clear Containers V1.0 mini-OS workloads can be used to bootstrap further
customer images. These customer images would generally be mapped into the
client via the host filesystem using **9p**, **DAX** or other filesystem and
virtual device interfaces. These customer images could for example:

* Mount a new subtree containing a payload and execute it.
* Mount a new subsystem and chroot to it for contained execution.

The mini-OS image has been optimized for size and speed. It may be replaced
or superceded -- in whole or in part -- by customer-created images.  Keep
in mind, of course, that any benefits the mini-OS provides may be lost
unless equivalent optimizations exist in the customer-created image, or have
been migrated into the image they create.



V2.0
====

Clear Containers V2.0 adopts an optimized version of the established ``qemu``
host virtualization engine, in order to support extra features not found in
Clear Containers V1.0. Clear Containers V2.0 is also compatible with the OCI
runtime specification standard, introducing a host-side abstraction tool to
ease host-side integration and to isolate integration instances from future
changes to the underlying Clear Containers architecture.


.. figure:: _static/images/clear-containers-v2.png
   :align: center
   :alt: Clear Containers V2.0

Host kernel optimizations
-------------------------

Clear Containers V2.0 host kernel optimizations are currently the same as
the V1.0 optimisations.



Host user space
---------------

Host user space is based around an optimized version of QEMU called
``qemu-lite``, with an OCI runtime-compliant wrapper called ``cor``.

Qemu-lite has the following modifications:

* **DAX support**, enabling fast and space efficient file access through
  zero-copy mapping and multi-container sharing of raw client filesystem
  images from the host filesystem.
* **Reduced "slimline" PC model** to reduce startup costs in both qemu
  and the client kernel.
* **Removed need for BIOS**, saving boot time.
* **No bootloader requirement**, to speed up boot.
* **Reduced memory footprint** by disabling memory-hungry features that
  are not required by the client system.
* **Direct kernel boot**, allowing fast booting by loading the kernel as
  an uncompressed ELF binary. Although the kernel image is slightly larger
  than a compressed one, it ends up being faster to read and boot the larger
  file than it is to uncompress and boot the slightly smaller file.
* **Added and OCI runtime-compliant wrapper AKA ``cor``** for easier
  integration with OCI-compliant host orchestration systems.



Client mini-OS
--------------

The Client mini-OS is based on the same Clear Linux based system as used in
Clear Containers V1.0; however, it may be built from more recent versions
and with more up-to date components, such as the kernel version.


Client customer images
----------------------

Client customer images are supported in the same manner as they are in Clear
Containers V1.0.



.. _SR-IOV: http://www.intel.com/content/www/us/en/pci-express/pci-sig-sr-iov-primer-sr-iov-technology-paper.html
.. _mmu.txt:  Documentation/virtual/kvm/mmu.txt