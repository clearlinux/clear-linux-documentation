.. _multi-boot-sles:

Install SUSE\* Linux Enterprise Server 12 SP2
#############################################

This guide describes SUSE-specific details of the :ref:`multi-boot`
tutorial.

#. Start the SUSE installer and follow the prompts.

#. At the :guilabel:`Suggested Partitioning` screen, choose
   :guilabel:`Expert Partitioner`. See Figure 1.

   .. figure:: figures/multi-boot-sles-1.png

      Figure 1: SUSE: Suggested partitioning.

   **Optional:** Under :guilabel:`Available Storage on Linux` section,
   right-click the SUSE :file:`/home` partition and delete it. In this example, it is :file:`/dev/sda8`. See Figure 2.

   .. figure:: figures/multi-boot-sles-2.png

      Figure 2: SUSE: Delete /home partition.

#. Under :guilabel:`Available Storage on Linux` section, right-click the SUSE
   root partition and resize it. In this example, :file:`/dev/sda7` is
   resized to 45 GB. See Figure 3.

   .. figure:: figures/multi-boot-sles-3.png

      Figure 3: SUSE: Resize root partition.

#. Click :guilabel:`Accept`.

#. Follow the remaining prompts to complete the SUSE installation.

#. At this point, you cannot boot |CL| because `Grub`
   is the default boot loader. Follow these steps to make the |CL|
   Systemd-Boot the default boot loader and add SUSE as a boot option:

   #. Boot into SUSE.

   #. Log in.

   #. Locate the SUSE :file:`grub.cfg` file in the :file:`/boot/grub2/` directory
      and look for the primary SUSE :guilabel:`menuentry` section. In Figure 4, the
      highlighted lines identify the kernel, the :file:`initrd` filenames, the
      root partition UUID, and the additional parameters used. Use this information
      to create a new Systemd-Boot entry for SUSE.

      .. figure:: figures/multi-boot-sles-4.png

         Figure 4: SUSE: grub.cfg file.

   #. Copy the kernel and the :file:`initrd` file to the EFI partition.

      .. code-block:: bash

         sudo cp /boot/vmlinuz-4.4.21-69-default /boot/efi

         sudo cp /boot/initrd-4.4.21-69-default /boot/efi

   #. Create a boot entry for SUSE. At a minimum, the file must contain
      these settings:

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

         .. code-block:: bash

            sudoedit /boot/efi/loader/entries/suse.conf

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

   .. code-block:: bash

      sudo bootctl install --path /boot/efi

   .. note::
      If an older version of SUSE does not have the `bootctl` command,
      skip this step and see :ref:`multi-boot-restore-bl` to restore
      Systemd-Boot.

#. Reboot.

If you want to install other :abbr:`OSes (operating systems)`, refer to
:ref:`multi-boot` for details.


.. _systemd boot loader documentation:
   https://wiki.archlinux.org/index.php/Systemd-boot
