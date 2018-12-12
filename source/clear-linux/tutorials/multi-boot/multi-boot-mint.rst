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

   #. Create a boot entry for Mint to invoke grub

      +---------+------------------------------------+
      | Setting | Description                        |
      +=========+====================================+
      | title   | Text to show in the boot menu      |
      +---------+------------------------------------+
      | efi     | Linux bootloader                   |
      +---------+------------------------------------+

      See the `systemd boot loader documentation`_ for additional
      details.

      .. code-block:: bash

         sudoedit /boot/efi/loader/entries/mint.conf

      Add the following lines to the :file:`mint.conf` file:

      .. code-block:: console

         title Mint 18.1 Serena MATE

         efi /EFI/mint/grubx64.efi

#. Reboot.

On |CL|, Systemd-Boot timeout needs to be set for this entry to show up. Please make sure the following is set each time |CL| does an update.

    .. code-block:: bash

       sudo clr-boot-manager set-timeout 20
       sudo clr-boot-manager update

If you want to install other :abbr:`OSes (operating systems)`, refer to
:ref:`multi-boot` for details.


.. _systemd boot loader documentation:
   https://wiki.archlinux.org/index.php/Systemd-boot
