.. _compatibility-check:

Check processor and EFI firmware compatibility with Clear Linux\*
*****************************************************************

On a system that is currently running a Linux operating system, follow the
instructions below to determine if your system's processor and EFI firmware is
capable of running |CL|. Otherwise, 
:ref:`run Clear Linux as a Live image <live-image>` and then perform the steps
below.

.. note::
   This does not check other system components (for example: storage and
   graphics) for compatibility with |CL|.

#. Download the `clear-linux-check-config.sh`_ file.

   If a browser is not available, use:

   .. code-block:: console

      $ curl -O https://download.clearlinux.org/current/clear-linux-check-config.sh

#. Make the script executable.

   .. code-block:: console

      $ chmod +x clear-linux-check-config.sh

#. Run the script.

   #. Check to see if the host's processor and EFI firmware is capable of
      running |CL|.

      .. code-block:: console

         $ ./clear-linux-check-config.sh host

   #. Check to see if the host is capable of running |CL| in a container.

      .. code-block:: console

         $ ./clear-linux-check-config.sh container

   The script will print a list of test results similar to the output below.
   All items should return a `SUCCESS` status. This example indicates the
   host's processor and EFI firmware support running |CL|.

   .. code-block:: console

      Checking if host is capable of running Clear Liunx* OS for Intel® Architecture

      SUCCESS: Intel CPU

      SUCCESS: 64-bit CPU (lm)

      SUCCESS: Streaming SIMD Extension v4.1 (sse4_1)

      SUCCESS: EFI Firmware

.. _clear-linux-check-config.sh: https://download.clearlinux.org/current/clear-linux-check-config.sh
