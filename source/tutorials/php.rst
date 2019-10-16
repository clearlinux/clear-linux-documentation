.. _php:

Installing and Configuring PHP
******************************

This tutorial describes how to configure and use PHP and PHP extensions on |CL-ATTR|. Although we specifically address PHP this tutorial can serve as a general guide for working with applications in the |CL| :ref:`stateless` environment.

We will focus on enabling PHP and PHP extensions in |CL|.  For a complete :abbr:`LAMP (Linux, Apache, MySQL, PHP)` setup in |CL| refer to the :ref:`web-server-install` section of the :ref:`wordpress` tutorial. For this tutorial you do not need to install MariaDB or WordPress.

.. contents::
    :local:
    :depth: 1


Prerequisites
*************

* :ref:`Install <bare-metal-install-desktop>` |CL| on your host system
* Follow :ref:`web-server-install` to install Apache\* and PHP


Configuring PHP
***************

.. important::

   This tutorial does not cover configuring the php-fpm service. There is a difference between php and php-fpm here. php-fpm sets configuration for the process management and pools of worker bees, and can optionally set some of the values defined in the :file:`php.ini` file. This tutorial is only looking at the PHP configuration directives, not those of php-fpm.


By default PHP looks for configuration settings in the :file:`php.ini` file, which resides in the `usr/share/defaults/php/` path. Because |CL| is designed to be a :ref:`stateless` operating system, you must create an optional configuration file to override the default values. Every time :command:`swupd` updates the system it will overwrite changes to the `/usr/share/defaults` file structure.


Beginning with |CL| version 31020, PHP has been modified to check for :file:`.ini` files in the /etc/php.d file structure.

You can verify the version of |CL| with :command:`swupd info`

.. code-block:: bash

    sudo swupd info

You will see output similar to:

.. code-block:: console

   Distribution:      Clear Linux OS
   Installed version: 31310
   Version URL:       https://cdn.download.clearlinux.org/update
   Content URL:       https://cdn.download.clearlinux.org/update


You can create a :file:`php.ini` as follows:

.. code-block:: bash

   sudo mkdir -p /etc/php.d
   sudo touch /etc/php.d/php.ini

This file can be edited with any of your specific configuration requirements, and will not be overwritten when swupd performs an update. The `PHP configuration file`_ documentation has complete detail about what you can set in this file.

You can verify the location of the PHP configuration files with the :command:`php --ini` command:

.. code-block:: bash

   php --ini

You should see output like this

.. code-block:: console

   Configuration File (php.ini) Path: /usr/share/defaults/php/
   Loaded Configuration File:         /usr/share/defaults/php/php.ini
   Scan for additional .ini files in: /etc/php.d
   Additional .ini files parsed:      (none)


This output indicates that PHP will read the php.ini file from `/usr/share/defaults/php` and will then load any further configuration from :file:`.ini` files in `/etc/php.d/`. We will create a :file:`php.ini` file in `/etc/php.d` for our use, and allow the defaults to be read from `/usr/share/defaults/php/`.


Install PHP extensions
**********************

PHP extensions are compiled libraries designed to enable specific functions in your PHP code. |CL| provides PHP extensions in the :file:`php-extras` bundle.  Install the bundle with swupd:

.. code-block:: bash

   sudo swupd bundle-add php-extras

You can see the list of extensions included in the `php-extras`_ bundle on the |CL| `Store`_.


Enable PHP extensions
*********************

To enable an installed extension we need to add it to the :file:`php.ini` for the composer to use it.

#. Create the :file:`php.ini` file, with the directive to load the php-imagick extension

   .. code-block:: bash

      sudo echo "extension=imagick.so" >> /etc/php.d/php.ini


No further detail is required to load the extension, but you must restart the httpd service for PHP to pick up the modification to the `/etc/php.d/php.ini` file.

   .. code-block:: bash

      sudo systemctl restart httpd

You can verify that the imagick extension has been loaded by searching through the runtime list of loaded PHP Modules.

   .. code-block:: bash

      php -m | grep imagick


.. note::

   Enabling an extension only requires that it be installed, added to the php.ini file and that the httpd service is restarted. However extensions may have configuration options.  These will be documented by the extension maintainer.  The options you need can be added to the :file:`/etc/php.d/php.ini` file as described by the documentation for the extension.  Be sure to restart httpd after making changes to the file.





.. _php-extras: https://clearlinux.org/software/bundle/php-extras

.. _Store: https://clearlinux.org/software/

.. _PHP configuration file: https://www.php.net/manual/en/configuration.file.php
