.. _compatibility-check:

Check processor and EFI firmware compatibility with Clear Linux OS for Intel® Architecture
======================================================================

On a system that is currently running a Linux operating system, follow the instructions below to determine if your target system is capable of running |CL|\*.  Otherwise, see the Note section below for other options.  

#. Download the `clear-linux-check-config.sh`_ script.

   If a browser is not available, use:

   .. code-block:: console

      curl -O https://download.clearlinux.org/current/clear-linux-check-config.sh

#. Make the script executable.

   .. code-block:: console

      chmod +x clear-linux-check-config.sh
      ./clear-linux-check-config.sh host

#. Run the script.

   #. Check to see if the host is capable of running |CL|.

      .. code-block:: console

         $ ./clear-linux-check-config.sh host

   #. Check to see if the host is capable of running |CL| in a container.

      .. code-block:: console

         $ ./clear-linux-check-config.sh container

   The script will print a list of test results similar to the output below.
   All items should return a *SUCCESS* status, thus indicating the target
   system fully supports running |CL|.

   .. code-block:: console

      Checking if host is capable of running |CL|\* OS for Intel®
      Architecture

      SUCCESS:  Intel CPU

      SUCCESS: 64-bit CPU (lm)

      SUCCESS:  Streaming SIMD Extension v4.1 (sse4_1)

      SUCCESS: EFI Firmware

.. note::

   Only a system running a Linux distribution can run the compatibility
   check. There are two alternative options:

   * Install and run a Linux distribution directly on your system.
   * Run a :ref:`live-image` from a USB drive (success does not guarantee your
     system is 100% compatible).
     
 .. _clear-linux-check-config.sh file: https://download.clearlinux.org/current/clear-linux-check-config.sh
     
