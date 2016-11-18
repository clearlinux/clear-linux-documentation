.. _vm-hyper-v:

Using Hyper-V
#############

This section explains how to run Clear Linux OS for Intel® Architecture
inside a `Windows Server Virtualization`_  *A.K.A.* **Hyper-V** environment.


Install Hyper-V*
================

Please refer to `Microsoft documentation`_ to install and configure
*Hyper-V* on your machine.


Create a virtual machine
========================

#. Download the `latest`_ live version (clear-XXXX-live.img.xz) of Clear Linux OS
   for Intel Architecture.

#. Decompress the downloaded image. Uncompressed image size is ~ **5GB**.

#. To convert a raw image to :abbr:`VHD (Virtual Hard Disk)`
   format, you can use VirtualBox_ or QEMU_.

   *  With *VirtualBox*, you can use one of the following commands::

         > VBoxManage convertfromraw clear-XXXX-live.img clear-XXXX-live.vhd --format VHD

      or::

         > vbox-img convert --srcfilename clear-XXXX-live.img --dstfilename clear-XXXX-live.vhd --srcformat raw --dstformat vhd

   *  With *QEMU*, you can use the following command::

         > qemu-img convert -f raw -O vpc clear-XXXX-live.img clear-XXXX-live.vhd

   You can test your new *VHD image* using the **PowerShell** command line::

         PS C:\> Test-VHD -Path c:\path\to\clear-XXXX-live.vhd

   Clear Linux OS for Intel Architecture uses *EFI* to boot.  Since this feature
   is availible only in `Generation 2`_ or later virtual machines, you'll need
   to convert from **VHD** to **VHDX**. To do this, you can use the following
   *PowerShell* command::

         PS C:\> Convert-VHD -Path c:\path\to\clear-XXXX-live.vhd -DestinationPath c:\path\to\clear-XXXX-live.vhdx

   You can save the new *VHDX* virtual hard disk in :file:`C:\\Users\\Public\\Documents\\Hyper-V\\Virtual Hard Disks`.

#. Create a virtual machine using the **Hyper-V Manager**:

   * Choose **Generation 2** when you need to *specify VM generation*.
   * Choose **Use an existing virtual hard disk** and browse to find the :file:`clear-XXXX-live.vhdx` file.
   * When finised, open VM settings, select Firmware Section and in Secure Boot
     config, **uncheck** Enable Secure Boot.

     +  Currently Clear Linux does not boot with secure boot enabled.

#. Finally, connect to your new VM and start it. You should see a prompt asking for
   a user; use::

      > User: root

   and set a root user password.

.. _Windows Server Virtualization: https://www.microsoft.com/en-us/server-cloud/solutions/virtualization.aspx
.. _Microsoft documentation: https://www.microsoft.com/en-us/server-cloud/solutions/virtualization.aspx
.. _latest: https://download.clearlinux.org/image/
.. _7zip: http://www.7-zip.org/
.. _VirtualBox: https://www.virtualbox.org/
.. _QEMU: http://wiki.qemu.org/Links
.. _Generation 2: https://technet.microsoft.com/en-us/library/dn282285.aspx
