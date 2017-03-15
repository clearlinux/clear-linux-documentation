.. _bdl-containers-basic:

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

.. note::

   If you are behind an HTTP proxy server, for example in a corporate
   setting, please follow the `Docker proxy instructions`_.

For more information on |CC| please see the
`Clear Containers runtime Github`_.

.. _Clear Containers runtime github: https://github.com/01org/cc-oci-runtime

.. _Docker proxy instructions:
   https://docs.docker.xom/engine/admin/systemd/#http-proxy