.. _enable-huge-pages:

Configure Huge Pages
########################

In |CL| hugepages are enabled by default. The default hugepage size is 2MB. 
The total number of hugepages is set to 0 by default. This guide shows you how
to add hugepages to the system and how to change the default hugepage size. 

#. To check the enabled state, run the following command.

   .. code-block:: bash
   
      cat /sys/kernel/mm/transparent_hugepage/enabled

   The output will look like
 
   .. code-block:: console

      [always] madvise never

   .. note::
      
      The active option is enclosed in brackets. In this case, always is active, 
      which means hugepages are enabled for every process. The `madvise` 
      option means that hugepages are enabled for processes that explicitly 
      call `madvise`_. 

#. To check the size of hugepages, run the below command.

   .. code-block:: bash

      cat /proc/meminfo | grep Huge

   The output should look similar to the following. Although hugepages is 
   enabled, there are no hugepages available to allocate.

   .. code-block:: console

      AnonHugePages:    624640 kB
      ShmemHugePages:        0 kB
      FileHugePages:         0 kB
      HugePages_Total:       0
      HugePages_Free:        0
      HugePages_Rsvd:        0
      HugePages_Surp:        0
      Hugepagesize:       2048 kB
      Hugetlb:               0 kB

#. If you need 1GB (1,048,576 bytes) of hugepages enabled, then `HugePages_Total`
   should be set to 512. Enable it temporarily using the following.

   .. code-block:: bash

      echo 512 | sudo tee /sys/kernel/mm/hugepages/hugepages-2048kB/nr_hugepages

   To view the change, run the command in the previous setp again.

#. Changing hugepages from the default 2MB to 1GB must be done at system boot
   through kernel boot parameters. In this example, we configure the size and 
   number of allocatable huge pages at boot.

   .. code-block:: bash
    
      sudo mkdir -p /etc/kernel/cmdline.d
      cat << EOF | sudo tee -a /etc/kernel/cmdline.d/hugepages.conf
      default_hugepagesz=1G
      hugepagesz=1G
      hugepages=10
      EOF
      sudo clr-boot-manager update
      sudo reboot

   .. _madvise: https://linux.die.net/man/2/madvise
