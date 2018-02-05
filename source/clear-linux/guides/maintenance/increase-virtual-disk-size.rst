.. _increase-virtual-disk-size:

Increase Clear Linux image virtual disk size
############################################

Prebuilt |CLOSIA| images come in different sizes, ranging anywhere
from 300MB to 20GB. This section shows you how to increase the size of your
prebuilt |CL| image if you need more capacity.

Determine the prebuilt image size
*********************************

There are two methods you can use to find the virtual disk size of your
prebuilt |CL| image.

The first method is to check the image's config JSON file, located in the
`releases`_ repository. For example, to find the size of the
Hyper-V* image version number 20450, you can follow these steps:

#.	Go to the `releases`_ repository.
#.	Drill down into the `20450 > clear > config > image` directory.
#.	Open the :file:`hyperv-config.json` file.
#.	Locate the `PartitionLayout` key. This example shows a
	512MB for the EFI partition, 32MB for the swap partition, and 8GB for the
	root partition.

	.. code-block:: console

	   "PartitionLayout" : [ { "disk" : "hyperv.img",
	                            "partition" : 1,
	                            "size" : "512M",
	                            "type" : "EFI" },
	                          { "disk" : "hyperv.img",
	                            "partition" : 2,
	                            "size" : "32M",
	                            "type" : "swap" },
	                          { "disk" : "hyperv.img",
	                            "partition" : 3,
	                            "size" : "8G",
	                            "type" : "linux" } ],

The second method is to simply boot up your :abbr:`VM (Virtual Machine)` and
execute the :command:`lsblk` command. Here's a sample output:

	.. code-block:: bash

		# lsblk

   .. code-block:: console

		NAME   MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
		sda      8:0   0    8.5G  0 disk
		├─sdd1   8:1   0    512M  0 part
		├─sdd2   8:2   0     32M  0 part [SWAP]
		└─sdd3   8:3   0      8G  0 part /

As you can see, both methods show the prebuilt Hyper-V image is about 8.5GB.

Increase virtual disk size
**************************

Follow these steps to increase the size of a prebuilt image:

#.	Shutdown your VM if it's running.
#.	Use an appropriate hypervisor tool to increase the virtual disk size of
	your VM.
#.	Power up the VM.
#. 	Login to an account with root privileges.
#.	Open a terminal emulator.
#.	Add the |CL| `storage-utils` bundle to install the `parted` and
	`resize2fs` tools.

	.. code-block:: bash

		# swupd bundle-add storage-utils

#.	Launch the :command:`parted` tool.

	.. code-block:: bash

		# parted

#.	In the `parted` tool, perform these steps:

	#.	Press :kbd:`p` to print the partitions table.
	#.	If you get the warning message:

		.. code-block:: console

			Warning: Not all of the space available to /dev/sda appears to be
			used, you can fix the GPT to use all of the space (an extra ... 
			blocks) or continue with the current setting?

			Fix/Ignore?

		Enter :command:`fix`.

	#.	Enter :command:`resizepart [partition number]` where [partition number]
		is the partition number you wish to modify.
	#.	Enter :command:`yes` when prompted.
	#.	Enter the new `End` size.

		.. note::

			If you want a partition to take up the remaining disk space, just
			enter the total size of the disk. When you print the partitions 
			tablewith the :command:`p` command, the total disk size is shown
			after the `Disk` label.

	#.	Enter :kbd:`q` to exit `parted` when you are finished resizing the
		image.
	#.	Enter :command:`resize2fs -p /dev/[modified partition name]` where
		[modified partition name] is the partition that was changed in `parted`.

	Figure 1 below shows an example of how to increase the size of a |CL|
	Hyper-V image from 8.5GB to 20GB. Prior to the performing the steps shown
	in Figure 1, we used the Hyper-V Manager to increase the virtual disk size
	from 8.5GB to 20GB.

	.. figure:: figures/increase-virtual-disk-size-1.png
		:scale: 100 %
		:alt: Increase root partition size example

		Figure 1: Increase root partition size example

.. _releases: https://download.clearlinux.org/releases/
