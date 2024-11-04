.. _flatpak-tutorial:

Flatpak\*
#########

This tutorial shows how to install a `Flatpak`_ app on |CL| using GNOME\* Software
and the command line.

.. contents::
   :local:
   :depth: 1

Description
***********

`Flatpak`_ is a framework for building and distributing desktop apps on
Linux\*. Flatpak allows you to build a single app and install it on different
distributions of Linux. Flatpak apps are available through `Flathub`_ or the
`Clear Linux Store`_.

Prerequisites
*************

* |CL| installed on host system

  Refer to :ref:`Get started <get-started>` for installation instructions.

* `desktop-autostart` bundle installed

  Flatpak is included via `desktop`, which is included in the
  `desktop-autostart` bundle. The Flathub repository is pre-configured when
  the `desktop-autostart` bundle is installed.

  Install the `desktop-autostart` bundle with the following command:

  .. code-block:: bash

     sudo swupd bundle-add desktop-autostart

Install a Flatpak app with GNOME Software
*****************************************

|CL| desktop comes with GNOME Software installed. Flatpak apps can be
installed from within GNOME Software.

#. Launch GNOME Software from your desktop.

#. Search for the Flatpak app that you want to install, as shown in Figure 1.

   .. figure:: /_figures/flatpak/flatpak-01.png
      :scale: 50%
      :alt: Searching for Filezilla app in GNOME Software

      Figure 1: Searching for Filezilla\* app in GNOME Software

#. When you find the app you want to install, click it to view application
   details.

#. On the app detail page, click the :guilabel:`Install` button, as shown in
   Figure 2.

   .. figure:: /_figures/flatpak/flatpak-02.png
      :scale: 50%
      :alt: Filezilla Flatpak detail page in GNOME Software

      Figure 2: Filezilla Flatpak detail page in GNOME Software

#. After installation is complete, the new application will be in your
   GNOME applications list, as shown in Figure 3.

   .. figure:: /_figures/flatpak/flatpak-03.png
      :scale: 50%
      :alt: Newly installed Filezilla application

      Figure 3: Newly installed Filezilla application

#. Click the application icon to launch the application.

Install a Flatpak with the command line
***************************************

Both Flathub and the Clear Linux Store provide the command line instructions
for installing a Flatpak. Figure 4 shows the command line instructions to
install Filezilla\* from the Clear Linux Store:

.. figure:: /_figures/flatpak/flatpak-04.png
   :scale: 50%
   :alt: Command line instructions to install Filezilla from the Clear Linux Store

   Figure 4: Command line instructions to install Filezilla from the Clear Linux Store

In this example, we install Filezilla.

#. Open a terminal and enter the install command for the desired app:

   .. code-block:: bash

      flatpak install flathub org.filezillaproject.Filezilla

   You may be prompted to select which repository to use:

   .. code-block:: bash

      Looking for matches…
      Remote ‘flathub’ found in multiple installations:

         1) system
         2) user

      Which do you want to use (0 to abort)? [0-2]: 2

      org.filezillaproject.Filezilla permissions:
          ipc      network              ssh-auth             wayland      x11
          dri      file access [1]      dbus access [2]

          [1] host, xdg-run/dconf, ~/.config/dconf:ro
          [2] ca.desrt.dconf, org.freedesktop.Notifications, org.freedesktop.PowerManagement,
              org.gnome.SessionManager


              ID                                       Arch      Branch    Remote    Download
       1. [✓] org.filezillaproject.Filezilla           x86_64    stable    flathub   11.5 MB / 11.5 MB
       2. [✓] org.filezillaproject.Filezilla.Locale    x86_64    stable    flathub    4.6 kB / 3.8 MB

      Installation complete.

#. After installation, run the application with the following command:

   .. code-block:: bash

      flatpak run org.filezillaproject.Filezilla

.. _Flatpak: https://flatpak.org
.. _Flathub: https://flathub.org
.. _Clear Linux Store: https://clearlinux.org/software
