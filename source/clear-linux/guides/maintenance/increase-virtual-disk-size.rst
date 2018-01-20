.. _increase-virtual-disk-size:

Increase Clear Linux image virtual disk size
############################################

Pre-built |CLOSIA| images come in different sizes, ranging anywhere
from 300M to 20G.  This section shows you how to increase the size of your 
pre-built |CL| image if you need more capacity.

Determine the pre-built image size
**********************************

There are two methods you can use to find the virtual disk size of your 
pre-built |CL| image.

The first method is to check the image's config JSON file located in the 
`releases`_ repository.  For example, to find the size of the 
Hyper-V image version number 20450, you can follow these steps:

#.	Go to the `releases`_ repository.
#.	Drill down into the `20450 > clear > config > image` directory.
#.	Open the :file:`hyperv-config.json` file.  
#.	Locate the `PartitionLayout` key like this example.  This one shows an 
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
execute the :command:`lsblk` command.  Here's a sample output:

	.. code-block:: console

		# lsblk

		NAME   MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
		sda      8:0   0    8.5G  0 disk
		├─sdd1   8:1   0    512M  0 part 
		├─sdd2   8:2   0     32M  0 part [SWAP]
		└─sdd3   8:3   0      8G  0 part /

As you can see, both methods show the pre-built Hyper-V image is about 8.5GB. 

Increase the root partition size
********************************

To increase the image size of a pre-built image, follow these steps:

#.	Shutdown your VM, if it's running.  
#.	Use the appropriate hypervisor tool to increase the virtual disk size of 
	your VM.
#.	Power up the VM.
#. 	Log into an account with root privileges.  
#.	Open a terminal emulator.
#.	Add the |CL| `storage-utils` bundle to install the `parted` and 
	`resize2fs` tools.

	.. code-block:: console

		# swupd bundle-add storage-utils

#.	Launch the :command:`parted` command.

	.. code-block:: console

		# parted

#.	In the `parted` tool, perform these steps:

	#.	Press :kbd:`p` to print the partitions table.
	#.	Enter :command:`fix` when prompted.
	#.	Enter :command:`resizepart [partition number]` where [partition number] 
		is the partition number you wish to modify.
	#.	Enter :command:`yes` when prompted.
	#.	Ener the new `End` size.  The `End` size is the total size of the disk.
	#.	Enter :kbd:`q` to exit `parted`.
	#.	Enter :command:`resize2fs -p /dev/[modified partition name]` where 
		[modified partition name] is the partition that was changed in `parted`.

	Figure 1 below shows an example of increasing the size of a |CL| Hyper-V image 
	from 8.5GB to 20GB.  Hyper-V Manager was used prior to increase the virtual disk
	size from 8.5GB to 20GB before performing the steps show in Figure 1.  

	.. figure:: figures/increase-virtual-disk-size-1.png
		:scale: 100 %
		:alt: Increase root partition size example

		Figure 1: Increase root partition size example 

.. _releases: https://download.clearlinux.org/releases/
