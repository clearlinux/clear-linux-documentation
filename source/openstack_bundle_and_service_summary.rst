OpenStack* Bundle and service summary
############################################################

OpenStack provides an Infrastructure-as-a-Service (IaaS) solution
through a variety of complementary services. Each service offers an
application programming interface (API) that facilitates this
integration. The following table provides a list of OpenStack MVP
services:

.. csv-table:: OpenStack MVP services
   :header: "Bundle Name (service)", "Project Name", "Description"
   :widths: 90, 90, 300

   "openstack-compute", "Nova", "Manages the lifecycle of compute instances in an OpenStack environment. Responsibilities include spawning, scheduling and decommissioning of virtual machines on demand."
   "openstack-identity", "Keystone", "Provides an authentication and authorization service for other OpenStack services. Provides a catalog of endpoints for all OpenStack services."
   "openstack-image", "Glance", "Stores and retrieves virtual machine disk images. OpenStack Compute makes use of this during instance provisioning."


OpenStack is highly configurable to meet different needs. This guide
uses two-node architecture with legacy networking (Nova-network).

-  The controller node runs the Identity Service, Image Service,
   management portion of Compute, and the Dashboard. It also includes
   supporting services such as a SQL database and message queue.
   Optionally, the controller node runs management portions of Block
   Storage services.
-  The compute node runs the hypervisor portion of Compute that operates
   project virtual machines or instances. By default, Compute uses KVM
   as the hypervisor. Compute also provisions project networks and
   provides firewalling (security groups) services. You can run more
   than one compute node.
