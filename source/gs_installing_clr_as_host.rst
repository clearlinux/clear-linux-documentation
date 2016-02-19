.. _gs_installing_clr_as_host:

Installing the OS as host
##########################################################

Running Clear Linux* OS for Intel® Architecture natively on a system is easy 
using the installer image. To get started you'll need the following:

* A USB stick flashed with the `installer image <http://download.clearlinux.org/image/>`_. 
  For instructions on how to do this, see :ref:`gs_creating_bootable_usb`.
* Host machine running :ref:`gs_supported_hardware`.
* Network access via DHCP.

Installing Clear Linux OS for Intel Architecture to a target system
===================================================================

1. Configure the BIOS; this may involve changing the boot device order 
   to boot first from the USB device. 
2. Insert the USB device that is flashed with the 
   `installer image <http://download.clearlinux.org/image/>`_ into the 
   target system, then reboot. 
3. The Installer user interface will appear. Once all appropriate configuration
   options have been chosen the installer will install the OS.

The entire installation should take no more than a few minutes. 

For feedback on installation or other topics, please feel free to write in to our 
`mailing list <https://lists.clearlinux.org/mailman/listinfo/dev>`_.

Note: You can also try :ref:`vm-kvm`.

