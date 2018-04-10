.. _multi-boot-reset-bl:

Recover the Clear Linux boot loader
***********************************

The installation of a new operating system or an upgrade of an existing
operating system can result in making the |CL| Systemd-Boot no
longer the default boot loader. To restore it, follow the steps below.

#. Boot the |CL| installer from a USB thumb drive. See :ref:`bootable-usb`.

#. At the introduction screen, press :kbd:`Control+Alt+F2` to bring up the
   |CL| console. See Figure 1.

   .. figure:: figures/multi-boot-reset-bl-1.png

      Figure 1: |CL|: Console

#. Log in as *root*.

   .. note::
      Logging in for the first time as *root* through the console requires
      setting a new password.

#. Find the location of the |CL| EFI partition, in this example it is
   :file:`/dev/sda3`. See Figure 2.

   .. code-block:: console

      # fdisk –l

   .. figure:: figures/multi-boot-reset-bl-2.png

      Figure 2: |CL| - fdisk -l

#. Mount the EFI partition.

   .. code-block:: console

      # mount /dev/sda3 /mnt

#. Re-install Systemd-Boot to make it the default boot loader.

   .. code-block:: console

      # bootctl install --path /mnt

#. Unmount the EFI partition.

   .. code-block:: console

      # umount /mnt

#. Reboot.

If you want to install other OSes, refer to :ref:`multi-boot` for details. 
