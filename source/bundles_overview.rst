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

The Clear Linux\* OS for Intel® Architecture takes a slightly different
approach. While we also use the concept of packages to manage compiling
source code into binaries, we do not use the package concept to deploy
software. Instead, we provide "bundles" that  provide a set of functionality
to the system administrator, independent of how many and which pieces of
the upstream open source projects are needed for this functionality.

Useful bundle commands
======================

To see a list of currently-installed bundles, enter:

.. code-block:: console

   # swupd bundle-list

To see the list of all available bundles, enter:

.. code-block:: console

   # swupd bundle-list --all

To see the list of optional bundles to install, enter:

.. code-block:: console

   # swupd new bundle-add --list


To add a bundle, enter:

.. code-block:: console

   # swupd bundle-add [bundle name]

Bundle overview table
=====================

Current list of available bundles as of ``[[24 April 2017]]``.

.. raw:: html

   <head>
       <title>Bundles in Clear Linux OS for Intel® Architecture</title>
       <style type="text/css">
       table {
           margin: 2em;
           border: 1px solid #e0e0e0;
           border-collapse: collapse;
           width: auto;
       }

       th {
           align: center;
           padding: 0.33em;
           border: #ccc solid 1px;
           background-color: #555;
           color: #fff;
           text-transform: uppercase;
           font-size: 1.21em
       }

       tbody tr:nth-child(odd) {
           background-color: #e0e0e0;
       }

       .bundlename {
           font-family: monospace;
           font-size: 1.13em;
           font-weight: bolder;
           padding-left: 0.42em;
       }

       .bundlestatus {
           font-family: sans;
           font-weight: lighter;
       }

       .bundledesc {
           font-size: 0.93em;
           line-height: 0.88em;
           font-family: sans;
       }

       li,
       ul {
           margin-left: 0.53em;
           padding-left: 0.23em;
       }
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
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/application-server">application-server</a>
               </td>
               <td class="bundlestatus">Active</td>
               <td class="bundledesc">
                   <p>Run an application server via HTTP
                       <li>Includes (web-server-basic) bundle.</li>
                   </p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/big-data-basic">big-data-basic</a></td>
               <td class="bundlestatus">WIP</td>
               <td class="bundledesc">
                   <p>Tools and frameworks for big data management</p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/bootloader">bootloader</a></td>
               <td class="bundlestatus">Active</td>
               <td class="bundledesc">
                   <p>Loads kernel from disk and boots the system</p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/c-basic">c-basic</a></td>
               <td class="bundlestatus">Active</td>
               <td class="bundledesc">
                   <p>Build and run C/C++ language programs</p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/cloud-control">cloud-control</a></td>
               <td class="bundlestatus">Active</td>
               <td class="bundledesc">
                   <p>Run a cloud orchestration server
                       <li>Includes (kvm-host) bundle.</li>
                       <li>Includes (network-basic) bundle.</li>
                       <li>Includes (storage-cluster) bundle.</li>
                   </p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/cloud-native-basic">cloud-native-basic</a></td>
               <td class="bundlestatus">WIP</td>
               <td class="bundledesc">
                   <p>Contains ClearLinux native software for Cloud
                       <li>Includes (containers-basic) bundle.</li>
                   </p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/cloud-network">cloud-network</a></td>
               <td class="bundlestatus">Active</td>
               <td class="bundledesc">
                   <p>Configure a cloud orchestration network
                       <li>Includes (openssh-server) bundle.</li>
                       <li>Includes (network-basic) bundle.</li>
                   </p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/clr-devops">clr-devops</a></td>
               <td class="bundlestatus">Active</td>
               <td class="bundledesc">
                   <p>Run all Clear Linux devops workloads
                       <li>Includes (os-installer) bundle.</li>
                       <li>Includes (os-core-update) bundle.</li>
                       <li>Includes (mixer) bundle.</li>
                       <li>Includes (java-basic) bundle.</li>
                       <li>Includes (rust-basic) bundle.</li>
                       <li>Includes (koji) bundle.</li>
                   </p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/containers-basic">containers-basic</a></td>
               <td class="bundlestatus">Active</td>
               <td class="bundledesc">
                   <p>Run container applications from Dockerhub</p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/containers-basic-dev">containers-basic-dev</a></td>
               <td class="bundlestatus">Active</td>
               <td class="bundledesc">
                   <p>All packages required to build the containers-basic bundle.
                       <li>Includes (containers-basic) bundle.</li>
                       <li>Includes (os-core-dev) bundle.</li>
                       <li>Includes (dev-utils) bundle.</li>
                       <li>Includes (containers-virt-dev) bundle.</li>
                   </p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/containers-virt">containers-virt</a></td>
               <td class="bundlestatus">Active</td>
               <td class="bundledesc">
                   <p>Run container applications from Dockerhub in lightweight virtual machines
                       <li>Includes (kernel-container) bundle.</li>
                       <li>Includes (containers-basic) bundle.</li>
                   </p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/containers-virt-dev">containers-virt-dev</a></td>
               <td class="bundlestatus">Active</td>
               <td class="bundledesc">
                   <p>All packages required to build the containers-virt bundle.
                       <li>Includes (containers-virt) bundle.</li>
                       <li>Includes (os-core-dev) bundle.</li>
                       <li>Includes (dev-utils) bundle.</li>
                       <li>Includes (kernel-container) bundle.</li>
                       <li>Includes (containers-basic) bundle.</li>
                   </p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/cryptography">cryptography</a></td>
               <td class="bundlestatus">Active</td>
               <td class="bundledesc">
                   <p>Encrypt, decrypt, sign and verify objects</p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/database-basic">database-basic</a></td>
               <td class="bundlestatus">Active</td>
               <td class="bundledesc">
                   <p>Run a SQL database</p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/database-basic-dev">database-basic-dev</a></td>
               <td class="bundlestatus">Active</td>
               <td class="bundledesc">
                   <p>All packages required to build the database-basic bundle.
                       <li>Includes (database-basic) bundle.</li>
                       <li>Includes (os-core-dev) bundle.</li>
                       <li>Includes (dev-utils) bundle.</li>
                   </p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/desktop">desktop</a></td>
               <td class="bundlestatus">Active</td>
               <td class="bundledesc">
                   <p>Run the GNOME GUI desktop environment
                       <li>Includes (libX11client) bundle.</li>
                       <li>Includes (desktop-apps) bundle.</li>
                       <li>Includes (desktop-gnomelibs) bundle.</li>
                       <li>Includes (desktop-assets) bundle.</li>
                       <li>Includes (desktop-locales) bundle.</li>
                       <li>Includes (sysadmin-basic) bundle.</li>
                   </p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/desktop-apps">desktop-apps</a></td>
               <td class="bundlestatus">Active</td>
               <td class="bundledesc">
                   <p>Applications for the desktop
                       <li>Includes (libX11client) bundle.</li>
                       <li>Includes (desktop-gnomelibs) bundle.</li>
                   </p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/desktop-assets">desktop-assets</a></td>
               <td class="bundlestatus">Active</td>
               <td class="bundledesc">
                   <p>Images and Icons for the desktop</p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/desktop-gnomelibs">desktop-gnomelibs</a></td>
               <td class="bundlestatus">Active</td>
               <td class="bundledesc">
                   <p>Helper bundle with common libraries used by desktopy things
                       <li>Includes (libX11client) bundle.</li>
                   </p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/desktop-locales">desktop-locales</a></td>
               <td class="bundlestatus">Active</td>
               <td class="bundledesc">
                   <p>translations and documentation for desktop components</p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/dev-utils">dev-utils</a></td>
               <td class="bundlestatus">Active</td>
               <td class="bundledesc">
                   <p>Assist application development</p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/dev-utils-dev">dev-utils-dev</a></td>
               <td class="bundlestatus">Active</td>
               <td class="bundledesc">
                   <p>All packages required to build the dev-utils bundle.
                       <li>Includes (dev-utils) bundle.</li>
                       <li>Includes (os-core-dev) bundle.</li>
                       <li>Includes (dev-utils) bundle.</li>
                   </p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/editors">editors</a></td>
               <td class="bundlestatus">Active</td>
               <td class="bundledesc">
                   <p>Run popular terminal text editors
                       <li>Includes (python-basic) bundle.</li>
                   </p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/editors-dev">editors-dev</a></td>
               <td class="bundlestatus">Active</td>
               <td class="bundledesc">
                   <p>All packages required to build the editors bundle.
                       <li>Includes (editors) bundle.</li>
                       <li>Includes (os-core-dev) bundle.</li>
                       <li>Includes (dev-utils) bundle.</li>
                       <li>Includes (python-basic) bundle.</li>
                       <li>Includes (python-basic-dev) bundle.</li>
                   </p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/games">games</a></td>
               <td class="bundlestatus">Active</td>
               <td class="bundledesc">
                   <p>Play games in Clear Linux
                       <li>Includes (libX11client) bundle.</li>
                   </p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/go-basic">go-basic</a></td>
               <td class="bundlestatus">Active</td>
               <td class="bundledesc">
                   <p>Build and run go language programs</p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/go-basic-dev">go-basic-dev</a></td>
               <td class="bundlestatus">Active</td>
               <td class="bundledesc">
                   <p>All packages required to build the go-basic bundle.
                       <li>Includes (go-basic) bundle.</li>
                       <li>Includes (os-core-dev) bundle.</li>
                       <li>Includes (dev-utils) bundle.</li>
                   </p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/haskell-basic">haskell-basic</a></td>
               <td class="bundlestatus">Active</td>
               <td class="bundledesc">
                   <p>Build and run haskell language programs</p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/java-basic">java-basic</a></td>
               <td class="bundlestatus">Active</td>
               <td class="bundledesc">
                   <p>Build and run java language programs
                       <li>Includes (libX11client) bundle.</li>
                   </p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/kernel-aws">kernel-aws</a></td>
               <td class="bundlestatus">WIP</td>
               <td class="bundledesc">
                   <p>Run the kvm specific kernel
                       <li>Includes (bootloader) bundle.</li>
                   </p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/kernel-container">kernel-container</a></td>
               <td class="bundlestatus">Active</td>
               <td class="bundledesc">
                   <p>Run the container specific kernel</p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/kernel-hyperv">kernel-hyperv</a></td>
               <td class="bundlestatus">Active</td>
               <td class="bundledesc">
                   <p>Run the hyperv specific kernel
                       <li>Includes (bootloader) bundle.</li>
                   </p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/kernel-hyperv">kernel-hyperv</a></td>
               <td class="bundlestatus">Active</td>
               <td class="bundledesc">
                   <p>Run the hyperv specific LTS kernel
                       <li>Includes (bootloader) bundle.</li>
                   </p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/kernel-hyperv-mini">kernel-hyperv-mini</a></td>
               <td class="bundlestatus">WIP</td>
               <td class="bundledesc">
                   <p>Run the hyperv mini-os specific kernel
                       <li>Includes (bootloader) bundle.</li>
                   </p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/kernel-kvm">kernel-kvm</a></td>
               <td class="bundlestatus">Active</td>
               <td class="bundledesc">
                   <p>Run the kvm specific kernel
                       <li>Includes (bootloader) bundle.</li>
                   </p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/kernel-lts">kernel-lts</a></td>
               <td class="bundlestatus">Active</td>
               <td class="bundledesc">
                   <p>Run the lts native kernel
                       <li>Includes (bootloader) bundle.</li>
                   </p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/kernel-native">kernel-native</a></td>
               <td class="bundlestatus">Active</td>
               <td class="bundledesc">
                   <p>Run the native kernel
                       <li>Includes (bootloader) bundle.</li>
                   </p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/koji">koji</a></td>
               <td class="bundlestatus">WIP</td>
               <td class="bundledesc">
                   <p>Sets up a koji build service (builder-only, for now) based on NFS mounts.</p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/kvm-host">kvm-host</a></td>
               <td class="bundlestatus">Active</td>
               <td class="bundledesc">
                   <p>Run virtual machines
                       <li>Includes (libX11client) bundle.</li>
                   </p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/libX11client">libX11client</a></td>
               <td class="bundlestatus">Active</td>
               <td class="bundledesc">
                   <p>Grouping only bundle for use in X using bundles</p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/machine-learning-basic">machine-learning-basic</a></td>
               <td class="bundlestatus">Active</td>
               <td class="bundledesc">
                   <p>Build machine learning applications
                       <li>Includes (c-basic) bundle.</li>
                       <li>Includes (python-extras) bundle.</li>
                   </p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/machine-learning-web-ui">machine-learning-web-ui</a></td>
               <td class="bundlestatus">Active</td>
               <td class="bundledesc">
                   <p>Web based, interactive tools for machine learning
                       <li>Includes (python-basic) bundle.</li>
                       <li>Includes (R-extras) bundle.</li>
                   </p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/mail-utils">mail-utils</a></td>
               <td class="bundlestatus">Active</td>
               <td class="bundledesc">
                   <p>Process, read and send email</p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/mail-utils-dev">mail-utils-dev</a></td>
               <td class="bundlestatus">Active</td>
               <td class="bundledesc">
                   <p>All packages required to build the mail-utils bundle.
                       <li>Includes (mail-utils) bundle.</li>
                       <li>Includes (os-core-dev) bundle.</li>
                       <li>Includes (dev-utils) bundle.</li>
                   </p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/mixer">mixer</a></td>
               <td class="bundlestatus">Active</td>
               <td class="bundledesc">
                   <p>Create Clear Linux releases
                       <li>Includes (python-basic) bundle.</li>
                       <li>Includes (sysadmin-basic) bundle.</li>
                   </p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/network-basic">network-basic</a></td>
               <td class="bundlestatus">Active</td>
               <td class="bundledesc">
                   <p>Run network utilities and modify network settings
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
                       <li>Includes (python-basic) bundle.</li>
                   </p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/network-basic-dev">network-basic-dev</a></td>
               <td class="bundlestatus">Active</td>
               <td class="bundledesc">
                   <p>All packages required to build the network-basic bundle.
                       <li>Includes (network-basic) bundle.</li>
                       <li>Includes (os-core-dev) bundle.</li>
                       <li>Includes (dev-utils) bundle.</li>
                       <li>Includes (openssh-server) bundle.</li>
                       <li>Includes (perl-basic) bundle.</li>
                       <li>Includes (python-basic) bundle.</li>
                       <li>Includes (perl-basic-dev) bundle.</li>
                       <li>Includes (python-basic-dev) bundle.</li>
                   </p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/nodejs-basic">nodejs-basic</a></td>
               <td class="bundlestatus">Active</td>
               <td class="bundledesc">
                   <p>Run javascript server side</p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/openssh-server">openssh-server</a></td>
               <td class="bundlestatus">Active</td>
               <td class="bundledesc">
                   <p>Run an ssh server</p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/os-clear-containers">os-clear-containers</a></td>
               <td class="bundlestatus">Active</td>
               <td class="bundledesc">
                   <p>Control Clear Containers guest setup and workloads</p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/os-cloudguest">os-cloudguest</a></td>
               <td class="bundlestatus">Active</td>
               <td class="bundledesc">
                   <p>Run any initialization processes required of a generic cloud guest VM
                       <li>Includes (openssh-server) bundle.</li>
                   </p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/os-cloudguest-azure">os-cloudguest-azure</a></td>
               <td class="bundlestatus">Active</td>
               <td class="bundledesc">
                   <p>Run any initialization process requried of an Azure cloud guest VM
                       <li>Includes (openssh-server) bundle.</li>
                       <li>Includes (python-basic) bundle.</li>
                   </p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/os-clr-on-clr">os-clr-on-clr</a></td>
               <td class="bundlestatus">Active</td>
               <td class="bundledesc">
                   <p>Run any process required for Clear Linux development
                       <li>Includes (c-basic) bundle.</li>
                       <li>Includes (dev-utils) bundle.</li>
                       <li>Includes (dev-utils-dev) bundle.</li>
                       <li>Includes (editors) bundle.</li>
                       <li>Includes (go-basic) bundle.</li>
                       <li>Includes (koji) bundle.</li>
                       <li>Includes (kvm-host) bundle.</li>
                       <li>Includes (mail-utils) bundle.</li>
                       <li>Includes (mail-utils-dev) bundle.</li>
                       <li>Includes (mixer) bundle.</li>
                       <li>Includes (network-basic) bundle.</li>
                       <li>Includes (network-basic-dev) bundle.</li>
                       <li>Includes (openssh-server) bundle.</li>
                       <li>Includes (os-core) bundle.</li>
                       <li>Includes (os-core-dev) bundle.</li>
                       <li>Includes (os-core-update-dev) bundle.</li>
                       <li>Includes (perl-basic) bundle.</li>
                       <li>Includes (python-basic) bundle.</li>
                       <li>Includes (storage-utils) bundle.</li>
                       <li>Includes (storage-utils-dev) bundle.</li>
                       <li>Includes (sysadmin-basic) bundle.</li>
                       <li>Includes (sysadmin-basic-dev) bundle.</li>
                   </p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/os-clr-on-clr-dev">os-clr-on-clr-dev</a></td>
               <td class="bundlestatus">Active</td>
               <td class="bundledesc">
                   <p>All packages required to build the os-clr-on-clr bundle.
                       <li>Includes (os-clr-on-clr) bundle.</li>
                       <li>Includes (c-basic) bundle.</li>
                       <li>Includes (dev-utils) bundle.</li>
                       <li>Includes (dev-utils-dev) bundle.</li>
                       <li>Includes (editors) bundle.</li>
                       <li>Includes (go-basic) bundle.</li>
                       <li>Includes (koji) bundle.</li>
                       <li>Includes (kvm-host) bundle.</li>
                       <li>Includes (mail-utils) bundle.</li>
                       <li>Includes (mail-utils-dev) bundle.</li>
                       <li>Includes (mixer) bundle.</li>
                       <li>Includes (network-basic) bundle.</li>
                       <li>Includes (network-basic-dev) bundle.</li>
                       <li>Includes (openssh-server) bundle.</li>
                       <li>Includes (os-core) bundle.</li>
                       <li>Includes (os-core-dev) bundle.</li>
                       <li>Includes (os-core-update-dev) bundle.</li>
                       <li>Includes (perl-basic) bundle.</li>
                       <li>Includes (python-basic) bundle.</li>
                       <li>Includes (storage-utils) bundle.</li>
                       <li>Includes (storage-utils-dev) bundle.</li>
                       <li>Includes (sysadmin-basic) bundle.</li>
                       <li>Includes (sysadmin-basic-dev) bundle.</li>
                       <li>Includes (dev-utils-dev) bundle.</li>
                       <li>Includes (editors-dev) bundle.</li>
                       <li>Includes (go-basic-dev) bundle.</li>
                       <li>Includes (mail-utils-dev) bundle.</li>
                       <li>Includes (network-basic-dev) bundle.</li>
                       <li>Includes (os-core-dev) bundle.</li>
                       <li>Includes (perl-basic-dev) bundle.</li>
                       <li>Includes (python-basic-dev) bundle.</li>
                       <li>Includes (storage-utils-dev) bundle.</li>
                       <li>Includes (sysadmin-basic-dev) bundle.</li>
                   </p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/os-core">os-core</a></td>
               <td class="bundlestatus">Active</td>
               <td class="bundledesc">
                   <p>Run a minimal Linux userspace</p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/os-core-dev">os-core-dev</a></td>
               <td class="bundlestatus">Active</td>
               <td class="bundledesc">
                   <p>All packages required to build the os-core bundle.
                       <li>Includes (os-core) bundle.</li>
                   </p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/os-core-update">os-core-update</a></td>
               <td class="bundlestatus">Active</td>
               <td class="bundledesc">
                   <p>Provides basic suite for running the Clear Linux for iA Updater
                       <li>Includes (os-core) bundle.</li>
                   </p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/os-core-update-dev">os-core-update-dev</a></td>
               <td class="bundlestatus">Active</td>
               <td class="bundledesc">
                   <p>All packages required to build the os-core-update bundle.
                       <li>Includes (os-core-update) bundle.</li>
                       <li>Includes (os-core-dev) bundle.</li>
                       <li>Includes (dev-utils) bundle.</li>
                       <li>Includes (os-core) bundle.</li>
                       <li>Includes (os-core-dev) bundle.</li>
                   </p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/os-dev-extras">os-dev-extras</a></td>
               <td class="bundlestatus">Deprecated</td>
               <td class="bundledesc">
                   <p>Development utilities and helpful base Linux dev environment tools</p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/os-installer">os-installer</a></td>
               <td class="bundlestatus">Active</td>
               <td class="bundledesc">
                   <p>Run image creation and installation for Clear Linux</p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/os-testsuite">os-testsuite</a></td>
               <td class="bundlestatus">WIP</td>
               <td class="bundledesc">
                   <p>Provides basic test suite for Clear Linux for iA</p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/os-testsuite-phoronix">os-testsuite-phoronix</a></td>
               <td class="bundlestatus">Active</td>
               <td class="bundledesc">
                   <p>Run the Phoronix testsuite
                       <li>Includes (c-basic) bundle.</li>
                       <li>Includes (database-basic) bundle.</li>
                       <li>Includes (go-basic) bundle.</li>
                       <li>Includes (machine-learning-basic) bundle.</li>
                       <li>Includes (os-utils-gui) bundle.</li>
                       <li>Includes (php-basic) bundle.</li>
                       <li>Includes (games) bundle.</li>
                   </p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/os-utils-gui">os-utils-gui</a></td>
               <td class="bundlestatus">Active</td>
               <td class="bundledesc">
                   <p>Provides a graphical desktop environment
                       <li>Includes (cryptography) bundle.</li>
                       <li>Includes (python-basic) bundle.</li>
                       <li>Includes (xfce4-desktop) bundle.</li>
                   </p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/os-utils-gui-dev">os-utils-gui-dev</a></td>
               <td class="bundlestatus">Active</td>
               <td class="bundledesc">
                   <p>All packages required to build the os-utils-gui bundle.
                       <li>Includes (os-utils-gui) bundle.</li>
                       <li>Includes (os-core-dev) bundle.</li>
                       <li>Includes (dev-utils) bundle.</li>
                       <li>Includes (cryptography) bundle.</li>
                       <li>Includes (python-basic) bundle.</li>
                       <li>Includes (xfce4-desktop) bundle.</li>
                       <li>Includes (python-basic-dev) bundle.</li>
                   </p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/perl-basic">perl-basic</a></td>
               <td class="bundlestatus">Active</td>
               <td class="bundledesc">
                   <p>Run perl language programs</p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/perl-basic-dev">perl-basic-dev</a></td>
               <td class="bundlestatus">Active</td>
               <td class="bundledesc">
                   <p>All packages required to build the perl-basic bundle.
                       <li>Includes (perl-basic) bundle.</li>
                       <li>Includes (os-core-dev) bundle.</li>
                       <li>Includes (dev-utils) bundle.</li>
                   </p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/perl-extras">perl-extras</a></td>
               <td class="bundlestatus">Active</td>
               <td class="bundledesc">
                   <p>Improve user experience with a common set of prebuilt perl libraries
                       <li>Includes (perl-basic) bundle.</li>
                   </p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/php-basic">php-basic</a></td>
               <td class="bundlestatus">Active</td>
               <td class="bundledesc">
                   <p>Run php language programs</p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/pnp-tools-basic">pnp-tools-basic</a></td>
               <td class="bundlestatus">Active</td>
               <td class="bundledesc">
                   <p>Run performance and power measurements
                       <li>Includes (perl-basic) bundle.</li>
                       <li>Includes (tcl-basic) bundle.</li>
                   </p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/pxe-server">pxe-server</a></td>
               <td class="bundlestatus">Active</td>
               <td class="bundledesc">
                   <p>Run a PXE server</p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/python-basic">python-basic</a></td>
               <td class="bundlestatus">Active</td>
               <td class="bundledesc">
                   <p>Run python language programs</p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/python-basic-dev">python-basic-dev</a></td>
               <td class="bundlestatus">Active</td>
               <td class="bundledesc">
                   <p>All packages required to build the python-basic bundle.
                       <li>Includes (python-basic) bundle.</li>
                       <li>Includes (os-core-dev) bundle.</li>
                       <li>Includes (dev-utils) bundle.</li>
                   </p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/python-extras">python-extras</a></td>
               <td class="bundlestatus">Active</td>
               <td class="bundledesc">
                   <p>Improve user experience with a common set of prebuilt python libraries
                       <li>Includes (python-basic) bundle.</li>
                   </p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/R-basic">R-basic</a></td>
               <td class="bundlestatus">Active</td>
               <td class="bundledesc">
                   <p>Run R language programs
                       <li>Includes (libX11client) bundle.</li>
                   </p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/R-extras">R-extras</a></td>
               <td class="bundlestatus">Active</td>
               <td class="bundledesc">
                   <p>Improve the user experience with a common set of prebuilt R libraries
                       <li>Includes (R-basic) bundle.</li>
                   </p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/ruby-basic">ruby-basic</a></td>
               <td class="bundlestatus">Active</td>
               <td class="bundledesc">
                   <p>Run ruby language programs</p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/rust-basic">rust-basic</a></td>
               <td class="bundlestatus">Active</td>
               <td class="bundledesc">
                   <p>Build and run rust language programs</p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/shells">shells</a></td>
               <td class="bundlestatus">Active</td>
               <td class="bundledesc">
                   <p>Run a shell</p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/storage-cluster">storage-cluster</a></td>
               <td class="bundlestatus">Active</td>
               <td class="bundledesc">
                   <p>Run a storage server</p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/storage-utils">storage-utils</a></td>
               <td class="bundlestatus">Active</td>
               <td class="bundledesc">
                   <p>Run disk and filesystem management functions</p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/storage-utils-dev">storage-utils-dev</a></td>
               <td class="bundlestatus">Active</td>
               <td class="bundledesc">
                   <p>All packages required to build the storage-utils bundle.
                       <li>Includes (storage-utils) bundle.</li>
                       <li>Includes (os-core-dev) bundle.</li>
                       <li>Includes (dev-utils) bundle.</li>
                   </p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/stream">stream</a></td>
               <td class="bundlestatus">WIP</td>
               <td class="bundledesc">
                   <p>Run an audio or visual streaming server</p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/sysadmin-basic">sysadmin-basic</a></td>
               <td class="bundlestatus">Active</td>
               <td class="bundledesc">
                   <p>Run common utilites useful for managing a system</p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/sysadmin-basic-dev">sysadmin-basic-dev</a></td>
               <td class="bundlestatus">Active</td>
               <td class="bundledesc">
                   <p>All packages required to build the sysadmin-basic bundle.
                       <li>Includes (sysadmin-basic) bundle.</li>
                       <li>Includes (os-core-dev) bundle.</li>
                       <li>Includes (dev-utils) bundle.</li>
                   </p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/sysadmin-hostmgmt">sysadmin-hostmgmt</a></td>
               <td class="bundlestatus">Active</td>
               <td class="bundledesc">
                   <p>Utilities and Services for managing large-scale clusters of networked hosts
                       <li>Includes (pxe-server) bundle.</li>
                       <li>Includes (python-basic) bundle.</li>
                   </p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/sysadmin-remote-managed">sysadmin-remote-managed</a></td>
               <td class="bundlestatus">WIP</td>
               <td class="bundledesc">
                   <p>Enable the host to be managed remotely by configuration management tools
                       <li>Includes (openssh-server) bundle.</li>
                       <li>Includes (python-basic) bundle.</li>
                   </p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/tcl-basic">tcl-basic</a></td>
               <td class="bundlestatus">Active</td>
               <td class="bundledesc">
                   <p>Run tk/tcl language programs
                       <li>Includes (libX11client) bundle.</li>
                   </p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/telemetrics">telemetrics</a></td>
               <td class="bundlestatus">Active</td>
               <td class="bundledesc">
                   <p>Run telemetrics client</p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/user-basic">user-basic</a></td>
               <td class="bundlestatus">Active</td>
               <td class="bundledesc">
                   <p>Meta bundle capturing most console user work flows
                       <li>Includes (dev-utils) bundle.</li>
                       <li>Includes (editors) bundle.</li>
                       <li>Includes (kvm-host) bundle.</li>
                       <li>Includes (mail-utils) bundle.</li>
                       <li>Includes (network-basic) bundle.</li>
                       <li>Includes (openssh-server) bundle.</li>
                       <li>Includes (os-core-update) bundle.</li>
                       <li>Includes (shells) bundle.</li>
                       <li>Includes (storage-utils) bundle.</li>
                       <li>Includes (sysadmin-basic) bundle.</li>
                   </p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/user-basic-dev">user-basic-dev</a></td>
               <td class="bundlestatus">Active</td>
               <td class="bundledesc">
                   <p>All packages required to build the user-basic bundle.
                       <li>Includes (user-basic) bundle.</li>
                       <li>Includes (os-core-dev) bundle.</li>
                       <li>Includes (dev-utils) bundle.</li>
                       <li>Includes (editors) bundle.</li>
                       <li>Includes (kvm-host) bundle.</li>
                       <li>Includes (mail-utils) bundle.</li>
                       <li>Includes (network-basic) bundle.</li>
                       <li>Includes (openssh-server) bundle.</li>
                       <li>Includes (os-core-update) bundle.</li>
                       <li>Includes (shells) bundle.</li>
                       <li>Includes (storage-utils) bundle.</li>
                       <li>Includes (sysadmin-basic) bundle.</li>
                       <li>Includes (dev-utils-dev) bundle.</li>
                       <li>Includes (editors-dev) bundle.</li>
                       <li>Includes (mail-utils-dev) bundle.</li>
                       <li>Includes (network-basic-dev) bundle.</li>
                       <li>Includes (os-core-update-dev) bundle.</li>
                       <li>Includes (storage-utils-dev) bundle.</li>
                       <li>Includes (sysadmin-basic-dev) bundle.</li>
                   </p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/web-server-basic">web-server-basic</a></td>
               <td class="bundlestatus">Active</td>
               <td class="bundledesc">
                   <p>Run a HTTP web server</p>
               </td>
           </tr>
           <tr>
               <td class="bundlename"><a href="https://github.com/clearlinux/clr-bundles/tree/master/bundles/xfce4-desktop">xfce4-desktop</a></td>
               <td class="bundlestatus">Active</td>
               <td class="bundledesc">
                   <p>Run GUI desktop environment
                       <li>Includes (libX11client) bundle.</li>
                   </p>
               </td>
           </tr>
       </tbody>
   </table>

