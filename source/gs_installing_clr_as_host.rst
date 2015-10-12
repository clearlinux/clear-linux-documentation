Installing the OS as host
##########################################################

Running Clear Linux* OS for Intel® Architecture natively on a system is easy with the simple installer image. To get started you'll need the following:

* A USB stick flashed with the `installer image <http://download.clearlinux.org/image/>`_. Instructions for how to do this are `here <gs_creating_bootable_usb.html>`_.
* Host machine running `supported hardware <gs_supported_hardware.html>`_.
* Network access via DHCP.

Installing Clear Linux OS for Intel Architecture to a target system
++++++++++++++++++++++++++++++++++++++++++++

1. Configure the BIOS; this may involve changing the boot device order to boot first from the USB device. 
2. Insert the USB device that is flashed with the `installer image <http://download.clearlinux.org/image/>`_ into the target system, then reboot. As the system boots, you'll see::

	Clear Linux OS for Intel Architecture installation in progress... Your computer will power off once installation completes successfully.

The entire installation should take no more than a few minutes. If you run into any trouble, log in as root during the installation phase and check the status of the install with

.. code:: text

	$ systemctl status ister

You might need to switch to another TTY.

For feedback on installation or other topics, please feel free to write in to our `mailing list <https://lists.clearlinux.org/mailman/listinfo/dev>`_.

Note: You can also `run Clear Linux OS for Intel Architecture in a virtual environment <gs_running_clr_virtual.html>`_.

