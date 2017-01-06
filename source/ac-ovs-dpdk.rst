.. _ac-ovs-dpdk:

OpenvSwitch and DPDK
####################

Introduction
============

Enabling `DPDK`_ support on the **OpenvSwitch project** can yield significant
network performance improvements. To illustrate one such example, we'll 
cover a simple use case with :ref:`f1ovs`, where one virtual machine sends
1,000,000 HTTP requests to another virtual machine using 
* *Linux bridges**
* **OpenvSwitch bridges**
* And custom-built **OpenvSwitch-DPDK bridges** as the network link.

.. _f1ovs:

.. figure:: _static/images/use_case.png

   Figure 1: Basic virtual network environment.

**Requirements:**

To follow along with this example, you will need:

* At least one platform using Clear Linux* OS for Intel® Architecture 
  (recommended release >= ``7160``) as Host,
* The ``kernel-native`` bundle enabled on that particular Host, 
* And the ``network-advanced``, and ``os-clr-on-clr`` bundles installed.

 .. code-block:: bash
	
		# swupd bundle-add network-advanced os-clr-on-clr

You'll also need two `kvm`_ images (recommended release  >= ``7160``).
These images will create the guest virtual machines A and B. These virtual machines
must also have ``network-basic`` and ``lamp-basic`` bundles installed.
 
 .. code-block:: bash

    # swupd bundle-add network-basic lamp-basic


Using Linux Bridges
===================

#. Create a script named **qemu-ifup** for a linux bridge in a virtual machine.

   .. code-block:: bash

      #!/bin/bash
	    set -x
	    switch=br0
	     if [ -n "$1" ];then
	     	tunctl -u whoami -t $1
	     	ip link set $1 up
	     	sleep 0.5s
	     	brctl addif $switch $1
	     	exit 0
	     else
	        echo "Error: no interface specified"
	        exit 1
	     fi
	
#. Enable execute permission on the script, preserving its group permissions with
   respect to other files.

   .. code-block:: bash

      # chmod a+x qemu-ifup

#. Create a bridge using the OpenvSwitch tool; you can verify whether the bridge
   was successfully created by using ip tool.

   .. code-block:: bash

      # brctl addbr br0

 Note: At this point, you have the option to add a NIC with ``brctl addif br0 <network interface>``.  Sample interface below should be replaced with your local
 NIC's designation.

.. code-block:: bash

   # brctl addif br0 enp3s0f0

When the above option is used, and the NIC is connected to DHCP server, so Steps
1 and 2 under the `Setting IP address`_ section.

#. Set up the Linux bridge.

   .. code-block:: bash

      # ip link set dev br0 up

#. Run guest virtual machine A using the next configuration as reference, where
   the **$IMAGE** var is the Clear Linux image name.

   .. code-block:: bash

	  qemu-system-x86_64 \
	    -enable-kvm -m 1024 \
	    -bios OVMF.fd \
	    -smp cpus=2,cores=1 -cpu host \
	    -vga none -nographic \
	    -drive file="$IMAGE",if=virtio,aio=threads \
	    -net nic,macaddr=00:11:22:33:44:55,model=virtio -net tap,script=qemu-ifup \
	    -debugcon file:debug.log -global isa-debugcon.iobase=0x402


#. Run guest virtual machine B using the configuration from the previous step; 
   take care to update the MAC address.

#. Follow the instructions from the `Setting IP Address`_ section.

#. And to clean the previous environment, turn off the virtual machines and delete
   the bridge.

   .. code-block:: bash

	  # ip link set dev br0 down
	  # brctl delbr br0


Using OpenvSwitch
=================

#. Start the OpenvSwitch service.

   .. code-block:: bash

      # systemctl start openvswitch.service

#. Create a bridge using the OpenvSwitch tool; you can verify whether or not the
   bridge was successfully created by running ip tool.

   .. code-block:: bash

	  # ovs-vsctl add-br br0
	  # ip a

#. Create **UP-DOWN** scripts which can bring up the tap devices through the
   bridge we created in Step 2. 

   The **ovs-ifdown** script should look something like:

   .. code-block:: bash

	  #!/bin/sh
	   switch="br0"
	   /usr/bin/ifconfig $1 0.0.0.0 down
	   ovs-vsctl del-port ${switch} $1

   And the **ovs-ifup script** should look something like:

   .. code-block:: bash

	  #!/bin/sh
	   switch="br0"
	   /usr/bin/ifconfig $1 0.0.0.0 up
	   ovs-vsctl add-port ${switch} $1

#. Enable execute permission on the scripts, preserving their group permissions
   with respect to other files.

   .. code-block:: bash

	  # chmod a+x ovs-ifdown
	  # chmod a+x ovs-ifup

#. Run guest virtual machine A using the next configuration as reference, where
   **$IMAGE** var is the name of the Clear Linux* OS for Intel Architecture image. 
   Notice the network configuration uses the up-down scripts.

   .. code-block:: bash

      qemu-system-x86_64 \
          -enable-kvm -m 1024 \
          -bios OVMF.fd \
          -smp cpus=2,cores=1 -cpu host \
          -vga none -nographic \
          -drive file="$IMAGE",if=virtio,aio=threads \
          -net nic,model=virtio,macaddr=00:11:22:33:44:55 -net tap,script=ovs-ifup,downscript=ovs-ifdown \
          -debugcon file:debug.log -global isa-debugcon.iobase=0x402

#. Run guest virtual machine B using the configuration from step 5, only
   it's necessary to change the MAC address to something like *00:11:22:33:44:56*

#. Follow the instructions in the `Setting IP address`_ section.


Using Linux OpenvSwitch-DPDK
============================

#. If the system is running release 12489 or older, it must be updated with
   this command.

   .. code-block:: bash

      # swupd update

#. Install the ``network-basic`` bundle.

   .. code-block:: bash

      # swupd bundle-add network-basic

#. Enable VT-d technology in the BIOS.

#. Enable VT-d in the host kernel command line, to enable VT-d in the host kernel
   command line, the ``clear-linux-native-<current-kernel-version>.conf``
   file must be edited. Add ``iommu=pt intel_iommu=on`` to the end of the line.
   The file is found within the UEFI boot partition.

   .. code-block:: bash

      # systemctl start boot.mount
      # cd /boot/loader/entries/

#. Unmount the UEFI partition and reboot the machine.
   
   .. code-block:: bash

      # cd /
      # systemctl stop boot.mount
      # reboot
    
#. Set number of hugepages.

   .. code-block:: bash

      # echo 1024 > /sys/kernel/mm/hugepages/hugepages-2048kB/nr_hugepages

#. Allocate pages on NUMA machines.

   .. code-block:: bash

      # echo 1024 > /sys/devices/system/node/node0/hugepages/hugepages-2048kB/nr_hugepages
      # echo 1024 > /sys/devices/system/node/node1/hugepages/hugepages-2048kB/nr_hugepages

#. Make memory available for the DPDK.

   .. code-block:: bash

      # mkdir -p /mnt/huge
      # mount -t hugetlbfs nodev /mnt/huge

#. Download a clear linux image and OVMF.fd file, this image will be used as
   the guest VMs in the `Clear Linux downloads`_.

#. Start the OpenvSwitch service.

   .. code-block:: bash

      # systemctl start openvswitch

#. OpenvSwitch must be configured to enable the DPDK functionality like core
   mask, socket memory, and others. This example reproduces the environment
   shown in figure 1.0. The `OpenvSwitch documentation`_ provides additional
   information about DPDK configuration.

   .. code-block:: bash

      # ovs-vsctl --no-wait init
      # ovs-vsctl --no-wait set Open_vSwitch . other_config:dpdk-lcore-mask=0x2
      # ovs-vsctl --no-wait set Open_vSwitch . other_config:dpdk-socket-mem=2048
      # ovs-vsctl --no-wait set Open_vSwitch . other_config:dpdk-init=true

#. Restart the OpenvSwitch service in order to update the new DPDK configuration.

   .. code-block:: bash

      # systemctl restart openvswitch

#. Create a virtual bridge using openvswitch.
   
   .. code-block:: bash

      # ovs-vsctl add-br br0 -- set bridge br0 datapath_type=netdev

#. Add the vhost-dpdk ports to the bridge.
   
   .. code-block:: bash

      # ovs-vsctl add-port br0 vhost-user1 -- set Interface vhost-user1 type=dpdkvhostuser
      # ovs-vsctl add-port br0 vhost-user2 -- set Interface vhost-user2 type=dpdkvhostuser

#. Run guest virtual machine A using the next configuration as reference, where
   **$IMAGE** var is the name of the Clear Linux* OS for Intel Architecture image.

   .. code-block:: bash

      $ qemu-system-x86_64 \
          -enable-kvm -m 1024 \
          -bios OVMF.fd \
          -smp 4 -cpu host \
          -vga none -nographic \
          -drive file="$IMAGE",if=virtio,aio=threads \
          -chardev socket,id=char1,path=/run/openvswitch/vhost-user1 \
          -netdev type=vhost-user,id=mynet1,chardev=char1,vhostforce \
          -device virtio-net-pci,mac=00:00:00:00:00:01,netdev=mynet1 \
          -object memory-backend-file,id=mem,size=1024M,mem-path=/dev/ hugepages,share=on \
          -numa node,memdev=mem -mem-prealloc \
          -debugcon file:debug.log -global isa-debugcon.iobase=0x402

#. Run guest virtual machine B, use the configuration from the previous step; 
   simply change the MAC address and the port socket. You can use 00:00:00:00:00:02 as a 
   MAC address and vhost-user2 as a socket.

#. Follow the instructions from the `Setting IP address`_ section.



.. _Setting IP address:

Setting IP address
==================

#. Set an IP address to virtual machine for virtual machine A:
   
   .. code-block:: bash

      # ip addr add dev enp0s2 10.0.0.5/24

   for virtual machine B:

   .. code-block:: bash

      # ip addr add dev enp0s2 10.0.0.6/24

#. Check if there is communication between both virtual machines using ping tool.

#. Verify that Apache service is running:

   .. code-block:: bash

      # systemctl status httpd.service
      # systemctl start httpd.service 

   Start httpd service only if it is inactive. Use apache benchmark to get
   information about the network performance between both virtual machines.

   .. code-block:: bash

      # ab -n 1000000 -c 100 http://10.0.0.6/


.. _DPDK: http://dpdk.org/
.. _kvm: https://download.clearlinux.org/releases/
.. _Clear Linux downloads: https://download.clearlinux.org/image/
.. _OpenvSwitch documentation: http://docs.openvswitch.org/en/latest/
