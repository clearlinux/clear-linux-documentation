.. _enable-user-space:

Create and enable a new user space
##################################

This section provides steps to complete the following basic setup tasks for
a newly installed |CL| system:

* Create a new user
* Update the OS to its most current version using `swupd`.
* Install the most common applications for system administrators and
  developers using bundles.
* Setup a new user.
* Add the new user to the `wheel` group.
* Install a GUI using those `sudo` privileges.

.. note::
   You must be logged in as the root user to complete the tasks in this
   section.

Create a new user
=================

To create a new user and set a password for that user, enter the following
commands as a root user:

.. code-block:: console

   useradd <userid>
   passwd <userid>

Replace <userid> with the name of the user account you want to create and
with the password for said user.  The :command:`passwd` command prompts you
to enter a new password and then retype the new password for the new user
account you just created.

Install and update software
===========================

|CL| has a unique application and architecture to add and update applications
and to perform system updates called software update utility or
:command:`swupd`. Software applications are installed as bundles using the
sub-command :command:`bundle-add`.

The `os-clr-on-clr` bundle installs the vast majority of
applications useful to a system administrator or a developer. The bundle
contains other bundles such as `sysadmin-basic`, `editors`, `c-basic`,
`dev-utils-dev`, and other useful packages.

Install the `os-clr-on-clr` bundle using the software update
utility:

.. code-block:: console

   swupd bundle-add os-clr-on-clr

.. note::

   The image we installed may not be the latest version of |CL| available on
   the server. However, whenever the command
   :command:`swupd bundle-add <bundle>` runs, the OS is updated to the latest
   available version. Our website provides more `information about swupd`_.

We provide the full list of bundles and packages installed with the
`os-clr-on-clr`_ bundle. Additionally, we have listed
`all Clear Linux bundles`_, active or deprecated. Click any bundle on the
list to view the manifest of the bundle.

Finish setting up your new user
===============================

Before logging off as root and logging into your new user account, we must
enable the :command:`sudo` command for your new `<userid>`.

To be able to execute all applications with root privileges, we must add the
`<userid>` to the `wheel group`_.

#. Add `<userid>` to the `wheel` group:

   .. code-block:: console

      usermod -G wheel -a <userid>

#. Now, we can log out of root and into our new `<userid>`.

   To log off as root, enter :command:`exit`.

   The command will bring you back to the `login:` prompt.

#. Enter the new `<userid>` and the password you created earlier.

   You will now be in the home directory of `<userid>`. The bundle
   `os-clr-on-clr`_ contains the majority of applications that a developer or
   system administrator would want but it does not include a graphical user
   interface. The `desktop` bundle includes the Gnome Desktop Manager and
   additional supporting applications.

Install a GUI to test sudo
--------------------------
.. note::
If you are following this sequence after just setting up the pre-configured VMware virtual machine from
the repo, you must :ref:increase virtual disk size<increase-virtual-disk-size> or the following step
will fail.

To test the :command:`sudo` command and ensure it is set up correctly,
install the Gnome Desktop Manager (gdm) and start it.

#. To install Gnome using :command:`swupd`, enter the following command:

   .. code-block:: console

      sudo swupd bundle-add desktop

#. To start the Gnome Desktop Manager, enter the following command:

   .. code-block:: console

      systemctl start gdm

#. The system prompts you to authenticate the user. Enter the password for
   `<userid>` and the Gnome Desktop should start as shown in figure 13:

   .. figure:: figures/gnomedt.png
      :scale: 50 %
      :alt: Gnome Desktop

      Figure 13: :guilabel:`Gnome Desktop`

#. To start the Gnome Desktop each time you start your system, enter
   the following command:

   .. code-block:: console

      systemctl enable gdm

Next steps
==========

With your system now running |CL| many paths are open for you.

Visit our :ref:`tutorials <tutorials>` page for examples on using your |CL|
system.

.. _`information about swupd`:
   https://clearlinux.org/features/software-update

.. _`os-clr-on-clr`:
   https://github.com/clearlinux/clr-bundles/blob/master/bundles/os-clr-on-clr

.. _`all Clear Linux bundles`:
   https://github.com/clearlinux/clr-bundles/tree/master/bundles

.. _`wheel group`:
   https://en.wikipedia.org/wiki/Wheel_(Unix_term)
