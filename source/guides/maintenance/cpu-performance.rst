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
and technologies to balance performance, energy, and thermal efficiencies.

By default, |CL| prioritizes maximum CPU performance with the philosophy that
the faster the program finishes execution, the faster the CPU can return to a
low energy idle state. It is important to understand and evaluate all of these
technologies when troubleshooting or considering changing the defaults.

.. contents::
   :local:
   :depth: 1

CPU power saving mechanisms
***************************

C-states and P-states are both CPU power saving mechanisms that are entered
under different operating conditions. The tradeoff is a slightly longer time
to exit these states when the CPU is needed once again.

.. _c-states-section:

C-states (idle states)
======================

C-states are hardware sleep states that are entered when it is determined that
the CPU is idle and not executing instructions.

C-states aim to reduce power utilization by increasingly reducing clock
frequency, voltages, and features in each state.

Although C-states can typically be limited or disabled in a system's UEFI or
BIOS configuration, these settings are overridden when the `intel_idle driver`_
is in use.

To view the current cpuidle driver run this command in a terminal:

.. code:: bash

   cat /sys/devices/system/cpu/cpuidle/current_driver

For troubleshooting, C-states can be limited with a kernel command line boot
parameter by adding :command:`processor.max_cstate=N intel_idle.max_cstate=N`
or completely disabled with :command:`idle=poll`.

.. note::

   * :command:`processor.max_cstate=0` is changed to :command:`processor.max_cstate=1`
     by the kernel to be a valid value.

   * :command:`intel_idle.max_cstate=0` disables the Intel Idle driver, not set
     it to C-state 0.

.. _p-states-section:

P-states (performance states)
=============================

P-states, also known as *Intel SpeedStep® technology* on Intel processors or
*Cool'n'Quiet* on AMD processors, are states entered while the CPU is active and
executing instructions.

P-states aim to reduce power utilization by adjusting CPU clock frequency and
voltages based on CPU demand.

P-states can typically be limited or disabled in a system's firmware (UEFI/BIOS).

Turbo boost
-----------

`Intel® Turbo Boost Technology`_, found on some modern Intel CPUs, allows core(s) on
a processor to temporarily operate at a higher than rated CPU clock frequency
to accommodate demanding workloads if the CPU is under defined power and
thermal thresholds.

Turbo boost is an extension of P-states. As such, changing or limiting
C-states or P-states impact the ability of a process to enter Turbo boost.

Turbo boost can be disabled in a system's UEFI or BIOS. Turbo boost can also
be disabled within |CL| with the command:

.. code:: bash

   echo 1 | sudo tee /sys/devices/system/cpu/intel_pstate/no_turbo

Linux CPU clock frequency scaling
*********************************

The CPUFreq subsystem in Linux allows the OS to control :ref:`C-states
<c-states-section>` and :ref:`P-states <P-states-section>`
via CPU drivers and governors that provide algorithms that define how and when
to enter these states.

Scaling driver
==============

Linux uses the `Intel P-state driver`_, :command:`intel_pstate`, for modern Intel
processors from the Sandy Bridge generation or newer. Other processors may
default to the :command:`acpi-cpufreq*` driver which reads values from the systems
UEFI or BIOS.

To view the current CPU frequency scaling driver run this command in a terminal:

.. code:: bash

   cat /sys/devices/system/cpu/cpu*/cpufreq/scaling_driver

Scaling governor
================

|CL| sets the CPU governor to *performance* which calls for the CPU to operate
at maximum clock frequency. In other words, P-state P0. While this may sound
wasteful at first, it is important to remember that power utilization does not
increase significantly simply because of a locked clock frequency without a
workload.

To view the current CPU frequency scaling governor run this command in a terminal:

.. code:: bash

   cat /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor

To change the CPU frequency scaling governor:

#. Disable |CL| enforcement of certain power and performance settings:

   .. code:: bash

      sudo systemctl mask clr-power.timer

#. Change the governor. In the example below, the governor is set to
   *performance*:

   .. code:: bash

      echo performance | sudo tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor

The list of all governors can be found in the Linux kernel documentation on
`CPUFreq Governors`_.

.. note::

   The intel_pstate driver only supports *performance* and *powersave* governors.

Thermal management
******************

`thermald`_ is a Linux thermal management daemon used to prevent the
overheating of platforms. When temperature thresholds are exceeded, thermald
forces a C-state by inserting CPU sleep cycles and adjusts available cooling
methods. This can be especially desirable for laptops.

By default, thermald is disabled in |CL| and starts automatically if battery
power is detected. thermald can be manually enabled using the systemd service
by running the command:

.. code:: bash

   sudo systemctl enable --now thermald

For more information, see the thermald man page:

.. code:: bash

   man thermald

`ThermalMonitor`_ is a GUI application that can visually graph and log
temperatures from thermald. To use ThermalMonitor, add the
:command:`desktop-apps-extras` bundle and add your user account to the power
group:

.. code:: bash

   sudo swupd bundle-add desktop-apps-extras
   sudo usermod -a -G power <USER>
   ThermalMonitor

.. note::

   After adding a new group, you must log out and log back in for the new group
   to take effect.


.. _`Intel P-state driver`: https://www.kernel.org/doc/Documentation/cpu-freq/intel-pstate.txt

.. _`CPUFreq Governors`: https://www.kernel.org/doc/Documentation/cpu-freq/governors.txt

.. _thermald: https://01.org/linux-thermal-daemon

.. _`intel_idle driver`: https://github.com/torvalds/linux/blob/master/drivers/idle/intel_idle.c

.. _`ThermalMonitor`: https://github.com/intel/thermal_daemon/tree/master/tools/thermal_monitor

.. _`Intel® Turbo Boost Technology`: https://www.intel.com/content/www/us/en/architecture-and-technology/turbo-boost/turbo-boost-technology.html
