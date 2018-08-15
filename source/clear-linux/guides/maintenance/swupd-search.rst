.. _swupd-search: 

Use swupd search to find bundles
#################################

.. contents:: :local: 
   depth: 2

This help document shows you how to use `swupd search` to search for and add 
a bundle. 

Assumptions
***********

This guide assumes you: 

* Possess a basic knowledge of :ref:`swupd <swupd-guide>` 
* Understand :ref:`how swupd differs <swupd-about>` from  
  other Linux\* distributions 
* Plan to use :ref:`mixer` to build your own |CL| OS

How do I search for a bundle? 
*****************************

Example: Kata Containers
========================

Containers have revolutionized the way we manage cloud infrastructure. Whereas traditional containers share the same OS kernel, raising security concerns, with Kata Containers, each container has its own kernel instance and runs on its own :abbr:`Virtual Machine (VM)`. Whether you're running 3 or 300 nodes on your cluster, Kata Containers provide a lightweight, fast, and secure option for app/container management.  

In |CL|, you only need to add one bundle to use `Kata Containers`_: 
`containers virt`_. We also recommend our tutorial: :ref:`kata`

So far, we need a *kata* containers bundle. So how do we search for it?  First, use :command:`swupd search` with **only one term** like *kata*. 

#. Enter this command, followed by 'kata' as the search term: 

   .. code-block:: bash

      sudo swupd search -b kata

   .. note::
      
      `swupd search` downloads |CL| manifest data and searches for matching paths. Enter only one term, or hyphenated term, per search. Use the command :command:`man swupd` to learn more. 

      `-b` flag, or `--binary`, means: Restrict search to program binary paths.

#. The `swupd search` results show a match for our use case.

   .. code-block:: console

      Bundle containers-virt    (834 MB to install)
          /usr/bin/kata-virtfs-lite-proxy-helper
          /usr/bin/kata-runtime
          /usr/bin/kata-qemu-lite-system-x86_64
          /usr/bin/kata-qemu-lite-pr-helper
          /usr/bin/kata-qemu-lite-ga
          /usr/bin/kata-collect-data.sh

   .. note::

      If the bundle is already installed, *[installed]* appears in search results. If this doesn't apppear, the bundle needs to be installed. 

#. Add the bundle `containers-virt`:

   .. code-block:: bash

      sudo swupd bundle-add containers-virt

      .. note:: 

         To add other bundles, replace `containers-virt` with your selected bundle.

#. When prompted, enter your password. 

#. Upon successful installation, your console should show similar data:
  
   .. code-block:: console 

      Downloading packs...

      Extracting containers-virt pack for version 24430
          ...50%
      Extracting kernel-container pack for version 24430
          ...100%
      Starting download of remaining update content. This may take a while...
          ...100%
      Finishing download of update content...
      Installing bundle(s) files...
          ...100%
      Calling post-update helper scripts.
      Successfully installed 1 bundle

.. note:: 
   
   For developers who do not wish to adopt the |CL| Common Tooling Framework (e.g., Autospec, etc.), select the complementary :file:`-dev` bundle in order to successfully build each bundle. 

FAQ
===

Find answers to these common questions: 

* How do I install and *use* :ref:`Kata Containers <kata>` on |CL|? 

* How do I :ref:`kata_migration`?

* How do I show all :ref:`bundles available <swupd-guide>`?

* How do I :ref:`update swupd<swupd-guide>`? 

* How do I :ref:`remove bundles<swupd-guide>`? 

.. _Kata Containers: https://clearlinux.org/blogs/clear-linux-os-announces-support-kata-containers

.. _containers virt: https://github.com/clearlinux/clr-bundles/blob/master/bundles/containers-virt