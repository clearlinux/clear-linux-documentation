.. _restart:

Restart system services after an OS update
##########################################

This guide describes how to use the :command:`clr-service-restart` tool.

.. contents::
   :local:
   :depth: 1

Overview
********

|CL-ATTR| includes a :command:`clr-service-restart` tool that shows which
system daemons require a restart.

:command:`clr-service-restart` reads various files in the :file:`procfs`
filesystem provided by the kernel and relies on :command:`systemd` to
determine which services to restart.


How it works
************

:command:`clr-service-restart` implements a whitelist to identify which
daemons can be restarted. As a system administrator, you can customize the
default |CL| OS whitelist using :command:`allow` or :command:`disallow` options
for restarting system services. When a software update occurs,
:command:`clr-service-restart` consults the whitelist to see if a service daemon
is allowed to be restarted or not.


Basic options
*************

:command:`clr-service-restart` has three basic options: :command:`allow`,
:command:`disallow`, and :command:`default`.

allow
=====

The :command:`allow` option identifies a daemon to restart after an OS software
update. The :command:`clr-service-restart` daemon creates a symlink in
:file:`/etc/clr-service-restart` as a record. The example below tells
:command:`clr-service-restart` to restart the *tallow* daemon after an
OS software update.

.. code-block:: bash

   sudo clr-service-restart allow tallow.service

disallow
========

The :command:`disallow` option tells :command:`clr-service-restart` not to
restart the specified daemon even if the OS defaults permit the daemon to be
restarted. The :command:`clr-service-restart` daemon creates a symlink in
:file:`/etc/clr-service-restart` that points to :file:`/dev/null` as a
record. The example below tells :command:`clr-service-restart` not to
restart the *rngd* daemon after an OS software update.

.. code-block:: bash

   sudo clr-service-restart disallow rngd

default
=======

The :command:`default` option makes :command:`clr-service-restart` revert back
to the OS defaults and delete any symlink  in :file:`/etc/clr-service-restart`.
The example below  tells :command:`clr-service-restart` to restart *rngd*
automatically again, because *rngd* is whitelisted for automatic service
restarts by default in |CL|.

.. code-block:: bash

   sudo clr-service-restart default rngd

Monitor options
***************

:command:`clr-service-restart` works in the background and is invoked with
:command:`swupd` automatically. Review the journal output to verify that
services are restarted after an OS software update.

If you pass both options (:command:`-a` and :command:`-n`) described below,
:command:`clr-service-restart` displays a complete list of system services
that require a restart. Use both options to verify that all desired daemons
are restarted.


-n option
=========

The :command:`-n` option makes :command:`clr-service-restart` perform no restarts.
Instead it displays the services that could potentially be restarted. When used,
:command:`clr-service-restart` outputs a list of messages showing:

* Which service needs a restart.
* What unit it is.
* Why it needs a restart.
* Which command is required to restart the unit.

-a option
=========

The :command:`-a` option makes :command:`clr-service-restart` consider all system
services, not only the ones that are whitelisted. Because the default whitelist
in |CL| is relatively short, you can use this option to restart all impacted
services when you log in on the system.

Example
*******

In the example below, :command:`clr-service-restart` is invoked with both the
:command:`-a` and :command:`-n` options, which displays a complete list of system
services that require a restart.

Command:

.. code-block:: bash

     sudo clr-service-restart -a -n

Sample output:

.. code-block:: console

     upower.service: needs a restart (a library dependency was updated)
     /usr/bin/systemctl --no-ask-password try-restart upower.service
     NetworkManager.service: needs a restart (a library dependency was
     updated)
     /usr/bin/systemctl --no-ask-password try-restart NetworkManager.service
     ....

Telemetry
*********

:command:`clr-service-restart` may cause problems such as a short service
outage when a daemon is being restarted, or if a daemon fails to properly
restart. To minimize issues, :command:`clr-service-restart` creates a
telemetry record and sends it to the optional |CL| telemetry service if both
conditions below are met:

* If a unit fails to automatically restart after an OS update.
* If that unit resides in the system location :file:`/usr/lib/systemd/system`.

If you do not install the |CL| telemetrics bundle, the data is discarded. If
you install the telemetrics bundle and you opt to send telemetry, then the
system unit name is sent to the |CL| telemetry service. We evaluate the
report and update the whitelist to remove services that are not safe to
restart.


Conclusion
**********

The |CL| team enjoys coming up with simple and efficient solutions to make
your work easier. We made a GitHub\* project of :command:`clr-service-restart`
and we invite you to look at the code, share your thoughts, and work with us
on improving the project. You can find the project at:

https://github.com/clearlinux/clr-service-restart
