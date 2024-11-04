.. _stateless:

Stateless
#########

In most operating systems, user data, system data, and configuration files
can become intermingled.

.. figure:: figures/stateless-1.png
   :scale: 45%
   :align: center
   :alt: Stateless: User and system files mixed

   Figure 1: Without stateless, user and system files become mixed on the filesystem over time.

|CL-ATTR| has a stateless design philosophy with the goal to provide an
:abbr:`OS (operating system)` that functions without excessive user
configuration or customization. Stateless in this context does *not* mean
ephemeral or non-persistent.

.. contents:: :local:
   :depth: 1

File-level separation
*********************

To accomplish a stateless design the Linux Filesystem Hierarchy is separated
between user-owned areas and |CL|-owned areas.

.. figure:: figures/stateless-2.png
   :scale: 45%
   :align: center
   :alt: Stateless: User and system files separation

   Figure 2: With stateless, user and system files are separated on the filesystem.

System areas
============
File under the :file:`/usr` directory are managed by |CL| as system files.
Files written under the :file:`/usr` directory by users can get removed
through system updates with :ref:`swupd <swupd-guide>`. This operating
assumption allows |CL| to verify and maintain integrity of system files.

User areas
==========
Files under the :file:`/etc/`, :file:`/home`, and :file:`/var` directories are
owned and managed by the user. A freshly installed |CL| system will only have
a minimal set of files in the :file:`/etc/` directory and software installed
by |CL| does not write to :file:`/etc`. This operating assumption allows |CL|
users to clearly identify the configuration that makes their system unique.


Software configuration
**********************

With stateless separation, default software configurations are read in order
from predefined source code, |CL| provided defaults, and user-provided
configuration.

Default configurations
======================

Software in |CL| provides default configuration values so that it is
immediately functional, whenever it is appropriate to do so.

|CL| distributed software packages may be directly modified to include default
configuration values or default configuration files may be provided by |CL|
under :file:`/usr/share/defaults`. These files can be referenced as templates
for customization.

For example, the default configuration that Apache uses when installed can be
found at :file:`/usr/share/defaults/httpd/httpd.conf` directory.


Overriding configurations
=========================

If a configuration needs to be changed, the appropriate file should be
modified by the user under :file:`/etc/`. If the configuration file does not
already exist, it can be created in the appropriate location.

User defined configuration files should contain the minimal set of desired
changes and rely on default configuration for the rest.

For example, a customized Apache configuration can be used instead by:

#. Create the destination directory for the configuration:

   .. code-block:: bash

      sudo mkdir /etc/httpd

#. Copy the default configuration as a reference template:

   .. code-block:: bash

      sudo cp /usr/share/defaults/httpd/httpd.conf /etc/httpd/

#. Make any desired modifications to the configurations:

   .. code-block:: bash

      sudoedit /etc/httpd/httpd.conf

#. Reload the service or reboot the system to pickup any changes:

   .. code-block:: bash

      systemctl daemon-reload httpd && systemctl restart httpd

This pattern can be used to modify the configurations of other programs too.
The `stateless man page`_ has application-specific examples.

System reset
************

Once advantage of the stateless design is that the system defaults can be
easily restored by simply deleting everything under :file:`/etc/` and
:file:`/var`.

Running the commands below effectively performs a system reset as if it was
just installed:

.. code-block:: bash

   sudo rm -rf /etc
   sudo rm -rf /var

In other Linux distributions, this can be a catastrophic action that renders
a system unable to boot.

Additional information
**********************

* `stateless man page`_

.. _`stateless man page`: https://github.com/clearlinux/clr-man-pages/blob/master/stateless.7.rst


