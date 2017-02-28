.. _bdl-containers-basic:

containers-basic
################

Overview
========

The `containers-basic` bundle adds the necessary tools to enable running
containers using Docker*. The bundle includes Intel® Clear Containers as an
additional Docker runtime.

Clear Containers enables a hardware backed Virtual Machine (VM) based container
runtime, compared with the normal software namespace containers provided by
standard Docker `runc` runtime.

Default runtime
===============
If your system has `VT-x` enabled then, under Clear Linux,  Clear Containers
will be used as the default Docker runtime, otherwise the standard Docker
`runc` runtime will be used.


To identify which runtimes are available, as well as which  is being used as
the default on your installed system, you can run the following command. Clear
Containers runtime will be listed as `cor`::

    $ sudo docker info | grep Runtime

For more information on Clear Containers please see the `Clear Containers runtime github`_.

.. _Clear Containers runtime github: https://github.com/01org/cc-oci-runtime

