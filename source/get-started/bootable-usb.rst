.. _bootable-usb:

Create a bootable USB drive using Etcher*
#########################################

Use Etcher* software, an open source project from Balena*, to flash a |CL| image to a USB drive on macOS*, Linux\*, or Windows* operating systems. 

Prerequisites
*************

* Download the |CL| Desktop or Server image from the `Downloads`_ page
* Recommended minimum **4GB** USB drive or larger
* Download and install `Etcher`_

* Make sure you completed all `Prerequisites`_.

Burn the |CL| image onto a USB drive
====================================

.. caution::

   Burning an image formats the USB drive and destroys all pre-existing
   content.  Back up your data before proceeding.

#. Launch Etcher.

   .. figure:: /_figures/bootable-usb/balenaEtcher_Start.PNG
      :scale: 100%
      :alt: Start screen
         
      Figure 1: Start screen
 
#. Press :guilabel:`Select Image`.

#. Change directory to where the image resides.

#. Select the image and click :guilabel:`Open`.

   .. figure:: /_figures/bootable-usb/balenaEtcher_ImageSelect.PNG
      :scale: 100%
      :alt: In Open, select the image
         
      Figure 2: In Open, select the image

#. Plug in the USB drive.

#. Identify the USB drive or click :guilabel:`Change` to select a 
   different USB.
    
   .. note::

      This shows all USB drives attached to the system.

   .. figure:: /_figures/bootable-usb/balenaEtcher_DriveSlect.PNG
      :scale: 100%
      :alt: USB drives attached
         
      Figure 3: USB drives attached

#. Select the proper device and press :guilabel:`Continue`.

   .. figure:: /_figures/bootable-usb/balenaEtcher_ReadyToFlash.PNG
      :scale: 100%
      :alt: USB Flash Device selected
      
      Figure 4: USB Flash Device selected

#. When ready Press the :guilabel:`Flash!` Button.

#. The dialog shows :guilabel:`Flashing` while in progress.

   .. figure:: /_figures/bootable-usb/balenaEtcher_StartingToFlash.PNG
      :scale: 100%
      :alt: Starting to flash

      Figure 5: Starting to flash

#. Flashing in progress.

   .. figure:: /_figures/bootable-usb/balenaEtcher_Flashing.PNG
      :scale: 100%
      :alt:  Flashing, percentage complete
      
      Figure 6: Flashing, percentage complete

#. :guilabel:`Flash complete` shows when the process is finished.

   .. figure:: /_figures/bootable-usb/balenaEtcher_Done.PNG
      :scale: 100%
      :alt: Flash Complete!
      
      Figure 7: Flash Complete!

   .. note::

      The process may take more than a few minutes. When the process completes, close BalenaEtcher.
      
Ejecting the |CL| image USB drive
=================================

.. caution::

   If you do not properly unmount the USB drive before removing it, it may cause file system checksum errors in it. If this happens, burn the image again, ensuring all the USB drive partitions are unmounted first before removing drive.

#. Unmount the USB per your OS instructions. 

#. Then eject the USB. 
   
.. _Downloads: https://clearlinux.org/downloads
.. _Etcher: https://www.balena.io/etcher/
