.. _multi-boot-restore-bl:

Restore the |CL-ATTR| boot loader
###################################

This guide is part of the :ref:`multi-boot` tutorial. If you install a new
:abbr:`OS (operating system)` or upgrade an existing OS, the default boot
loader may change from |CL| Systemd-Boot. This guide describes how to restore
Systemd-Boot.

#. Boot the |CL| installer from a USB thumb drive. See :ref:`bootable-usb`.

#. Log in as *root*.

   .. note::
      When you log in for the first time as *root* through the console, you must set a new password.

#. Find the location of the |CL| EFI partition. In this example, it is
   :file:`/dev/sda1`. See Figure 2.

   .. code-block:: bash

      fdisk -l

   .. figure:: figures/multi-boot-restore-bl-1.png

      Figure 1: |CL|: fdisk -l command.

#. Mount the EFI partition.

   .. code-block:: bash

      mount /dev/sda3 /mnt

#. Re-install Systemd-Boot to make it the default boot loader.

   .. code-block:: bash

      bootctl install --path /mnt

#. Unmount the EFI partition.

   .. code-block:: bash

      umount /mnt

#. Reboot.

If you want to install other :abbr:`OSes (operating systems)`, refer to
:ref:`multi-boot` for details.
