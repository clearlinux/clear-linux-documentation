.. _enable-systemd-boot-menu:

Enable systemd-boot Menu
########################

The default installation of |CL| does not set a timeout value for the systemd-boot 
bootloader. At boot time, you will not be presented with the systemd-boot menu. Without 
a menu, you cannot interact with systemd-boot such as selecting a different kernel,
editing kernel command line parameters, etc. 

To set a timeout value for the systemd-boot menu, follow these steps:

#. Boot up |CL|.

#. Log in.

#. Set a timeout (for example: 20 seconds).

   .. code-block:: bash
      
      sudo clr-boot-manager set-timeout 20

#. Reboot.
