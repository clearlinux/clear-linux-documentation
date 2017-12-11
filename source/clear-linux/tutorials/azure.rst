.. _azure:

Clear Linux\* OS on Microsoft\* Azure\*
#######################################

Clear Linux OS is now an offering in the Azure Marketplace.

:ref:`fig-wp-install-1`

Clear Linux OS is designed with cloud and data center environments in mind
and is tuned to maximize the performance and value of Intel® architecture.
In Azure our boot times are lightning-quick, with all on-boot services
launched in less than a second on nodes with warm caches [1]_.

There are three offerings of Clear Linux OS within the Azure Marketplace.
They can be created through the `Azure Portal <https://portal.azure.com>`_ or
by using the `Azure Command Line tools <https://github.com/Azure/azure-cli>`_.
Each offering can be further customized by using the swupd command to
install additional bundles. Learn more about Clear Linux OS and bundles in
our :ref:`documentation<clear-linux>`.

For additional information visit the Clear Linux
`Azure Partner Mini Case Study`_ and the `Azure Partner Datasheet`_

Offerings
=========

The three offerings, and the commands to launch VM instances from the command line for each, are:

* **Basic** - This is a bare-bones generic offering, from which users may
  extend functionality by adding bundles of their choosing:

* **Containers** - This offering comes with the containers-basic bundle already
  installed.

* **Machine Learning** - This offering comes pre-loaded with popular open
  source tools for developing machine learning applications.

Azure Command Line Interface
============================

The Azure Command Line Interface offers the ability to create and manage
resources in Azure from the command line. The examples here are based on
Version 1.0 of the Azure CLI, which is implemented in Javascript and
distributed through the Node Package Manager. Version 2.0 of the Azure CLI is
implemented in Python. This example will be updated when Azure CLI 2.0 is fully
released.

The following command shows the version number of the most recent images that
have been uploaded into the Azure Marketplace.

::

  azure vm image list -p clear-linux-project -l westus -o clear-linux-os | grep -v "Getting" | cut -f5 -d: | sed -e 's/\s*//g'| sed -e 's/\..*//' | sort -u | tail -1

The following scriplet can be used to create and start a virtual machine
instance in Azure based on a marketplace offering. The resource group needs to
already exist. This script tries to use a resource group of the form
"<azure_username>-clr-vms". For example, for an Azure user named Rob trying to
create an instance of version ``12920`` of the ``basic`` offering for Clear
Linux OS, this script creates an instance with the public hostname of
``rob-12920-basic-1234``.

::

  #!/bin/bash
  clrversion=XXXXX
  azuser='azure_username'
  location="westus"
  resourceGroup="${azuser}-clr-vms"
  offering=basic
  # offering=containers
  # offering=machine-learning
  uniquesuffix=$((1 + RANDOM % 1000)) # More like "probably unique suffix"...

  azure vm create --vm-size Standard_D1_v2 \
          --admin-username ${azuser} \
          --ssh-publickey-file ~/.ssh/id_rsa.pub \
          --name=${azuser}-${clrversion}-${offering}-${uniquesuffix} \
          --location=${location} \
          --resource-group ${resourceGroup} \
          --os-type Linux \
          --image-urn clear-linux-project:clear-linux-os:${offering}:${clrversion}.0.0 \
          --nic-name clr-nic1 \
          --vnet-name ${clrversion}-${offering}-vnet \
          --vnet-address-prefix 10.0.0.0/8 \
          --vnet-subnet-name ${clrversion}-vnet-subnet \
          --vnet-subnet-address-prefix 10.0.0.0/8 \
          --plan-name ${offering} \
          --plan-publisher clear-linux-project \
          --plan-product clear-linux-os \
          --public-ip-domain-name ${azuser}-${clrversion}-${offering}-${uniquesuffix} \
          --public-ip-allocation-method "Dynamic" \
          --public-ip-name "${clrversion}-${offering}-${uniquesuffix}"



SSH Sessions
============

To keep SSH sessions to Clear Linux Guests in Azure from being dropped
after periods of inactivity, you can give the following option to SSH via
the command line::

   -o ServerAliveInterval=180

Alternatively, you can add this setting to your SSH config file as shown
below::

   Host *:
      ServerAliveInterval 180

.. [1]
   Software and workloads used in performance tests may have been optimized
   for performance only on Intel microprocessors. Performance tests are
   measured using specific computer systems, components, software, operations
   and functions. Any change to any of those factors may cause the results to
   vary. You should consult other information and performance tests to assist
   you in fully evaluating your contemplated purchases, including the
   performance of that product when combined with other products. For more
   complete information, visit http://www.intel.com/performance/datacenter.
   Configuration: Clear Linux OS release 11130 on SKU Standard_DS3_v2 in
   Microsoft\* Azure\*.


.. _Azure Partner Datasheet:
   http://download.microsoft.com/download/D/9/E/D9E22342-96D9-4455-BB15-99A1AF514DDD/Microsoft%20Azure%20Partner%20Datasheet%20-%20Intel%20Clear%20Linux.pdf

.. _Azure Partner Mini Case Study:
   http://download.microsoft.com/download/D/9/E/D9E22342-96D9-4455-BB15-99A1AF514DDD/Microsoft%20Azure%20Partner%20Mini%20Case%20Study%20-%20Intel%20Clear%20Linux.pdf
