.. _multi-boot-sles:

Install SUSE\* Linux Enterprise 12 SP2
**************************************

#. Start the SUSE installer and follow the prompts.

#. At the :guilabel:`Suggested Partitioning` screen, choose
   :guilabel:`Expert Partitioner`. See Figure 1.

   .. figure:: figures/multi-boot-sles-1.png

      Figure 1: SUSE: Suggested partitioning

   **Optional:** Under :guilabel:`Available Storage on Linux` section,
   right-click the SUSE :file:`/home` partition and delete it. In this example, it is :file:`/dev/sda8`. See Figure 2.

   .. figure:: figures/multi-boot-sles-2.png

      Figure 2: SUSE: Delete /home partition

#. Under :guilabel:`Available Storage on Linux` section, right-click the SUSE
   root partition and resize it. In this example, :file:`/dev/sda7` is
   resized to 45 GB. See Figure 3.

   .. figure:: figures/multi-boot-sles-3.png

      Figure 3: SUSE: Resize root partition

#. Click :guilabel:`Accept`.

#. Follow the remaining prompts to complete the installation of SUSE.

#. At this point, |CL| cannot boot because `Grub`
   is the default boot loader. Follow these steps to make the |CL|
   Systemd-Boot the default boot loader and add SUSE as a boot option:

   #. Boot into SUSE.

   #. Log in.

   #. Get root privileges with the following command:

      .. code-block:: console

         $ sudo -s

   #. Locate SUSE’s :file:`grub.cfg` in the :file:`/boot/grub2/` directory
      and look for the primary SUSE :guilabel:`menuentry` section. The
      highlighted lines identify the kernel, the :file:`initrd` filenames,
      the root partition UUID, and the additional parameters used. Use this
      information to create a new Systemd-Boot entry. See Figure 4.

      .. figure:: figures/multi-boot-sles-4.png

         Figure 4: SUSE: grub.cfg

   #. Copy the kernel and the :file:`initrd` file to the EFI partition.

      .. code-block:: console

         # cp /boot/vmlinuz-4.4.21-69-default /boot/efi

         # cp /boot/initrd-4.4.21-69-default /boot/efi

   #. Create a boot entry for SUSE. The file must at least contain these
      settings:

      +---------+---------------------------------------+
      | Setting | Description                           |
      +=========+=======================================+
      | title   | Text to show in the boot menu         |
      +---------+---------------------------------------+
      | linux   | Linux kernel image                    |
      +---------+---------------------------------------+
      | initrd  | initramfs image                       |
      +---------+---------------------------------------+
      | options | Options to pass to the EFI program or |
      |         | kernel boot parameters                |
      +---------+---------------------------------------+

      See the `systemd boot loader documentation`_ for additional
      details.

      The *options* parameter must specify the root partition UUID and
      any additional parameters SUSE requires.

      .. note:: The root partition UUID used below is unique to this example.

         .. code-block:: console

            # cd /boot/efi/loader/entries

            # vi suse.conf

         Add the following lines to the :file:`suse.conf` file:

            .. code-block:: console

               title SUSE Linux Enterprise 12 SP2

               linux /vmlinuz-4.4.21-69-default

               initrd /initrd-4.4.21-69-default

               options root=UUID=b9e25e98-a644-4ac3-b955-ae32800ee350 ro
               resume=/dev/disk/by-uuid/6a50c032-1c1e-4b4a-b799-ca365bb10dc7
               splash=silent showopts crashkernel=109M,high
               crashkernel=72M,low

#. Re-install Systemd-Boot to make it the default boot loader.

   .. code-block:: console

      # bootctl install --path /boot/efi

   .. note::
      If an older version of SUSE does not have the `bootctl` command,
      skip this step and see :ref:`multi-boot-restore-bl` to restore the |CL|
      Systemd-Boot boot loader.

#. Reboot.

If you want to install other OSes, refer to :ref:`multi-boot` for details. 


.. _systemd boot loader documentation:
   https://wiki.archlinux.org/index.php/Systemd-boot
