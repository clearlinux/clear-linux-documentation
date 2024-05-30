.. _autoproxy:

Autoproxy
#########

Autoproxy is provided to enable |CL-ATTR| to work smoothly behind a
corporate proxy.

.. contents::
   :local:
   :depth: 1

Description
***********

Autoproxy tries to detect a Proxy Auto-Config (PAC) script and use it to
automatically resolve the proxy needed for a given connection. With
Autoproxy, you can use |CL| inside any proxy environment without having to
manually configure the proxies.

Corporate and private networks can be very complex, needing to restrict and
control network connections for security reasons. The typical side effects
are limited or blocked connectivity, and require manual configuration of
proxies to perform the most mundane tasks, such as cloning a repo or checking
for updates. With |CL|, all of the work is done behind the scenes to
effortlessly use your network and have connections “just work”.

This feature removes severe complications with network connectivity due to
proxy issues. You can automate tasks, such as unit testing, without worrying
about the proxy not being set, and you can remove unset proxies from the
equation when dealing with network unavailability across systems.

How it works
************

We designed Autoproxy around tools provided by most Linux\*
distributions with a few minor additions and modifications. We leveraged the
DHCP and network information obtained from systemd and created a
PAC-discovery daemon. The daemon uses the information to resolve a URL for a
PAC file. The daemon then passes the URL into PACrunner\*. PACrunner
downloads the PAC file and uses the newly implemented Duktape\* engine to
parse it.

.. figure:: figures/autoproxy_0.png
   :width: 400px

   Figure 1: Autoproxy Flow

From that point on, any cURL\* or network requests query PACrunner for the
correct proxy to use. We modified the cURL library to communicate with
PACrunner over DBus. However, cURL will ignore PACrunner and run normally if
no PAC file is loaded or if you manually set any proxies. Thus, your
environment settings are respected and no time is wasted trying to resolve a
proxy. All these steps happen in the background with no user interaction.

Troubleshooting
===============

Autoproxy allows |CL| to operate seamlessly behind a proxy
because :ref:`swupd <swupd-guide>` and other |CL| tools are implemented on
top of libcurl. Tools that do not use libcurl, like git, must
be configured independently. 

If you are familiar with PAC files and WPAD, you can use
:command:`pacdiscovery` and :command:`FindProxyForURL` to
troubleshoot problems with autproxy.

.. note::

   Learn more about WPAD, PAC files, and PAC functions at `findproxyforurl`_.

.. _findproxyforurl: http://findproxyforurl.com/

Run :command:`pacdiscovery` with no arguments to indicate

1. if there is a problem resolving the :command:`WPAD` host name resolution: 

   .. code-block:: bash

      pacdiscovery

   .. code-block:: console

      failed getaddrinfo: No address associated with hostname
      Unable to find wpad host

2. or if the :command:`pacrunner` service is disabled (masked).

   .. code-block:: bash

      pacdiscovery

   .. code-block:: console

      PAC url: http://autoproxy.your.domain.com/wpad.dat
      Failed to create proxy config: Unit pacrunner.service is masked.

Unmask the :command:`pacrunner` service by running:

.. code-block:: bash

   systemctl unmask pacrunner.service

:command:`FindProxyForURL` with :command:`busctl` can also indicate if the
:command:`pacrunner.service` is masked.

.. code-block:: bash

   busctl call org.pacrunner /org/pacrunner/client org.pacrunner.Client 

.. code-block:: console
   
   FindProxyForURL ss "http://www.google.com" "google.com"
   Unit pacrunner.service is masked.
   dig wpad, dig wpad.<domain>

:command:`FindProxyForURL` returns the URL and port of the proxy server when
an external URL and host are provided as arguments.

.. code-block:: bash

   busctl call org.pacrunner /org/pacrunner/client org.pacrunner.Client 

.. code-block:: console

   FindProxyForURL ss "http://www.google.com" "google.com"
   s "PROXY proxy.your.domain.com:<port>"

If a proxy server is not avialable, or if :command:`pacrunner` is running
without a PAC file, :command:`FindProxyForURL` will return "DIRECT". 

.. code-block:: bash

   busctl call org.pacrunner /org/pacrunner/client org.pacrunner.Client 

.. code-block:: console 

   FindProxyForURL ss "http://www.google.com" "google.com"
   s "DIRECT"

Once :command:`pacdiscovery` is able to look up :command:`WPAD`, restart the
:command:`pacrunner` service:

.. code-block:: bash

   systemctl stop pacrunner
   systemctl restart pacdiscovery

.. note::

   A "domain" or "search" entry in :file:`/etc/resolv.conf` is required
   for short name lookups to resolve. The :file:`resolv.conf` man page has
   additional details.