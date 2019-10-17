.. _php:

PHP and PHP-FPM
***************

This tutorial describes how to configure and use PHP and PHP-FPM  on |CL-ATTR|. Although we specifically address PHP this tutorial can serve as a general guide for working with applications in the |CL| :ref:`stateless` environment.

.. contents::
    :local:
    :depth: 1

Overview
********

`PHP (PHP:Hypertext Preprocessor)`_ is an Open Source general-purpose scripting language that is popular with web-developers who leverage its ability to create dynamically generated web pages.  `PHP-FPM (FastCGI Process Manager)`_ is a PHP FastCGI implementation that controls process management, workers, and logging for PHP. The two applications work in conjunction but each has its own configuration.



Prerequisites
*************

* :ref:`Install <bare-metal-install-desktop>` |CL| on your host system
* Follow :ref:`web-server-install` to install Apache\* and PHP

.. note::

   PHP does not require Apache's httpd service for operation. We use this environment as an example for this tutorial.  If you are not using the httpd service, please adjust accordingly when you encounter instructions that require httpd.


Configure PHP
*************

.. important::

   This section does not cover configuring the PHP-FPM service. There is a difference between the two configurations. This section is only looking at the PHP configuration directives, not those of PHP-FPM.


By default PHP looks for configuration settings in the :file:`php.ini` file, which resides in the `usr/share/defaults/php/` path. Because |CL| is designed to be a :ref:`stateless` operating system, you must create an optional configuration file to override the default values. Every time :command:`swupd` updates the system it will overwrite changes to the `/usr/share/defaults` file structure. To save you configuration options through updates, you must create a PHP configuration file in a location that will not be overwritten. The recommended location is within the :file:`/etc` file structure.  For PHP we will create a :file:`/etc/php.d` directory for all PHP config files.

Create a :file:`php.ini`.

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


This output indicates that PHP will read the php.ini file from `/usr/share/defaults/php` and will then load any further configuration from :file:`.ini` files in `/etc/php.d/`. We use the :file:`php.ini` file in `/etc/php.d` for our specific needs, and allow the defaults to be read from `/usr/share/defaults/php/`.


Install PHP extensions
**********************

PHP extensions are compiled libraries designed to enable specific functions in your PHP code. |CL| provides PHP extensions in the :file:`php-extras` bundle.  Install the bundle with swupd:

.. code-block:: bash

   sudo swupd bundle-add php-extras

You can see the list of extensions included in the `php-extras`_ bundle on the |CL| `Store`_.


Enable PHP extensions
*********************

To enable an installed extension we need to add it to the :file:`php.ini` for the composer to use it.

Create the :file:`php.ini` file, with the directive to load the php-imagick extension

.. code-block:: bash

   sudo echo "extension=imagick.so" >> /etc/php.d/php.ini


No further detail is required to load the extension, but you must restart the httpd service for PHP to pick up the modification to the `/etc/php.d/php.ini` file.

.. code-block:: bash

   sudo systemctl restart httpd

You can verify that the imagick extension has been loaded by searching through the runtime list of loaded PHP Modules.

.. code-block:: bash

   php -m | grep imagick


.. note::

   Enabling an extension only requires that it be installed, added to the php.ini file and that the httpd service is restarted. However extensions may have their own configuration options.  These will be documented by the extension maintainer.  The options you need can be added to the :file:`/etc/php.d/php.ini` file as described by the documentation for the extension.  Be sure to restart httpd after making changes to the file.

Configure PHP-FPM
*****************

The PHP-FPM configuration file is separate from the :file:`php.ini` file used by PHP. |CL| installs the default :file:`php-fpm.conf` file in /usr/share/defaults/php and this file will be overwritten with its default values during each software update. However, PHP-FPM requires that the configuration file exist in that location, and by design will not read configuration options from a different path.

One solution to changing PHP-FPM configuration options in |CL| is to manually override the php-fpm.service unit in systemd to pass an explicit location to a custom :file:`php-fpm.conf` file.

#. Copy the :file:`/usr/share/defaults/php/php-fpm.conf` file to the :file:`/etc/php.d`

   .. code-block:: bash

      sudo cp /usr/share/defaults/php/php-fpm.conf /etc/php.d/php-fpm.conf

#. Make changes to the :file:`php-fpm.conf` file as needed. The `FPM documentation`_ has detail on the configuration options available to PHP-FPM.


#. Edit the systemd service unit file

   .. code-block:: bash

      sudo systemctl edit --full php-fpm.service

   This will open the php-fpm.service file for systemd in your editor.  Change the  :command:`ExecStart` configuration to add the :command:`--fpm-config` option to point to the custom location.

   .. code-block:: bash

      sudo systemctl edit --full php-fpm.service

   .. code-block:: console

      [Unit]
      Description=The PHP FastCGI Process Manager
      After=syslog.target network.target

      [Service]
      Type=notify
      PIDFile=/run/php-fpm.pid
      ExecStart=/usr/sbin/php-fpm --nodaemonize --fpm-config /etc/php.d/php-fpm.conf
      ExecReload=/bin/kill -USR2 $MAINPID
      PrivateTmp=true

      [Install]
      WantedBy=multi-user.target

#. Restart the service

   .. code-block:: bash

      sudo systemctl restart php-fpm.service

#. Verify that the new path has been picked up

   .. code-block:: bash

      sudo systemctl show php-fpm.service |grep ExecStart

   You should see the new path in the output

   .. code-block:: console

      ExecStart={ path=/usr/sbin/php-fpm ; argv[]=/usr/sbin/php-fpm --nodaemonize --fpm-config /etc/php.d/php-fpm.conf ; ignore_errors=no ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }






.. _PHP (PHP:Hypertext Preprocessor): https://www.php.net/

.. _PHP-FPM (FastCGI Process Manager): https://php-fpm.org/

.. _php-extras: https://clearlinux.org/software/bundle/php-extras

.. _Store: https://clearlinux.org/software/

.. _PHP configuration file: https://www.php.net/manual/en/configuration.file.php

.. _FPM documentation: https://www.php.net/manual/en/install.fpm.configuration.php
