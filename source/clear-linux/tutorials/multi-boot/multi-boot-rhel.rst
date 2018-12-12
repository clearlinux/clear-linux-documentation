.. _multi-boot-rhel:

Install Red Hat\* Enterprise Linux 7.4 Beta
###########################################

This guide describes Red Hat-specific details of the :ref:`multi-boot`
tutorial.

#. Start the Red Hat installer and follow the prompts.

#. At the :guilabel:`INSTALLATION SUMMARY` screen, choose
   :guilabel:`INSTALLATION DESTINATION`. See Figure 1.

   .. figure:: figures/multi-boot-rhel-1.png

      Figure 1: Red Hat: Installation summary.

#. In the :guilabel:`Device Selection` section, select a drive on which to
   install the OS. See Figure 2.

   .. figure:: figures/multi-boot-rhel-2.png

      Figure 2: Red Hat: Installation destination.

#. Under the :guilabel:`Other Storage Options` section, choose
   :guilabel:`I will configure partitioning`. See Figure 2.

#. Click :guilabel:`Done`.

#. Under the :menuselection:`New Red Hat Enterprise Linux 7.4 Installation
   --> New mount points will use the following partitioning scheme` section,
   select :menuselection:`Standard Partition` from the drop down list. See
   Figure 3.

   .. figure:: figures/multi-boot-rhel-3.png

      Figure 3: Red Hat: New partition scheme.

#. Create a new root partition.

   #. Click the :menuselection:`+` button on the lower left corner.

   #. Enter `/` and the new partition size. For this example, we specified 45
      GB. See Figure 4.

      .. figure:: figures/multi-boot-rhel-4.png

         Figure 4: Red Hat: Create new root partition.

   #. Click :guilabel:`Add mount point`.

#. Share the swap partition that was created by |CL|. See Figure 5.

   #. Expand :guilabel:`Unknown`.

   #. Select :guilabel:`swap / sda2`.

   #. Select :guilabel:`Reformat`.

   #. Click :guilabel:`Update Settings`.

      .. figure:: figures/multi-boot-rhel-5.png

         Figure 5: Red Hat: Configure swap partition.

#. Share the EFI partition that was created by |CL|. See Figure 6.

   #. Expand :guilabel:`Unknown.`

   #. Select :guilabel:`EFI System Partition / sda3`.

   #. Under :guilabel:`Mount Point`, enter `/boot/efi`.

   #. Click :guilabel:`Update Settings`.

      .. figure:: figures/multi-boot-rhel-6.png

         Figure 6: Red Hat: Configure EFI partition.

#. Click :guilabel:`Done`.

#. Follow the remaining prompts to complete the Red Hat installation.
         
#. At this point, you cannot boot |CL| because `Grub`
   is the default boot loader. Follow these steps to make the |CL|
   Systemd-Boot the default boot loader and add Red Hat as a boot option:

   #. Boot into Red Hat.

   #. Log in.

   #. Create a boot entry for Red Hat to invoke grub

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

         sudoedit /boot/efi/loader/entries/redhat.conf

      Add the following lines to the :file:`redhat.conf` file:

      .. code-block:: console

         title Red Hat Enterprise Linux 7.4 Beta

         efi /EFI/redhat/grubx64.efi

#. Reboot.

If you want to install other :abbr:`OSes (operating systems)`, refer to
:ref:`multi-boot` for details.


.. _systemd boot loader documentation:
   https://wiki.archlinux.org/index.php/Systemd-boot
