.. _enable-user-space:

Create and enable a new user space
##################################

This section provides steps to complete the following basic setup tasks for
a newly installed |CLOSIA| system:

* Create a new user.
* Update the OS to its most current version using `swupd`.
* Install the most common applications for system administrators and
  developers using bundles.
* Set up a new user and add the new user to the `wheel` group.
* Install a GUI to test `sudo` privileges.

.. note::
   Log in as the root user to complete the tasks in this
   section.

Create a new user
******************

To create a new user and set a password for that user, enter the following
commands as a root user:

.. code-block:: bash

   useradd <userid>
   passwd <userid>

Replace the <userid> with the name of the user account you want to create
including the password for that user. The :command:`passwd` command prompts
you to enter a new password. Retype the new password for the new user
account just created.

Install and update the OS software to its current version
*********************************************************

|CL| has a unique application and architecture to add and update applications
and to perform system updates called software update utility or
:command:`swupd`. Software applications are installed as bundles using the
sub-command :command:`bundle-add`.

The `os-clr-on-clr` bundle installs the vast majority of
applications useful to a system administrator or a developer. The bundle
contains other bundles such as `sysadmin-basic`, `editors`, `c-basic`,
`dev-utils-dev`, and other useful packages.

Install the `os-clr-on-clr` bundle:

.. code-block:: bash

   swupd bundle-add os-clr-on-clr

We provide the full list of bundles and packages installed with the
`os-clr-on-clr`_ bundle. Additionally, we have listed
`all Clear Linux bundles`_, active or deprecated. Click any bundle on the
list to view the manifest of the bundle.

Set up a new user and add the new user to the `wheel` group
***********************************************************

Before logging off as root and logging into your new user account,
enable the :command:`sudo` command for your new `<userid>`.

To be able to execute all applications with root privileges, add the
`<userid>` to the `wheel group`_.

#. Add `<userid>` to the `wheel` group:

   .. code-block:: bash

      usermod -G wheel -a <userid>

#. Log out of root and into the new `<userid>`.

   To log off as root, enter :command:`exit`.

   The command will bring you back to the `login:` prompt.

#. Enter the new `<userid>` and the password created earlier.

   You will now be in the home directory of `<userid>`. The bundle
   `os-clr-on-clr`_ contains the majority of applications that a developer or
   system administrator would want, but it does not include a graphical user
   interface. The `desktop` bundle includes the GNOME\* Display Manager and
   additional supporting applications.

Install a GUI to test `sudo` privileges
========================================
.. note::

   If you are following this sequence after just setting up the
   pre-configured VMware\* virtual machine from the repo, you must 
   :ref:`increase virtual disk size<increase-virtual-disk-size>` or the
   following step will fail.

To test the :command:`sudo` command and ensure it is set up correctly,
install the GNOME Display Manager (gdm) and start it.

#. To install the the GNOME Display Manager using :command:`swupd`, enter
   the following command:

   .. code-block:: bash

      sudo swupd bundle-add desktop

#. To start the GNOME Display Manager, enter the following command:

   .. code-block:: bash

      systemctl start gdm

#. The system prompts you to authenticate the user. Enter the password for
   `<userid>`, and the GNOME Display Manager starts as shown in Figure
   1:

   .. figure:: figures/gnomedt.png
      :scale: 50 %
      :alt: Gnome Desktop

      Figure 1: :guilabel:`Gnome Desktop`

#. To start the GNOME Display Manager each time you start your system, enter
   the following command:

   .. code-block:: bash

      systemctl enable gdm

Next steps
***********

With your system now running |CL|, many opportunities exist.

Visit the :ref:`tutorials <tutorials>` page for examples on using your |CL|
system.

.. _`os-clr-on-clr`:
   https://github.com/clearlinux/clr-bundles/blob/master/bundles/os-clr-on-clr

.. _`all Clear Linux bundles`:
   https://github.com/clearlinux/clr-bundles/tree/master/bundles

.. _`wheel group`:
   https://en.wikipedia.org/wiki/Wheel_(Unix_term)
