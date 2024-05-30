.. _wp-install:

WordPress\* Server
##################

This tutorial shows you how to install the WordPress\* components on your |CL|
:abbr:`LAMP (Linux, Apache\*, MySQL\*, PHP)` server. At the end of
:ref:`lamp-server-install`, you created a WordPress-ready database using
phpMyAdmin\* and MariaDB\*. Now that the LAMP server is up and running, you
can add the WordPress components needed to host a WordPress website on your system.

Before you begin
****************

This tutorial assumes that you have successfully completed
:ref:`bare-metal-install-desktop` and you have :ref:`lamp-server-install`.

Create a WordPress server
*************************

WordPress can be installed in a variety of ways. These instructions are
written for users who have followed our instructions for installing phpMyAdmin
when they :ref:`set up a LAMP web server <lamp-server-install>`. Note that
all steps in this tutorial have been tested using a NUC6i5SYH Intel® NUC.
Visit the `NUC6i5SYH product page`_ for detailed information.

Numerous online articles are available to help you name your website and
acquire the necessary certificates. Those tasks are beyond the scope of this tutorial.

You can take several actions to harden your website from attacks. The security
of your website and the data it contains are complex and ever-evolving tasks.
Prioritize security if you plan to expose your website to the outside world.
This tutorial does not address security measures that you can take to harden
your site but we strongly encourage you to take action.

.. note::

   Throughout this tutorial, we reference your website name as <your_website>.


Download WordPress and manage directories
=========================================

For this tutorial, you will create a WordPress blog that can be accessed at:
\http://<your_website>/blog.

To accomplish this setup, you must add WordPress components to the :file:`/var/www/html/blog`
directory.

Follow these steps:


#. Navigate to the top level of the website’s root directory:

   .. code-block:: bash

      cd /var/www/html

#. Download the latest version of WordPress:

   .. code-block:: bash

      sudo curl -O https://wordpress.org/latest.tar.gz

#. Extract all files and directories from the downloaded file:

   .. code-block:: bash

      sudo tar –xzvf latest.tar.gz

#. Rename the top-level WordPress directory to “blog”:

   .. code-block:: bash

      sudo mv wordpress blog

#. Remove the downloaded tar file:

   .. code-block:: bash

      sudo rm latest.tar.gz

Set up WordPress with web-based GUI
===================================

Recall that you created a database and user when you installed phpMyAdmin when you
set up a |CL| based :ref:`web server <lamp-server-install>`. Next, you must
connect WordPress to the database and install WordPress.

To continue with the setup, go to: \http://<your_website>/blog/wp-admin/install.php.
The WordPress language option screen appears, as shown in figure 1.

#. Select :guilabel:`English` and click :guilabel:`Continue`.

   .. rst-class:: dropshadow

   .. figure:: ../_figures/wordpress/wp-install-1.png
      :alt: WordPress language selection
      :width:     600

      `Figure 1: WordPress language selection screen.`


   The WordPress installation continues until the Welcome screen appears, as shown in
   figure 2:

   .. rst-class:: dropshadow

   .. figure:: ../_figures/wordpress/wp-install-2.png
      :alt: WordPress welcome screen
      :width:     600

      `Figure 2: WordPress Welcome screen.`

#. Click :guilabel:`Let’s go!`.

#. Enter database connection specifics in the screen that appears, as shown in figure 3
   below.

   * Database name:       WordPress
   * Database username:   wordpressuser
   * Database password:   wp-example  (asterisks will not appear in the text box)
   * Database host:  localhost
   * Table prefix:   wp\_

   .. rst-class:: dropshadow

   .. figure:: ../_figures/wordpress/wp-install-3.png
      :alt: Database connection details
      :width:     600

      `Figure 3: Information necessary for WordPress to connect to the database.`

#. Click :guilabel:`Submit` to complete the setup.

   Figure 4 shows the confirmation screen that verifies a successful setup. WordPress
   is connected to the MariaDB database.

   .. rst-class:: dropshadow

   .. figure:: ../_figures/wordpress/wp-install-4.png
      :alt: Successful database connection.
      :width:     600

      `Figure 4: Successful WordPress connection.`

#. Click :guilabel:`Run the install`.
   The installer runs until WordPress is fully installed on your system.

Complete successful login
=========================

Once the installation is complete, you can name your blog and create a WordPress username
and password. See figure 5.

.. rst-class:: dropshadow

.. figure:: ../_figures/wordpress/wp-install-5.png
   :alt: WordPress user creation
   :width:     600

   `Figure 5: WordPress site information screen.`


#. Enter all required information.
#. Click :guilabel:`Install WordPress`.
#. Verify that the initial login screen appears once the installation is complete. See figure 6:

   .. rst-class:: dropshadow

   .. figure:: ../_figures/wordpress/wp-install-6.png
      :alt: WordPress login
      :width:     600

      `Figure 6: The WordPress login screen.`

#. Enter your WordPress username and password.
#. Check :guilabel:`Remember me` to save your credentials.
#. Click :guilabel:`Log in`.

Figure 7 shows the WordPress dashboard after a successful login:

.. rst-class:: dropshadow

.. figure:: ../_figures/wordpress/wp-install-7.png
   :alt: WordPress Dashboard
   :width:     600

   `Figure 7: The WordPress dashboard.`

You are ready to go!

To check out your blog as it is seen by the outside world, enter:
\http://<your_website>/blog on your browser. Figure 8 shows the result:

.. figure:: ../_figures/wordpress/wp-install-8.png
   :alt: WordPress blog
   :width:     600

   `Figure 8: Your WordPress blog.`

**Congratulations, your WordPress blog is up and running!**

You have successfully installed WordPress on a host system.

Add new entries to your blog and share them with the world using |CL|!

*Intel and the Intel logo are trademarks of Intel Corporation or its subsidiaries.*

.. _`step-by-step guide`:
   https://codex.wordpress.org/Installing_WordPress#Famous_5-Minute_Install

.. _`NUC6i5SYH product page`:
   http://www.intel.com/content/www/us/en/nuc/nuc-kit-nuc6i5syh.html
