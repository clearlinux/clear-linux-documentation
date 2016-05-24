.. _openstack_conf_vars_list:

Variables for OpenStack* Deployment
###################################

This installer provides a variety of configurations you can set through
variables; below you will find a reference of the components supported
with Clear Linux* OS for Intel® Architecture.

Required Variables
==================

.. csv-table::
   :header: "*(Component)* `Variable`", "Description"
   :widths: 90, 150

   "*(Heat, Neutron, Nova, RabbitMQ)* **rabbitmq_password**", "Password of RabbitMQ user "
   "*(ALL)* **database_root_password**","Password for root database user"
   "*(Keystone)* **keystone_database_password**", "Password for 'keystone' database"
   "*(ALL)* **keystone_admin_password**", "Password for 'admin' user"
   "*(Glance)* **glance_user_password**", "Password for 'glance' user"
   "*(Glance)* **glance_database_password**", "Password for 'glance' database"
   "*(Neutron, Nova)* **nova_user_password**", "Password for 'nova' user"
   "*(Nova)* **nova_database_password**", "Password for 'nova' database"
   "*(Neutron)* **neutron_database_password**", "Password for 'neutron' database"
   "*(Neutron, Nova)* **neutron_user_password**", "Password for 'neutron' user"
   "*(Neutron, Nova)* **metadata_proxy_shared_secret**", "Secret for the metadata proxy"
   "*(Heat)* **heat_domain_admin_password**", "Password for heat domain admin user"
   "*(Heat)* **heat_user_password**", "Password for heat user"
   "*(Heat)* **heat_database_password**", "Password for heat database"
   "*(Heat)* **heat_domain**", "The heat domain that contains projects and users for stacks"
   "*(Swift)* **swift_user_password**", "Password for 'swift' user"
   "*(Swift)* **swift_database_password**", "Password for 'swift' database"
   "*(Swift)* **swift_replica_count**", "Replica number for each object. IMPORTANT: This number must be lower than the sum of all the storage devices among all storage nodes. It can be changed later."
   "*(Swift)* **swift_hash_path_suffix**", "Suffix for the object path name"
   "*(Swift)* **swift_hash_path_prefix**", "Prefix for the object path name"
   "*(Swift)* **swift_storage_device_path**", "The path of the storage devices"
   "*(Swift)* **swift_storage_devices**", "A list of the storage devices dedicated to swift deployment. For more information, see :ref:`openstack_swift_deployment_scenarios`"

Optional Variables
==================

.. csv-table::
   :header: "*(Component)* **Variable** : Default value", "Description"
   :widths: 90, 150

   "*(ALL)* **swupd_args**: unset", "Optional arguments for swupd"
   "*(ALL)* **log_debug**: False", "Set to True to enable debug log level on all services"
   "*(Heat, Neutron, Nova, RabbitMQ)* **rabbitmq_username**: openstack", "User ID for RabbitMQ"
   "*(Neutron, Nova)* **neutron_public_interface_name**: unset", "Public interface of Neutron machines, if is not set, it will take the default interface reported by **ip route**"
   "*(Nova)* **nova_public_interface_name**: unset", "Public interface of Neutron machines, if is not set, it will take the default interface reported by **ip route**"
   "*(Nova)* **nova_virt_type**: qemu", "Virtualization type (qemu | kvm), if this is not set, then the playbook will try to guess it"
   "*(Neutron)* **os_tuning_params**: net.ipv4.ip_forward: 1, net.ipv4.conf.default.rp_filter: 0, net.ipv4.conf.all.rp_filter: 0, net.bridge.bridge-nf-call-iptables: 1, net.bridge.bridge-nf-call-ip6tables: 1", "syctl values needed by neutron when using openvswitch deployment scenario"
   "*(Swift)* **swift_public_interface_name**, "Public interface of storage nodes, also known as the storage network interface name; If is not set, it will take the default interface reported by **ip route**"


Note:
-----
If you would like to override a default, you can define it in the
:ref:`openstack_conf_vars_about`.

**Back to Configuration Section** :ref:`configure_openstack_environment`
