.. _fix-broken-install:

Fix a broken installation of |CL-ATTR|
######################################

This guide explains how to fix a broken installation of |CL| using a live
desktop image on a USB. It's assumed you already installed |CL| on a
target system, but your operating system does not boot or function properly.
This guide addresses installation issues that may have impacted the
:file:`/usr` directory.

Prerequisites
*************

* :ref:`Download and install the live desktop image on a USB <bare-metal-install-beta>`

Boot a live desktop image to fix target system
**********************************************

#. Boot the |CL| live desktop image.

.. include:: ../../get-started/bare-metal-install-beta/bare-metal-install-beta.rst
   :start-after: install-on-target-start:
   :end-before: install-on-target-end:

Mount root, verify, and run swupd
*********************************

#. Open a Terminal window.

#. Log in as `root` and set a password.

#. Assure the system is connected to the network.

#. Mount the system’s root partition.

   #. To find the root partition, run:

      .. code-block:: bash

         lsblk

      We find the root partition at `/dev/sda3/`.

   #. Next, mount it.

      .. code-block:: bash

         sudo mount /dev/sda3 /mnt

#. Verify that you mounted the correct root partition by checking the list
   of bundles that you installed on it.

   .. code-block:: bash

      sudo ls /usr/share/clear/bundles

#. Next, run swupd to fix any issues on the target system.

   .. code-block:: bash

      sudo swupd verify --fix --picky --path=/mnt

   :ref:`Learn more about how swupd works <swupd-guide>`.

#. After the process is complete, unmount the root partition:

   .. code-block:: bash

      sudo umount /mnt

#. Reboot the system, remove the live desktop USB drive,
   and boot into the repaired system.

   .. code-block:: bash

      sudo reboot

**Congratulations!** You successfully restored |CL|.