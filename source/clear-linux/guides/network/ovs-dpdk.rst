.. _ovs-dpdk:

Enable DPDK support on Open vSwitch
###################################

To significantly improve network performance, enable `DPDK`_ support on the
`Open vSwitch`_ project. This guide describes a simple use case shown in
:ref:`Figure 1 <f1ovs>`, where one :abbr:`VM (virtual machine)` sends 1,000,000 HTTP
requests to another VM.

This guide describes how to connect VMs using each of the following methods:

* Linux\* bridge.
* Open vSwitch\* bridge.
* Custom-built Open vSwitch-DPDK bridge.

After setup is complete, measure network performance to see which bridge has
the best results.

.. _f1ovs:

.. figure:: ./figures/use-case.png

   Figure 1: Basic virtual network environment.

Prerequisites
*************

Perform the steps below before you run the example.

#.  Log in and get root privileges.

    .. code-block:: bash

       sudo -s

#.  Download |CLOSIA| release 13360 or higher from `Clear Linux releases`_.
    Update your system with the command:

    .. code-block:: bash

       swupd update

#.  Install the `network-basic` and `kvm-host` bundles.

    .. code-block:: bash

       swupd bundle-add network-basic
       swupd bundle-add kvm-host

#.  Download a |CL| image and :file:`OVMF.fd` file from
    `Clear Linux images`_. The images will be used as guest VMs.


Use Linux bridge
****************

#. Create a script named :file:`qemu-ifup` for a Linux bridge in a virtual
   machine.

   .. code-block:: bash

      !/bin/bash

      set -x

      switch=br0

      if [ -n "$1" ];then
          # tunctl -u `whoami` -t $1 (use ip tuntap instead!)
          ip tuntap add $1 mode tap user `whoami`
          ip link set $1 up
          sleep 0.5s
          brctl addif $switch $1
          exit 0;
      else
          echo "Error: no interface specified"
          exit 1
      fi

#. Enable execute permission on the script. Preserve the group
   permissions with respect to other files using the options below.

   .. code-block:: bash

      chmod a+x qemu-ifup

#. Create a bridge using the :command:`brctl` tool. Use the `ip` tool to
   verify whether or not the bridge was successfully created.

   .. code-block:: bash

      brctl addbr br0
      ip a

#. Add a NIC using the syntax `brctl addif br0 <network interface>`.

   .. code-block:: bash

      brctl addif br0 enp3s0f0

#. Set up the Linux bridge.

   .. code-block:: bash

      ip link set dev br0 up

#. Run guest virtual machine A using the following reference configuration,
   where the :envvar:`$IMAGE` variable is the |CL| image name.

   .. code-block:: bash

        qemu-system-x86_64 \
            -enable-kvm -m 1024 \
            -bios OVMF.fd \
            -smp cpus=2,cores=1 -cpu host \
            -vga none -nographic \
            -drive file="$IMAGE",if=virtio,aio=threads \
            -net nic,macaddr=00:11:22:33:44:55,model=virtio -net tap,script=qemu-ifup \
            -debugcon file:debug.log -global isa-debugcon.iobase=0x402

#. Run guest virtual machine B using a similar reference configuration. Be
   sure to change the MAC address to a different value.

#. Follow the instructions in the :ref:`set-ip-addr-ovs-dpdk` section.

#. When testing is complete, clean the previous environment, turn off the
   virtual machines, and delete the bridge.

   .. code-block:: bash

      ip link set dev br0 down
      brctl delbr br0

Use Open vSwitch bridge
***********************

#. Start the Open vSwitch service.

   .. code-block:: bash

      systemctl start openvswitch.service

#. Create a bridge using the Open vSwitch tool. Use the `ip` tool to verify whether
   or not the bridge was successfully created.

   .. code-block:: bash

      ovs-vsctl add-br br0
      ip a

#. Create an `UP` script named :file:`ovs-ifup` to bring up the tap devices.

   .. code-block:: bash

      !/bin/sh

      switch="br0"
      /usr/bin/ifconfig $1 0.0.0.0 up
      ovs-vsctl add-port ${switch} $1

#. Create a `DOWN` script named :file:`ovs-ifdown` to bring down the tap
   devices.

   .. code-block:: bash

      !/bin/sh

      switch="br0"
      /usr/bin/ifconfig $1 0.0.0.0 down
      ovs-vsctl del-port ${switch} $1

#. Enable execute permission on the scripts. Preserve the group
   permissions with respect to other files using the options below.

   .. code-block:: bash

      chmod a+x ovs-ifdown
      chmod a+x ovs-ifup

#. Run guest virtual machine A using the following reference configuration,
   where the :envvar:`$IMAGE` variable is the |CL| image name. Note that
   the network configuration uses the :file:`ovs-ifup` and
   :file:`ovs-ifdown` scripts.

   .. code-block:: bash

        qemu-system-x86_64 \
            -enable-kvm -m 1024 \
            -bios OVMF.fd \
            -smp cpus=2,cores=1 -cpu host \
            -vga none -nographic \
            -drive file="$IMAGE",if=virtio,aio=threads \
            -net nic,model=virtio,macaddr=00:11:22:33:44:55 -net tap,script=ovs-ifup,downscript=ovs-ifdown \
            -debugcon file:debug.log -global isa-debugcon.iobase=0x402

#. Run guest virtual machine B using a similar reference configuration. Be
   sure to change the MAC address to a different value.

#. Follow the instructions in the :ref:`set-ip-addr-ovs-dpdk` section.

#. When testing is complete, clean the previous environment, turn off the virtual
   machines, and delete the bridge.

   .. code-block:: bash

      ovs-vsctl del-br br0
      ovs-vsctl show


Use custom-built Open vSwitch-DPDK bridge
*****************************************

#. Enable VT-d technology in the BIOS.

#. Enable VT-d in the host kernel command line. You must edit the
   :file:`clear-linux-native-{current-kernel-version}.conf` file in the
   UEFI boot partition. Add `iommu=pt intel_iommu=on` to the end of the
   line.

   .. code-block:: bash

      systemctl start boot.mount
      cd /boot/loader/entries/

#. Unmount the UEFI partition and reboot the machine.

   .. code-block:: bash

      cd /
      systemctl stop boot.mount
      reboot

#. Set number of hugepages.

   .. code-block:: bash

      echo 1024 > /sys/kernel/mm/hugepages/hugepages-2048kB/nr_hugepages

#. Allocate pages on NUMA machines.

   .. code-block:: bash

      echo 1024 > /sys/devices/system/node/node0/hugepages/hugepages-2048kB/nr_hugepages
      echo 1024 > /sys/devices/system/node/node1/hugepages/hugepages-2048kB/nr_hugepages

#. Make memory available for the DPDK.

   .. code-block:: bash

      mkdir -p /mnt/huge
      mount -t hugetlbfs nodev /mnt/huge

#. Download a |CL| image and :file:`OVMF.fd` file from
   `Clear Linux images`_. The images will be used as guest VMs.

#. Start the Open vSwitch service.

   .. code-block:: bash

      systemctl start openvswitch

#. Configure Open vSwitch to enable DPDK functionality such as core
   mask, socket memory, and others. This example reproduces the environment
   shown in :ref:`Figure 1`. See the `Open vSwitch documentation`_ for more
   information about DPDK configuration.

   .. code-block:: bash

      ovs-vsctl --no-wait init
      ovs-vsctl --no-wait set Open_vSwitch . other_config:dpdk-lcore-mask=0x2
      ovs-vsctl --no-wait set Open_vSwitch . other_config:dpdk-socket-mem=2048
      ovs-vsctl --no-wait set Open_vSwitch . other_config:dpdk-init=true

#. Restart the Open vSwitch service to update the new DPDK configuration.

   .. code-block:: bash

      systemctl restart openvswitch

#. Create a virtual bridge using Open vSwitch.

   .. code-block:: bash

      ovs-vsctl add-br br0 -- set bridge br0 datapath_type=netdev

#. Add the vhost-dpdk ports to the bridge.

   .. code-block:: bash

      ovs-vsctl add-port br0 vhost-user1 -- set Interface vhost-user1 type=dpdkvhostuser
      ovs-vsctl add-port br0 vhost-user2 -- set Interface vhost-user2 type=dpdkvhostuser

#. Run guest virtual machine A using the following reference configuration,
   where the :envvar:`$IMAGE` variable is the |CL| image name.

   .. code-block:: bash

        qemu-system-x86_64 \
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

#. Run guest virtual machine B using a similar reference configuration. Be
   sure to change the MAC address and port socket to different values.
   For example, use `vhost-user2` as a socket.

#. Follow the instructions in the :ref:`set-ip-addr-ovs-dpdk` section.



.. _set-ip-addr-ovs-dpdk:

Set IP address
**************

#. Set an IP address for virtual machine A.

   .. code-block:: bash

      ip addr add dev enp0s2 10.0.0.5/24

#. Set an IP address for virtual machine B.

   .. code-block:: bash

      ip addr add dev enp0s2 10.0.0.6/24

#. Check if there is communication between both virtual machines using the
   ping tool.

#. Verify the Apache\* service is running. If the httpd service is inactive,
   use the `start` command.

   .. code-block:: bash

      systemctl status httpd.service
      systemctl start httpd.service

#. Use Apache benchmarks to get information about the network performance
   between both virtual machines.

   .. code-block:: bash

      ab -n 1000000 -c 100 http://10.0.0.6/


.. _DPDK: http://dpdk.org/
.. _Clear Linux releases: https://download.clearlinux.org/releases/
.. _Clear Linux images: https://download.clearlinux.org/image/
.. _Open vSwitch: http://openvswitch.org/
.. _Open vSwitch documentation: http://docs.openvswitch.org/en/latest/
