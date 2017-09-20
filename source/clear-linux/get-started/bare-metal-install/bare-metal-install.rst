.. _bare-metal-install:

Install Clear Linux host OS on bare metal
#########################################

This instruction set will guide you through the automatic installation of |CL|
on bare metal using a bootable USB drive.

.. include:: ../compatibility-check.rst
   :Start-after: compatibility-check:

.. include:: ../bootable-usb/bootable-usb-linux.rst
   :Start-after: bootable-usb-linux:
   :end-before: download-cl-image

.. include:: ../bootable-usb/bootable-usb-linux.rst
   :Start-after: download-cl-image:
   :end-before: copy-usb-linux

.. include:: ../bootable-usb/bootable-usb-linux.rst
   :Start-after: copy-usb-linux:
   :end-before: usb-next

.. _install-on-target:

Install Clear Linux on your target system
=========================================

The USB drive that was created in the previous step has been formatted as a
UEFI boot device. Our target system has a hard drive installed containing a
single primary partition. The target system needs a wired Internet connection
with DHCP.

Follow these steps to install |CL| on the target system:

#. Insert the USB drive into an available USB slot.

#. Power on the system.

#. Open the system BIOS setup menu, normally by pressing the F2 key. Your
   BIOS setup menu entry point may vary.

#. In the setup menu, enable the UEFI boot and set the USB drive as the first
   option in the device boot order.

#. Save these settings and exit.

#. Reboot the target system and the |CL| Installer menu will start.

   .. note::

      Use the arrow keys, space bar, and enter key to navigate the menu of the
      |CL| Installer.

#. In this tutorial, we will enable telemetrics and select the `Automatic`
   installation type.

   The primary drive to install |CL| onto is :file:`/dev/sdb` since the
   target system identifies the USB drive as :file:`/dev/sda`.

#. Follow the instructions to begin the installation.

   The installation is completed in the following stages:

   .. code-block:: console

      Reading configuration
      Validating configuration
      Creating partitions
      Creating file systems
      Setting up mount points
      Starting swupd.  May take several minutes
      Cleaning up
      Successful installation

   Once complete, an `<OK>` prompt appears in the dialog box, letting you know
   that you have successfully installed |CL| onto your system.

#. Press enter once the <OK> prompt appears. The following dialog box takes
   its place:

   .. code-block:: console

      Successful installation, the system will be rebooted

      <OK>

#. Press enter, remove the USB drive from the system, and the system will
    reboot running |CL|.

.. _initial-setup:

Clear Linux initial setup after installation
============================================

Your newly installed |CL| boots on your target system and presents a full
screen console requesting `Login:`. |CL| is designed to install with minimal
software overhead. Therefore, some housekeeping and package installations
must occur before you have a full-featured |CL| operating system.

Set up your root and user accounts
----------------------------------

#. At the initial login prompt, enter: root

#. Once you are prompted, enter a new password

#. Re-enter the password to verify it.

You have set your root password and are logged in with root privileges.

The next step is to create a new user and set a password for
that user:

.. code-block:: console

   useradd <userid>
   passwd <userid>

Replace <userid> with the name of the user account you want to create.

Remain logged in as the root user because there are some other things to do
before we can fully enable your new user space.

Software installation and updates
---------------------------------

|CL| has a unique application and architecture to add and update applications
and to perform system updates called software update utility or `swupd`.
Software applications are installed as bundles using the command
:command:`bundle-add`.

Next, we should install some useful applications using the software update
utility. The `os-clr-on-clr` bundle installs the vast majority of
applications useful to a system administrator or a developer. The bundle
contains other bundles such as `sysadmin-basic`, `editors`, `c-basic`, `dev-
utils-dev`, and other useful packages.

.. code-block:: console

   swupd bundle-add os-clr-on-clr

.. note::

   The image we installed may not be the latest version of |CL| available on
   the server. However, whenever the command
   :command:`swupd bundle-add <bundle>` runs, the OS is updated to the latest
   available version. Our website provides more `information about swupd`_.

We provide the full list of bundles and packages installed with the
`os-clr-on-clr`_ bundle. Additionally, we have listed
`all Clear Linux bundles`_, active or deprecated. Click any bundle on the
list to view the manifest of the bundle.

Finish setting up your new user
-------------------------------

Before logging off as root and logging into your new user account, we must
enable the :command:`sudo` command for your new `<userid>`.

To be able to execute all applications with root privileges, we must add the
`<userid>` to the `wheel group`_ and enable the wheel group in the
:file:`/etc/sudoers` file.

#. To add `<userid>` to the wheel group, enter the following command:

   .. code-block:: console

      usermod -G wheel -a <userid>

#. To open the :file:`/etc/sudoers` file, enter the following command:

   .. code-block:: console

      vi /etc/sudoers

   .. note::

      Normally, we would use the visudo script to edit the :file:`/etc/sudoers`
      file to safely modify the contents of the file. In this instance, the file
      does not exist yet. Therefore, we create the initial instance of the file.

#. In the vi\* editor window, press the :kbd:`o` to open a new line.

#. Add the following line to the file:

   .. code-block:: console

      %wheel ALL=(ALL) ALL

#. To save the changes to the file and exit vi, press the :kbd:`ESC` key
   followed by the :kbd:`:` and :kbd:`x` keys.

   .. important::

      Creating the file logged as the root user keeps the permissions of the
      file with the root user.

   Now, we can log out of root and into our new <userid>.

#. To log off as root, enter :command:`exit`.

   The command should bring you back to the `Login:` prompt.

#. Enter your new `<userid>` and the password you created earlier.

   You should now be in the home directory of `<userid>`. The bundle
   `os-clr-on-clr`_ contains the majority of applications that a developer or
   system administrator would want but it does not include a graphical user
   interface. The `desktop` bundle includes the Gnome Desktop Manager and
   additional supporting applications.

Install a GUI
-------------

#. To test the :command:`sudo` command and ensure we set it up correctly, we
   can install the Gnome Desktop Manager (gdm) and start it.

#. To install Gnome using swupd, enter the following command:

   .. code-block:: console

      sudo swupd bundle-add desktop

#. To start the Gnome Desktop Manager, enter the following command:

   .. code-block:: console

      systemctl start gdm

   You will be prompted to authenticate your user.  Enter the password for
   `<userid>` and the Gnome Desktop should start as shown in figure 1:

   .. figure:: figures/gnomedt.png
      :alt: Gnome Desktop

      Figure 1: :guilabel:`Gnome Desktop`

#. To start the Gnome Desktop each time you start your system, enter
   the following command:

   .. code-block:: console

      systemctl enable gdm

**Congratulations!**

You have successfully installed |CL| on a bare metal system.

Additionally, you performed the following basic setup for your system:

* Setup of a root user.
* Updated the OS to its most current version using `swupd`.
* Installed the most common applications for system administrators and
  developers using bundles.
* Setup of a new user.
* Setup of `sudo` privileges for that new user.
* Installed a GUI using those `sudo` privileges.

Next steps
==========

With your system now running |CL| many paths are open for you.

Visit our :ref:`tutorials` page for examples on using your |CL|
system.

.. _`information about swupd`:
   https://clearlinux.org/features/software-update

.. _`os-clr-on-clr`:
   https://github.com/clearlinux/clr-bundles/blob/master/bundles/os-clr-on-clr

.. _`all Clear Linux bundles`:
   https://github.com/clearlinux/clr-bundles/tree/master/bundles

.. _`wheel group`:
   https://en.wikipedia.org/wiki/Wheel_(Unix_term)
