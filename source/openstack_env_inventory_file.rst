.. _openstack_env_inventory_file:

The "hosts" file
################

The :file:`hosts` file is an inventory file where you specify, via
``ini`` format, the roles your machine plays.

The hosts file can be structured with different groups, where each
group plays a specific role in your environment and network mapping.

Consider the following example::

    [openstack_identity]
    192.168.50.13

Here the :role:`[openstack_identity]` syntax defines the group, and
``192.168.50.13`` specifies the machines that possess that role. You
may define multiple machines in the same group; this is a standard
configuration for :role:`[openstack_compute]` nodes::

    [openstack_compute]
    192.168.50.16
    192.168.50.17


Inventory file groups
---------------------

Below you will find the description of each group in the `hosts` file.

.. csv-table:: "Inventory File Groups"
      :header: "Group", "Components", "Comments"
   :widths: 40, 40, 300 

   "[dbservers]", "MariaDB", ""
   "[messaging_servers]", "RabbitMQ", ""
   "[openstack_identity]", "Keystone, Horizon", ""
   "[openstack_image]", "Glance", ""
   "[openstack_compute_controller]", "Nova", ""
   "[openstack_compute]", "Nova", "Accepts multiple entries to have multiple compute nodes. You can add more entries and re-run the installer to add them to your environment."
   "[openstack_networking]", "Neutron", ""
   "[openstack_orchestration]", "Heat", ""


Important Notes
---------------

* To omit any role, do not add an entry under its group section.

* To create an ``All In One`` scenario, specify the same machine name or IPv4
  Address under all of the groups.

For further reference, check out the `Ansible`_ documentation.


**Back to Configuration Section** :ref:`configure_openstack_environment`

.. _Ansible: http://docs.ansible.com/ansible/intro_inventory.html
