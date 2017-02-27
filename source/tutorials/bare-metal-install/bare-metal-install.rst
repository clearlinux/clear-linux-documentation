.. _bare-metal-install:

Clear Linux host OS install on bare metal
#########################################

Verify your system hardware is supported by |CLOSIA|. |CL| can run on all
Intel® 64bit processors which support UEFI\* and SSE\* v4.1 streaming SIMD\*
instructions. The following processor families can run |CL|:

* 2nd Generation, or later, Intel® Core™ processor family.
* Intel® Xeon® Processor E3
* Intel® Xeon® Processor E5
* Intel® Xeon® Processor E7
* Intel® Atom™ processor C2000 product family for servers -- Q3 2013 version
  or later.
* Intel® Atom™ processor E3800 series -- Q4 2013 version or later.

Additionally, all the steps of this tutorial were tested using a NUC6i5SYH
Intel® NUC. Visit the `NUC6i5SYH product page`_ for detailed information.

If you are unsure whether or not your system is compatible with |CL|, you can
follow these instructions to find out.

.. toctree::
    :maxdepth: 1

    compatibility-check.rst

.. note::

   Only a system running a Linux distribution can run the compatibility
   check. There are two options:
   * Install and run a Linux distribution directly on your system.
   * Run a live image from a USB stick.

.. _bootable-usb:

Create a Clear Linux bootable USB drive
=======================================

This procedure was created on an Ubuntu 16.04-based system where the USB
drive is identified as :file:`/dev/sdb`. Make sure to map your correct USB
device for this process. We recommend you use an 8GB USB drive or larger.
Copying the |CL| image onto the USB drive formats the drive as a UEFI boot
device. Therefore, the contents of the USB drive will be destroyed during the
creation of the bootable USB drive. Make sure to save anything stored in the
drive before proceeding.

Download the Latest Clear Linux Image
-------------------------------------

Get the latest available |CL| installer image that you want to install
to your system by using your web browser and downloading the latest
:file:`clear-[release]-installer.img.xz` file from
https://download.clearlinux.org/image/ where `[release]` is the release
number of the current image that is available in this directory listing.

This example uses release 10980 so we will download the
:file:`clear-10980-installer.img.xz` image file and, optionally, the
:file:`clear-10980-installer.img.xz-SHA512SUMS` file needed to verify the
download.

To verify the download, follow these steps:

1. Go to the directory with the downloaded files.
2. To verify the integrity of the file, enter the following commands:

   .. code-block:: console

      sha512sum ./clear-10980-installer.img.xz>sha.tmp
      diff clear-10980-installer.img.xz-SHA512SUMS sha.tmp

If the files differ, the diff command outputs the difference to the console,
otherwise, diff does not have any output to the console and returns you to
the command prompt.

3. Once the downloaded file is verified, delete the :file:`sha.tmp` file with
   the following command:

.. code-block:: console

    rm sha.tmp

Copy the Clear Linux image to a USB drive
-----------------------------------------

This example assumes that the USB drive is connected to your system as
:file:`/dev/sdb` and is not mounted.

To ensure the device is not mounted, enter the following command:

.. code-block:: console

   umount /dev/sdb

To log in as root, simply enter:

.. code-block:: console

   su

Once prompted, enter your root password.

To extract the downloaded image file and put it on the USB drive, enter the
following command:

.. code-block:: console

   xzcat –v clear-10980-installer.img.xz | dd of=/dev/sdb

.. note::

   These commands only work in the directory containing the downloaded file.

The decompression and copy of the image file takes some time to complete and
the –v option for xzcat displays the progress.

Once the image has been decompressed and copied to the USB drive, you can
remove the USB drive from the system and move it to your target system.


Install Clear Linux on your target system
=========================================

The USB drive that was created in the previous step has been formatted as a
UEFI boot device. Our target system has a hard drive installed containing a
single primary partition. The target system needs a wired Internet connection
with DHCP.

Follow these steps to install |CL| on the target system:

1. Insert the USB drive into an available USB slot.

2. Power on the system.

3. Open the system BIOS setup menu, normally by pressing the F2 key. Your
   BIOS setup menu entry point may vary.

4. In the setup menu, enable the UEFI boot and set the USB drive as the first
   option in the device boot order.

5. Save these settings and exit.

6. Reboot the target system and the |CL| Installer menu will start.

.. note::

   Use the arrow keys, space bar, and enter key to navigate the menu of the
   |CL| Installer.

7. In this tutorial, we will enable telemetrics and select the `Automatic`
   installation type.

The primary drive to install |CL| onto is :file:`/dev/sdb` since the
target system identifies the USB drive as :file:`/dev/sda`.

8. Follow the instructions to begin the installation.

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

9. Press enter once the <OK> prompt appears. The following dialog box takes
   its place:

.. code-block:: console

   Successful installation, the system will be rebooted

   <OK>

10. Press enter, remove the USB drive from the system, and the system will
    reboot running |CL|.

Clear Linux initial setup after installation
============================================

Your newly installed |CL| boots on your target system and presents a full
screen console requesting `Login:`. |CL| is designed to install with minimal
software overhead. Therefore, some housekeeping and package installations
must occur before you have a full-featured |CL| operating system.

Set up your root and user accounts
----------------------------------

1. At the initial login prompt, enter: root
2. Once you are prompted, enter a new password
3. Re-enter the password to verify it.

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

1. To add `<userid>` to the wheel group, enter the following command:

   .. code-block:: console

      usermod -G wheel -a <userid>

2. To open the :file:`/etc/sudoers` file, enter the following command:

   .. code-block:: console

      vi /etc/sudoers

.. note::

   Normally, we would use the visudo script to edit the :file:`/etc/sudoers`
   file to safely modify the contents of the file. In this instance, the file
   does not exist yet. Therefore, we create the initial instance of the file.

3. In the vi\* editor window, press the :kbd:`o` to open a new line.

4. Add the following line to the file:

   .. code-block:: console

      %wheel ALL=(ALL) ALL

5. To save the changes to the file and exit vi, press the :kbd:`ESC` key
   followed by the :kbd:`:` and :kbd:`x` keys.

.. important::

   Creating the file logged as the root user keeps the permissions of the
   file with the root user.

Now, we can log out of root and into our new <userid>.

To log off as root, enter :command:`exit`.

The command should bring you back to the `Login:` prompt.

Enter your new `<userid>` and the password you created earlier.

You should now be in the home directory of `<userid>`. The bundle
`os-clr-on-clr`_ contains the majority of applications that a developer or
system administrator would want but it does not include a graphical user
interface. The `os-utils-gui` bundle includes the XFCE graphical user
interface.

To test the :command:`sudo` command and ensure we set it up correctly, we can
install the XFCE :abbr:`GUI (graphical user interface)`.

To install XFCE using swupd, enter the following command:

.. code-block:: console

   sudo swupd bundle-add os-utils-gui

To start xfce, enter the following command:

.. code-block:: console

   startx

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

We have created a :ref:`tutorial <web-server-install>` for setting up your
|CL| system as a :abbr:`LAMP (Linux, Apache MySQL, PHP)` web sever.

Once you have setup your system as a web server, we recommend you try out our
:ref:`tutorial on installing WordPress <wp-install>` to host your own
CMS-based website on your |CL| system.

.. _`NUC6i5SYH product page`:
   http://www.intel.com/content/www/us/en/nuc/nuc-kit-nuc6i5syh.html

.. _`information about swupd`:
   https://clearlinux.org/documentation/swupdate_about_sw_update.html

.. _`os-clr-on-clr`:
   https://github.com/clearlinux/clr-bundles/blob/master/bundles/os-clr-on-clr

.. _`all Clear Linux bundles`:
   https://github.com/clearlinux/clr-bundles/tree/master/bundles

.. _`wheel group`:
   https://en.wikipedia.org/wiki/Wheel_(Unix_term)
