.. _swupd-search: 

Use swupd search to find a bundle
#################################

.. contents:: :local: 
   depth: 2

This help document shows you how to use `swupd search` as a Developer. 

Assumptions: 

* Basic knowledge of using :ref:`swupd <swupd-guide>` 
* Understanding how :ref:`swupd <swupd-about>` differs from  
  other Linux\* distributions 
* You plan to use :ref:`mixer` to build your own |CLOSIA|for a specific 
  use case 

This example illustrates how to search for and add a bundle. 

Scenario 1: Data Science with Python
====================================

We're developing a custom Clear Linux OS for data science with Python. We'll 
develop our own mix, from which we'll create a release image. That image 
will be distributed to data center (DC) clients across the United States  
who need this data to determine DC workload balancing. Why? We need to
create a tool to analyze energy consumption based on population 
statistics and consumption data. Our tool's custom dashboard will include 
heat-maps showing where and when energy consumption peaks in large 
metropolitan areas. 

So far, we know we need Python data science capabilities. 

First, use :command:`swupd search` with a general term like *Python*. 

#. Enter this command and add 'Python' as the search term: 

   .. code-block:: bash

      sudo swupd search -b Python

   .. note::
      
      `swupd search` searches for matching paths in the manifest data. 
      Enter only one term, or one hyphenated term, at a time. 
      Use the command :command:`man swupd` to learn more. 

      `-b` flag, or `--binary`, means: Restrict search to program binary paths. 

#. Results of `swupd search` shows the best match for our use case.

   .. code-block:: console

      Bundle python-data-science	(923 MB to install)
      		/usr/bin/ipython3
      		/usr/bin/ipython

   .. note::

      Result above is one of several shown in standard output.  

      If the bundle is already installed, *[installed]* appears in search results. If that doesn't apppear, the bundle needs to be installed. 

#. Add the bundle `python-data-science`.

   .. code-block:: bash

      sudo swupd bundle-add python-data-science

#. When prompted, enter your password. 

   .. note:: 

      You should see console data similar to the following: 

   .. code-block:: console 

      Password: 
      Downloading packs...

      Extracting python-data-science pack for version 23710
      ...50%
      Extracting python-extras pack for version 23830
      ...100%
      Starting download of remaining update content. This may take a while...
      ...100%
      Finishing download of update content...
      Installing bundle(s) files...
      ...100%
      Calling post-update helper scripts.
      Successfully installed 1 bundle
FAQ
===

Find answers to these common questions: 

* How do I show all :ref:`bundles available<swupd-guide>`?

* How do I :ref:`add new bundles<swupd-guide>`? 

.. note:: 
   
   For developers who do not wish to adopt the |CL| Common Tooling Framework (e.g., Autospec, etc.), select the complementary :file:`-dev` bundle in order to successfully build each bundle. 