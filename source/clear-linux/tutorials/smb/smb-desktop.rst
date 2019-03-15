.. _smb-desktop:

Connect to Windows\* share from |CL-ATTR| desktop
#################################################

This tutorial explains how to access an existing shared location on Windows\* via SMB in the |CL-ATTR| GNOME GUI desktop.

Prerequisites
*************

* You have already `set up a shared location on Windows`_

Connect to Windows shared location with Nautilus
************************************************

#. From the desktop, select :guilabel:`Files` from the application menu.

   .. note::

   	  GNOME Files is also known as `Nautilus`.


#. In :guilabel:`Files`, select :guilabel:`Other Locations`.

   .. figure:: figures/smb-desktop-1.png
  	  :scale: 100%
	  :alt: Files, Other Locations

	  Figure 1: Files, Other Locations

#. In the taskbar at bottom beside :guilabel:`Connect to Server`,
   enter the file-sharing address using the Windows sharing schema:

   .. code-block:: bash

	  smb://servername/Share


   .. figure:: figures/smb-desktop-2.png
  	  :scale: 100%
	  :alt: Connect to Server

	  Figure 2: Connect to Server

   #. Optional: If there are issues with DNS, you can use an IP address in
      place of the server name. You must still specify the share.

   #. On the Windows machine, in a CLI, retrieve the IP address by entering
      the command:

	  .. code-block:: bash

	     ifconfig

#. Select :guilabel:`Connect`.

#. The server will request authentication, as shown in Figure 3.

   .. figure:: figures/smb-desktop-3.png
  	  :scale: 100%
	  :alt: Authentication

	  Figure 3: Authentication

#. Log in with the same Windows system credentials for which you granted
   access to the share.

#. Select the appropriate checkbox to save your credentials. Consider
   carefully the security risks as a result of your selection.


.. _set up a shared location on Windows: https://www.howtogeek.com/176471/how-to-share-files-between-windows-and-linux/



