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
   boot loader. To restore it, see :ref:`multi-boot-restore-bl`.

.. note::
   Updating any Linux installation may result in changes of their kernels or
   initrds. Keep their corresponding Systemd-Boot
   :file:`/boot/efi/loader/entries/*.conf` files up-to-update.

.. _multi-boot-detail-proc:

Detailed procedures
*******************

   :ref:`multi-boot-cl` (below)

.. toctree::
   :maxdepth: 2

   multi-boot-win
   multi-boot-rhel
   multi-boot-sles
   multi-boot-ubuntu
   multi-boot-mint
   multi-boot-restore-bl


.. _multi-boot-cl:

Install the Clear Linux OS
**************************

#. Create a bootable USB drive of the |CL| installer using one of the methods
   below.

   * :ref:`bootable-usb-linux`
   * :ref:`bootable-usb-mac`
   * :ref:`bootable-usb-windows`

#. Start the |CL| installer and follow the prompts.

#. On the *Choose Installation Type* screen, choose *Manual (Advanced)*,
   as shown in Figure 1.

   .. figure:: figures/multi-boot-01.png

      Figure 1: |CL| installer: Choose installation type screen

   .. note::
      If you are not familiar with text-based installation
      interfaces, here are some navigation tips:

      * Use the :kbd:`Up Arrow` and :kbd:`Down Arrow` keys to move between
        the options on the screen.

      * Use the :kbd:`Space` to select or highlight an option.

      * Press :kbd:`Enter` to activate the selected option and to move ahead.

#. On the :guilabel:`Choose partitioning method` screen, choose
   :guilabel:`Manually configure mounts and partitions`, as shown in
   Figure 2.

   .. figure:: figures/multi-boot-02.png

      Figure 2: |CL|: Choose partitioning method

#. Select the drive, in this case :file:`/dev/sda` and press :kbd:`Enter` to
   go into the `cgdisk` partitioning tool. See Figure 3.

   .. figure:: figures/multi-boot-03.png

   Figure 3: |CL|: Choose drive to partition

#. Create a new root partition.

   #. Select :guilabel:`New`. See Figure 4.

      .. _multi-boot-04:

      .. figure:: figures/multi-boot-04.png

         Figure 4: |CL|: Create new partition

   #. Accept the default first sector.

   #. Specify the desired size of the partition. For this example, we
      specified *50GB*. See Figure 5.

      .. figure:: figures/multi-boot-05.png

         Figure 5: |CL|: New partition size

   #. Set the partition type to :guilabel:`8300 (Linux filesystem)`. See
      Figure 6.

      .. figure:: figures/multi-boot-06.png

         Figure 6: |CL|: Set partition type

   #. Name the partition :file:`CL-root`. This name makes it easier to
      identify later. See Figure 7.

      .. figure:: figures/multi-boot-07.png

         Figure 7: |CL|: Name partition

#. Create a new swap partition. See Figure 8.

   .. figure:: figures/multi-boot-08.png

      Figure 8: |CL|: Create swap partition

   #. Select the `free space` partition located at the bottom of the column.

   #. Select :guilabel:`New`. See :ref:`Figure 4<multi-boot-04>`.

   #. Accept the default first sector.

   #. Specify the desired size of the swap partition. For this example, we
      used 8GB. See the `recommended swap partition sizes`_ for guidance.

   #. Set the partition type to :guilabel:`8200 (Linux swap)`.

   #. Name the partition :file:`CL-swap`.

#. Create a new EFI partition. See Figure 9.

   .. figure:: figures/multi-boot-09.png

      Figure 9: |CL|: Create EFI partition

   #. In the Partition Type column, select :guilabel:`free space` located at
      the bottom of the column.

   #. Select :guilabel:`New`. See :ref:`Figure 4<multi-boot-04>`.

   #. Accept the default first sector.

   #. Specify the desired size of the partition. For this example, we used
      1024 MB. This partition will hold |CL|, the kernels of the other
      operating systems, and their boot information. Its size depends on the
      number of installed operating systems. In general, allocate about 100MB
      per operating system. For this example, we used 1024 MB.

   #. Set the partition type to :guilabel:`ef00 (EFI partition)`.

   #. Name the partition :file:`CL-EFI`.

#. Select :guilabel:`Write` to apply the new partition table.

#. Select :guilabel:`Quit` to exit the `cgdisk` tool.

#. On the :guilabel:`Set mount points` screen, specify the mount points and
   format settings as shown in Figure 10.

   .. figure:: figures/multi-boot-10.png

      Figure 10: |CL|: Set mount points

#. On the :guilabel:`User configuration` screen, select
   :guilabel:`Create an administrative user`. See Figure 11.

   .. figure:: figures/multi-boot-11.png

      Figure 11: |CL|: User configuration

#. Select :guilabel:`Add user to sudoers?`. See Figure 12.

   .. figure:: figures/multi-boot-12.png

      Figure 12: |CL|: Add user as sudoer

#. Follow the remaining prompts to complete the installation and go through
   the out-of-box-experience of |CL|.

#. Log in.

#. Get root privileges.

   .. code-block:: console

      $ sudo -s

#. Add a timeout period for Systemd-Boot to wait, otherwise it will not
   present the boot menu and will always boot |CL|.

   .. code-block:: console

      # clr-boot-manager set-timeout 20

      # clr-boot-manager update

#. Reboot.

If you want to install other OSes, refer to :ref:`multi-boot-detail-proc`.

.. _recommended swap partition sizes:
   https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/5/html/Deployment_Guide/ch-swapspace.html
