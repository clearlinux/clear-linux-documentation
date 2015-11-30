List of bundles
############################################################

This is a list of the basic bundles in Clear Linux* OS for Intel® Architecture:


.. raw:: html

	<head>
		<title>Bundles in ClearLinux</title>
		<style media="screen" type="text/css">
			table { margin: 2em; border-collapse: collapse; }
			td, th { padding: .5em; border: 1px #ccc solid; }
			thead { background: #fc9; }
		</style>

	</head>

	<table border: 1px; callpadding: 15>
	    <thead>
	        <th align=left>Bundle Name</th>
	        <th align=center>Status</th>
	        <th align=left>Description</th>
	        <!-- <th align=left>Capabilities</th> -->
	        <!-- <th align=left>Maintainer</th> -->
	    </thead>
	    <tbody>
	        <tr>
	            <td align=left> bat</td>
	            <td align=center> ACTIVE</td>
	            <td align=left>
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
	            <td align=left> bootloader</td>
	            <td align=center> ACTIVE</td>
	            <td align=left>
	                <p> UEFI bootloaders</p>
	            </td>
	            <!-- <td align=left><p></p></td> -->
	            <!-- <td align=left><p></p></td> -->
	        </tr>
	        <tr>
	            <td align=left> clr-devops</td>
	            <td align=center> ACTIVE</td>
	            <td align=left>
	                <p> Provides build/release tools for Clear devops team</p>
	            </td>
	            <!-- <td align=left><p></p></td> -->
	            <!-- <td align=left><p></p></td> -->
	        </tr>
	        <tr>
	            <td align=left> containers-basic</td>
	            <td align=center> WIP</td>
	            <td align=left>
	                <p> Installs rkt base for Clear Containers</p>
	                <li>Includes (storage-utils) bundle.</p>
	                    <li>Includes (network-basic) bundle.</p>
	                        <li>Includes (kernel-container) bundle.</p>
	            </td>
	            <!-- <td align=left><p></p></td> -->
	            <!-- <td align=left><p></p></td> -->
	        </tr>
	        <tr>
	            <td align=left> cryptography</td>
	            <td align=center> ACTIVE</td>
	            <td align=left>
	                <p> Cryptographic tools</p>
	            </td>
	            <!-- <td align=left><p></p></td> -->
	            <!-- <td align=left><p></p></td> -->
	        </tr>
	        <tr>
	            <td align=left> database-mariadb</td>
	            <td align=center> ACTIVE</td>
	            <td align=left>
	                <p> Provides components needed to run MariaDB</p>
	            </td>
	            <!-- <td align=left><p></p></td> -->
	            <!-- <td align=left><p></p></td> -->
	        </tr>
	        <tr>
	            <td align=left> database-mongodb</td>
	            <td align=center> WIP</td>
	            <td align=left>
	                <p> Provides components needed to run mongodb</p>
	            </td>
	            <!-- <td align=left><p></p></td> -->
	            <!-- <td align=left><p></p></td> -->
	        </tr>
	        <tr>
	            <td align=left> devtools-basic</td>
	            <td align=center> ACTIVE</td>
	            <td align=left>
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
	            <td align=left> devtools-extras</td>
	            <td align=center> ACTIVE</td>
	            <td align=left>
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
	            <td align=left> dev-utils</td>
	            <td align=center> ACTIVE</td>
	            <td align=left>
	                <p> Provides a limited set of development utilities</p>
	            </td>
	            <!-- <td align=left><p></p></td> -->
	            <!-- <td align=left><p></p></td> -->
	        </tr>
	        <tr>
	            <td align=left> dpdk-dev</td>
	            <td align=center> ACTIVE</td>
	            <td align=left>
	                <p> All headers and libraries necessary to develop with the Data Plane Development Kit.</p>
	                <li>Includes (os-core-dev) bundle.</p>
	            </td>
	            <!-- <td align=left><p></p></td> -->
	            <!-- <td align=left><p></p></td> -->
	        </tr>
	        <tr>
	            <td align=left> editors</td>
	            <td align=center> ACTIVE</td>
	            <td align=left>
	                <p> Provides popular text editors</p>
	            </td>
	            <!-- <td align=left><p></p></td> -->
	            <!-- <td align=left><p></p></td> -->
	        </tr>
	        <tr>
	            <td align=left> file-utils</td>
	            <td align=center> ACTIVE</td>
	            <td align=left>
	                <p> Provides basic set of file manipulation utilities</p>
	            </td>
	            <!-- <td align=left><p></p></td> -->
	            <!-- <td align=left><p></p></td> -->
	        </tr>
	        <tr>
	            <td align=left> go-basic</td>
	            <td align=center> ACTIVE</td>
	            <td align=left>
	                <p> Provides basic Go language development</p>
	            </td>
	            <!-- <td align=left><p></p></td> -->
	            <!-- <td align=left><p></p></td> -->
	        </tr>
	        <tr>
	            <td align=left> go-extras</td>
	            <td align=center> ACTIVE</td>
	            <td align=left>
	                <p> Most popular Golang libraries</p>
	                <li>Includes (go-basic) bundle.</p>
	            </td>
	            <!-- <td align=left><p></p></td> -->
	            <!-- <td align=left><p></p></td> -->
	        </tr>
	        <tr>
	            <td align=left> hpc-basic</td>
	            <td align=center> ACTIVE</td>
	            <td align=left>
	                <p> Provides basic suite of MPI/HPC development tools</p>
	                <li>Includes (os-core-dev) bundle.</p>
	            </td>
	            <!-- <td align=left><p></p></td> -->
	            <!-- <td align=left><p></p></td> -->
	        </tr>
	        <tr>
	            <td align=left> iot</td>
	            <td align=center> WIP</td>
	            <td align=left>
	                <p> The IoT (Internet of Things) base bundle</p>
	            </td>
	            <!-- <td align=left><p></p></td> -->
	            <!-- <td align=left><p></p></td> -->
	        </tr>
	        <tr>
	            <td align=left> kernel-container</td>
	            <td align=center> WIP</td>
	            <td align=left>
	                <p> Provides a Linux kernel appropriate for a Clear Container</p>
	            </td>
	            <!-- <td align=left><p></p></td> -->
	            <!-- <td align=left><p></p></td> -->
	        </tr>
	        <tr>
	            <td align=left> kernel-kvm</td>
	            <td align=center> ACTIVE</td>
	            <td align=left>
	                <p> Provides a Linux kernel appropriate for running under KVM</p>
	                <li>Includes (bootloader) bundle.</p>
	            </td>
	            <!-- <td align=left><p></p></td> -->
	            <!-- <td align=left><p></p></td> -->
	        </tr>
	        <tr>
	            <td align=left> kernel-native</td>
	            <td align=center> ACTIVE</td>
	            <td align=left>
	                <p> Provides a Linux kernel appropriate for physical machines</p>
	                <li>Includes (bootloader) bundle.</p>
	            </td>
	            <!-- <td align=left><p></p></td> -->
	            <!-- <td align=left><p></p></td> -->
	        </tr>
	        <tr>
	            <td align=left> kernel-pxe</td>
	            <td align=center> ACTIVE</td>
	            <td align=left>
	                <p> Provides a Linux kernel linking an initramfs as root</p>
	            </td>
	            <!-- <td align=left><p></p></td> -->
	            <!-- <td align=left><p></p></td> -->
	        </tr>
	        <tr>
	            <td align=left> koji</td>
	            <td align=center> WIP</td>
	            <td align=left>
	                <p> Sets up a koji build service (builder-only, for now) based on NFS mounts.</p>
	            </td>
	            <!-- <td align=left><p></p></td> -->
	            <!-- <td align=left><p></p></td> -->
	        </tr>
	        <tr>
	            <td align=left> kvm-host</td>
	            <td align=center> WIP</td>
	            <td align=left>
	                <p> Provides necessary tools to run usable virtual machines with QEMU-KVM (independently of OpenStack).</p>
	                <li>Includes (kernel-kvm) bundle.</p>
	            </td>
	            <!-- <td align=left><p></p></td> -->
	            <!-- <td align=left><p></p></td> -->
	        </tr>
	        <tr>
	            <td align=left> lamp-basic</td>
	            <td align=center> ACTIVE</td>
	            <td align=left>
	                <p> Basic LAMP Server (apache2, mariadb, php5)</p>
	            </td>
	            <!-- <td align=left><p></p></td> -->
	            <!-- <td align=left><p></p></td> -->
	        </tr>
	        <tr>
	            <td align=left> mail-utils</td>
	            <td align=center> WIP</td>
	            <td align=left>
	                <p> Provides utilities for reading and sending email</p>
	            </td>
	            <!-- <td align=left><p></p></td> -->
	            <!-- <td align=left><p></p></td> -->
	        </tr>
	        <tr>
	            <td align=left> message-broker-rabbitmq</td>
	            <td align=center> ACTIVE</td>
	            <td align=left>
	                <p> Provides the RabbitMQ messaging service</p>
	            </td>
	            <!-- <td align=left><p></p></td> -->
	            <!-- <td align=left><p></p></td> -->
	        </tr>
	        <tr>
	            <td align=left> net-utils</td>
	            <td align=center> ACTIVE</td>
	            <td align=left>
	                <p> Provides an essential suite of core networking configuration and debug tools</p>
	            </td>
	            <!-- <td align=left><p></p></td> -->
	            <!-- <td align=left><p></p></td> -->
	        </tr>
	        <tr>
	            <td align=left> network-advanced</td>
	            <td align=center> WIP</td>
	            <td align=left>
	                <p> More utilities for advanced host-level networking; bridge, switch, netfilter, vpn etc.</p>
	            </td>
	            <!-- <td align=left><p></p></td> -->
	            <!-- <td align=left><p></p></td> -->
	        </tr>
	        <tr>
	            <td align=left> network-basic</td>
	            <td align=center> ACTIVE</td>
	            <td align=left>
	                <p> Provides a basic suite of networking utilities</p>
	            </td>
	            <!-- <td align=left><p></p></td> -->
	            <!-- <td align=left><p></p></td> -->
	        </tr>
	        <tr>
	            <td align=left> network-proxy-client</td>
	            <td align=center> WIP</td>
	            <td align=left>
	                <p> Tools for dealing with client-side network proxy settings.</p>
	            </td>
	            <!-- <td align=left><p></p></td> -->
	            <!-- <td align=left><p></p></td> -->
	        </tr>
	        <tr>
	            <td align=left> openssh-server</td>
	            <td align=center> ACTIVE</td>
	            <td align=left>
	                <p> Provides an SSH server (and client)</p>
	            </td>
	            <!-- <td align=left><p></p></td> -->
	            <!-- <td align=left><p></p></td> -->
	        </tr>
	        <tr>
	            <td align=left> openstack-all-in-one</td>
	            <td align=center> WIP</td>
	            <td align=left>
	                <p> Provides an All-in-one OpenStack deployment</p>
	                <li>Includes (database-mariadb) bundle.</p>
	                    <li>Includes (database-mongodb) bundle.</p>
	                        <li>Includes (message-broker-rabbitmq) bundle.</p>
	                            <li>Includes (openstack-block-storage) bundle.</p>
	                                <li>Includes (openstack-block-storage-controller) bundle.</p>
	                                    <li>Includes (openstack-compute) bundle.</p>
	                                        <li>Includes (openstack-compute-controller) bundle.</p>
	                                            <li>Includes (openstack-dashboard) bundle.</p>
	                                                <li>Includes (openstack-database) bundle.</p>
	                                                    <li>Includes (openstack-identity) bundle.</p>
	                                                        <li>Includes (openstack-image) bundle.</p>
	                                                            <li>Includes (openstack-lbaas) bundle.</p>
	                                                                <li>Includes (openstack-network) bundle.</p>
	                                                                    <li>Includes (openstack-object-storage) bundle.</p>
	                                                                        <li>Includes (openstack-orchestration) bundle.</p>
	                                                                            <li>Includes (openstack-python-clients) bundle.</p>
	                                                                                <li>Includes (openstack-telemetry-controller) bundle.</p>
	            </td>
	            <!-- <td align=left><p></p></td> -->
	            <!-- <td align=left><p></p></td> -->
	        </tr>
	        <tr>
	            <td align=left> openstack-block-storage</td>
	            <td align=center> WIP</td>
	            <td align=left>
	                <p> Provides an OpenStack Cinder service</p>
	            </td>
	            <!-- <td align=left><p></p></td> -->
	            <!-- <td align=left><p></p></td> -->
	        </tr>
	        <tr>
	            <td align=left> openstack-block-storage-controller</td>
	            <td align=center> WIP</td>
	            <td align=left>
	                <p> Provides an OpenStack Cinder controller service</p>
	            </td>
	            <!-- <td align=left><p></p></td> -->
	            <!-- <td align=left><p></p></td> -->
	        </tr>
	        <tr>
	            <td align=left> openstack-compute</td>
	            <td align=center> WIP</td>
	            <td align=left>
	                <p> Provides an OpenStack nova-compute node</p>
	            </td>
	            <!-- <td align=left><p></p></td> -->
	            <!-- <td align=left><p></p></td> -->
	        </tr>
	        <tr>
	            <td align=left> openstack-compute-controller</td>
	            <td align=center> WIP</td>
	            <td align=left>
	                <p> Provides an OpenStack Nova control server</p>
	            </td>
	            <!-- <td align=left><p></p></td> -->
	            <!-- <td align=left><p></p></td> -->
	        </tr>
	        <tr>
	            <td align=left> openstack-configure</td>
	            <td align=center> WIP</td>
	            <td align=left>
	                <p> Provides a suggested default configuration for OpenStack on Clear Linux.</p>
	            </td>
	            <!-- <td align=left><p></p></td> -->
	            <!-- <td align=left><p></p></td> -->
	        </tr>
	        <tr>
	            <td align=left> openstack-controller</td>
	            <td align=center> WIP</td>
	            <td align=left>
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
	            <td align=left> openstack-dashboard</td>
	            <td align=center> WIP</td>
	            <td align=left>
	                <p> Provides an OpenStack Horizon server</p>
	            </td>
	            <!-- <td align=left><p></p></td> -->
	            <!-- <td align=left><p></p></td> -->
	        </tr>
	        <tr>
	            <td align=left> openstack-database</td>
	            <td align=center> WIP</td>
	            <td align=left>
	                <p> Provides a Database as a Service server</p>
	            </td>
	            <!-- <td align=left><p></p></td> -->
	            <!-- <td align=left><p></p></td> -->
	        </tr>
	        <tr>
	            <td align=left> openstack-identity</td>
	            <td align=center> WIP</td>
	            <td align=left>
	                <p> Provides an OpenStack Keystone server</p>
	            </td>
	            <!-- <td align=left><p></p></td> -->
	            <!-- <td align=left><p></p></td> -->
	        </tr>
	        <tr>
	            <td align=left> openstack-image</td>
	            <td align=center> WIP</td>
	            <td align=left>
	                <p> Provides an OpenStack Glance server</p>
	            </td>
	            <!-- <td align=left><p></p></td> -->
	            <!-- <td align=left><p></p></td> -->
	        </tr>
	        <tr>
	            <td align=left> openstack-lbaas</td>
	            <td align=center> WIP</td>
	            <td align=left>
	                <p> Provides Load Balancing as a Service</p>
	            </td>
	            <!-- <td align=left><p></p></td> -->
	            <!-- <td align=left><p></p></td> -->
	        </tr>
	        <tr>
	            <td align=left> openstack-network</td>
	            <td align=center> WIP</td>
	            <td align=left>
	                <p> Provides an OpenStack Neutron server</p>
	            </td>
	            <!-- <td align=left><p></p></td> -->
	            <!-- <td align=left><p></p></td> -->
	        </tr>
	        <tr>
	            <td align=left> openstack-object-storage</td>
	            <td align=center> WIP</td>
	            <td align=left>
	                <p> Provides an OpenStack Swift service</p>
	            </td>
	            <!-- <td align=left><p></p></td> -->
	            <!-- <td align=left><p></p></td> -->
	        </tr>
	        <tr>
	            <td align=left> openstack-orchestration</td>
	            <td align=center> WIP</td>
	            <td align=left>
	                <p> Provides an OpenStack Heat service</p>
	            </td>
	            <!-- <td align=left><p></p></td> -->
	            <!-- <td align=left><p></p></td> -->
	        </tr>
	        <tr>
	            <td align=left> openstack-python-clients</td>
	            <td align=center> WIP</td>
	            <td align=left>
	                <p> Provides OpenStack command-line utilities</p>
	            </td>
	            <!-- <td align=left><p></p></td> -->
	            <!-- <td align=left><p></p></td> -->
	        </tr>
	        <tr>
	            <td align=left> openstack-telemetry-controller</td>
	            <td align=center> WIP</td>
	            <td align=left>
	                <p> Provides an OpenStack Telemetry server</p>
	            </td>
	            <!-- <td align=left><p></p></td> -->
	            <!-- <td align=left><p></p></td> -->
	        </tr>
	        <tr>
	            <td align=left> openstack-test-suite</td>
	            <td align=center> WIP</td>
	            <td align=left>
	                <p> Provides an OpenStack Tempest/test suite </p>
	            </td>
	            <!-- <td align=left><p></p></td> -->
	            <!-- <td align=left><p></p></td> -->
	        </tr>
	        <tr>
	            <td align=left> os-cloudguest</td>
	            <td align=center> WIP</td>
	            <td align=left>
	                <p> Provides cloud-init cloud guest configuration utilities</p>
	                <li>Includes (openssh-server) bundle.</p>
	                    <li>Includes (telemetrics) bundle.</p>
	            </td>
	            <!-- <td align=left><p></p></td> -->
	            <!-- <td align=left><p></p></td> -->
	        </tr>
	        <tr>
	            <td align=left> os-clr-on-clr</td>
	            <td align=center> WIP</td>
	            <td align=left>
	                <p> content for development of the Clear Linux OS on the Clear Linux OS</p>
	                <li>Includes (storage-utils) bundle.</p>
	                    <li>Includes (mail-utils) bundle.</p>
	            </td>
	            <!-- <td align=left><p></p></td> -->
	            <!-- <td align=left><p></p></td> -->
	        </tr>
	        <tr>
	            <td align=left> os-core</td>
	            <td align=center> ACTIVE</td>
	            <td align=left>
	                <p> The basic core OS components of Clear Linux for iA </p>
	            </td>
	            <!-- <td align=left><p></p></td> -->
	            <!-- <td align=left><p></p></td> -->
	        </tr>
	        <tr>
	            <td align=left> os-core-dev</td>
	            <td align=center> ACTIVE</td>
	            <td align=left>
	                <p> Basic development tools</p>
	            </td>
	            <!-- <td align=left><p></p></td> -->
	            <!-- <td align=left><p></p></td> -->
	        </tr>
	        <tr>
	            <td align=left> os-core-update</td>
	            <td align=center> ACTIVE</td>
	            <td align=left>
	                <p> Provides basic suite for running the Clear Linux for iA Updater</p>
	            </td>
	            <!-- <td align=left><p></p></td> -->
	            <!-- <td align=left><p></p></td> -->
	        </tr>
	        <tr>
	            <td align=left> os-installer</td>
	            <td align=center> ACTIVE</td>
	            <td align=left>
	                <p> Provides an installer for Clear Linux for iA</p>
	                <li>Includes (telemetrics) bundle.</p>
	                    <li>Includes (network-proxy-client) bundle.</p>
	            </td>
	            <!-- <td align=left><p></p></td> -->
	            <!-- <td align=left><p></p></td> -->
	        </tr>
	        <tr>
	            <td align=left> os-testsuite</td>
	            <td align=center> WIP</td>
	            <td align=left>
	                <p> Provides basic test suite for Clear Linux for iA</p>
	            </td>
	            <!-- <td align=left><p></p></td> -->
	            <!-- <td align=left><p></p></td> -->
	        </tr>
	        <tr>
	            <td align=left> os-testsuite-phoronix</td>
	            <td align=center> ACTIVE</td>
	            <td align=left>
	                <p> All the required pieces for running the Phoronix Test Suite</p>
	                <li>Includes (os-utils) bundle.</p>
	                    <li>Includes (devtools-basic) bundle.</p>
	            </td>
	            <!-- <td align=left><p></p></td> -->
	            <!-- <td align=left><p></p></td> -->
	        </tr>
	        <tr>
	            <td align=left> os-utils</td>
	            <td align=center> ACTIVE</td>
	            <td align=left>
	                <p> Provides a core set of OS utilities</p>
	                <li>Includes (editors) bundle.</p>
	                    <li>Includes (dev-utils) bundle.</p>
	                        <li>Includes (sysadmin) bundle.</p>
	                            <li>Includes (network-basic) bundle.</p>
	                                <li>Includes (file-utils) bundle.</p>
	                                    <li>Includes (network-proxy-client) bundle.</p>
	            </td>
	            <!-- <td align=left><p></p></td> -->
	            <!-- <td align=left><p></p></td> -->
	        </tr>
	        <tr>
	            <td align=left> os-utils-gui</td>
	            <td align=center> ACTIVE</td>
	            <td align=left>
	                <p> Provides a graphical desktop environment </p>
	            </td>
	            <!-- <td align=left><p></p></td> -->
	            <!-- <td align=left><p></p></td> -->
	        </tr>
	        <tr>
	            <td align=left> perl-basic</td>
	            <td align=center> ACTIVE</td>
	            <td align=left>
	                <p> Provides essential Perl language and dev tools</p>
	            </td>
	            <!-- <td align=left><p></p></td> -->
	            <!-- <td align=left><p></p></td> -->
	        </tr>
	        <tr>
	            <td align=left> perl-extras</td>
	            <td align=center> ACTIVE</td>
	            <td align=left>
	                <p> Provides extra libraries for Perl</p>
	                <li>Includes (perl-basic) bundle.</p>
	            </td>
	            <!-- <td align=left><p></p></td> -->
	            <!-- <td align=left><p></p></td> -->
	        </tr>
	        <tr>
	            <td align=left> pnp-tools-advanced</td>
	            <td align=center> WIP</td>
	            <td align=left>
	                <p> Provides advanced Power and Performance measurement tools</p>
	            </td>
	            <!-- <td align=left><p></p></td> -->
	            <!-- <td align=left><p></p></td> -->
	        </tr>
	        <tr>
	            <td align=left> pnp-tools-basic</td>
	            <td align=center> WIP</td>
	            <td align=left>
	                <p> Provides basic Power and Performance testing tools</p>
	            </td>
	            <!-- <td align=left><p></p></td> -->
	            <!-- <td align=left><p></p></td> -->
	        </tr>
	        <tr>
	            <td align=left> pnp-tools-intermediate</td>
	            <td align=center> WIP</td>
	            <td align=left>
	                <p> Provides a deeper-level suite of Power and Performance testing tools</p>
	            </td>
	            <!-- <td align=left><p></p></td> -->
	            <!-- <td align=left><p></p></td> -->
	        </tr>
	        <tr>
	            <td align=left> python-basic</td>
	            <td align=center> ACTIVE</td>
	            <td align=left>
	                <p> Provides core Python language and libraries</p>
	            </td>
	            <!-- <td align=left><p></p></td> -->
	            <!-- <td align=left><p></p></td> -->
	        </tr>
	        <tr>
	            <td align=left> python-extras</td>
	            <td align=center> ACTIVE</td>
	            <td align=left>
	                <p> Provides extra libraries for Python</p>
	                <li>Includes (python-basic) bundle.</p>
	            </td>
	            <!-- <td align=left><p></p></td> -->
	            <!-- <td align=left><p></p></td> -->
	        </tr>
	        <tr>
	            <td align=left> R-basic</td>
	            <td align=center> ACTIVE</td>
	            <td align=left>
	                <p> Provides core R language and libraries</p>
	            </td>
	            <!-- <td align=left><p></p></td> -->
	            <!-- <td align=left><p></p></td> -->
	        </tr>
	        <tr>
	            <td align=left> R-extras</td>
	            <td align=center> ACTIVE</td>
	            <td align=left>
	                <p> Provides deeper functionality R language libraries</p>
	                <li>Includes (R-basic) bundle.</p>
	            </td>
	            <!-- <td align=left><p></p></td> -->
	            <!-- <td align=left><p></p></td> -->
	        </tr>
	        <tr>
	            <td align=left> ruby-basic</td>
	            <td align=center> ACTIVE</td>
	            <td align=left>
	                <p> Top 3 basic Ruby Libraries</p>
	            </td>
	            <!-- <td align=left><p></p></td> -->
	            <!-- <td align=left><p></p></td> -->
	        </tr>
	        <tr>
	            <td align=left> ruby-extras</td>
	            <td align=center> ACTIVE</td>
	            <td align=left>
	                <p> Top 3 to 6 basic Ruby Libraries</p>
	                <li>Includes (ruby-basic) bundle.</p>
	            </td>
	            <!-- <td align=left><p></p></td> -->
	            <!-- <td align=left><p></p></td> -->
	        </tr>
	        <tr>
	            <td align=left> shells</td>
	            <td align=center> ACTIVE</td>
	            <td align=left>
	                <p> All available shell programs for Clear, along with ancillary files</p>
	            </td>
	            <!-- <td align=left><p></p></td> -->
	            <!-- <td align=left><p></p></td> -->
	        </tr>
	        <tr>
	            <td align=left> storage-utils</td>
	            <td align=center> ACTIVE</td>
	            <td align=left>
	                <p> Provides basic storage-related utilities</p>
	            </td>
	            <!-- <td align=left><p></p></td> -->
	            <!-- <td align=left><p></p></td> -->
	        </tr>
	        <tr>
	            <td align=left> sysadmin</td>
	            <td align=center> ACTIVE</td>
	            <td align=left>
	                <p> Provides a basic set of system administration utilities.</p>
	            </td>
	            <!-- <td align=left><p></p></td> -->
	            <!-- <td align=left><p></p></td> -->
	        </tr>
	        <tr>
	            <td align=left> telemetrics</td>
	            <td align=center> ACTIVE</td>
	            <td align=left>
	                <p> Provides the Telemetrics client for Clear Linux for iA</p>
	            </td>
	            <!-- <td align=left><p></p></td> -->
	            <!-- <td align=left><p></p></td> -->
	        </tr>
	        <tr>
	            <td align=left> virtualbox-guest</td>
	            <td align=center> ACTIVE</td>
	            <td align=left>
	                <p> Include the modules and binaries meant to be used as a VirtualBox instance</p>
	            </td>
	            <!-- <td align=left><p></p></td> -->
	            <!-- <td align=left><p></p></td> -->
	        </tr>
	    </tbody>
	</table>