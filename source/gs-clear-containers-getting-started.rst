.. _gs-clear-containers-getting-started:

Clear Containers getting started guide
######################################

Intel® Clear Containers for Docker* Engine is now available 
for multiple operating systems. This enables executing existing
Docker applications in the secure and fast Intel Clear Containers
environment.  See also the `Architecture Overview`_.


Binary packages
===============

The primary host platform is Clear Linux* Project for Intel® 
Architecture, version 4000 or better. However, binaries for a
range of operating systems are available from:

- https://software.opensuse.org/package/clear-containers-docker

Currently experimental builds are available for:

- CentOS*, Scientific Linux* 7
- Fedora* 21, 22, 23
- openSUSE* 13.1, 13.2, Tumbleweed
- SUSE* Linux Enterprise 12
- Debian* 8.0
- Ubuntu* 15.04

If you have any feedback, please mail it to the 
dev@lists.clearlinux.org mailing list. Subscription to this 
list is available at: https://lists.clearlinux.org/mailman/listinfo/dev.

Installation instructions
=========================

Using hosts other than Clear Linux OS for Intel Architecture
------------------------------------------------------------

If you are *not* using Clear Linux OS for Intel Architecture, follow the instructions below:

#. Visit the link below and select your operating system by clicking the appropriate icon:
   https://software.opensuse.org/download.html?project=home%3Aclearlinux%3Apreview&package=clear-containers-docker

#. Follow the brief instructions shown.

#. If your host is behind a proxy, you will need to add the proxies to the docker service. Create ``/etc/systemd/system/docker.service.d/proxy.conf`` and add the next lines to the file::

    [Service]
    Environment=HTTP_PROXY=http://proxy.example.com:80/
    Environment=NO_PROXY=localhost,127.0.0.1

#. Reload your systemd configuration::

   $ sudo systemctl daemon-reload

#. Start the Docker service::

   $ systemctl restart docker

Using Clear Linux OS for Intel Architecture as Host
---------------------------------------------------

If you are running Clear Linux OS for Intel Architecture on your 
host system, follow the instructions below:

#. Enable the repository by running the following as the ``root`` user::

   # swupd bundle-add containers-basic

#. Reload your systemd configuration::

   $ sudo systemctl daemon-reload

#. Start the Docker service::

   $ systemctl restart docker

Source Code
===========

The experimental source code is based on the Docker version 1.9.0
upstream release and is available at:

- https://github.com/clearlinux/docker



.. _Architecture Overview: https://clearlinux.org/documentation/clear-containers.html#architecture-overview