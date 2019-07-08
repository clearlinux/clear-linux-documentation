.. _kernel_boot_params:

Modify kernel boot parameters
#############################

Changing kernel boot paramters can drastically change the way the OS behaves,
so be cautious when doing so. |CL| provides a simple way to do this that is
consistent with its :ref:`stateless` nature. All configuration changes belong
in the :file:`/etc/kernel/` path. The :command:`clr-boot-manager` generates
boot entries, so we'll use it to run an update each time we change a boot
paramter. 

.. warning::

   Be careful when editing boot parameters as the system can be made
   non-bootable.

.. contents:: 
    :local:
    :depth: 1

Add a boot parameter
********************



Remove a boot parameter
***********************

Remove the "quiet" kernel boot option:

.. code-block:: bash

   sudo mkdir -p /etc/kernel/cmdline-removal.d
   echo "quiet" | sudo tee /etc/kernel/cmdline-removal.d/quiet.conf

Update the boot manager and reboot the system:

.. code-block:: bash

   sudo clr-boot-manager update
   sudo reboot now

Restoring default boot parameters
*********************************