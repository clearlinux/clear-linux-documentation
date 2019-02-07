.. _enable-user-space:

Create and enable a new user space
##################################

This section provides steps to complete the following basic setup tasks for
a newly installed |CL-ATTR| system:

.. contents::
   :local:
   :depth: 1

Prerequisites
*************

Log in as the root user to complete the tasks in this section. Enter:

.. code-block:: bash

   sudo -i

Create a new user
******************

To create a new user and set a password for that user, enter the following
commands as a `root` user:

.. code-block:: bash

   useradd <userid>
   passwd <userid>

Replace the <userid> with the name of the user account you want to create
including the password for that user. The :command:`passwd` command prompts
you to enter a new password. Retype the new password for the new user
account just created.

Install and update the OS software to its current version
*********************************************************

The |CL| software utility :ref:`swupd <swupd-guide>` allows you to perform system updates while reaping the benefits of upstream development.

To update your newly installed OS, run.

.. code-block:: bash

   sudo swupd update

Software applications are installed as bundles using the command
:command:`swupd bundle-add`. Experienced Linux* users can compare
using `swupd` to running :command:`apt-get` or :command:`yum install` for
package management. Yet |CL| manages packages at the level of bundles, which
are integrated stacks of packages.

The `sysadmin-basic` bundle installs the vast majority of applications useful to a system administrator. To install it, enter:

.. code-block:: bash

   swupd bundle-add sysadmin-basic

Select this link to view a full list of bundles and packages installed with the `sysadmin-basic`_ bundle. Additionally, we list `all bundles`_ for
|CL|, active or deprecated. Click any bundle on the list to view the
manifest of the bundle.

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
   `sysadmin-basic`_ contains the majority of applications that a system
   administrator would want, but it does not include a graphical user
   interface. The `desktop` bundle includes the GNOME\* Display Manager and
   additional supporting applications.

Next steps
***********

Check out our :ref:`tutorials`.

.. _`sysadmin-basic`:
   https://github.com/clearlinux/clr-bundles/blob/master/bundles/sysadmin-basic

.. _`all bundles`:
   https://github.com/clearlinux/clr-bundles/tree/master/bundles

.. _`wheel group`:
   https://en.wikipedia.org/wiki/Wheel_(Unix_term)
