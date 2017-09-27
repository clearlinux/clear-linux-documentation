.. _vnc:

Secure Remote Desktop to a Clear Linux Host by VNC’ing Through an SSH Tunnel
############################################################################

Virtual Network Computing (VNC) is a client-server tool that provides remote 
access of |CLOSIA| through a graphical user interface.  In addition to keyboard 
and mouse events, it transmits the remote host’s display over the network to 
the client system.  

This tutorial shows how to:

* Install the VNC server on a |CL| host
* Configure the server for 2 different VNC-server-start methods
* Install a VNC viewer app on the client system
* Initiate a VNC session and connect it to from a client
* Establish a secure SSH tunnel to encrypt VNC traffic 

Enable the VNC server components on the |CL| host
-------------------------------------------------
#.	Log in and get root privileges.

	.. code-block:: console

		$ sudo -s

#.	Install these bundles and reboot the system to start the necessary services.

	.. code-block:: console

		# swupd bundle-add os-utils-gui openssh-server
		# reboot

	.. note::

		* `os-utils-gui`: to get the TigerVNC server and the XFCE X Display Manager
		* `openssh-server`: to provide SSH functionality
		* The default X Display Manager presented through VNC on |CL| is XFCE.  
		  To use the Gnome Display Manager (GDM) instead, add the `desktop-autostart` 
		  bundle.

Configure the VNC server start methods on the |CL| host
-------------------------------------------------------
There are several methods to start the VNC server on the host before the client 
can connect to it.  The first method requires the user to SSH in and manually 
start it.  The second is to automate the starting of the VNC server by setting up 
a Systemd service script for each user.  Both methods can be deployed 
concurrently on the same host.  

Configuring for these methods are detailed below.   

Method 1: User manually starts the VNC server
*********************************************
Each user must perform these steps to initialize the VNC settings for their use.

#.	Login as the user. 

#.	Create the initial VNC settings.  A password must be set.    

	.. code-block:: console

		$ vncserver 

	Example output:

		.. code-block:: console

			$ vncserver

			You will require a password to access your desktops.

			Password:
			Verify:
			Would you like to enter a view-only password (y/n)? n
			xauth:  file /home/vnc-user-a/.Xauthority does not exist

			New 'clr-linux:2 (vnc-user-a)' desktop is clr-linux:2

			Creating default startup script /home/vnc-user-a/.vnc/xstartup
			Creating default config /home/user-a/.vnc/config
			Starting applications specified in /home/vnc-user-a/.vnc/xstartup
			Log file is /home/vnc-user-a/.vnc/clr-linux:2.log

	Upon completion, VNC will add default configuration files and a password file 
	in a hidden directory (`%HOME/.vnc`) for that user.  

	Also, a VNC session will start.  VNC will show the display ID (the number 
	following the colon ‘`:`’) for this session.  In the above example, the display 
	ID is 2.  The display ID is needed for the client app to specify which session 
	to connect to.  

#.	Kill the VNC session for the time being with this command (substitute 
	`<display-id>` with appropriate value):

	.. code-block:: console

		$ vncserver -kill :<display-id>

	.. note::

		To list active VNC sessions, enter this command:

		.. code-block:: console

			$ vncserver -list

#.	Optional configurations.

	* To customize settings such as screen size, security type, etc., modify 
	  the `%HOME/.vnc/config` file.  
	* To customize the applications to run at startup, modify 
	  the `%HOME/.vnc/xstartup` file.  

	See the `vncserver` Man page for additional information.

Method 2: Automate starting the VNC server on-demand for each user
******************************************************************
To automatically start a VNC session for each user via a Systemd service, the 
system administrator must perform these steps.    

#.	Log in and get root privileges.

	.. code-block:: console

		$ sudo -s

#.	Make sure the user accounts already exit.  Use the following to list all users:

	.. code-block:: console

		# cut -d: -f1 /etc/passwd

#.	Create a service script called `vncserver@:X.service` (where is `X` the display 
	ID) for each user in `/etc/systemd/system`.  Each user is assigned a unique display 
	ID number.  Below is an example showing `vnc-user-b` is assigned a display ID of 
	‘`5`’ via the service filename.  

	.. code-block:: console

		# mkdir -p /etc/system/system
		# cat > /etc/systemd/system/vncserver@:5.service << EOF

		[Unit]
		Description=VNC Remote Desktop Service for VNC-user-b
		After=syslog.target network.target

		[Service]
		Type=simple
		User=vnc-user-b
		PAMName=login
		PIDFile=/home/vnc-user-b/.vnc/%H%i.pid
		ExecStartPre=/bin/sh -c '/usr/bin/vncserver -kill %i > /dev/null 2>&1 || :'
		ExecStart=/usr/bin/vncserver %i -geometry 2000x1200 -alwaysshared -fg
		ExecStop=/usr/bin/vncserver -kill %i

		[Install]
		WantedBy=multi-user.target

		EOF

	.. note::

		* Be sure the correct username is entered for the `User` and `PIDFile` 
		  fields.  The username in `Description` field is optional, but useful for 
		  `systemctl` service identification purpose.
		* To see additional parameters that can be supplied to `vncserver`, see 
		  the `vncserver` Man page.

#.	Each user `MUST` log into his/her account and set a VNC password with the 
	`vncpasswd` command `BEFORE` proceeding to the next step.

#.	Start the VNC service scripts and also set it to start automatically after 
	the |CL| host boots. Now, a VNC session for each user will start automatically 
	when a VNC client connection is initiated.    

	.. code-block:: console

		# systemctl daemon-reload
		# systemctl start vncserver@:X.service
		# systemctl enable vncserver@:X.service

#.	After starting the services, verify they are running.  

	.. code-block:: console

		# systemctl | grep vnc

	Below is an example of 2 services that were started successfully for users 
	`vnc-user-b` and `vnc-user-c`.

	.. code-block:: console

		# systemctl | grep vnc

		vncserver@:5.Service 	loaded active running   VNC Remote Desktop Service for VNC-user-b                           
		vncserver@:6.service 	loaded active running   VNC Remote Desktop Service for VNC-user-c                           
		system-vncserver.slice 	loaded active active    system-vncserver.slice    

Install VNC viewer and SSH client on the client system
******************************************************
On the client system side, a VNC viewer app is needed.  An SSH client is only
needed if the VNC-server-side start method is manual (Method 1 as described above).   

#.	Install a VNC viewer app on the client system.
	
	* On some example Linux distros:		
		- Clear Linux:	 

			.. code-block:: console

				# swupd bundle-add desktop-autostart
		
		- Ubuntu, Mint:

			.. code-block:: console

				# apt-get install xtightvncviewer 

		- Fedora: 

			.. code-block:: console

				# dnf install tigervnc

	* On Windows:
		- Install `RealVNC`_ for Windows 

	* On macOS:
		- Use the built-in `Screen Sharing` app

#.	Install an SSH client app on the client system.

	* On most Linux distros (Clear Linux, Ubuntu, Mint, Fedora, etc.) and macOS:
		- SSH is already built-in

	* On Windows:
		- Install `Putty`_


Initiate a VNC session on the |CL| host
***************************************
If the VNC server is configured for manual start (Method 1 described above),
the user must manually SSH in and start a VNC session by following these steps
first.  Otherwise, skip to the `Connect to VNC session on |CL| host section below.

#.	SSH into the Clear Linux host.

		* On Linux distros and macOS:

			.. code-block:: console
		
				$ ssh <username>@<clear-linux-host-ip-address>

		* On Windows:
			
			- Launch Putty
			- Under the Category section, go to Session
			- Enter the IP address of the Clear Linux host in the Host Name (or IP address) field. (See Figure 1)
			- Set the Connection type to SSH


.. _RealVNC: https://www.realvnc.com/en/connect/download/viewer/windows/
.. _Putty: https://the.earth.li/~sgtatham/putty/latest/w64/putty-64bit-0.70-installer.msi

