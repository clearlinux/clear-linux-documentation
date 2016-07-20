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

``# swupd bundle-add --list``

Or

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
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/bat">bat</a>
        </td>
        <td class="bundlestatus">ACTIVE</td>
        <td class="bundledesc">
            <p>Provides the neccesary bundles to perform BAT succesfully</p>
            <li>Includes (devtools-extras) bundle.</p>
                <li>Includes (openstack-test-suite) bundle.</p>
                    <li>Includes (pnp-tools-advanced) bundle.</p>
                        <li>Includes (openstack-all-in-one) bundle.</p>
                            <li>Includes (storage-utils) bundle.</p>
                                <li>Includes (sysadmin-hostmgmt) bundle.</p>
                                    <li>Includes (kvm-host) bundle.</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/bootloader">bootloader</a>
        </td>
        <td class="bundlestatus">ACTIVE</td>
        <td class="bundledesc">
            <p>UEFI bootloaders</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/cloud-control">cloud-control</a>
        </td>
        <td class="bundlestatus">WIP</td>
        <td class="bundledesc">
            <p>Support packages for a cloud control surface</p>
            <li>Includes (os-utils) bundle.</p>
                <li>Includes (kvm-host) bundle.</p>
                    <li>Includes (net-utils) bundle.</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/cloud-dashboard">cloud-dashboard</a>
        </td>
        <td class="bundlestatus">WIP</td>
        <td class="bundledesc">
            <p>A graphical, web-based frontend UI for a cloud scheduler service. Dependencies only for now.</p>
            <li>Includes (nodejs-basic) bundle.</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/cloud-network">cloud-network</a>
        </td>
        <td class="bundlestatus">WIP</td>
        <td class="bundledesc">
            <p>Support for cloud networking agents</p>
            <li>Includes (openssh-server) bundle.</p>
                <li>Includes (net-utils) bundle.</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/clr-devops">clr-devops</a>
        </td>
        <td class="bundlestatus">ACTIVE</td>
        <td class="bundledesc">
            <p>Provides build/release tools for Clear devops team</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/containers-basic">containers-basic</a>
        </td>
        <td class="bundlestatus">WIP</td>
        <td class="bundledesc">
            <p>Installs rkt base for Clear Containers</p>
            <li>Includes (storage-utils) bundle.</p>
                <li>Includes (network-basic) bundle.</p>
                    <li>Includes (kernel-container) bundle.</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/cryptography">cryptography</a>
        </td>
        <td class="bundlestatus">ACTIVE</td>
        <td class="bundledesc">
            <p>Cryptographic tools</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/database-mariadb">database-mariadb</a>
        </td>
        <td class="bundlestatus">ACTIVE</td>
        <td class="bundledesc">
            <p>Provides components needed to run MariaDB</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/database-mariadb-dev">database-mariadb-dev</a>
        </td>
        <td class="bundlestatus">ACTIVE</td>
        <td class="bundledesc">
            <p>Provides MariaDB development tools (libraries and drivers)</p>
            <li>Includes (database-mariadb) bundle.</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/database-mongodb">database-mongodb</a>
        </td>
        <td class="bundlestatus">Deprecated</td>
        <td class="bundledesc">
            <p>Provides components needed to run mongodb</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/devtools-basic">devtools-basic</a>
        </td>
        <td class="bundlestatus">ACTIVE</td>
        <td class="bundledesc">
            <p>Provides basic set of languages and tools for development</p>
            <li>Includes (R-basic) bundle.</p>
                <li>Includes (go-basic) bundle.</p>
                    <li>Includes (hpc-basic) bundle.</p>
                        <li>Includes (os-core-dev) bundle.</p>
                            <li>Includes (os-dev-extras) bundle.</p>
                                <li>Includes (perl-basic) bundle.</p>
                                    <li>Includes (python-basic) bundle.</p>
                                        <li>Includes (ruby-basic) bundle.</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/devtools-extras">devtools-extras</a>
        </td>
        <td class="bundlestatus">ACTIVE</td>
        <td class="bundledesc">
            <p>Provides extra set of languages and tools for development</p>
            <li>Includes (R-extras) bundle.</p>
                <li>Includes (devtools-basic) bundle.</p>
                    <li>Includes (go-extras) bundle.</p>
                        <li>Includes (perl-extras) bundle.</p>
                            <li>Includes (python-extras) bundle.</p>
                                <li>Includes (ruby-extras) bundle.</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/dev-utils">dev-utils</a>
        </td>
        <td class="bundlestatus">ACTIVE</td>
        <td class="bundledesc">
            <p>Provides a limited set of development utilities</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/dev-utils-dev">dev-utils-dev</a>
        </td>
        <td class="bundlestatus">ACTIVE</td>
        <td class="bundledesc">
            <p>All packages required to build the dev-utils bundle.</p>
            <li>Includes (dev-utils) bundle.</p>
                <li>Includes (os-core-dev) bundle.</p>
                    <li>Includes (os-dev-extras) bundle.</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/dev-utils-doc">dev-utils-doc</a>
        </td>
        <td class="bundlestatus">ACTIVE</td>
        <td class="bundledesc">
            <p>Provides documentation and manpages for dev-utils</p>
            <li>Includes (dev-utils) bundle.</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/dpdk-dev">dpdk-dev</a>
        </td>
        <td class="bundlestatus">ACTIVE</td>
        <td class="bundledesc">
            <p>All headers and libraries necessary to develop with the Data Plane Development Kit.</p>
            <li>Includes (os-core-dev) bundle.</p>
                <li>Includes (os-dev-extras) bundle.</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/editors">editors</a>
        </td>
        <td class="bundlestatus">ACTIVE</td>
        <td class="bundledesc">
            <p>Provides popular text editors</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/editors-dev">editors-dev</a>
        </td>
        <td class="bundlestatus">ACTIVE</td>
        <td class="bundledesc">
            <p>All packages required to build the editors bundle.</p>
            <li>Includes (editors) bundle.</p>
                <li>Includes (os-core-dev) bundle.</p>
                    <li>Includes (os-dev-extras) bundle.</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/editors-doc">editors-doc</a>
        </td>
        <td class="bundlestatus">ACTIVE</td>
        <td class="bundledesc">
            <p>Provides documentation and manpages for editors</p>
            <li>Includes (editors) bundle.</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/file-utils">file-utils</a>
        </td>
        <td class="bundlestatus">ACTIVE</td>
        <td class="bundledesc">
            <p>Provides basic set of file manipulation utilities</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/file-utils-dev">file-utils-dev</a>
        </td>
        <td class="bundlestatus">ACTIVE</td>
        <td class="bundledesc">
            <p>All packages required to build the file-utils bundle.</p>
            <li>Includes (file-utils) bundle.</p>
                <li>Includes (os-core-dev) bundle.</p>
                    <li>Includes (os-dev-extras) bundle.</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/file-utils-doc">file-utils-doc</a>
        </td>
        <td class="bundlestatus">ACTIVE</td>
        <td class="bundledesc">
            <p>Provides documentation and manpages for file-utils</p>
            <li>Includes (file-utils) bundle.</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/games">games</a>
        </td>
        <td class="bundlestatus">ACTIVE</td>
        <td class="bundledesc">
            <p>A colossal, but entertaining waste of time</p>
            <li>Includes (libX11client) bundle.</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/go-basic">go-basic</a>
        </td>
        <td class="bundlestatus">ACTIVE</td>
        <td class="bundledesc">
            <p>Provides basic Go language development</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/go-extras">go-extras</a>
        </td>
        <td class="bundlestatus">ACTIVE</td>
        <td class="bundledesc">
            <p>Most popular Golang libraries</p>
            <li>Includes (go-basic) bundle.</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/hpc-basic">hpc-basic</a>
        </td>
        <td class="bundlestatus">ACTIVE</td>
        <td class="bundledesc">
            <p>Provides basic suite of MPI/HPC development tools</p>
            <li>Includes (os-core-dev) bundle.</p>
                <li>Includes (os-dev-extras) bundle.</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/internet-console-utils">internet-console-utils</a>
        </td>
        <td class="bundlestatus">WIP</td>
        <td class="bundledesc">
            <p>Includes internet console tools to interact with internet</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/internet-console-utils-dev">internet-console-utils-dev</a>
        </td>
        <td class="bundlestatus">WIP</td>
        <td class="bundledesc">
            <p>All packages required to build the internet-console-utils bundle.</p>
            <li>Includes (internet-console-utils) bundle.</p>
                <li>Includes (os-core-dev) bundle.</p>
                    <li>Includes (os-dev-extras) bundle.</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/internet-console-utils-doc">internet-console-utils-doc</a>
        </td>
        <td class="bundlestatus">WIP</td>
        <td class="bundledesc">
            <p>Provides documentation and manpages for internet-console-utils</p>
            <li>Includes (internet-console-utils) bundle.</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/iot">iot</a>
        </td>
        <td class="bundlestatus">Deprecated</td>
        <td class="bundledesc">
            <p>The IoT (Internet of Things) base bundle</p>
            <li>Includes (iot-extras) bundle.</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/iot-base">iot-base</a>
        </td>
        <td class="bundlestatus">WIP</td>
        <td class="bundledesc">
            <p>The IoT (Internet of Things) base bundle</p>
            <li>Includes (kernel-iot) bundle.</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/iot">iot</a>
        </td>
        <td class="bundlestatus"># [STATUS]:</td>
        <td class="bundledesc">
            <p>The IoT (Internet of Things) base bundle</p>
            <li>Includes (iot-base) bundle.</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/iot-extras">iot-extras</a>
        </td>
        <td class="bundlestatus">WIP</td>
        <td class="bundledesc">
            <p>The IoT (Internet of Things) base bundle</p>
            <li>Includes (iot-base) bundle.</p>
                <li>Includes (nodejs-basic) bundle.</p>
                    <li>Includes (iot-message-broker) bundle.</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/">
                </a>
        </td>
        <td class="bundlestatus"></td>
        <td class="bundledesc">
            <p></p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/java-basic">java-basic</a>
        </td>
        <td class="bundlestatus">ACTIVE</td>
        <td class="bundledesc">
            <p>Provides all openjdk tools</p>
            <li>Includes (libX11client) bundle.</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/kernel-container">kernel-container</a>
        </td>
        <td class="bundlestatus">WIP</td>
        <td class="bundledesc">
            <p>Provides a Linux kernel appropriate for a Clear Container</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/kernel-embedded">kernel-embedded</a>
        </td>
        <td class="bundlestatus">Deprecated</td>
        <td class="bundledesc">
            <p>Provides a Linux kernel appropriate for embedded devices</p>
            <li>Includes (kernel-iot) bundle.</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/kernel-hyperv">kernel-hyperv</a>
        </td>
        <td class="bundlestatus">ACTIVE</td>
        <td class="bundledesc">
            <p>Provides a Linux kernel appropriate for running under HyperV</p>
            <li>Includes (bootloader) bundle.</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/kernel-iot">kernel-iot</a>
        </td>
        <td class="bundlestatus">ACTIVE</td>
        <td class="bundledesc">
            <p>Provides a Linux kernel appropriate for iot devices</p>
            <li>Includes (bootloader) bundle.</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/kernel-kvm">kernel-kvm</a>
        </td>
        <td class="bundlestatus">ACTIVE</td>
        <td class="bundledesc">
            <p>Provides a Linux kernel appropriate for running under KVM</p>
            <li>Includes (bootloader) bundle.</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/kernel-lts">kernel-lts</a>
        </td>
        <td class="bundlestatus">ACTIVE</td>
        <td class="bundledesc">
            <p>Provides a Linux LTS kernel appropriate for physical machines</p>
            <li>Includes (bootloader) bundle.</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/kernel-native">kernel-native</a>
        </td>
        <td class="bundlestatus">ACTIVE</td>
        <td class="bundledesc">
            <p>Provides a Linux kernel appropriate for physical machines</p>
            <li>Includes (bootloader) bundle.</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/kernel-pxe">kernel-pxe</a>
        </td>
        <td class="bundlestatus">Deprecated</td>
        <td class="bundledesc">
            <p>Provides a Linux kernel linking an initramfs as root</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/koji">koji</a>
        </td>
        <td class="bundlestatus">WIP</td>
        <td class="bundledesc">
            <p>Sets up a koji build service (builder-only, for now) based on NFS mounts.</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/kvm-host">kvm-host</a>
        </td>
        <td class="bundlestatus">WIP</td>
        <td class="bundledesc">
            <p>Provides necessary tools to run usable virtual machines with QEMU-KVM (independently of OpenStack).</p>
            <li>Includes (libX11client) bundle.</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/lamp-basic">lamp-basic</a>
        </td>
        <td class="bundlestatus">ACTIVE</td>
        <td class="bundledesc">
            <p>Basic LAMP Server (apache2, mariadb, php5)</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/libX11client">libX11client</a>
        </td>
        <td class="bundlestatus">ACTIVE</td>
        <td class="bundledesc">
            <p>Provides basic client libraries for X11 applications</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/lnmp-basic">lnmp-basic</a>
        </td>
        <td class="bundlestatus">WIP</td>
        <td class="bundledesc">
            <p>Basic LNMP Server (nginx, mariadb, php5)</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/machine-learning-basic">machine-learning-basic</a>
        </td>
        <td class="bundlestatus">ACTIVE</td>
        <td class="bundledesc">
            <p>Basic components for machine learning development </p>
            <li>Includes (os-core-dev) bundle.</p>
                <li>Includes (devtools-extras) bundle.</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/mail-utils">mail-utils</a>
        </td>
        <td class="bundlestatus">WIP</td>
        <td class="bundledesc">
            <p>Provides utilities for reading and sending email</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/mail-utils-dev">mail-utils-dev</a>
        </td>
        <td class="bundlestatus">WIP</td>
        <td class="bundledesc">
            <p>All packages required to build the mail-utils bundle.</p>
            <li>Includes (mail-utils) bundle.</p>
                <li>Includes (os-core-dev) bundle.</p>
                    <li>Includes (os-dev-extras) bundle.</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/message-broker-rabbitmq">message-broker-rabbitmq</a>
        </td>
        <td class="bundlestatus">ACTIVE</td>
        <td class="bundledesc">
            <p>Provides the RabbitMQ messaging service</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/mixer">mixer</a>
        </td>
        <td class="bundlestatus">WIP</td>
        <td class="bundledesc">
            <p>Provide required utilities to make derivative releases</p>
            <li>Includes (os-clr-on-clr) bundle.</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/net-utils">net-utils</a>
        </td>
        <td class="bundlestatus">ACTIVE</td>
        <td class="bundledesc">
            <p>Provides an essential suite of core networking configuration and debug tools</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/network-advanced">network-advanced</a>
        </td>
        <td class="bundlestatus">WIP</td>
        <td class="bundledesc">
            <p>More utilities for advanced host-level networking; bridge, switch, netfilter, vpn etc.</p>
            <li>Includes (network-basic) bundle.</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/network-basic">network-basic</a>
        </td>
        <td class="bundlestatus">ACTIVE</td>
        <td class="bundledesc">
            <p>Provides a basic suite of networking utilities</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/network-basic-dev">network-basic-dev</a>
        </td>
        <td class="bundlestatus">ACTIVE</td>
        <td class="bundledesc">
            <p>All packages required to build the network-basic bundle.</p>
            <li>Includes (network-basic) bundle.</p>
                <li>Includes (os-core-dev) bundle.</p>
                    <li>Includes (os-dev-extras) bundle.</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/network-basic-doc">network-basic-doc</a>
        </td>
        <td class="bundlestatus">ACTIVE</td>
        <td class="bundledesc">
            <p>Provides documentation and manpages for network-basic</p>
            <li>Includes (network-basic) bundle.</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/network-proxy-client">network-proxy-client</a>
        </td>
        <td class="bundlestatus">WIP</td>
        <td class="bundledesc">
            <p>Tools for dealing with client-side network proxy settings.</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/network-proxy-client-dev">network-proxy-client-dev</a>
        </td>
        <td class="bundlestatus">WIP</td>
        <td class="bundledesc">
            <p>All packages required to build the network-proxy-client bundle.</p>
            <li>Includes (network-proxy-client) bundle.</p>
                <li>Includes (os-core-dev) bundle.</p>
                    <li>Includes (os-dev-extras) bundle.</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/network-proxy-client-doc">network-proxy-client-doc</a>
        </td>
        <td class="bundlestatus">WIP</td>
        <td class="bundledesc">
            <p>Provides documentation and manpages for network-proxy-client</p>
            <li>Includes (network-proxy-client) bundle.</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/nfs-utils">nfs-utils</a>
        </td>
        <td class="bundlestatus">WIP</td>
        <td class="bundledesc">
            <p>Provides NFS binaries, associated utilities, and tools. Currently only client services are fully supported.</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/nodejs-basic">nodejs-basic</a>
        </td>
        <td class="bundlestatus">ACTIVE</td>
        <td class="bundledesc">
            <p>NodeJS and associated dev tools</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/opencontainers-dev">opencontainers-dev</a>
        </td>
        <td class="bundlestatus">WIP</td>
        <td class="bundledesc">
            <p>Includes required components for developing against the Open Container Specification</p>
            <li>Includes (go-basic) bundle.</p>
                <li>Includes (network-advanced) bundle.</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/openssh-server">openssh-server</a>
        </td>
        <td class="bundlestatus">ACTIVE</td>
        <td class="bundledesc">
            <p>Provides an SSH server (and client)</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/openstack-all-in-one">openstack-all-in-one</a>
        </td>
        <td class="bundlestatus">WIP</td>
        <td class="bundledesc">
            <p>Provides an All-in-one OpenStack deployment</p>
            <li>Includes (database-mariadb) bundle.</p>
                <li>Includes (message-broker-rabbitmq) bundle.</p>
                    <li>Includes (openstack-block-storage) bundle.</p>
                        <li>Includes (openstack-block-storage-controller) bundle.</p>
                            <li>Includes (openstack-dashboard) bundle.</p>
                                <li>Includes (openstack-identity) bundle.</p>
                                    <li>Includes (openstack-image) bundle.</p>
                                        <li>Includes (openstack-object-storage) bundle.</p>
                                            <li>Includes (openstack-orchestration) bundle.</p>
                                                <li>Includes (openstack-python-clients) bundle.</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/openstack-block-storage">openstack-block-storage</a>
        </td>
        <td class="bundlestatus">WIP</td>
        <td class="bundledesc">
            <p>Provides an OpenStack Cinder service</p>
            <li>Includes (openstack-common) bundle.</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/openstack-block-storage-controller">openstack-block-storage-controller</a>
        </td>
        <td class="bundlestatus">WIP</td>
        <td class="bundledesc">
            <p>Provides an OpenStack Cinder controller service</p>
            <li>Includes (openstack-common) bundle.</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/openstack-common">openstack-common</a>
        </td>
        <td class="bundlestatus">WIP</td>
        <td class="bundledesc">
            <p>common components for OpenStack functionalit</p>
            <li>Includes (python-basic) bundle.</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/openstack-compute">openstack-compute</a>
        </td>
        <td class="bundlestatus">Deprecated</td>
        <td class="bundledesc">
            <p>Provides an OpenStack nova-compute node</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/openstack-compute-controller">openstack-compute-controller</a>
        </td>
        <td class="bundlestatus">Deprecated</td>
        <td class="bundledesc">
            <p>Provides an OpenStack Nova control server</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/openstack-configure">openstack-configure</a>
        </td>
        <td class="bundlestatus">Deprecated</td>
        <td class="bundledesc">
            <p>Provides a suggested default configuration for OpenStack on Clear Linux.</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/openstack-controller">openstack-controller</a>
        </td>
        <td class="bundlestatus">Deprecated</td>
        <td class="bundledesc">
            <p>Provides an OpenStack multi-service control server</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/openstack-dashboard">openstack-dashboard</a>
        </td>
        <td class="bundlestatus">WIP</td>
        <td class="bundledesc">
            <p>Provides an OpenStack Horizon server</p>
            <li>Includes (openstack-common) bundle.</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/openstack-database">openstack-database</a>
        </td>
        <td class="bundlestatus">Deprecated</td>
        <td class="bundledesc">
            <p>Provides a Database as a Service server</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/openstack-data-processing">openstack-data-processing</a>
        </td>
        <td class="bundlestatus">Deprecated</td>
        <td class="bundledesc">
            <p>Provides a simple means to provision a data-intensive application cluster </p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/openstack-identity">openstack-identity</a>
        </td>
        <td class="bundlestatus">WIP</td>
        <td class="bundledesc">
            <p>Provides an OpenStack Keystone server</p>
            <li>Includes (openstack-common) bundle.</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/openstack-image">openstack-image</a>
        </td>
        <td class="bundlestatus">WIP</td>
        <td class="bundledesc">
            <p>Provides an OpenStack Glance server</p>
            <li>Includes (openstack-common) bundle.</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/openstack-lbaas">openstack-lbaas</a>
        </td>
        <td class="bundlestatus">Deprecated</td>
        <td class="bundledesc">
            <p>Provides Load Balancing as a Service</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/openstack-network">openstack-network</a>
        </td>
        <td class="bundlestatus">Deprecated</td>
        <td class="bundledesc">
            <p>Provides an OpenStack Neutron server</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/openstack-object-storage">openstack-object-storage</a>
        </td>
        <td class="bundlestatus">WIP</td>
        <td class="bundledesc">
            <p>Provides an OpenStack Swift service</p>
            <li>Includes (openstack-common) bundle.</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/openstack-orchestration">openstack-orchestration</a>
        </td>
        <td class="bundlestatus">WIP</td>
        <td class="bundledesc">
            <p>Provides an OpenStack Heat service</p>
            <li>Includes (openstack-common) bundle.</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/openstack-python-clients">openstack-python-clients</a>
        </td>
        <td class="bundlestatus">WIP</td>
        <td class="bundledesc">
            <p>Provides OpenStack command-line utilities</p>
            <li>Includes (openstack-common) bundle.</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/openstack-telemetry">openstack-telemetry</a>
        </td>
        <td class="bundlestatus">Deprecated</td>
        <td class="bundledesc">
            <p>Provides an OpenStack Telemetry server</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/openstack-telemetry-controller">openstack-telemetry-controller</a>
        </td>
        <td class="bundlestatus">Deprecated</td>
        <td class="bundledesc">
            <p>Provides an OpenStack Telemetry server</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/openstack-test-suite">openstack-test-suite</a>
        </td>
        <td class="bundlestatus">WIP</td>
        <td class="bundledesc">
            <p>Provides an OpenStack Tempest/test suite </p>
            <li>Includes (openstack-common) bundle.</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/openstack-vpnaas">openstack-vpnaas</a>
        </td>
        <td class="bundlestatus">Deprecated</td>
        <td class="bundledesc">
            <p>Provides VPN as a Service</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/os-cloudguest">os-cloudguest</a>
        </td>
        <td class="bundlestatus">WIP</td>
        <td class="bundledesc">
            <p>Provides clr-cloud-init cloud guest configuration utilities</p>
            <li>Includes (openssh-server) bundle.</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/os-cloudguest-azure">os-cloudguest-azure</a>
        </td>
        <td class="bundlestatus">WIP</td>
        <td class="bundledesc">
            <p>Basic requirements for a cloud guest image on MS Azure</p>
            <li>Includes (openssh-server) bundle.</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/os-cloudguest-cci">os-cloudguest-cci</a>
        </td>
        <td class="bundlestatus">WIP</td>
        <td class="bundledesc">
            <p>Retired bundle - now provided by os-cloudguest</p>
            <li>Includes (os-cloudguest) bundle.</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/os-clr-on-clr">os-clr-on-clr</a>
        </td>
        <td class="bundlestatus">WIP</td>
        <td class="bundledesc">
            <p>content for development of the Clear Linux OS on the Clear Linux OS</p>
            <li>Includes (os-core-dev) bundle.</p>
                <li>Includes (os-dev-extras) bundle.</p>
                    <li>Includes (mail-utils) bundle.</p>
                        <li>Includes (storage-utils) bundle.</p>
                            <li>Includes (os-core-update) bundle.</p>
                                <li>Includes (python-basic) bundle.</p>
                                    <li>Includes (perl-basic) bundle.</p>
                                        <li>Includes (os-utils) bundle.</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/os-clr-on-clr-dev">os-clr-on-clr-dev</a>
        </td>
        <td class="bundlestatus">WIP</td>
        <td class="bundledesc">
            <p>All packages required to build the os-clr-on-clr bundle.</p>
            <li>Includes (os-clr-on-clr) bundle.</p>
                <li>Includes (os-core-dev) bundle.</p>
                    <li>Includes (os-dev-extras) bundle.</p>
                        <li>Includes (mail-utils) bundle.</p>
                            <li>Includes (storage-utils) bundle.</p>
                                <li>Includes (os-core-update) bundle.</p>
                                    <li>Includes (python-basic) bundle.</p>
                                        <li>Includes (perl-basic) bundle.</p>
                                            <li>Includes (os-utils) bundle.</p>
                                                <li>Includes (mail-utils-dev) bundle.</p>
                                                    <li>Includes (storage-utils-dev) bundle.</p>
                                                        <li>Includes (os-core-update-dev) bundle.</p>
                                                            <li>Includes (python-basic-dev) bundle.</p>
                                                                <li>Includes (perl-basic-dev) bundle.</p>
                                                                    <li>Includes (os-utils-dev) bundle.</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/os-core">os-core</a>
        </td>
        <td class="bundlestatus">ACTIVE</td>
        <td class="bundledesc">
            <p>The basic core OS components of Clear Linux for iA </p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/os-core-dev">os-core-dev</a>
        </td>
        <td class="bundlestatus">ACTIVE</td>
        <td class="bundledesc">
            <p>All packages required to build the os-core bundle.</p>
            <li>Includes (os-core) bundle.</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/os-core-doc">os-core-doc</a>
        </td>
        <td class="bundlestatus">ACTIVE</td>
        <td class="bundledesc">
            <p>Provides documentation and manpages for os-core</p>
            <li>Includes (os-core) bundle.</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/os-core-update">os-core-update</a>
        </td>
        <td class="bundlestatus">ACTIVE</td>
        <td class="bundledesc">
            <p>Provides basic suite for running the Clear Linux for iA Updater</p>
            <li>Includes (os-core) bundle.</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/os-core-update-dev">os-core-update-dev</a>
        </td>
        <td class="bundlestatus">ACTIVE</td>
        <td class="bundledesc">
            <p>All packages required to build the os-core-update bundle.</p>
            <li>Includes (os-core-update) bundle.</p>
                <li>Includes (os-core-dev) bundle.</p>
                    <li>Includes (os-dev-extras) bundle.</p>
                        <li>Includes (os-core) bundle.</p>
                            <li>Includes (os-core-dev) bundle.</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/os-dev-extras">os-dev-extras</a>
        </td>
        <td class="bundlestatus">ACTIVE</td>
        <td class="bundledesc">
            <p>Development utilities and helpful base Linux dev environment tools</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/os-dev-full">os-dev-full</a>
        </td>
        <td class="bundlestatus">WIP</td>
        <td class="bundledesc">
            <p>A bundle containing all development libraries and headers</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/os-installer">os-installer</a>
        </td>
        <td class="bundlestatus">ACTIVE</td>
        <td class="bundledesc">
            <p>Provides an installer for Clear Linux for iA</p>
            <li>Includes (telemetrics) bundle.</p>
                <li>Includes (network-proxy-client) bundle.</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/os-testsuite">os-testsuite</a>
        </td>
        <td class="bundlestatus">WIP</td>
        <td class="bundledesc">
            <p>Provides basic test suite for Clear Linux for iA</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/os-testsuite-phoronix">os-testsuite-phoronix</a>
        </td>
        <td class="bundlestatus">ACTIVE</td>
        <td class="bundledesc">
            <p>All the required pieces for running the Phoronix Test Suite</p>
            <li>Includes (os-utils-gui) bundle.</p>
                <li>Includes (devtools-extras) bundle.</p>
                    <li>Includes (lamp-basic) bundle.</p>
                        <li>Includes (machine-learning-basic) bundle.</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/os-utils">os-utils</a>
        </td>
        <td class="bundlestatus">ACTIVE</td>
        <td class="bundledesc">
            <p>Provides a core set of OS utilities</p>
            <li>Includes (editors) bundle.</p>
                <li>Includes (dev-utils) bundle.</p>
                    <li>Includes (sysadmin-basic) bundle.</p>
                        <li>Includes (network-basic) bundle.</p>
                            <li>Includes (file-utils) bundle.</p>
                                <li>Includes (network-proxy-client) bundle.</p>
                                    <li>Includes (internet-console-utils) bundle.</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/os-utils-dev">os-utils-dev</a>
        </td>
        <td class="bundlestatus">ACTIVE</td>
        <td class="bundledesc">
            <p>All packages required to build the os-utils bundle.</p>
            <li>Includes (os-utils) bundle.</p>
                <li>Includes (os-core-dev) bundle.</p>
                    <li>Includes (os-dev-extras) bundle.</p>
                        <li>Includes (editors) bundle.</p>
                            <li>Includes (dev-utils) bundle.</p>
                                <li>Includes (sysadmin-basic) bundle.</p>
                                    <li>Includes (network-basic) bundle.</p>
                                        <li>Includes (file-utils) bundle.</p>
                                            <li>Includes (network-proxy-client) bundle.</p>
                                                <li>Includes (internet-console-utils) bundle.</p>
                                                    <li>Includes (editors-dev) bundle.</p>
                                                        <li>Includes (dev-utils-dev) bundle.</p>
                                                            <li>Includes (sysadmin-basic-dev) bundle.</p>
                                                                <li>Includes (network-basic-dev) bundle.</p>
                                                                    <li>Includes (file-utils-dev) bundle.</p>
                                                                        <li>Includes (network-proxy-client-dev) bundle.</p>
                                                                            <li>Includes (internet-console-utils-dev) bundle.</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/os-utils-doc">os-utils-doc</a>
        </td>
        <td class="bundlestatus">ACTIVE</td>
        <td class="bundledesc">
            <p>Provides documentation and manpages for os-utils</p>
            <li>Includes (os-utils) bundle.</p>
                <li>Includes (editors-doc) bundle.</p>
                    <li>Includes (dev-utils-doc) bundle.</p>
                        <li>Includes (sysadmin-basic-doc) bundle.</p>
                            <li>Includes (network-basic-doc) bundle.</p>
                                <li>Includes (file-utils-doc) bundle.</p>
                                    <li>Includes (network-proxy-client-doc) bundle.</p>
                                        <li>Includes (internet-console-utils-doc) bundle.</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/os-utils-gui">os-utils-gui</a>
        </td>
        <td class="bundlestatus">ACTIVE</td>
        <td class="bundledesc">
            <p>Provides a graphical desktop environment </p>
            <li>Includes (os-utils) bundle.</p>
                <li>Includes (python-basic) bundle.</p>
                    <li>Includes (xfce4-desktop) bundle.</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/perl-basic">perl-basic</a>
        </td>
        <td class="bundlestatus">ACTIVE</td>
        <td class="bundledesc">
            <p>Provides essential Perl language and dev tools</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/perl-basic-dev">perl-basic-dev</a>
        </td>
        <td class="bundlestatus">ACTIVE</td>
        <td class="bundledesc">
            <p>All packages required to build the perl-basic bundle.</p>
            <li>Includes (perl-basic) bundle.</p>
                <li>Includes (os-core-dev) bundle.</p>
                    <li>Includes (os-dev-extras) bundle.</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/perl-extras">perl-extras</a>
        </td>
        <td class="bundlestatus">ACTIVE</td>
        <td class="bundledesc">
            <p>Provides extra libraries for Perl</p>
            <li>Includes (perl-basic) bundle.</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/pnp-tools-advanced">pnp-tools-advanced</a>
        </td>
        <td class="bundlestatus">WIP</td>
        <td class="bundledesc">
            <p>Provides advanced Power and Performance measurement tools</p>
            <li>Includes (pnp-tools-intermediate) bundle.</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/pnp-tools-basic">pnp-tools-basic</a>
        </td>
        <td class="bundlestatus">WIP</td>
        <td class="bundledesc">
            <p>Provides basic Power and Performance testing tools</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/pnp-tools-intermediate">pnp-tools-intermediate</a>
        </td>
        <td class="bundlestatus">WIP</td>
        <td class="bundledesc">
            <p>Provides a deeper-level suite of Power and Performance testing tools</p>
            <li>Includes (pnp-tools-basic) bundle.</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/pxe-server">pxe-server</a>
        </td>
        <td class="bundlestatus">ACTIVE</td>
        <td class="bundledesc">
            <p>All the bits to run a PXE server for Clear Linux</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/python-basic">python-basic</a>
        </td>
        <td class="bundlestatus">ACTIVE</td>
        <td class="bundledesc">
            <p>Provides core Python language and libraries</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/python-basic-dev">python-basic-dev</a>
        </td>
        <td class="bundlestatus">ACTIVE</td>
        <td class="bundledesc">
            <p>All packages required to build the python-basic bundle.</p>
            <li>Includes (python-basic) bundle.</p>
                <li>Includes (os-core-dev) bundle.</p>
                    <li>Includes (os-dev-extras) bundle.</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/python-extras">python-extras</a>
        </td>
        <td class="bundlestatus">ACTIVE</td>
        <td class="bundledesc">
            <p>Provides extra libraries for Python</p>
            <li>Includes (python-basic) bundle.</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/R-basic">R-basic</a>
        </td>
        <td class="bundlestatus">ACTIVE</td>
        <td class="bundledesc">
            <p>Provides core R language and libraries</p>
            <li>Includes (libX11client) bundle.</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/R-extras">R-extras</a>
        </td>
        <td class="bundlestatus">ACTIVE</td>
        <td class="bundledesc">
            <p>Provides deeper functionality R language libraries</p>
            <li>Includes (R-basic) bundle.</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/ruby-basic">ruby-basic</a>
        </td>
        <td class="bundlestatus">ACTIVE</td>
        <td class="bundledesc">
            <p>Top 3 basic Ruby Libraries</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/ruby-extras">ruby-extras</a>
        </td>
        <td class="bundlestatus">ACTIVE</td>
        <td class="bundledesc">
            <p>Top 3 to 6 basic Ruby Libraries</p>
            <li>Includes (ruby-basic) bundle.</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/rust-basic">rust-basic</a>
        </td>
        <td class="bundlestatus">ACTIVE</td>
        <td class="bundledesc">
            <p>rust compiler and cargo packaging tool</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/shells">shells</a>
        </td>
        <td class="bundlestatus">ACTIVE</td>
        <td class="bundledesc">
            <p>All available shell programs for Clear, along with ancillary files</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/storage-cluster">storage-cluster</a>
        </td>
        <td class="bundlestatus">WIP</td>
        <td class="bundledesc">
            <p>Ceph Cluster Storage</p>
            <li>Includes (storage-utils) bundle.</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/storage-utils">storage-utils</a>
        </td>
        <td class="bundlestatus">ACTIVE</td>
        <td class="bundledesc">
            <p>Provides basic storage-related utilities</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/storage-utils-dev">storage-utils-dev</a>
        </td>
        <td class="bundlestatus">ACTIVE</td>
        <td class="bundledesc">
            <p>All packages required to build the storage-utils bundle.</p>
            <li>Includes (storage-utils) bundle.</p>
                <li>Includes (os-core-dev) bundle.</p>
                    <li>Includes (os-dev-extras) bundle.</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/sysadmin">sysadmin</a>
        </td>
        <td class="bundlestatus">ACTIVE</td>
        <td class="bundledesc">
            <p>Moved to sysadmin-basic</p>
            <li>Includes (sysadmin-basic) bundle.</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/sysadmin-advanced">sysadmin-advanced</a>
        </td>
        <td class="bundlestatus">ACTIVE</td>
        <td class="bundledesc">
            <p>Toolchest that a sysadmin needs to diagnose issues</p>
            <li>Includes (sysadmin-basic) bundle.</p>
                <li>Includes (pnp-tools-advanced) bundle.</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/sysadmin-basic">sysadmin-basic</a>
        </td>
        <td class="bundlestatus">ACTIVE</td>
        <td class="bundledesc">
            <p>Provides a basic set of system administration utilities.</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/sysadmin-basic-dev">sysadmin-basic-dev</a>
        </td>
        <td class="bundlestatus">ACTIVE</td>
        <td class="bundledesc">
            <p>All packages required to build the sysadmin-basic bundle.</p>
            <li>Includes (sysadmin-basic) bundle.</p>
                <li>Includes (os-core-dev) bundle.</p>
                    <li>Includes (os-dev-extras) bundle.</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/sysadmin-basic-doc">sysadmin-basic-doc</a>
        </td>
        <td class="bundlestatus">ACTIVE</td>
        <td class="bundledesc">
            <p>Provides documentation and manpages for sysadmin-basic</p>
            <li>Includes (sysadmin-basic) bundle.</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/sysadmin-hostmgmt">sysadmin-hostmgmt</a>
        </td>
        <td class="bundlestatus">WIP</td>
        <td class="bundledesc">
            <p>Utilities and Services for managing large-scale clusters of networked hosts</p>
            <li>Includes (os-utils) bundle.</p>
                <li>Includes (pxe-server) bundle.</p>
                    <li>Includes (python-basic) bundle.</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/tcl-basic">tcl-basic</a>
        </td>
        <td class="bundlestatus">WIP</td>
        <td class="bundledesc">
            <p>Components related to the TCL interpreter and associated tools</p>
            <li>Includes (libX11client) bundle.</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/telemetrics">telemetrics</a>
        </td>
        <td class="bundlestatus">ACTIVE</td>
        <td class="bundledesc">
            <p>Provides the Telemetrics client for Clear Linux for iA</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/virtualbox-guest">virtualbox-guest</a>
        </td>
        <td class="bundlestatus">ACTIVE</td>
        <td class="bundledesc">
            <p>Include the modules and binaries meant to be used as a VirtualBox instance</p>
            <li>Includes (kernel-lts) bundle.</p>
        </td>
    </tr>
    <tr>
        <td class="bundlename">
            <a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/xfce4-desktop">xfce4-desktop</a>
        </td>
        <td class="bundlestatus">ACTIVE</td>
        <td class="bundledesc">
            <p>Provides the XFCE4 graphical desktop environment </p>
            <li>Includes (libX11client) bundle.</p>
        </td>
    </tr>
    </table>

