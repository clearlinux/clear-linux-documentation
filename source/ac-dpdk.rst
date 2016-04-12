.. _ac-dpdk:

DPDK
####

Introduction
============

This document describes *how to* run a basic use case that involves **l3fwd
DPDK example**, the objective is to *send packages between 2 platforms* using a
traffic generator called :ref:`pktgen <sec_pktgen>` where l3fwd example
application will forward those packages (:ref:`f1`).

.. _f1:

.. figure:: _static/images/pktgen_lw3fd.png
   :align: center
   :alt: platform A and B

   Figure 1: environment for l3fwd DPDK application.


**Requirements:**

* 2 platform using Clear Linux (recommended release 7160 or higher).
* both Clear Linux images have to use **kernel-native boundle**
* Install "dpdk-dev", "os-core-dev" and "sysadmin-basic" bundles

  .. code-block:: bash

      # swupd bundle-add dpdk-dev os-core-dev sysadmin-basic

* The Platforms must have 2 NICs at least each one, check Network cards compatibility, it's very important to verify if your NIC is compatible with DPDK project, you can check it in this site http://dpdk.org/doc/nics.
* 2 Network cables.


1. Disable iommu on Clear Linux (platform A and B). 
===================================================

1. mount the :abbr:`ESP (EFI system partition)`

   .. code-block:: bash

       # systemctl start boot.mount

2. move to entries directory 

   .. code-block:: bash

      # cd /boot/loader/entries/

 edit **Clear-linux-native-.conf** and add **intel_iommu=off** in the end of the last line. 

3. Umount *ESP* and reboot

   .. code-block:: bash

      # cd /
      # systemctl stop boot.mount
      # reboot


2. Installing dpdk bundle on Clear Linux and build l3fwd example (platform B).
==============================================================================

1. Install dpdk bundle you can use the following command: 

 .. code-block:: bash

    # swupd bundle-add dpdk-dev

2. Move to l3fwd example 

 .. code-block:: bash

	# cd /usr/share/dpdk/examples/l3fwd

3. Assign RTE_SDK var the path where makefiles are

 .. code-block:: bash

    # export RTE_SDK=/usr/share/dpdk/

4. Assign RTE_TARGET var the value where config file is

 .. code-block:: bash

    # export RTE_TARGET=x86_64-native-linuxapp-gcc

5. Build the l3fwd application and add the configuration header to CFLAGS var

 .. code-block:: bash

    # make CFLAGS+="-include /usr/include/rte_config.h"



.. _sec_pktgen:

3. Building pktgen (platform A).
================================

Currently **pktgen project** is not included in Clear Linux, for that reason
it is necessary to download it from upstream and build it:

1. Install dpdk bundle

 .. code-block:: bash

    # swupd bundle-add dpdk-dev

2. Download pktgen tar package 2.9.12 version from this site: http://dpdk.org/browse/apps/pktgen-dpdk/refs/

3. Decompress packages and move to uncompressed source directory. 

4. Assign RTE_SDK var the path where makefiles are

 .. code-block:: bash 

    # export RTE_SDK=/usr/share/dpdk/

5. Assign RTE_TARGET var the value where config file is

 .. code-block:: bash

    # export RTE_TARGET=x86_64-native-linuxapp-gcc

6. Build Pktgen project setting CONFIG_RTE_BUILD_SHARED_LIB variable with "n"
 
 .. code-block:: bash

    # make CONFIG_RTE_BUILD_SHARED_LIB=n


4. Binding NIC's to dpdk kernel drivers (platform A and B). 
=============================================================

l3fwd application will use 2 NIC's, DPDK has useful tools in order for binding NICs to DPDK modules in order to run DPDK applications.

1. Load dpdk I/O kernel module

 .. code-block:: bash 

    # modprobe igb_uio

2. Check your status of your NIC's, this in order to know which network cards are not busy, in case that another application is using them, the status will be “Active” and those NICs could not be bound.

 .. code-block:: bash

    # dpdk_nic_bind.py --status

3. Binding 2 available NICs using the syntax: **dpdk_nic_bind.py --bind=igb_uio <device-entry>** , example:

 .. code-block:: bash

	# dpdk_nic_bind.py --bind=igb_uio 01:00.0

4. Be sure that your NIC's was binding correctly checking the status (point 2), drv should has igb_uio value, at this point the NIC's are using the DPDK modules. 


5. Setting hugepages (platform A and B).
==========================================

Clear Linux supports hugepages for the large memory pool allocation used for packet buffers.

1. Set number of hugepages.

 .. code-block:: bash 

    # echo 1024 > /sys/kernel/mm/hugepages/hugepages-2048kB/nr_hugepages

2. Allocate pages on NUMA machines.

 .. code-block:: bash
	
    # echo 1024 > /sys/devices/system/node/node0/hugepages/hugepages-2048kB/nr_hugepages
    # echo 1024 > /sys/devices/system/node/node1/hugepages/hugepages-2048kB/nr_hugepages

3. Making memory available for DPDK.

 .. code-block:: bash

    # mkdir -p /mnt/huge $ mount -t hugetlbfs nodev /mnt/huge

 If you would like to know more about this, you can check this site: http://dpdk.org/doc/guides/linux_gsg/sys_reqs.html


6. Setting a physical environment (platform A and B).
=====================================================

In order to achieve the model proposed in the introduction of this document
(:ref:`f1`), we need to connect the first grantley’s NICs  to the second
grantley’s NICs using the network cables (:ref:`f2`).

.. _f2:

.. figure:: _static/images/pyshical_net.png

    Figure 2: Physical network environment.


7. Running l3fwd application (platform B).
==========================================

l3fwd application is one of the DPDK examples available when you install dpdk-dev bundle, this application is going to forward packages for one NIC to another.

1. Move to l3fwd example

 .. code-block:: bash 

    # cd  /usr/share/dpdk/examples/l3fwd

2. The next step is very important, DPDK needs poll drivers for working, these poll drivers are shared objects and they are in /usr/lib64, dpdk just support some NICs, you can see which in the next link: <http://dpdk.org/doc/nics>, you need to know which kernel module the NIC is using and choose poll driver according to your NICs.

3. At this point the system must have hugepages requirements and the NICs bound and the configuration for running pktgen depends to the network use case and the available system resources, use “-d” flag for setting the pull driver, example, the NICs’ are using e1000 network driver, this means that they are going to use e1000 poll driver (librte_pmd_e1000.so), it should be in /usr/lib64 in clear linux and it should be enough to add the name, e.g

 .. code-block:: bash

    # ./build/l3fwd -c 0x3 -n 2 -d librte_pmd_e1000.so -- -p 0x3 --config="(0,0,0),(1,0,1)"

4. When the application start to run, it will show a lot information about the steps that l3fwd is doing, pay attention when the application in the step when it is Initializing ports, after port 0 initialization it will show a mac address and the same for port 1, save this information in order to set configuration to Pktgen project.


8. Running pktgen application (platform A).
===========================================

Pktgen is network traffic generator, it will be used to measure the network packaging performance in a forwarding use case.

1. At this point the system must have hugepages requirements and the NICs bound, and the configuration for running pktgen depends to the network use case and the available system resources, this is just a basic configuration.

 .. code-block:: bash

    # ./app/app/x86_64-native-linuxapp-gcc/pktgen -c 0xf -n 4 -- -p 0xf -P -m "1.0, 2.1"

2. Active colorful output (this step is optional). 

 .. code-block:: bash

    Pktgen> theme enable

3. l3fwd application showed a mac address per port initialized, this mac addresses must have set in pktgen environment (Pktgen prompt): set mac <port number> <mac address> example:

 .. code-block:: bash

    Pktgen> set mac 0 00:1E:67:CB:E8:C9
    Pktgen> set mac 1 00:1E:67:CB:E8:C9

4. Start to send packages using the next command:

 .. code-block:: bash

    Pktgen> start 0-1

5. If you have done the steps of this document correctly, you should see that pktgen is sending and receiving packages.

For more information about Pktgen: https://media.readthedocs.org/pdf/pktgen/latest/pktgen.pdf


Annex A: Using pass-through for running on virtual machines.
============================================================

This section will explain how to do in order to work in a virtual environment where virtual machines will take the control of host's NIC's.

1. Create a new directory and move to it.

2. Download "start_qemu.sh" script in order to run a kvm virtual machine:

 .. code-block:: bash

    $ curl -O https://download.clearlinux.org/image/start_qemu.sh

3. Download a bare-metal Clear Linux image and rename it as "clear.img".

4. Look for entry for device and vendor & device ID:

 .. code-block:: bash
	
    $ lspci -nn | grep Ethernet

 This is an output example from last step: **03:00.0 Ethernet controller [0200]: Intel Corporation I350 Gigabit Network Connection [8086:1521]**
 where 8086:1521 is vendor:device ID and 03:00.0 is the entry for device this information is necessary for unbinding host's NICs.
    
5. Unbind NICs from host, this in order to do passthrough with virtual machines, currently Clear Linux support this action, you can use the following commands:

 * echo "vendor device_ID" > /sys/bus/pci/drivers/pci-stub/new_id
 * echo "entry for device" > /sys/bus/pci/drivers/igb/unbind
 * echo "entry for device" > /sys/bus/pci/drivers/pci-stub/bind
 * echo "vendor device_ID" > /sys/bus/pci/drivers/pci-stub/remove_id

 e.g

 .. code-block:: bash

    $ echo "8086 1521" > /sys/bus/pci/drivers/pci-stub/new_id
    $ echo "0000:03:00.0" > /sys/bus/pci/drivers/igb/unbind
    $ echo "0000:03:00.0" > /sys/bus/pci/drivers/pci-stub/bind
    $ echo "8086 1521" > /sys/bus/pci/drivers/pci-stub/remove_id

6. Assign to kvm virtual machine (guest) the unbound NICs previously. Modify the "start_qemu.sh" script in qemu-system-x86_64 arguments, and  add the lines with the host's NICs information.

 **-device pci-assign,host="<entry for device>",id=passnic0,addr=03.0**
 **-device pci-assign,host="<entry for device>",id=passnic1,addr=04.0**

 e.g
 
 .. code-block:: bash

    -device pci-assign,host=03:00.0,id=passnic0,addr=03.0 \
    -device pci-assign,host=03:00.3,id=passnic1,addr=04.0 \

5. Assign to kvm virtual machine (guest) the unbound NICs previously. Modify the "start_qemu.sh" script in qemu-system-x86_64 arguments, and  add the lines with the host's NICs information.

 **-device pci-assign,host="<entry for device>",id=passnic0,addr=03.0**
 **-device pci-assign,host="<entry for device>",id=passnic1,addr=04.0**

 e.g

 .. code-block:: bash
 
    -device pci-assign,host=03:00.0,id=passnic0,addr=03.0 \
    -device pci-assign,host=03:00.3,id=passnic1,addr=04.0 \


6. If you would like to add more NUMA machines to the virtual machine, you can add the next line in Makefile boot target:

 **-numa node,mem=<memory>,cpus=<number of cpus>**

 e.g.

 you have a virtual machine with 4096 of memory and 4 cpus the configuration should be next:

 .. code-block:: bash
 
    -numa node,mem=2048,cpus=0-1 \
    -numa node,mem=2048,cpus=2-3 \

 this means that each NUMA machine have to use the same quantity of memory.

7. Run "start_qemu.sh" script.





