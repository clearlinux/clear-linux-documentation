.. _vm-virtualbox:

Using VirtualBox
################

This section explains how to run Clear Linux inside a `VirtualBox`_
environment.

Download VirtualBox
===================

VirtualBox is a hypervisor supported by *Oracle**. You can
download it from the `official VirtualBox website`_ and select
the operating system you are using.

Download **version 5.0 or greater** to ensure support for
the :abbr:`AVX (Advanced Vector Extensions)` needed to run
Clear Linux.


Create a virtual machine in VirtualBox
======================================

#. Download the `latest`_ live version of Clear Linux (clear-XXXX-live.img.xz)
   from https://download.clearlinux.org/image/.

#. Decompress the downloaded image. Uncompressed image size is ~ **5GB**.

   - On Linux ::

       $ xz -d clear-XXXX-live.img.xz

   - On Windows you can use `7zip`_.

#. To convert a Clear Linux raw image to :abbr:`VDI (VirtualBox Disk Image)`
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

Clear Linux can support kernel modules for VirtualBox. Install the bundle
that supports these modules with::

  # swupd bundle-add virtualbox-guest

And to use the VirtualBox additions, load the ``vboxsf`` module::

  # modprobe vboxsf


.. _official VirtualBox website: https://www.virtualbox.org/wiki/Downloads
.. _VirtualBox: https://www.virtualbox.org/
.. _latest: https://download.clearlinux.org/image/
.. _7zip: http://www.7-zip.org/

