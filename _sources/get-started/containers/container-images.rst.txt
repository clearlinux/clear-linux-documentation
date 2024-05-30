.. _container-images:

|CL-ATTR| container images
##########################

|CL| can run inside of a container on top of any operating system as long as
it is hosting a containerized environment, such as Docker* or Kubernetes*. A
|CL| base image is available for standalone use as well as variations of
popular application images built from the |CL| base image.

Browse all |CL| container images on `the Docker Hub* website
<https://hub.docker.com/search?q=clearlinux&type=image>`_. Find the
Dockerfiles used to build |CL| container images `on GitHub
<https://github.com/clearlinux/dockerfiles>`_.

See the `containers <https://clearlinux.org/downloads/containers>`_ page for
the benefits of using |CL| containers and using |CL| as a container host.

Container image types
*********************

|CL| base image
===============

The `Clear Linux OS base container <https://hub.docker.com/_/clearlinux>`_ is
an official image on Docker Hub*. The |CL| base container image can be used to
run a standalone or as a `parent image
<https://docs.docker.com/glossary/#parent_image>`_ for building other
container images. 

On a Docker host simply use the command :command:`docker run clearlinux` to
pull and start a |CL| container. 


|CL|-based runtime images
=========================

|CL| container images for programming languages and their runtimes are
available on Docker Hub*. These can be used by developers to create and run
applications using these popular runtimes. 

Below are some popular |CL|-based runtime images:

* `clearlinux/golang <https://hub.docker.com/r/clearlinux/golang>`_
* `clearlinux/node <https://hub.docker.com/r/clearlinux/node>`_
* `clearlinux/numpy <https://hub.docker.com/r/clearlinux/numpy>`_
* `clearlinux/python <https://hub.docker.com/r/clearlinux/python>`_
* `clearlinux/perl <https://hub.docker.com/r/clearlinux/perl>`_
* `clearlinux/r-base <https://hub.docker.com/r/clearlinux/r-base>`_

More |CL|-based images can be found on Docker Hub:
https://hub.docker.com/u/clearlinux.


|CL|-based application images
=============================

|CL| container images for common applications are available on Docker Hub.
These can be used to create and deploy containerized services.

Below are some popular |CL|-based runtime images:

* `clearlinux/nginx <https://hub.docker.com/r/clearlinux/nginx>`_
* `clearlinux/mariadb <https://hub.docker.com/r/clearlinux/mariadb>`_
* `clearlinux/postgres <https://hub.docker.com/r/clearlinux/postgres>`_
* `clearlinux/redis <https://hub.docker.com/r/clearlinux/redis>`_
* `clearlinux/tensorflow <https://hub.docker.com/r/clearlinux/tensorflow>`_
* `clearlinux/wordpress <https://hub.docker.com/r/clearlinux/wordpress>`_


More |CL|-based images can be found on Docker Hub:
https://hub.docker.com/u/clearlinux.

Related topics
==============
* :ref:`container-image-new`
* :ref:`container-image-modify`
* :ref:`docker`
* :ref:`kata`
