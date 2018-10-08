.. _bdl-openssh-server:

openssh-server
##############

This bundle provides the OpenSSH\* package needed to enable a SSH service.
Remote users require a SSH service to be able to use an encrypted login
shell. The first time OpenSSH starts, it generates the server SSH keys needed
for the service.

|CL| enables the `sshd.socket` unit, which will listen on port 22 by default and
start the openssh service as required.

Change Default Port
===================
In order to change the default listen port for the OpenSSH\* service, perform
the following steps:

#. Edit the sshd.socket unit file, provide the `ListenStream` option in the
   `[Socket]` section with no value in order to remove the |CL| default port
   value, then provide the `ListenStream` option again with the new default
   port to listen. In this example, we change `ListenStream` to
   listen on port 4200 instead of the |CL| default:

   .. code-block:: console

      # systemctl edit sshd.socket

#. Verify your changes:

   .. code-block:: console

      # cat /etc/systemd/system/sshd.socket.d/override.conf
      [Socket]
      ListenStream=
      ListenStream=4200

#. Reload the systemd daemon configurations:

   .. code-block:: console

      # systemctl daemon-reload

#. Restart the sshd.socket unit:

   .. code-block:: console

      # systemctl restart sshd.socket


SFTP
====

|CL| *disables* the :abbr:`SFTP (SSH File Transfer Protocol)` subsystem by
default due to security considerations. To enable the SFTP subsystem, perform
the following configuration of the :abbr:`SSHD (SSH Daemon)` service file:

#. Create a systemd drop-in directory for the SSHD service:

   .. code-block:: console

      # mkdir -p /etc/systemd/system/sshd@.service.d

#. Create the following file:
   :file:`/etc/systemd/system/sshd@.service.d/sftp.conf`

#. Add the OPTIONS environment variable

   .. code-block:: console

      [Service]
      Environment="OPTIONS=-o Subsystem=\"sftp /usr/libexec/sftp-server\""

#. Reload systemd configuration:

   .. code-block:: console

      # systemctl daemon-reload

Congratulations! The SFTP subsystem is enabled.

Root login
==========

To enable root login via ssh, perform the following steps:

#. Create a *ssh* directory in :file:`/etc`, only if it does not exist)

   .. code-block:: console

      # mkdir /etc/ssh

#. Set the configuration variable.

   .. code-block:: console

      # echo "PermitRootLogin yes" >> /etc/ssh/sshd_config
