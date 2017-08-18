.. _compatibility-check:

Check system compatibility with Clear Linux OS for Intel® Architecture
######################################################################

If you’re unsure whether your system will be capable of running
|CL|\* OS for Intel® Architecture, you can determine ahead of time by
downloading and running the simple clear-linux-check-config.sh script locally
on your target system if it is already running a Linux distribution.

This script is available in the current download directory at clearlinux.org
and checks the hardware capabilities of your system to determine whether it
will work with the latest release of |CL|. To run the clear-linux-
check- config.sh script, enter the following commands on your target system:

.. code-block:: console

   curl -O https://download.clearlinux.org/current/clear-linux-check-config.sh
   chmod +x clear-linux-check-config.sh
   ./clear-linux-check-config.sh host

The script will print a list of test results similar to the output below. All
items should return a 'SUCCESS' status and if it does, your target system
fully supports installing and running |CL|.

.. code-block:: console

   Checking if host is capable of running |CL|\* OS for Intel®
   Architecture

   SUCCESS:  Intel CPU

   SUCCESS: 64-bit CPU (lm)

   SUCCESS:  Streaming SIMD Extension v4.1 (sse4_1)

   SUCCESS: EFI Firmware