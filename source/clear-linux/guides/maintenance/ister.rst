.. _ister:

ister
#####

The `ister.py tool`_ is a template based installer used by |CL-ATTR| to produce
images for each release. The same ister tool is available for use to create
custom images based on upstream |CL|.

Description
***********

|CL| is a rolling release and produces on average 10 releases per week using the
ister tool. With each release, we produce multiple `different image types`_ for
different environments and use cases such as installers, Hyper-V, KVM, or
VMWare.

For each image, we also publish the corresponding JSON configuration file used
by ister to generate the image. These JSON configuration files describe image
type, partitions, version, and which bundles will be preinstalled by default
with the image.

The :ref:`mixer<mixer>` tool uses ister to build an image for your custom mix.
Like upstream images, a JSON configuration file is defined for the image, which
ister uses to generate the image.

Configuration files for upstream images may be used to recreate an image, for
example when you want to:

* Use an older version of |CL| and the image is no longer available (only after
  March 2017).
* Customize the partitions of an image.
* Customize the bundles preinstalled in an image.
* Run your own post installation script.

How to use ister
****************

Learn how to use ister to recreate an upstream image. Refer to the
:ref:`mixer <mixer>` guide for instruction on using ister to build an image for
a custom mix.

Example: Recreate an upstream image
===================================

Prerequisites
-------------

#. |CL| installed.

#. :command:`os-installer` bundle is installed.

#. ister.py has sudo privilege.

Recreate upstream image
-----------------------

Follow these steps to recreate an upstream image based on the image's JSON
configuration file:

#. Download the JSON configuration file for the desired image:

   * `Configuration files for the current release`_
   * `Previous releases`_ (only after March 2017)

   For a previous release, the configuration file for the specific release is
   located at
   ``https://cdn.download.clearlinux.org/releases/<version number>/clear/config/image/``

#. The JSON configuration file for the image may have an accompanying
   “PostNonChroot” script that is executed at the end of the image creation
   process. If it does, download the script as well and make it executable.

#. Edit the JSON configuration file as needed.

#. If your configuration file has an accompanying "PostNonChroot" script, change
   the default path of the script to match yours.

#. Generate the new image with the following command:

   .. code-block:: bash

   	sudo ister.py -t [JSON configuration]

Related topics
**************

* :ref:`mixer`
* :ref:`bulk-provision`

.. _ister.py tool: https://github.com/bryteise/ister
.. _different image types: https://cdn.download.clearlinux.org/image/README-IMAGES.html
.. _Configuration files for the current release: https://cdn.download.clearlinux.org/current/config/image/
.. _Previous releases: https://cdn.download.clearlinux.org/releases/