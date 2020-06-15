.. _php:

PHP and PHP-FPM
###############

This tutorial describes how to configure and use :abbr:`PHP (PHP: Hypertext Preprocessor)`
and :abbr:`PHP-FPM (PHP FastCGI Process Manager)` on |CL-ATTR|.

.. contents::
    :local:
    :depth: 1

Description
***********

The `PHP language`_ is an Open Source general-purpose scripting language that is popular
with web-developers who leverage its ability to create dynamically generated
web pages. `PHP-FPM`_ is a PHP FastCGI implementation that controls process
management, workers, and logging for PHP. The two applications work together,
but each one has its own configuration.

This tutorial specifically addresses PHP and PHP-FPM, however, it provides a
general guide for working with applications in the |CL| :ref:`stateless`
environment.


Background
**********

By default, PHP looks for configuration settings in the :file:`php.ini` file,
which resides in the :file:`usr/share/defaults/php/` path. Because |CL| is a
:ref:`stateless` operating system, you must create an optional configuration
file to override the default values. Every time :command:`swupd` updates the
system, it overwrites changes to the :file:`/usr/share/defaults` file
structure. To save your configuration options through updates, you must create
a PHP configuration file in a location that will not be overwritten. The
recommended location is within the :file:`/etc` file structure, which is why this
tutorial creates a :file:`/etc/php.d` directory.

The PHP-FPM configuration file is separate from the :file:`php.ini` file used
by PHP, however it has a similar default path restriction. |CL| installs the
default :file:`php-fpm.conf` file in :file:`/usr/share/defaults/php`. This
file with its default values is overwritten during each software update.
However, PHP-FPM requires that the configuration file exist in that location,
and, by design, does not read configuration options from a different path.
This tutorial describes a solution to changing PHP-FPM configuration options
in |CL|, by manually  overriding the php-fpm.service unit in systemd to pass
an explicit location to a custom :file:`php-fpm.conf` file.


Prerequisites
*************

* :ref:`Install <bare-metal-install-desktop>` |CL| on your host system.
* Use :command:`swupd` to install the :file:`php-basic` bundle:

  .. code-block:: bash

     sudo swupd bundle-add php-basic

.. note::

   PHP does not require a web server for operation. If you need a web
   server, refer to :ref:`lamp-server-install` for instructions on setting
   up a :abbr:`LAMP (Linux, Apache\*, MySQL\*, PHP)` server, or use
   :command:`swupd` to install :file:`nginx` or similar.


Configure PHP
*************

.. important::

   This section does **not** describe configuration for the PHP-FPM service, which is
   described later in this guide.

This section creates a :file:`/etc/php.d` directory for all PHP configuration
files to work around the default path restriction.

#.  Create a :file:`php.ini` file:

    .. code-block:: bash

       sudo mkdir -p /etc/php.d
       sudo touch /etc/php.d/my-php.ini

    This file can be edited with any of your specific configuration
    requirements, and will not be overwritten when :command:`swupd` performs
    an update. The `PHP configuration file`_ documentation contains details
    about what you can set in this file.

#.  Verify the location of the PHP configuration files:

    .. code-block:: bash

       php --ini

    You should see output like this:

    .. code-block:: console

       Configuration File (php.ini) Path: /usr/share/defaults/php/
       Loaded Configuration File:         /usr/share/defaults/php/php.ini
       Scan for additional .ini files in: /etc/php.d
       Additional .ini files parsed:


    This output indicates that PHP will read the :file:`php.ini` file from
    :file:`/usr/share/defaults/php` and will then load any further
    configuration from :file:`.ini` files in :file:`/etc/php.d/`. The
    :file:`my-php.ini` file in :file:`/etc/php.d` contains your configuration
    details, and allows the defaults to be read from
    :file:`/usr/share/defaults/php/`. Note that the :file:`my-php.ini` file
    has not been parsed, because the file has no content at this
    point and is disregarded.

Install PHP extensions
**********************

PHP extensions are compiled libraries designed to enable specific functions in
your PHP code. |CL| provides PHP extensions in the :file:`php-extras` bundle.

#.  Install the bundle with swupd:

    .. code-block:: bash

       sudo swupd bundle-add php-extras

#.  Find the list of extensions included in the `php-extras`_ bundle on the
    |CL| `Store`_.


Enable PHP extensions
*********************

To enable an installed extension, you must add it to the :file:`php.ini` file
for the composer.

#.  Create the :file:`my-php.ini` file using the directive to load the
    php-imagick extension:

    .. code-block:: bash

       sudo echo "extension=imagick.so" >> /etc/php.d/my-php.ini

#.  Restart the php-fpm service for PHP to pick up the modification to the
    :file:`/etc/php.d/my-php.ini` file:

    .. code-block:: bash

       sudo systemctl restart php-fpm

#.  Verify that the imagick extension has been loaded by searching through the
    runtime list of loaded PHP Modules:

    .. code-block:: bash

       php -m | grep imagick


.. note::

   To enable an extension, you must install it, add it to the
   :file:`my-php.ini` file, and restart the :file:`php-fpm` service. However,
   some extensions may have configuration options, which will be documented by
   the extension maintainer. Add the options you need to the
   :file:`/etc/php.d/my-php.ini` file as described in the extension's
   documentation. Be sure to restart :file:`php-fpm` after changing the file.

Configure PHP-FPM
*****************

The PHP-FPM configuration file is separate from the :file:`php.ini` file used
by PHP, however, it has a similar default path restriction. Follow the steps
below to configure PHP-FPM.


#.  Copy the :file:`/usr/share/defaults/php/php-fpm.conf` file to the
    :file:`/etc/php.d` file:

    .. code-block:: bash

       sudo cp /usr/share/defaults/php/php-fpm.conf /etc/php.d/php-fpm.conf

#.  Make changes to the :file:`php-fpm.conf` file as needed. The
    `FPM documentation`_ has details on the configuration options available
    to PHP-FPM.

#.  Edit the systemd service unit file:

    .. code-block:: bash

       sudo systemctl edit --full php-fpm.service

    This opens the :file:`php-fpm.service` file for systemd in your editor.

#.  Change the :command:`ExecStart` configuration to add the
    :command:`--fpm-config` option to point to the custom location:

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

#.  Restart the service:

    .. code-block:: bash

       sudo systemctl restart php-fpm.service

#.  Verify that the new path has been picked up:

    .. code-block:: bash

       sudo systemctl status php-fpm.service

    You should see the new path in the output:

    .. code-block:: console

       ● php-fpm.service - The PHP FastCGI Process Manager
       Loaded: loaded (/etc/systemd/system/php-fpm.service; enabled; vendor preset: disabled)
       Active: active (running) since Thu 2019-10-17 13:19:34 PDT; 8min ago
       Main PID: 14452 (php-fpm)
       Status: "Processes active: 0, idle: 0, Requests: 0, slow: 0, Traffic: 0req/sec"
        Tasks: 1
       Memory: 11.1M
       CGroup: /system.slice/php-fpm.service
               └─14452 php-fpm: master process (/etc/php.d/php-fpm.conf)


.. _PHP language: https://www.php.net/

.. _PHP-FPM: https://php-fpm.org/

.. _php-extras: https://clearlinux.org/software/bundle/php-extras

.. _Store: https://clearlinux.org/software/

.. _PHP configuration file: https://www.php.net/manual/en/configuration.file.php

.. _FPM documentation: https://www.php.net/manual/en/install.fpm.configuration.php
