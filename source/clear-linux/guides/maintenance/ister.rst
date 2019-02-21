.. _ister:

ister.py
########

The `ister.py tool`_ is a template based installer used by |CL-ATTR| to produce
images for each release. The same ister tool is available for use in |CL| to
create custom images based on an upstream image.

.. contents::
   :local:
   :depth: 1

Description
***********

|CL| is a rolling release and produces on average 10 releases per week using the
ister tool. With each release we produce multiple
`image types for different environments`_  and use cases such as installers,
Hyper-V, KVM, or VMWare.

Each image has a JSON configuration file used by ister to generate the image.
These JSON configuration files describe the image type, partitions, version,
and which bundles will be preinstalled by default with the image. For each image
type we produce, the corresponding JSON configuration file for the image is also
published.

The :ref:`mixer<mixer>` tool also uses ister to build images for your custom
mix. Like upstream images, a JSON configuration file is defined for the image,
which ister uses to generate the image. Refer to the :ref:`mixer<mixer>` guide
for instruction on using ister to build an image for a custom mix.

Examples
********

Recreate an upstream image
==========================

The published configuration files for upstream images may be used to recreate an
image, for example when you want to:

* Use an older version of |CL| and the image is no longer available (only after
  March 2017).
* Customize the partitions of an image.
* Customize the bundles preinstalled in an image.
* Run your own post installation script.


Follow these steps to recreate an upstream image based on the image's JSON
configuration file:

#. Install the :command:`os-installer` bundle. Refer to `Install a bundle`_ for
   more details.

#. Download the `ister.py tool`_ and grant it sudo privileges.

#. Download the JSON configuration file for the desired image:

   * `Configuration files for the current release`_
   * `Previous releases`_ (only after March 2017)

   For a previous release, navigate to `Previous releases`_, select the version
   you want, and find the JSON configuration file under
   :file:`/clear/config/image`. For example:
   ``https://cdn.download.clearlinux.org/releases/15700/clear/config/image/``

#. Download “PostNonChroot” script (if applicable).

   The JSON configuration file for the image may have an accompanying
   “PostNonChroot” script that is executed at the end of the image creation
   process. If it does, download the script and make it executable.

#. Edit the JSON configuration file as needed.

#. If your configuration file has an accompanying "PostNonChroot" script, change
   the default path of the script to match your path.

#. Generate the new image with the following command:

   .. code-block:: bash

   	sudo ister.py -t [JSON configuration]

Related topics
**************

* :ref:`mixer`
* :ref:`bulk-provision`

.. _ister.py tool: https://github.com/bryteise/ister
.. _image types for different environments: https://cdn.download.clearlinux.org/image/README-IMAGES.html
.. _Configuration files for the current release: https://cdn.download.clearlinux.org/current/config/image/
.. _Previous releases: https://cdn.download.clearlinux.org/releases/
.. _Install a bundle: https://clearlinux.org/documentation/clear-linux/guides/maintenance/swupd-guide#adding-a-bundle