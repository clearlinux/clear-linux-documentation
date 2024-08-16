.. _proxy:

Proxy Configuration
###################

When working behind a corporate proxy server, one typically has to configure
proxy settings for applications to reach the Internet.  |CL-ATTR| has 
implemented an :ref:`autoproxy` feature to try and eliminate manual 
configurations as much as possible.  However, there are still some applications 
that cannot take full advantage of the :ref:`autoproxy` feature due to their 
own ways of configuring proxy settings.  This guide shows you how to configure 
proxy settings for some of the known applications manually.  

.. contents::
    :local:
    :depth: 1

Prerequisites
*************

* You have installed |CL| on your host system.

  For detailed instructions on installing |CL| on a bare metal system, visit
  the :ref:`bare metal installation guide <bare-metal-install-desktop>`.

General proxy settings for many applications
============================================

#. First, apply these general proxy settings which should work for many 
   applications.  If they do not work for a specific application, such as the 
   ones listed below, apply application-specific proxy settings as needed.

   Proxy settings:

   .. code-block:: none

      export http_proxy=http://<YOUR.HTTP-PROXY.URL:PORT>
      export https_proxy=http://<YOUR.HTTPS-PROXY.URL:PORT>
      export ftp_proxy=http://<YOUR.FTP-PROXY.URL:PORT>
      export socks_proxy=http://<YOUR.SOCKS-PROXY.URL:PORT>
      export no_proxy="<YOUR-DOMAIN>,localhost"
      export HTTP_PROXY=$http_proxy
      export HTTPS_PROXY=$https_proxy
      export FTP_PROXY=$ftp_proxy
      export SOCKS_PROXY=$socks_proxy
      export NO_PROXY=$no_proxy

   * *User-specific*, put them in :file:`$HOME/.bashrc`.

   * *For all users*, put them in :file:`/etc/profile.d/proxy.conf`. 

#. For the proxies to take effect, either :command:`source` the file manually
   or log out and log back in.

Docker\*
========

Please refer the official Docker links on how to configure proxies:

* `Docker client`_
* `Docker daemon`_

git over SSH
============

Add the following to your :file:`~/.ssh/config` file:

.. code-block:: none

   host github.com
        port 22
        user git
        ProxyCommand connect-proxy -S <YOUR.SSH-PROXY.URL:PORT> %h %p

.. note::

   Though :command:`netcat` is included with |CL|, it is not the BSD version,
   which is the one usually used to enable git over SSH.

autospec/mock
=============

:ref:`autospec` uses mock to do builds.  Configure mock's proxy settings with
these steps:  

#. Override the general mock configuration file with a custom one, otherwise
   your settings will get overwritten each time autospec is updated.

   .. code-block:: bash

      sudo mkdir -p /etc/mock
      sudo cp ~/clearlinux/projects/common/conf/clear.cfg /etc/mock/clear-custom.cfg

#. :command:`sudoedit` :file:`/etc/mock/clear-custom.cfg` and add the highlighted
   lines.

   .. code-block:: none
      :emphasize-lines: 3-5

      ...
      config_opts['use_bootstrap_container'] = False
      config_opts['http_proxy'] = '<YOUR.HTTP.PROXY.URL>:<PORT>'
      config_opts['https_proxy'] = '<YOUR.HTTPS.PROXY.URL>:<PORT>'
      config_opts['no_proxy'] = '<YOUR.DOMAIN>,192.168.0.0/16,localhost,127.0.0.0/8'

Kubernetes
==========

See :ref:`Setting proxy servers for Kubernetes <kubernetes>`.

.. _Docker client:
   https://docs.docker.com/network/proxy/#configure-the-docker-client

.. _Docker daemon:
   https://docs.docker.com/config/daemon/systemd/#httphttps-proxy

