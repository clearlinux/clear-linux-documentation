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

   #. Create a boot entry for SUSE to invoke grub

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

         sudoedit /boot/efi/loader/entries/suse.conf

      Add the following lines to the :file:`suse.conf` file:

      .. code-block:: console

         title SUSE Enterprise Linux 7.4 Beta

         efi /EFI/suse/grubx64.efi

#. Reboot.

On |CL|, Systemd-Boot timeout needs to be set for this entry to show up. Please make sure the following is set each time |CL| does an update

    .. code-block:: bash

       sudo clr-boot-manager set-timeout 20
       sudo clr-boot-manager update


If you want to install other :abbr:`OSes (operating systems)`, refer to
:ref:`multi-boot` for details.


.. _systemd boot loader documentation:
   https://wiki.archlinux.org/index.php/Systemd-boot
