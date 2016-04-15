.. _ciao-cluster-setup:

.. contents::

ciao cluster setup
##################


This topic explains how to set up a cluster of machines running Clear Linux* OS
for Intel® Architecture with :abbr:`Cloud Integrated Advanced Orchestrator (CIAO)`, or ciao.

While the table of contents provides links to specific points of information, this
topic is intended as an ordered workflow. Be sure to start your cluster components
in the correct order as explained below.

Infrastructure prerequisites
============================

Hardware needs
--------------

You'll need at least four machines and a switch connecting them to form
your beginning ciao cluster. The switch is assumed to be plugged directly
into an "upstream" network running a DHCP server. The following examples
assume you have four nodes on a ``192.168.0.0/16`` network:

Controller node
~~~~~~~~~~~~~~~

* IP ``192.168.0.101``
* Runs Controller, Scheduler, SSL Keystone.


Network node ("nn")
~~~~~~~~~~~~~~~~~~~

* IP ``192.168.0.102``
* Runs Launcher with ``--network=nn`` option
* Has CNCI image in ``/var/lib/ciao/images``. See below for more on CNCI image preparation.

Compute node 1 ("cn1")
~~~~~~~~~~~~~~~~~~~~~~

* IP ``192.168.0.103``
* Runs Launcher with ``--network=cn`` option
* Has workload images in ``/var/lib/ciao/images``

Compute node 2 ("cn2")
~~~~~~~~~~~~~~~~~~~~~~

* ``IP 192.168.0.104``
* Runs Launcher with ``--network=cn option``
* Has workload images in ``/var/lib/ciao/images``


Network needs
-------------


Our system assumes cluster nodes have full connectivity at a routed
IP level.  Additionally, the network node must have access to a DHCP
server which serves address which also are routable across the cluster.

It is possible to use a corporate or a lab network and not install a
separate DHCP server; however, the DHCP server and network management
infrastructure supplying your switch's upstream port needs to allow you
to have enough IPs for your nodes and some appliance VMs ciao runs for
network management purposes.  One of these ``CNCI`` appliances (Compute
Node Concentrator Instance, see the `CNCI Agent`_ documentation for more
information) is run for each tenant network.  If you're testing with
two tenants, you will have to CNCI VMs, each needing one DHCP address.

.. note::

  If you are using ``dnsmasq`` as your DHCP/DNS server, complete the following:

  #. Ensure that the ``dhcp-sequential-ip`` option is set.
  #. Configure ``dhcp-host=*:*:*:*:*:*,id:*`` to ensure that the CNCIs get
     unique IP addresses even when their hostnames are the same inside the VM. A
  #. Set up static MAC to IP mappings (using the dhcp-host option) for your cluster
     nodes to ensure you never lose network connectivity.
  #. Configure a dynamic range within the subnet with enough IPs for the
     number of tenant CNCI instances you wish to run.

Node setup
==========

Install Clear Linux OS for Intel Architecture as host on all nodes
------------------------------------------------------------------

Install Clear Linux OS for Intel Architecture as the host
OS on all nodes by following the instructions in the topic 
:ref:`gs_installing_clr_as_host`. The current April 2016
`downloadable images`_ are compatible with ciao.

After the installation, complete the following steps:

#. Ensure your system is 100% up to date::

    $ swupd verify

#. If the above command does not show zero failures, run the command below repeatedly
   until it shows zero uncorrected errors.::

    $ swupd verify --fix

#. After the installation is verified as up-to-date, add the following additional bundle,
   which adds componenents needed by CIAO::

    $ swupd bundle-add cloud-control

#. As a final double check, run the updater again and then repair if any errors persist::

    $ swupd verify
    $ swupd verify --fix


Build the CIAO software
-----------------------

#. On your development machine, obtain the relevant ciao packages by following
   the instructions given at :ref:`go-get-ciao`. Note that this is not a complete
   manual on how to use the ``go get`` tool, but it contains enough information
   to help experienced developers obtain the binaries needed to build ciao.

#. Install and build the binaries needed for ciao::

   $ cd $GOPATH/src github.com/01org/ciao
   $ go install ./...

The binaries will install to ``$GOPATH/bin``. You should have ``cnci_agent``, ``ciao-launcher``, ``ciao-controller``, and ``ciao-scheduler``.

Build certificates
------------------

Create the ssntp-internal communications certificates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

On your development machine, generate the certificates for each of your
roles; general instructions can be found under the `ciao-cert`_ documentation.

Pass in the host name for the host on which you will be running the service
when generating the certificate.

Create unique certificates for each of your scheduler, compute node and network
node launchers, cnciagent, controller, and the CNCI launcher; save each with a
unique name. The names, locations, and contents (signer and role) of the
certificates are very important. The rest of this topic will consistently use
the following example file names:

* ``CAcert-[scheduler-node-hostname].pem``: copy to all nodes' ``/etc/pki/ciao`` and the CNCI image's ``/var/lib/ciao``. See below for more on CNCI image preparation.
* ``cert-CNAgent-localhost.pem``: copy to all compute nodes' ``/etc/pki/ciao``.
* ``cert-CNCIAgent-localhost.pem``: copy into your CNCI image's ``/var/lib/ciao``. See below for more on CNCI image preparation.
* ``cert-Controller-localhost.pem``: copy into your controller node's ``/etc/pki/ciao``.
* ``cert-NetworkingAgent-localhost.pem``: copy into your network node's ``/etc/pki/ciao``.
* ``cert-Scheduler-[scheduler-node-hostname].pem``: copy into your controller node's ``/etc/pki/ciao``.

Create the controller web certificates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

On your development box, generate ssl certificates for the controller's https service::

    $ openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout controller_key.pem -out controller_cert.pem

Copy the ``controller_cert.pem`` and ``controller_key.pem`` files to your
controller node.  You can use the same location where you will be storing
your controller binary (ciao-controller).  For our dev test clusters, the keys
are already in ``/etc/pki/ciao``.

You'll also need to pull that certificate into your browser as noted below in
the `Starting a workload` section.

Keystone node
-------------

Some node needs to run your Keystone service. You can run it anywhere
that is network accessible from both your control node's controller software
and your web browser. For convenience, you might run it on your control
node or on your network node. General documentation on setting up Keystone
services can be found at the `Openstack developer`_ website.


Controller node setup
---------------------

The controller node will host your controller and scheduler. Certificates are assumed
to be in ``/etc/pki/ciao``, generated with the correct roles and names
as previously described.

Scheduler
~~~~~~~~~

Copy in the scheduler binary from your build/develop machine to any
location, then launch it first (does not require root)::

    ./ciao-scheduler --cacert=/etc/pki/ciao/CAcert-[scheduler-node-hostname].pem --cert=/etc/pki/ciao/cert-Scheduler-[scheduler-node-hostname].pem --heartbeat

With the optional ``--heartbeat`` option, the scheduler console will
output once per second a heartbeat message showing connected Controller
and Compute Node client statistics. It also displays a line of
information for each command or event traversing the SSNTP server.
As the sole SSNTP server in the ciao cluster, it is a key debugging point
to understand failed flows of actions/reactions across your cluster.
Launching it first means this console output helps confirm your subsequent
cluster configurations actions are indeed succeeding.

ciao-controller
~~~~~~~~~~~~~~~

**Important: Do not start the ciao controller just yet!** It should only
be started after a network node is connected to the scheduler; otherwise
workloads may fail to start. This restriction will be adressed once 
`ciao issue #12`_ is closed.

Compute node setup
------------------

Each compute node needs one launcher daemon connected to the scheduler.
Certificates are assumed to be in ``/etc/pki/ciao``, generated with the
correct roles and names as previously described.

Copy in the launcher binary from your build/development machine to any
location.

Prepopulate the OS image cache
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We have tested the `Fedora 23 cloud image`_, Clear Linux OS for Intel
Architecture cloud `downloadable images`_, and an Ubuntu image. Each will
be referenced very specifically by a UUID in our configuration files, so
follow the instructions here exactly. Symlinks are used so you, as a human,
can easily see which image is which with a human-readable name, while still
having the UUID-name file nodes that the cloud config expects. 

Fedora* Cloud::

    <Insert link here>

Clear Linux OS for Intel Architecture Cloud::

    <Insert link here>

Ubuntu::

    <Insert link here>

Start the compute node launcher
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The launcher is run with options declaring certificates, maximum VMs
(controls when "FULL" is returned by a node, scale to the resources
available on your node), server location, and compute node ("cn")
launching type. For example::

    sudo ./launcher --cacert=/etc/pki/ciao/CAcert-[scheduler-node-hostname].pem --cert=/etc/pki/ciao/cert-CNAgent-localhost.pem --server=<your-server-address> --network=cn

Optionally add ``-logtostderr`` (more verbose with also ``-v=2``) to get
console logging output.

The launcher runs as root because launching qemu/kvm virtual machines
requires ``/dev/kvm`` and other restricted resource access.

Network node setup
------------------

The network node hosts VMs running the Compute Network Concentrator(s)
Instance "CNCI" agent, one per tenant. These VMs are automatically
launched by the controller.

Certificates are assumed to be in ``/etc/pki/ciao``, generated with the
correct roles and names as previously described.

Pre-populate the CNCI image cache
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This section describes how to generate a CNCI image from a vanilla
clear cloud qcow2 image::

  $ cd /var/lib/ciao/images
  $ curl -O https://download.clearlinux.org/demos/ciao/clear-7370-ciao-networking.img.xz
  $ xz -T0 --decompress clear-7370-ciao-networking.img.xz
  $ ln -s clear-7370-ciao-networking.img 4e16e743-265a-4bf2-9fd1-57ada0b28904
  $ $GOPATH/src/github.com/01org/ciao/networking/cnci_agent/scripts/update_cnci_cloud_image.sh /var/lib/ciao/images/clear-7370-ciao-networking.img /etc/pki/ciao/

Start the network node launcher
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The network node's launcher is run almost the same as the compute node.
The primary difference is that it uses the network node ("nn") launching
type::

  $ sudo ./ciao-launcher --cacert=/etc/pki/ciao/CAcert-[scheduler-node-hostname].pem --cert=/etc/pki/ciao/cert-NetworkingAgent-localhost.pem --server=<your-server-address> --network=nn

Starting the controller
=======================

Starting the Controller on the controller node is what truly activates your
cluster for use. **NOTE: Before starting the controller you must have a scheduler
and network node already up and running together.**

#. Copy in the ciao-controller binary from your build/development machine to any
   location. Certificates are assumed to be in ``/etc/pki/ciao``, generated with
   the correct roles and names as previously described.

#. Copy in the initial database table data from the ciao-controller source
   (``$GOPATH/src/github.com/01org/ciao/ciao-controller`` on your
   build/development) to the same directory as the ciao-controller binary.
   Copying in ``*.csv`` will work.

#. Copy in the controller html templates from the ciao-controller source to the
   same directory as the ciao-controller binary. Copying in ``*.gtpl`` will work.

#. Copy in the test.yaml file from
   ``$GOPATH/src/github.com/01org/ciao/ciao-controller/test.yaml``.

The `ciao-controller workload_resources.csv`_ and the 
`ciao-controller workload_template.csv`_ have four stanzas, so yours
should as well to successfully run each of the four images currently
described earlier on this page (ie: Fedora, Clear, Docker Ubuntu, CNCI). 
To run other images of your choosing you'd do similar to the above for
pre-populating OS images, and similarly edit these two files on your
controller node.

If the controller is on the same physical machine as the scheduler, the
``--url`` option is optional; otherwise it refers to your scheduler
SSNTP server IP.

In order for the ciao-controller go code to correctly use the CA
certificate generated earlier when you built your keystone server,
this certificate needs to be installed in the control node and be
part of the control node CA root. On Clear Linux OS for Intel
Architecture, this is accomplished with::

    $ sudo mkdir /etc/ca-certs
    $ sudo cp cacert.pem /etc/ca-certs
    $ sudo c_hash /etc/ca-certs/cacert.pem
    
Note the generated hash from the prior command and use it in the next commands::

    $ sudo ln -s /etc/ca-certs/cacert.pem /etc/ca-certs/<hashvalue>
    $ sudo mkdir /etc/ssl
    $ sudo ln -s /etc/ca-certs/ /etc/ssl/certs
    $ sudo ln -s /etc/ca-certs/cacert.pem /usr/share/ca-certs/<hashvalue>

You will need to tell the controller where the keystone service is located and
pass it the Ciao service username and password. DO NOT USE
localhost for your server name. **It must be the fully qualified DNS
name of the system which is hosting the keystone service**.
An SSL-enabled Keystone is required, with additional parameters
for ciao-controller pointing at its certificates::

  $ sudo ./ciao-controller --cacert=/etc/pki/ciao/CAcert-[scheduler-node-hostname].pem --cert=/etc/pki/ciao/cert-Controller-localhost.pem -identity=https://[keystone-FQDN]:35357 --username=<Ciao keystone service username> --password=<Ciao keystone service password> --url <scheduler-FQDN> --httpskey=./key.pem --httpscert=./cert.pem

Optionally add ``-logtostderr`` (more verbose with also ``-v=2``) to get
console logging output.

Point a browser at your controller node. For example:

`https://192.168.0.101:8889/stats <http://192.168.0.101:8889/stats>`__

You should see a page with graphs showing resource data for your
connected nodes, a table of your Network node's CNCI VM status (each
with an IP from your upstream net's dhcp server), a blank event log and
a blank list of compute workload instances.


Starting a workload
===================

Because we are using self-signed certificates and our debug code counts
on AJAX being able to communicate directly with the keystone service,
you need to find a way to accept the certificate for the keystone
service before you will be able to launch a workload. For some browsers,
it's sufficient to go to the controller's web server and accept the
certificate. You may also update your system's CA certs on the system your
browser is running on to include the keystone ``.pem`` file. You'll have to
check your operating system's instructions on how to do this. For Chrome*
on Linux, other problems persist, so that browser is unfortunately not
a working option at this time.

To start a workload, you will first need to log in as a valid user with
permissions for one or more projects (tenants).

`https://192.168.0.1:8889/login <http://192.168.0.1:8889/login>`__

Login information will be validated to the keystone service. After
successful login, you will be redirected to a page where you can launch
workloads.

#. Select a tenant, such as: "Ciao Test User No Limits".
#. Select an image, such as: "Clear Cloud".
#. Enter an instance count, such as: "1".
#. Press "Send".

If you would like to see performance data, you may optionally check the
"trace" box and provide a label for the test run. These stats will be
available to you from the controller node stats UI.

You should note a change in activity in the `controller node stats
UI <http://192.168.0.101:8889/stats>`__, with a new VM showing as
pending and then running.

The Clear Cloud VM consumes a bit more than 128MB of RAM; so within
~30 seconds (the refresh rate of the stats page), you should see the
status as ``running`` instead of ``pending``.

You will also see activity related to this launch across your cluster
components if you've got consoles open and logging to standard output as
described above.

Resetting your cluster
======================

In the `controller node stats UI <http://192.168.0.101:8889/stats>`__:

#. Select and delete all workload VM instances.
#. Stop all daemons.
#. Delete the "ciao-controller.db" from the directory in which you ran the
   "ciao-controller" binary.
#. Delete "/tmp/ciao-controller-stats.db".

On the network node, run the following commands::

  $ sudo killall -9 qemu-system-x86_64
  $ sudo rm -rf /var/lib/ciao/instances/
  $ sudo reboot

If you were unable to successfully delete all workload VM instances
through the UI, then on each compute node run these commands::

  $ sudo killall -9 qemu-system-x86_64
  $ sudo rm -rf /var/lib/ciao/instances/
  $ sudo reboot

Restart your scheduler, network node launcher, compute node launcher,
and controller.

Debug tips
==========

General debug
-------------

For general debuging, you can:

* Reset you cluster.
* Pull in up to date go binaries.
* Enable verbose console logging.
* Reduce your tenants to one (specifically the one with no limits).
* Launch less VMs in a herd. Our NUC's can handle approx. <= 50-100
  starting at once per compute node. Our Haswell-EP servers can handle
  approx. <= 500 starting at once per compute node.
* Tweak the launcher to enable remote access. For example, when using netcat, if you Control-C, that kills netcat.
  Instead from the host, send a Control-C via netcat to the target as::

    echo -ne "99||\x03" | netcat 192.168.0.102 6309

* Ssh into the node(s) by IP, look at top, df, ps, ip a, ip r, netstat -a, etc.
* Ssh into the CNCI(s) by IP, look at top, df, ps, ip a, ip r, netstat -a,
  etc. (KVM Image: username: root password: supernova) (Cloud Image: username: supernova Password: supernova)
* Ssh into the workload instance VM by CNCI IP and port ``33000+ip[2]<<8+ip[3]``.

Controller debug
----------------

The controller's port 8889 listener has a number of interesting debug data
outputs at urls like:

* `hostname:8889/workload <http://hostname:8889/workload>`__
* `hostname:8889/debug <http://hostname:8889/debug>`__
* `hostname:8889/tenantDebug <http://hostname:8889/tenantDebug>`__
* `hostname:8889/stats <http://hostname:8889/stats>`__
* `hostname:8889/login <http://hostname:8889/login>`__
* `hostname:8889/getNodeStats <http://hostname:8889/getNodeStats>`__
* `hostname:8889/getInstances <http://hostname:8889/getInstances>`__
* `hostname:8889/getTenants <http://hostname:8889/getTenants>`__
* `hostname:8889/getEventLog <http://hostname:8889/getEventLog>`__
* `hostname:8889/getNodeSummary <http://hostname:8889/getNodeSummary>`__
* `hostname:8889/getWorkloads <http://hostname:8889/getWorkloads>`__
* `hostname:8889/getCNCI <http://hostname:8889/getCNCI>`__

Network debug
-------------

Data center DHCP server
~~~~~~~~~~~~~~~~~~~~~~~

The Data Center DHCP server is the server that serves the Physical
network.

We have seen a tendency for the Data Center DHCP server to serve out the
same IP address to all the CNCIs.

Check the DHCP server lease file to ensure that each CNCI has a
different IP address. The UI will also show this.

If the CNCI's do not have different IP addresses, nothing will work
properly.

Reset the DHCP server, clear its leases and then reset the cluster. A
script that can do this is::

    echo 0 > /proc/sys/net/ipv4/ip_forward
    iptables -F
    iptables -t nat -F
    iptables -t mangle -F
    iptables -X
    iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
    iptables -A FORWARD -i eth0 -o eth1 -m state --state RELATED,ESTABLISHED -j ACCEPT
    iptables -A FORWARD -i eth1 -o eth0 -j ACCEPT
    #iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 8889 -j DNAT --to 192.168.0.101:8889
    #iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 35357 -j DNAT --to 192.168.0.101:35357
    #iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 5000 -j DNAT --to 192.168.0.101:5000
    iptables -t nat -A PREROUTING -p tcp --dport 8889 -j DNAT --to 192.168.0.101:8889
    iptables -t nat -A PREROUTING -p tcp --dport 35357 -j DNAT --to 192.168.0.101:35357
    iptables -t nat -A PREROUTING -p tcp --dport 5000 -j DNAT --to 192.168.0.101:5000
    echo 1 > /proc/sys/net/ipv4/ip_forward
    killall dnsmasq
    rm -f /var/lib/misc/tenant_dns.leases
    dnsmasq -C tenant_dns.cfg

Compute node
~~~~~~~~~~~~

Once instances are created, do the following:

#. Run this command to Check the gre tunnels to find out the CNCI IP address for each interface::

    ip -d link | grep alias

#. Ensure that you can ping the CNCI IP from the CN IP. If not you have a problem with base network connectivity.
#. Check that you can ping the Scheduler IP.
#. Make sure your top level DHCP server always serves the same IP address to the same compute node.
   If not you will have issues restarting the cluster easily.
#. If you are using dnsmasq use the dhcp-host option to achieve this. For example::

    dhcp-host=c0:3f:d5:63:13:d9,192.168.0.101

   The above is example only. Insert your MAC and the desired IP address.

Network node
~~~~~~~~~~~~

Complete the following:

#. Make sure your top-level DHCP server always serves the same IP address
   to the same network node.
#. Check that you can ping the Scheduler IP.
#. Check that you can ping all the CNs::

    $ ip -d link | grep alias

   Note: You *cannot* ping the CNCI IP from the same Network Node (a
   macvtap vepa mode limitation). However you can ping it with any other NN or CN/

#. For Data Center DHCP Server, check that the CNCI MAC addresses all show up with unique IP addresses.
   If not your DHCP server may not be able to handle large volume of DHCP
   requests coming very close to on another.

   * If you are using dnsmasq as your DHCP/DNS Server ensure that the dhcp-sequential-ip option is set.

#. Or, if your DHCP server is spec compliant and is seeing duplicate
   client-id's (ie: multiple vm's with the same hostname):

   * If you are using dnsmasq, you can choose to be spec-non-compliant and
     work around with::

       dhcp-host=*:*:*:*:*:*,id:*

   * The above command instructs: "For all source MAC's, ignore the client id."

CNCI image
~~~~~~~~~~

Complete the following:

#. Ensure that the CNCI Image has both dnsmasq and iptables installed.
#. In case of systemd-based operating systems, ensure that ``UseMTU=true``. The default is sometimes false, but in newer bundles
   of Clear Linux OS for Intel Architecture, the default is set to true.

CNCI
~~~~

Complete the following:

#. ssh into the CNCI (user: UPDATE with password UPDATE).
#. Run the following command::

    $ systemctl status cnci-agent -l

   * Check that the agent is running.
   * Ensure that it is connecting to the correct scheduler address.
   * Check that its UUID matches the controller-generated UUID for the CNCI.

#. If the cnci-agent failed to start, run the command below to determine the reason::

    $ journalctl -b

Once instances are created:

#. Check that you can ping the instance IP address.
#. ``ip -d link | grep alias``: Check to see that there exists a gre tunnel to the CN.
#. ``ps auxw | grep dns``: Check to see that a dnsqmasq running on behalf of the tenant subnet.
#. ``cat /tmp/dns*leases``: Check to see that your instance has connected to CNCI and requested an IP address. If you do not
   see your instance MAC in the leases, it means your VM never connected to the CNCI, which
   means that the VM will not have network access.
#. ``iptables-save``: Check to see the ssh forwarding rules are setup correctly.

Instance
~~~~~~~~

Complete the following:

#. In case of systemd-based operating systems, ensure that ``UseMTU=true``. The
   default is sometimes false, but in newer bundles of Clear Linux OS for Intel Architecture, the default is set to true.
#. If the instance cannot be pinged from the CNCI as inferred from
   ``ip -d link | grep alias``:

   * Check that the interface is setup correctly to perform DHCP.
   * Check that the launcher is attaching the right interface to the VM.
   * Check that the interface exists on the CN and is attached to the right
     bridge and is attached to the right tunnel.

#. If the instance can be pinged but you cannot SSH into the instance:

   * Check the MTU set on the interface. The MTU has to match the MTU sent by the CNCI (1400 currently).
   * If the MTU on the interface is still 1500, then the DHCP client on the instance does not respect the MTU sent in by the DHCP server.

.. _ciao issue #12: https://github.com/01org/ciao/issues/12
.. _ciao-controller workload_resources.csv: https://github.com/01org/ciao/blob/master/ciao-controller/workload_resources.csv
.. _ciao-controller workload_template.csv: https://github.com/01org/ciao/blob/master/ciao-controller/workload_template.csv
.. _downloadable images: https://download.clearlinux.org/image
.. _Fedora 23 cloud image: https://download.fedoraproject.org/pub/fedora/linux/releases/23/Cloud/x86_64/Images/Fedora-Cloud-Base-23-20151030.x86_64.qcow2
.. _Openstack developer: http://docs.openstack.org/developer/keystone/setup.html
.. _go: https://golang.org/doc/articles/go_command.html
.. _ciao-cert: https://github.com/01org/ciao/blob/master/ssntp/ciao-cert/README.md
.. _CNCI Agent: https://github.com/01org/ciao/tree/master/networking/cnci_agent
