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
the upstream open source projects are needed for this functionality.


To see a list of currently-installed bundles
============================================

.. code-block:: console

   # ls /usr/share/clear/bundles



To see the list of optional bundles you can install
===================================================

.. code-block:: console

   # swupd bundle-add --list


To add a bundle
===============

.. code-block:: console

   # swupd bundle-add [bundle name]




Current list of available bundles as of ``[[12 October 2016]]``.

.. raw:: html

  <head>
	<title>Bundles in Clear Linux OS for Intel® Architecture</title>
	  <style type="text/css">
  		table { margin: 2em; border: 1px solid #e0e0e0; border-collapse: collapse; width: auto; }
  		th { align: center; padding: 0.33em; border: #ccc solid 1px; background-color: #555; color: #fff; text-transform: uppercase; font-size: 1.21em }
  		tbody tr:nth-child(odd) { background-color:#e0e0e0; }
  	    .bundlename { font-family: monospace; font-size: 1.13em; font-weight: bolder; padding-left: 0.42em;}
  	    .bundlestatus { font-family: sans; font-weight: lighter;  }
  	    .bundledesc { font-size: 0.93em; line-height: 0.88em; font-family: sans; }
  		li, ul { margin-left: 0.53em; padding-left: 0.23em; }
		</style>
	</head>

  <table>
    <thead>
    <tr>
      <th align=left>Bundle Name</th>
      <th align=center>Status</th>
      <th align=left>Description</th>
    </tr>
    </thead>
    <tbody>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/bat">bat</a></td>
      <td class="bundlestatus">Deprecated</td>
      <td class="bundledesc"><p>Provides the neccesary bundles to perform BAT succesfully</p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/bootloader">bootloader</a></td>
      <td class="bundlestatus">Active</td>
      <td class="bundledesc"><p>Loads kernel from disk and boots the system</p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/c-basic">c-basic</a></td>
      <td class="bundlestatus">Active</td>
      <td class="bundledesc"><p>Build and run C/C++ language programs</p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/cloud-control">cloud-control</a></td>
      <td class="bundlestatus">Active</td>
      <td class="bundledesc"><p>Run a cloud orchestration server
          <li>Includes (kvm-host) bundle.</li>
          <li>Includes (network-basic) bundle.</li></p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/cloud-dashboard">cloud-dashboard</a></td>
      <td class="bundlestatus">Active</td>
      <td class="bundledesc"><p>Run web-based UI for a cloud scheduler service
          <li>Includes (nodejs-basic) bundle.</li></p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/cloud-network">cloud-network</a></td>
      <td class="bundlestatus">Deprecated</td>
      <td class="bundledesc"><p>Support for cloud networking agents
          <li>Includes (openssh-server) bundle.</li>
          <li>Includes (network-basic) bundle.</li></p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/clr-devops">clr-devops</a></td>
      <td class="bundlestatus">Active</td>
      <td class="bundledesc"><p>Run all Clear Linux devops workloads
          <li>Includes (os-installer) bundle.</li>
          <li>Includes (os-core-update) bundle.</li>
          <li>Includes (mixer) bundle.</li>
          <li>Includes (java-basic) bundle.</li>
          <li>Includes (rust-basic) bundle.</li></p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/containers-basic">containers-basic</a></td>
      <td class="bundlestatus">Active</td>
      <td class="bundledesc"><p>Run container applications from Dockerhub
          <li>Includes (kernel-container) bundle.</li>
          <li>Includes (network-basic) bundle.</li>
          <li>Includes (storage-utils) bundle.</li></p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/containers-basic-dev">containers-basic-dev</a></td>
      <td class="bundlestatus">Active</td>
      <td class="bundledesc"><p>All packages required to build the containers-basic bundle.
          <li>Includes (containers-basic) bundle.</li>
          <li>Includes (os-core-dev) bundle.</li>
          <li>Includes (os-dev-extras) bundle.</li>
          <li>Includes (kernel-container) bundle.</li>
          <li>Includes (network-basic) bundle.</li>
          <li>Includes (storage-utils) bundle.</li>
          <li>Includes (network-basic-dev) bundle.</li>
          <li>Includes (storage-utils-dev) bundle.</li></p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/cryptography">cryptography</a></td>
      <td class="bundlestatus">Active</td>
      <td class="bundledesc"><p>Encrypt, decrypt, sign and verify objects</p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/database-basic">database-basic</a></td>
      <td class="bundlestatus">Active</td>
      <td class="bundledesc"><p>Run a SQL database</p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/database-mariadb">database-mariadb</a></td>
      <td class="bundlestatus">Deprecated</td>
      <td class="bundledesc"><p>Provides components needed to run MariaDB</p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/database-mariadb-dev">database-mariadb-dev</a></td>
      <td class="bundlestatus">Deprecated</td>
      <td class="bundledesc"><p>Provides MariaDB development tools (libraries and drivers)</p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/database-mongodb">database-mongodb</a></td>
      <td class="bundlestatus">Deprecated</td>
      <td class="bundledesc"><p>Provides components needed to run mongodb</p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/devtools-basic">devtools-basic</a></td>
      <td class="bundlestatus">Deprecated</td>
      <td class="bundledesc"><p>Provides basic set of languages and tools for development</p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/devtools-extras">devtools-extras</a></td>
      <td class="bundlestatus">Deprecated</td>
      <td class="bundledesc"><p>Provides extra set of languages and tools for development</p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/dev-utils">dev-utils</a></td>
      <td class="bundlestatus">Active</td>
      <td class="bundledesc"><p>Assist application development</p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/dev-utils-dev">dev-utils-dev</a></td>
      <td class="bundlestatus">Active</td>
      <td class="bundledesc"><p>All packages required to build the dev-utils bundle.
          <li>Includes (dev-utils) bundle.</li>
          <li>Includes (os-core-dev) bundle.</li>
          <li>Includes (os-dev-extras) bundle.</li></p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/dev-utils-doc">dev-utils-doc</a></td>
      <td class="bundlestatus">Active</td>
      <td class="bundledesc"><p>Provides documentation and manpages for dev-utils
          <li>Includes (dev-utils) bundle.</li></p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/dpdk-dev">dpdk-dev</a></td>
      <td class="bundlestatus">Deprecated</td>
      <td class="bundledesc"><p>All headers and libraries necessary to develop with the Data Plane Development Kit.</p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/editors">editors</a></td>
      <td class="bundlestatus">Active</td>
      <td class="bundledesc"><p>Run popular terminal text editors
          <li>Includes (python-basic) bundle.</li></p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/editors-dev">editors-dev</a></td>
      <td class="bundlestatus">Active</td>
      <td class="bundledesc"><p>All packages required to build the editors bundle.
          <li>Includes (editors) bundle.</li>
          <li>Includes (os-core-dev) bundle.</li>
          <li>Includes (os-dev-extras) bundle.</li>
          <li>Includes (python-basic) bundle.</li>
          <li>Includes (python-basic-dev) bundle.</li></p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/editors-doc">editors-doc</a></td>
      <td class="bundlestatus">Active</td>
      <td class="bundledesc"><p>Provides documentation and manpages for editors
          <li>Includes (editors) bundle.</li></p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/file-utils">file-utils</a></td>
      <td class="bundlestatus">Deprecated</td>
      <td class="bundledesc"><p>Provides basic set of file manipulation utilities</p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/file-utils-dev">file-utils-dev</a></td>
      <td class="bundlestatus">Deprecated</td>
      <td class="bundledesc"><p>All packages required to build the file-utils bundle.</p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/file-utils-doc">file-utils-doc</a></td>
      <td class="bundlestatus">Deprecated</td>
      <td class="bundledesc"><p>Provides documentation and manpages for file-utils</p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/games">games</a></td>
      <td class="bundlestatus">Active</td>
      <td class="bundledesc"><p>Play games in Clear Linux
          <li>Includes (libX11client) bundle.</li></p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/go-basic">go-basic</a></td>
      <td class="bundlestatus">Active</td>
      <td class="bundledesc"><p>Build and run go language programs</p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/go-basic-dev">go-basic-dev</a></td>
      <td class="bundlestatus">Active</td>
      <td class="bundledesc"><p>All packages required to build the go-basic bundle.
          <li>Includes (go-basic) bundle.</li>
          <li>Includes (os-core-dev) bundle.</li>
          <li>Includes (os-dev-extras) bundle.</li></p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/go-extras">go-extras</a></td>
      <td class="bundlestatus">Active</td>
      <td class="bundledesc"><p>Improve the user experience with a common set of go libraries
          <li>Includes (go-basic) bundle.</li></p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/hpc-basic">hpc-basic</a></td>
      <td class="bundlestatus">Deprecated</td>
      <td class="bundledesc"><p>Provides basic suite of MPI/HPC development tools</p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/internet-console-utils">internet-console-utils</a></td>
      <td class="bundlestatus">Deprecated</td>
      <td class="bundledesc"><p>Includes internet console tools to interact with internet</p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/internet-console-utils-dev">internet-console-utils-dev</a></td>
      <td class="bundlestatus">Deprecated</td>
      <td class="bundledesc"><p>All packages required to build the internet-console-utils bundle.</p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/internet-console-utils-doc">internet-console-utils-doc</a></td>
      <td class="bundlestatus">Deprecated</td>
      <td class="bundledesc"><p>Provides documentation and manpages for internet-console-utils</p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/iot">iot</a></td>
      <td class="bundlestatus">Deprecated</td>
      <td class="bundledesc"><p>The IoT (Internet of Things) base bundle
          <li>Includes (iot-extras) bundle.</li></p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/iot-base">iot-base</a></td>
      <td class="bundlestatus">WIP</td>
      <td class="bundledesc"><p>The IoT (Internet of Things) base bundle
          <li>Includes (kernel-iot) bundle.</li></p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/iot-dev">iot-dev</a></td>
      <td class="bundlestatus">Deprecated</td>
      <td class="bundledesc"><p>The IoT (Internet of Things) base bundle</p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/iot-extras">iot-extras</a></td>
      <td class="bundlestatus">WIP</td>
      <td class="bundledesc"><p>The IoT (Internet of Things) base bundle
          <li>Includes (iot-base) bundle.</li>
          <li>Includes (nodejs-basic) bundle.</li></p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/iot-message-broker">iot-message-broker</a></td>
      <td class="bundlestatus">Deprecated</td>
      <td class="bundledesc"><p>Unknown bundle</p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/java-basic">java-basic</a></td>
      <td class="bundlestatus">Active</td>
      <td class="bundledesc"><p>Build and run java language programs
          <li>Includes (libX11client) bundle.</li></p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/kernel-container">kernel-container</a></td>
      <td class="bundlestatus">Active</td>
      <td class="bundledesc"><p>Run the container specific kernel</p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/kernel-embedded">kernel-embedded</a></td>
      <td class="bundlestatus">Deprecated</td>
      <td class="bundledesc"><p>Provides a Linux kernel appropriate for embedded devices
          <li>Includes (kernel-iot) bundle.</li></p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/kernel-hyperv">kernel-hyperv</a></td>
      <td class="bundlestatus">Active</td>
      <td class="bundledesc"><p>Run the hyperv specific kernel
          <li>Includes (bootloader) bundle.</li></p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/kernel-iot">kernel-iot</a></td>
      <td class="bundlestatus">Active</td>
      <td class="bundledesc"><p>Run the iot specific kernel
          <li>Includes (bootloader) bundle.</li></p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/kernel-kvm">kernel-kvm</a></td>
      <td class="bundlestatus">Active</td>
      <td class="bundledesc"><p>Run the kvm specific kernel
          <li>Includes (bootloader) bundle.</li></p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/kernel-lts">kernel-lts</a></td>
      <td class="bundlestatus">Active</td>
      <td class="bundledesc"><p>Run the lts native kernel
          <li>Includes (bootloader) bundle.</li></p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/kernel-native">kernel-native</a></td>
      <td class="bundlestatus">Active</td>
      <td class="bundledesc"><p>Run the native kernel
          <li>Includes (bootloader) bundle.</li></p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/kernel-pxe">kernel-pxe</a></td>
      <td class="bundlestatus">Deprecated</td>
      <td class="bundledesc"><p>Provides a Linux kernel linking an initramfs as root</p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/koji">koji</a></td>
      <td class="bundlestatus">WIP</td>
      <td class="bundledesc"><p>Sets up a koji build service (builder-only, for now) based on NFS mounts.</p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/kvm-host">kvm-host</a></td>
      <td class="bundlestatus">Active</td>
      <td class="bundledesc"><p>Run virtual machines
          <li>Includes (libX11client) bundle.</li></p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/lamp-basic">lamp-basic</a></td>
      <td class="bundlestatus">Deprecated</td>
      <td class="bundledesc"><p>Basic LAMP Server (apache2, mariadb, php5)
          <li>Includes (database-basic) bundle.</li>
          <li>Includes (php-basic) bundle.</li>
          <li>Includes (web-server-basic) bundle.</li></p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/libX11client">libX11client</a></td>
      <td class="bundlestatus">Active</td>
      <td class="bundledesc"><p>Grouping only bundle for use in X using bundles</p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/lnmp-basic">lnmp-basic</a></td>
      <td class="bundlestatus">Deprecated</td>
      <td class="bundledesc"><p>Basic LNMP Server (nginx, mariadb, php5)
          <li>Includes (database-basic) bundle.</li>
          <li>Includes (php-basic) bundle.</li>
          <li>Includes (web-server-basic) bundle.</li></p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/machine-learning-basic">machine-learning-basic</a></td>
      <td class="bundlestatus">Active</td>
      <td class="bundledesc"><p>Build machine learning applications
          <li>Includes (c-basic) bundle.</li>
          <li>Includes (python-extras) bundle.</li></p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/mail-utils">mail-utils</a></td>
      <td class="bundlestatus">Active</td>
      <td class="bundledesc"><p>Process, read and send email</p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/mail-utils-dev">mail-utils-dev</a></td>
      <td class="bundlestatus">Active</td>
      <td class="bundledesc"><p>All packages required to build the mail-utils bundle.
          <li>Includes (mail-utils) bundle.</li>
          <li>Includes (os-core-dev) bundle.</li>
          <li>Includes (os-dev-extras) bundle.</li></p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/message-broker-rabbitmq">message-broker-rabbitmq</a></td>
      <td class="bundlestatus">Deprecated</td>
      <td class="bundledesc"><p>Provides the RabbitMQ messaging service</p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/mixer">mixer</a></td>
      <td class="bundlestatus">Active</td>
      <td class="bundledesc"><p>Create Clear Linux releases
          <li>Includes (python-basic) bundle.</li>
          <li>Includes (sysadmin-basic) bundle.</li></p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/net-utils">net-utils</a></td>
      <td class="bundlestatus">Deprecated</td>
      <td class="bundledesc"><p>Provides an essential suite of core networking configuration and debug tools</p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/network-advanced">network-advanced</a></td>
      <td class="bundlestatus">Deprecated</td>
      <td class="bundledesc"><p>More utilities for advanced host-level networking; bridge, switch, netfilter, vpn etc.</p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/network-basic">network-basic</a></td>
      <td class="bundlestatus">Active</td>
      <td class="bundledesc"><p>Run network utilities and modify network settings
          <li>Includes # bundle.</li>
          <li>Includes TODO bundle.</li>
          <li>Includes remove bundle.</li>
          <li>Includes openssh-server bundle.</li>
          <li>Includes for bundle.</li>
          <li>Includes format bundle.</li>
          <li>Includes change bundle.</li>
          <li>Includes # bundle.</li>
          <li>Includes perl-basic bundle.</li>
          <li>Includes and bundle.</li>
          <li>Includes tcl-basic bundle.</li>
          <li>Includes d bundle.</li>
          <li>Includes to bundle.</li>
          <li>Includes avoid bundle.</li>
          <li>Includes duplication bundle.</li>
          <li>Includes (openssh-server) bundle.</li>
          <li>Includes (perl-basic) bundle.</li>
          <li>Includes (tcl-basic) bundle.</li></p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/network-basic-dev">network-basic-dev</a></td>
      <td class="bundlestatus">Active</td>
      <td class="bundledesc"><p>All packages required to build the network-basic bundle.
          <li>Includes (network-basic) bundle.</li>
          <li>Includes (os-core-dev) bundle.</li>
          <li>Includes (os-dev-extras) bundle.</li>
          <li>Includes (openssh-server) bundle.</li>
          <li>Includes (perl-basic) bundle.</li>
          <li>Includes (tcl-basic) bundle.</li>
          <li>Includes (perl-basic-dev) bundle.</li></p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/network-basic-doc">network-basic-doc</a></td>
      <td class="bundlestatus">Active</td>
      <td class="bundledesc"><p>Provides documentation and manpages for network-basic
          <li>Includes (network-basic) bundle.</li></p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/network-proxy-client">network-proxy-client</a></td>
      <td class="bundlestatus">Deprecated</td>
      <td class="bundledesc"><p>Tools for dealing with client-side network proxy settings.</p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/network-proxy-client-dev">network-proxy-client-dev</a></td>
      <td class="bundlestatus">Deprecated</td>
      <td class="bundledesc"><p>All packages required to build the network-proxy-client bundle.</p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/network-proxy-client-doc">network-proxy-client-doc</a></td>
      <td class="bundlestatus">Deprecated</td>
      <td class="bundledesc"><p>Provides documentation and manpages for network-proxy-client</p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/nfs-utils">nfs-utils</a></td>
      <td class="bundlestatus">Active</td>
      <td class="bundledesc"><p>Run an NFS client</p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/nodejs-basic">nodejs-basic</a></td>
      <td class="bundlestatus">Active</td>
      <td class="bundledesc"><p>Run javascript server side</p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/opencontainers-dev">opencontainers-dev</a></td>
      <td class="bundlestatus">Deprecated</td>
      <td class="bundledesc"><p>Includes required components for developing against the Open Container Specification</p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/openssh-server">openssh-server</a></td>
      <td class="bundlestatus">Active</td>
      <td class="bundledesc"><p>Run an ssh server</p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/openstack-all-in-one">openstack-all-in-one</a></td>
      <td class="bundlestatus">Deprecated</td>
      <td class="bundledesc"><p>Provides an All-in-one OpenStack deployment</p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/openstack-block-storage">openstack-block-storage</a></td>
      <td class="bundlestatus">Deprecated</td>
      <td class="bundledesc"><p>Run openstack block storage service</p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/openstack-block-storage-controller">openstack-block-storage-controller</a></td>
      <td class="bundlestatus">Deprecated</td>
      <td class="bundledesc"><p>Run openstack block storage controller service</p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/openstack-common">openstack-common</a></td>
      <td class="bundlestatus">Active</td>
      <td class="bundledesc"><p>Grouping bundle used by all openstack using bundles
          <li>Includes (python-basic) bundle.</li></p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/openstack-compute">openstack-compute</a></td>
      <td class="bundlestatus">Deprecated</td>
      <td class="bundledesc"><p>Provides an OpenStack nova-compute node</p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/openstack-compute-controller">openstack-compute-controller</a></td>
      <td class="bundlestatus">Deprecated</td>
      <td class="bundledesc"><p>Provides an OpenStack Nova control server</p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/openstack-configure">openstack-configure</a></td>
      <td class="bundlestatus">Deprecated</td>
      <td class="bundledesc"><p>Provides a suggested default configuration for OpenStack on Clear Linux.</p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/openstack-controller">openstack-controller</a></td>
      <td class="bundlestatus">Deprecated</td>
      <td class="bundledesc"><p>Provides an OpenStack multi-service control server</p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/openstack-dashboard">openstack-dashboard</a></td>
      <td class="bundlestatus">Deprecated</td>
      <td class="bundledesc"><p>Provides an OpenStack Horizon server</p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/openstack-database">openstack-database</a></td>
      <td class="bundlestatus">Deprecated</td>
      <td class="bundledesc"><p>Provides a Database as a Service server</p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/openstack-data-processing">openstack-data-processing</a></td>
      <td class="bundlestatus">Deprecated</td>
      <td class="bundledesc"><p>Provides a simple means to provision a data-intensive application cluster </p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/openstack-identity">openstack-identity</a></td>
      <td class="bundlestatus">Active</td>
      <td class="bundledesc"><p>Run openstack identity service
          <li>Includes (openstack-common) bundle.</li></p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/openstack-image">openstack-image</a></td>
      <td class="bundlestatus">Deprecated</td>
      <td class="bundledesc"><p>Provides an OpenStack Glance server</p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/openstack-lbaas">openstack-lbaas</a></td>
      <td class="bundlestatus">Deprecated</td>
      <td class="bundledesc"><p>Provides Load Balancing as a Service</p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/openstack-network">openstack-network</a></td>
      <td class="bundlestatus">Deprecated</td>
      <td class="bundledesc"><p>Provides an OpenStack Neutron server</p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/openstack-object-storage">openstack-object-storage</a></td>
      <td class="bundlestatus">Deprecated</td>
      <td class="bundledesc"><p>Provides an OpenStack Swift service</p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/openstack-orchestration">openstack-orchestration</a></td>
      <td class="bundlestatus">Deprecated</td>
      <td class="bundledesc"><p>Provides an OpenStack Heat service</p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/openstack-python-clients">openstack-python-clients</a></td>
      <td class="bundlestatus">Active</td>
      <td class="bundledesc"><p>Run openstack utilities
          <li>Includes (openstack-common) bundle.</li></p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/openstack-telemetry">openstack-telemetry</a></td>
      <td class="bundlestatus">Deprecated</td>
      <td class="bundledesc"><p>Provides an OpenStack Telemetry server</p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/openstack-telemetry-controller">openstack-telemetry-controller</a></td>
      <td class="bundlestatus">Deprecated</td>
      <td class="bundledesc"><p>Provides an OpenStack Telemetry server</p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/openstack-test-suite">openstack-test-suite</a></td>
      <td class="bundlestatus">Deprecated</td>
      <td class="bundledesc"><p>Provides an OpenStack Tempest/test suite</p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/openstack-vpnaas">openstack-vpnaas</a></td>
      <td class="bundlestatus">Deprecated</td>
      <td class="bundledesc"><p>Provides VPN as a Service</p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/os-clear-containers">os-clear-containers</a></td>
      <td class="bundlestatus">Active</td>
      <td class="bundledesc"><p>Control Clear Containers guest setup and workloads</p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/os-cloudguest">os-cloudguest</a></td>
      <td class="bundlestatus">Active</td>
      <td class="bundledesc"><p>Run any initialization processes required of a generic cloud guest VM
          <li>Includes (openssh-server) bundle.</li></p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/os-cloudguest-azure">os-cloudguest-azure</a></td>
      <td class="bundlestatus">Active</td>
      <td class="bundledesc"><p>Run any initialization process requried of an Azure cloud guest VM
          <li>Includes (openssh-server) bundle.</li></p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/os-cloudguest-cci">os-cloudguest-cci</a></td>
      <td class="bundlestatus">Deprecated</td>
      <td class="bundledesc"><p>Retired bundle - now provided by os-cloudguest
          <li>Includes (os-cloudguest) bundle.</li></p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/os-clr-on-clr">os-clr-on-clr</a></td>
      <td class="bundlestatus">Active</td>
      <td class="bundledesc"><p>Run any process required for Clear Linux development
          <li>Includes (c-basic) bundle.</li>
          <li>Includes (dev-utils-dev) bundle.</li>
          <li>Includes (dev-utils-doc) bundle.</li>
          <li>Includes (editors-doc) bundle.</li>
          <li>Includes (go-basic) bundle.</li>
          <li>Includes (koji) bundle.</li>
          <li>Includes (kvm-host) bundle.</li>
          <li>Includes (mail-utils) bundle.</li>
          <li>Includes (mail-utils-dev) bundle.</li>
          <li>Includes (mixer) bundle.</li>
          <li>Includes (network-basic-dev) bundle.</li>
          <li>Includes (network-basic-doc) bundle.</li>
          <li>Includes (openssh-server) bundle.</li>
          <li>Includes (os-core-dev) bundle.</li>
          <li>Includes (os-core-doc) bundle.</li>
          <li>Includes (os-core-update-dev) bundle.</li>
          <li>Includes (perl-basic) bundle.</li>
          <li>Includes (python-basic) bundle.</li>
          <li>Includes (storage-utils-dev) bundle.</li>
          <li>Includes # bundle.</li>
          <li>Includes needs bundle.</li>
          <li>Includes autodoc bundle.</li>
          <li>Includes first bundle.</li>
          <li>Includes (storage-utils-doc) bundle.</li>
          <li>Includes (sysadmin-basic-dev) bundle.</li>
          <li>Includes (sysadmin-basic-doc) bundle.</li></p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/os-clr-on-clr-dev">os-clr-on-clr-dev</a></td>
      <td class="bundlestatus">Active</td>
      <td class="bundledesc"><p>All packages required to build the os-clr-on-clr bundle.
          <li>Includes (os-clr-on-clr) bundle.</li>
          <li>Includes (os-dev-extras) bundle.</li>
          <li>Includes (c-basic) bundle.</li>
          <li>Includes (dev-utils-dev) bundle.</li>
          <li>Includes (dev-utils-doc) bundle.</li>
          <li>Includes (editors-doc) bundle.</li>
          <li>Includes (go-basic) bundle.</li>
          <li>Includes (koji) bundle.</li>
          <li>Includes (kvm-host) bundle.</li>
          <li>Includes (mail-utils) bundle.</li>
          <li>Includes (mail-utils-dev) bundle.</li>
          <li>Includes (mixer) bundle.</li>
          <li>Includes (network-basic-dev) bundle.</li>
          <li>Includes (network-basic-doc) bundle.</li>
          <li>Includes (openssh-server) bundle.</li>
          <li>Includes (os-core-dev) bundle.</li>
          <li>Includes (os-core-doc) bundle.</li>
          <li>Includes (os-core-update-dev) bundle.</li>
          <li>Includes (perl-basic) bundle.</li>
          <li>Includes (python-basic) bundle.</li>
          <li>Includes (storage-utils-dev) bundle.</li>
          <li>Includes # bundle.</li>
          <li>Includes needs bundle.</li>
          <li>Includes autodoc bundle.</li>
          <li>Includes first bundle.</li>
          <li>Includes (storage-utils-doc) bundle.</li>
          <li>Includes (sysadmin-basic-dev) bundle.</li>
          <li>Includes (sysadmin-basic-doc) bundle.</li>
          <li>Includes (go-basic-dev) bundle.</li>
          <li>Includes (mail-utils-dev) bundle.</li>
          <li>Includes (perl-basic-dev) bundle.</li>
          <li>Includes (python-basic-dev) bundle.</li></p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/os-core">os-core</a></td>
      <td class="bundlestatus">Active</td>
      <td class="bundledesc"><p>Run a minimal Linux userspace</p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/os-core-dev">os-core-dev</a></td>
      <td class="bundlestatus">Active</td>
      <td class="bundledesc"><p>All packages required to build the os-core bundle.
          <li>Includes (os-core) bundle.</li></p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/os-core-doc">os-core-doc</a></td>
      <td class="bundlestatus">Active</td>
      <td class="bundledesc"><p>Provides documentation and manpages for os-core
          <li>Includes (os-core) bundle.</li></p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/os-core-update">os-core-update</a></td>
      <td class="bundlestatus">Active</td>
      <td class="bundledesc"><p>Provides basic suite for running the Clear Linux for iA Updater
          <li>Includes (os-core) bundle.</li></p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/os-core-update-dev">os-core-update-dev</a></td>
      <td class="bundlestatus">Active</td>
      <td class="bundledesc"><p>All packages required to build the os-core-update bundle.
          <li>Includes (os-core-update) bundle.</li>
          <li>Includes (os-core-dev) bundle.</li>
          <li>Includes (os-dev-extras) bundle.</li>
          <li>Includes (os-core) bundle.</li>
          <li>Includes (os-core-dev) bundle.</li></p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/os-dev-extras">os-dev-extras</a></td>
      <td class="bundlestatus">Active</td>
      <td class="bundledesc"><p>Development utilities and helpful base Linux dev environment tools</p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/os-dev-full">os-dev-full</a></td>
      <td class="bundlestatus">Deprecated</td>
      <td class="bundledesc"><p>A bundle containing all development libraries and headers</p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/os-installer">os-installer</a></td>
      <td class="bundlestatus">Active</td>
      <td class="bundledesc"><p>Run image creation and installation for Clear Linux
          <li>Includes (network-basic) bundle.</li></p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/os-testsuite">os-testsuite</a></td>
      <td class="bundlestatus">WIP</td>
      <td class="bundledesc"><p>Provides basic test suite for Clear Linux for iA</p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/os-testsuite-phoronix">os-testsuite-phoronix</a></td>
      <td class="bundlestatus">Active</td>
      <td class="bundledesc"><p>Run the Phoronix testsuite
          <li>Includes (database-basic) bundle.</li>
          <li>Includes (php-basic) bundle.</li>
          <li>Includes (web-server-basic) bundle.</li>
          <li>Includes (machine-learning-basic) bundle.</li>
          <li>Includes (os-utils-gui) bundle.</li></p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/os-utils">os-utils</a></td>
      <td class="bundlestatus">Deprecated</td>
      <td class="bundledesc"><p>Provides a core set of OS utilities</p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/os-utils-dev">os-utils-dev</a></td>
      <td class="bundlestatus">Deprecated</td>
      <td class="bundledesc"><p>All packages required to build the os-utils bundle.</p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/os-utils-doc">os-utils-doc</a></td>
      <td class="bundlestatus">Deprecated</td>
      <td class="bundledesc"><p>Provides documentation and manpages for os-utils</p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/os-utils-gui">os-utils-gui</a></td>
      <td class="bundlestatus">Active</td>
      <td class="bundledesc"><p>Provides a graphical desktop environment
          <li>Includes (cryptography) bundle.</li>
          <li>Includes (python-basic) bundle.</li>
          <li>Includes (xfce4-desktop) bundle.</li></p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/perl-basic">perl-basic</a></td>
      <td class="bundlestatus">Active</td>
      <td class="bundledesc"><p>Run perl language programs</p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/perl-basic-dev">perl-basic-dev</a></td>
      <td class="bundlestatus">Active</td>
      <td class="bundledesc"><p>All packages required to build the perl-basic bundle.
          <li>Includes (perl-basic) bundle.</li>
          <li>Includes (os-core-dev) bundle.</li>
          <li>Includes (os-dev-extras) bundle.</li></p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/perl-extras">perl-extras</a></td>
      <td class="bundlestatus">Active</td>
      <td class="bundledesc"><p>Improve user experience with a common set of prebuilt perl libraries
          <li>Includes (perl-basic) bundle.</li></p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/php-basic">php-basic</a></td>
      <td class="bundlestatus">Active</td>
      <td class="bundledesc"><p>Run php language programs</p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/pnp-tools-advanced">pnp-tools-advanced</a></td>
      <td class="bundlestatus">Deprecated</td>
      <td class="bundledesc"><p>Provides advanced Power and Performance measurement tools</p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/pnp-tools-basic">pnp-tools-basic</a></td>
      <td class="bundlestatus">Active</td>
      <td class="bundledesc"><p>Run performance and power measurements
          <li>Includes (perl-basic) bundle.</li>
          <li>Includes (tcl-basic) bundle.</li></p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/pnp-tools-intermediate">pnp-tools-intermediate</a></td>
      <td class="bundlestatus">Deprecated</td>
      <td class="bundledesc"><p>Provides a deeper-level suite of Power and Performance testing tools</p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/pxe-server">pxe-server</a></td>
      <td class="bundlestatus">Active</td>
      <td class="bundledesc"><p>Run a PXE server</p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/python-basic">python-basic</a></td>
      <td class="bundlestatus">Active</td>
      <td class="bundledesc"><p>Run python language programs</p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/python-basic-dev">python-basic-dev</a></td>
      <td class="bundlestatus">Active</td>
      <td class="bundledesc"><p>All packages required to build the python-basic bundle.
          <li>Includes (python-basic) bundle.</li>
          <li>Includes (os-core-dev) bundle.</li>
          <li>Includes (os-dev-extras) bundle.</li></p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/python-extras">python-extras</a></td>
      <td class="bundlestatus">Active</td>
      <td class="bundledesc"><p>Improve user experience with a common set of prebuilt python libraries
          <li>Includes (python-basic) bundle.</li></p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/R-basic">R-basic</a></td>
      <td class="bundlestatus">Active</td>
      <td class="bundledesc"><p>Run R language programs
          <li>Includes (libX11client) bundle.</li></p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/R-extras">R-extras</a></td>
      <td class="bundlestatus">Active</td>
      <td class="bundledesc"><p>Improve the user experience with a common set of prebuilt R libraries
          <li>Includes (R-basic) bundle.</li></p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/ruby-basic">ruby-basic</a></td>
      <td class="bundlestatus">Active</td>
      <td class="bundledesc"><p>Run ruby language programs</p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/ruby-extras">ruby-extras</a></td>
      <td class="bundlestatus">Deprecated</td>
      <td class="bundledesc"><p>Improve user experience with a common set of prebuilt ruby libraries</p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/rust-basic">rust-basic</a></td>
      <td class="bundlestatus">Active</td>
      <td class="bundledesc"><p>Build and run rust language programs</p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/shells">shells</a></td>
      <td class="bundlestatus">Active</td>
      <td class="bundledesc"><p>Run a shell</p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/storage-cluster">storage-cluster</a></td>
      <td class="bundlestatus">WIP</td>
      <td class="bundledesc"><p>Run a storage server
          <li>Includes (storage-utils) bundle.</li></p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/storage-utils">storage-utils</a></td>
      <td class="bundlestatus">Active</td>
      <td class="bundledesc"><p>Run disk and filesystem management functions</p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/storage-utils-dev">storage-utils-dev</a></td>
      <td class="bundlestatus">Active</td>
      <td class="bundledesc"><p>All packages required to build the storage-utils bundle.
          <li>Includes (storage-utils) bundle.</li>
          <li>Includes (os-core-dev) bundle.</li>
          <li>Includes (os-dev-extras) bundle.</li></p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/sysadmin">sysadmin</a></td>
      <td class="bundlestatus">Deprecated</td>
      <td class="bundledesc"><p>Moved to sysadmin-basic
          <li>Includes (sysadmin-basic) bundle.</li></p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/sysadmin-advanced">sysadmin-advanced</a></td>
      <td class="bundlestatus">Active</td>
      <td class="bundledesc"><p>Toolchest that a sysadmin needs to diagnose issues
          <li>Includes (sysadmin-basic) bundle.</li>
          <li>Includes (pnp-tools-advanced) bundle.</li></p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/sysadmin-basic">sysadmin-basic</a></td>
      <td class="bundlestatus">Active</td>
      <td class="bundledesc"><p>Run common utilites useful for managing a system</p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/sysadmin-basic-dev">sysadmin-basic-dev</a></td>
      <td class="bundlestatus">Active</td>
      <td class="bundledesc"><p>All packages required to build the sysadmin-basic bundle.
          <li>Includes (sysadmin-basic) bundle.</li>
          <li>Includes (os-core-dev) bundle.</li>
          <li>Includes (os-dev-extras) bundle.</li></p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/sysadmin-basic-doc">sysadmin-basic-doc</a></td>
      <td class="bundlestatus">Active</td>
      <td class="bundledesc"><p>Provides documentation and manpages for sysadmin-basic
          <li>Includes (sysadmin-basic) bundle.</li></p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/sysadmin-hostmgmt">sysadmin-hostmgmt</a></td>
      <td class="bundlestatus">WIP</td>
      <td class="bundledesc"><p>Utilities and Services for managing large-scale clusters of networked hosts
          <li>Includes (pxe-server) bundle.</li>
          <li>Includes (python-basic) bundle.</li></p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/tcl-basic">tcl-basic</a></td>
      <td class="bundlestatus">Active</td>
      <td class="bundledesc"><p>Run tk/tcl language programs
          <li>Includes (libX11client) bundle.</li></p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/telemetrics">telemetrics</a></td>
      <td class="bundlestatus">Active</td>
      <td class="bundledesc"><p>Run telemetrics client</p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/virtualbox-guest">virtualbox-guest</a></td>
      <td class="bundlestatus">Deprecated</td>
      <td class="bundledesc"><p>Include the kernel modules to be used in a VirtualBox instance
          <li>Includes (kernel-lts) bundle.</li></p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/web-server-basic">web-server-basic</a></td>
      <td class="bundlestatus">Active</td>
      <td class="bundledesc"><p>Run a HTTP web server</p></td>
    </tr>
    <tr>
      <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/xfce4-desktop">xfce4-desktop</a></td>
      <td class="bundlestatus">Active</td>
      <td class="bundledesc"><p>Run GUI desktop environment
          <li>Includes (libX11client) bundle.</li></p></td>
    </tr>
    </tbody>
  </table>





