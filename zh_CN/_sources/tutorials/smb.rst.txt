.. _clear-samba-share-to-Windows:

Samba\* as a host
#################

This tutorial describes how to enable simple file sharing from a system
running |CL-ATTR| to a Windows machine using Samba. For more advanced sharing,
refer to the `Samba guide`_.

Prerequisites
*************

This tutorial assumes you have installed |CL| on your host system. For
detailed instructions, follow the steps in :ref:`bare-metal-install-desktop`.

Before you install any new packages, update |CL| with the following command:

.. code-block:: bash

   sudo swupd update


Set up file sharing
*******************

#.	Log in and get root privileges.

	.. code-block:: bash

		sudo -s

#.	Add the storage-utils bundle, which includes the Samba binaries.

	.. code-block:: bash

		swupd bundle-add storage-utils

	.. note::

		The os-clr-on-clr bundle also includes the Samba binaries.

#.	Create a configuration file called :file:`/etc/samba/smb.conf`. In this
	example, `[Downloads]` enables a folder share with a specific user.
	`[Documents]` enables a folder share with any user. The example assumes that a
	user account `clearlinuxuser` already exists.

	If `valid users` is not specified, then anyone with a user account on the
	machine and with their Samba password already set can access the folder.
	However, the account is only able to access files and folders for which
	they have appropriate permissions.

	Use :command:`chown` or :command:`chmod` to change either the owner of the
	file or the permissions to allow other users to access the file.

	.. code-block:: console

		[Global]
		map to guest = bad user

		[Downloads]
		path=/home/clearlinuxuser/Downloads
		read only = no
		guest ok = no
		valid users = clearlinuxuser

		[Documents]
		path=/home/clearlinuxuser/Documents
		read only = no
		browsable = yes
		guest ok = yes

#.	Enable the Samba daemon to start every time.

	.. code-block:: bash

		systemctl enable smb
		systemctl start smb

#.	Use :command:`smbpasswd` to add the initial password for the user
	account to access the share. Be aware that Samba maintains its own list of
	passwords for user accounts. The Samba password list can be different than
	the password used to log in.

	.. code-block:: bash

		smbpasswd -a clearlinuxuser

Setup is complete and a Windows machine on the same network can access the
shares. Windows uses the format :file:`\\\\[server IP or hostname]\\folder` to
access shares. Access the shares directly with Windows Explorer or by
mapping a network drive.

Use the IP address of the |CL| machine for an easy access method. If the
|CL| machine is behind an Active Directory domain controller or a DNS server,
use the hostname of the |CL| machine. For other ways to access shares using a
hostname instead of an IP address, see `Chapter 7 of the Samba guide`_.


Map |CL| drive in Windows
*************************

#.	Open Windows Explorer and click on the left sidebar on :guilabel:`This PC`
	to change the options available at the top.

#.	Click the :guilabel:`Map Network Drive` icon and enter the path in the
	format: :file:`\\\\[server IP or hostname]\\[shared folder]`

#.	Check the box :guilabel:`Connect using different credentials`. Enter
	the Samba user `clearlinuxuser` and the password created with
	:command:`smbpasswd`. See Figure 1 for details.

	.. figure:: /_figures/samba/smb-1.png
		:scale: 70%
		:alt: Map a network drive in Windows Explorer

		Figure 1: Map a network drive in Windows Explorer.

When complete, Windows Explorer displays the share drive as shown in Figure 2.

.. figure:: /_figures/samba/smb-2.png
	:scale: 70%
	:alt: View a share drive in Windows Explorer

	Figure 2: View a share drive in Windows Explorer.





.. _Samba guide: https://www.samba.org/samba/docs/using_samba/ch00.html
.. _Chapter 7 of the Samba guide: https://www.samba.org/samba/docs/using_samba/ch07.html
