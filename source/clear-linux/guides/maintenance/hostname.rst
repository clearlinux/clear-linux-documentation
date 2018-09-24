.. _hostname:

Modify hostname on |CL-ATTR|
############################

This guide describes how to modify and view the hostname of your 
|CL-ATTR| system.


By default, |CL| installations have a machine generated name. This 
long string of letters and numbers is fine for computers, but is not 
human-friendly. Administrators and users will often want to rename 
their machines with a name that is easier to remember, type, and search 
for. Renaming a machine also makes it easier to identify, by including 
meaningful data in the name. A meaningful, human-friendly machine 
name might:

   * indicate the computer purpose e.g. “regression-test.”
   * indicate the owner e.g. “sally-test-box1.”
   * indicate the geographical location e.g. “az-bld2-lab.”


.. note::

   There are three types of hostname: “static”, “transient”, and “pretty.” 
   The most common is the static hostname. If the static hostname exists, 
   it is used to generate the transient hostname, which is maintained by 
   the kernel. The transient hostname can be changed by DHCP or mDNS at 
   runtime. The pretty hostname is a human readable name that is used for 
   presentation to the user.

   Static hostnames must be between two and 63 characters long, must start 
   and end with a letter or number, and may contain letters (case-insensitive), 
   numbers, dashes, or dots.  Pretty hostnames can use free-form UTF8 characters
   to make the hostname more aesthetically pleasing for the user.  


Setting your hostname
*********************

|CL| uses the :command:`hostnamectl` command to display and modify the 
machine name. :command:`hostnamectl` is part of the **os-core** bundle. 

This example sets the hostname to “telemetry-test-2-h15,” to identify a 
|CL| telemetry test machine on the second floor at grid location H15. 
Make sure to reboot after setting a new hostname.

   .. code-block:: bash

      sudo hostnamectl set-hostname telemetry-test-2-h15
      sudo reboot


View your hostname
******************

View your current hostname using the following command:

   .. code-block:: bash

      hostnamectl

You should see output similar to:

   .. code-block:: console

       Static hostname: telemetry-test-2-h15
       Pretty hostname: telemetry-test-2-h15
             Icon name: computer-desktop
               Chassis: desktop
            Machine ID: 4d0d60207a904ebbab96680a51ac1339
               Boot ID: 98d3514e5a984e8cbbdf46a2f0d6b397
      Operating System: Clear Linux OS
                Kernel: Linux 4.18.8-632.native
          Architecture: x86-64

 
**Congratulations!** You successfully modified the hostname of your |CL| system.
