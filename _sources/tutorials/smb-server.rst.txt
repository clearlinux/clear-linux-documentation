.. _smb-server:

Samba Server
############

This tutorial describes how to enable simple file sharing on a system
running |CL-ATTR| and how to access the share from clients on other operating 
systems. 

.. contents::
   :local:
   :depth: 1

Prerequisites
*************

* |CL| is installed on your host system.

  For detailed instructions, follow one of these guides:

  * *Desktop* version: :ref:`bare-metal-install-desktop`
  * *Server* version: :ref:`bare-metal-install-server`

* Update your |CL| system to the latest version. 

  .. code-block:: bash

     sudo swupd update

Set up file sharing
*******************

#. Add the :command:`samba` bundle, which includes the Samba binaries.

   .. code-block:: bash

      sudo swupd bundle-add samba

#. Create the :file:`/etc/samba` directory.

   .. code-block:: bash

      sudo mkdir /etc/samba

#. Create a configuration file named :file:`/etc/samba/smb.conf`. In this
   simple example, :envvar:`[SharedDrive]` enables a folder share located in 
   :file:`/home/clear/mysharedrive` granting users `samba-user-1` and 
   `samba-user-2` access. 

   If :envvar:`valid users` is not specified, then anyone with a user account
   on the machine and with their Samba password already set can access the
   folder. However, the account is only able to access files and folders for
   which they have appropriate permissions.

   For more advanced sharing, refer to the `Samba guide`_.

   .. code-block:: console

      [Global]
      map to guest = Bad User

      [SharedDrive]
      path=/home/clear/myshareddrive
      read only = no
      guest ok = no
      browsable = yes
      valid users = samba-user-1 samba-user-2

#. Start the Samba service and set it to start automatically on boot.

   .. code-block:: bash

      sudo systemctl enable --now smb

#. Verify the service started properly.

   .. code-block:: bash

      sudo systemctl status smb

#. Use :command:`smbpasswd` to add the initial password for the user
   account to access the share. Be aware that Samba maintains its own list of
   passwords for user accounts. The Samba password list can be different from
   the password used to log in.

   For example:

   .. code-block:: bash

      sudo smbpasswd -a samba-user-1

Access the shared drive
***********************

Depending on your operating system, connect to the shared drive using one 
of the methods belows:

* On |CL|:

  a. Add the `samba` bundle.

     .. code-block:: bash

        sudo swupd bundle-add samba
  
  #. List available shares.

     .. code-block:: bash

        smbclient -L //<ip-address-of-smb-server>

  #. Connect to a shared drive.
     
     .. code-block:: bash

        smbclient //<ip-address-of-smb-server>/<shared-drive> -U <user>

* On Windows:

  a. Open `File Explorer`.

  #. Enter :command:`\\<ip-address-of-samba-server>\<shared-drive>` in the
     URL field. See Figure 1.

     .. rst-class:: dropshadow

     .. figure:: ../_figures/samba/smb-server-01.png
        :scale: 100%
        :alt: Windows > File Explorer > Connect to Samba share

        `Figure 1: Windows > File Explorer > Connect to Samba share`

* On macOS:

  a. Open the `Finder`.

  #. Press :kbd:`Command` + :kbd:`K` to open the dialog box for 
     connecting to a server.

  #. Enter :command:`smb://<ip-address-of-samba-server>/<shared-drive>`.
     in the URL field. See Figure 2.

     .. figure:: ../_figures/samba/smb-server-02.png
        :scale: 100%
        :alt: macOS > Finder > Connect to Samba share

        `Figure 2: macOS > Finder > Connect to Samba share`
     
.. _Samba guide: 
   https://www.samba.org/samba/docs/using_samba/ch00.html
