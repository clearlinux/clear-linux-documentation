.. _firmware:

Firmware
########

This guide shows how |CL-ATTR| handles firmware and microcode loading.

.. contents::
   :local:
   :depth: 1

Overview 
********

Many devices and system components require firmware or microcode, software
that runs directly on the device, to function correctly. Because firmware
loading requires privileged hardware access, the kernel is involved in the
process.

Firmware does not typically come with source code. Instead, firmware is
provided as binary blobs which are licensed for free or non-free use.

In |CL| firmware is loaded during device initialization which typically
happens at boot time. 

.. _firmware-included-begin:

Included firmware
*****************

The Linux kernel project contains a repository for firmware binaries that are
licensed to allow free redistribution. The Linux kernel's firmware repository
can be found here:
https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git

If the firmware for your device is included upstream, no action is required
for it to be automatically detected and loaded. 

|CL| packages these firmware binaries
in the `linux-firmware bundles
<https://clearlinux.org/software?search_api_fulltext=linux-firmware>`_ and
automatically includes them with the kernel. 

You can double-check the linux-firmware bundle is installed with the commands below:

   .. code-block:: bash

      sudo swupd bundle-add linux-firmware
      find /lib/firmware/




Additional firmware loading
***************************

Some device hardware manufacturers have a license that limits redistribution
of firmware. This means |CL| is unable to distribute those firmware and you
must manually obtain them from the manufacturer or another source.

You can place additional firmware in :file:`/etc/firmware`. |CL| reads this
directory for additional firmware files in conjunction with the typical
:file:`/lib/firmware` path to provide a :ref:`stateless design <stateless>`.


#. Create the :file:`/etc/firmware` directory

   .. code-block:: bash

      sudo mkdir -p /etc/firmware

#. Obtain the additional firmware binary from a trusted source.

#. Copy the firmware files including any subdirectories to
   :file:`/etc/firmware`. It is important to place the firmware files in
   expected path for proper loading. 

   .. code-block:: bash

      sudo cp -Rv <directory>/<filename>.<fw|bin> /etc/firmware 


CPU microcode loading
*********************

Microcode is low level code for processors loaded during the boot process that
contain stability and security updates. 

Microcode updates can be updated by motherboard firmware however this is not
always feasible or does not happen in a timely fashion. The `Linux microcode
loader`_ included in the Linux kernel allows for more flexibility and more
frequent updates.

|CL| uses the *early loading* mechanism described in the `Linux microcode
loader`_ documented by which the CPU microcode is loaded as early as possible
in the boot process by using an initial RAM disk (initrd). 


Troubleshooting
***************

Look at the output of :command:`sudo dmesg` to see device initialization and
expected firmware paths



.. _`Linux microcode loader`: https://www.kernel.org/doc/Documentation/x86/microcode.txt
