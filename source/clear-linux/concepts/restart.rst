.. _cl-restart:

Restart system services after an OS update
##########################################

The software life cycle describes how software is created, developed, and
deployed, and includes how to replace or update software. A good OS
provides tools for the entire software life cycle. These tools must include
ways to remove software components properly when replaced with something else.

Most of the work on software update code in |CL| has primarily focused on
adding new software to the system. We recommend that users reboot their system
once in a while, but we did not provide any tools to restart services easily,
until now.

User challenges
***************

It is difficult to determine which services to restart. You can either
evaluate each system and reboot manually, or figure out which services to
restart based on documentation like the |CL| release notes. Since neither
option solves the issue completely, the |CL| team created a solution.

Over the years, several OSes approached the problem and created partial
solutions such as the following:

* Automatically restart services during an upgrade.
* Evaluate services using these steps:

  * Mark updates requiring a reboot, such as kernel updates.
  * Inform the user of those updates.
  * Ask the user to restart.

Both solutions are acceptable for many OSes. However, |CL| updates software
automatically and users do not see notices from the updater unless they review
the journal.

|CL| requires a completely different solution, with the following
requirements:

* Eliminate the guesswork about what to restart and under what circumstances.
* Cannot restart everything. Many service daemons do not support an automatic
  background restart.
* Fit into the |CL| architectural perspective: be small, quick, and lean.

:command:`clr-service-restart` functionality
********************************************

Typical reasons to restart a service daemon include:

* A new version replaces the executable file itself.
* A new version replaces a library component used by a service daemon.

Our method restarts daemons for both cases by reading various files in the
:file:`procfs` filesystem provided by the kernel.

The second part of the problem is to determine whether or not running
processes are part of a system service. The tool focuses on system services
because most system services are background tasks with no direct user
interaction. Fortunately, :command:`systemd` provides a simple way to:

* Determine which active tasks are within the system domain.
* Determine which service daemon maps to the task.

We combined both solutions into a low-overhead tool that shows which system
daemons require a restart, as shown below:

    Figure 1: Invoke :command:`clr-service-restart`.

    .. code-block:: bash

       sudo clr-service-restart -a -n

    .. code-block:: console

      upower.service: needs a restart (a library dependency was updated)
      /usr/bin/systemctl --no-ask-password try-restart upower.service
      NetworkManager.service: needs a restart (a library dependency was
      updated)
      /usr/bin/systemctl --no-ask-password try-restart NetworkManager.service
      ....

:command:`clr-service-restart` implements a whitelist to identify which
daemons can be restarted. The system administrator maintains a customized
overlay of the default |CL| OS whitelist. When a software update occurs,
:command:`clr-service-restart` consults the whitelist to see if a service
daemon is allowed to be restarted or not. See the options section below for
details.


Options for :command:`clr-service-restart`
******************************************

The :option:`allow` option identifies a daemon to restart after an OS software
update. The :command:`clr-service-restart` daemon creates a symlink in
:file:`/etc/clr-service-restart` as a record. The example below tells
:command:`clr-service-restart` to restart the :option:`tallow` daemon after an
OS software update.

  .. code-block:: bash

     sudo clr-service-restart allow tallow.service

The :option:`disallow` option tells :command:`clr-service-restart` not to
restart the specified daemon even if the OS defaults permit the daemon to be
restarted. The :command:`clr-service-restart` daemon creates a symlink in
:file:`/etc/clr-service-restart` that points to :file:`/dev/null` as a record.
The example below tells :command:`clr-service-restart` not to restart the
:option:`rngd` daemon after an OS software update.

  .. code-block:: bash

     sudo clr-service-restart disallow rngd

The :option:`default` option makes :command:`clr-service-restart` revert back
to the OS defaults and delete any symlink in :file:`/etc/clr-service-restart`.
The example below tells :command:`clr-service-restart` to restart
:option:`rngd` automatically again, because :option:`rngd` is whitelisted for
automatic service restarts by default in |CL|.

  .. code-block:: bash

     sudo clr-service-restart default rngd

Monitor options for :command:`clr-service-restart`
==================================================

:command:`clr-service-restart` works in the background and is invoked with
:command:`swupd` automatically. Review the journal output to verify that
services are restarted after an OS software update.

To monitor :command:`clr-service-restart`, use one or both options described
below.

  :option:`-n`

This option makes :command:`clr-service-restart` perform no restarts. Instead
it displays the services that could potentially be restarted. When used,
:command:`clr-service-restart` outputs a list of messages showing:

* Which service needs a restart.
* What unit it is.
* Why it needs a restart.
* Which command is required to restart the unit.

  :option:`-a`

This option makes :command:`clr-service-restart` consider all system services,
not only the ones that are whitelisted. Because the default whitelist in |CL|
is relatively short, you can use this option to restart all impacted services
when you log in on the system.

If you pass both options (:option:`-a` and :option:`-n`),
:command:`clr-service-restart` displays a complete list of system services
that require a restart. Use both options to verify that all desired daemons
are restarted.


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
system unit name is sent to the |CL| telemetry service. We evaluate the report
and update the whitelist to remove services that are not safe to restart.

Conclusion
**********

The |CL| team enjoys coming up with simple and efficient solutions to make
your work easier. We made a github project of :command:`clr-service-restart`
and we invite you to look at the code, share your thoughts, and work with us
on improving the project. You can find the project at:

  https://github.com/clearlinux/clr-service-restart