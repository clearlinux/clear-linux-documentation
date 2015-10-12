Creating a bootable USB stick to install the OS
############################################################

This article explains how to create a bootable USB stick to `install Clear Linux* OS for Intel® Architecture as host <gs_installing_clr_as_host.html>`_ on a target computer. You can also `run the OS in a virtualized environment <gs_running_clr_virtual.html>`_.

What you need
-------------------
To create a bootable USB stick to install the OS, you need the following:

* A USB stick, formatted as ext4. Remember that the process of flashing to a USB completely deletes the contents of the drive; as always, run ``dd`` with caution.
* An OS image; the most current version can be found here: `https://download.clearlinux.org/image <https://download.clearlinux.org/image>`_. For older versions, see our `downloads page <http://download.clearlinux.org/>`_.

Grab the installer image
------------------------
.. code:: text

 $ wget https://download.clearlinux.org/image/clear-[release_number]-installer.img.xz

Check the SHA512
----------------
.. code:: text

 $ sha512sum clear-[release_number]-installer.img.xz

The above command outputs the checksum of the image you just downloaded; it will, of course, vary depending on the version you're testing.

Confirm the mount point on the USB drive
----------------------------------------
Using the ``lsblk`` command is helpful to show the block-level devices; a USB drive usually shows up under ``/sdb`` or ``/sdc`` (not ``/sda``) and should indicate disk space < the size of the USB drive.

.. code:: text

 $ lsblk /dev/sdb NAME MAJ:MIN RM SIZE RO TYPE MOUNTPOINT sdb 8:16 1 14.9G 0 disk ?? sdb1 8:17 1 14.9G 0 part

Make sure that the USB is not mounted
-------------------------------------
The easiest way is with ``# df``.

Flash the image to the USB
--------------------------
Flash the image with the following command, adding the -v option for verbose mode (recommended), as the image file may be large, and the process can take a while. This will likely need to be done as root.

.. code:: text

 # xzcat -v clear-[release_number]-installer.img.xz | dd of=/dev/sdb bs=4M

Wait for the final confirmation
-------------------------------
This example shows ``clear-2190-installer.img.xz`` flashed to a 16GB USB stick mounted on ``/sdc``.

.. image:: images\gs_confirmation_screen.png
    :align: center
    :alt: confirmation

Success!
++++++++
Your USB stick is now ready to `boot and install the Clear Linux OS for Intel Architecture <gs_installing_clr_as_host.html>`_.

