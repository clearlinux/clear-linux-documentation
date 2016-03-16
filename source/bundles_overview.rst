.. _bundles_overview:

Bundles overview
################

Linux-based operating systems contain the code of several hundred, if
not thousands, of open source projects. To make this manageable,
distributions use a concept called "packages" to configure and compile
the source code of these projects into binaries.

Many distributions then split the content of these compiled packages
into so-called sub-packages, which are the granularity at which these
distributions deploy their software. With those kinds of distributions,
system administrators can then install and update sub-packages
individually or as a set, using tools such as "yum" and "apt-get."

The Clear Linux* OS for Intel® Architecture takes a slightly different
approach. While we also use the concept of packages to manage compiling
source code into binaries, we do not use the package concept to deploy
software. Instead, we provide "bundles" that  provide a set of functionality
to the system administrator, independent of how many and which pieces of
the upstream open source projects are needed for this functionality. The
diagram below gives an overall picture of it.

.. image:: _static/images/bundles_overview.png
     :align: center
     :alt: bundles-overview


To add a bundle
===============

``# swupd bundle-add [bundle name]``

To see a list of installed bundles
==================================

``# ls /usr/share/clear/bundles``


Current list of available bundles: 

.. raw:: html
   
   <head>
	<title>Bundles in ClearLinux</title>
	<style type="text/css">
		table { margin: 2em; border: 1px solid #e0e0e0; border-collapse: collapse; width: auto; }
		th { align: center; padding: 0.5em; border: #ccc solid 1px; background-color: #555; color: #fff; text-transform: uppercase; font-size: 1.21em }
		tbody tr:nth-child(odd) { background-color:#e0e0e0; } 			
	    .bundlename { font-family: monospace; font-size: 1.23em; font-weight: bold;}
	    .bundlestatus { font-weight: bold; }
	    .bundledesc { font-size: 1em; line-height: 0.88em; font-family: sans; }
		li { margin-left: 0.53em; padding-left: 0.23em; }
		</style>
	</head>
    
    <table>
        <tr>
            <th align=left>Bundle Name</th>
            <th align=center>Status</th>
            <th align=left>Description</th>
            <!-- <th align=left>Capabilities</th> -->
            <!-- <th align=left>Maintainer</th> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> bat</td>
            <td align=center class="bundlestatus"> ACTIVE</td>
            <td align=left class="bundledesc">
                <p> Provides the neccesary bundles to perform BAT succesfully</p>
                <li>Includes (devtools-basic) bundle.</p>
                    <li>Includes (openstack-test-suite) bundle.</p>
                        <li>Includes (os-testsuite) bundle.</p>
                            <li>Includes (pnp-tools-basic) bundle.</p>
                                <li>Includes (openstack-all-in-one) bundle.</p>
                                    <li>Includes (storage-utils) bundle.</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> bootloader</td>
            <td align=center class="bundlestatus"> ACTIVE</td>
            <td align=left class="bundledesc">
                <p> UEFI bootloaders</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> cloud-control</td>
            <td align=center class="bundlestatus"> WIP</td>
            <td align=left class="bundledesc">
                <p> Support packages for a cloud control surface</p>
                <li>Includes (os-utils) bundle.</p>
                    <li>Includes (kvm-host) bundle.</p>
                        <li>Includes (net-utils) bundle.</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> clr-devops</td>
            <td align=center class="bundlestatus"> ACTIVE</td>
            <td align=left class="bundledesc">
                <p> Provides build/release tools for Clear devops team</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> containers-basic</td>
            <td align=center class="bundlestatus"> WIP</td>
            <td align=left class="bundledesc">
                <p> Installs rkt base for Clear Containers</p>
                <li>Includes (storage-utils) bundle.</p>
                    <li>Includes (network-basic) bundle.</p>
                        <li>Includes (kernel-container) bundle.</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> cryptography</td>
            <td align=center class="bundlestatus"> ACTIVE</td>
            <td align=left class="bundledesc">
                <p> Cryptographic tools</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> database-mariadb</td>
            <td align=center class="bundlestatus"> ACTIVE</td>
            <td align=left class="bundledesc">
                <p> Provides components needed to run MariaDB</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> database-mariadb-dev</td>
            <td align=center class="bundlestatus"> ACTIVE</td>
            <td align=left class="bundledesc">
                <p> Provides MariaDB development tools (libraries and drivers)</p>
                <li>Includes (database-mariadb) bundle.</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> database-mongodb</td>
            <td align=center class="bundlestatus"> WIP</td>
            <td align=left class="bundledesc">
                <p> Provides components needed to run mongodb</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> devtools-basic</td>
            <td align=center class="bundlestatus"> ACTIVE</td>
            <td align=left class="bundledesc">
                <p> Provides basic set of languages and tools for development</p>
                <li>Includes (R-basic) bundle.</p>
                    <li>Includes (go-basic) bundle.</p>
                        <li>Includes (hpc-basic) bundle.</p>
                            <li>Includes (os-core-dev) bundle.</p>
                                <li>Includes (perl-basic) bundle.</p>
                                    <li>Includes (python-basic) bundle.</p>
                                        <li>Includes (ruby-basic) bundle.</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> devtools-extras</td>
            <td align=center class="bundlestatus"> ACTIVE</td>
            <td align=left class="bundledesc">
                <p> Provides extra set of languages and tools for development</p>
                <li>Includes (R-extras) bundle.</p>
                    <li>Includes (devtools-basic) bundle.</p>
                        <li>Includes (go-extras) bundle.</p>
                            <li>Includes (perl-extras) bundle.</p>
                                <li>Includes (python-extras) bundle.</p>
                                    <li>Includes (ruby-extras) bundle.</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> dev-utils</td>
            <td align=center class="bundlestatus"> ACTIVE</td>
            <td align=left class="bundledesc">
                <p> Provides a limited set of development utilities</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> dpdk-dev</td>
            <td align=center class="bundlestatus"> ACTIVE</td>
            <td align=left class="bundledesc">
                <p> All headers and libraries necessary to develop with the Data Plane Development Kit.</p>
                <li>Includes (os-core-dev) bundle.</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> editors</td>
            <td align=center class="bundlestatus"> ACTIVE</td>
            <td align=left class="bundledesc">
                <p> Provides popular text editors</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> file-utils</td>
            <td align=center class="bundlestatus"> ACTIVE</td>
            <td align=left class="bundledesc">
                <p> Provides basic set of file manipulation utilities</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> Games</td>
            <td align=center class="bundlestatus"> ACTIVE</td>
            <td align=left class="bundledesc">
                <p> A colossal, but entertaining waste of time</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> go-basic</td>
            <td align=center class="bundlestatus"> ACTIVE</td>
            <td align=left class="bundledesc">
                <p> Provides basic Go language development</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> go-extras</td>
            <td align=center class="bundlestatus"> ACTIVE</td>
            <td align=left class="bundledesc">
                <p> Most popular Golang libraries</p>
                <li>Includes (go-basic) bundle.</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> hpc-basic</td>
            <td align=center class="bundlestatus"> ACTIVE</td>
            <td align=left class="bundledesc">
                <p> Provides basic suite of MPI/HPC development tools</p>
                <li>Includes (os-core-dev) bundle.</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> iot</td>
            <td align=center class="bundlestatus"> WIP</td>
            <td align=left class="bundledesc">
                <p> The IoT (Internet of Things) base bundle</p>
                <li>Includes (kernel-embedded) bundle.</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> java-basic</td>
            <td align=center class="bundlestatus"> ACTIVE</td>
            <td align=left class="bundledesc">
                <p> Provides all openjdk tools</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> kernel-container</td>
            <td align=center class="bundlestatus"> WIP</td>
            <td align=left class="bundledesc">
                <p> Provides a Linux kernel appropriate for a Clear Container</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> kernel-embedded</td>
            <td align=center class="bundlestatus"> ACTIVE</td>
            <td align=left class="bundledesc">
                <p> Provides a Linux kernel appropriate for embedded devices</p>
                <li>Includes (bootloader) bundle.</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> kernel-kvm</td>
            <td align=center class="bundlestatus"> ACTIVE</td>
            <td align=left class="bundledesc">
                <p> Provides a Linux kernel appropriate for running under KVM</p>
                <li>Includes (bootloader) bundle.</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> kernel-native</td>
            <td align=center class="bundlestatus"> ACTIVE</td>
            <td align=left class="bundledesc">
                <p> Provides a Linux kernel appropriate for physical machines</p>
                <li>Includes (bootloader) bundle.</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> kernel-pxe</td>
            <td align=center class="bundlestatus"> ACTIVE</td>
            <td align=left class="bundledesc">
                <p> Provides a Linux kernel linking an initramfs as root</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> koji</td>
            <td align=center class="bundlestatus"> WIP</td>
            <td align=left class="bundledesc">
                <p> Sets up a koji build service (builder-only, for now) based on NFS mounts.</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> kvm-host</td>
            <td align=center class="bundlestatus"> WIP</td>
            <td align=left class="bundledesc">
                <p> Provides necessary tools to run usable virtual machines with QEMU-KVM (independently of OpenStack).</p>
                <li>Includes (kernel-kvm) bundle.</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> lamp-basic</td>
            <td align=center class="bundlestatus"> ACTIVE</td>
            <td align=left class="bundledesc">
                <p> Basic LAMP Server (apache2, mariadb, php5)</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> mail-utils</td>
            <td align=center class="bundlestatus"> WIP</td>
            <td align=left class="bundledesc">
                <p> Provides utilities for reading and sending email</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> message-broker-rabbitmq</td>
            <td align=center class="bundlestatus"> ACTIVE</td>
            <td align=left class="bundledesc">
                <p> Provides the RabbitMQ messaging service</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> mixer</td>
            <td align=center class="bundlestatus"> WIP</td>
            <td align=left class="bundledesc">
                <p> Provide required utilities to make derivative releases</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> net-utils</td>
            <td align=center class="bundlestatus"> ACTIVE</td>
            <td align=left class="bundledesc">
                <p> Provides an essential suite of core networking configuration and debug tools</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> network-advanced</td>
            <td align=center class="bundlestatus"> WIP</td>
            <td align=left class="bundledesc">
                <p> More utilities for advanced host-level networking; bridge, switch, netfilter, vpn etc.</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> network-basic</td>
            <td align=center class="bundlestatus"> ACTIVE</td>
            <td align=left class="bundledesc">
                <p> Provides a basic suite of networking utilities</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> network-proxy-client</td>
            <td align=center class="bundlestatus"> WIP</td>
            <td align=left class="bundledesc">
                <p> Tools for dealing with client-side network proxy settings.</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> nfs-utils</td>
            <td align=center class="bundlestatus"> WIP</td>
            <td align=left class="bundledesc">
                <p> Provides NFS binaries, associated utilities, and tools. Currently only client services are fully supported.</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> openssh-server</td>
            <td align=center class="bundlestatus"> ACTIVE</td>
            <td align=left class="bundledesc">
                <p> Provides an SSH server (and client)</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> openstack-all-in-one</td>
            <td align=center class="bundlestatus"> WIP</td>
            <td align=left class="bundledesc">
                <p> Provides an All-in-one OpenStack deployment</p>
                <li>Includes (database-mariadb) bundle.</p>
                    <li>Includes (database-mongodb) bundle.</p>
                        <li>Includes (message-broker-rabbitmq) bundle.</p>
                            <li>Includes (openstack-block-storage) bundle.</p>
                                <li>Includes (openstack-block-storage-controller) bundle.</p>
                                    <li>Includes (openstack-compute) bundle.</p>
                                        <li>Includes (openstack-compute-controller) bundle.</p>
                                            <li>Includes (openstack-dashboard) bundle.</p>
                                                <li>Includes (openstack-data-processing) bundle.</p>
                                                    <li>Includes (openstack-database) bundle.</p>
                                                        <li>Includes (openstack-identity) bundle.</p>
                                                            <li>Includes (openstack-image) bundle.</p>
                                                                <li>Includes (openstack-lbaas) bundle.</p>
                                                                    <li>Includes (openstack-network) bundle.</p>
                                                                        <li>Includes (openstack-object-storage) bundle.</p>
                                                                            <li>Includes (openstack-orchestration) bundle.</p>
                                                                                <li>Includes (openstack-python-clients) bundle.</p>
                                                                                    <li>Includes (openstack-telemetry) bundle.</p>
                                                                                        <li>Includes (openstack-vpnaas) bundle.</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> openstack-block-storage</td>
            <td align=center class="bundlestatus"> WIP</td>
            <td align=left class="bundledesc">
                <p> Provides an OpenStack Cinder service</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> openstack-block-storage-controller</td>
            <td align=center class="bundlestatus"> WIP</td>
            <td align=left class="bundledesc">
                <p> Provides an OpenStack Cinder controller service</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> openstack-compute</td>
            <td align=center class="bundlestatus"> WIP</td>
            <td align=left class="bundledesc">
                <p> Provides an OpenStack nova-compute node</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> openstack-compute-controller</td>
            <td align=center class="bundlestatus"> WIP</td>
            <td align=left class="bundledesc">
                <p> Provides an OpenStack Nova control server</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> openstack-configure</td>
            <td align=center class="bundlestatus"> WIP</td>
            <td align=left class="bundledesc">
                <p> Provides a suggested default configuration for OpenStack on Clear Linux.</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> openstack-controller</td>
            <td align=center class="bundlestatus"> WIP</td>
            <td align=left class="bundledesc">
                <p> Provides an OpenStack multi-service control server</p>
                <li>Includes (database-mariadb) bundle.</p>
                    <li>Includes (message-broker-rabbitmq) bundle.</p>
                        <li>Includes (openstack-identity) bundle.</p>
                            <li>Includes (openstack-image) bundle.</p>
                                <li>Includes (openstack-compute-controller) bundle.</p>
                                    <li>Includes (openstack-dashboard) bundle.</p>
                                        <li>Includes (openstack-python-clients) bundle.</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> openstack-dashboard</td>
            <td align=center class="bundlestatus"> WIP</td>
            <td align=left class="bundledesc">
                <p> Provides an OpenStack Horizon server</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> openstack-database</td>
            <td align=center class="bundlestatus"> WIP</td>
            <td align=left class="bundledesc">
                <p> Provides a Database as a Service server</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> openstack-data-processing</td>
            <td align=center class="bundlestatus"> WIP </td>
            <td align=left class="bundledesc">
                <p> Provides a simple means to provision a data-intensive application cluster </p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> openstack-identity</td>
            <td align=center class="bundlestatus"> WIP</td>
            <td align=left class="bundledesc">
                <p> Provides an OpenStack Keystone server</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> openstack-image</td>
            <td align=center class="bundlestatus"> WIP</td>
            <td align=left class="bundledesc">
                <p> Provides an OpenStack Glance server</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> openstack-lbaas</td>
            <td align=center class="bundlestatus"> WIP</td>
            <td align=left class="bundledesc">
                <p> Provides Load Balancing as a Service</p>
                <li>Includes (openstack-network) bundle.</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> openstack-network</td>
            <td align=center class="bundlestatus"> WIP</td>
            <td align=left class="bundledesc">
                <p> Provides an OpenStack Neutron server</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> openstack-object-storage</td>
            <td align=center class="bundlestatus"> WIP</td>
            <td align=left class="bundledesc">
                <p> Provides an OpenStack Swift service</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> openstack-orchestration</td>
            <td align=center class="bundlestatus"> WIP</td>
            <td align=left class="bundledesc">
                <p> Provides an OpenStack Heat service</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> openstack-python-clients</td>
            <td align=center class="bundlestatus"> WIP</td>
            <td align=left class="bundledesc">
                <p> Provides OpenStack command-line utilities</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> openstack-telemetry</td>
            <td align=center class="bundlestatus"> WIP</td>
            <td align=left class="bundledesc">
                <p> Provides an OpenStack Telemetry server</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> openstack-telemetry-controller</td>
            <td align=center class="bundlestatus"> Deprecated</td>
            <td align=left class="bundledesc">
                <p> Provides an OpenStack Telemetry server</p>
                <li>Includes (openstack-telemetry) bundle.</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> openstack-test-suite</td>
            <td align=center class="bundlestatus"> WIP</td>
            <td align=left class="bundledesc">
                <p> Provides an OpenStack Tempest/test suite </p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> openstack-vpnaas</td>
            <td align=center class="bundlestatus"> WIP</td>
            <td align=left class="bundledesc">
                <p> Provides VPN as a Service</p>
                <li>Includes (openstack-network) bundle.</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> os-cloudguest</td>
            <td align=center class="bundlestatus"> WIP</td>
            <td align=left class="bundledesc">
                <p> Provides clr-cloud-init cloud guest configuration utilities</p>
                <li>Includes (openssh-server) bundle.</p>
                    <li>Includes (telemetrics) bundle.</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> os-cloudguest-cci</td>
            <td align=center class="bundlestatus"> WIP</td>
            <td align=left class="bundledesc">
                <p> Retired bundle - now provided by os-cloudguest</p>
                <li>Includes (os-cloudguest) bundle.</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> os-clr-on-clr</td>
            <td align=center class="bundlestatus"> WIP</td>
            <td align=left class="bundledesc">
                <p> content for development of the Clear Linux OS on the Clear Linux OS</p>
                <li>Includes (os-dev-extras) bundle.</p>
                    <li>Includes (mail-utils) bundle.</p>
                        <li>Includes (storage-utils) bundle.</p>
                            <li>Includes (os-core-update) bundle.</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> os-core</td>
            <td align=center class="bundlestatus"> ACTIVE</td>
            <td align=left class="bundledesc">
                <p> The basic core OS components of Clear Linux for iA </p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> os-core-dev</td>
            <td align=center class="bundlestatus"> ACTIVE</td>
            <td align=left class="bundledesc">
                <p> Basic development tools</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> os-core-update</td>
            <td align=center class="bundlestatus"> ACTIVE</td>
            <td align=left class="bundledesc">
                <p> Provides basic suite for running the Clear Linux for iA Updater</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> os-dev-extras</td>
            <td align=center class="bundlestatus"> ACTIVE</td>
            <td align=left class="bundledesc">
                <p> Additional C/C++ development packages (beyond os-core-dev)</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> os-dev-full</td>
            <td align=center class="bundlestatus"> WIP</td>
            <td align=left class="bundledesc">
                <p> A bundle containing all development libraries and headers</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> os-installer</td>
            <td align=center class="bundlestatus"> ACTIVE</td>
            <td align=left class="bundledesc">
                <p> Provides an installer for Clear Linux for iA</p>
                <li>Includes (telemetrics) bundle.</p>
                    <li>Includes (network-proxy-client) bundle.</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> os-testsuite</td>
            <td align=center class="bundlestatus"> WIP</td>
            <td align=left class="bundledesc">
                <p> Provides basic test suite for Clear Linux for iA</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> os-testsuite-phoronix</td>
            <td align=center class="bundlestatus"> ACTIVE</td>
            <td align=left class="bundledesc">
                <p> All the required pieces for running the Phoronix Test Suite</p>
                <li>Includes (os-utils) bundle.</p>
                    <li>Includes (devtools-basic) bundle.</p>
                        <li>Includes (hpc-basic) bundle.</p>
                            <li>Includes (R-extras) bundle.</p>
                                <li>Includes (lamp-basic) bundle.</p>
                                    <li>Includes (go-basic) bundle.</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> os-utils</td>
            <td align=center class="bundlestatus"> ACTIVE</td>
            <td align=left class="bundledesc">
                <p> Provides a core set of OS utilities</p>
                <li>Includes (editors) bundle.</p>
                    <li>Includes (dev-utils) bundle.</p>
                        <li>Includes (sysadmin-basic) bundle.</p>
                            <li>Includes (network-basic) bundle.</p>
                                <li>Includes (file-utils) bundle.</p>
                                    <li>Includes (network-proxy-client) bundle.</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> os-utils-gui</td>
            <td align=center class="bundlestatus"> ACTIVE</td>
            <td align=left class="bundledesc">
                <p> Provides a graphical desktop environment </p>
                <li>Includes (os-utils) bundle.</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> perl-basic</td>
            <td align=center class="bundlestatus"> ACTIVE</td>
            <td align=left class="bundledesc">
                <p> Provides essential Perl language and dev tools</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> perl-extras</td>
            <td align=center class="bundlestatus"> ACTIVE</td>
            <td align=left class="bundledesc">
                <p> Provides extra libraries for Perl</p>
                <li>Includes (perl-basic) bundle.</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> pnp-tools-advanced</td>
            <td align=center class="bundlestatus"> WIP</td>
            <td align=left class="bundledesc">
                <p> Provides advanced Power and Performance measurement tools</p>
                <li>Includes (pnp-tools-intermediate) bundle.</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> pnp-tools-basic</td>
            <td align=center class="bundlestatus"> WIP</td>
            <td align=left class="bundledesc">
                <p> Provides basic Power and Performance testing tools</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> pnp-tools-intermediate</td>
            <td align=center class="bundlestatus"> WIP</td>
            <td align=left class="bundledesc">
                <p> Provides a deeper-level suite of Power and Performance testing tools</p>
                <li>Includes (pnp-tools-basic) bundle.</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> pxe-server</td>
            <td align=center class="bundlestatus"> ACTIVE</td>
            <td align=left class="bundledesc">
                <p> All the bits to run a PXE server for Clear Linux</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> python-basic</td>
            <td align=center class="bundlestatus"> ACTIVE</td>
            <td align=left class="bundledesc">
                <p> Provides core Python language and libraries</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> python-extras</td>
            <td align=center class="bundlestatus"> ACTIVE</td>
            <td align=left class="bundledesc">
                <p> Provides extra libraries for Python</p>
                <li>Includes (python-basic) bundle.</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> R-basic</td>
            <td align=center class="bundlestatus"> ACTIVE</td>
            <td align=left class="bundledesc">
                <p> Provides core R language and libraries</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> R-extras</td>
            <td align=center class="bundlestatus"> ACTIVE</td>
            <td align=left class="bundledesc">
                <p> Provides deeper functionality R language libraries</p>
                <li>Includes (R-basic) bundle.</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> ruby-basic</td>
            <td align=center class="bundlestatus"> ACTIVE</td>
            <td align=left class="bundledesc">
                <p> Top 3 basic Ruby Libraries</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> ruby-extras</td>
            <td align=center class="bundlestatus"> ACTIVE</td>
            <td align=left class="bundledesc">
                <p> Top 3 to 6 basic Ruby Libraries</p>
                <li>Includes (ruby-basic) bundle.</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> rust-basic</td>
            <td align=center class="bundlestatus"> ACTIVE</td>
            <td align=left class="bundledesc">
                <p> rust compiler and cargo packaging tool</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> shells</td>
            <td align=center class="bundlestatus"> ACTIVE</td>
            <td align=left class="bundledesc">
                <p> All available shell programs for Clear, along with ancillary files</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> storage-cluster</td>
            <td align=center class="bundlestatus"> WIP</td>
            <td align=left class="bundledesc">
                <p> Ceph Cluster Storage</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> storage-utils</td>
            <td align=center class="bundlestatus"> ACTIVE</td>
            <td align=left class="bundledesc">
                <p> Provides basic storage-related utilities</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> sysadmin</td>
            <td align=center class="bundlestatus"> ACTIVE</td>
            <td align=left class="bundledesc">
                <p> Moved to sysadmin-basic</p>
                <li>Includes (sysadmin-basic) bundle.</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> sysadmin-advanced</td>
            <td align=center class="bundlestatus"> ACTIVE</td>
            <td align=left class="bundledesc">
                <p> Toolchest that a sysadmin needs to diagnose issues</p>
                <li>Includes (sysadmin-basic) bundle.</p>
                    <li>Includes (pnp-tools-advanced) bundle.</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> sysadmin-basic</td>
            <td align=center class="bundlestatus"> ACTIVE</td>
            <td align=left class="bundledesc">
                <p> Provides a basic set of system administration utilities.</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> sysadmin-hostmgmt</td>
            <td align=center class="bundlestatus"> WIP</td>
            <td align=left class="bundledesc">
                <p> Utilities and Services for managing large-scale clusters of networked hosts</p>
                <li>Includes (os-utils) bundle.</p>
                    <li>Includes (pxe-server) bundle.</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> telemetrics</td>
            <td align=center class="bundlestatus"> ACTIVE</td>
            <td align=left class="bundledesc">
                <p> Provides the Telemetrics client for Clear Linux for iA</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
        <tr>
            <td align=left class="bundlename"> virtualbox-guest</td>
            <td align=center class="bundlestatus"> ACTIVE</td>
            <td align=left class="bundledesc">
                <p> Include the modules and binaries meant to be used as a VirtualBox instance</p>
            </td>
            <!-- <td align=left><p></p></td> -->
            <!-- <td align=left><p></p></td> -->
        </tr>
    </table>
