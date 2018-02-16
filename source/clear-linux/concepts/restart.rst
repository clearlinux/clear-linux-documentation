.. _cl-restart:

Restarting system services after an OS update
#############################################

The software life cycle describes how software is created, developed, and
deployed, but also includes how to replace or update software. A good OS
provides tools for the entire software life cycle. These tools must include
ways to remove software components properly when replaced with something else.

Most of the work on software update code in |CL| has primarily focused on
adding new software to the system. Aside from recommending to users to reboot
their system once in a while to ensure the new software is running, we did not
provide any tools to do this easily, until now.

User challenges
***************

Users might find it difficult to determine which services to restart. Users
can either evaluate each system and reboot manually, or figure out which
services to restart based on documentation like the |CL| Release Notes.
Since neither option solves the issue for many users, we established
improvement in this area was needed.

Over the years, several OSes have approached the problem and come up with
partial solutions. Some solutions are based on three steps:

#. Mark updates requiring a reboot, such as kernel updates.
#. Inform the user of those updates.
#. Ask usersto restart.

Other variants automatically restart services during an upgrade. These
solutions are acceptable since there is nothing wrong with regularly
restarting services when your OS does not update automatically. Users are
already logged into a terminal, aware of updates happening, and ready to
respond to messages and notices about additional actions to take after an OS
update.

However, |CL| updates software automatically and users never see any notices
from the updater. Users can still review the journal, which stores updater
notices.

This scenario requires a completely different solution. Thus, we arrive at the
following solution requirements:

* Eliminate the guesswork about what to restart and under what circumstances.
* Cannot restart everything. Many service deamons do not yet support an automatic
  background restart.
* Fit into the |CL| architectural perspective: be small, quick, and lean.

Enter :command:`clr-service-restart`
************************************

After exploring possible solutions, we devised a simple and efficient method
of catching the most typical reasons to restart a service daemon:

* The new version replaced the executable file itself.
* The new version replaces a library component used by a service daemon.

Both cases are extremely common. Thus, any solution that can detect these situations will provide good results for
our purposes. There are other cases to consider, for instance, when
configuration files or shared data files change on disk, but this is less
common. Our method focuses on restarting daemons when it is really needed,
especially in the case of security updates.

The kernel actually provides us with this exact information in the
:file:`procfs` filesystem. Both the deleted executable file case and the
upgraded library component file case are detectable by reading
various files in the :file:`procfs` filesystem.

The second part of the problem is to determine whether or not actual running
processes are part of a system service. The reason we're only interested
in system services is because that is where the risk is large for
security issues, and most system services are background tasks that
have no direct user interaction. We did not consider restarting things such
as desktop tasks because it would ruin any sort of user experience quickly.

Fortunately, :command:`systemd` provides us with a simple way of determining
what tasks are active and entirely within the system domain, and we can
directly determine what service daemon they are part of. This approach
eliminates any daemon that is not started to begin with.

The combination of these two partial solutions effectively gives us a nice
tool, with very little overhead, that shows which system daemons
are in need of a restart:

    Figure 1: Invoking :command:`clr-service-restart' to show all system
    services in need of a restart

    .. code-block:: bash

      $ sudo clr-service-restart -a -n

    .. code-block:: console

      upower.service: needs a restart (a library dependency was updated)
      /usr/bin/systemctl --no-ask-password try-restart upower.service
      NetworkManager.service: needs a restart (a library dependency was
      updated)
      /usr/bin/systemctl --no-ask-password try-restart NetworkManager.service
      ....

Making it `safe`
****************

Now that we know exactly what daemons should be restarted, we can go
ahead and restart all of them, right? Not so fast! You definitely
don't want to do this automatically. Restarting the gdm.service automatically
on all the PCs in the office will not get you brownie points.

Before doing the restart, we need some selection mechanism to figure out what
is OK to restart, and what is not. Since we want to restart the important
processes automatically and in the background, we want to be conservative
and start with low-risk daemons that we know are restartable without
any significant impact. So, we need a whitelist.

We've implemented this whitelist in |CL| by making
:command:`clr-service-restart` a one-stop tool to manipulate this
whitelist. By default, the |CL| OS provides a basic set of whitelist entries
that permit :command:`clr-service-restart`
to perform automatic restarts of service daemons if they are whitelisted
already. On top of that, the system administrator can maintain
their own overlay customization of the whitelist, by allowing them to either
'allow' or 'disallow' restarting of system services as well. When a software
update occurs, the whitelist is consulted to see if a service daemon is
allowed to be restarted or not.

This gives local administrators full control over the process. Either the
local administrator can turn restarting all off, or they can add more
services to the list if needed.

Options for :command:`clr-service-restart`
==========================================

The :option:`allow` option tells :command:`clr-service-restart` that on this
machine, the tallow daemon may be restarted automatically after an OS
software update. The :command:`clr-service-restart` daemon creates the
appropriate symlink in :file:`/etc/clr-service-restart` to keep a record
of this.

  .. code-block:: bash

  $ sudo clr-service-restart allow tallow.service

The :option:`disallow` command tells :command:`clr-service-restart` that
although the OS defaults permit :option:`rngd` to be restarted, it should not
be done on this particular system. A symlink is created in
:file:`/etc/clr-service-restart` that points to :file:`/dev/null` to record
this. Note that you don't need to add the :option:'.service' part to refer to
the correct unit name.

  .. code-block:: bash

  $ sudo clr-service-restart disallow rngd

The :option:`default` command makes :command:`clr-service-restart` revert
back to the OS provided defaults and delete any symlink in
:file:`/etc/clr-service-restart`. In the following example, it causes
:option:`rngd` to be restarted automatically again, because it is whitelisted
for automatic service restarts by default in |CL|.

  .. code-block:: bash

  $ sudo clr-service-restart default rngd

Checking in on :command:`clr-service-restart`
*********************************************

:command:`clr-service-restart` works in the background and is invoked by
:command:`swupd` automatically. The journal output shows
that services are being restarted once in a while after an OS software update.

This still means that there are system services that are not being restarted,
so you may want check on the current situation and potentially take action.
To enable this, :command:`clr-service-restart` can be invoked with two
additional options, which are described below.

  :option:`-n`

This option makes :command:`clr-service-restart` perform no restarts. Instead
it displays the services that could potentially be restarted. When used,
:command:`clr-service-restart` outputs a list of messages showing which
service needs a restart, what unit it is, and why it needs a restart. Also,
it shows the command that it would have used to restart this unit.

  :option:`-a`

This option makes :command:`clr-service-restart` consider all system
services, not just the ones that are whitelisted. Because the default
whitelist in |CL| is relatively short at the moment, you may want to use this
option to restart everything that it can find when you log in on the system.

Of course, if you pass both options (:option:`-a` and :option:`-n`), you will
see the complete list of system services that need a restart. This is
very handy to answer the question whether you may have missed restarting
another daemon or not, without actually doing this inadvertently.

Telemetry
*********

The |CL| team has attempted to minimize any disruption caused by this tool,
but we realize that it can cause problems, either in the form of a short
service outage when a daemon is being restarted, or worse, when a daemon
fails to properly restart.

For that reason, we have created a whitelist to ensure units that we do not
trust to restart are left alone, however, if something bad does happen, we
want to have a way of catching it early.

We've implemented this as follows:
If we find a unit that fails to automatically restart after an OS update,
and that unit resides in the system location :file:`/usr/lib/systemd/system`,
then we create a telemetry record and
send that record to the optional |CL| telemetry service.

If you don't have the |CL| telemetrics bundle installed, nothing will happen
with this data - it is discarded. However, if you do have the
telemetrics bundle installed, and you opted in to send telemetry, then
the name of the system unit is sent to our telemetry service. This allows
us to quickly correct mistakes and remove services that are not as
safe to restart as we thought.

Conclusion
**********

As always, we enjoy coming up with simple and efficient solutions that make
our |CL| users' lives easier, and we love to share them with a bigger
audience. We've made a github project of :command:`clr-service-restart` and
you are invited to look at the code, share your thoughts, and work with us on
improving the project. You can find the project at:

  https://github.com/clearlinux/clr-service-restart