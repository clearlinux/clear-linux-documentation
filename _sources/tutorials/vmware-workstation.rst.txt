
.. _vmware-workstation:

VMware\* Workstation Pro
########################

VMware Workstation Pro allows you to run multiple operating systems as
:abbr:`VMs (virtual machines)` on a single host. It is a more advanced version
of VMware Workstation Player.

This tutorial shows how to do a manual installation of VMware Workstation
Pro on a |CL-ATTR| host using the console plus the VMware Workstation Pro GUI.

VMware Workstation Pro on Linux installs two major components:

#. VMware hypervisor software
#. VMware kernel modules

.. note::

   |CL| is not an officially supported host OS for VMware Workstation Pro. This
   tutorial follows the generic Linux installation instructions with details
   specific to a manual installation on |CL|.

Prerequisites
*************

Enable virtualization in the BIOS before installing VMware Workstation Pro.

Install VMware Workstation Pro
******************************

Use the console installer to install the VMware Workstation Pro hypervisor
software:

#. Download
   `VMware Workstation Pro for Linux <https://www.vmware.com/products/workstation-pro/workstation-pro-evaluation.html>`_.

   .. note::

      The downloaded file is named with a :file:`.bundle` file extension but
      this is not a |CL| :ref:`bundle <bundles-guide>`!

#. In a terminal, :command:`cd` to the directory where the `.bundle` installation
   file was saved.

   .. code-block:: bash

	    cd ~/Downloads/

#. Make the `.bundle` installation file executable. Replace
   [VMware-Workstation-xxxx-xxxx.architecture] with the actual file name.

   .. code-block:: bash

      chmod +x ./[VMware-Workstation-xxxx-xxxx.architecture].bundle

#. Start the installation.

   .. code-block:: bash

      sudo ./VMware-Workstation-[xxxx-xxxx].architecture.bundle

   .. code-block:: console

	    Extracting VMware Installer...done.

#. When prompted to specify the system service scripts directory, use the common
   suggestion:

   .. code-block:: console

	    System service scripts directory (commonly /etc/init.d).: /etc/init.d

   You will see output similar to the following:

   .. code-block:: console

	    Installing VMware VMX 15.5.0
	        Configuring...No rc*.d style init script directories were given to the installer.
	    You must manually add the necessary links to ensure that the vmware    ]  49%
	    service at /etc/init.d/vmware is automatically started and stopped on
	    Installing VMware Workstation 15.5.0
	        Configuring...
	    [######################################################################] 100%
	    Installation was successful.

   .. note::

	  During installation you will get an error about "No rc*.d style init
	  script directories" being given. This can safely be ignored as |CL| uses
	  :command:`systemd`.

Install VMware kernel modules
*****************************

After installing VMware Workstation Pro, additional VMware kernel modules must
be compiled and installed. Before installing the VMware kernel modules, install
DKMS, which will provide the necessary tools to add the VMware kernel modules.

Install DKMS
============

.. include:: ../guides/kernel/kernel-modules-dkms.rst
   :start-after: kernel-modules-dkms-install-begin:
   :end-before: kernel-modules-dkms-install-end:

Install kernel modules
======================

Launch the VMware Workstation Pro GUI to finish the installation and build the
needed kernel modules.

#. On the |CL| desktop, find the VMware Workstation Pro icon and click to launch.

#. Click through the installation customization screens as directed in the
   VMware Kernel Module Updater.

#. On the last screen click :guilabel:`Finish`. VMware Workstation Pro will launch.

#. Create and configure a new VM!

Troubleshooting
***************

If problems occur during installation, the recommended first step is to identify
which major component the issues are occurring in (hypervisor or kernel modules).
This will help direct further troubleshooting.

Troubleshooting tips:

* If the issue is with compiling the kernel modules and you are running the native
  kernel, try installing the LTS kernel instead.

* If modules failed to install or load, check logs in :file:`/tmp/vmware-<username>/*.log`

* Try re-installing all VMware modules with the following command:

  .. code-block:: bash

     sudo vmware-modconfig --console --install-all
