.. _vm-virtualbox:

================
Using VirtualBox
================

This section explains how to run Clear Linux inside
VirtualBox_ environment.

Download VirtualBox
-------------------

Virtualbox is a hypervisor supported by *Oracle**, you can
download it from its official site
https://www.virtualbox.org/wiki/Downloads
and select the operating system you are using,
furthermore you can download its source code. At this point is very
important to download **version 5.0 or grather**, this is in order to
get support for :abbr:`AVX (Advanced Vector Extensions)` feature
that is used in Clear Linux.


Create a virtual machine in VirtualBox
--------------------------------------

1. Download the latest_ Clear linux live version (clear-XXXX-live.img.xz)
   from https://download.clearlinux.org/image/.

2. Decompress Clear Linux image. Uncompressed image size is ~ **5GiB**.

   - On Linux ::

       $ xz -d clear-XXXX-live.img.xz

   - On Windows

      You can use 7zip_.

3. To convert Clear Linux raw image to :abbr:`VDI (VirtualBox Disk Image)`
   format, you can use one of the following commands::

      $ VBoxManage convertfromraw clear-XXXX-live.img clear-XXXX-live.vdi --format VDI

   or::

      $ vbox-img convert --srcfilename clear-XXXX-live.img --dstfilename clear-XXXX-live.vdi --srcformat raw --dstformat vdi


   Note: Be sure you have Virtual box directory in your PATH (i.e.: on Windows
   :file:`C:\\Program Files\\Oracle\\VirtualBox`)

4. Create virtual machine using the VirtualBox assistant:

   * Type: **Linux**
   * Version: **Linux 2.6 / 3.x / 4.x (64-bit)**
   * Attach the virtual disk created in the step number 3 as virtual hard disk file

5. Once it is created, go to settings to enable **EFI support**

   * System -> Enable EFI (special OSes only)

Run your new VM
---------------

Clear Linux comes with VirtualBox kernel modules in a bundle. You can install
these modules using

.. code:: bash

  # swupd bundle-add virtualbox-guest

In order to use the VirtualBox additions it's necessary to load vboxsf module

.. code:: bash

  # modprobe vboxsf

.. _VirtualBox: https://www.virtualbox.org/
.. _latest: https://download.clearlinux.org/latest
.. _7zip: http://www.7-zip.org/

