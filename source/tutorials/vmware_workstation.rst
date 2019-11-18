
VMware Workstation Pro\*
########################

VMware Workstation Pro\* allows you to run multiple operating systems as
:abbr:`VMs (virtual machines)` on a single host.

VMware Workstation on Linux\* installs two major components:

#. Hypervisor
#. Kernel modules

This tutorial shows how to do a manual installation of VMware Workstation
Pro15.5.0 on a |CL| host using the console plus the VMware Workstation GUI.

.. note::

   |CL| is not an officially supported OS for VMware Workstation. This tutorial
   follows the generic installation instructions with details specific to a
   manual installation on |CL|.

Prerequisites
*************

Sure virtualization is enabled in the BIOS before installing VMware Workstation.

Install DKMS
************

.. include:: ../guides/kernel/kernel-modules-dkms.rst
   :start-after: kernel-modules-dkms-install-begin:
   :end-before: kernel-modules-dkms-install-end:

Install Hypervisor
******************

Use the console installer to install the VMware Workstation hypervisor:

#. Download
   `Workstation 15.5 Pro for Linux <https://www.vmware.com/products/workstation-pro/workstation-pro-evaluation.html>`_.

#. In a terminal, :command:`cd` to the directory where the `.bundle` installation
   file was saved.

#. Extract the VMware Workstation installer.
   Substituting the file name, enter the command:

   .. code-block:: bash

      sudo sh VMware-Workstation-xxxx-xxxx.architecture.bundle

   .. code-block:: console

	  Extracting VMware Installer...done.

#. When prompted to specify system service scripts directory, use the common
   suggestion:

   .. code-block:: console

	  System service scripts directory (commonly /etc/init.d).: /etc/init.d

#. You will see output similar to the following:

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
	  script directories" being given. This can be safely ignored as |CL| uses
	  :command:`systemd`.


Finish Installation
*******************

Launch the VMware Workstation Pro GUI to finish the installation and build the
needed kernel modules.

#. On the |CL| desktop, find the VMware Workstation icon and click to launch.

#. Click through the installation customization screens as directed in the
   installer.

#. On the last screen click :guilabel:`Finish`. VMware Workstation will launch.

#. Create and configure a new VM!

Troubleshooting
***************

If problems occur during installation, the recommended first step is to identify
which major component the issues are occurring in (hypervisor or kernel modules).
This will help direct further troubleshooting.

Troubleshooting tips:

* If the issue is with compiling the kernel modules and you are running the native
  kernel, try building VMware using the LTS kernel instead.

* To show if modules failed to load, check logs in :file:`tmp/vmware-<username>/*.log`

* To try re-installing all VMware modules run the following command:

  .. code-block:: bash

     vmware-modconfig --console --install-all
