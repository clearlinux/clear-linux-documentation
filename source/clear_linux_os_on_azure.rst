.. _clear_linux_os_on_azure

Clear Linux* OS on Microsoft* Azure*
====================================

Clear Linux OS is now an offering in the Azure Marketplace.

Clear Linux OS is designed with cloud and data center environments in mind
and is tuned to maximize the performance and value of Intel® architecture.
In Azure our boot times are lightning-quick, with all on-boot services
launched in less than a second on nodes with warm caches [1]_.

There are three offerings of Clear Linux OS within the Azure Marketplace. They can
be created through the `Azure Portal <https://portal.azure.com>`_ or by
using the `Azure Command Line tools <https://github.com/Azure/azure-cli>`_.
Each offering can be further customized by using the swupd command to install
additional bundles. Learn more about Clear Linux OS and bundles
at https://clearlinux.org/documentation.

Offerings
~~~~~~~~~

The three offerings, and the commands to launch VM instances from the command line for each, are:

* **Basic** - This is a bare-bones generic offering, from which users may
  extend functionality by adding bundles of their choosing:

  * > (command line coming soon)

* **Containers** - This offering comes with the containers-basic bundle already installed.

  * > (command line coming soon) 

* **Machine Learning** - This offering comes with the containers-basic bundle already installed.

  * > (command line coming soon)


SSH Sessions
~~~~~~~~~~~~

To keep SSH sessions to Clear Linux Guests in Azure alive, you can give the
following option to SSH via the command line::

	-o ServerAliveInterval=180

Alternatively, you can add this setting to your SSH config file as shown below::

	Host *:
		ServerAliveInterval 180

.. [1] Software and workloads used in performance tests may have been optimized for performance only on Intel microprocessors. Performance tests are measured using specific computer systems, components, software, operations and functions. Any change to any of those factors may cause the results to vary. You should consult other information and performance tests to assist you in fully evaluating your contemplated purchases, including the performance of that product when combined with other products. For more complete information, visit http://www.intel.com/performance/datacenter. Configuration: Clear Linux OS release 11130 on SKU Standard_DS3_v2 in Microsoft* Azure*.