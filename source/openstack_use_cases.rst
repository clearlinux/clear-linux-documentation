OpenStack* use cases with Clear Linux* OS for Intel® Architecture
###################################################################

The installation and configuration of a Cloud Management Platform
depends on use cases and associated architectural choices.

OpenStack supports the following use cases:

-  *General purpose* -- A cloud built with common components that should
   address about 80 percent of common use cases.

-  *Compute-focused* -- A cloud designed to address compute-intensive
   workloads such as high performance computing (HPC).

-  *Storage-focused* -- A cloud focused on storage intensive workloads
   such as data analytics with parallel file systems.

-  *Network-focused* -- A cloud depending on high performance and
   reliable networking, such as a Content Delivery Network (CDN).

Clear Linux OS for Intel Architecture is designed with all of these use
cases in mind, but the initial target is to enable only those services
required for Cloud. As such, the Minimum Viable Product (MVP) is
defined as giving the capability for Clear Linux OS for Intel Architecture to boot an instance
(Virtual Machine) through OpenStack Services. In order to achieve this,
it's necessary to enable only those OpenStack services and dependent
components involved during that interaction. The following diagram
presents an example architecture of MVP:

.. image:: images\openstack_example_architecture.jpg
    :align: center
    :alt: sample OpenStack* architecture