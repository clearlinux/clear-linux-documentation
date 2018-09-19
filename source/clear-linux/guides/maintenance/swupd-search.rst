.. _swupd-search: 

Use swupd search to find bundles
################################

This document explains how to use `swupd search` to find and add
bundles in |CL-ATTR|. 

Assumptions
***********

This guide assumes you: 

* Possess a basic knowledge of :ref:`swupd <swupd-guide>` 
* Understand :ref:`how swupd differs <swupd-about>` from  
  other Linux\* distributions 
* May :ref:`mixer` to produce a custom distribution/image

How do I search for a bundle? 
*****************************

Use `swupd search` to locate the bundle where the application binary exists. 

Example: Kata Containers
========================

Containers have revolutionized the way we manage cloud infrastructure. 
Traditional containers often share the same OS kernel, which raises 
security concerns. Instead, with Kata Containers, each container has its own 
kernel instance and runs on its own :abbr:`Virtual Machine (VM)`. Whether you're running 3 or 300 nodes on your cluster, Kata Containers provide a 
lightweight, fast, and secure option for app/container management.  

In |CL|, you only need to add `one bundle`_ to use `Kata Containers`_: 
`containers-virt`. Also, check out our tutorial: :ref:`kata`.

We need to find *kata* containers in a bundle. How do we search for it? 

#. Enter :command:`swupd search`, followed by 'kata' as the search term: 

   .. code-block:: bash

      sudo swupd search kata

   .. note:: 

      `swupd search` downloads |CL| manifest data and searches for
      matching paths. Enter only one term, or hyphenated term, per 
      search. Use the command :command:`man swupd` to learn more.

#. Alternatively, if you want to search binaries only, add the `-b`
   flag: 

   .. code-block:: bash

      sudo swupd search -b kata

   .. note::

      `-b` flag, or `--binary`, means: Restrict search to program binary paths. Omit this flag if you want a larger scope of search results.  

      Only the base bundle is returned. In |CL|, *bundles* can contain 
      other *bundles* via `includes`. For more details, see `Bundle Definition Files`_ and its subdirectory *bundles*. 

      If your search does not produce results on a specific term when using
      the `-b` flag, abbreviate the search term. For example, if you search 
      for *kubernetes* and it does not show results, instead abbreviate the 
      term to *kube* to show results. 

#. Optionally, you can review our `bundles`_ or individual `packages`_

#. Using `sudo swupd search -b kata` shows a match for our use case.

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

      To add multiple bundles simply add a space followed by the bundle name.

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

Related Topics
==============

Learn how to:

* :ref:`kata` on |CL| 

* :ref:`kata_migration`

* :ref:`swupd-guide` 

* :ref:`Show all available bundles <swupd-guide>`

* :ref:`Remove bundles<swupd-guide>` 

.. _Kata Containers: https://clearlinux.org/blogs/clear-linux-os-announces-support-kata-containers

.. _one bundle: https://github.com/clearlinux/clr-bundles/blob/master/bundles/containers-virt

.. _Bundle Definition Files: https://github.com/clearlinux/clr-bundles

 .. _bundles: https://github.com/clearlinux/clr-bundles/tree/master/bundles 

 .. _packages: https://github.com/clearlinux/clr-bundles/blob/master/packages 
