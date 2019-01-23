.. _ister:

Create custom upstream |CL| images with ister.py
################################################


.. Bun: ister is Clear Linux specific? (It looks tuned to CL), but not in the CL project repo? This is good content - but if its part of CL it should be a full guide (will require some more info). If its an external tool, lets do it as a tutorial.
.. Bun: this url https://cdn.download.clearlinux.org/releases/<version number>/clear/config/image/ doesnt work for all releases -for eg 08 Mar 2017
.. Bun: please provide a brief description of what can be edited in the config

|CL-ATTR| is a rolling release and produces on average 10 releases per week
using the `ister.py tool`_. This tutorial shows how to use the same ister tool
with a published image configuration file to recreate an upstream image.

Overview
********

With each release, we produce multiple `different image types`_  for different environments and use cases such as installers, Hyper-V, KVM, or VMWare. For each image, we publish a corresponding JSON configuration file used to generate the image. These JSON configuration files describe XXXXXX.

These configurations files are useful to recreate an image, for example when you want to:

* Use an older version of |CL| and the image is no longer available.
* Customize the partitions of an image.
* Customize the bundles preinstalled in an image.
* Run your own post installation script.

Prerequisites
*************

#. **|CL| installed**

#. **Required bundles**

   ister requires that the :command:`os-installer` bundle is installed.

#. **ister.py has sudo privilege**

Recreate an upstream image
**************************

Follow these steps to recreate an upstream image based on the image's JSON
configuration file:

#. Download the JSON configuration file for the desired image. Find the JSON
   configuration file for the desired image:

   * `Configuration files for the current release`_
   * `Previous releases`_.

   For a previous release, the configuration file for the specific release is
   located at
   ``https://cdn.download.clearlinux.org/releases/<version number>/clear/config/image/``

#. The JSON configuration file for the image may have an accompanying
   “PostNonChroot” script that is executed at the end of the image creation
   process. If it does, download the script as well and make it executable.

#. Edit the JSON configuration file as needed.

   .. todo DETAILS!!! such as...

#. If your configuration file has an accompanying "PostNonChroot" script, change
   the default path of the script to match yours.

#. Generate the new image with the following command:

   .. code-block:: bash

   	  sudo ister.py -t [JSON configuration]



.. _ister.py tool: https://github.com/bryteise/ister
.. _different image types: https://cdn.download.clearlinux.org/image/README-IMAGES.html
.. _Configuration files for the current release: https://cdn.download.clearlinux.org/current/config/image/
.. _Previous releases: https://cdn.download.clearlinux.org/releases/