.. _proxmox:

|CL-ATTR| on Proxmox\* Virtual Environment 
##########################################

This guide explains how to create a new VM in Proxmox VE 6.1-3, install and run |CL| on as a guest OS.

.. contents::
   :local:
   :depth: 1

Prerequisites
*************

* Proxmox VE 6.1-3 server already set up and you have familiarity with how 
  to use it.

Download the Latest |CL| Live Server Image
******************************************

#. Visit our `Downloads`_ page.

#. Download the file :file:`clear-<release number>-live-server.iso`,
   also called the |CL| Server.

   .. note::

      <release-number> is the latest |CL| auto-numbered release.

Upload |CL| Live Server Image to Promox Server
**********************************************

#. Connect to your Proxmox server and log into an account with sufficient
   permission to create and manage VMs.

#. Under the :guilabel:`Server View` window, select the :guilabel:`local` 
   storage.  See Figure 1.

#. On the right window, click :guilabel:`Upload`.

   .. figure:: ../../_figures/proxmox/proxmox-01.png
      :scale: 100%
      :alt: Proxmox - Upload ISO

      Figure 1: Proxmox - Upload ISO

#. Set the :guilabel:`Content` as `ISO image`. See Figure 2.

#. Click :guilabel:`Select File...` and select the |CL| ISO.

#. Click :guilabel:`Upload`.

   .. figure:: ../../_figures/proxmox/proxmox-02.png
      :scale: 100%
      :alt: Proxmox - Select ISO to upload

      Figure 2: Proxmox - Select ISO to upload

   The ISO should now appear in the :guilabel:`Content` list.  See Figure 3.

   .. figure:: ../../_figures/proxmox/proxmox-03.png
      :scale: 100%
      :alt: Proxmox - Content list

      Figure 3: Proxmox - Content list

Create VM on Proxmox 
********************

#. Under the :guilabel:`Server View` window, select your Proxmox node.
   See Figure 4.

#. On the right window, click :guilabel:`Create VM`.

   .. figure:: ../../_figures/proxmox/proxmox-04.png
      :scale: 100%
      :alt: Proxmox - Create VM

      Figure 4: Proxmox - Create VM

#. In the :guilabel:`General` tab:
   | See Figure 5.
  
   a. Check the :guilabel:`Advanced` checkbox. 
 
   #. In the :guilabel:`Name` field, give the VM a name.

   .. figure:: ../../_figures/proxmox/proxmox-05.png
      :scale: 100%
      :alt: Proxmox - Create VM - General settings

      Figure 5: Proxmox - Create VM - General settings

#. In the :guilabel:`OS` tab:
   See Figure 6.

   a. Select :guilabel:`Use CD/DVD disc image file (iso)`.
   
   #. For :guilabel:`Storage`, select :guilabel:`local`.

   #. For :guilabel:`ISO image`, select the |CL| ISO you uploaded earlier.

   #. Set the :guilabel:`Type` to :guilabel:`Linux`.
  
   #. Set the :guilabel:`Version` to :guilabel:`5.x - 2.6 kernel`.

   .. figure:: ../../_figures/proxmox/proxmox-06.png
      :scale: 100%
      :alt: Proxmox - Create VM - OS settings

      Figure 6: Proxmox - Create VM - OS settings

#. In the :guilabel:`System` tab:
   See Figure 7.
   
   a. For :guilabel:`BIOS`, select :guilabel:`OVMF (UEFI)`.
   
   #. For :guilabel:`Storage`, select an appropriate location.
   
   #. For :guilabel:`Machine`, select :guilabel:`q35`.

   .. figure:: ../../_figures/proxmox/proxmox-07.png
      :scale: 100%
      :alt: Proxmox - Create VM - System settings

      Figure 7: Proxmox - Create VM - System settings

#. In the :guilabel:`Hard Disk` tab:
   See Figure 8.
   
   a. For :guilabel:`Disk size (GiB)`, set the desired disk size for your VM.  
      A minimum of 4GB is required for |CL|.   

   .. figure:: ../../_figures/proxmox/proxmox-08.png
      :scale: 100%
      :alt: Proxmox - Create VM - Hard Disk settings

      Figure 8: Proxmox - Create VM - Hard Disk settings

#. In the :guilabel:`CPU` tab:
   See Figure 9.

   a. Set the :guilabel:`Type` to :guilabel:`host`.

   #. For the :guilabel:`Extra CPU Flags`, scroll to the bottom and turn on the 
      :guilabel:`aes` setting by clicking the :guilabel:`+` radio button.

   .. figure:: ../../_figures/proxmox/proxmox-09.png
      :scale: 100%
      :alt: Proxmox - Create VM - CPU settings

      Figure 9: Proxmox - Create VM - CPU settings

#. In the :guilabel:`Memory` tab:
   See Figure 10.

   a. For :guilabel:`Memory (MiB)`, set a desired value.

   .. figure:: ../../_figures/proxmox/proxmox-10.png
      :scale: 100%
      :alt: Proxmox - Create VM - Memory settings

      Figure 10: Proxmox - Create VM - Memory settings

#. In the :guilabel:`Network` tab:
   See Figure 11.

   a. For :guilabel:`Model`, select :guilabel:`E1000`.

   .. figure:: ../../_figures/proxmox/proxmox-11.png
      :scale: 100%
      :alt: Proxmox - Create VM - Network settings

      Figure 11: Proxmox - Create VM - Network settings

#. In the :guilabel:`Confirm` tab:
   See Figure 12.

   a. Confirm the settings.

   #. Click :guilabel:`Finish` to create the VM.  The new VM should appear 
      under the :guilabel:`Server View` window.  
   
   .. figure:: ../../_figures/proxmox/proxmox-12.png
      :scale: 100%
      :alt: Proxmox - Create VM - Confirm settings

      Figure 12: Proxmox - Create VM - Confirm settings

Start VM and Install |CL| on Promox
***********************************

#. Under the :guilabel:`Server View` window, select your newly-created VM.
   See Figure 13.

#. On the right window, click :guilabel:`Start`.

#. Click :guilabel:`Console` button to bring up a console and interact with it.

   .. figure:: ../../_figures/proxmox/proxmox-13.png
      :scale: 100%
      :alt: Proxmox - Start VM

      Figure 13: Proxmox - Start VM

#. Follow the instructions in the :ref:`bare-metal-install-server` guide 
   starting at the `Launch the Clear Linux OS Installer` section.

.. _Downloads: https://clearlinux.org/downloads
