.. _cgdisk-manual-install:

Clear Linux partitioning using CGDISK
#####################################

These instructions will guide you through the initial setup of your hard drive
partitions using the :command:`cgdisk` utility as part of the |CL| manual
installation process.

Prerequisites
*************

This guide assumes that you have followed the :ref:`bare-metal-install`
guide and intend to :ref:`install Clear Linux manually <bare-metal-manual-install>`
by choosing the :guilabel:`< Manual(Advanced) >` menu item on the
``Choose Installation Type`` |CL| Installer setup menu as shown in figure 1:

.. figure:: figures/cmi-step4.png
   :scale: 50 %
   :alt: Choose installation Type

   Figure 1: :guilabel:`Choose installation Type`


Partition using CGDISK
**********************

You will need to create a :abbr:`GPT (GUID Partition Table)` since
|CL| only supports the :abbr:`UEFI (Unified Extensible Firmware Interface)`
specification. For a complete description of the :command:`cgdisk` utility and
how to use it, you can visit Rod Smith's `GPT fdisk tutorial`_.

For this guide we will start with a hard drive that has not been
partitioned and we will use the entire drive for this |CL| installation.

#. On the ``Choose partitioning method`` menu, shown in figure 2, select the
   :guilabel:`< Manually configure mounts and partitions >` menu item to
   manually partition your hard drive.

   .. figure:: figures/cmi-step5.png
      :scale: 50 %
      :alt: Choose partitioning method

      Figure 2: :guilabel:`Choose partitioning method`

   This will show the current device on your system that you can partition. In
   this example, shown in figure 3, :file:`/dev/sda` is available but
   currently does not have any partitions defined.

#. Select the :guilabel:`< Partition /dev/sda >` menu item and press
   :kbd:`Enter` to begin the process of modifying this disk.

   .. figure:: figures/cmi-step6.png
      :scale: 50 %
      :alt: Choose a drive to partition using cgdisk tool

      Figure 3: :guilabel:`Choose a drive to partition using cgdisk tool`

   The :command:`cgdisk` application will start and display the current
   settings for :file:`/dev/sda` as shown in figure 4.

   .. figure:: figures/cgd-1.png
      :scale: 50 %
      :alt: cgdisk

      Figure 4: :guilabel:`cgdisk`

Linux Partition setup
*********************

In order to properly set up the |CL| partitioning scheme, we will be creating
three partitions using the :command:`cgdisk` utility in the following order:

  #. EFI boot partition
  #. Linux swap partition
  #. Linux root partition

For a complete understanding of these partitions, you can review the
`Linux partitioning scheme`_ information found on https://wiki.archilinux.org.

Create EFI boot partition
=========================

#. With the current free space highlighted in the :command:`cgdisk` utility,
   you can either select the :guilabel:`[ New ]` and press :kbd:`Enter` or
   just press the :kbd:`N` key to begin the process of defining a new
   partition.

   You will be prompted to enter the first sector. Press the :kbd:`Enter` key
   to accept the default value that is shown in the application.

   .. note::
      In this example, the first sector starts at 2048. For more information
      about alignment using the cgdisk tool, see
      `Rod Smith's Partitioning Advice about alignment`_.

#. The program will then ask for the size of the partition. For this example,
   enter ``512M`` and press :kbd:`Enter` to create a partition that is 512MB
   in size. This is shown in figure 5:

   .. figure:: figures/cgd-2.png
      :scale: 50 %
      :alt: cgdisk - New

      Figure 5: :guilabel:`cgdisk - New partition`

#. The next step in creating the new partition is to define the type of
   partition. The :command:`cgdisk` utility has pre-defined partition
   types that can be displayed by pressing the :kbd:`L` key at this prompt to
   show the hex codes you can use. These codes are used to set the correct
   :abbr:`GUID (Globally unique identifier)` for *GPT partition types*. This
   is shown in figure 6:

   .. figure:: figures/cgd-3.png
      :scale: 50 %
      :alt: cgdisk - hex codes for partition types

      Figure 6: :guilabel:`cgdisk - hex codes for partition types`

   The codes that you are interested in using for your three partitions are:

   * ef00 - EFI System
   * 8200 - Linux swap
   * 8300 - Linux filesystem

#. Since we are currently creating the EFI boot partition, enter ``ef00`` as
   the hexcode for this partition and press :kbd:`Enter`.

#. The final field to enter is the partition name. enter ``boot`` and press
   :kbd:`Enter` to finish setting up the EFI boot partition. You will see that
   the first partition will be displayed as a 512MiB partition type of
   ``EFI System`` and a partition name of ``boot`` as shown in figure 7:

   .. figure:: figures/cgd-5.png
      :scale: 50 %
      :alt: cgdisk - boot partition defined

      Figure 7: :guilabel:`cgdisk - boot partition defined`

Create Linux swap partition
***************************

You are now ready to create the Linux swap partition. You will notice in
figure 7 that there are 2 areas defined as free space. The first area at the
top of the list, the 1007.0 KiB free space, is due to starting the previously
defined EFI boot partition at sector 2048. This is discussed
in `Rod Smith's Partitioning advice about alignment`_.

#. Move your cursor to highlight the larger free space of 334.8 GiB at the
   bottom of the partition list before you begin to create the Linux swap
   partition. This is shown in figure 8:

   .. figure:: figures/cgd-6.png
      :scale: 50 %
      :alt: cgdisk - free space selection

      Figure 8: :guilabel:`cgdisk - free space selection`

#. To create the Linux swap partition, with the largest free space highlighted,
   select the :guilabel:`[ New ]` command or press the :kbd:`N` key and enter
   the following values for the Linux swap partition:

   .. code-block:: console

      First sector:  press :kbd:`Enter` to select the default value
      Size in sectors:  4G
      Hex code or GUID:  8200
      Enter new partition name:  swap

    Your :command:`cgdisk` partition list should now look like figure 9.

    .. figure:: figures/cgd-8.png
       :scale: 50 %
       :alt: cgdisk - swap partition defined

       Figure 9: :guilabel:`cgdisk - swap partition defined`

Create Linux filesystem partition
*********************************

The final partition that you will create is the Linux filesystem partition to
be used as the root mount point for you |CL| installation.

#. Highlight the largest free space entry at the bottom of the list and select
   the :guilabel:`[ New ]` option or press the :kbd:`N` key and enter the
   following values to create the Linux filesystem partition:

   .. code-block:: console

      First sector:  press :kbd:`Enter` to select the default value
      Size in sectors:  press :kbd:`Enter` to select the default value, which
                        will be the remainder of available space on the disk
      Hex code or GUID:  8300
      Enter new partition name:  root

   With all the partitions now defined, you should see a list similar to what
   is shown in figure 10:

   .. figure:: figures/cgd-9.png
      :scale: 50 %
      :alt: cgdisk - defined partitions

      Figure 10: :guilabel:`cgdisk - defined partitions`

#. If you are satisfied that the partition scheme is correct, you will need to
   write this GPT to the hard drive. Select the :guilabel:`[ Write ]` command
   or press the :kbd:`W` key and you will be prompted with:

   .. code-block:: console

      Are you sure you want to write the partition table to disk? (yes or no)

#. Enter ``yes`` and press :kbd:`Enter` to write this data to the hard drive
   and then select the :guilabel:`[ Quit ]` command or press :kbd:`Q` to exit
   the :command:`cgdisk` utility and return to the |CL| manual installation
   process.

   You will see the partitions that you just created as shown in figure 11 and
   ready for the next step in the |CL| installer setup process.

#. Move your cursor to the :guilabel:`< Next >` field and press :kbd:`Enter`.

   .. figure:: figures/cmi-step6-done.png
      :scale: 50 %
      :alt: defined partitions

      Figure 11: :guilabel:`defined partitions`

Set mount points
****************

The ``Set mount points`` menu will set the mount points that the |CL|
installer will use for your |CL| installation and is shown in figure 12.

.. figure:: figures/cmi-step7-start.png
   :scale: 50 %
   :alt: Set mount points

   Figure 12: :guilabel:`Set mount points`

In this menu you will need to set the mount points for the boot and root
partitions and select to format them.

#. Highlight the EFI System partition type
   entry and press the :kbd:`Enter` key to edit this item. The
   ``Set mount point of sda1`` menu will be shown and you will need to enter
   the following information to set the mount to the :file:`/boot` directory
   entry as shown in figure 13:

   .. figure:: figures/cmi-step7-boot.png
      :scale: 50 %
      :alt: Set mount point of sda1

      Figure 13: :guilabel:`Set mount point of sda1`

#. Do the same for the Linux filesystem partition type by highlighting the
   :guilabel:`sda3` menu entry and entering the information shown in figure 14
   to set the :file:`/` root directory:

   .. figure:: figures/cmi-step7-root.png
      :scale: 50 %
      :alt: Set mount point of sda3

      Figure 14: :guilabel:`Set mount point of sda3`

   The final :guilabel:`Set mount points` menu item will look like figure 15:

   .. figure:: figures/cmi-step7-done.png
      :scale: 50 %
      :alt: Set mount point completed

      Figure 15: :guilabel:`Set mount point completed`

#. Move your cursor to the :guilabel:`< Next >` field and press :kbd:`Enter`
   to proceed to the :guilabel:`Warning!` menu to accept your changes as shown
   in figure 16. highlight the :guilabel:`< Yes >` field and press
   :kbd:`Enter` to accept these changes and move on to the next step of the
   |CL| manual install process.

   .. figure:: figures/cmi7of13.png
      :scale: 50 %
      :alt: Warning

      Figure 16: :guilabel:`Warning`

   This completes the process of manually setting up your hard drive
   partitions and you can now :ref:`continue with the Clear Linux manual install<choose-target-device>`.

.. _`GPT fdisk tutorial`:
   http://www.rodsbooks.com/gdisk/

.. _`Rod Smith's Partitioning Advice about alignment`:
   http://www.rodsbooks.com/gdisk/advice.html#alignment

.. _`information about swupd`:
   https://clearlinux.org/features/software-update

.. _`Linux partitioning scheme`:
   https://wiki.archlinux.org/index.php/partitioning#Partition_scheme