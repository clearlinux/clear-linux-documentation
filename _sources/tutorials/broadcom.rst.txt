.. _broadcom:

Broadcom\* Drivers
##################

Broadcom manufactures wireless network interfaces, including devices that
support WiFi and Bluetooth® technology.

Broadcom wireless devices on Linux\* have a lot of different combinations of
possible required software depending on the exact model of your device. These
combinations of software can overlap and conflict, creating an additional
challenge to get working.

As with most hardware devices, two components are needed for complete
functionality: a device driver and device firmware. These instructions show
how to identify Broadcom wireless hardware and configure a |CL| system with
the correct drivers and firmware for functionality. 

.. important::

   The Linux community has documented solutions and caveats for using specific
   Broadcom devices on Linux over time. It is worth doing research on your
   particular device model to see what others have already encountered.

.. contents:: :local:
    :depth: 1


Identify your device model
**************************

Broadcom device models start with BCM in the name and are identified by the
PCI vendor ID 14e4. To identify the exact model of Broadcom device you have
installed:

#. Run the commands below:

   .. code-block:: bash

      lspci -vnn -d 14e4:

Once the device model has been identified, you can cross-reference which
drivers support it.


Drivers
*******

brcmfmac and brcmsmac
=====================

*brcmfmac* and *brcmsmac*, historically known as *brcm80211*, are open-source
drivers for some newer Broadcom devices. These drivers are available in the
upstream Linux kernel, are enabled in the |CL| kernels, and will be
automatically loaded if a compatible device is detected. 

#. See if your device is listed on the support matrix of this driver:
   https://wireless.wiki.kernel.org/en/users/Drivers/brcm80211#supported_chips

   It is important to note that not all functionality is developed for these
   drivers yet. If you are looking for specific functionality, be sure to
   review the "To be done" list.

#. The firmware for cards supported by the *brcmfmac* and *brcmsmac* drivers
   are usually made available. Continue reading the `Firmware`_ section of
   this document.


b43 and b43legacy
=================

*b43* and *b43legacy* are community reverse-engineered open-source drivers for
some newer and older Broadcom devices. These drivers are available in the
upstream Linux kernel, are enabled in the |CL| kernels, and will be
automatically loaded if a compatible device is detected. 

#. See if your device is listed on the support matrix of this driver:
   https://wireless.wiki.kernel.org/en/users/Drivers/b43#list_of_hardware

#. The firmware for cards supported by the *b43* and *b43legacy* drivers
   usually needs to be sourced and installed manually. Continue reading the
   `Firmware`_ section of this document.


broadcom-wl
===========

*broadcom-wl*, also known as *broadcom-sta* or *wl*, is the proprietary closed
source driver from Broadcom and tends to work only for older devices. It is
also unmaintained and needs to be patched to work with newer kernels (>=4.7).
As such, it is not part of the Linux kernel, cannot be distributed by |CL|,
and has to be built as an out-of-tree kernel module.

.. note::

   It is recommended to use the :ref:`LTS kernel <compatible-kernels>` if you
   have to use this driver.

#. See if your device is supported and download the **Linux\* STA 64-bit
   driver** from
   `Broadcom's download website
   <https://www.broadcom.com/support/download-search?pg=&pf=Wireless+LAN+Infrastructure>`_
   or another trusted source.
   
   
#. Extract the downloaded archive into a separate folder. For example:
   
   .. code-block:: bash

      mkdir ./broadcom-wl/
      tar xvf ./hybrid-v35_64-nodebug-pcoem-6_30_223_271.tar.gz -C broadcom-wl/
      cd ./broadcom-wl/
   
#. Create a patches folder in the source tree and copy any necessary patches
   to it. You will have to research which specific set of patches are required
   for the running kernel version. The `gentoo repository for broadcom-sta
   <https://github.com/gentoo/gentoo/tree/master/net-wireless/broadcom-sta/files>`_
   is a good place to start looking for up-to-date patches.

   .. code-block:: bash
      
      mkdir ./patches/

#. :ref:`Install the DKMS bundle <kernel-modules-dkms-install-begin>` for your
   kernel. DKMS provides the framework to automatically rebuild the wl driver
   against new kernels versions from |CL| updates.

#.  In the extracted driver directory, create a :file:`dkms.conf` file based
    the contents below to provide DKMS information about how to build and
    install the kernel module. This example uses version *6.30.223.271*.

    .. code-block:: bash

       cat <<'EOF' >> dkms.conf
       PACKAGE_NAME=broadcom-wl
       PACKAGE_VERSION=6.30.223.271
       MAKE="make KBASE=/lib/modules/${kernelver}"
       CLEAN="make KBASE=/lib/modules/${kernelver} clean"
       BUILT_MODULE_NAME=wl
       DEST_MODULE_LOCATION=/kernel/drivers/net/wireless
       AUTOINSTALL=yes
       EOF

#. Add the filename of any patches previously added to the :file:`patches`
   folder to the :file:`dkms.conf` file so that DKMS applies them to the
   driver source before building. Below are example patch names to show the
   format used in :file:`dkms.conf`.

   .. code-block:: bash

      echo "PATCH[0]="first.patch" >> dkms.conf
      echo "PATCH[1]="second.patch" >> dkms.conf
      echo "PATCH[2]="third.patch" >> dkms.conf

#. Copy the directory to the dkms tree. This example uses version
   *6.30.223.271*.

   .. code-block:: bash

      sudo cp -Rv . /usr/src/broadcom-wl-6.30.223.271

#. Run the :command:`dkms` commands to add the broadcom-wl module to the dkms
   tree, build it, and install it. This example uses version *6.30.223.271*.

   .. code-block:: bash

      sudo dkms add -m broadcom-wl -v 6.30.223.271
      sudo dkms install -m broadcom-wl -v 6.30.223.271

#. Blacklist all other variations of Broadcom drivers from loading to prevent
   conflicts and problems.

   .. code-block:: bash

      sudo mkdir -p /etc/modprobe.d/

      sudo tee /etc/modprobe.d/broadcom.conf > /dev/null <<'EOF'
      blacklist b43
      blacklist b43legacy
      blacklist ssb
      blacklist bcm43xx
      blacklist brcm80211
      blacklist brcmfmac
      blacklist brcmsmac
      blacklist bcma
      EOF

#. Reboot the system and check that the module is loaded and working. If not,
   try manually updating dependencies and loading the module.

   .. code-block:: bash

      depmod -a
      modprobe wl


Firmware
********

In addition to device drivers, devices require firmware that gets loaded onto
the device directly.

Firmware for Broadcom devices are not fully open-source and not always
licensed for redistribution. |CL| kernel bundles :ref:`include the
linux-firmware bundle <firmware-included-begin>` which contains the firmware
binaries that are able to be redistributed. If your device's firmware is part
of the linux-firmware repository, nothing else is needed. This is usually
the case for devices supported by the *brcmfmac* and *brcmsmac* drivers.

In other cases, firmware may need to be obtained or extracted manually from a
trusted source because it is not licensed for distribution. This is usually
the case for devices supported by the *b43* and *b43legacy* drivers. Obtaining
these firmware is out of scope for this document, however there is information
about solutions to this problem available on the `Linux wireless wiki
<http://linuxwireless.sipsolutions.net/en/users/Drivers/b43/#firmware>`_.

On |CL| systems, firmware should be placed in :file:`/etc/firmware`. See the
:ref:`firmware` documentation for more information on loading custom
firmware.


Troubleshooting
***************

- See which drivers are currently loaded with the :command:`lsmod` and
  :command:`modinfo` commands.

- If your device is not showing up or having intermittent issues, ensure the
  card is not blocked by the kernel with the :command:`rfkill` command.

- Try blacklisting all the other variations of drivers not intended to be
  used. In some cases, the wrong device driver will be loaded causing
  problems. 

- If an external firmware image is required, it may be trying to load from a
  different path than expected. Check the output of :command:`sudo dmesg |
  grep -i firmware` for firmware loading issues.

*The Bluetooth® word mark and logos are registered trademarks owned by Bluetooth SIG, Inc. and any use of such marks by Intel Corporation is under license.*