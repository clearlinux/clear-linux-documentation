.. _clear-samba-share-to-Windows:

Enabling simple file sharing from Clear Linux to a Windows machine using Samba
##############################################################################

This guide covers the steps you need to enable simple file sharing
from |CLOSIA| to Windows. For more advanced sharing, please refer to the
`Samba guide`_.

#.	Follow the :ref:`install-on-target` guide to install |CL|.
#.	Add the storage-utils bundle, which includes the Samba binaries, after |CL|
	is setup. The os-clr-on-clr bundle also includes the Samba binaries.

	.. code-block:: console

		$sudo swupd bundle-add storage-utils

#.	Create a configuration file at :file:`/etc/samba/smb.conf` and add the following
	(change as needed). The following configuration has two simple examples.
        The first example demonstrates sharing a folder to a specific user and
        the second example demonstrates sharing a folder to anyone. The examples
	assume that a user account named "clearlinuxuser" already exists.
	If "valid users" is not specified as shown, then anyone with a user account
	on this machine and with their Samba password set can access the files.
        However, that account is only able to access files and folders that the
        account has permission to on the system. Use :command:`chown`
	or :command:`chmod` to change either the owner of the file or the
	permissions to allow other users to access that file.

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

#.	As root user, enable the Samba daemon so that it starts every time.

	.. code-block:: console

		# systemctl enable smb
		# systemctl start smb

#.	Samba maintains its own list of passwords for user accounts. This list
        of passwords can be different than the password used to log in. As root
        user, use :command:`smbpasswd` to add the initial password needed by
        the user account to access the share.

	.. code-block:: console

		# smbpasswd -a clearlinuxuser

#. 	At this point, a Windows machine on the same network can
	access the shares. Windows uses the `\\\\[server IP or hostname]\\folder`
	format to access shares. This access is done either directly using
        Windows Explorer or by mapping the drive to a letter in Windows.
        It is easiest to use the IP address of the machine to access it.
        However, you can use the hostname of the |CL| machine as long as it is
        behind an Active Directory domain controller or is behind a DNS server.
        For other ways to access the shares using a hostname instead of an IP address,
        consult `Chapter 7 of the Samba guide`_.

Mapping |CL| drive in Windows
*****************************

#.	Open up Windows Explorer and click on the left sidebar on :guilabel:`This PC`
	to change the options available at the top.
#.	Choose the :guilabel:`Map network drive` icon and put
	in the path as `\\\\[server IP or hostname]\\[shared folder]`.
#.	Check the box :guilabel:`Connect Using Different Credentials` to put in the Samba
	user defined above "clearlinuxuser" and the password created with
	:command:`smbpasswd`. See Figure 1 and Figure 2.

	.. figure:: figures/smb-1.png
		:scale: 70%
		:alt: Mapping a share in Windows Explorer

		Figure 1: Mapping a share in Windows Explorer

	.. figure:: figures/smb-2.png
		:scale: 70%
		:alt: Mapping a share in Windows Explorer

		Figure 2: Mapping a share in Windows Explorer





.. _Samba guide: https://www.samba.org/samba/docs/using_samba/ch00.html
.. _Chapter 7 of the Samba guide: https://www.samba.org/samba/docs/using_samba/ch07.html
