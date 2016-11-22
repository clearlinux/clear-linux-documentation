.. _gs_installing_clr_as_host:

Installing the OS as host
#########################

Running Clear Linux* OS for Intel® Architecture natively on a system is
easy with the installer image. To get started you'll need the following:

* A USB stick flashed with the `installer image`_.  For instructions on how to
  do this, see :ref:`gs_creating_bootable_usb`.
* A host machine running :ref:`gs_supported_hardware`.
* Network access via DHCP.

Installing Clear Linux OS for Intel Architecture to a target system
===================================================================

#. Configure the BIOS; this may involve changing the priority of the boot 
   device to boot from USB port first. 
#. Insert the USB device that is flashed with the 
   `installer image`_ into the target system, then reboot. 
#. The installer user interface will appear. Once all appropriate configuration
   options have been chosen, the installer will install the OS.

The entire installation should take no more than a few minutes. 

For feedback on installation or other topics, please feel free to write in to our 
`mailing list`_.

Note: You can also try :ref:`vm-kvm`.

.. _installer image: http://download.clearlinux.org/image
.. _mailing list: https://lists.clearlinux.org/mailman/listinfo/dev
