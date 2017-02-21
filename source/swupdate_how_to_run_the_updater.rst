How to run the updater
######################

This section describes how to manually trigger the software update code in Clear Linux* OS for Intel® Architecture.

Prerequisites
~~~~~~~~~~~~~

-  System is up and running a Clear Linux OS for Intel
   Architecture official build, 7420 later.

-  Device is on a well-connected network.

-  Device is able to connect to release infrastructure. For example:
   http://update.clearlinux.org/update/300/

Running the updater
~~~~~~~~~~~~~~~~~~~

#. Open a Terminal Emulator.

#. Become root and trigger an update with this command::
.. code-block:: bash
   $ swupd update

#. If the updater console output indicates a kernel update occurred,
   then at your convenience reboot to begin using the new OS version.

Updater options
~~~~~~~~~~~~~~~

Help options:

.. code-block:: console
   -h, --help Display help options.

Application options:
.. code-block:: console
   -d, --download          Download all content, but do not actually install the update
   -u, --url=[URL]         RFC-3986 encoded url for version string and content file downloads
   -P, --port=[port #]     Port number to connect to at the url for version string and content file downloads
   -c, --contenturl=[URL]  RFC-3986 encoded url for content file downloads
   -v, --versionurl=[URL]  RFC-3986 encoded url for version string download
   -s, --status            Show current OS version and latest version available on server
   -F, --format=[staging,1,2,etc.]  the format suffix for version file downloads
   -p, --path=[PATH...]    Use [PATH...] as the path to verify (eg: a chroot or btrfs subvol
   -x, --force             Attempt to proceed even if non-critical errors found
   -n, --nosigcheck        Do not attempt to enforce certificate or signature checking
   -S, --statedir          Specify alternate swupd state directory
   -C, --certpath          Specify alternate path to swupd certificates
   -t, --time         	   Show verbose time output for swupd operations
