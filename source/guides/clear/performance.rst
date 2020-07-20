.. _performance:

Performance
###########

|CL-ATTR| is built with optimizations across the whole stack for improved
performance. |CL| achieves its performance through a variety of design decisions
and software building techniques.

.. contents:: :local:
   :depth: 1

Overview
********

The |CL| philosophy is to do everything with performance in mind. The |CL| team
applies this philosophy in the project's codebase and operating culture.

Below are some examples of the |CL| philosophy:

**Consider performance holistically.**
  Performance optimizations are considered across hardware and software. |CL|
  shows the performance potential of a holistic approach on Linux, using Intel®
  architecture with optimizations across the full stack.

**Optimize for runtime performance.**
  In general, |CL| will trade the one-time cost of longer build time and larger
  storage footprint for the repeated benefit of improved runtime performance.
  |CL| users benefit from the optimized software but aren't affected by the
  increased build time because the |CL| team builds the software before
  distributing it to |CL| clients.

**Optimize performance for server and cloud use cases first.**
  Design decisions that optimize performance for server and cloud also benefit
  other use cases, such as IoT devices and desktop clients.

|CL| has become well-known for the performance it can deliver.
`Phoronix publishes
Linux performance comparisons <https://www.phoronix.com/scan.php?page=news_topic&q=Clear+Linux>`_
that include |CL|.

Software build toolchain
************************

|CL| uses many techniques in its software build toolchain to improve software
performance, such as aggressive compiler flags and CPU-specific optimizations.
If maintained manually, these techniques can become complex to support due to
the volume of packages and the potential for technical drift of package
performance configurations. The |CL| team built the :ref:`autospec` tool to
manage this complexity and to apply the techniques used in the software build
toolchain across the entire project. autospec is available as part of the OS for
developers to use when they build their own projects on |CL|.

Latest versions of compilers and low-level libraries
====================================================

|CL| is a rolling release distribution and follows upstream software
repositories, including compilers and libraries, for updates. |CL| includes
upstream source-level optimizations as soon as they're available.

A benchmark approach to compiler performance
============================================

|CL| chooses the compiler used to build each software package on a case-by-case
basis to maximize performance. Typically, |CL| uses the open source `GNU Compiler
Collection <https://gcc.gnu.org/>`_ (GCC) with the standard low-level
libraries `Glibc <https://www.gnu.org/software/libc/>`_ and
`libstdc++ <https://gcc.gnu.org/onlinedocs/libstdc++/>`_ for C and C++
programming languages. If there is a performance advantage, |CL| will build
packages with `Clang / LLVM <https://clang.llvm.org/>`_.

|CL| uses patched compilers and low-level libraries for exact control of the
software build. Patches include changes that default to more aggressive
optimizations or optimizations that haven't yet been merged upstream.

View the full list of patches in the autospec repositories on GitHub:

* https://github.com/clearlinux-pkgs/gcc
* https://github.com/clearlinux-pkgs/glibc
* https://github.com/clearlinux-pkgs/llvm

Aggressive compiler flags
=========================

|CL| uses aggressive
`compiler flags <https://gcc.gnu.org/onlinedocs/gcc/Optimize-Options.html>`_ to
optimize software builds for runtime performance. Some significant flags that
|CL| often implements are:

`mtune and march <https://gcc.gnu.org/onlinedocs/gcc/x86-Options.html>`_
	Options used to tune generated code with optimized instructions for specific
	CPU types instead of creating generic code for maximum compatibility.

	|CL| defines its minimum hardware requirements to be second-generation
	Intel® microarchitecture code name Westmere (released in 2010) or later.
	This enables compiler optimizations that are available only on newer
	architectures. Whenever possible, |CL| tunes code for the Haswell generation
	processors or newer.

	|CL| sets	:command:`march=westmere` and :command:`mtune=haswell`.

	.. note::
		|CL| doesn't require Advanced Encryption Standard (AES), so it should
		run on some Intel CPUs from the first generation of Intel® microarchitecture code name Nehalem (released in 2008). Refer to the
		`recommended minimum system requirements <https://docs.01.org/clearlinux/latest/reference/system-requirements.html>`_ for specific requirements.

`O3 <https://gcc.gnu.org/onlinedocs/gcc/Optimize-Options.html>`_
	The largest preset of compiler options optimizations for performance. O3
	favors runtime performance.

	View the "Optimize Options" section of the GCC man page for additional
	information: :command:`man gcc`

`LTO <https://gcc.gnu.org/onlinedocs/gccint/LTO.html>`_
	Link-time optimization that performs an optimization between compiled object
	files and creation of executable binaries by adding extra information to the
	compiled object to help the linker.

`PGO <https://en.wikipedia.org/wiki/Profile-guided_optimization>`_
	Profile guided optimization or field guided optimization performs
	optimization based on information sampled during the execution of the program.


Compiler flags are set at different levels in the |CL| build environment:

User flags
	The set of default flags used by |CL| when a user compiles software
	from source. The flags are exported as system-wide environment variables from
	the
	`/usr/share/defaults/etc/profile <https://github.com/clearlinux-pkgs/filesystem/blob/master/profile.x86_64>`_ file to the user’s shell by default. These are the
	standard variables read by the compiler, named :command:`*FLAGS`, depending
	on the compiler.

	.. note::
		Source code may come with software build systems that
		override these values. This will cause a difference in expected flags.
		The |CL| autospec tooling will attempt to ignore these overrides, but
		the build system may still need patching. A manual build will not ignore
		the build system override values if they exist.

Global flags
	Compiler flags applied at a global level for all packages. The |CL| RPM
	configuration (`clr-rpm-config <https://github.com/clearlinux/clr-rpm-config>`_)
	contains global compiler flags. Search the :file:`macros` file for
	:command:`global_cflags` and search the :file:`rpmrc` file for
	:command:`optflags`. Global compiler flags may be overridden.

	.. note::
		|CL| doesn't use RPMs to install software. |CL|
		distributes software in the form of :ref:`bundles-guide`. The RPM format
		is only used during the |CL| build process as a way to resolve
		dependencies.

Per-package flags
	Compiler flags applied at a per-package level. The package's autospec
	repository contains the package-specific compiler flags. Search the
	:file:`.spec` file for the
	section starting with :command:`export CFLAGS`.

Multiple builds of libraries with CPU-specific optimizations
============================================================

To fully use the capabilities in different generations of CPU hardware, |CL|
will perform multiple builds of libraries with CPU-specific optimizations. For
example, |CL| builds libraries with Intel® Advanced Vector Extensions 2 (Intel®
AVX2) and Intel® Advanced Vector Extensions 512 (Intel® AVX-512). |CL| can then
dynamically link to the library with the newest optimization based on the
processor in the running system. Runtime libraries used by ordinary applications
benefit from these CPU specific optimizations.

The autospec repository for Python* shows an example of this optimization:
https://github.com/clearlinux-pkgs/python3

Kernel
******

A modern kernel with variants optimized for different platforms
===============================================================

|CL| is a rolling release distribution that uses the newest upstream Linux
kernel. The Linux kernel has frequent updates which can include performance
enhancements. It's a policy of the |CL| team to try to upstream any performance
enhancements in the Linux kernel for all to use.

|CL| `builds different kernel variants <https://docs.01.org/clearlinux/latest/guides/clear/compatible-kernels.html>`_ for compatibility with specific platforms.
For example, kernels meant to run on virtual machines skip support for much of
the physical hardware that doesn’t show up in VM environments and will slow down
boot.

View the kernel configuration and patches to the default native kernel in the
autospec repository: https://github.com/clearlinux-pkgs/linux/

Utility to enforce kernel runtime parameters
============================================

The Linux kernel exposes parameters for tuning the behavior of drivers and
devices such as certain buffers and resource management strategies. |CL| uses a
small utility, `clr-power-tweaks <https://github.com/clearlinux-pkgs/clr-power-tweaks>`_,
to set and enforce kernel parameter values weighted towards performance upon
boot. View the set performance values by running :command:`sudo clr_power --debug`.

Operating system
****************

Operating system and software build-time optimizations set the stage for high
performance. Decisions made after the installation of |CL| are equally as
important.


CPU performance governor
========================

|CL| uses the performance CPU governor which calls for the CPU to operate at
maximum clock frequency. In other words, P-state P0. The idea behind prioritizing
maximum CPU performance is that the faster a program finishes execution, the
faster the CPU can return to a low energy idle state. See the `CPU Power and
Performance documentation <https://docs.01.org/clearlinux/latest/guides/maintenance/cpu-performance.html>`_
for further details.

Restructured boot sequence
==========================

To optimize boot speed, |CL| uses a restructured order for boot processes that
minimizes the time services wait on slow operations and the time boot processes
wait on each other.

Systemd-bootchart is a tool for graphing the boot sequence and writes logs to a
file under :file:`/run/log`. The tool and corresponding log file make diagnosing slow
boot problems easier. All |CL| systems have `systemd-bootchart <https://github.com/systemd/systemd-bootchart>`_ enabled by default for every boot. systemd-bootchart configuration is
non-blocking to not materially slow down boot performance.

Related topics
**************

* :ref:`cpu-performance`
* `A Linux* OS for Linux Developers <https://clearlinux.org/blogs-news/linux-os-linux-developers>`_
* `The Performance Race <https://clearlinux.org/news-blogs/performance-race>`_
* `Boosting Python* from profile-guided to platform-specific optimizations <https://clearlinux.org/news-blogs/boosting-python-profile-guided-platform-specific-optimizations>`_
* `Transparent use of library packages optimized for Intel® architecture <https://clearlinux.org/news-blogs/transparent-use-library-packages-optimized-intel-architecture>`_

*Intel and the Intel logo are trademarks of Intel Corporation or its subsidiaries.*
