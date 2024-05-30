.. _mirror-upstream-server:
  
Mirror Upstream |CL| Update Server
##################################

For organizations that want to use the |CL| upstream updates, but want the 
benefits of a local mirror, this tutorial shows how to set up one and
configure your |CL| clients to use it.

.. contents::
    :local:
    :depth: 1

Prerequisites
*************

* The recommended disk space for the mirror server should have at least 100GB 
  of disk space as each complete update content is approximately 45GB.  

Install up |CL| server to host updates
**************************************

#. Follow the :ref:`bare-metal-install-server` guide to install |CL| server.
   Add a user with `Administrator` privilege.

#. After installation is complete, boot it up.

#. Add the `wget` bundle.  This will be used to clone the upstream |CL| server.  

   .. code-block:: bash

      sudo swupd bundle-add wget

Clone the |CL| update content
*****************************

|CL| periodically releases a "minversion", which is a complete update.  
Then, subsequent releases are small updates until the next minversion.

Download a minversion to start your mirror.  

#. Determine a proper minversion by looking at a `Manifest.MoM`_ file 
   for a particular release of |CL|.  

   For example, if you look at 
   https://cdn.download.clearlinux.org/update/33010/Manifest.MoM, 
   you will see that the minversion is 32900.  So clone this version as the 
   starting point.

   .. code-block:: console
      :emphasize-lines: 4

      MANIFEST        30
      version:        33010
      previous:       33000
      minversion:     32900
      filecount:      1131
      timestamp:      1588358889
      contentsize:    0

#. Make a directory to store the cache.

   .. code-block:: bash

      mkdir ~/mirror-download-clearlinux-org && cd $_

#. Recursively download the :file:`update/0` folder.

   .. code-block:: bash

      wget --no-verbose \
      --no-parent --recursive \
      --no-host-directories -erobots=off \
      --reject "index.html" https://cdn.download.clearlinux.org/update/0/

#. Recursively download the :file:`update/version` folder.

   .. code-block:: bash

      wget --no-verbose \
      --no-parent --recursive \
      --no-host-directories -erobots=off \
      --reject "index.html" https://cdn.download.clearlinux.org/update/version/

#. Now, recursively download the determined minversion, which for this example 
   is 32900.

   .. code-block:: bash

      wget --no-verbose \
      --no-parent --recursive \
      --no-host-directories -erobots=off \
      --reject "index.html" https://cdn.download.clearlinux.org/update/32900/

   .. note::

      A minversion is pretty big, which is approximately 45GB.  Depending on your
      proximity to the upstream server and your connection speed to the Internet,
      it may take up to a couple of days or more to complete the download.  So
      be patient.  

#. Download later versions, up to the latest, if you like.

Setup a web server to host the mirrored content
***********************************************

By design, the |CL| swupd client communicates with the update server using
HTTPS for security reasons.  However, it can use HTTP by adding the 
:command:`--allow-insecure-http` flag, if needed.  Setting an HTTPS is a lot 
more involved.  For this tutorial, we'll just use an HTTP server for 
demonstration purpose. 

#. Install the `nginx` bundle.

   .. code-block:: bash

      sudo swupd bundle-add nginx

#. Configure the web server.

   a. Create a symbolic link to the mirrored update content directory.

      .. code-block:: bash
      
         sudo mkdir -p /var/www && cd $_
         sudo ln -sf $HOME/mirror-download-clearlinux-org mirror-download-clearlinux-org

   #. Set up nginx configuration files.

      .. code-block:: bash

         sudo mkdir -p /etc/nginx/conf.d
         sudo cp /usr/share/nginx/conf/nginx.conf.example /etc/nginx/nginx.conf

   #. Grant $USER permission to run the web server.
      
      .. code-block:: bash

         sudo tee -a /etc/nginx/nginx.conf << EOF
         user $USER;
         EOF

   #. Configure the web server.
      
      .. code-block:: bash

         sudo tee -a /etc/nginx/conf.d/mirror-download-clearlinux-org.conf << EOF
         server {
           listen 80;
	   listen [::]:80;
	   server_name localhost;
	   location / {
	     root /var/www/mirror-download-clearlinux-org;
             autoindex on;
           }
         }
         EOF

   #. Set nginx to start automatically on boot and then start it.

      .. code-block:: bash

         sudo systemctl enable nginx --now

Test your mirror
****************

Now, try out your mirror by installing |CL| and adding bundles from it.  

#. Download either the live desktop or live server installer ISO of the 
   `same version` as the mirrored version, which is 32900 for this tutorial.  
   Go to `https://cdn.download.clearlinux.org/releases/<release-version>/clear`.

#. Burn the ISO to a thumb drive.  See :ref:`bootable-usb`.

#. Boot it up and start the installer.  Depending on which version of 
   |CL| you want to install, follow one of these guides:

   * *Desktop* version: :ref:`bare-metal-install-desktop`
   * *Server* version: :ref:`bare-metal-install-server`

   In the :guilabel:`Advanced options` tab of the installer, select 
   :guilabel:`Swupd Mirror`.  See Figure 1.

   .. rst-class:: dropshadow

   .. figure:: ../_figures/mirror-upstream-server/mirror-upstream-server-01.png
      :scale: 100%
      :alt: Advanced options > Swupd Mirror

      `Figure 1: Advanced options > Swupd Mirror`

   In the :guilabel:`Mirror URL` field, set it to the IP address of your mirror.    It should be something like this: http://<IP address of mirror server>/update.
   And check the option :guilabel:`Allow installation over insecure connections (http://)`.  See Figure 2.

   .. rst-class:: dropshadow

   .. figure:: ../_figures/mirror-upstream-server/mirror-upstream-server-02.png
      :scale: 100%
      :alt: Advanced options > Mirror URL setting

      `Figure 2: Advanced options > Mirror URL setting`

#. After installation completes, boot up, and log in.

#. Verify that the swupd client is pointing to your mirror.

   .. code-block:: bash

      sudo swupd info

   Example output:

   .. code-block:: console

      Warning: This is an insecure connection
      The --allow-insecure-http flag was used, be aware that this poses a threat the system

      Distribution:      Clear Linux OS
      Installed version: 32900
      Version URL:       https://192.168.1.100/update
      Content URL:       https://192.168.1.100/update

#. Try listing available bundles on your mirror.

   .. code-block:: bash

      sudo swupd bundle-list -a

#. Add a bundle.

   .. code-block:: bash

      sudo swupd bundle-add <bundle-name>

Keep your mirror in sync with upstream
**************************************

Be sure to keep your mirror in sync with upstream so that your clients have the 
latest and greatest software and security updates.  You can do that continuing
to clone the newer upstream releases.  

.. _Manifest.MoM:
   https://docs.01.org/clearlinux/latest/reference/manpages/swupd.1.html 
