.. _multi-boot-mint:

Install Linux Mint\* 18.1 *Serena* MATE
#######################################

This guide describes Linux Mint-specific details of the :ref:`multi-boot`
tutorial.

#. Start the Mint installer and follow the prompts.

#. At the :guilabel:`Installation type` screen, choose
   :guilabel:`Something else`. See Figure 1.

   .. figure:: figures/multi-boot-mint-1.png

      Figure 1: Mint: Installation type.

#. Create a new root partition.

   #. Under the :guilabel:`Device` column, select :guilabel:`free space`. See
      Figure 2.

      .. figure:: figures/multi-boot-mint-2.png

         Figure 2: Mint: Add partition.

   #. Click the :guilabel:`+` button.

   #. In the :guilabel:`Size` field, enter a value for the new partition
      size. For this example, we used *40000 MB*, as shown in Figure 3.

      .. figure:: figures/multi-boot-mint-3.png

         Figure 3: Mint: Configure new partition settings.

   #. Set :guilabel:`Use as` to :guilabel:`Ext4 journaling file system`.

   #. Set the :guilabel:`Mount point` to :guilabel:`/`.

   #. Click :guilabel:`OK`.

#. Share the swap partition created by |CL|.

   #. Under the :guilabel:`Device` column, select :file:`/dev/sda2`.

   #. Click :guilabel:`Change`.

   #. Confirm :guilabel:`Use as` is set to :guilabel:`Swap area`. See Figure 4.

      .. figure:: figures/multi-boot-mint-4.png

         Figure 4: Mint: Set swap partition.

#. Follow the remaining prompts to complete the Mint installation.

#. At this point, you cannot boot |CL| because `Grub`
   is the default boot loader. Follow these steps to make the |CL|
   Systemd-Boot the default boot loader and add Mint as a boot option.

   #. Boot into Mint.

   #. Log in.

   #. Locate the Mint :file:`grub.cfg` file in the :file:`/boot/grub/`
      directory and look for the :guilabel:`menuentry` section. In Figure 5, the
      highlighted lines identify the kernel, the :file:`initrd` files, the root
      partition UUID, and the additional parameters used. Use this information
      to create a new Systemd-Boot entry for Mint.

      .. figure:: figures/multi-boot-mint-5.png

         Figure 5: Mint: grub.cfg file.

   #. Copy the kernel and :file:`initrd` file to the EFI partition.

      .. code-block:: bash

         sudo cp /boot/vmlinuz-4.4.0-53-generic /boot/efi

         sudo cp /boot/initrd.img-4.4.0-53-generic /boot/efi

   #. Create a boot entry for Mint. At a minimum, the file must contain
      these settings:

      +---------+------------------------------------+
      | Setting | Description                        |
      +=========+====================================+
      | title   | Text to show in the boot menu      |
      +---------+------------------------------------+
      | linux   | Linux kernel image                 |
      +---------+------------------------------------+
      | initrd  | initramfs image                    |
      +---------+------------------------------------+
      | options | Options to pass to the EFI program |
      |         | or kernel boot parameters          |
      +---------+------------------------------------+

      See the `systemd boot loader documentation`_ for additional
      details.

      The *options* parameters must specify the root partition UUID and
      any additional parameters that Mint requires.

      .. note:: The root partition UUID used below is unique to this example.

      .. code-block:: bash

         sudoedit /boot/efi/loader/entries/mint.conf

      Add the following lines to the :file:`mint.conf` file:

      .. code-block:: console

         title Mint 18.1 Serena MATE

         linux /vmlinuz-4.4.0-53-generic

         initrd /initrd.img-4.4.0-53-generic

         options root=UUID=af4901e1-6238-470a-8c14-bc0f0f7715ec ro

#. Re-install Systemd-Boot to make it the default boot loader.

   .. code-block:: bash

      sudo bootctl install --path /boot/efi

   .. note::
      If an older version of Mint does not have the `bootctl` command,
      skip this step and see :ref:`multi-boot-restore-bl` to restore
      Systemd-Boot.

#. Reboot.

If you want to install other :abbr:`OSes (operating systems)`, refer to
:ref:`multi-boot` for details.


.. _systemd boot loader documentation:
   https://wiki.archlinux.org/index.php/Systemd-boot
