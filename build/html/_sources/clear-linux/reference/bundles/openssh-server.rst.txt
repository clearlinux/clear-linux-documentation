.. _bdl-openssh-server:

openssh-server
##############

This bundle provides the OpenSSH\* package needed to enable a SSH service.
Remote users require a SSH service to be able to use an encrypted login
shell. The first time OpenSSH starts, it generates the server SSH keys needed
for the service.

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
