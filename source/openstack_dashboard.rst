.. _openstack_dashboard:

Dashboard
####################

The OpenStack Dashboard, also known as Horizon, is a web-based interface
for cloud administrators and users to manage various OpenStack resources
and services.

The Dashboard enables web-based interactions with the
OpenStack Compute cloud controller through the OpenStack APIs.

Installation and configuration
------------------------------

The dashboard relies on functional core services including
Identity, Image service, Compute, and either Networking (neutron)
or legacy networking (nova-network). Environments with
stand-alone services such as Object Storage cannot use the
dashboard.

To get started with OpenStack Dashboard services:

#. Install the OpenStack Dashboard bundle::
   
        # clr_bundle_add openstack-dashboard

#. Enable and start the dashboard socket and the Nginx server::
   
        # systemctl enable nginx uwsgi@horizon.socket
        # systemctl restart nginx uwsgi@horizon.socket

Next topic: :ref:`openstack_networking`.