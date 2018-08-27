.. _deploy-at-scale.rst:

Deploying |CL| at Scale
#######################

Once you are comfortable with `Clear Linux concepts`_, your next step
as a system administrator may be needing to understand how to deploy 
|CL| at scale in your environment.  

Throughout this document the term *endpoint* will be used to generally refer 
to a system targeted for |CL| installation, whether that is a datacenter 
system or unit deployed in field.  

.. note::

    This is not a replacement or blueprint for designing your IT operating 
    environment. These are simply recommendations that should be  implemented 
    with consideration. 
    
    Your |CL| deployment should complement the 
    existing environment and available tools. It is assumed foundational core IT 
    dependencies, such as network, in your environment are in a healthy and scaled
    to suit the deployment.



.. contents:: :local:
    :depth: 2





Pick a |CL| usage and update strategy
=====================================

Different business scenarios can call for different deployment methodologies. 
|CLOSIA| offers the flexibility to continue consuming the upstream |CL|
distribution or the option to fork away from the |CL| distribution and
act as your own :abbr:`OSV (Operating System Vendor)`. 


Below are overviews of both approaches and some considerations.
 



Option #1: Use the |CL| as the upstream origin (mixin)
------------------------------------------------------

This approach is *easier to adopt* by relying on the |CL| upstream for 
packaging updates for you to deploy. 


Custom software or packages that are not available in a preformed bundles can 
be added using the `mixin process`_ to form a custom bundle. 
If custom bundles are needed, you will solely be responsible for maintaining 
the custom bundle(s) and testing between |CL| releases in your environment, 
while the rest of the operating system and preformed bundles come from the 
|CL| upstream.
    


#. Ensure |CL| systems are able to be inventoried, managed, and orchestrated 
   to coordinate software updates.

#. The Clear upstream is updated extremely fast with autoupdate enabled by 
   default, however you may wish to act as an intermediary buffer between
   the OS releases. If you do decide to act as a gate to |CL| versions, 
   define a desired release cadence for yourself which is realistic with the 
   operational expectations of your environment.

#. Make use of a web caching proxy for |CL| updates for devices connected to 
   a local area network (LAN), such as a datacenter, to increase the speed 
   and resiliency of updates from the |CL| update servers. 
   
   Your caching proxy server is just like any other web application;
   |WEB-SERVER-SCALE|

 

Option #2: Create your own Linux distribution (mix)
---------------------------------------------------

This approach forks away from the |CL| upstream and has you act as your own 
:abbr:`OSV (Operating System Vendor)` by leveraging the `mixer process`_ to 
create customized images based on |CL|. This is a level of responsibility 
that requires having more infrastructure and processes  to adopt. In return, this approach 
*offers you a high degree of control and customization*.


* Development systems which are generating bundles and updates should be 
  sufficiently performant for the task and separate from the swupd update 
  webservers which are serving update content to production machines.

* swupd update webservers which are serving update content to 
  production machines (see `mixer process`_ for more information) should be
  appropriately scaled and  
  
  Your swupd update server is just like any other web application;
  |WEB-SERVER-SCALE|

     

Adopt an agile methodology
--------------------------
The cloud, and other scaled deployments, are all about flexibility and speed.
It only makes sense that any |CL| deployment strategy should follow suit. 

Manually rebuilding your own bundles or mix upon every release is not 
sustainable at a large scale. A |CL| deployment pipeline should be agile 
enough to validate and produce new versions with speed. Whether or not those 
updates actually make their way to your production can be separate 
business decision. However this *ability to frequently roll new versions* of 
software to your endpoints is a very important prerequisite. 

You own the validation and lifecycle of the OS and should treat it like any 
other software development lifecycle. Below are some pointers on this subject:

* Thoroughly understand the custom software packages, which are not 
  distributed with |CL|, that you will need to integrate with |CL| and 
  maintain along with their dependencies.


* Setup a path to production for building |CL| based images. At minimum this 
  should include:

    * A development clr-on-clr environment to test building packages and 
      bundles for |CL| systems. 

    * A pre-production environment to deploy |CL| versions to before 
      production 


* Employ a continuous integration and continuous deployment (CI/CD) philosophy
  in order to:

    - Automatically pull custom packages as they are updated from their 
      upstream projects or vendors. 

    - Generate |CL| bundles and potentially bootable images with your 
      customizations, if any. 

    - Measure against metrics and indicators which are relevant to your 
      business (e.g. performance, power, etc) from release to release.

    - Integrate with your organization's governance processes, such as change 
      control.







Versioning Infrastructure
-------------------------

|CL| version numbers have a deep meaning as they version of the whole 
infrastructure stack  - from the OS components to libraries to applications. 

Good record keeping can be powerful here.You should keep a detailed registry 
and history of previously deployed versions and their contents.

With a simple glance at the |CL| version numbers deployed, you should be able 
to determine with confidence if your Clear systems are patched against a 
particular security vulnerability or incorporate a critical new feature.
 
This practice opens the door to measured tracking and responses for software 
fixes. 




Pick an image distribution strategy
===================================

Once you have decided on a usage and update strategy, you should understand 
*how* the |CL| will be deployed to your endpoints. In a large scale 
deployment, interactive installers should be avoided in favor of automated 
installations or prebuilt images.

There are many well-known ways to install an operating system at scale. Each 
have their own benefits, and one may lend itself easier in your environment 
depending on the resources available to you.

See the `reference of Clear Linux image types`_
 

Below are some common ways to install |CL| to systems at scale:


Baremetal
----------

Preboot Execution Environments (PXE) or other 
out-of-band booting options are one way to a |CL| image or installer 
offers a way to distribute |CL| to physical baremetal systems on a LAN.

This option works well if your customizations are fairly small in size 
and infrastructure can be stateless. 

The |CL| `downloads page`_ offers a Live Image and can be deployed as 
a PXE boot server if one doesn't already exist in your environment. Also see
`documentation on installing Clear Linux on bare metal systems`_



Cloud Instances or Virtual Machines 
-----------------------------------
Image templates in the form of cloneable disks are an effective way to 
distribute |CL| for virtual machine environments, whether on-premise or 
hosted by a Cloud Solution Provider (CSP). 

When used in concert with cloud VM migration features, 
this can be a good option for allowing your applications a degree of high 
availability and workload mobility; VMs can be restarted on a cluster of 
hypervisor host or moved between datacenters transparently. 

The |CL| `downloads page`_ offers example prebuilt VM images and is 
readily available on popular CSPs. Also see 
`documentation on installing Clear Linux in VMs`_.



Containers
----------

Containerization platforms allow images to pulled from a 
repository and deployed repeatedly as isolated containers.  

Containers with a |CL| image can be a good option to blueprint and ship 
your application, including all its dependencies, as an artifact while 
allowing you or your customers to dynamically orchestrate and scale 
applications.

|CL| is capable of running a Docker host, has a container image which can 
be pulled from DockerHub, or building a customized container.
For more information visit the `containers page`_.

     


Considerations with stateless systems
=====================================
An important |CL| concept is statelessness and partitioning of system data 
from user data. This concept can change the way you think about an at scale 
deployment.


Backup strategy
---------------

A |CL| system and its infrastructure should be considered commodity and 
easily reproducible. Avoid focusing on backing up the operating system itself 
or default values. 

Instead, focus on backing up what's important and unique - the application 
and data.  In other words, only focus on backing up critical areas like 
`/home`,  `/etc`,  and `/var`.

 


Meaningful Logging & Telemetry
------------------------------

Offload logging and telemetry from endpoints to external servers so it is
persistent and can be accessed on another server when an issue occurs.


* Remote syslogging in |CL| is available through the 
  `systemd journal-remote service`_  


* |CL| offers a `native telemetry solution`_ which can be a powerful tool 
  in a large deployment to quickly crowdsource issues of interest. Take 
  advantage of this feature with care consideration of who the audience is 
  for telemetry events, what information is valuable to collect, and expose 
  events appropriately.  

  Your telemetry server is just like any other web application;
  |WEB-SERVER-SCALE|

 

 
Orchestration and Configuration Management
------------------------------------------------

In cloud environments, where systems can be ephemeral, being able to configure
and maintain generic instances is valuable.


|CL| offers an efficient cloud-init style solution, `micro-config-drive`_, 
through the *os-cloudguest* bundles which allows you to configure many 
common Day 1 operations such as setting hostname, creating users, or placing 
SSH keys in an automated way at boot.
 

A configuration management tool is useful for maintaining consistent system 
and application-level configuration. Ansible\* is offered through the 
*sysadmin-hostmgmt* bundle as a configuration management and automation tool. 

 

Cloud-native applications
-----------------------------------

An Infrastructure OS can design for good behavior, but it is ultimately up 
applications to make agile design choices and flows. Applications deployed 
upon |CL| should aim to be host-aware but not depend on any specific host to 
run. References should be relative and dynamic when possible.

The application architecture should incorporate an appropriate tolerance for 
infrastructure outages. Don't just keep stateless design as a noted feature. 
Continuously test its use; Automate its use by redeploying |CL| and 
application on new hosts. This naturally minimizes configuration drift, 
challenges your monitoring systems, and business continuity plans.





.. _`Clear Linux concepts`: https://clearlinux.org/documentation/clear-linux/concepts
.. _`mixin process`: https://clearlinux.org/documentation/clear-linux/guides/maintenance/mixin
.. _`mixer process`: https://clearlinux.org/documentation/clear-linux/guides/maintenance/mixer
.. _`reference of Clear Linux image types`: https://clearlinux.org/documentation/clear-linux/guides/maintenance/image-types
.. _`documentation on installing Clear Linux on bare metal systems`: https://clearlinux.org/documentation/clear-linux/get-started/bare-metal-install
.. _`downloads page`: https://download.clearlinux.org/image/
.. _`documentation on installing Clear Linux in VMs`: https://clearlinux.org/documentation/clear-linux/get-started/virtual-machine-install
.. _`containers page`: https://clearlinux.org/containers
.. _`systemd journal-remote service`: https://www.freedesktop.org/software/systemd/man/systemd-journal-remote.service.html
.. _`native telemetry solution`: https://clearlinux.org/features/telemetry
.. _`micro-config-drive`: https://github.com/clearlinux/micro-config-drive

.. |WEB-SERVER-SCALE| replace:: 
   There are many well-known ways to achieve a scalable and resilient web 
   servers for this purpose however, implementation details out of scope from this 
   document. In general, they should be located close to your endpoints, 
   high available according to your business needs, and easy to scale with a 
   loadbalancer when necessary.
