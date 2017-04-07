.. _flatpak:

Use Flatpak\* to install applications on |CLOSIA|
#################################################

This tutorial provides all the required steps to install Flatpak as well as
downloading, installing, and running LibreOffice on |CL|.

Please visit the `Flatpak website`_ for more information about Flatpak and
how to use it.

Before you begin
================

This tutorial assumes you have installed |CL| on your host system.
For detailed instructions on installing |CL| on a bare metal system, visit
our :ref:`bare metal installation tutorial<bare-metal-install>`.

Install Flatpak on your host system
===================================

Flatpak is included as part of the bundle `os-utils-gui`. To install the
application, log in to your user account and enter the following command:

.. code-block:: console

   $ sudo swupd bundle-add os-utils-gui


Install and run the LibreOffice Flatpak image
=============================================

Application developers have the option to bundle their applications using
Flatpak to allow the installation of a single distribution of their
application on different distributions of Linux, including Clear Linux.
Flatpak provides a `list of applications`_ available through Flatpak.

Download and install the Latest LibreOffice Flatpak
---------------------------------------------------

To get the latest version of the LibreOffice Flatpak repository, either
`download it here`_ or you can enter the following command:

.. code-block:: console

   $ curl –O http://download.documentfoundation.org/libreoffice/flatpak/latest/LibreOffice.flatpak

The command downloads the latest LibreOffice.flatpak and saves it in your
current directory.

Once the download is complete, the next step is to install LibreOffice along
with the runtime environment LibreOffice needs to execute. As mentioned on
the `Flatpak website`_, with the release of Flatpak 0.8.0 and
LibreOffice.flatpak 4.2.4, you no longer have to specifically install the
runtime required to execute LibreOffice since it will automatically install
the runtime referenced in the LibreOffice.flatpak file.

To install LibreOffice run the following command:

.. code-block:: console

   $ sudo flatpak install --bundle LibreOffice.flatpak

The output from this command will look similar to the following.

.. note::

   You will be prompted to install the runtime environment if it is not
   already installed.  Type :kbd:`y` to allow this task to execute.

.. code-block:: console

   GLib-GIO-Message: Using the 'memory' GSettings backend.
   Your settings will not be saved or shared with other applications.
   This application depends on runtimes from:
   http://sdk.gnome.org/repo/
   Configure this as new remote 'gnome' [y/n]: y
   Required runtime for org.libreoffice.LibreOffice/x86_64/fresh
   (org.gnome.Platform/x86_64/3.20) is not installed, searching...
   Found in remote gnome, do you want to install it? [y/n]: y
   Installing: org.gnome.Platform/x86_64/3.20 from gnome

   Receiving delta parts: 0/11 2.5 MB/s 4.9 MB/223.2 MB 1 minutes 28 seconds
   remain
   Receiving delta parts: 0/11 2.9 MB/s 8.7 MB/223.2 MB 1 minutes 13 seconds
   remain
   11 delta parts, 84 loose fetched; 218002 KiB transferred in 17 seconds
   Installing: org.gnome.Platform.Locale/x86_64/3.20 from gnome

   5 metadata, 1 content objects fetched; 13 KiB transferred in 1 seconds
   Installing: org.libreoffice.LibreOffice/x86_64/fresh from bundle
   LibreOffice.flatpak

Once the LibreOffice Flatpak application has been installed, you can launch
LibreOffice with the following command from the command line:

.. code-block:: console

   $ flatpak run org.libreoffice.LibreOffice

Add LibreOffice to your Xfce desktop
====================================

To add a LibreOffice launcher to the XFCE desktop, right click your mouse
anywhere on the XFCE desktop. The dialog box shown in figure 1 pops up.
Several options are available, including creating a launcher. In the dialog
box, select :guilabel:`Create Launcher`.

.. figure:: figures/flatpak1.png
   :alt: XFCE desktop contextual menu

   Figure 1: Select :guilabel:`Create Launcher`

The :guilabel:`Create Launcher` dialog appears, see figure 2.

.. figure:: figures/flatpak2.png
    :alt: Create Launcher dialog box

    Figure 2: The :guilabel:`Create Launcher` dialog box

Enter the following data into each field:

   Name:  LibreOffice

   Comment:  LibreOffice

   Command:  flatpak run org.libreoffice.LibreOffice

   Working Directory: $HOME

   Icon:    Click on the :guilabel:`No icon` field to bring up a list of
   available icons, see figure 2. In the :guilabel:`Search icon:` field, enter
   ``Libreoffice-main.`` Click the :guilabel:`libreoffice-main` icon in the
   window and select :guilabel:`OK`.

   .. figure:: figures/flatpak3.png
      :alt: Select an icon

      Figure 3: Select an icon dialog box.

   Options:  Leave the :guilabel:`Use startup notification` and
   :guilabel:`Run in terminal` unchecked.

Once all the fields have been filled out, click on the :guilabel:`Create`
button.

A new icon appears on your XFCE desktop titled :guilabel:`LibreOffice.` To
execute the application, double click on the :guilabel:`LibreOffice` icon. A
dialog appears stating: The application is an untrusted application launcher,
the application is in an insecure location, and not marked as executable.
Select the :guilabel:`Mark Executable` to ensure this dialog box will no
longer appear every time you launch the application.

LibreOffice starts normally.

.. _Flatpak website: http://flatpak.org

.. _list of applications: http://flatpak.org/apps.html

.. _dowload it here:
   http://download.documentfoundation.org/libreoffice/flatpak/latest/LibreOffice.flatpak

