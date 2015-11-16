<<<<<<< HEAD
Dashboard
############################################################

The OpenStack Dashboard, also known as Horizon, is a web-based interface
for cloud administrators to manage various OpenStack resources and
services. This dashboard enables interaction with the OpenStack Compute
cloud controller via OpenStack APIs.

Installation and configuration
------------------------------
=======
.. _openstack_dashboard:

Dashboard
####################

The OpenStack Dashboard, also known as Horizon, is a web-based interface
for cloud administrators and users to manage various OpenStack resources
and services.

The Dashboard enables web-based interactions with the
OpenStack Compute cloud controller through the OpenStack APIs.
>>>>>>> staging

Installation and configuration
------------------------------

The dashboard relies on functional core services including
Identity, Image service, Compute, and either Networking (neutron)
or legacy networking (nova-network). Environments with
stand-alone services such as Object Storage cannot use the
dashboard.

To get started with OpenStack Dashboard services:

#. Install the OpenStack Dashboard bundle::
   
<<<<<<< HEAD
   	# clr_bundle_add openstack-dashboard

#. Enable and start the memcached service and the httpd server::
   
   	# systemctl enable httpd memcached  
   	# systemctl restart httpd memcached
=======
        # swupd bundle-add openstack-dashboard
        # swupd verify --fix

#. Enable and start the dashboard socket and the Nginx server::
   
        # systemctl enable nginx uwsgi@horizon.socket
        # systemctl restart nginx uwsgi@horizon.socket

Next topic: :ref:`openstack_networking`.
>>>>>>> staging
