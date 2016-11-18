.. _bdl-openssh-server:

openssh-server
##############

This bundle provides an ssh server.

SFTP
====

Clear Linux *disables* sftp subsystem by default for security reasons.
To enable sftp subsystem you will need to add this configuration in the sshd
service file.

First, create a systemd drop-in directory for the sshd service::

  # mkdir /etc/systemd/system/sshd@.service.d

Now create a file called :file:`/etc/systemd/system/sshd@.service.d/sftp.conf`
that adds the OPTIONS environment variable::

  [Service]
  Environment="OPTIONS=-o Subsystem=\"sftp /usr/libexec/sftp-server\""

Now, sftp subsystem is enabled.

Root login
==========

To enable root login via ssh, you should do the following:

#. Create a *ssh* directory in /etc (if not exist)::

   # mkdir /etc/ssh

#. Set config variable::

   # echo "PermitRootLogin yes" >> /etc/ssh/sshd_config


