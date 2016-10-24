.. _openstack_bundle_and_service_summary:

OpenStack* bundle and service summary
#####################################

OpenStack provides an Infrastructure-as-a-Service (IaaS) solution
through a variety of complementary services. Each service offers an
application programming interface (API) that facilitates this
integration. The following table provides a list of OpenStack services:

.. csv-table:: OpenStack services
   :header: "Bundle Name (service)", "Project Name", "Description"
   :widths: 90, 90, 300

   "openstack-compute-controller", "Nova", "Manages the lifecycle of
   compute instances in an OpenStack environment. Responsibilities include
   spawning, scheduling and decommissioning of virtual machines on demand."
   "openstack-identity", "Keystone", "Provides an authentication and
   authorization service for other OpenStack services. Provides a catalog
   of endpoints for all OpenStack services."
   "openstack-image", "Glance", "Stores and retrieves virtual machine disk
   images. OpenStack Compute makes use of this during instance provisioning."
   "openstack-dashboard", "Horizon", "Provides a web-based self-service portal
   to interact with underlying OpenStack services."
   "openstack-network", "Neutron", "Enables Network-Connectivity-as-a-Service
   for some OpenStack services. Besides, it provides an API for users to define
   networks and the attachments into them."
   "openstack-object-storage", "Swift", "Stores and retrieves arbitrary
   unstructured data objects. It is highly fault tolerant with its data
   replication and scale-out architecture."
   "openstack-block-storage/openstack-block-storage-controller", "Cinder", "Provides
   persistent block storage to running instances."
   "openstack-telemetry", "Ceilometer", "Monitors and meters the
   OpenStack cloud for billing, benchmarking, scalability, and statistical
   purposes."
   "openstack-orchestration", "Heat", "Orchestrates multiple composite cloud
   applications by using either the native Heat Orchestration Template (HOT)
   template format or the AWS CloudFormation template format."

OpenStack is highly configurable to meet different needs. This guide
uses a two-node architecture.

-  The controller node runs the Identity Service, Image Service, the
   management portion of Compute, and the Dashboard. It also includes
   supporting services, such as an SQL database and message queue.
   Optionally, the controller node runs management portions of Block
   Storage services.
-  The compute node runs the hypervisor portion of Compute that operates
   project virtual machines or instances. By default, Compute uses KVM
   as the hypervisor. Compute also provisions project networks and
   provides firewalling (security groups) services. You can run more
   than one compute node.
-  (Optional) Block Storage node contains the disks that the Block
   Storage service provisions for instances. You can deploy more than
   one block storage node.
-  (Optional) Object Storage node contain the disks that the Object
   Storage service uses for storing accounts, containers, and objects.
   This service requires two nodes. Each node requires a minimum of one
   network interface. You can deploy more than two object storage nodes.
-  The self-service networks option augments the provider networks option
   with layer-3 (routing) services that enable self-service networks
   using overlay segmentation methods. Additionally, this option provides
   the foundation for advanced services such as LBaaS and FWaaS.

Next topic: :ref:`installing_openstack`.
