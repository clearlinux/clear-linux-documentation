.. _multi-boot:

Multi-boot Clear Linux with other operating systems
###################################################

Starting with version 16140, |CLOSIA| uses the Systemd-Boot boot loader,
which does not support multi-booting without manual manipulation. This
document shows how to modify the boot loader for |CL| to work with other
operating systems.

Process overview
****************

The general process to install other operating systems for a
multi-booting computer is as follows:

#. Install |CL| first with a EFI partition large enough to store the kernels
   of other operating systems and their initrds in the case of Linux\*
   distributions.

#. Install the next operating system without creating its own EFI
   partition.

#. Boot into the newly installed operating system.

#. For Linux distributions, copy its kernel and `initrd` to the |CL| EFI
   partition. This step is not needed for Windows\*.

#. Add an entry for the newly installed operating system in the
   Systemd-Boot menu.

#. Make Systemd-Boot the default boot loader.

#. Repeat the previous steps for each additional operating system. Always
   install |CL| first. Install other operating systems in any order.

.. note::
   This process is not guaranteed to work with all Linux distributions and
   all their versions.

Detailed procedures
*******************

.. toctree::
   :maxdepth: 2

   multi-boot-cl
   multi-boot-win
   multi-boot-rhel
   multi-boot-sles
   multi-boot-ubuntu
   multi-boot-mint
   multi-boot-reset-bl

Tested operating systems
************************

The following operating systems were tested on an Intel® NUC6i7KYK with 32GB
RAM and a 360GB SSD. Table 1 lists the information specific to the
installation of the tested operating systems.

.. csv-table:: Table 1: OS specific installation information
   :header: # , OS, Version, Partition Size [1], Swap Size [2], EFI Partition Size [3], Download Link

   1,Clear Linux,16140,50GB,8GB,1GB,https://download.clearlinux.org/image/clear-15870-installer.img.xz
   2,Windows ,Server 2016,50GB,N/A,Shared with #1,From Microsoft
   3,RedHat,Server 7.4 Beta,45GB,Shared with #1,Shared with #1,From RedHat
   4,SUSE,Server 12 SP2,45GB,Shared with #1,Shared with #1,From SUSE
   5,Ubuntu,16.04.02 LTS Desktop,40GB,Shared with #1,Shared with #1,https://www.ubuntu.com/download/desktop
   6,Mint,18.1 ?Serena? MATE,40GB,Shared with #1,Shared with #1,https://linuxmint.com/edition.php?id=228

.. [#] Configure the partition size as desired.

.. [#] To save disk space, a single swap partition can be shared among
   multiple Linux installations. Swap size was determined using these
   `recommended swap partition sizes`_.


.. [#] This partition will hold the |CL| and other operating
   systems’ kernel and boot information. The partition size is dependent on
   the number of operating systems that will be installed. In general,
   allocate about 100MB per operating system. For this demonstration, we used
   1GB.

.. note::
   Updating any installed operating systems will likely result
   in the |CL| Systemd-Boot no longer being the default
   boot loader. To restore it, see :ref:`multi-boot-reset-bl`.

.. note::
   Updating any Linux installation may result in changes of their kernels or
   initrds. Keep their corresponding Systemd-Boot
   :file:`/boot/efi/loader/entries/*.conf` files up-to-update.


.. _recommended swap partition sizes:
   https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/5/html/Deployment_Guide/ch-swapspace.html


