.. _bootable-usb:

Create a bootable USB drive using Etcher\*
##########################################

Use Etcher* software from Balena\* to flash the |CL| image to a USB drive. 
An `Advanced: Linux CLI`_ option is also available.

Prerequisites
*************

* Download the |CL| Desktop or Server image from the `Downloads`_ page
* Recommended minimum **4GB** USB drive or larger
* Download and install the `Etcher`_ version per your operating system.

Burn the |CL| image onto a USB drive
====================================

.. caution::

   Burning an image formats the USB drive and destroys all pre-existing
   content.  Back up your data before proceeding.

#. Launch Etcher.

   .. rst-class:: dropshadow

   .. figure:: /_figures/bootable-usb/balenaEtcher_Start.PNG
      :scale: 100%
      :alt: Start screen
         
      Figure 1: Start screen
 
#. Press :guilabel:`Select Image`.

#. Change directory to where the image resides.

#. Select the image and click :guilabel:`Open`.

   .. rst-class:: dropshadow

   .. figure:: /_figures/bootable-usb/balenaEtcher_ImageSelect.PNG
      :scale: 100%
      :alt: In Open, select the image
         
      Figure 2: In Open, select the image

#. Plug in the USB drive.

#. Identify the USB drive or click :guilabel:`Change` to select a 
   different USB.
    
   .. note::

      This shows all USB drives attached to the system.

   .. rst-class:: dropshadow

   .. figure:: /_figures/bootable-usb/balenaEtcher_DriveSlect.PNG
      :scale: 100%
      :alt: USB drives attached
         
      Figure 3: USB drives attached

#. Select the proper device and press :guilabel:`Continue`.

   .. rst-class:: dropshadow

   .. figure:: /_figures/bootable-usb/balenaEtcher_ReadyToFlash.PNG
      :scale: 100%
      :alt: USB Flash Device selected
      
      Figure 4: USB Flash Device selected

#. When ready press the :guilabel:`Flash!` Button. 
   The dialog shows :guilabel:`Flashing` while in progress.

   .. rst-class:: dropshadow

   .. figure:: /_figures/bootable-usb/balenaEtcher_StartingToFlash.PNG
      :scale: 100%
      :alt: Starting to flash

      Figure 5: Starting to flash

   .. rst-class:: dropshadow

   .. figure:: /_figures/bootable-usb/balenaEtcher_Flashing.PNG
      :scale: 100%
      :alt:  Flashing, percentage complete
      
      Figure 6: Flashing, percentage complete

#. :guilabel:`Flash complete!` shows when the process is finished.

   .. rst-class:: dropshadow

   .. figure:: /_figures/bootable-usb/balenaEtcher_Done.PNG
      :scale: 100%
      :alt: Flash Complete!
      
      Figure 7: Flash Complete!

   .. note::

      The process may take more than a few minutes. When the process completes, close BalenaEtcher.
      
Advanced: Linux CLI
===================

#. Open a Terminal window.

#. Change directory to where the image resides. 

#. Plug in the USB drive.  

#. Identify all drives attached to the system. In the example output below, there are 3 drives (`/dev/sda`, `/dev/sdb`, and `/dev/sdc`) attached, where `/dev/sda` is the primary drive and the remaining are USB drives.   

   .. code-block:: bash 

      lsblk -po NAME,SIZE,VENDOR,MODEL,TRAN,TYPE,PARTLABEL,MOUNTPOINT 
   
   Example output:   

   .. code-block:: console 

      NAME          SIZE VENDOR   MODEL                    TRAN   TYPE PARTLABEL                    MOUNTPOINT 
      /dev/sda    119.2G ATA      SAMSUNG_MZ7PC128HAFU-000 sata   disk                                
      ├─/dev/sda1   450M                                          part Basic data partition           
      ├─/dev/sda2   100M                                          part EFI system partition           
      ├─/dev/sda3    16M                                          part Microsoft reserved partition   
      ├─/dev/sda4  97.2G                                          part Basic data partition           
      ├─/dev/sda5   142M                                          part EFI                            
      ├─/dev/sda6   245M                                          part linux-swap                   [SWAP]  
      └─/dev/sda7  21.1G                                          part /                            / 
      /dev/sdb      7.5G General  UDisk                    usb    disk                                
      └─/dev/sdb1   7.5G                                          part Microsoft Basic Data         /run/media/clear/CENA_X64FRE 
      /dev/sdc       15G          Patriot_Memory           usb    disk                                
      └─/dev/sdc1    15G                                          part                              /run/media/clear/U  

   .. note::   

      Some Linux distros may automatically mount a USB drive when it is plugged in. 

#. Unmount the USB drive you want to use before burning an image onto it.
   Use the :command:`umount` command followed by the device identifier/partition. For example, to unmount all ``/dev/sdc`` partitions:   

   .. code-block:: bash 

      sudo umount /dev/sdc*   

#. Burn the image onto the USB drive. This example burns an image onto
   ``/dev/sdc``. The device name of the USB may vary.   

   .. code-block:: bash

      sudo dd if=./clear-[version number]-live-[desktop | server].iso of=/dev/sdc oflag=sync bs=4M status=progress

Eject the |CL| image USB drive
==============================

.. caution::

   If you do not properly unmount the USB drive before removing it, it may cause file system checksum errors in it. If this happens, burn the image again, ensuring all the USB drive partitions are unmounted first before removing drive.

#. Unmount the USB per your OS instructions. 

#. Then eject the USB. 
   
.. _Downloads: https://clearlinux.org/downloads
.. _Etcher: https://www.balena.io/etcher/
