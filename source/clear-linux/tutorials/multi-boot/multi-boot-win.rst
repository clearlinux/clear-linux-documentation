.. _multi-boot-win:

Install Windows\* Server 2016
#############################

This guide describes Windows-specific details of the :ref:`multi-boot`
tutorial.

#. Start the Windows installer and follow the prompts.

#. At the :guilabel:`Type of installation` screen, choose
   :guilabel:`Custom: Install Windows only (advanced)`. See Figure 1.

   .. figure:: figures/multi-boot-win-1.png

      Figure 1: Windows: Choose installation type.

#. Select :guilabel:`Unallocated Space` and create a new partition of the
   desired size. In this example, we specified 50000 MB. See Figure 2.

   .. figure:: figures/multi-boot-win-2.png

      Figure 2: Windows: Create new partition.

   .. note::
      Windows creates its own 100 MB EFI partition if none exists.
      In this example, Windows sees the EFI partition created during the
      |CL| installation and does not create one.

#. Select the newly created partition and follow the remaining prompts
   to complete the Windows installation. See Figure 3.

   .. figure:: figures/multi-boot-win-3.png

      Figure 3: Windows: Install on newly created partition.

#. Finish the Windows out-of-box-experience process.

#. At this point, you cannot boot |CL| because Windows is the
   default boot loader. See :ref:`multi-boot-restore-bl` to restore
   Systemd-Boot and add Windows to its boot menu.


If you want to install other :abbr:`OSes (operating systems)`, refer to
:ref:`multi-boot` for details.

