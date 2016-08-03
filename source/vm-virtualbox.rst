.. _vm-virtualbox:

Using VirtualBox
################

This section explains how to run Clear Linux OS for Intel® Architecture
inside a `VirtualBox`_\* environment.

Download VirtualBox
===================

VirtualBox is a hypervisor supported by Oracle. You can
download it from the `official VirtualBox website`_ and select
the operating system you are using.

Download **version 5.0 or greater** to ensure support for
the :abbr:`AVX (Advanced Vector Extensions)` needed to run
Clear Linux OS for Intel Architecture.


Create a virtual machine in VirtualBox
======================================

#. Download the `latest`_ live version (clear-XXXX-live.img.xz)
   from https://download.clearlinux.org/image/.

#. Decompress the downloaded image. Uncompressed image size is ~ **5GB**.

   - On Linux ::

       $ xz -d clear-XXXX-live.img.xz

   - On Windows you can use `7zip`_.

#. To convert a raw image to :abbr:`VDI (VirtualBox Disk Image)`
   format, you can use one of the following commands::

      $ VBoxManage convertfromraw clear-XXXX-live.img clear-XXXX-live.vdi --format VDI

   or::

      $ vbox-img convert --srcfilename clear-XXXX-live.img --dstfilename clear-XXXX-live.vdi --srcformat raw --dstformat vdi


   Note: Be sure you have Virtual box directory in your PATH (i.e.: on Windows
   :file:`C:\\Program Files\\Oracle\\VirtualBox`).

#. Create a virtual machine using the VirtualBox assistant:

   * Type: **Linux**
   * Version: **Linux 2.6 / 3.x / 4.x (64-bit)**
   * Attach the virtual disk created in the step number 3 as virtual hard disk file

#. After it is created, go to settings to enable **EFI support**

   * System -> Enable EFI (special OSes only)


Run your new VM
===============

Clear Linux OS for Intel Architecture support VirtualBox kernel modules used
by the Linux kernel 4.4 :abbr:`LTS (Long Term Support)` (*kernel-lts bundle*).
This kernel was selected due to Clear Linux OS main kernel
(*kernel-native bundle*) keeps up-to-date with Linux Kernel upstream and
some times VirtualBox kernel modules doesn't fit in early days of a new
kernel release.

To install the VirtualBox kernel modules you should follow these steps:

#. Install the bundle that supports VirtualBox modules::

     # swupd bundle-add virtualbox-guest

#. Set a timeout in the bootmanager to shows a menu at boot time::

     # clr-boot-manager set-timeout 10

#. Update the bootloader entries with::

     # clr-boot-manager update

#. Reboot your system with::

     # reboot

   and choose LTS kernel version.

#. (*Optional*) Unset timeout to boot directly to LTS version::

     # clr-boot-manager set-timeout 0

#. (*Mandatory*) Update bootmanger to use always LTS version::

     # clr-boot-manager update



And to use the VirtualBox additions, load the ``vboxsf`` module::

  # modprobe vboxsf


.. _official VirtualBox website: https://www.virtualbox.org/wiki/Downloads
.. _VirtualBox: https://www.virtualbox.org/
.. _latest: https://download.clearlinux.org/image/
.. _7zip: http://www.7-zip.org/
