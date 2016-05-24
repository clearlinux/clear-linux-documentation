How to run the updater
######################

This section describes how to manually trigger the software update code in Clear Linux* OS for Intel® Architecture.

Prerequisites
~~~~~~~~~~~~~

-  System is up and running a Clear Linux OS for Intel
   Architecture official build, 300 or later.

-  Device is on a well-connected network.

-  Device is able to connect to release infrastructure. For example:
   http://update.clearlinux.org/update/300/

Running the updater
~~~~~~~~~~~~~~~~~~~

#. Open a Terminal Emulator.

#. Become root and trigger an update with this command::

    # swupd update

#. If the updater console output indicates a kernel update occurred,
   then at your convenience reboot to begin using the new OS version.

Updater options
~~~~~~~~~~~~~~~

Help options:

-  ``-h, --help`` Display help options.

Application options:

-  ``-d, --download`` Download all content, but do not actually install
   the update.

-  ``-v, --verbose`` Increase verbosity of log and console messages.
