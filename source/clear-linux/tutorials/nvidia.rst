.. _nvidia:

Install NVIDIA Drivers
######################

NVIDIA is a manufacture of graphics processing units (GPU), also known as
graphics cards. 

NVIDIA devices on Linux have two popular device driver options: the opensource
drivers from the `nouveau project`_ or the proprietary drivers published by
NVIDIA. The nouveau drivers are built into the |CL-ATTR| kernel and are loaded
automatically at system boot if a compatible card is detected. 

These instructions show how to use the proprietary NVIDIA drivers which
require a manual installation.


.. contents:: :local:
    :depth: 2



Prerequisites 
*************

* A |CL| system with a desktop installed
* A NVIDIA device installed


Install the LTS kernel and DKMS
*******************************

The Long Term Support (LTS) kernel variant is most likely to remain
compatible with NVIDIA drivers. The :ref:`Dynamic Kernel Module System (DKMS) <kernel-modules-dkms>` allows the NVIDIA kernel modules to be automatically
integrated when kernel updates occur in |CL|. Install both using the
instructions below:


.. include:: ../guides/maintenance/kernel-modules-dkms.rst
   :start-after: kernel-modules-dkms-install-begin:
   :end-before: kernel-modules-dkms-install-end:


Download and install the NVIDIA Linux Driver
********************************************


Download the NVIDIA Linux Driver
================================

#. Identify the model of NVIDIA GPU that is installed.

   .. code-block:: bash

      lshw -C display


#. Go to the `NVIDIA Driver Downloads website`_ . Search for and download the
   appropriate driver based on the model of  NVIDIA GPU you have with *Linux
   64-bit* selected as the Operating System . 


#. Open a terminal and navigate to where the
   :file:`NVIDIA-Linux-x86_64-<VERSION>.run` file was saved. In this
   example, it was saved in the Downloads folder.

   .. code-block:: bash

      cd ~/Downloads/


#. Extract the contents of the .run file.

   .. code-block:: bash

      sh NVIDIA-Linux-x86_64-<VERSION>.run --extract-only


Disable the nouveau driver
==========================

#. The proprietary NVIDIA driver is incompatible with the nouveau driver and
   needs to be disabled before installation can continue.

   Disable the nouveau driver by creating a file under :file:`/etc/modprobe.d`
   and reboot.

   .. code-block:: bash

      sudo mkdir /etc/modprobe.d

      echo "blacklist nouveau" | sudo tee --append /etc/modprobe.d/nvidia-disable-nouveau.conf
      echo "options nouveau modeset=0" | sudo tee --append /etc/modprobe.d/nvidia-disable-nouveau.conf
      

#. Reboot the system and log back in. It is normal for the graphical
   environment to not start with no NVIDIA driver loaded.


Install the NVIDIA Linux Driver
===============================

#. Navigate into the directory where the NVIDIA installer was extracted.

   .. code-block:: bash

      cd ~/Downloads/NVIDIA-Linux-x86_64-<VERSION>/   


#. Run the installer with the advanced options below.

   .. code-block:: bash
      
      sudo ./nvidia-installer --no-nvidia-modprobe --no-distro-scripts --no-opengl-files --no-libglx-indirect --no-install-libglvnd --no-install-compat32-libs --dkms --ui=none

#. The installer will prompt to register the kernel module sources with
   DKMS. Enter Y for yes.

   .. code-block:: bash

      Welcome to the NVIDIA Software Installer for Unix/Linux

      <snipped>

      Would you like to register the kernel module sources with DKMS? This will allow DKMS to automatically build a new
      module, if you install a different kernel later.
      [default: (Y)es]: Y



#. The graphical interface may automatically start after the NVIDIA driver
   is loaded. If it does restart, log back in.


#. Validate the nvidia kernel modules are loaded.

   .. code-block:: bash

      lsmod | grep ^nvidia


.. note::

   The NVIDIA installer places files under the :file:`/usr` subdirectory which
   are not managed by |CL| updates. The :command:`swupd verify --fix` command
   should be avoided with the proprietary NVIDIA drivers in use.
      

Uninstalling the NVIDIA driver
******************************

The NVIDIA drivers and associated software can be uninstalled and nouveau
driver restored by: 

#. Remove the previously created file :file:`etc/modprobe.d` that is
   preventing nouveau from loading.

   .. code-block:: bash

      sudo rm /etc/modprobe.d/nvidia-disable-nouveau.conf


#. Run the :command:`sudo nvidia-uninstall`

#. Follow the prompts on the screen and reboot the system. 



Additional resources
********************

* `Why aren't the NVIDIA Linux drivers open source? <https://nvidia.custhelp.com/app/answers/detail/a_id/1849/kw/Linux>`_

* `Where can I get support for NVIDIA Linux drivers? <https://nvidia.custhelp.com/app/answers/detail/a_id/44/kw/linux>`_


.. _`nouveau project`:  https://nouveau.freedesktop.org/wiki/

.. _`NVIDIA Driver Downloads website`: https://www.nvidia.com/download/index.aspx
