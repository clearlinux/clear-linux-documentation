OpenStack* Dashboard
############################################################

The OpenStack Dashboard, also known as Horizon, is a web-based interface
for cloud administrators to manage various OpenStack resources and
services. This dashboard enables interaction with the OpenStack Compute
cloud controller via OpenStack APIs.

Installation and configuration
------------------------------

Please note that the dashboard relies on functional core services in
`OpenStack MVP <openstack_installing_bundles.html>`__,
including identity, image service, compute, and either networking
(``neutron``) or legacy networking (``nova-network``).

Environments with stand-alone services, such as Object Storage, cannot
use the dashboard.

To get started with OpenStack Dashboard services:

#. Install the OpenStack Dashboard bundle::
   
   	# clr_bundle_add openstack-dashboard

#. Enable and start the memcached service and the httpd server::
   
   	# systemctl enable httpd memcached  
   	# systemctl restart httpd memcached
