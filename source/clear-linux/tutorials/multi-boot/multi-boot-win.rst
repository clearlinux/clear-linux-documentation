.. _multi-boot-win:

Install Windows\* Server 2019
#############################

This guide describes Windows-specific details of the :ref:`multi-boot`
tutorial. In this case, we download the free trial of Windows Server 2019.

#. Download `Microsoft Windows Server 2019`_ from the link.

#. Start the Windows installer and follow the prompts.

#. In the Windows Setup, Windows Server 2019, select your preferences, and
   then select :guilabel:`Next`.

#. In the dialogue,
   :guilabel:`Select the operating system you want to install`, select the type of Operating system you want to install.

#. Select :guilabel:`Next`.

#. In the :guilabel:`Applicable notices and license terms`, select the
   checkbox to accept the terms, then select :guilabel:`Next`.

#. In the dialogue, :guilabel:`What type of installation do you want?`,
   choose :guilabel:`Custom: Install Windows only (advanced)`. See Figure 1.

   .. figure:: figures/multi-boot-win-1.png

      Figure 1: Windows: Choose installation type.

#. Select :guilabel:`Unallocated Space`, then select :guilabel:`New`, to
   create a new partition of the desired size. In this example, we specified 50000 MB. See Figure 2.

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

#. Go to :ref:`multi-boot-restore-bl` to restore Systemd-Boot and add
   Windows to its boot menu.

   .. note::

      At this point you cannot boot |CL| because Windows is now the
      default boot loader.


If you want to install other :abbr:`OSes (operating systems)`, refer to
:ref:`multi-boot` for details.


.. _Microsoft Windows Server 2019: https://www.microsoft.com/en-us/cloud-platform/windows-server