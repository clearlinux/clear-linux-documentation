.. _clear-linux-dissector:

Clear Linux Dissector
#####################

The Clear Linux Dissector is a web application that compares contents of Linux-based images.

.. contents:: :local:
   :depth: 1

Description
+++++++++++

If you do not have a Linux image, yet, but you have a pretty good idea of what you want to include in your image, you can `View Distro Data`_.

If you already have a Yocto Project image that you would like to build with Clear, you can `Compare Images With Clear`_ to find the necessary packages. You can also compare images in order to find new patches for performance and security enhancements.

You can also `Compare Clear Releases`_ to see the changes between two Clear Linux Releases.

Set Up
++++++

Clear Linux Dissector is a web application, not a website, which means you will need to set up your own instance in order to use it. This tutorial outlines how to set up your own instance of the Clear Linux Dissector with the necessary data for usage.

Set Up Instance
===============

#. Clone the clear-linux-dissector-web git repo.
   
   .. code-block:: bash

        $ git clone https://github.com/intel/clear-linux-dissector-web.git

#. Change directory into clear-linux-dissector-web.

   .. code-block:: bash

        $ cd clear-linux-dissector-web

#. Run the dockersetup.py script. Note that if you are behind a proxy, you must set the command line variables `--http-proxy`, `--https-proxy`, and `--socks-proxy`. This script will ask for a username and password to create a superuser; take note of these credentials as you will use this to log in to the web interface.

   .. code-block:: bash

        $ ./dockersetup.py

#. After you run the dockersetup, the Clear Linux Dissector should be up and running on your localhost at https://localhost:8081. Now, you should be able to see the front end interface, but before using the Clear Linux Dissector, you must import data.

Import Clear Linux Data
=======================

There are two ways to import Clear Linux Data: from the command line and from the User Interface. Either way, the data will be imported from http://download.clearlinux.org/releases.

From Command Line
-----------------

To import the latest Clear Linux release, run the following command (`branchname` can be anything; it is simply a name to refer to the imported Clear Linux release). Ensure you use this exact command, as paths are in relation to the layersapp docker image and not your system. 

.. code-block:: bash

    $ docker-compose run --rm layersapp /opt/layerindex/layerindex/tools/import_clear.py -d -p /opt/dissector -o /opt/sources -b <branchname>

To import a specific Clear Linux release, pass in the variable `--release` with the release number (e.g. 31380).

.. code-block:: bash

    $ docker-compose run --rm layersapp /opt/layerindex/layerindex/tools/import_clear.py -d -p /opt/dissector -o /opt/sources -b clear-31380 -r 31380


From User Interface
-------------------

Visit https://localhost:8081/layerindex/comparison/import/. 

.. figure:: /_figures/clear-linux-dissector/distro-data-import.png
   :alt: Distro Data Import

   'Figure 1: Distro Data Import Page'

The first time you import Clear Linux data, you will need to create a new branch. You can choose to update your branch in subsquent imports.

To import the latest Clear Linux release, check the Get latest box. Otherwise, input which release you want to import. 

Click import and you will be taken to a page that will display the task status. It will take a long time to upload the Clear Linux data. This will be the final page when the Clear Linux data is completely uploaded.

.. figure:: /_figures/clear-linux-dissector/distro-data-import-final.png
   :alt: Distro Data Import Finished

   'Figure 2: Finished Distro Data Import'

Import Yocto Project Data (for comparing Yocto Project images)
==============================================================

Currently, you can only import Yocto Project Data from the command line. The data will be imported from https://layers.openembedded.org.

From Command Line
-----------------

To import the latest Yocto Project data from the master branch, run the following command:

.. code-block:: bash

    $ docker-compose run --rm layersapp /opt/layerindex/layerindex/tools/import_layers.py https://layers.openembedded.org

You can also import Yocto Project data from a specific branch. Before doing so, you must create a branch object in the admin page. Navigate to https://localhost:8081/admin/layerindex/branch/add/ and input the Branch name and the corresponding Bitbake Branch name (e.g. zeus).

.. figure:: /_figures/clear-linux-dissector/create-yoctoproject-branch.png
   :alt: Create Yocto Project Branch

   'Figure 3: How to Create Yocto Project Branch'

Now, you can run the following command to import a specific Yocto Project branch:

.. code-block:: bash

    $ docker-compose run --rm layersapp /opt/layerindex/layerindex/tools/import_layers.py https://layers.opnembedded.org -b zeus

You can also update your Yocto Project branches with the following command:

.. code-block:: bash

    $ docker-compose run --rm layersapp /opt/layerindex/layerindex/update.py

View Distro Data
++++++++++++++++

If you have a pretty good idea of what you want in your clear image, you can view Distro Data to find proper packages. 

#. From homepage, click on `Distro Data`.

   .. figure:: /_figures/clear-linux-dissector/distro-data-select.png
      :alt: Distro Data Select

      Select Distro Data

#. Select which Clear Linux distribution you want to search in the `Branch` section in the top right, and then search for the package you'd like to include.

   .. figure:: /_figures/clear-linux-dissector/distro-data-form.png
      :alt: Distro Data Form

      Distro Data Form

#. Select the package you want to include. 

#. You can now see the Clear Linux and corresponding Yocto Project versions of your package side by side, as well as Patches and configure options.

   .. figure:: /_figures/clear-linux-dissector/distro-data.png
      :alt: Distro Data

      Distro Data

   .. figure:: /_figures/clear-linux-dissector/distro-data-patches.png
      :alt: Distro Data Patches

      Distro Data Patches

   .. figure:: /_figures/clear-linux-dissector/distro-data-configure-options.png
      :alt: Distro Data Configure Options

      Distro Data Configure Options

Compare Images With Clear
+++++++++++++++++++++++++

If you already have a Yocto Project image that you want to build with Clear, you can use Image Comparison to find the necessary packages. Before starting, ensure that you are on the machine that built the Yocto Project image. 

#. From homepage, click on `Image comparsion`. 

   .. figure:: /_figures/clear-linux-dissector/image-comparison-select.png
      :alt: Image Comparison Select

      Image Comparison Select

#. Follow instructions to run the oe-image-manifest-script and upload the result .tar.gz file and choose which branch you want to compare it to. 

   .. figure:: /_figures/clear-linux-dissector/image-comparison-form.png
      :alt: Image Comparison Form

      Image Comparison Form

#. Resulting list will show which packages are in the original Yocto Projectimage and the corresponding Clear Linux packages. 

   .. figure:: /_figures/clear-linux-dissector/image-comparison-result.png
      :alt: Image Comparison Result

      Image Comparison Result

Compare Clear Releases
++++++++++++++++++++++

If you want to view the differences between two Clear releases, you can use the Release Comparison. Before starting, you must import the two Clear releases you'd like to compare by following How to Import Clear Linux Data. 

#. From homepage, click on `Release Comparison`.

   .. figure:: /_figures/clear-linux-dissector/release-comparison-select.png
      :alt: Release Comparison Select

      Release Comparison Select

#. Select the two releases you'd like to compare and click `Create Comparison`.

   .. figure:: /_figures/clear-linux-dissector/release-comparison-form.png
      :alt: Release Comparison Form

      Release Comparison Form

#. Resulting list will show changes between the two releases, such as packages added, upgraded, and downgraded. 

   .. figure:: /_figures/clear-linux-dissector/release-comparison-result.png
      :alt: Release Comparison Result

      Result Comparison Result
