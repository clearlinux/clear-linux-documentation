.. _openssh-server:

Enable and configure SSH service
################################

This guide describes how to set up the SSH service.

.. contents::
   :local:
   :depth: 1

Overview
********

The :command:`openssh-server` bundle provides the OpenSSH package that
enables an SSH service in |CL-ATTR|. Remote users require an SSH service to be
able to use an encrypted login shell. The SSH daemon has all of its configuration built in and no template configuration file is present on the file system.

|CL| enables the `sshd.socket` unit, which listens on port 22 by default
and starts the OpenSSH service as required. The first time OpenSSH starts, it
generates the server SSH keys needed for the service.

Prerequisites
*************

Ensure the :command:`openssh-server` bundle is installed.

To list all bundles on your host, enter:

.. code-block:: bash

   sudo swupd bundle-list

To add the :command:`openssh-server` bundle, enter:

.. code-block:: bash

   sudo swupd bundle-add openssh-server

Change default port
*******************

Perform the following steps to change the default listening port for the
OpenSSH service.

#. Open the :file:`sshd.socket` file:

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


   Make sure to include a new line after the last line of text in the :file:`sshd.socket` file.

#. Verify your changes:

   .. code-block:: bash

      cat /etc/systemd/system/sshd.socket.d/override.conf

   The following output is displayed:

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

#. Confirm the sshd.socket unit is listening on your new port:

   .. code-block:: bash

      sudo systemctl status sshd.socket

   .. note::

      Output should show :guilabel:`Active:` as `active(listening)`.

Enable SFTP
***********

|CL| *disables* the :abbr:`SFTP (SSH File Transfer Protocol)` subsystem by
default due to security considerations. To enable the SFTP subsystem, you can
configure the :file:`/etc/ssh/sshd_config` file.

#. Create the following file, if it does not already exist:
   :file:`/etc/ssh/sshd_config`

#. Add the the SFTP subsystem in :file:`/etc/ssh/sshd_config`:

   .. code-block:: console

      subsystem sftp /usr/libexec/sftp-server


Congratulations! The SFTP subsystem is enabled. You do not need to restart the sshd service.

Enable root login
*****************

To enable root login via SSH, perform the following steps:


#. Create the following file, if it does not already exist:
   :file:`/etc/ssh/sshd_config`

#. Set the configuration variable in :file:`/etc/ssh/sshd_config`:

   .. code-block:: console

      PermitRootLogin yes

You have now enabled root login on your system.  You do not need to restart the sshd service. 

Enable X11-forwarding
*********************

X11 forwarding allows you to securely run graphical applications (that is, X
clients) over the SSH connection. This enables remote GUI apps without the need
for full VNC or remote desktop setup. To enable X11-forwarding via SSH,
perform the following steps:

#. Create the following file, if it does not already exist:
   :file:`/etc/ssh/sshd_config`

#. Set the following configuration variables.

   .. code-block:: bash

      AllowTcpForwarding yes
      X11UseLocalhost yes
      X11DisplayOffset 10
      X11Forwarding yes

You have now enabled X11-forwarding!  You do not need to restart the sshd service.
