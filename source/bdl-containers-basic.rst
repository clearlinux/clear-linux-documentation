.. _bdl-containers-basic:

containers-basic
################

This bundle provides container applications

Multiple runtime support for Docker
===================================

Docker\* 1.12+ provides a way to execute containers using different **"oci
runtimes"**. An **"oci runtime"** is  software compatible with :abbr:`OCI 
(Open Containers Initiative)` specification that is responsible to create
a container.

.. note:: Docker in Clear Linux is configured to use 2 runtimes:

**cc-oci-runtime**: This is the default runtime used by docker in Clear Linux (if
Vt-x support is enabled). This runtime provides the capability to create secure
containers using Clear Containers (based VM containers).

**runc**: This runtime is used to spawn and run containers using namespaces and
cgroups (this is the traditional way to create containers used by docker).

In Clear Linux, each time a container is created it uses cc-oci-runtime (*A.K.A*
**cor**). 

To start a secure container with cc-oci-runtime aka cor::

  docker run -ti debian sh 

In the case you want to start a non secure container. You can
use the option **--runtime=runc** in the docker command **"run"**

To start an non-secure container using runc runtime::

  docker run --runtime=runc -ti debian sh

Change default runtime
======================

To modify the default runtime you can override
the stateless docker daemon configuration
creating the file :file:`/etc/systemd/system/docker-cor.service.d/docker.conf`
and adding **--default-runtinme=runc**::

  [Service]                                                  
  ExecStart=/usr/bin/dockerd -H fd:// --storage-driver=overlay --add runtime cor=cc-oci-runtime --default-runtime=runc    

HTTP proxy
==========

If you are behind an HTTP proxy server, for example in corporate settings, you
will need to add this configuration in the Docker systemd service file.

First, create a systemd drop-in directory for the docker service::

  mkdir /etc/systemd/system/docker-cor.service.d

Now create a file called :file:`/etc/systemd/system/docker-cor.service.d/http-proxy.conf`
that adds the HTTP_PROXY environment variable::

  [Service]
  Environment="HTTP_PROXY=http://proxy.example.com:80/"

If you have internal Docker registries that you need to contact without proxying
you can specify them via the NO_PROXY environment variable::

  Environment="HTTP_PROXY=http://proxy.example.com:80/" "NO_PROXY=localhost,127.0.0.1,docker-registry.somecorporation.com"

Flush changes::

  $ sudo systemctl daemon-reload

Verify that the configuration has been loaded::

  $ systemctl show --property=Environment docker-cor
  Environment=HTTP_PROXY=http://proxy.example.com:80/

Restart Docker::

  $ sudo systemctl restart docker-cor

To get more info you can view https://docs.docker.com/engine/admin/systemd/

