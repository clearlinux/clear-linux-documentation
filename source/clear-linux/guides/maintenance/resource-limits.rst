.. _resource-limits:

Resource limits
###############

Linux systems employ limiting or quota mechanisms to provide quality of
service for system resources and contain rogue processes.

These limits are layered at the system-level and user-level. If these limits
need to be modified, it is useful to understand the different limit
configurations.  

.. contents:: :local:
    :depth: 2


System-wide limits
==================
 
Some global resource limits are implemented in the Linux kernel and are
controllable with kernel parameters. 

For example, a global limit for the maximum number of open files is set with
the *fs.file-max* parameter. This limit applies to all processes and users an
cannot be exceeded other limit values. 

You can check the current value with:

.. code::

   sysctl -n fs.file-max

This value is set intentionally high on |CL| systems by default. 

The value can be overridden temporarily with :command:`sysctl -w
fs.file-max=<NUMBER>` or permanently with a :file:`/etc/sysctl.d/*.conf` file
(see :command:`man sysctl.d` for details).



Per-user limits
===============

For processes not managed by systemd, resource limits can be set for PAM
logins on a per-user basis with upper and lower limits in the
:file:`/etc/security/limits.conf` file.

You can set temporary values and check the current values with the
:command:`ulimit` command. For example, to change the soft limit of maximum
number of open file descriptors for the current user:

.. code::

   ulimit -S -n <NUMBER>

See :command:`man limits.conf` for details. 


Service limits
==============

Resource limits for services started with systemd units do not follow normal
user limits because the process is started in a seperate `Linux control group
(cgroup) <https://www.kernel.org/doc/Documentation/cgroup-v2.txt>`_ Linux
cgroups associate related process groups and provide resource accounting. 

Resource limits for individual systemd services can be controlled inside their
unit files or its configuration drop-in directory with the resource Limit
directives. See `process properties section of the systemd.exec man page
<https://www.freedesktop.org/software/systemd/man/systemd.exec.html>`_.

Resource limits for all systemd services can be controlled with a file in the
:file:`/etc/systemd/system.conf.d/` directory. For example, to have no
restriction on the number of open files: 

.. code::
   
   sudo mkdir -p /etc/systemd/system.conf.d/

   sudo tee /etc/systemd/system.conf.d/50-nfiles.conf  > /dev/null <<'EOF'
   [Manager]
   DefaultLimitNOFILE=infinity
   EOF







