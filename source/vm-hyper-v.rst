.. _vm-hyper-v:

Using Hyper-V
#############

This section explains how to run Clear Linux inside
`Windows Server Virtualization`_  *A.K.A.* **Hyper-V** environment.


Install Hyper-V
===============

Please refer to `Microsoft documentation`_ to install and configure
*Hyper-V* on your machine.


Create a virtual machine
========================

1. Download the latest_ Clear Linux live version (clear-XXXX-live.img.xz)
   from https://download.clearlinux.org/image/.

2. Decompress Clear Linux image (you can use 7zip_). Uncompressed image
   size is ~ **5GiB**.

3. To convert Clear Linux raw image to :abbr:`VHD (Virtual Hard Disk)`
   format, you need to use VirtualBox_ or QEMU_ (windows version available on
   internet)

   *  Using *VirtualBox* you can use one of the following commands::

         VBoxManage convertfromraw clear-XXXX-live.img clear-XXXX-live.vhd --format VHD

      or::

         vbox-img convert --srcfilename clear-XXXX-live.img --dstfilename clear-XXXX-live.vhd --srcformat raw --dstformat vhd

   *  Using *QEMU* you can use the following command::

         qemu-img convert -f raw -O vpc clear-XXXX-live.img clear-XXXX-live.vhd

   You can test your new *VHD image* using the **PowerShell** command line with::

         PS C:\> Test-VHD -Path c:\path\to\clear-XXXX-live.vhd

   Clear Linux uses *EFI* to boot, and this featue is only availible in `Generation 2`_
   virtual machines, so, you need to convert from **VHD** to **VHDX**, to do this
   you can use the following *PowerShell* command::

         PS C:\> Convert-VHD -Path c:\path\to\clear-XXXX-live.vhd -DestinationPath c:\path\to\clear-XXXX-live.vhdx

   You can save the new *VHDX* virtual hard disk in :file:`C:\\Users\\Public\\Documents\\Hyper-V\\Virtual Hard Disks`.

4. Create virtual machine using the **Hyper-V Manager**:

   * Choose **Generation 2** when you need to *specify VM generation*.
   * Choose **Use an existing virtual hard disk** and browse to find the :file:`clear-XXXX-live.vhdx` file.

5. Connect to your new VM and start it.

   You will see a prompt asking for a user, use:

       * User: root
       * A new password will be asked for user root


.. _Windows Server Virtualization: https://www.microsoft.com/en-us/server-cloud/solutions/virtualization.aspx
.. _Microsoft documentation: https://www.microsoft.com/en-us/server-cloud/solutions/virtualization.aspx
.. _latest: https://download.clearlinux.org/latest
.. _7zip: http://www.7-zip.org/
.. _VirtualBox: https://www.virtualbox.org/
.. _QEMU: http://wiki.qemu.org/Links
.. _Generation 2: https://technet.microsoft.com/en-us/library/dn282285.aspx
