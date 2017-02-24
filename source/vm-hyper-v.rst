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

#. Download and uncompress the latest hyperv disk image (`clear-XXXX-hyperv.img.xz`) of Clear Linux OS
   for Intel Architecture from https://download.clearlinux.org/image/.

#. Create a virtual machine using the **Hyper-V Manager**:

   * Choose **Generation 2** when you need to *specify VM generation*.
   * Choose **Use an existing virtual hard disk** and browse to find the :file:`clear-XXXX-hyperv.vhdx` file.
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
