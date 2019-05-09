.. _flatpak:

Use Flatpak\* to install applications on |CL-ATTR|
##################################################

This tutorial provides all the required steps to install Flatpak as well as
downloading, installing, and running LibreOffice\* on |CL-ATTR|.

Please visit the `Flatpak website`_ for more information about Flatpak and
how to use it. You can also `download it here`_.

Before you begin
****************

This tutorial assumes you have installed |CL| on your host system.
For detailed instructions on installing |CL| on a bare metal system, visit
our :ref:`bare metal installation tutorial<bare-metal-install-server>`.

Install Flatpak on your host system
===================================

Flatpak is included as part of the bundle `desktop`. To install the
application, log in to your user account and enter the following command:

.. code-block:: bash

   sudo swupd bundle-add desktop


Install and run the LibreOffice Flatpak image
=============================================

Application developers have the option to bundle their applications using
Flatpak to allow the installation of a single distribution of their
application on different distributions of Linux, including |CL|.
Flatpak provides a `list of applications`_ available through Flathub.

|CL| enables the Flathub repository by default.


Installing using gnome software
-------------------------------

All you need to do is to launch `gnome software`, search for the LibreOffice
app, and click the install button.

.. figure:: figures/01-install-libreoffice.gif
   :alt: install libreoffice step by step

   Figure 1: Installing LibreOffice using gnome-software



Installing using the command line
---------------------------------

Open the `gnome-terminal` and type the following command to install the
LibreOffice app.

.. code-block:: bash

   flatpak install --user flathub org.libreoffice.LibreOffice
   Installing in user:
   org.libreoffice.LibreOffice/x86_64/stable        flathub 2aff77bd5cf1
     permissions: ipc, network, pulseaudio, wayland, x11, dri
     file access: host, xdg-run/dconf
     dbus access: ca.desrt.dconf, org.gtk.vfs.*
     dbus ownership: org.libreoffice.LibreOfficeIpc0
   org.libreoffice.LibreOffice.Locale/x86_64/stable flathub 924157b3b009
   Is this ok [y/n]: y
   Installing for user: org.libreoffice.LibreOffice/x86_64/stable from flathub
   [####################] 403 metadata, 4661 content objects fetched; 222574 KiB transferred in 99 seconds
   Now at 2aff77bd5cf1.
   Installing for user: org.libreoffice.LibreOffice.Locale/x86_64/stable from flathub
   [####################] 10 metadata, 71 content objects fetched; 1013 KiB transferred in 3 seconds
   Now at 924157b3b009.


Launch LibreOffice
==================
A new set of icons will appear in your Gnome applications list titled :guilabel:`LibreOffice.` To
execute the application, highlight the application and click on the :guilabel:`LibreOffice` icon.
LibreOffice will start normally.

.. figure:: figures/02-openlibreoffice.gif
   :alt: Opening LibreOffice app

   Figure 2: Select :guilabel:`LibreOffice` app

Using the command line
----------------------

.. code-block:: bash

   flatpak run org.libreoffice.LibreOffice


.. _Flatpak website: http://flatpak.org

.. _list of applications: http://flatpak.org/apps.html

.. _download it here:
   http://download.documentfoundation.org/libreoffice/flatpak/latest/LibreOffice.flatpak

