.. _clear-linux-dissector:

Clear Linux\* Dissector
#######################

The Clear Linux\* Dissector tool compares contents of Linux-based images. It
supports the comparison of |CL| and Yocto Project\* images.

.. contents:: :local:
   :depth: 1

Description
***********

Clear Linux Dissector provides tools for comparing |CL| images and Yocto Project
images.

* **View distribution data.**

  View the distribution data of a specific |CL| and Yocto Project distribution
  side-by-side. Helpful to determine if a |CL| version contains the packages and
  patches needed to move from a specific Yocto Project distribution to |CL|.

* **Compare images.**

  Compare |CL| and Yocto Project images to identify which packages you will need
  to move from a Yocto Project image to a |CL| image.

* **Compare releases.**

  Compare different |CL| releases to see changes between |CL| versions.

Prerequisites
*************

#. Must be on a Linux machine.

Set Up Clear Linux Dissector
****************************

Clear Linux Dissector is a web application, which means you will need to set up
an instance of the application in order to use it.

#. First, clone the clear-linux-dissector-web git repository.

   .. code-block:: bash

      git clone https://github.com/intel/clear-linux-dissector-web.git

#. Change directory into clear-linux-dissector-web.

   .. code-block:: bash

      cd clear-linux-dissector-web

#. Run the dockersetup.py script.

   If you are behind a proxy, you must set the command line variables
   :command:`--http-proxy`, :command:`--https-proxy`, and :command:`--socks-proxy`.

   This script will ask for a `username` and `password` to create a superuser;
   Take note of these credentials as you will use this to log in to the web interface.

   .. code-block:: bash

      ./dockersetup.py

#. After running the dockersetup.py script, the Clear Linux Dissector should be
   up and running on localhost. View the front-end interface at https://localhost:8081.

Before using the Clear Linux Dissector, you must first `Import Data`_.

Import Data
***********

Clear Linux Dissector compares image data from both |CL| and Yocto Project images.
In order to compare an image, it must first be imported into the Clear Linux
Dissector tool.

Import |CL| Data
================

|CL| data is imported from http://download.clearlinux.org/releases.

Import |CL| Data via CLI
------------------------

* To import the latest |CL| release, run the following command:

  .. code-block:: bash

      docker-compose run --rm layersapp /opt/layerindex/layerindex/tools/import_clear.py -d -p /opt/dissector -o /opt/sources -b <branchname>

  `<branchname>` is the name you assign to the |CL| release being imported. The
  `<branchname>` you provide will be used in the GUI during compare to refer
  to this imported release.

  .. note::

      Do not edit the paths in the command, because they are in relation to the
      `layersapp` Docker image that the application runs in.

* To import a specific |CL| release, use the :command:`-r` flag with the desired
  release number (for example 31380):

  .. code-block:: bash

      docker-compose run --rm layersapp /opt/layerindex/layerindex/tools/import_clear.py -d -p /opt/dissector -o /opt/sources -b <branchname> -r 31380

Import |CL| Data via GUI
------------------------

#. In a browser, navigate to the data import page at
   https://localhost:8081/layerindex/comparison/import/.

   .. figure:: ../../_figures/clear-linux-dissector/distro-data-import.png
      :scale: 45%
      :alt: Distro Data Import page

      Figure 1: Distro Data Import page

#. The first time you import |CL| data, you will need to create a new comparison
   branch. The branch name you provide will be used in the GUI during compare
   to refer to this imported release. You can choose to update your branch in
   later imports.

#. To import the latest |CL| release, check the :guilabel:`Get latest` box.

#. To import a specific release, enter the release number in the
   :guilabel:`Release` field.

#. Click :guilabel:`IMPORT` and you will be taken to a page that displays the task
   status. It will take a long time to upload the |CL| data.

#. Once the |CL| data is uploaded, you will see a page similar to the following:

   .. figure:: ../../_figures/clear-linux-dissector/distro-data-import-final.png
      :scale: 45%
      :alt: Finished distribution data import

      Figure 2: Finished distribution data import

Import Yocto Project Data
=========================

Yocto Project data is imported from https://layers.openembedded.org.

Import Yocto Project Data via CLI
---------------------------------

To import the latest Yocto Project data from the master branch:

* Run the following command:

  .. code-block:: bash

      docker-compose run --rm layersapp /opt/layerindex/layerindex/tools/import_layers.py https://layers.openembedded.org

To import Yocto Project data from a specific branch:

#. First create a branch object in the admin page.

   #. Navigate to https://localhost:8081/admin/layerindex/branch/add/ and enter the
      branch name in the :guilabel:`Branch name` field.

   #. Enter the corresponding Bitbake branch name (for example "zeus") in the
      :guilabel:`Bitbake branch` field.

      .. figure:: ../../_figures/clear-linux-dissector/create-yoctoproject-branch.png
         :scale: 45%
         :alt: Importing Yocto Project data from branch

         Figure 3: Importing Yocto Project data from branch


#. Run the following command to import a specific Yocto Project branch:

   .. code-block:: bash

       docker-compose run --rm layersapp /opt/layerindex/layerindex/tools/import_layers.py https://layers.opnembedded.org -b zeus

To update your Yocto Project branches:

* Run the following command:

  .. code-block:: bash

     docker-compose run --rm layersapp /opt/layerindex/layerindex/update.py

View Distribution Data
**********************
View the distribution data of a specific |CL| and Yocto Project distribution
side-by-side with the `Distro data` tool.

#. From the homepage, click on :guilabel:`Distro data`.

   .. figure:: ../../_figures/clear-linux-dissector/distro-data-select.png
      :scale: 45%
      :alt: Distro data button

      Figure 4: Distro data button

#. In the :guilabel:`Branch` section in the top left of the screen, select which
   imported |CL| distribution you want to search in, then search for the package
   you'd like to include, as shown in Figure 5:

   .. figure:: ../../_figures/clear-linux-dissector/distro-data-form.png
      :scale: 45%
      :alt: Select distribution to search

      Figure 5: Select distribution to search

#. Select the package you want to include.

#. The results show the |CL| and corresponding Yocto Project versions of your
   package side-by-side, as well as Patches and configure options.

   .. figure:: ../../_figures/clear-linux-dissector/distro-data.png
      :scale: 45%
      :alt: Side-by-side distribution data comparison

      Figure 6: Side-by-side distribution data comparison


   .. figure:: ../../_figures/clear-linux-dissector/distro-data-patches.png
      :scale: 45%
      :alt: Side-by-side distribution patch comparison

      Figure 7: Side-by-side distribution patch comparison

   .. figure:: ../../_figures/clear-linux-dissector/distro-data-configure-options.png
      :scale: 45%
      :alt: Side-by-side distribution data configuration options comparison

      Figure 8: Side-by-side distribution data configuration options comparison

Compare |CL| to Yocto Project image
***********************************

If you want to migrate from an existing Yocto Project image to |CL|, you can use
`Image comparison` tool to find the necessary packages. Before starting, make
sure that you are on the same machine that built the original Yocto Project image.

#. From the homepage, click on :guilabel:`Image comparsion`.

   .. figure:: ../../_figures/clear-linux-dissector/image-comparison-select.png
      :scale: 45%
      :alt: Image comparison button

      Figure 9: Image comparison button

#. Follow instructions to run the `oe-image-manifest-script`. Upload the
   resulting .tar.gz file and choose which branch you want to compare it to.

   .. figure:: ../../_figures/clear-linux-dissector/image-comparison-form.png
      :scale: 45%
      :alt: Create a new comparison

      Figure 10: Create a new comparison

#. The resulting list will show which packages are in the original Yocto Project
   image and the corresponding |CL| packages.

   .. figure:: ../../_figures/clear-linux-dissector/image-comparison-result.png
      :scale: 45%
      :alt: Image comparison result

      Figure 11: Image comparison result

Compare |CL| Releases
*********************

To view the differences between two |CL| releases, use the `Release comparison`
tool. Before comparing |CL| releases, you must first import the |CL| releases
that you want to compare by following How to Import Clear Linux Data (TODO link).

Once you have the |CL| releases imported:

#. From the home page, click on :guilabel:`Release comparison`.

   .. figure:: ../../_figures/clear-linux-dissector/release-comparison-select.png
      :scale: 45%
      :alt: Release comparison button

      Figure 12: Release comparison button

#. Select the two releases you'd like to compare and click :guilabel:`CREATE COMPARISON`.

   .. figure:: ../../_figures/clear-linux-dissector/release-comparison-form.png
      :scale: 45%
      :alt: Select releases to compare

      Figure 13: Select releases to compare

#. The resulting list will show changes between the two releases such as packages
   added, upgraded, and downgraded.

   .. figure:: ../../_figures/clear-linux-dissector/release-comparison-result.png
      :scale: 45%
      :alt: Release comparison result

      Figure 14: Release comparison result
