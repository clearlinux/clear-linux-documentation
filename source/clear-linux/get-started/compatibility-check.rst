.. _compatibility-check:

Check processor and EFI firmware compatibility with Clear Linux OS for Intel® Architecture
======================================================================

On a system that is currently running a Linux operating system, follow the instructions below to determine if your target system is capable of running |CL|.  Otherwise, run |CL| as a `live image`_ and perform the steps below.  

#. Download the `clear-linux-check-config.sh file`_ script.

   If a browser is not available, use:

   .. code-block:: console

      $ curl -O https://download.clearlinux.org/current/clear-linux-check-config.sh

#. Make the script executable.

   .. code-block:: console

      $ chmod +x clear-linux-check-config.sh
      
#. Run the script.

   #. Check to see if the host's processor and EFI firmware is capable of running |CL|.

      .. code-block:: console

         $ ./clear-linux-check-config.sh host

   #. Check to see if the host is capable of running |CL| in a container.

      .. code-block:: console

         $ ./clear-linux-check-config.sh container

   The script will print a list of test results similar to the output below.  
   All items should return a *SUCCESS* status.  This example indicates the host's prcessor and EFI firmware supports running |CL|.

   .. code-block:: console

      Checking if host is capable of running |CL|\* OS for Intel®
      Architecture

      SUCCESS: Intel CPU

      SUCCESS: 64-bit CPU (lm)

      SUCCESS: Streaming SIMD Extension v4.1 (sse4_1)

      SUCCESS: EFI Firmware

   * Run a :ref:`live-image` from a USB drive (success does not guarantee your
     system is 100% compatible).
     
 .. _clear-linux-check-config.sh file: https://download.clearlinux.org/current/clear-linux-check-config.sh
 .. _live image: https://clearlinux.org/documentation/clear-linux/get-started/live-image.html    
