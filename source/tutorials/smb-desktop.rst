.. _smb-desktop:

Samba\* as a client
###################

This tutorial explains how to access an existing shared drive on
Windows\* via Server Message Block (SMB) / Common Internet File System (CIFS)
from the |CL| GNOME desktop.  CIFS filesystem is generally used to access
shared storage locations, or share files.

Prerequisites
*************

* You have already `set up a shared location on Windows`_

Connect to Windows shared location with Nautilus
************************************************

#. From the desktop, select :guilabel:`Files` from the application menu.

   .. note::

   	  GNOME Files is also known as `Nautilus`.

#. In :guilabel:`Files`, select :guilabel:`Other Locations`.

   .. figure:: /_figures/samba/smb-desktop-1.png
      :scale: 100%
      :alt: Files, Other Locations

      Figure 1: Files, Other Locations

#. In the lower taskbar, beside :guilabel:`Connect to Server`,
   enter the file-sharing address using the Windows sharing schema:

   .. code-block:: bash

	    smb://servername/Share

   .. figure:: /_figures/samba/smb-desktop-2.png
      :scale: 100%
      :alt: Connect to Server

      Figure 2: Connect to Server

#. Optional: If there are issues with DNS, you can use an IP address in
   place of the `servername` above. You must still specify the share.

#. Optional: On the Windows machine, in a CLI, retrieve the IP address by
   entering the command:

   .. code-block:: bash

      ifconfig

   .. note::

      If using the IP address, assure that it is accessible and secure.

#. Select :guilabel:`Connect`.

#. The server will request authentication, as shown in Figure 3.

   .. figure:: /_figures/samba/smb-desktop-3.png
      :scale: 100%
      :alt: Authentication

      Figure 3: Authentication

#. Log in with the same Windows system credentials for which you granted
   access to the share.

#. Select the appropriate checkbox to save your credentials. Consider
   carefully the security risks as a result of your selection.


.. _set up a shared location on Windows: https://www.howtogeek.com/176471/how-to-share-files-between-windows-and-linux/



