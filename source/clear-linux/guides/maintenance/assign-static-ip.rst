.. _assign-static-ip:

Assign a static IP address to a network interface
#################################################

Introduction
************

*<< Need input: why you need to do this and/or how it relates to other
tasks. Prerequisites? Any issues that are solved by doing this? >>*

Process
*******

#.	Make this directory:

	.. code-block:: bash

		$ sudo mkdir -p /etc/systemd/network

#.	Identify the interface to be assigned the static IP address:

	.. code-block:: bash

		$ ip addr

	The system returns the following:

	.. code-block:: console

		1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
		    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
		    inet 127.0.0.1/8 scope host lo
		       valid_lft forever preferred_lft forever
		    inet6 ::1/128 scope host
		       valid_lft forever preferred_lft forever

		2: wlp1s0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc mq state DOWN group default qlen 1000
		    link/ether 4a:98:8d:e5:43:15 brd ff:ff:ff:ff:ff:ff

		3: eno1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq state UP group default qlen 1000
		    link/ether f4:4d:30:68:96:20 brd ff:ff:ff:ff:ff:ff
		    inet 10.0.1.2/24 brd 10.54.74.255 scope global dynamic eno1
		       valid_lft 6766sec preferred_lft 6766sec
		    inet6 fe80::f64d:30ff:fe68:9620/64 scope link
		       valid_lft forever preferred_lft forever

	In this example, we will use the `eno1` interface.

#.	Create the :file:`70-static.network` file and add the following:

	.. code-block:: bash

		$ sudo vi /etc/systemd/network/70-static.network

		[Match]
		Name=[interface name]
		[Network]
		Address=[IP address]/24
		DHCP=yes # to get DNS info, etc.

	Replace [interface-name] and [IP-address] with your specific settings.

#.	Restart the networkd service:

	.. code-block:: bash

		# sudo systemctl restart systemd-networkd

**Congratulations!** You have successfully assigned a static IP address.