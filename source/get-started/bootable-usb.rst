.. _bootable-usb:

Create a bootable USB drive using BalenaEtcher
##############################################

Prerequisites
*************

* Download the |CL| Desktop or Server image from the `Downloads`_ page
* Recommended minimum **4GB** USB drive or larger
* Download and install `BalenaEtcher`_

.. _bootable-usb-linux:

* Make sure you completed all `Prerequisites`_.

Burn the |CL| image onto a USB drive
====================================

.. caution::

   Burning an image formats the USB drive and destroys all pre-existing
   content.  Back up your data before proceeding.

#. Launch balenaEtcher.

   .. figure:: /_figures/bootable-usb/balenaEtcher_Start.PNG
      :scale: 100%
      :alt: BalenaEtcher Start
         
      Figure X: BalenaEtcher Start
 
#. Press :guilabel:`Select Image`.

#. Change directory to where the image resides.

#. Open the Image.

   .. figure:: /_figures/bootable-usb/balenaEtcher_ImgaeSlect.PNG
      :scale: 100%
      :alt: 
         
      Figure X: 

#. Plug in the USB drive.

#. Identify the USB drive using the :guilabel:`Change` under the middel icon.
    
   .. note::
      This shows all USB drives attached to the system.

   .. figure:: /_figures/bootable-usb/balenaEtcher_DriveSlect.PNG
      :scale: 100%
      :alt: 
         
      Figure X: 

#. Select the proper drive and press :guilabel:`Continue`.

   .. figure:: /_figures/bootable-usb/balenaEtcher_ReadyToFlash.PNG
      :scale: 100%
      :alt: 
      
      Figure X: 

#. When ready Press the  :guilabel:`Flash!` Button.

#. Flashing starting.

   .. figure:: /_figures/bootable-usb/balenaEtcher_StartingToFlash.PNG
      :scale: 100%
      :alt: 

      Figure X: 

#. Flashing in progress.

   .. figure:: /_figures/bootable-usb/balenaEtcher_Flashing.PNG
      :scale: 100%
      :alt: 
      
      Figure X: 

#. Flashing complete.

   .. figure:: /_figures/bootable-usb/balenaEtcher_Done.PNG
      :scale: 100%
      :alt: 
      
      Figure X: 

   .. note::
      The process can take more than a few minutes. When the process completes, close BalenaEtcher.
      

Ejecting the |CL| image USB drive
=================================

.. caution::

   Not fully unmounting the USB drive before removing the drive could cause
   file system checksum errors in it. If this happens, burn the image again,
   ensuring all the USB drive partitions are unmounted first befor removing drive.


#. Select the Windows taskbar menu for USB and select
   :guilabel:`Eject <drive name>`.
   
 
.. _Downloads: https://clearlinux.org/downloads
.. _BalenaEtcher: https://www.balena.io/etcher/
