.. _multi-boot:

Multi-boot |CL-ATTR| with other operating systems
#################################################

|CL-ATTR| uses the Systemd-Boot boot loader, which supports
multi-booting with manual configuration. This tutorial shows how to
configure the |CL| bootloader to work with other
:abbr:`OSes (operating systems)`. We recommend having at least two USB
devices of 16GB minimum size for ease of installation.

.. warning::

   Always back up critical data before installing an additional OS on a target system. Some data loss may occur.

clr-boot-manager
****************

The `clr-boot-manager` is designed to install the bootloader, kernel,
initrd, and accompanying metadata files for GPT disks using UEFI. The
bootloader supports booting other OSes using a shared boot directory, such
as the EFI System Partition for UEFI-booting operating systems. We present
mulit-boot solutions that require first setting a `Systemd-Boot` timeout
period and then allowing `clr-boot-manager` to invoke GRUB if selected.

.. _multi-boot-detail-proc:

Detailed procedures
*******************

.. toctree::
   :maxdepth: 1

   multi-boot-ubuntu
   multi-boot-mint
   multi-boot-win
   multi-boot-restore-bl

Overview
********

Follow this process to install other operating systems for a multi-boot
computer. Install |CL| first, then install other operating systems.

#. Install |CL| first with an EFI partition large enough to store the kernels
   of other operating systems and their initrds, in the case of Linux distributions.

   .. note::

      Apply set-timeout in the `clr-boot-manager`. This enables display of all multi-boot options before a default boot.

#. Install the next operating system without creating its own EFI
   partition.

#. Boot into the newly installed operating system.

#. For Linux distributions, copy its kernel and `initrd` to the |CL| EFI
   partition. This step is not needed for Windows\*.

   .. note::

      Ubuntu offers a simpler solution in one step.

#. Add an entry for the newly installed operating system in the
   Systemd-Boot menu.

#. Make Systemd-Boot the default boot loader.

#. Repeat the previous steps to install each additional operating system.

If you update any installed operating systems, be aware that:

*  The default boot loader may change from |CL| Systemd-Boot. Perform the
   steps in :ref:`multi-boot-restore-bl`.

*  Linux kernels or `initrd` images may change.
   Keep their corresponding Systemd-Boot
   :file:`/boot/efi/loader/entries/*.conf` files up-to-date.

This process is not guaranteed to work with all Linux distributions and
their versions.

.. _multi-boot-cl:

Install |CL|
************

#. Install |CL| using :ref:`bare-metal-install-server`.

#. Follow the `Advanced Configuration`, `Manual partition` method below.
   Allow enough free space for other OSes that you plan to install.

.. include:: ../../get-started/bare-metal-install-server/bare-metal-install-server.rst
   :start-after: advanced-config-install-start:
   :end-before: advanced-config-install-end:

#. After installation is complete, open a Terminal and run:

   .. code-block:: bash

      sudo clr-boot-manager set-timeout 20
      sudo clr-boot-manager update

   .. note::

      Run these commands each time that you run a `swupd update`.

Tested operating systems
************************

The following operating systems were tested on an Intel® NUC7i7BNB with 16GB
RAM and a 112GB SSD. Table 1 lists the information specific to the
installation of the tested operating systems.

.. csv-table:: Table 1: OS specific installation information
   :header: # , OS, Version, Partition Size [#]_, Swap Size [#]_, EFI Partition Size [#]_, Download Link

   1, Clear Linux, 29400, 30 GB, 256 MB, 150 MB, https://clearlinux.org/downloads

   2,Ubuntu\*,18.04.0 LTS Desktop,40 GB,Shared with #1,Shared with #1,https://www.ubuntu.com/download/desktop

   3,Linux Mint\*,19.1 *Tessa* Cinnamon,40 GB,Shared with #1,Shared with #1,https://linuxmint.com/download.php

   4,Windows,Server 2019,50 GB,N/A,Shared with #1,https://www.microsoft.com/en-us/cloud-platform/windows-server

Table notes:

.. [#] Configure the partition size as desired.


.. [#] To save disk space, share a single swap partition between
   multiple Linux installations. Swap size was determined using these
   `recommended swap partition sizes`_.


.. [#] The EFI partition holds the kernel and boot information for |CL| and
   other operating systems. The partition size is dependent on the number
   of operating systems to be installed. In general, allocate about 100 MB
   per operating system.


.. _recommended swap partition sizes:
   https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/5/html/Deployment_Guide/ch-swapspace.html

.. _Default partition schema: https://clearlinux.org/documentation/clear-linux/get-started/bare-metal-install-server#default-partition-schema

.. _Disk encryption: https://clearlinux.org/documentation/clear-linux/get-started/bare-metal-install-server#disk-encryption

.. _Telemetry: https://clearlinux.org/documentation/clear-linux/get-started/bare-metal-install-server#telemetry