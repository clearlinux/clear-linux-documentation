.. _kernel_boot_params:

Modify kernel boot parameters
#############################

Changing kernel boot paramters can drastically change the way the OS behaves,
so be cautious when doing so. |CL| provides a simple way to do this that is
consistent with its :ref:`stateless` nature. All configuration changes belong
in the :file:`/etc/kernel/` path. The :command:`clr-boot-manager` generates
boot entries, so we'll use it to run an update each time we change a boot
parameter. 

.. note::

   When testing boot parameters, use ``clr-boot-manager get-timeout``
   and ``clr-boot-manager set-timeout`` to set a non-zero boot timeout.
   You may then enter ``e`` at the boot menu to restore or remove any
   changes from the boot command.

For more detailed information about the capabilities of the clr-boot-manager,
view the man pages from a terminal session:

.. code-block:: bash

   man clr-boot-manager

.. contents:: 
    :local:
    :depth: 1

Updating the boot manager
*************************

The system must be updated and rebooted each time a changes is made
to the boot parameters:

.. code-block:: bash

   sudo clr-boot-manager update
   sudo reboot now

Add a boot parameter
********************

Add the "debug" kernel boot option:

.. code-block:: bash

   sudo mkdir -p /etc/kernel/cmdline.d
   echo "debug" | sudo tee /etc/kernel/cmdline.d/debug.conf

Update the boot manager and reboot.

Remove a boot parameter
***********************

Remove the "quiet" kernel boot option:

.. code-block:: bash

   sudo mkdir -p /etc/kernel/cmdline-removal.d
   echo "quiet" | sudo tee /etc/kernel/cmdline-removal.d/quiet.conf

Update the boot manager and reboot.

Restoring default boot parameters
*********************************

Delete the contents of kernel settings directories to reset boot parameters:

.. code-block:: bash

   sudo rm /etc/kernel/cmdline.d/*
   sudo rm /etc/kernel/cmdline-removal.d/*

Update the boot manager and reboot.