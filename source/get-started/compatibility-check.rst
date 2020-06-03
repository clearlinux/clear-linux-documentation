.. _compatibility-check:

Check Processor Compatibility
#############################

Before installing |CL-ATTR|, check your host system's processor compatibility using one of 
the following options:

.. note::
   This does not check other system components (for example: storage and
   graphics) for compatibility with |CL|.

Option 1: Use the :command:`clear-linux-check-config.sh` script on an existing Linux system
*******************************************************************************************

#. Download the `clear-linux-check-config.sh`_ file.

   If a browser is not available, use:

   .. code-block:: bash

      curl -O https://cdn.download.clearlinux.org/current/clear-linux-check-config.sh

#. Make the script executable.

   .. code-block:: bash

      chmod +x clear-linux-check-config.sh

#. Run the script.

   #. Check to see if the host's processor is capable of running |CL|.

      .. code-block:: bash

         ./clear-linux-check-config.sh host

   #. Check to see if the host is capable of running |CL| in a container.

      .. code-block:: bash

         ./clear-linux-check-config.sh container

   The script prints a list of test results similar to the output below.
   All items should return a `SUCCESS` status. This example indicates the
   host's processor supports running |CL|.

   .. code-block:: console

      Checking if host is capable of running Clear Linux* OS

      SUCCESS: 64-bit CPU (lm)
      SUCCESS: Supplemental Streaming SIMD Extensions 3 (ssse3)
      SUCCESS: Streaming SIMD Extension v4.1 (sse4_1)
      SUCCESS: Streaming SIMD Extensions v4.2 (sse4_2)
      SUCCESS: Carry-less Multiplication extensions (pclmulqdq)

Option 2: Use a |CL| live image on a non-Linux system
=====================================================

#. `Download`_ either the `Desktop` or `Server` version of the live image ISO.

#. Follow the instruction to :ref:`bootable-usb`.

#. Boot up the |CL| live image on the USB.

#. Check compatibility as follows:

   * *Desktop version:*
     
     a. Open a terminal.

     #. Check compatibility.

        .. code-block:: bash

	   sudo clr-installer --system-check

   * *Server version:*

     a. Log in as `root` and set a password.

     #. Check compatibility.

        .. code-block:: bash

	   clr-installer --system-check

   Expected output for a compatible host processor:

   .. code-block:: console

      Checking for required CPU feature: lm [success]
      Checking for required CPU feature: sse4_2 [success]
      Checking for required CPU feature: sse4_1 [success]
      Checking for required CPU feature: pclmulqdq [success]
      Checking for required CPU feature: ssse3 [success]
      Success: System is compatible

.. _clear-linux-check-config.sh: 
   https://cdn.download.clearlinux.org/current/clear-linux-check-config.sh

.. _Download:
   https://clearlinux.org/downloads   
