.. _system-requirements:

Recommended minimum system requirements
#######################################

|CL-ATTR| can run on most modern hardware and is capable of running with
modest hardware resources. Out of the box, |CL| can run on a single CPU core,
1 GB RAM, and minimum of disk space of:

* 4 GB for the *live server*
* 20 GB for the *live desktop*

.. caution::

   Advanced users who wish to install on a disk using less than the recommended
   space requirements may use the flag ``--skip-validation-size``. Use of this
   flag may cause the installation to fail due to inadequate disk space.


For use cases requiring minimal resources, |CL| :ref:`about <about>` can
be used to create a highly customized installation that can even run on a
system with a 128MB of memory and 600MB of disk space, for example.


Installer requirements
**********************

The *live desktop* installer requires at least 1 GB of RAM because more
resources are required to run in live mode than after |CL| is installed onto
persistent storage.

For hardware with less resources, use the *live server* installer because it
has a smaller memory footprint.

See https://clearlinux.org/downloads for more download options.


System requirements
*******************

|CL| requires an x86 64-bit processor which supports Intel® Streaming SIMD
Extensions 4.2 (Intel® SSE 4.2). 

For information on the boot loader, see the `clr-boot-manager readme`_ .

The |CL| installer performs a system compatibility check upon booting. To
manually verify system compatibility with |CL|, run the :ref:`compatibility
check tool<compatibility-check>` or go to http://ark.intel.com and check for
these features:

* Instruction Set:

  - 64-bit

* Instruction Set Extensions:

  - Supplemental Streaming SIMD Extension 3 (SSSE3)
  - Intel® Streaming SIMD Extensions 4.1 (Intel® SSE 4.1)
  - Intel® Streaming SIMD Extensions 4.2 (Intel® SSE 4.2)
  - Carry-less Multiplication (PCLMUL)

The following processor families have been verified to run |CL|:

* Intel® Core™ processor family (2nd generation or greater)
* Intel® Xeon® E3-xxxx processor
* Intel® Xeon® E5-xxxx processor
* Intel® Xeon® E7-xxxx processor
* Intel Atom® processor C Series
* Intel Atom® processor E Series


Recommended configurations
**************************

For general |CL| desktop use the recommended minimum requirements include:

=========    ===============================
Component    Configuration
---------    -------------------------------
Processor    Compatible x86 64-bit processor
---------    -------------------------------
Memory       4GB RAM
---------    -------------------------------
Disk         20 GB
---------    -------------------------------
Graphics     Device with openGL support (e.g. Intel HD/UHD Graphics)
---------    -------------------------------
Network      Active Internet connection
=========    ===============================


*Intel, Intel Core, Xeon, Intel Atom, and the Intel logo are trademarks of
Intel Corporation or its subsidiaries.*

.. _clr-boot-manager readme: https://github.com/clearlinux/clr-boot-manager