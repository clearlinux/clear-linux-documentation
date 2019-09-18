.. _nvidia:

NVIDIA\* Drivers
################

NVIDIA manufactures graphics processing units (GPU), also known as
graphics cards.

NVIDIA devices on Linux\* have two popular device driver options: the
opensource drivers from the `nouveau project`_ or the proprietary drivers
published by NVIDIA. The nouveau drivers are built into the |CL-ATTR|
kernel and are loaded automatically at system boot if a compatible card
is detected.

These instructions show how to use the proprietary NVIDIA drivers, which
require a manual installation.

.. warning::

   Software installed outside of :ref:`swupd <swupd-guide>` is not updated
   with |CL| updates and must be updated and maintained manually.

   For example, the file :file:`/usr/lib/libGL.so` conflicts with the file
   provided by the mesa package in |CL| and the file NVIDIA provides. If a |CL|
   update overwrites these files, a reinstallation of the NVIDIA driver might
   be required.

.. contents:: :local:
    :depth: 1

Prerequisites
*************

* A |CL| system with a desktop installed
* An NVIDIA device installed

Install DKMS
************

The :ref:`Dynamic Kernel Module System (DKMS)
<kernel-modules-dkms>` allows the NVIDIA kernel modules to be automatically
integrated when kernel updates occur in |CL|.

Install the appropriate DKMS bundle using the instructions below:

.. note::
   The Long Term Support (LTS) kernel variant is more likely to remain
   compatible between updates with NVIDIA drivers.

.. include:: /guides/kernel/kernel-modules-dkms.rst
   :start-after: kernel-modules-dkms-install-begin:
   :end-before: kernel-modules-dkms-install-end:

Download and install the NVIDIA drivers
***************************************

Download the NVIDIA drivers for Linux
=====================================

#. Identify the NVIDIA GPU model that is installed.

   .. code-block:: bash

      sudo lshw -C display

#. Go to the `NVIDIA Driver Downloads website`_ . Search for and download the
   appropriate driver based on the NVIDIA GPU model you have with *Linux
   64-bit* selected as the Operating System .

#. Open a terminal and navigate to where the
   :file:`NVIDIA-Linux-x86_64-<VERSION>.run` file was saved. In this
   example, it was saved in the Downloads folder.

   .. code-block:: bash

      cd ~/Downloads/

#. Make the :file:`NVIDIA-Linux-x86_64-<VERSION>.run` file executable.

   .. code-block:: bash

      chmod +x :file:`NVIDIA-Linux-x86_64-<VERSION>.run`

Disable the nouveau driver
==========================

The proprietary NVIDIA driver is incompatible with the nouveau driver and
must be disabled before installation can continue.

#. Disable the nouveau driver by creating a blacklist file under
   :file:`/etc/modprobe.d` and reboot.

   .. code-block:: bash

      sudo mkdir /etc/modprobe.d

      printf "blacklist nouveau \noptions nouveau modeset=0 \n" | sudo tee --append /etc/modprobe.d/disable-nouveau.conf

#. Reboot the system and log back in. It is normal for the graphical
   environment not to start without the NVIDIA driver loaded.

Configure alternative software paths
====================================

The NVIDIA installer is directed to install files under
:file:`/opt/nvidia` as much as possible to keep its contents isolated from the
rest of the |CL| system files under :file:`/usr`.  The dynamic linker and X
server must be configured to use the content under
:file:`/opt/nvidia`.

#. Configure the dynamic linker to look for and to cache shared libraries under
   :file:`/opt/nvidia/lib` and :file:`/opt/nvidia/lib32` in addition to the
   default paths.

   .. code-block:: bash

      echo "include /etc/ld.so.conf.d/*.conf" |  sudo tee --append /etc/ld.so.conf

      sudo mkdir /etc/ld.so.conf.d
      printf "/opt/nvidia/lib \n/opt/nvidia/lib32 \n" | sudo tee --append /etc/ld.so.conf.d/nvidia.conf

#. Reload the dynamic linker run-time bindings and library cache.

   .. code-block:: bash

      sudo ldconfig

#. Create a Xorg configuration file to search for modules under
   :file:`/opt/nvidia` in addition to the default path.

   .. code-block:: bash

      sudo mkdir -p /etc/X11/xorg.conf.d/

      sudo tee /etc/X11/xorg.conf.d/nvidia-files-opt.conf > /dev/null <<'EOF'
      Section "Files"
              ModulePath      "/usr/lib64/xorg/modules"
              ModulePath      "/opt/nvidia/lib64/xorg/modules"
      EndSection
      EOF

Install the NVIDIA drivers
==========================

#. A terminal not running on */dev/tty1* is useful to view uninterrupted
   installation progress. Switch to a secondary virtual terminal by pushing
   :command:`CTRL + ALT + F2` or remotely login over SSH.

#. Navigate to the directory where the NVIDIA installer was downloaded.

   .. code-block:: bash

      cd ~/Downloads/

#. Run the installer with the advanced options below.

   .. code-block:: bash

      sudo ./NVIDIA-Linux-x86_64-<VERSION>.run \
      --utility-prefix=/opt/nvidia \
      --opengl-prefix=/opt/nvidia \
      --compat32-prefix=/opt/nvidia \
      --compat32-libdir=lib32 \
      --x-prefix=/opt/nvidia \
      --x-module-path=/opt/nvidia/lib64/xorg/modules \
      --x-library-path=/opt/nvidia/lib64 \
      --x-sysconfig-path=/etc/X11/xorg.conf.d \
      --documentation-prefix=/opt/nvidia \
      --application-profile-path=/etc/nvidia \
      --no-precompiled-interface \
      --no-nvidia-modprobe \
      --no-distro-scripts \
      --force-libglx-indirect \
      --glvnd-egl-config-path=/etc/glvnd/egl_vendor.d \
      --egl-external-platform-config-path=/etc/egl/egl_external_platform.d  \
      --dkms \
      --silent

#. The graphical interface may automatically start after the NVIDIA driver
   is loaded. Return to the working terminal and log back in if necessary.

#. Confirm that the NVIDIA kernel modules are loaded.

   .. code-block:: bash

      lsmod | grep ^nvidia

#. Run a |CL| system verification to restore files that the NVIDIA installer
   likely deleted.

   .. code-block:: bash

      sudo swupd repair --quick --bundles=lib-opengl

.. note::

   The NVIDIA software places some files under the :file:`/usr` subdirectory
   that are not managed by |CL| and conflict with the |CL| stateless design.

   Although a limited version of :command:`swupd repair` is run above,
   other uses of the :command:`swupd repair` command should be avoided
   with the proprietary NVIDIA drivers installed.

Updating the NVIDIA drivers
***************************

The proprietary NVIDIA drivers are installed manually outside of
:ref:`swupd <swupd-guide>` and must be updated manually when needed.

Updating the NVIDIA drivers follows the same steps as initial installation,
however the desktop environment must first be stopped so that the drivers are
not in use.

#. Follow the steps in the `Download the NVIDIA Drivers for Linux`_ section
   to get the latest NVIDIA drivers.

#. Temporarily set the default boot target to the *multi-user*, which is
   a non-graphical runtime.

   .. code-block:: bash

      sudo systemctl set-default multi-user.target

#. Reboot the system and log back in. It is normal for the graphical
   environment not to start.

#. Follow the steps in the `Install the NVIDIA Drivers`_ section to update
   the NVIDIA drivers. This installation will overwrite the previous NVIDIA
   drivers and files.

#. Set the default boot target back to the *graphical* target.

   .. code-block:: bash

      sudo systemctl set-default graphical.target

#. Reboot the system and log back in.

#. Trigger a flatpak update that will download the runtime corresponding
   with the new NVIDIA drivers for the flatpak apps that require it.

   .. code-block:: bash

      flatpak update

Uninstalling the NVIDIA drivers
*******************************

The NVIDIA drivers and associated software can be uninstalled and nouveau
driver restored with the instructions in this section.

#. Remove the :file:`modprobe.d` file that prevents nouveau from loading.

   .. code-block:: bash

      sudo rm /etc/modprobe.d/disable-nouveau.conf

#. Remove the :file:`xorg.conf.d` file that adds a search path for X modules.

   .. code:: bash

      sudo rm /etc/X11/xorg.conf.d/nvidia-files-opt.conf

#. Run the :command:`sudo /opt/nvidia/bin/nvidia-uninstall`

#. Follow the prompts on the screen and reboot the system.

Debugging installation of NVIDIA drivers
****************************************

* The NVIDIA driver places installer and uninstaller logs under
  :file:`/var/log/nvidia-install` and :file:`/var/log/nvidia-uninstall`.

* :file:`NVIDIA-Linux-x86_64-<VERSION>.run --advanced-options` shows many
  parameters to control installation behavior.

* :file:`NVIDIA-Linux-x86_64-<VERSION>.run --extract-only` extracts
  installation files into a directory named
  :file:`NVIDIA-Linux-x86_64-<VERSION>`.

Additional resources
********************

* `Why aren't the NVIDIA Linux drivers open source? <https://nvidia.custhelp.com/app/answers/detail/a_id/1849/kw/Linux>`_

* `Where can I get support for NVIDIA Linux drivers? <https://nvidia.custhelp.com/app/answers/detail/a_id/44/kw/linux>`_

* `NVIDIA Accelerated Linux Graphics Driver Installation Guides <https://download.nvidia.com/XFree86/Linux-x86_64/>`_

.. _`nouveau project`:  https://nouveau.freedesktop.org/wiki/

.. _`NVIDIA Driver Downloads website`: https://www.nvidia.com/download/index.aspx
