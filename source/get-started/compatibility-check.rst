.. _compatibility-check:

Check processor and EFI firmware compatibility
##############################################

Before installing |CL-ATTR|, check your host system's processor and EFI firmware
compatibility. To check compatibilty, choose one of the following paths:

* From a system with a Linux\* OS installed, follow the instructions to :ref:`check-compatibility-steps`.

* From a non-Linux OS, first :ref:`bare-metal-install-desktop` and then follow
  the instructions to :ref:`check-compatibility-steps`.

.. note::
   This does not check other system components (for example: storage and
   graphics) for compatibility with |CL|.

.. _check-compatibility-steps:

Check compatibility
*******************

#. Download the `clear-linux-check-config.sh`_ file.

   If a browser is not available, use:

   .. code-block:: console

      curl -O https://cdn.download.clearlinux.org/current/clear-linux-check-config.sh

#. Make the script executable.

   .. code-block:: console

      chmod +x clear-linux-check-config.sh

#. Run the script.

   #. Check to see if the host's processor and EFI firmware is capable of
      running |CL|.

      .. code-block:: console

         ./clear-linux-check-config.sh host

   #. Check to see if the host is capable of running |CL| in a container.

      .. code-block:: console

         ./clear-linux-check-config.sh container

   The script prints a list of test results similar to the output below.
   All items should return a `SUCCESS` status. This example indicates the
   host's processor and EFI firmware support running |CL|.

   .. code-block:: console

      Checking if host is capable of running Clear Linux* OS

      SUCCESS: 64-bit CPU (lm)
      SUCCESS: Supplemental Streaming SIMD Extensions 3 (ssse3)
      SUCCESS: Streaming SIMD Extension v4.1 (sse4_1)
      SUCCESS: Streaming SIMD Extensions v4.2 (sse4_2)
      SUCCESS: Advanced Encryption Standard instruction set (aes)
      SUCCESS: Carry-less Multiplication extensions (pclmulqdq)
      SUCCESS: EFI Firmware

.. _clear-linux-check-config.sh: https://cdn.download.clearlinux.org/current/clear-linux-check-config.sh
