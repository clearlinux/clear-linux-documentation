.. _tutorial-proxy:

Setting up proxy
################

This tutorial shows you how to configure your system for use behind a
corporate proxy. 

|CL| :ref:`tooling` applications already benefit from the :ref:`autoproxy`
feature. 

.. contents:: 
    :local:
    :depth: 1

Prerequisites
*************

This tutorial assumes you have installed |CL| on your host system.
For detailed instructions on installing |CL| on a bare metal system, visit
the :ref:`bare metal installation guide <bare-metal-install-desktop>`.

.. Throughout this document we use the following variables, which you should
   replace with your own proxy information in the following format:
   #.. code-block:: bash
       $http_proxy = your.proxy.url:port
       $https_proxy = your.proxy.url:port
       $no_proxy = ".yourdomain.com, localhost"
       $ssh_proxy = your.proxy.url:port

Shells and programs in a desktop session
****************************************

Terminal
========

Add the following to your ~/.bashrc:

.. code-block:: bash

    export http_proxy=http://your.http-proxy.url:port
    export https_proxy=http://your.https-proxy.url:port
    export no_proxy=".your-company-domain.com,localhost"

Gnome desktop
=============

wget
****

Run this command to enable downloading from websites from the terminal:

.. code-block:: bash

    echo >> ~/.wgetrc <<EOF
    http_proxy = your.http-proxy.url:port
    https_proxy = your.https-proxy.url:port
    ftp_proxy = your.http-proxy.url:port
    no_proxy = your-company-domain.com, localhost
    EOF

System service (Docker)
***********************

For Docker (and other services that use systemd), you can follow these steps to configure and check proxy settings:

.. note::

    Be sure to use :command:`sudo`, as you will need elevated permissions.

#. Create :file:`/etc/systemd/system/docker.service.d` directory to host
   configuration information for the Docker service.

#. Create :file:`/etc/systemd/system/docker.service.d/http-proxy.conf` and add:

    .. code-block:: bash

        [Service]
        Environment="HTTP_PROXY=http://your.http-proxy.url:port/"
        Environment="HTTPS_PROXY=http://your.https-proxy.url:port/"

#. Load the changes and restart the service:

    .. code-block:: bash

        sudo systemctl daemon-reload
        sudo systemctl restart docker

#. Verify that changes have loaded:

    .. code-block:: bash

        systemctl show --property=Environment docker

    .. code-block:: console

        Environment=HTTP_PROXY=http://your.http-proxy.url:port/ HTTPS_PROXY=http://your.https-proxy.url:port/

Redsocks
********

git over ssh
************

Add the following to your :file:`~/.ssh/config`:

.. code-block:: bash

    host github.com
    port 22    
    user git
    ProxyCommand connect-proxy -S your.ssh-proxy.url:port %h %p

.. note::

    Thought netcat is included with Clear Linux, it is not the BSD version,
    which is the one usually used to enable git over ssh.

Transitioning between proxy and non-proxy environments
******************************************************
