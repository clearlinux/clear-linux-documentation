.. _vm-vmware-player:

=======================================
Clear Linux on VMware* Player
=======================================

This section explains how to run Clear Linux inside
`VMWare Player`_ environment.

Install VMware player
---------------------

*VMware Workstation Player*, formerly VMware Player, is a virtualization
software package for x64 computers running Microsoft Windows or Linux. To 
download VMware player, you can click on the following link:
https://www.vmware.com/products/player/playerpro-evaluation.html

Player on Linux
^^^^^^^^^^^^^^^

If you have chosen Linux option, you got a :file:`VMWARE_FILE.bundle` file. To
install VMWare Player, run:

::

  $ sudo bash ./VMware-Player-12.0.0-2985596.x86_64.bundle

Player on windows
^^^^^^^^^^^^^^^^^

Please follow the instructions from the Setup Assistant

Prepare Clear Linux Image
-------------------------

Download the latest_ Clear Linux live disk image  from
https://download.clearlinux.org/image/. In  Clear Linux website you can find
different image flavors (kvm, clear-containers, cloud and live), please
download the live image (clear-XXXX-live.img.xz).

1. Decompress the image:

  - On Linux ::

        $ unxz clear-VERSION-live.img.xz

  - On Windows

        You can use 7zip_.

2. Convert installer to :abbr:`VMDK (Virtual Machine Disk)` format.

  - On linux

    Convert Clear Linux raw installer image in vmdk virtual disk, for doing
    this there are a lot of tools, this is an option:

    ::

      $ qemu-img convert -O vmdk clear-VERSION-live.img clear.vmdk

  - On Windows

    To convert live image to vmdk format ( from raw format to vmdk) you can
    use different tools for this purpose (e.g., VBoxManage from VirtualBox_).


Run Clear Linux* using VMware* Player
-------------------------------------


Create a new Virtual Machine
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Click on “Create a new Virtual Machine”

1. Select “**I will install the operating system later**”, and click on “Next”.

2. Select “**Linux**” as “Guest operating system” and version “**Other Linux 3.x
   kernel 64-bit**”.

3. Type a name for the new virtual machine.

4. Perform the *remaining steps* using the default options.

Change boot type to EFI 
^^^^^^^^^^^^^^^^^^^^^^^

You must change VMware virtual machine *configuration* to
**support efi firmware**, by editing a configuration .vmx file,
that is located in the virtual machine folder, and add the next line:

::

  firmware = "efi"

Attach Clear Linux image as SATA disk
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When you have created a new virtual machine, you can edit its configuration:

1. Click on “Edit virtual machine settings”

2. Remove any default attached hard disk

3. Click on “Add” option below devices list tab and choose Hard disk.

  i. Choose “SATA” as virtual disk type.

    - Use the  existing Clear Linux* virtual disk

The  Clear Linux live disk must set as “SATA 0:1 Hard Disk (SATA)” you can
verify it in “Advanced button” in the disk settings



Start the virtual machine
-------------------------

After the above configuration start the virtual machine.

.. _VMWare Player: http://www.vmware.com/products/player/
.. _latest: https://download.clearlinux.org/latest
.. _7zip: http://www.7-zip.org/
.. _VirtualBox: https://www.virtualbox.org/

