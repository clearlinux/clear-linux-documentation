.. _vm-vmware-player:

Using *VMware* Player
#####################

This section explains how to run Clear Linux within a `VMWare Player`_
environment.

Install VMware player
=====================

*VMware Workstation Player*, formerly VMware Player, is a virtualization
software package for x64 computers running Microsoft Windows or Linux. Download
VMware player from the `VMware website`_.

Player on Linux
---------------

For the Linux option, you should have a ``VMware-Player-[version]_FILE.bundle`` file. To
install it, run:

::

  $ sudo bash ./VMware-Player-[version].x86_64.bundle

Player on Windows
-----------------

Follow the instructions from the Setup Assistant.


Prepare Clear Linux Image
=========================

#. Download the `latest`_ Clear Linux **live** disk image, named
   ``[clear-[version_number]-live.img.xz]``.

#. Decompress the Clear Linux image. Uncompressed image size ~ **5GB**.

   * On Linux ::

        $ unxz clear-VERSION-live.img.xz

   * On Windows you can use `7zip`_.

#. Convert the installer to :abbr:`VMDK (Virtual Machine Disk)` format.

   * On Linux, you can use ``qemu-img convert``::

      $ qemu-img convert -O vmdk clear-VERSION-live.img clear.vmdk

   * On Windows, you can convert the live image to vmdk format (from raw format to vmdk)
    with a tool like VBoxManage from `VirtualBox`_.


Run Clear Linux* using VMware* Player
=====================================


#. Create a new virtual machine.

#. Click on “Create a new Virtual Machine”.

   * Select “**I will install the operating system later**”, and click on “Next”.
   * Select “**Linux**” as “Guest operating system” and version **Other Linux 3.x kernel 64-bit**.
   * Type a name for the new virtual machine.
   * Perform the *remaining steps* using the default options.

#. Change boot type to EFI.  You must change the VMware virtual machine *configuration*
   to **Support EFI firmware**; you can do this by editing the configuration ``.vmx``
   file located in the virtual machine folder and adding the following line::

     firmware = "efi"

#. Attach the Clear Linux image as SATA disk.  And when you have a new virtual machine,
   edit its configuration as follows:

   * Click on “Edit virtual machine settings”.
   * Remove any default attached hard disk.
   * Click on “Add” option below devices list tab and choose Hard disk.

      * Choose **SATA** as the virtual disk type.
      * Use the  existing Clear Linux virtual disk

     The  Clear Linux live disk must set as ``SATA 0:1 Hard Disk (SATA)``; you can verify
     this under the “Advanced" section of the disk settings.

Start the virtual machine
=========================

After configuring the settings above, start the virtual machine.


.. _VMware website: https://www.vmware.com/products/player/playerpro-evaluation.html
.. _VMWare Player: http://www.vmware.com/products/player/
.. _latest: https://download.clearlinux.org/current/
.. _7zip: http://www.7-zip.org/
.. _VirtualBox: https://www.virtualbox.org/

