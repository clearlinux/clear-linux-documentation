.. _cpu-performance:

CPU Power and Performance
#########################

This guide explains the CPU power and performance mechanisms in |CL-ATTR|.

.. contents::
   :local:
   :depth: 1

Overview
********

Modern x86 :abbr:`CPUs (central processing units)` employ a number of features
to balance performance, energy, and thermal efficiency.

By default, |CL| prioritizes maximum CPU performance, assuming that
the faster the program finishes execution, the faster the CPU can return to a
low energy idle state. It is important to understand and evaluate the impact
of each feature when troubleshooting or considering changing the defaults.

.. contents::
   :local:
   :depth: 1

CPU power saving mechanisms
***************************

C-states and P-states are both CPU power saving mechanisms that are entered
under different operating conditions. The tradeoff is a slightly longer time
to exit these states when the CPU is needed.

.. _c-states-section:

C-states (idle states)
======================

Hardware enters a C-state when the CPU is idle and not executing instructions.
C-states decrease power utilization by reducing clock frequency,
voltages, and features in each state. Although C-states can typically be
limited or disabled in a system's UEFI or BIOS configuration, these settings
are overridden when the `intel_idle driver`_ is in use.

To view the current ``cpuidle`` driver run this command in a terminal:

.. code-block:: bash

   cat /sys/devices/system/cpu/cpuidle/current_driver

For troubleshooting, C-states can be limited with a kernel command line boot
parameter by adding :command:`processor.max_cstate=N intel_idle.max_cstate=N`
or completely disabled with :command:`idle=poll`.

.. note::

   *  :command:`processor.max_cstate=0` is changed to a valid value by the
      kernel: :command:`processor.max_cstate=1`.

   *  :command:`intel_idle.max_cstate=0` disables the Intel Idle driver rather
      than set it to C-state 0.

.. _p-states-section:

P-states (performance states)
=============================

The CPU can enter a P-state, also known as Intel SpeedStep® technology on
Intel processors or AMD\* Cool'n'Quiet\* technology, while it is active
and executing instructions. P-states reduce power utilization by adjusting CPU
clock frequency and voltages based on CPU demand. P-states can typically be
limited or disabled in a system's firmware (UEFI/BIOS).

Turbo boost
-----------

`Intel® Turbo Boost Technology`_, found on some modern Intel CPUs, allows
cores on a processor to temporarily operate at a higher than rated CPU clock
frequency to accommodate demanding workloads if the CPU is under defined power
and thermal thresholds. Intel Turbo Boost Technology is an extension of
P-states, so it can be impacted by limiting C-states or P-states.

Intel Turbo Boost Technology can be disabled in a system's UEFI/BIOS or in
|CL|:

.. code-block:: bash

   echo 1 | sudo tee /sys/devices/system/cpu/intel_pstate/no_turbo

Linux CPU clock frequency scaling
*********************************

The ``CPUFreq`` subsystem in Linux allows the OS to control
:ref:`C-states <c-states-section>` and :ref:`P-states <P-states-section>`
via CPU drivers and governors that provide algorithms that define how and when
to enter these states.

Scaling driver
==============

Linux uses the `Intel P-state driver`_, :command:`intel_pstate`, for
modern Intel processors from the Sandy Bridge generation or newer. Other
processors may default to the :command:`acpi-cpufreq` driver which reads
values from the systems UEFI or BIOS.

To view the current CPU frequency scaling driver, run this command in a
terminal:

.. code-block:: bash

   cat /sys/devices/system/cpu/cpu*/cpufreq/scaling_driver

Scaling governor
================

|CL| sets the CPU governor to ``performance`` which calls for the CPU to
operate at maximum clock frequency. In other words, P-state P0. While this may
sound wasteful at first, it is important to remember that power utilization
does not increase significantly simply because of a locked clock frequency
without a workload.

To view the current CPU frequency scaling governor, run this command in a
terminal:

.. code-block:: bash

   cat /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor

Each core will report its own status. Your output should look similar to this
example with four cores:

.. code-block:: console

   performance
   performance
   performance
   performance

The list of all governors can be found in the Linux kernel documentation on
`CPUFreq Governors`_.

.. note::

   The intel_pstate driver only supports *performance* and *powersave* governors.

There are 2 ways to change the CPU frequency scaling governor:

#. Disable |CL| enforcement of certain power and performance settings:

   .. code-block:: bash

      sudo systemctl mask clr-power.timer

#. Change the governor value in :file:`/sys/devices`. In the example below,
   the governor is set to *performance*:

   .. code-block:: bash

      echo performance | sudo tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor

Thermal management
******************

`thermald`_ is a Linux thermal management daemon used to prevent platforms 
from overheating. :command:`thermald` forces a C-state by inserting CPU sleep
cycles and adjusting any available cooling methods. This can be especially
desirable for laptops.

:command:`thermald` is disabled by default in |CL| and starts automatically
if it detects battery power. Enable :command:`thermald` manually by using
the systemd service by running the command:

.. code-block:: bash

   sudo systemctl enable --now thermald

For more information, see the :command:`thermald` man page:

.. code-block:: bash

   man thermald

`ThermalMonitor`_ is a GUI application that can visually graph and log
temperatures from :command:`thermald`. To use ThermalMonitor, add the
:command:`desktop-apps-extras` bundle and add your user account to the power
group:

.. code-block:: bash

   sudo swupd bundle-add desktop-apps-extras
   sudo usermod -a -G power <USER>
   ThermalMonitor

.. note::

   After adding a new group, you must log out and log back in for the new group
   to take effect.

Enhanced thermal configuration
===============================

Better thermal control and performance can be achieved by providing platform
specific configuration to :command:`thermald`.

`Linux DPTF Extract Utility`_ is a companion tool to :command:`thermald`,
This tool uses Intel® Dynamic Platform and Thermal Framework (Intel® DPTF)
technology and can convert to the :file:`thermal_conf.xml` configuration format
used by :command:`thermald`. Closed-source projects, like this one, cannot be
packaged as a bundle in |CL|, so you must install it manually:

#. Make sure your machine's BIOS has DPTF feature and is enabled. It will usually be in the :guilabel:`Advanced` or :guilabel:`Advanced>Power` section of the BIOS. 

   .. figure:: /_figures/cpu-perf-guide/dptf_bios.png

   .. note:: 

      Intel DPTF requires BIOS support and is typically only available on
      laptops.

#. Generate thermal configuration. :command:`thermald` configuration files
   will be generated and saved to :file:`/etc/thermal/` folder. 

   .. code-block:: bash

      sudo swupd bundle-add acpica-unix2  # install acpi tools
      git clone https://github.com/intel/dptfxtract.git
      cd dptfxtract
      sudo acpidump > acpi.out
      acpixtract -a acpi.out
      sudo ./dptfxtract *.dat

#. Restart :command:`thermald` service to take effect.

   .. code-block:: bash

      sudo systemctl restart thermald.service

#. Check whether the configuration is in use.

   .. code-block:: bash

      sudo systemctl status thermald.service

The following output means the configuration has already been applied:

.. code-block:: console

   thermald[*]: [WARN]Using generated /etc/thermald/thermal-conf.xml.auto

*Intel® Turbo Boost Technology requires a PC with a processor with Intel Turbo
Boost Technology capability. Intel Turbo Boost Technology performance varies
depending on hardware, software and overall system configuration. Check with
your PC manufacturer on whether your system delivers Intel Turbo Boost Technology.
For more information, see http://www.intel.com/technology/turboboost*

*Intel, Intel SpeedStep, and the Intel logo are trademarks of Intel Corporation or its subsidiaries.*


.. _`Intel P-state driver`: https://www.kernel.org/doc/Documentation/cpu-freq/intel-pstate.txt

.. _`CPUFreq Governors`: https://www.kernel.org/doc/Documentation/cpu-freq/governors.txt

.. _thermald: https://01.org/linux-thermal-daemon

.. _`intel_idle driver`: https://github.com/torvalds/linux/blob/master/drivers/idle/intel_idle.c

.. _`ThermalMonitor`: https://github.com/intel/thermal_daemon/tree/master/tools/thermal_monitor

.. _`Intel® Turbo Boost Technology`: https://www.intel.com/content/www/us/en/architecture-and-technology/turbo-boost/turbo-boost-technology.html

.. _`Linux DPTF Extract Utility`: https://github.com/intel/dptfxtract

.. _`Intel DPTF`: https://software.intel.com/en-us/articles/2-in-1-tablet-mode-game-performance-with-intel-dynamic-platform-and-thermal-framework-intel
