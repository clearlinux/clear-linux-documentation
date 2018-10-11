.. _bdl-openssh-server:

openssh-server
##############

The **openssh-server** bundle provides the OpenSSH\* package needed to enable 
a SSH service in |CL-ATTR|. Remote users require a SSH service to be able to 
use an encrypted login shell. 

|CL| enables the `sshd.socket` unit, which will listen on port 22 by default 
and start the OpenSSH service as required. The first time OpenSSH starts, it 
generates the server SSH keys needed for the service.

Change default port
*******************
Perform the following steps to change the default listen port for the 
OpenSSH service:

#. Open the sshd.socket file:

   .. code-block:: bash

      sudo systemctl edit sshd.socket

#. Add the `[Socket]` section and `ListenStream` option to the sshd.socket 
   file as shown below. The first `ListenStream` entry removes the |CL| 
   default listen port value. The second `ListenStream` entry sets the new 
   default listen port value. In this example, we set the new default port 
   to 4200:

   .. code-block:: console

      [Socket]
      ListenStream=
      ListenStream=4200


   Make sure to include a new line after the last line of text in the sshd.socket file.

#. Verify your changes:

   .. code-block:: bash

      cat /etc/systemd/system/sshd.socket.d/override.conf
      
   You should see the following output: 
      
   .. code-block:: console

      [Socket]
      ListenStream=
      ListenStream=4200

#. Reload the systemd daemon configurations:

   .. code-block:: bash

      sudo systemctl daemon-reload

#. Restart the sshd.socket unit:

   .. code-block:: bash

      sudo systemctl restart sshd.socket

#. Confirm the the sshd.socket unit is listening on your new port: 

   .. code-block:: bash
   
      systemctl status sshd.socket

Enable SFTP
***********

|CL| *disables* the :abbr:`SFTP (SSH File Transfer Protocol)` subsystem by
default due to security considerations. To enable the SFTP subsystem, perform
the following configuration of the :abbr:`SSHD (SSH Daemon)` service file:

#. Create a systemd drop-in directory for the SSHD service:

   .. code-block:: bash

      mkdir -p /etc/systemd/system/sshd@.service.d

#. Create the following file:
   :file:`/etc/systemd/system/sshd@.service.d/sftp.conf`

#. Add the OPTIONS environment variable to the sftp.conf file.

   .. code-block:: console

      [Service]
      Environment="OPTIONS=-o Subsystem=\"sftp /usr/libexec/sftp-server\""

#. Reload systemd configuration:

   .. code-block:: bash

      systemctl daemon-reload

Congratulations! The SFTP subsystem is enabled.

Enable root login
*****************

To enable root login via SSH, perform the following steps:

#. Create a *ssh* directory in :file:`/etc`, if it does not already exist.

   .. code-block:: bash

      mkdir /etc/ssh

#. Set the configuration variable.

   .. code-block:: bash

      echo "PermitRootLogin yes" >> /etc/ssh/sshd_config
