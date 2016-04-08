.. _openstack_conf_vars_list:

Variables for OpenStack Deployment
##################################

This installer provides a variety of configurations you can set through
variables; below you will find a reference of the components supported
with Clear Linux* OS for Intel® Architecture.

.. csv-table:: "Required Parameters Per Component"
   :header: "Variable", "Components Impacted", "Description"
   :widths: 90, 90, 150

   "rabbitmq_password", "RabbitMQ, Neutron, Nova, Heat", "Password of
   RabbitMQ user "
   "database_root_password", "ALL", "Password for root database user"
   "keystone_database_password", "Keystone", "Password for 'keystone'
   database"
   "keystone_admin_password", "ALL", "Password for 'admin' user"
   "glance_user_password", "Glance", "Password for 'glance' user"
   "glance_database_password", "Glance", "Password for 'glance' database"
   "nova_user_password", "Nova, Neutron", "Password for 'nova' user"
   "nova_database_password", "Nova", "Password for 'nova' database"
   "neutron_database_password", "Neutron", "Password for 'neutron'
   database"
   "neutron_user_password", "Neutron, Nova", "Password for 'neutron'
   user"
   "metadata_proxy_shared_secret", "Neutron, Nova", "Proxy"
   "heat_domain_admin_password", "Heat", "Password for heat domain admin
   user"
   "heat_user_password", "Heat", "Password for heat user"
   "heat_database_password", "Heat", "Password for heat database"
   "heat_domain", "Heat", "The heat domain that contains projects and
   users for stacks"


.. csv-table:: "Optional Parameters Per Component"
   :header: "*(Component)* `Variable` : **Value**", "Description"
   :widths: 90, 150

   "*(ALL)* `swupd_args` : **unset**", "Optional arguments for swupd"
   "*(ALL)* `log_debug` : **False**", "Set to True to enable debug log level on all services"
   "*(Heat, Neutron, Nova, RabbitMQ)* `rabbitmq_username` : **openstack**", "User ID for RabbitMQ"
   "*(Neutron, Nova)* `neutron_public_interface_name`: **unset**", "Public interface of Neutron machines, if is not set, it will take the default interface reported by `ip route`"
   "*(Nova)* `nova_public_interface_name` : **unset**", "Public interface of Neutron machines, if is not set, it will take the default interface reported by `ip route`"
   "*(Nova)* `nova_virt_type`: **qemu**", "Virtualization type (qemu | kvm), if this is not set, then the playbook will try to guess it"
   "*(Neutron)* `os_tuning_params`: **net.ipv4.ip_forward: 1, net.ipv4.conf.default.rp_filter: 0, net.ipv4.conf.all.rp_filter: 0, net.bridge.bridge-nf-call-iptables: 1, net.bridge.bridge-nf-call-ip6tables: 1**", "syctl values needed by neutron when using openvswitch deployment scenario"

Note:
-----
If you would like to override a default, you can define it in the
:ref:`openstack_conf_vars_about`.

**Back to Configuration Section** :ref:`configure_openstack_environment`
