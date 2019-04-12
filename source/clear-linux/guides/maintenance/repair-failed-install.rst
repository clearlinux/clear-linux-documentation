.. _repair-failed-install:

Repair a failed installation of |CL-ATTR|
#########################################

This guide explains how to repair a failed installation of |CL| using a live
installer image on a USB. It's assumed you already installed |CL| on a target system, but your operating system does not boot or function properly.

Prerequisites
*************

* :ref:`download-cl-installer-image`

Boot installer image to repair target system
********************************************

#. Boot the |CL| installer image.

   .. warning::

      Only launch the installer to enable command-line access to the target system. Do not proceed with the installation.

.. include:: ../bare-metal-install-beta/bare-metal-install.rst
   :start-after: install-on-target-start:
   :end-before: install-on-target-end:

#. Press :kbd:`CTL+ALT+F2` to launch the console.

#. Log in as `root` and set a password.

#. Assure the system is connected to the network.

#. Mount the system’s root partition.

   #. To find the root partition, run:

      .. code-block:: bash

         lsblk

      We find root is `/dev/sda3/`.

   #. Next, mount root.

      .. code-block:: bash

         mount /dev/sda3 /mnt

#. Next, run swupd to fix any issues on the target system.

   .. code-block:: bash

      swupd verify --fix --picky --path=/mnt

   :ref:`Learn more about how swupd works <swupd-guide>`.

#. Unmount:

   .. code-block:: bash

      umount /mnt

#. Reboot your system to assure all changes take effect.

   .. code-block:: bash

      sudo reboot

#. Before your system reboots, remove the |CL| image installer.

**Congratulations!** You successfully restored |CL|.