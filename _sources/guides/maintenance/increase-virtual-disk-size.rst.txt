.. _increase-virtual-disk-size:

Increase Virtual Disk Size of an Image
######################################

|CL-ATTR| pre-built images come in different sizes, ranging from 300 MB to 20
GB. This guide describes how to increase the disk size of your pre-built 
image if you need more capacity.  We will use the :ref:`KVM image<kvm>` as 
an example to demonstrate the process of increasing disk size and expanding
the last partition to take up the added space.   

.. contents::
   :local:
   :depth: 1

Determine disk size and list of partitions
******************************************

There are two methods to find the disk size and the list of partitions of 
a pre-built |CL| image.  

Method 1: Use :command:`lsblk` on the VM
========================================

The first method is to boot up your VM and execute the :command:`lsblk` 
command as shown below:

.. code-block:: bash

   lsblk

An example output of the :command:`lsblk` command:

.. code-block:: console
   :emphasize-lines: 4,7

   NAME   MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
   fd0      2:0    1    4K  0 disk 
   sr0     11:0    1 1024M  0 rom  
   vda    254:0    0  8.6G  0 disk 
   ├─vda1 254:1    0  510M  0 part 
   ├─vda2 254:2    0   33M  0 part [SWAP]
   └─vda3 254:3    0    8G  0 part /

An example of this can also be seen in Figure 1.

Method 2: Look at the image configuration YAML file 
===================================================

The second method to look at the image configuration YAML file that was
used to produce the image. 

For example, to find the size of the KVM image version number 31880,
follow these steps:

#. Go to the `releases`_ repository.
#. Drill down into the `31880 > clear > config > image` directory.
#. Download and open the :file:`kvm.yaml` file.
#. Locate the `targetMedia` section.

   The example shows a total disk size of 8.54 GB, 512 MB for the EFI 
   partition, 32 MB for the swap partition, and 8 GB for the root partition.

   .. code-block:: console
      :linenos:
      :emphasize-lines: 3,9,13,18

      targetMedia:
      - name: ${bdevice}
        size: "8.54G"
        type: disk
        children:
        - name: ${bdevice}1
          fstype: vfat
          mountpoint: /boot
          size: "512M"
          type: part
        - name: ${bdevice}2
          fstype: swap
          size: "32M"
          type: part
        - name: ${bdevice}3
          fstype: ext4
          mountpoint: /
          size: "8G"
          type: part

Increase virtual disk size
**************************

Before you can expand the last partition of your image, you must make 
space available by increasing the virtual disk size.  After that, you
can resize the last partition and finally resize the filesystem. 
Follow these steps:

Increase virtual disk size
==========================

#. Shut down your VM.
#. Use the process defined by your hypervisor or cloud provider to increase
   the virtual disk size of your |CL| VM.
#. Power up your VM.

Resize the last partition of the virtual disk
=============================================

#. Log in.
#. Open a terminal window.
#. Add the :command:`storage-utils` bundle to install the
   :command:`parted` and :command:`resize2fs` tools.

   .. code-block:: bash

      sudo swupd bundle-add storage-utils

#. Launch the :command:`parted` tool.

   .. code-block:: bash

      sudo parted

#. In the `parted` tool, perform these steps:

   a. Press :command:`p` to print the partitions table.
   #. If the warning message below is displayed, enter :command:`Fix`.

      .. code-block:: console

         Warning: Not all of the space available to :file:`/dev/sda` appears 
         to be used, you can fix the GPT to use all of the space (an extra ...
         blocks) or continue with the current setting?

         Fix/Ignore?

   #. Enter :command:`resizepart <partition number>` where
      *<partition number>* is the number of the partition to modify.
   #. Enter the new `End` size.

      .. note::

         If you want a partition to take up the remaining disk space, then
         enter the total size of the disk. When you print the partitions
         table with the :command:`p` command, the total disk size is shown
         after the :guilabel:`Disk` label.

         An example of this can be seen in Figure 1.

   #. Enter :command:`q` to exit `parted` when you are finished resizing the
      partition.

      Figure 1 depicts the described steps to resize the partition of the 
      virtual disk from 8.5 GB to 30 GB.

      .. rst-class:: dropshadow

      .. figure:: ../../_figures/increase-virtual-disk-size/01-increase-virtual-disk-size.png
         :scale: 100 %
         :alt: Increase root partition size

         Figure 1: Increase root partition size

Resize the filesystem
=====================

#. Enter :command:`sudo resize2fs -p /dev/<modified partition name>` where
   *<modified partition name>* is the partition that was changed in the `parted`
   tool.

#. Run :command:`lsblk` to verify that the filesystem size has increased.

   Figure 2 depicts the described steps to resize the filesystem of the virtual
   disk from 8.5 GB to 30 GB.

   .. rst-class:: dropshadow

   .. figure:: ../../_figures/increase-virtual-disk-size/02-increase-virtual-disk-size.png
      :scale: 100 %
      :alt: Increase root filesystem with resize2fs

      Figure 2: Increase root filesystem with :command:`resize2fs` 

.. _releases: https://cdn.download.clearlinux.org/releases/
