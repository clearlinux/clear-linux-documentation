.. _clear-linux-dissector:

Clear Linux\* Dissector
#######################

The Clear Linux\* Dissector application compares and examines contents of |CL|
and Yocto Project\* images.

.. contents:: :local:
   :depth: 1

Description
***********

The Clear Linux Dissector provides a set of tools to:

* Compare packages, patches, and configuration between a |CL| release and the
  equivalent Yocto Project image.

* Compare |CL| and Yocto Project images to identify the packages needed to move
  from a Yocto Project image to a |CL| image or compare two Yocto Project images
  to identify differences.

* Compare |CL| releases to see differences between |CL| versions.

Prerequisites
*************

Clear Linux Dissector requires the following are installed:

* A version of Linux

* `Docker/* <https://docs.docker.com/v17.09/engine/installation/>`_

* `Docker Compose <https://docs.docker.com/compose/install/>`_

* `Python 3 <https://www.python.org/download/releases/3.0/>`_


Set Up Clear Linux Dissector
****************************

Clear Linux Dissector is a web application. An instance of the application is
required in order to use the tools. To set up the application, follow these steps:

#. Clone the `clear-linux-dissector-web Git repository <https://github.com/intel/clear-linux-dissector-web>`_.

   .. code-block:: bash

      git clone https://github.com/intel/clear-linux-dissector-web.git

#. :command:`cd` into the :file:`clear-linux-dissector-web` directory.

   .. code-block:: bash

      cd clear-linux-dissector-web

#. Run the :file:`dockersetup.py` script.

   If you are behind a proxy, you must also set the proxy command line options
   :command:`--http-proxy`, :command:`--https-proxy`, and :command:`--socks-proxy`.

   .. code-block:: bash

      ./dockersetup.py

   The script will ask for a `username` and `password` to create a superuser;
   make note of these credentials as you will use them to log in to the web
   interface.

#. After running the :file:`dockersetup.py` script, the Clear Linux Dissector
   application should be up and running on localhost. Access the application via
   a browser at `https://localhost:8081`.

   [TODO] Add screenshot of login page.

#. Log into the application using the credentials you entered during set up.

   [TODO] Add screenshot of app home page.

Before using the Clear Linux Dissector, you must first `Import Data`_.

Import Data
***********

Clear Linux Dissector can compare image data from both |CL| and Yocto Project
images. In order to compare an image, the image must first be imported into the
Clear Linux Dissector tool.

|CL| data is imported from http://download.clearlinux.org/releases/. Yocto
Project data is imported from https://layers.openembedded.org.

Import |CL| Data via CLI
========================

* To import the latest |CL| release, use the following command:

  .. code-block:: bash

      docker-compose run --rm layersapp /opt/layerindex/layerindex/tools/import_clear.py -d -p /opt/dissector -o /opt/sources -b <branchname>

* To import a specific |CL| release, use the :command:`-r` flag with the desired
  release number. The following example imports release 31380:

  .. code-block:: bash

      docker-compose run --rm layersapp /opt/layerindex/layerindex/tools/import_clear.py -d -p /opt/dissector -o /opt/sources -b <branchname> -r 31380

`<branchname>` is the name of the new Dissector tool comparison branch for the
|CL| release being imported. The `<branchname>` you provide will be used in the
Dissector GUI during comparison to refer to this imported release.

.. note::

   Do not edit the paths in the command. The paths are relative to the `layersapp`
   Docker image that the application runs in.

Import |CL| Data via GUI
========================

#. On the Clear Linux Dissector application homepage, click
   :guilabel:`Import distro data`.

#. Fill out the Distro Data Import form:

   #. Select :guilabel:`Create new branch`.

   #. Enter a new comparison branch name in the :guilabel:`Name` field.
      The name you provide will be used in the GUI during comparison to refer to
      this imported release.

      [TODO] Do we describe this elsewhere? "You can choose to update your comparison branch during
      later imports."

   #. Enter a short description for the comparison branch in the
      :guilabel:`Short description` field.
      [TODO] Is this required?

   #. Choose the |CL| release to import:

      * To import the latest |CL| release, check the :guilabel:`Get latest` box.

      * To import a specific release, enter the release number in the
        :guilabel:`Release` field. `View all |CL| releases <http://download.clearlinux.org/releases/>`_.

   [TODO] need updated screen shot.

   .. figure:: ../../_figures/clear-linux-dissector/distro-data-import.png
      :scale: 80%
      :alt: Distro Data Import page

#. Click :guilabel:`IMPORT`. The import task status page will load. Note that it
   will take some time to import the data.

#. Once the |CL| data has been imported, you will see a page similar to the
   following:

   [TODO] need updated screen shot.

   .. figure:: ../../_figures/clear-linux-dissector/distro-data-import-final.png
      :scale: 80%
      :alt: Finished distribution data import

Import Yocto Project Data via CLI
=================================

* To import the latest Yocto Project data from the master branch, use the
  following command:

  .. code-block:: bash

      docker-compose run --rm layersapp /opt/layerindex/layerindex/tools/import_layers.py https://layers.openembedded.org

* To import Yocto Project data from a specific branch:

  #. Go to the admin page in your instance of the application. For example:
     `https://localhost:8081/admin`

  #. Under the `LAYERINDEX` section, click :guilabel:`add` to add a
     comparison branch.

     [TODO] New screenshot

  #. Fill out the Add branch form:

     #. Enter the branch name in the :guilabel:`Branch name` field.

     #. Enter the corresponding Bitbake branch name (for example "zeus") in the
        :guilabel:`Bitbake branch` field.

     [TODO] need updated screen shot.

     .. figure:: ../../_figures/clear-linux-dissector/create-yoctoproject-branch.png
        :scale: 80%
        :alt: Importing Yocto Project data from branch

  #. Click :guilabel:`SAVE`.

  #. In your CLI, import the specific Yocto Project branch into your new
     comparison branch. The following example imports the zeus branch:

     .. code-block:: bash

         docker-compose run --rm layersapp /opt/layerindex/layerindex/tools/import_layers.py https://layers.opnembedded.org -b zeus

* To update an existing Yocto Project branch, use the following command:

  .. code-block:: bash

     docker-compose run --rm layersapp /opt/layerindex/layerindex/update.py

View Distribution Data
**********************

Use the `Distro data` tool to view the package data of a specific |CL| or Yocto
Project distribution. Package data includes package version, description, license,
and a link to the package's homepage.

#. From the Clear Linux Dissector application homepage, click on
   :guilabel:`Distro data`.

   [TODO] PICK UP step thru here

#. In the :guilabel:`Branch` dropdown at the top left of the screen, select the
   imported |CL| distribution you want to search in.

   [TODO] need updated screen shot.

   .. figure:: ../../_figures/clear-linux-dissector/distro-data-form.png
      :scale: 80%
      :alt: Select distribution to search

#. Enter the package you would like to examine in the :guilabel:`Keyword` field
   and click :guilabel:`SEARCH`.

#. In the :guilabel:`Package` section, select the package you want to examine.

#. The results listing shows the |CL| and corresponding Yocto Project versions
   of the selected package side-by-side, as well as Patches and configure options.

   [TODO] need updated screen shot. 

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

#. From the Clear Linux Dissector application homepage, click on
   :guilabel:`Image comparison`.

#. On the Compare Image page, follow instructions to run the
   :file:`oe-image-manifest-script`. This will generate a .tar.gz file.

   [TODO] need updated screen shot.

   .. figure:: ../../_figures/clear-linux-dissector/image-comparison-form.png
      :scale: 80%
      :alt: Create a new comparison

#. Upload the .tar.gz file and select which comparison branch you want to compare
   it to.

   [TODO] is it select which Dissector comparison branch to compare to?

#. The resulting list will show which packages are in the original Yocto Project
   image and the corresponding |CL| packages.

   [TODO] need updated screen shot.

   .. figure:: ../../_figures/clear-linux-dissector/image-comparison-result.png
      :scale: 80%
      :alt: Image comparison result

Compare |CL| Releases
*********************

Use the `Release comparison` tool to view the differences between two |CL|
releases. Before comparing |CL| releases, you must first import the |CL| releases
that you want to compare by following the steps in `Import Data`_.

#. From the Clear Linux Dissector application homepage, click on :guilabel:`Release comparison`.

#. Select the releases to compare and click :guilabel:`CREATE COMPARISON`.

   [TODO] need updated screen shot.

   .. figure:: ../../_figures/clear-linux-dissector/release-comparison-form.png
      :scale: 80%
      :alt: Select releases to compare

#. The resulting list will show changes between the two releases such as packages
   added, upgraded, and downgraded.

   [TODO] need updated screen shot.
   
   .. figure:: ../../_figures/clear-linux-dissector/release-comparison-result.png
      :scale: 80%
      :alt: Release comparison result
