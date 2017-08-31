.. _containers-basic:

containers-basic
################

The `containers-basic` bundle adds the necessary tools to enable running
containers using Docker*. The bundle includes Intel® |CC| as an
additional Docker runtime.

|CC| enable a hardware backed :abbr:`VM (Virtual Machine)` based
container runtime, compared with the normal software namespace containers
provided by standard Docker `runc` runtime.

Default runtime
===============
If your system has `VT-x` enabled, then, under |CL|, |CC|
will be used as the default Docker runtime, otherwise, the standard Docker
`runc` runtime will be used.

To identify which runtimes are available and which is being used as
the default on your installed system, run the following command.

.. code-block:: console

   sudo docker info | grep Runtime

The |CC| runtime will be listed as `cor`.

For more information on |CC| please see the
`Clear Containers runtime GitHub`_.

Working with a proxy
====================

If you are behind an HTTP proxy server, in a corporate
setting for example, please follow the `Docker proxy instructions`_.

.. _Clear Containers runtime GitHub: https://github.com/01org/cc-oci-runtime

.. _Docker proxy instructions:
   https://docs.docker.com/engine/admin/systemd/#http-proxy
