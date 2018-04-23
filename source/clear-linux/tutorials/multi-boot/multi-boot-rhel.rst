.. _multi-boot-rhel:

Install Red Hat\* Enterprise Linux 7.4 Beta
*******************************************

#. Start the Red Hat installer and follow the prompts.

#. At the :guilabel:`INSTALLATION SUMMARY` screen, choose
   :guilabel:`INSTALLATION DESTINATION`. See Figure 1.

   .. figure:: figures/multi-boot-rhel-1.png

      Figure 1: Red Hat: Installation summary

#. In the :guilabel:`Device Selection` section, select a drive on which to
   install the OS. See Figure 2.

   .. figure:: figures/multi-boot-rhel-2.png

      Figure 2: Red Hat: Installation destination

#. Under the :guilabel:`Other Storage Options` section, choose
   :guilabel:`I will configure partitioning`. See Figure 2.

#. Click :guilabel:`Done`.

#. Under :menuselection:`New Red Hat Enterprise Linux 7.4 Installation --> New mount points will use the following partitioning scheme` section,
   select :menuselection:`Standard Partition` from the drop down list. See
   Figure 3.

   .. figure:: figures/multi-boot-rhel-3.png

      Figure 3: Red Hat: New partition scheme

#. Create a new root partition.

   #. Click the :menuselection:`+` button on the lower left corner.

   #. Enter `/` and the new partition size. For this example, we specified 45
      GB. See Figure 4.

      .. figure:: figures/multi-boot-rhel-4.png

         Figure 4: Red Hat: Create new root partition

   #. Click :guilabel:`Add mount point`.

#. Share the swap partition that was created by |CL|. See Figure 5.

   #. Expand :guilabel:`Unknown`.

   #. Select :guilabel:`swap / sda2`.

   #. Select :guilabel:`Reformat`.

   #. Click :guilabel:`Update Settings`.

      .. figure:: figures/multi-boot-rhel-5.png

         Figure 5: Red Hat: Configure swap partition

#. Share the EFI partition that was created by |CL|. See Figure 6.

   #. Expand :guilabel:`Unknown.`

   #. Select :guilabel:`EFI System Partition / sda3`.

   #. Under :guilabel:`Mount Point`, enter `/boot/efi`.

   #. Click :guilabel:`Update Settings`.

      .. figure:: figures/multi-boot-rhel-6.png

         Figure 6: Red Hat: Configure EFI partition

#. Click :guilabel:`Done`.

#. Follow the remaining prompts to complete the installation of Red Hat.

#. At this point, the ability to boot |CL| is lost because `Grub`
   was set as the default boot loader. Follow these steps to make the |CL|
   Systemd-Boot the default boot loader and add Red Hat as a boot option:

   #. Boot into Red Hat.

   #. Log in.

   #. Get root privilege with the following command:

      .. code-block:: console

         $ sudo -s

   #. Locate Fedora’s :file:`grub.cfg` file at the
      :file:`/boot/efi/EFI/redhat/` directory and look for the primary Red
      Hat :guilabel:`menuentry` section. The highlighted lines identify
      the kernel and `initrd` filenames, root partition UUID, and
      additional parameters used. This information is used to create a
      new Systemd-Boot entry for Red Hat. See Figure 7.

      .. figure:: figures/multi-boot-rhel-7.png

         Figure 7: Red Hat: grub.cfg

   #. Copy the kernel and `initrd` to the EFI partition.

      .. code-block:: console

         # cp /boot/vmlinuz-3.10.0-663.el7.x86_64 /boot/efi

         # cp /boot/initramfs-3.10.0-663.el7.x86_64.img /boot/efi

   #. Create a boot entry for Red Hat. The file must, at a minimum, contain
      these settings:

      +---------+---------------------------------------------------+
      | Setting | Description                                       |
      +=========+===================================================+
      | title   | Text to show in the boot menu                     |
      +---------+---------------------------------------------------+
      | linux   | Linux kernel image                                |
      +---------+---------------------------------------------------+
      | initrd  | initramfs image                                   |
      +---------+---------------------------------------------------+
      | options | Options to pass to the EFI program or kernel boot |
      |         | parameters                                        |
      +---------+---------------------------------------------------+

      See the `systemd boot loader documentation`_ for additional
      details.

      The *options* parameters must specify the root partition UUID and any
      additional parameters that Red Hat requires.

      .. note:: The root partition UUID used below is unique to this example.

         .. code-block:: console

            # cd /boot/efi/loader/entries

            # vi redhat.conf

      Add the following lines to :file:`redhat.conf`

      .. code-block:: console

         title Red Hat Enterprise Linux 7.4 Beta

         linux /vmlinuz-3.10.0-663.el7.x86\_64

         initrd /initramfs-3.10.0-663.el7.x86\_64.img

         options root=UUID=30655c74-6cc1-4c55-8fcc-ac8bddcea4db ro
         crashkernel=auto rhgb LANG=en\_US.UTF-8

   #. Re-install Systemd-Boot to make it the default boot loader.

      .. note::
         This version of Red Hat does not support `bootctl install`. Perform
         the steps in :ref:`multi-boot-restore-bl` instead.

   #. Reboot.

If you want to install other OSes, refer to :ref:`multi-boot` for details. 


.. _systemd boot loader documentation:
   https://wiki.archlinux.org/index.php/Systemd-boot
