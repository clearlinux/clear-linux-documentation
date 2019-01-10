.. _multi-boot-ubuntu:

Install Ubuntu\* 18.04 LTS Desktop
##################################

This guide explains how to install Ubuntu 18.04 LTS Desktop on a separate
partition of a target on which |CL| is already installed.

#. Start the Ubuntu installer, and follow the prompts.

#. At the :guilabel:`Installation type` screen, choose
   :guilabel:`Something else`. See Figure 1.

   .. figure:: figures/multi-boot-ubuntu-1.png

      Figure 1: Ubuntu: Installation type.

#. Create a new root partition.

   #. Under the :guilabel:`Device` column, select :guilabel:`free space`. See
      Figure 2.

      .. figure:: figures/multi-boot-ubuntu-2.png

         Figure 2: Ubuntu: Add partition.

   #. Click the :guilabel:`+` button on the lower left corner.

   #. Enter the new partition size. For this example, we used *40000 MB*, as
      shown in Figure 3.

      .. figure:: figures/multi-boot-ubuntu-3.png

         Figure 3: Ubuntu: Configure new root partition.

   #. Set :guilabel:`Use as` to :guilabel:`Ext4 journaling file system`.

   #. Set the :guilabel:`Mount point` to `/`.

   #. Click :guilabel:`OK`.

   #. Under the :guilabel:`Format?` column, select the new partition to be
      formatted, in this example :file:`/dev/sda8`.

#. Share the swap partition that was created by |CL|.

   #. Under the :guilabel:`Device` column, select :file:`/dev/sda2`.

   #. Click :guilabel:`Change`.

   #. Confirm :guilabel:`Use as` is set to :guilabel:`swap area`. See Figure 4.

      .. figure:: figures/multi-boot-ubuntu-4.png

         Figure 4: Ubuntu: Set swap partition.

#. Follow the remaining prompts to complete the Ubuntu installation.

#. Upon reboot, remove the USB/installation media.

#. Follow these steps to make `Systemd-Boot` the default boot loader and add
   Ubuntu as a boot option:

   #. Boot into Ubuntu.

   #. Log in.

#. Open a Terminal, and cd into the root directory:

   .. code-block:: bash

      cd  /

#. Next, create a boot entry for Ubuntu to invoke grub, using this format:

   +---------+------------------------------------+
   | Setting | Description                        |
   +=========+====================================+
   | title   | Text to show in the boot menu      |
   +---------+------------------------------------+
   | efi     | Linux bootloader                   |
   +---------+------------------------------------+

   .. note::

      See the `systemd boot loader documentation`_ for additional details.

#. To do so, enter the command:

   .. code-block:: bash

      sudoedit /boot/efi/loader/entries/ubuntu.conf

#. Add the following lines to the :file:`ubuntu.conf` file:

   .. code-block:: bash

      title Ubuntu 18.04 LTS Desktop

      efi /EFI/ubuntu/grubx64.efi

#. Save and close the file.

#. Reboot.

#. Log in.

#. Open a new Terminal.

#. Re-install `Systemd-Boot` to make it the default boot loader.

   .. code-block:: bash

      sudo bootctl install --path /boot/efi

   .. note::

      If an older version of Ubuntu does not have the `bootctl` command,
      skip this step and see :ref:`multi-boot-restore-bl` to restore
      Systemd-Boot.

#. After running the above command, the output should look similar to
   Figure 6.

   .. figure:: figures/multi-boot-ubuntu-6.png

      Figure 6: Created EFI boot entry Linux Boot Manager.

#. Reboot the target system.

#. Upon reboot, the GRUB menu should appear with the new option for Ubuntu,
   as well as |CL|.

If you want to install other :abbr:`OSes (operating systems)`, refer to
:ref:`multi-boot` for details.

.. _systemd boot loader documentation:
   https://wiki.archlinux.org/index.php/Systemd-boot

