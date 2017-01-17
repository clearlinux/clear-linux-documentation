.. _wp-install:

Creating a Clear Linux WordPress* server
########################################

Prerequisites
=============

This tutorial assumes you have already
:ref:`installed Clear Linux on a bare metal system <bare-metal-install>`
and that you have :ref:`set up a LAMP web server <web-server-install>`.

Additionally, all the steps on this tutorial were tested using a NUC6i5SYH
Intel® NUC. Visit the `NUC6i5SYH product page`_ for detailed information.

Before installing any new packages, update the |CL| OS with the
console command:

.. code-block:: console

   sudo swupd update


Creating a WordPress server
===========================

This tutorial walks you through the process of installing the WordPress
components on your |CL| LAMP server. At the end of the
:ref:`web server tutorial <web-server-install>`, we created the initial
WordPress MySQL database `WordPress` using phpMyAdmin\* and MariaDB\*.
With the LAMP server up and running, we can add the WordPress components
needed to host a WordPress website on your host system.

Throughout this tutorial we will reference your website name as
<your_website>. There are numerous articles available on-line regarding how
to name your website and acquire the necessary certificates. Those tasks are
beyond the scope of this tutorial.

There are also several actions you can take to harden your website from
attacks. The security of your website and the data it contains are complex
and ever-evolving tasks. They should be at the top of your to do list if you
plan to expose your website to the outside world. This tutorial does not
address security measures that you can take to harden your site but we
strongly encourage you to look into it.

Installing WordPress
--------------------

The folks at WordPress have created a `step-by-step guide`_ to install
WordPress quickly and easily. We are following this procedure very closely.

We are setting up a WordPress blog which can be accessed at:

http://<your_website>/blog

To accomplish this setup, we must put the WordPress components in the
:file:`/usr/share/httpd/htdocs/blog` directory.

Let us get started:


1. To move to the top-level of the website’s root directory, enter the
   following command:

   .. code-block:: console

      cd /usr/share/httpd/htdocs

2. To download the latest version of WordPress, enter the following command:

   .. code-block:: console

      sudo curl -O https://wordpress.org/latest.tar.gz

3. To extract the all the files and directories from the downloaded file,
   enter the following command:

   .. code-block:: console

      sudo tar –xzvf latest.tar.gz

4. To rename the top-level WordPress directory to “blog”, enter the following
   command:

   .. code-block:: console

      sudo mv wordpress blog

5. To remove the downloaded tar file, enter the following command:

   .. code-block:: console

      sudo rm latest.tar.gz

Setting up WordPress
--------------------

With the WordPress components loaded into the
:file:`/usr/share/httpd/htdocs/blog` directory, we can set everything up.

Instead of editing the :file:`wp_config.php` file manually, we are using the
web-based configuration tool to setup the database name and user. We created
both in the :ref:`web server tutorial <web-server-install>`. In your browser,
go to: http://<your_website>/blog/wp-admin/install.php.

Your screen should look like figure 1:

.. figure:: figures/wp-install-1.png
    :alt: WordPress language selection
    :width:     600

    WordPress language selection screen.

Select :guilabel:`English` for the language and click the :guilabel:`Continue`
button.

The WordPress installation continues until the welcome screen shown in figure
2 appears:

.. figure:: figures/wp-install-2.png
    :alt: WordPress welcome screen
    :width:     600

    WordPress welcome screen.

Click the :guilabel:`Let’s go!` button to enter the information.

Enter the database name, username, and password we used when creating the
database:

   Database name:       WordPress
   Database username:   wordpressuser
   Database password:   wp-example

Enter the following values for the database host and the table prefix:

   Database host:  localhost
   Table prefix:   wp\_

Figure 3 shows the filled out fields.

.. figure:: figures/wp-install-3.png
    :alt: Database connection details
    :width:     600

    These details are needed for WordPress to connect to the database.

.. note::

   When you enter your password into the password field, it will be in clear
   text and not asterisks.

After entering all the data for accessing your database, click the
:guilabel:`Submit` button.

Figure 4 shows the following screen letting you know the communication
between WordPress and your database has been successfully set up.

.. figure:: figures/wp-install-4.png
    :alt: Successful database connection.
    :width:     600

    This screen shows WordPress was able to connect to the MySQL database.

Click the :guilabel:`Run the install` button.

Let the installer run until WordPress is fully installed on your system.

Once the installation is completed, you can name your blog and create a
Wordpress username and password, see figure 5.

.. figure:: figures/wp-install-5.png
    :alt: WordPress user creation
    :width:     600

    Provide WordPress the needed information to create a site and a user
    with the permissions to change it.

Enter all the required information and click the
:guilabel:`Install WordPress` button.

Once the installation is complete, the initial login screen appears, see
figure 6:

.. figure:: figures/wp-install-6.png
    :alt: WordPress login
    :width:     600

    The WordPress login screen.

Enter your WordPress username and password.
Check the :guilabel:`Remember me` checkbox, to save your credentials.
Click :guilabel:`Log in`.

Figure 7 shows the WordPress dashboard after a successful login:

.. figure:: figures/wp-install-7.png
    :alt: WordPress Dashboard
    :width:     600

    The WordPress dashboard appears after you log in successfully.

You are ready to go!

To check out your blog as it is seen by the outside world, enter:
http://<your_website>/blog on your browser. Figure 8 shows the result:

.. figure:: figures/wp-install-8.png
    :alt: WordPress blog
    :width:     600

    The final result is the fully realized WordPress blog.

**Congratulations, your WordPress blog is up and running!**

You have successfully installed WordPress on a host system.

Add new entries to your blog and share them with the world using |CLOSIA|!

.. _`step-by-step guide`:
   https://codex.wordpress.org/Installing_WordPress#Famous_5-Minute_Install

.. _`NUC6i5SYH product page`:
   http://www.intel.com/content/www/us/en/nuc/nuc-kit-nuc6i5syh.html