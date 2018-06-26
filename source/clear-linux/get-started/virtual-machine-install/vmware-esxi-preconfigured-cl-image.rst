.. _vmware-esxi-preconfigured-cl-image:

Run preconfigured Clear Linux image as a VMware\* ESXi guest OS
###############################################################

`VMware ESXi`_ is a type 1 bare-metal hypervisor which runs directly on top
of server hardware.  With VMware ESXi, you can create, configure, manage,
and run |CLOSIA| virtual machines at scale.

This section shows you how to deploy a preconfigured |CL| VMware image on
VMware ESXi 6.5.

If you would prefer to perform a manual installation of |CL| into a new VMware
ESXi :abbr:`VM (Virtual Machine)` instead, see :ref:`vmware-esxi-install-cl`.
Visit :ref:`image-types` to learn more about the available images.


.. note::

   VMware also offers a type 2 hypervisor called `VMware Workstation Player`_ which is designed for the desktop environment.
   See :ref:`vmw-player-preconf` or see :ref:`vmw-player`.


.. contents:: 
    :depth: 2


Download the latest Clear Linux VMware image
********************************************

Get the latest |CL| VMware prebuilt image from the `image`_ repository.
Look for :file:`clear-[version number]-vmware.vmdk.xz`. You can also use
this command: 

.. code-block:: bash

   curl -O https://download.clearlinux.org/image/clear-$(curl https://download.clearlinux.org/latest)-vmware.vmdk.xz

.. include:: ../../guides/maintenance/download-verify-uncompress-linux.rst
   :Start-after: verify-linux:
   :end-before: To uncompress a GZ

For alternative instructions on other operating systems, see:

* :ref:`download-verify-uncompress-mac`
* :ref:`download-verify-uncompress-windows`

Upload the Clear Linux image to the VMware server
*************************************************

Once the |CL| VMware prebuilt image has been downloaded and 
uncompressed on your local system, it must be uploaded to a datastore 
on the VMware ESXi server.

The steps in this section can also be referenced from the `VMware documentation on Using the Datastore File Browser`_ 

#.  Connect to the VMware ESXi server and login to an account with sufficient
    permission to create and manage VMs.

#.  Under the :guilabel:`Navigator` window on the left side, 
    select :guilabel:`Storage`.
    See Figure 1

#.  Under the :guilabel:`Datastores` tab, click 
    the :guilabel:`Datastore browser` button.

    .. figure:: figures/vmware-esxi/vmware-esxi-preconfigured-cl-image-1.png
      :scale: 100 %
      :alt: VMware ESXi - Navigator > Storage

      Figure 1: VMware ESXi - Navigator > Storage

#.  Click the :guilabel:`Create directory` button and name the directory
    `Clear Linux VM`. See Figure 2.

    .. figure:: figures/vmware-esxi/vmware-esxi-preconfigured-cl-image-2.png
      :scale: 100 %
      :alt: VMware ESXi - Datastore > Create directory

      Figure 2: VMware ESXi - Datastore > Create directory

#.  Select the newly-created directory and click the :guilabel:`Upload`
    button. See Figure 3.

    .. figure:: figures/vmware-esxi/vmware-esxi-preconfigured-cl-image-3.png
      :scale: 100 %
      :alt: VMware ESXi - Datastore > Upload VMware image

      Figure 3: VMware ESXi - Datastore > Upload VMware image

#.  Select the uncompressed |CL| VMware image file
    :file:`clear-[version number]-vmware.vmdk` and upload it.

Convert the Clear Linux image to an ESXi-supported format
*********************************************************

Once the |CL| VMware prebuilt image has been uploaded to the VMware ESXi datastore, 
it must be converted to a format for usable with VMware's ESXi hypervisor. 

The steps in this section can also be referenced from the `VMware documentation on Cloning and converting virtual machine disks with vmkfstools`_

#.  SSH into the `vSphere Management Assistant`_  appliance that is managing the ESXi host or connect to the vSphere hosting using the `vSphere CLI`_. 
    
    .. note::
        If there is no :abbr:`vMA (vSphere Management Assistant)` appliance or :abbr:`vCLI (vSphere CLI)` configured and available, 
        you can temporarily enable SSH directly on the ESXi host by referencing
        the `VMware documentation on Enable the Secure Shell (SSH)`_ .

        As a security best practice, remember to disable SSH access after following the steps in this section. 


#.  Locate the uploaded image, which is typically found in
    :file:`/vmfs/volumes/datastore1`.

#.  Use the :command:`vmkfstools` command to perform the conversion, as
    shown below:

    .. code-block:: console

       vmkfstools -i clear-[version number]-vmware.vmdk -d zeroedthick clear-[version number]-esxi.vmdk

    Two files should result from this:

    * :file:`clear-[version number]-esxi-flat.vmdk`
    * :file:`clear-[version number]-esxi.vmdk`

    The :file:`clear-[version number]-esxi.vmdk` file will be used in the
    next section when you create a new VM.



Create and configure a new VM
*****************************

In this section, you will create a new VM, configure its basic parameters
such as number of CPUs, memory size, and then attach the converted |CL| 
VMware image. Also, in order to boot |CL|, you must enable UEFI support. 

#.  Under the :guilabel:`Navigator` window, select 
    :guilabel:`Virtual Machines`. See Figure 4.

#.  In the right window, click the :guilabel:`Create / Register VM` button.

    .. figure:: figures/vmware-esxi/vmware-esxi-preconfigured-cl-image-4.png
      :scale: 100 %
      :alt: VMware ESXi - Navigator > Virtual Machines

      Figure 4: VMware ESXi - Navigator > Virtual Machines

#.  On the :guilabel:`Select creation type` step:

    #.  Select the :guilabel:`Create a new virtual machine` option. See
        Figure 5.

    #.  Click the :guilabel:`Next` button.

        .. figure:: figures/vmware-esxi/vmware-esxi-preconfigured-cl-image-5.png
          :scale: 100 %
          :alt: VMware ESXi - Create a new virtual machine

          Figure 5: VMware ESXi - Create a new virtual machine

#.  On the :guilabel:`Select a name and guest OS` step:

    #.  Give the new VM a name in the :guilabel:`Name` field. See Figure 6.
    #.  Set the :guilabel:`Compatability` option to :guilabel:`ESXi 6.5 virtual machine`.
    #.  Set the :guilabel:`Guest OS family` option to :guilabel:`Linux`.
    #.  Set the :guilabel:`Guest OS version` option to :guilabel:`Other 3.x or later Linux (64-bit)`.
    #.  Click the :guilabel:`Next` button.

        .. figure:: figures/vmware-esxi/vmware-esxi-preconfigured-cl-image-6.png
          :scale: 100 %
          :alt: VMware ESXi - Give a name and select guest OS type

          Figure 6: VMware ESXi - Give a name and select guest OS type

#.  On the :guilabel:`Select storage` step:

    #.  Accept the default option.
    #.  Click the :guilabel:`Next` button.

#.  On the :guilabel:`Customize settings` step:

    #.  Click the :guilabel:`Virtual Hardware` button. See Figure 7.
    #.  Expand the :guilabel:`CPU` setting and enable :guilabel:`Hardware virtualization` by
        checking :guilabel:`Expose hardware assisted virtualization to the guest OS`.

        .. figure:: figures/vmware-esxi/vmware-esxi-preconfigured-cl-image-7.png
          :scale: 100 %
          :alt: VMware ESXi - Enable hardware virtualization

          Figure 7: VMware ESXi - Enable hardware virtualization

    #.  Remove the default :guilabel:`Hard drive 1` setting by clicking
        the `X` icon on the right side. See Figure 8.

        .. figure:: figures/vmware-esxi/vmware-esxi-preconfigured-cl-image-8.png
          :scale: 100 %
          :alt: VMware ESXi - Remove hard drive

          Figure 8: VMware ESXi - Remove hard drive

    #.  Since a preconfigured image will be used, 
        the :guilabel:`CD/DVD Drive 1` setting will not be needed.  Disable it by unchecking the :guilabel:`Connect` checkbox. See Figure 9.

        .. figure:: figures/vmware-esxi/vmware-esxi-preconfigured-cl-image-9.png
          :scale: 100 %
          :alt: VMware ESXi - Disconnect the CD/DVD drive

          Figure 9: VMware ESXi - Disconnect the CD/DVD drive

    #.  Attach the :file:`clear-[version number]-esxi.vmdk` file that was
        converted from the preconfigured |CL| VMware image.

        #.  Click the :guilabel:`Add hard disk` button and select the
            :guilabel:`Existing hard drive` option. See Figure 10.

            .. figure:: figures/vmware-esxi/vmware-esxi-preconfigured-cl-image-10.png
              :scale: 100 %
              :alt: VMware ESXi - Add an existing hard drive

              Figure 10: VMware ESXi - Add an existing hard drive

        #.  Select the converted :file:`clear-[version number]-esxi.vmdk`
            file. Do not use the original unconverted :file:`clear-[version number]-vmware.vmdk` file. See Figure 11.

            .. figure:: figures/vmware-esxi/vmware-esxi-preconfigured-cl-image-11.png
              :scale: 100 %
              :alt: VMware ESXi - Select the converted `vmdk` file

            Figure 11: VMware ESXi - Select the converted :file:`clear-[version number]-esxi.vmdk` file

#.  |CL| needs UEFI support in order to boot.  Enable UEFI boot support.

    #.  Click the :guilabel:`VM Options` button. See Figure 12.
    #.  Expand the :guilabel:`Boot Options` setting.
    #.  For the :guilabel:`Firmware` setting, click the drop-down list to
        the right of it and select the :guilabel:`EFI` option.

        .. figure:: figures/vmware-esxi/vmware-esxi-preconfigured-cl-image-12.png
          :scale: 100 %
          :alt: VMware ESXi - Set boot firmware to EFI

          Figure 12: VMware ESXi - Set boot firmware to EFI

#.  Click the :guilabel:`Save` button.
#.  Click the :guilabel:`Next` button.
#.  Click the :guilabel:`Finish` button.

Power on the VM and boot Clear Linux
************************************

After configuring the settings above, power on the VM.

#.  Under the :guilabel:`Navigator` window, select :guilabel:`Virtual Machines`. See Figure 13.
#.  In the right window, select the newly-created VM.
#.  Click the :guilabel:`Power on` button.
#.  Click on the icon representing the VM to bring it into view and maximize
    its window.

    .. figure:: figures/vmware-esxi/vmware-esxi-preconfigured-cl-image-13.png
      :scale: 100 %
      :alt: VMware ESXi - Navigator > Virtual Machines > Power on VM

      Figure 13: VMware ESXi - Navigator > Virtual Machines > Power on VM

Also see:
---------

* :ref:`vmware-esxi-install-cl`

.. _VMware ESXi: https://www.vmware.com/products/esxi-and-esx.html
.. _`VMware documentation on Using the Datastore File Browser`: https://docs.vmware.com/en/VMware-vSphere/6.7/com.vmware.vsphere.html.hostclient.doc/GUID-7533A767-8396-4844-A3F2-206047D254EA.html
.. _`vSphere Management Assistant`: https://www.vmware.com/support/developer/vima/
.. _`vSphere CLI`: https://www.vmware.com/support/developer/vcli/
.. _`VMware documentation on Cloning and converting virtual machine disks with vmkfstools`: https://kb.vmware.com/kb/1028042 
.. _`VMware documentation on Enable the Secure Shell (SSH)`: https://docs.vmware.com/en/VMware-vSphere/6.7/com.vmware.vsphere.html.hostclient.doc/GUID-B649CB74-832F-467B-B6A4-8BA67AD5C1F0.html
.. _`VMware documentation on General ESXi Security Recommendations`: https://docs.vmware.com/en/VMware-vSphere/6.7/com.vmware.vsphere.security.doc/GUID-B39474AF-6778-499A-B8AB-E973BE6D4899.html
.. _VMware Workstation Player: https://www.vmware.com/products/workstation-player.html
.. _image: https://download.clearlinux.org/image
