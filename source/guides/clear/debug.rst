.. _debug:

Debug system
############

|CL-ATTR| introduces a novel approach to system software debugging using
*clr-debug-info*. On the client side, the |CL| debug system obtains any
necessary debug information on-the-fly over a network during a debugging
session. On the server side, the system curates and compresses debug
information into small pieces for efficient downloading.

For developers, this avoids the interruption during debugging that usually
happens when debug information is missing. This can be especially useful on
systems where storage is limited. 


.. contents:: :local:
    :depth: 2


Background
----------

Software that is compiled and packaged for general usage in an operating
system typically only contains components that are used to execute the
program, such as binaries and libraries. Extra developer data, such as the
actual source code and symbol information, are separated and excluded for
efficiency. 

The debug information helps relate binary code to human readable source code
lines and variables. Most of the time, this auxiliary information 
is not needed;
however without it, debugging a program results in limited visibility. 


Usage
-----

The clr-debug-info system is integrated into |CL| and seamlessly engages once
installed.

#. Install the *dev-utils* bundle.

   .. code:: bash

      sudo swupd bundle-add dev-utils 

   .. note::

      The *telemetrics* and *performance-tools* bundles also include
      clr-debug-info.


#. Start a debugging session against a program using a debugger, such as GDB. 
   For example, to debug *gnome-control-center* execute the following
   command:

   .. code:: bash

      gdb /usr/bin/gnome-control-center

As you step through the program and debug information is needed, the
clr_debug_daemon obtains it in the background.


Implementation
--------------

The implementation of the |CL| debug system is open source and available on
GitHub at: https://github.com/clearlinux/clr-debug-info/

.. figure:: figures/debug-diagram.png
   :width: 400px
   :alt: Debug system communication flow

   Figure 1: The communication flow of the |CL| debug system

The |CL| debug system implements a :abbr:`FUSE (filesystem in userspace)`
filesystem mounted at :file:`/usr/lib/debug` and :file:`/usr/src/debug`. The
FUSE filesystem starts automatically. You can verify its status by executing
:command:`systemctl status clr_debug_fuse.service`.

The *clr_debug_daemon* is responsible for fetching the appropriate package
debug content from the server and making it available for any debugging
programs that need it. It is socket activated whenever a request to the local
FUSE filesystem occurs. You can verify its status with :command:`systemctl
status clr_debug_daemon.service`.


|CL| hosts debuginfo content packaged for consumption by |CL| debug clients at
https://download.clearlinux.org/debuginfo/
