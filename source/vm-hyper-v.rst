.. _vm-hyper-v:

Using Hyper-V\*
###############

This section explains how to run |CLOSIA| inside a
`Windows Server Virtualization`_\* or **Hyper-V** environment.


Install Hyper-V
================

Please refer to the `Microsoft documentation`_ to install and configure
*Hyper-V* on your machine.


Create a virtual machine
========================

#. Download and uncompress the latest hyperv disk image :file:`clear-XXXX-
   hyperv.img.xz`) of |CLOSIA| from our `downloads`_ section.

#. Create a virtual machine using the **Hyper-V Manager**:

   #. Choose **Generation 2** when prompted to *specify VM generation*.
   #. Choose **Use an existing virtual hard disk** and browse to find the
      :file:`clear-XXXX-hyperv.vhdx` file.
   #. When finished, open VM settings, select Firmware Section and in Secure
      Boot config, **uncheck** Enable Secure Boot.

   .. note:: Currently, Clear Linux does not boot with :option:`secure boot`
      enabled.

#. Connect to your new VM and start it. You should see a prompt:

   .. code-block:: console

      > User: root

#. Set a root user password.

Your virtual machine running |CLOSIA| is ready!

.. _Windows Server Virtualization: https://www.microsoft.com/en-us/server-cloud/solutions/virtualization.aspx
.. _Microsoft documentation: https://www.microsoft.com/en-us/server-cloud/solutions/virtualization.aspx
.. _downloads: https://download.clearlinux.org/image/
.. _7zip: http://www.7-zip.org/
.. _VirtualBox: https://www.virtualbox.org/
.. _QEMU: http://wiki.qemu.org/Links
.. _Generation 2: https://technet.microsoft.com/en-us/library/dn282285.aspx
