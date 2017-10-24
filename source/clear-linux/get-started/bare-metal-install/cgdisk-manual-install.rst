.. _cgdisk-manual-install:

Clear Linux partitioning using CGDISK
#####################################

These instructions guide you through the initial setup of your hard drive
partitions using the :command:`cgdisk` utility as part of the |CL| manual
installation process. If you do not wish to continue creating your own
partitions, :ref:`return to the bare metal manual installation
<cgdisk-manual-setup>`.

Prerequisites
*************

This guide assumes that you have followed the :ref:`bare-metal-install`
guide and intend to :ref:`install Clear Linux manually
<bare-metal-manual-install>` by choosing the :guilabel:`< Manual(Advanced) >`
menu item on the :guilabel:`Choose Installation Type` |CL| Installer setup
menu as shown in figure 1:

.. figure:: figures/cgdisk-manual-install-1.png
   :scale: 50 %
   :alt: Choose installation Type

   Figure 1: :guilabel:`Choose installation Type`

Partition using CGDISK
**********************

We use the :command:`cgdisk` application to create a
:abbr:`GPT (GUID Partition Table)` since |CL| only supports the
:abbr:`UEFI (Unified Extensible Firmware Interface)` specification. For a
complete description of the :command:`cgdisk` utility and how to use it, visit
Rod Smith's website for a `GPT fdisk tutorial`_.

In this guide, we intend to use an unpartitioned hard drive for the |CL|
installation.

#. On the :guilabel:`Choose partitioning method` menu, shown in figure 2,
   select the :guilabel:`< Manually configure mounts and partitions >` menu
   item to manually partition your hard drive.

   .. figure:: figures/cgdisk-manual-install-2.png
      :scale: 50 %
      :alt: Choose partitioning method

      Figure 2: :guilabel:`Choose partitioning method`

   The screen then shows the current device on your system you can partition.
   In this example, shown in figure 3, :file:`/dev/sda` is available but
   does not have any partitions defined.

#. Select the :guilabel:`< Partition /dev/sda >` menu item and press
   :kbd:`Enter` to begin the process of modifying this disk.

   .. figure:: figures/cgdisk-manual-install-3.png
      :scale: 50 %
      :alt: Choose a drive to partition using cgdisk tool

      Figure 3: :guilabel:`Choose a drive to partition using cgdisk tool`

   The :command:`cgdisk` application starts and displays the settings for
   :file:`/dev/sda` as shown in figure 4.

   .. figure:: figures/cgdisk-manual-install-4.png
      :scale: 50 %
      :alt: cgdisk

      Figure 4: :guilabel:`cgdisk`

Linux Partition setup
*********************

In order to properly set up the |CL| partitioning scheme, we create three
partitions using the :command:`cgdisk` utility in the following order:

  #. EFI boot partition
  #. Linux swap partition
  #. Linux root partition

For a complete understanding of these partitions, you can review the
`Linux partitioning scheme`_ information.

Create the EFI boot partition
=============================

#. With the free space highlighted in the :command:`cgdisk` utility,
   you can either select the :guilabel:`[ New ]` button and press :kbd:`Enter`
   or press the :kbd:`N` key to define a new partition.

   The utility prompts you to enter the first sector. Press the :kbd:`Enter`
   key to accept the default value shown.

   .. note::
      In this example, the first sector starts at 2048. For more information
      about alignment using the cgdisk tool, see
      `Rod Smith's Partitioning Advice about alignment`_.

#. The program then prompts you for the size of the partition. To create a
   512MB partition, enter 512M and press :kbd:`Enter` as shown in figure 5:

   .. figure:: figures/cgdisk-manual-install-5.png
      :scale: 50 %
      :alt: cgdisk - New

      Figure 5: :guilabel:`cgdisk - New partition`

#. To define the type of partition, the :command:`cgdisk` utility has
   pre-defined partition types. Press the :kbd:`L` key to show the hex codes
   you can use. Use these codes to set the correct
   :abbr:`GUID (Globally unique identifier)` for *GPT partition types* as
   shown in figure 6:

   .. figure:: figures/cgdisk-manual-install-6.png
      :scale: 50 %
      :alt: cgdisk - hex codes for partition types

      Figure 6: :guilabel:`cgdisk - hex codes for partition types`

   We need to use the following three codes for our partitions:

   * ef00 - EFI System
   * 8200 - Linux swap
   * 8300 - Linux filesystem

#. To create the EFI boot partition, enter ``ef00`` as the hexcode for this
   partition and press :kbd:`Enter`.

#. To name the partition, enter ``boot`` and press :kbd:`Enter` to finish
   setting up the EFI boot partition. The utility shows the first partition as
   an ``EFI System`` 512MiB partition named ``boot`` as shown in figure 7:

   .. figure:: figures/cgdisk-manual-install-7.png
      :scale: 50 %
      :alt: cgdisk - boot partition defined

      Figure 7: :guilabel:`cgdisk - boot partition defined`

Create the Linux swap partition
===============================

Next, we must create the Linux swap partition. In figure 7, notice the two
areas defined as free space. We created the first 1007.0 KiB free space area
when we started the EFI boot partition at sector 2048. For more information
about it, review `Rod Smith's Partitioning advice about alignment`_.

#. Move your cursor to highlight the larger free space of 334.8 GiB at the
   bottom of the partition list before you begin to create the Linux swap
   partition as shown in figure 8:

   .. figure:: figures/cgdisk-manual-install-8.png
      :scale: 50 %
      :alt: cgdisk - free space selection

      Figure 8: :guilabel:`cgdisk - free space selection`

#. To create the Linux swap partition, with the largest free space
   highlighted, select the :guilabel:`[ New ]` button or press the :kbd:`N`
   key and enter the following values for the Linux swap partition:

   .. code-block:: console

      First sector:  press :kbd:`Enter` to select the default value
      Size in sectors:  4G
      Hex code or GUID:  8200
      Enter new partition name:  swap

   Your :command:`cgdisk` partition list should now look like figure 9.

   .. figure:: figures/cgdisk-manual-install-9.png
      :scale: 50 %
      :alt: cgdisk - swap partition defined

      Figure 9: :guilabel:`cgdisk - swap partition defined`

Create the Linux filesystem partition
*************************************

Lastly, we must create the the Linux filesystem partition to use it as the
root mount point for you |CL| installation.

#. Highlight the largest free space entry at the bottom of the list and select
   the :guilabel:`[ New ]` button or press the :kbd:`N` key and enter the
   following values to create the Linux filesystem partition:

   .. code-block:: console

      First sector:  press :kbd:`Enter` to select the default value
      Size in sectors:  press :kbd:`Enter` to select the default value, which
                        is the remainder of available space on the disk
      Hex code or GUID:  8300
      Enter new partition name:  root

   With all the partitions now defined, you should see a list similar to what
   is shown in figure 10:

   .. figure:: figures/cgdisk-manual-install-10.png
      :scale: 50 %
      :alt: cgdisk - defined partitions

      Figure 10: :guilabel:`cgdisk - defined partitions`

#. If you are satisfied that the partition scheme is correct, you need to
   write this GPT to the hard drive. Select the :guilabel:`[ Write ]` button
   or press the :kbd:`W` key and the :command:`cgdisk` program prompts with:

   .. code-block:: console

      Are you sure you want to write the partition table to disk? (yes or no)

#. Enter ``yes`` and press :kbd:`Enter` to write this data to the hard drive
   and then select the :guilabel:`[ Quit ]` button or press :kbd:`Q` to exit
   the :command:`cgdisk` utility.

#. You see the partitions that were created as shown in figure 11. Move your
   cursor to the :guilabel:`< Next >` button and press :kbd:`Enter`.

   .. figure:: figures/cgdisk-manual-install-11.png
      :scale: 50 %
      :alt: defined partitions

      Figure 11: :guilabel:`defined partitions`

Set the mount points
********************

The :guilabel:`Set mount points` menu sets the mount points that the |CL|
installer uses for your |CL| installation and is shown in figure 12.

.. figure:: figures/cgdisk-manual-install-12.png
   :scale: 50 %
   :alt: Set mount points

   Figure 12: :guilabel:`Set mount points`

In this menu you need to set the mount points for the boot and root partitions
and select to format them.

#. Highlight the EFI System partition type menu entry and press the
   :kbd:`Enter` key to edit this item. The :guilabel:`Set mount point of
   sda1` menu is be shown.

   #. For the :guilabel:`Enter mount point:` type `/boot` and press
      :kbd:`Enter`.
   
   #. Enable formatting the partition by checking the :guilabel:`[ ] Format`
      toggle field.

   Figure 13 shows the entered information.  Select the :guilabel:`< Yes >`
   button and press :kbd:`Enter`.

   .. figure:: figures/cgdisk-manual-install-13.png
      :scale: 50 %
      :alt: Set mount point of sda1

      Figure 13: :guilabel:`Set mount point of sda1`

#. Do the same for the Linux filesystem partition by highlighting the
   :guilabel:`Linux filesystem` menu entry and entering the information shown
   in figure 14 to set the :guilabel:`Enter mount point:` to :file:`/` and
   enable formatting:

   .. figure:: figures/cgdisk-manual-install-14.png
      :scale: 50 %
      :alt: Set mount point of sda3

      Figure 14: :guilabel:`Set mount point of sda3`

   The final :guilabel:`Set mount points` menu item looks like figure 15:

   .. figure:: figures/cgdisk-manual-install-15.png
      :scale: 50 %
      :alt: Set mount point completed

      Figure 15: :guilabel:`Set mount points completed`

#. Select the :guilabel:`< Next >` button and press :kbd:`Enter` to proceed to
   the :guilabel:`Warning!` menu to accept your changes as shown in figure 16.
   
   .. figure:: figures/cgdisk-manual-install-16.png
      :scale: 50 %
      :alt: Warning

      Figure 16: :guilabel:`Warning`

   Highlight the :guilabel:`< Yes >` button and press :kbd:`Enter` to accept
   these changes and move on to the next step of the |CL| manual install
   process.

   This completes the process of manually setting up your hard drive
   partitions and you can now :ref:`continue with the Clear Linux manual
   install<choose-target-device>`.

.. _`GPT fdisk tutorial`:
   http://www.rodsbooks.com/gdisk/

.. _`Rod Smith's Partitioning Advice about alignment`:
   http://www.rodsbooks.com/gdisk/advice.html#alignment

.. _`information about swupd`:
   https://clearlinux.org/features/software-update

.. _`Linux partitioning scheme`:
   https://wiki.archlinux.org/index.php/partitioning#Partition_scheme