.. _clear-linux-dissector:

Clear Linux\* Dissector
#######################

The Clear Linux\* Dissector tool compares and examines contents of |CL| and
Yocto Project\* images.

.. contents:: :local:
   :depth: 1

Description
***********

The Clear Linux Dissector provides a set of tools to:

* **View distribution data**

  Search and view package data of a |CL| distribution and it's Yocto Project
  equivalent. Compare packages, patches, and configuration between a |CL|
  release and the equivalent Yocto Project image.

* **Compare images**

  Compare |CL| and Yocto Project images to identify the packages needed to move
  from a Yocto Project image to a |CL| image. Compare Yocto Project images to
  identify differences between images.

* **Compare releases**

  Compare |CL| releases to see differences between |CL| versions.

Prerequisites
*************

* A version of Linux installed.

* `Docker/* <https://docs.docker.com/v17.09/engine/installation/>`_

* `Docker Compose <https://docs.docker.com/compose/install/>`_

* `Python 3 <https://www.python.org/download/releases/3.0/>`_


Set Up Clear Linux Dissector
****************************

Clear Linux Dissector is a web application. An instance of the application is
needed in order to use the tools.

#. Clone the clear-linux-dissector-web Git repository.

   .. code-block:: bash

      git clone https://github.com/intel/clear-linux-dissector-web.git

#. Change directory into clear-linux-dissector-web.

   .. code-block:: bash

      cd clear-linux-dissector-web

#. Run the :file:`dockersetup.py` script.

   If you are behind a proxy, you must also set the proxy command line options
   :command:`--http-proxy`, :command:`--https-proxy`, and :command:`--socks-proxy`.

   .. code-block:: bash

      ./dockersetup.py

   The script will ask for a `username` and `password` to create a superuser;
   Make note of these credentials as you will use them to log in to the web
   interface.

#. After running the :file:`dockersetup.py` script, the Clear Linux Dissector
   application should be up and running on localhost. Access the application via
   a browser at `https://localhost:8081`.

Before using the Clear Linux Dissector, you must first `Import Data`_.

Import Data
***********

Clear Linux Dissector can compare image data from both |CL| and Yocto Project
images. In order to compare an image, it must first be imported into the Clear
Linux Dissector tool.

Import |CL| Data
================

|CL| data is imported from http://download.clearlinux.org/releases.

Import |CL| Data via CLI
------------------------

* To import the latest |CL| release, use the following command:

  .. code-block:: bash

      docker-compose run --rm layersapp /opt/layerindex/layerindex/tools/import_clear.py -d -p /opt/dissector -o /opt/sources -b <branchname>

* To import a specific |CL| release, use the :command:`-r` flag with the desired
  release number. The following example imports release 31380:

  .. code-block:: bash

      docker-compose run --rm layersapp /opt/layerindex/layerindex/tools/import_clear.py -d -p /opt/dissector -o /opt/sources -b <branchname> -r 31380

`<branchname>` is the name of the new comparison branch for the |CL| release
being imported. The `<branchname>` you provide will be used in the GUI during
compare to refer to this imported release.

.. note::

   Do not edit the paths in the command, because they are in relation to the
   `layersapp` Docker image that the application runs in.

Import |CL| Data via GUI
------------------------

#. In a browser, navigate to the Distro Data Import page at
   https://localhost:8081/layerindex/comparison/import/.

   .. figure:: ../../_figures/clear-linux-dissector/distro-data-import.png
      :scale: 80%
      :alt: Distro Data Import page

#. Enter a new comparison branch name in the :guilabel:`Name` field. The branch
   name you provide will be used in the GUI during compare to refer to this
   imported release. You can choose to update your branch during later imports.

#. Choose the release to import:

   * To import the latest |CL| release, check the :guilabel:`Get latest` box.

   * To import a specific release, enter the release number in the
     :guilabel:`Release` field.

#. Click :guilabel:`IMPORT` and you will be taken to a page that displays the task
   status. It will take a long time to download the |CL| data.

#. Once the |CL| data is downloaded, you will see a page similar to the following:

   .. figure:: ../../_figures/clear-linux-dissector/distro-data-import-final.png
      :scale: 80%
      :alt: Finished distribution data import

Import Yocto Project Data
=========================

Yocto Project data is imported from https://layers.openembedded.org.

Import Yocto Project Data via CLI
---------------------------------

* To import the latest Yocto Project data from the master branch, use the
  following command:

  .. code-block:: bash

      docker-compose run --rm layersapp /opt/layerindex/layerindex/tools/import_layers.py https://layers.openembedded.org

* To import Yocto Project data from a specific branch:

  #. Create a branch object in the Dissector Admin page.

     #. Navigate to https://localhost:8081/admin/layerindex/branch/add/

        .. figure:: ../../_figures/clear-linux-dissector/create-yoctoproject-branch.png
           :scale: 80%
           :alt: Importing Yocto Project data from branch

     #. Enter the branch name in the :guilabel:`Branch name` field.

     #. Enter the corresponding Bitbake branch name (for example "zeus") in the
        :guilabel:`Bitbake branch` field.

     #. Click :guilabel:`SAVE`.

  #. Run the following command to import a specific Yocto Project branch. The
     following example imports the zeus branch:

     .. code-block:: bash

         docker-compose run --rm layersapp /opt/layerindex/layerindex/tools/import_layers.py https://layers.opnembedded.org -b zeus

* To update a Yocto Project branch, use the following command:

  .. code-block:: bash

     docker-compose run --rm layersapp /opt/layerindex/layerindex/update.py

View Distribution Data
**********************

Use the `Distro data` tool to view the package data of a specific |CL| or Yocto
Project distribution. Package data includes package version, description, license,
and a link to the package's homepage.

#. From the Clear Linux Dissector application homepage, click on
   :guilabel:`Distro data`.

   .. figure:: ../../_figures/clear-linux-dissector/distro-data-select.png
      :scale: 80%
      :alt: Distro data button

#. In the :guilabel:`Branch` section at the top left of the screen, select the
   imported |CL| distribution you want to search in

   .. figure:: ../../_figures/clear-linux-dissector/distro-data-form.png
      :scale: 80%
      :alt: Select distribution to search

#. Enter the package you would like to examine in the :guilabel:`Keyword` field
   and click :guilabel:`SEARCH`.

#. In the :guilabel:`Package` section, select the package you want to examine.

#. The results show the |CL| and corresponding Yocto Project versions of your
   selected package side-by-side, as well as Patches and configure options.

   .. figure:: ../../_figures/clear-linux-dissector/distro-data.png
      :scale: 80%
      :alt: Side-by-side distribution data comparison

   .. figure:: ../../_figures/clear-linux-dissector/distro-data-patches.png
      :scale: 80%
      :alt: Side-by-side distribution patch comparison

   .. figure:: ../../_figures/clear-linux-dissector/distro-data-configure-options.png
      :scale: 80%
      :alt: Side-by-side distribution data configuration options comparison

Compare |CL| to Yocto Project image
***********************************

Use the `Image comparison` tool to compare packages in an existing Yocto Project
image to |CL|. Useful if you want to migrate from an existing Yocto Project image
to |CL|.

.. note::

   This comparison requires using a provided script to collect Yocto Project data.
   The script must be run on the system used to build the Yocto Project image that
   you want to examine.

#. From the homepage, click on :guilabel:`Image comparison`.

   .. figure:: ../../_figures/clear-linux-dissector/image-comparison-select.png
      :scale: 80%
      :alt: Image comparison button

#. Follow instructions to run the `oe-image-manifest-script`. Upload the
   resulting .tar.gz file and choose which branch you want to compare it to.

   .. figure:: ../../_figures/clear-linux-dissector/image-comparison-form.png
      :scale: 80%
      :alt: Create a new comparison

#. The resulting list will show which packages are in the original Yocto Project
   image and the corresponding |CL| packages.

   .. figure:: ../../_figures/clear-linux-dissector/image-comparison-result.png
      :scale: 80%
      :alt: Image comparison result

Compare |CL| Releases
*********************

Use the `Release comparison` tool to view the differences between two |CL|
releases. Before comparing |CL| releases, you must first import the |CL| releases
that you want to compare by following the steps in `Import Data`_.
 
#. From the home page, click on :guilabel:`Release comparison`.

   .. figure:: ../../_figures/clear-linux-dissector/release-comparison-select.png
      :scale: 80%
      :alt: Release comparison button

#. Select the two releases you'd like to compare and click :guilabel:`CREATE COMPARISON`.

   .. figure:: ../../_figures/clear-linux-dissector/release-comparison-form.png
      :scale: 80%
      :alt: Select releases to compare

#. The resulting list will show changes between the two releases such as packages
   added, upgraded, and downgraded.

   .. figure:: ../../_figures/clear-linux-dissector/release-comparison-result.png
      :scale: 80%
      :alt: Release comparison result
