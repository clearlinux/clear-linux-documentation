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
   provided by the mesa package in |CL| and the file NVIDIA provides. If a
   |CL| update or repair overwrites these files, a reinstallation of the
   NVIDIA driver might be required.

.. contents:: :local:
    :depth: 1

Prerequisites
*************

* A |CL| system with a desktop installed
* An NVIDIA device installed


Known issues
============

Systems with multiple graphics devices, including integrated graphics (iGPU),
are known to be problematic.

.. note:: NVIDIA Optimus\*
   
   Some systems come with a hybrid graphics configuration for a balanced power
   and performance profile. This configuration is commonly found on
   laptops. `NVIDIA Optimus technology
   <https://www.geforce.com/hardware/technology/optimus>`_, is designed to
   allow switching seamlessly between a NVIDIA device and another graphics
   devices sharing the same display.
   
   Getting NVIDIA Optimus on Linux working well with both graphics devices
   adds an additional level of complexity with platform specific steps and may
   require additional software. Installation for systems with NVIDIA Optimus
   with both graphics devices operating is not covered by the scope of this
   documentation. As a simple workaround, some systems can disable one of the
   graphics devices or NVIDIA Optimus in the system firmware.

.. note::
   The :ref:`Long Term Support (LTS) kernel <compatible-kernels>` variant is
   more likely to be compatible with proprietary NVIDIA drivers.

**See the** `Troubleshooting`_ **section for more known issues and solutions.**


Installation
************

Configure workarounds
=====================

Some workarounds are required for the NVIDIA proprietary drivers to be usable
and sustainable on |CL|.


#. Remove the kernel command-line parameter *intel_iommu=igfx_off* or disable
   input–output memory management unit (IOMMU), also known as Intel®
   Virtualization Technology (Intel® VT) for Directed I/O (Intel® VT-d), in your system EFI/BIOS.
   See `this GitHub report
   <https://github.com/clearlinux/distribution/issues/1274>`_ and the NVIDIA
   documentation on `DMA issues
   <https://download.nvidia.com/XFree86/Linux-x86_64/440.44/README/dma_issues.html>`_
   for more information.

   The *intel_iommu-igfx_off* kernel parameter can be removed with the
   commands below: 
  
   .. code-block:: bash
    
      sudo mkdir -p /etc/kernel/cmdline-removal.d/
      echo "intel_iommu=igfx_off" | sudo tee /etc/kernel/cmdline-removal.d/intel-iommu.conf
    
#. Create a custom systemd unit that overwrites the :file:`libGL` library
   after every |CL| update with a pointer to the NVIDIA provided copy instead
   of the version provided by |CL|. These libraries conflict causing the
   NVIDIA driver to break when |CL| updates mesa. See the NVIDIA documentation
   on `installed components
   <https://download.nvidia.com/XFree86/Linux-x86_64/440.44/README/installedcomponents.html>`_
   for more information.

   a. Create a systemd service unit to overwrite the |CL| provided
      :file:`libGL.so.1` files with a symlink to the NVIDIA copies.
  
      .. code-block:: bash

         sudo tee /etc/systemd/system/fix-nvidia-libGL-trigger.service > /dev/null <<'EOF'
         [Unit]
         Description=Fixes libGL symlinks for the NVIDIA proprietary driver
         BindsTo=update-triggers.target

         [Service]
         Type=oneshot
         ExecStart=/usr/bin/ln -sfv /opt/nvidia/lib/libGL.so.1 /usr/lib/libGL.so.1
         ExecStart=/usr/bin/ln -sfv /opt/nvidia/lib32/libGL.so.1 /usr/lib32/libGL.so.1
         EOF

   b. Reload the systemd manager configuration to pickup the new serivce.
  
      .. code-block:: bash  
    
         sudo systemctl daemon-reload
       
   c. Add the service as a dependency to the |CL| updates trigger causing the
      service to run after every update.
  
      .. code-block:: bash  
      
         sudo systemctl add-wants update-triggers.target fix-nvidia-libGL-trigger.service

Install DKMS
============

The :ref:`Dynamic Kernel Module System (DKMS) <kernel-modules-dkms>` allows
the NVIDIA kernel modules to be automatically integrated when kernel updates
occur in |CL|. Install the appropriate DKMS bundle using the instructions
below:

.. note::
   The Long Term Support (LTS) kernel variant is more likely to remain
   compatible between updates with NVIDIA drivers.

.. include:: /guides/kernel/kernel-modules-dkms.rst
   :start-after: kernel-modules-dkms-install-begin:
   :end-before: kernel-modules-dkms-install-end:

Download the NVIDIA drivers
===========================

#. Identify the NVIDIA GPU model that is installed.

   .. code-block:: bash

      sudo lshw -C display

#. Go to the `NVIDIA Driver Downloads website`_ . Search for and download the
   appropriate driver based on the NVIDIA GPU model you have with *Linux
   64-bit* selected as the Operating System.

   .. code-block:: bash

      wget https://download.nvidia.com/XFree86/Linux-x86_64/<VERSION>/NVIDIA-Linux-x86_64-<VERSION>.run   

   If you already know the appropriate driver version for your device, you can
   also obtain a download link directly from one of the links below:

   - https://www.nvidia.com/en-us/drivers/unix/
   - https://download.nvidia.com/XFree86/Linux-x86_64/

      
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

#. Navigate to the directory where the NVIDIA installer was downloaded. In
   this example, it was saved in the :file:`Downloads` folder.

   .. code-block:: bash

      cd ~/Downloads/


#. Run the installer with the advanced options below.

   .. code-block:: bash

      sudo sh NVIDIA-Linux-x86_64-<VERSION>.run \
      --utility-prefix=/opt/nvidia \
      --opengl-prefix=/opt/nvidia \
      --compat32-prefix=/opt/nvidia \
      --compat32-libdir=lib32 \
      --x-prefix=/opt/nvidia \
      --x-module-path=/opt/nvidia/lib64/xorg/modules \
      --x-library-path=/opt/nvidia/lib64 \
      --x-sysconfig-path=/etc/X11/xorg.conf.d \
      --documentation-prefix=/opt/nvidia \
      --application-profile-path=/etc/nvidia/nvidia-application-profiles-rc.d \
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

#. Optional: Create a link for the nvidia-settings desktop entry to
   :file:`~/.local/share/applications` so that it appears in the launcher for easy access. 

   .. code-block:: bash

      ln -sv /opt/nvidia/share/applications/nvidia-settings.desktop $HOME/.local/share/applications


Updating
********

The proprietary NVIDIA drivers are installed manually outside of
:ref:`swupd <swupd-guide>` and must be updated manually when needed.

Updating the NVIDIA drivers follows the same steps as initial installation,
however the desktop environment must first be stopped so that the drivers are
not in use.

#. Follow the steps in the `Download the NVIDIA drivers`_ section
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

#. Trigger a :command:`flatpak update` to download the runtime corresponding
   with the new NVIDIA drivers for the flatpak apps that require it.

   .. important:: 

      Some flatpak applications won't start after updating the NVIDIA drivers
      until the flatpak runtime is updated with the corresponding driver
      version.
      
   .. code-block:: bash

      flatpak update 



      

Uninstallation
**************

The NVIDIA drivers and associated software can be uninstalled and nouveau
driver restored with the instructions in this section.

#. Remove the files created for workarounds.

   .. code-block:: bash

      sudo rm /etc/kernel/cmdline-removal.d/intel-iommu.conf
      sudo rm /etc/systemd/system/fix-nvidia-libGL-trigger.service
      sudo rm /etc/systemd/system/update-triggers.target.wants/fix-nvidia-libGL-trigger.service
      sudo systemctl daemon-reload
      

#. Remove the :file:`modprobe.d` file that prevents nouveau from loading.

   .. code-block:: bash

      sudo rm /etc/modprobe.d/disable-nouveau.conf
      
#. Remove the :file:`nvidia.conf` file so that dynamic linker does not
   look for cached libraries under :file:`/opt/nvidia/lib` and :file:`/opt/nvidia/lib32`.
   
   .. code-block:: bash
   
      sudo rm /etc/ld.so.conf.d/nvidia.conf
      sudo ldconfig

   Optionally, restore :file:`ld.so.conf` to default if no other configuration files under :file:`/etc/ld.so.conf.d`
   needs to be included.

   .. code-block:: bash
      
      sudo sed -i '/^include \/etc\/ld\.so\.conf\.d\/\*\.conf$/d' /etc/ld.so.conf


#. Remove the :file:`xorg.conf.d` file that adds a search path for X modules.

   .. code:: bash

      sudo rm /etc/X11/xorg.conf.d/nvidia-files-opt.conf

#. Remove the nvidia-settings desktop entry file if it was linked to
   :file:`~/.local/share/applications`.

   .. code:: bash

      unlink -v $HOME/.local/share/applications/nvidia-settings.desktop


#. Run the :command:`nvidia-uninstall` command.

   .. code:: bash

      sudo /opt/nvidia/bin/nvidia-uninstall

#. Follow the prompts on the screen and reboot the system.


Troubleshooting
***************

* The NVIDIA driver places installer and uninstaller logs under
  :file:`/var/log/nvidia-install` and :file:`/var/log/nvidia-uninstall`.

* :file:`NVIDIA-Linux-x86_64-<VERSION>.run --advanced-options` shows many
  parameters to control installation behavior.

* :file:`NVIDIA-Linux-x86_64-<VERSION>.run --extract-only` extracts
  installation files into a directory named
  :file:`NVIDIA-Linux-x86_64-<VERSION>`.

* The X server logs under :file:`/var/log/X*` contain useful
  information about display and driver loading. Check all the files and
  timestamps when troubleshooting.

* The DKMS build logs under :file:`/var/lib/dkms/nvidia*` contain information
  about kernel module builds which can be useful if the NVIDIA driver breaks
  between kernel upgrades.


No display or blank screen
==========================

Check to see if the display has come up on another graphics device, including
the integrated graphics device.

You might get a black screen or the login screen might not come up after
installing the NVIDIA drivers until an Xorg configuration has been defined for
your monitors.


"Oh no! Something has gone wrong" GNOME\* crash
===============================================


.. figure:: /_figures/nvidia/nvidia-gnome-crash.png
   :alt: NVIDIA driver GNOME crash on Clear Linux OS
   :align: center

   NVIDIA driver GNOME crash dialogue on Clear Linux OS.

There have been reports of GNOME crashing with an "Oh no! Something has gone
wrong" error message with NVIDIA drivers installed while other graphics
devices are enabled.

Try disabling other graphics devices, including integrated graphics, in your
system's EFI/BIOS. 


Slow boot times
===============


There have been reports of slow boot times with NVIDIA drivers installed.
Normally, when GDM detects NVIDIA proprietary drivers, it will disable Wayland
and enable X11. Should GDM fail to disbale Wayland, it may results in slow boot
times, according to `this GitHub reprot
<https://github.com/clearlinux/distribution/issues/1780>`_.

To manually disable Wayland:

.. code-block:: bash

      sudo tee /etc/gdm/custom.conf > /dev/null <<'EOF'
      [daemon]
      WaylandEnable=false
      EOF


Brightness control
==================

If you can't control the screen brightness with the NVIDIA driver installed,
try one of the solutions below:

- Add a kernel parameter *acpi_osi=* which disables the ACPI Operating System
  Identification function. Some system firmware may manipulate brightness
  control keys based on the reported operating system. Disabling the
  identification mechanism can cause the system firmware to expose brightness
  controls that are recognizable in Linux.

  .. code:: bash

     sudo mkdir -p /etc/kernel/cmdline.d 
     echo "acpi_osi=" | sudo tee /etc/kernel/cmdline.d/acpi-backlight.conf   
     sudo clr-boot-manager update  



- Add a kernel parameter for the nvidia driver:
  *NVreg_EnableBacklightHandler=1*. This handler overrides the ACPI-based one
  provided by the video.ko kernel module. This option is available with NVIDIA
  driver version 387.22 and above. 
  
  .. code:: bash

     sudo mkdir -p /etc/kernel/cmdline.d 
     echo "nvidia.NVreg_EnableBacklightHandler=1" | sudo tee /etc/kernel/cmdline.d/nvidia-backlight.conf   
     sudo clr-boot-manager update
     

- Add the *EnableBrightnessControl=1* options to the *Device*
  section of your xorg config. Below is an example:

  .. code:: bash

     sudo mkdir -p /etc/X11/xorg.conf.d/

     sudo tee /etc/X11/xorg.conf.d/nvidia-brightness.conf > /dev/null <<'EOF'
     Section "Device"
         Identifier     "Device0"
         Driver         "nvidia"
         Option         "RegistryDwords" "EnableBrightnessControl=1"
     EndSection   
     EOF

Additional resources
====================

* `Why aren't the NVIDIA Linux drivers open source? <https://nvidia.custhelp.com/app/answers/detail/a_id/1849/kw/Linux>`_

* `Where can I get support for NVIDIA Linux drivers? <https://nvidia.custhelp.com/app/answers/detail/a_id/44/kw/linux>`_

* `NVIDIA Accelerated Linux Graphics Driver Installation Guides <https://download.nvidia.com/XFree86/Linux-x86_64/>`_

*Intel and the Intel logo are trademarks of Intel Corporation or its subsidiaries.*

.. _`nouveau project`:  https://nouveau.freedesktop.org/wiki/

.. _`NVIDIA Driver Downloads website`: https://www.nvidia.com/download/index.aspx


