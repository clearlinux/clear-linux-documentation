.. _swupd-3rd-party:

swupd 3rd-party 
###############

Upstream |CL| offers a plethora of `bundles`_ to choose from.  

For users who want access to additional software outside of the distro, 
|CL| provides support for 3rd-party bundles.  

There are two components to 3rd-party bundles:

* Use :command:`mixer` to create 3rd-party bundles

* Use the :command:`swupd` subcommand :command:`3rd-party` to manage repos, 
  consume and manage bundles

Follow this guide to set up a web server to host 3rd-party bundles, 
build an example 3rd-party bundle, install and manage the bundle on a 
client system. 

.. contents::
   :local:
   :depth: 1

Also, see our `general guidelines`_ on sharing 3rd-party bundles.  

Prerequisite
*************

* Familiarity with :command:`mixer`
* Familiarity with :command:`swupd`
* You must be running |CL| version 32570 or higher

.. include:: ./mixer.rst
   :start-after: set-up-nginx-web-server-start:
   :end-before: set-up-nginx-web-server-end:

Create directory to hold 3rd-party app
**************************************

#. Create a top-level directory to hold all apps.
	
   .. code-block:: bash
      
      mkdir ~/my-3rd-party-apps && pushd $_

#. Create a directory for each app and put the content of your software in it.  

   In this example, the `helloclear.sh` app simply prints
   "Hello Clear!" when invoked.  

   .. code-block:: bash

      # make helloclear directory
      mkdir -p helloclear/usr/bin && pushd $_

      # create helloclear.sh script
      cat > helloclear.sh << EOF
      #!/bin/bash
      echo "Hello Clear!"
      EOF

      # make script executable
      chmod +x helloclear.sh

      popd

   .. note:: 
      
      * You can put whatever you want in your app's directory. All of the content 
        within each directory will get copied onto the client system under 
        :file:`/opt/3rd-party/bundles/<repo-name>/`.

      * To use a 3rd-party RPM, it is recommended to extract the content of the RPM 
        into a directory.  Use :command:`rpm2cpio <RPM>| sudo cpio -idv`.
       
Create bundle of 3rd-party app with mixer
*****************************************

Next, use :command:`mixer` to create a bundle for each of the apps from the previous 
section.  

#. Install the mixer tool.
   
   .. code-block:: bash

      sudo swupd bundle-add mixer

#. Create a mixer workspace.
   
   .. code-block:: bash

      mkdir ~/mixer && cd $_

#. Initialize a mix without any default bundles.
   
   .. code-block:: bash

      mixer init --no-default-bundles

#. Configure :file:`builder.conf` to set the default bundle, CONTENTURL, and VERSIONURL.  
   For the "URL"s in this example, it will be IP address of the web server that was
   set up earlier.
   Substitute <IP-address-of-web-server> with the IP address of your host.  

   .. code-block:: bash
      
      mixer config set Swupd.BUNDLE "os-core"
      mixer config set Swupd.CONTENTURL "http://<IP-address-of-web-server>"
      mixer config set Swupd.VERSIONURL "http://<IP-address-of-web-server>"

#. Create an empty local `os-core` bundle.  :command:`swupd` client expects the 
   `os-core` bundle to exist in a mix even if it’s empty.

   .. code-block:: bash
      
      mixer bundle create os-core --local

#. Using the `helloclear` app as an example, create the `helloclear` bundle  
   and use the `content()` directive with the path to the `helloclear` directory in
   the bundle definition.

   Refer to `bundle definition`_ for addition information on how to define a bundle.

   .. code-block:: bash
      
      mixer bundle create helloclear --local
      echo "content($HOME/my-3rd-party-apps/helloclear/)" >> local-bundles/helloclear

#. Add both bundles to the mix.

   .. code-block:: bash
      
      mixer bundle add os-core
      mixer bundle add helloclear

#. Build the bundles and generate the update content.

   .. code-block:: bash
      
      sudo mixer build bundles
      sudo mixer build update

Install and manage 3rd-party bundle on client system
****************************************************

Finally, use the :command:`swupd` client tool to install and 
manage the bundle created with :command:`mixer` earlier.
All installed 3rd-party bundles reside in :file:`/opt/3rd-party/bundles/<repo-name>/`.

#. First, add a repo link to the web server.
   The `os-core` bundle will be added automatically when adding a repo.  
   It contains items that mixer injected into the mix such as version information, 
   format, CONTENTURL, VERSIONURL, and certificate.
    
   .. code-block:: bash

      sudo swupd 3rd-party add my-3rd-party-repo \
      http://<IP-address-of-web-server> --allow-insecure-http

   .. note::
      
      By default, the :command:`swupd` client is designed to communicate 
      with an HTTPS server. For development purposes, the swupd client 
      can talk to an HTTP server if you add the flag ``--allow-insecure-http``.

      To avoid adding this flag each time when invoking :command:`swupd`, enter:

      .. code-block:: bash

         sudo mkdir -p /etc/swupd

         sudo tee -a /etc/swupd/config << EOF
         [GLOBAL]
         allow-insecure-http=true
         EOF

#. Query the list of bundles from the repo.
   
   .. code-block:: bash

      sudo swupd 3rd-party bundle-list -a 

#. Add the `helloclear` bundle.
   
   .. code-block:: bash

      sudo swupd 3rd-party bundle-add helloclear

#. List installed 3rd-party bundles.

   .. code-block:: bash

      sudo swupd 3rd-party bundle-list

#. Look in :file:`/opt/3rd-party` to confirm they were installed there.  
   
   .. code-block:: bash

      tree /opt/3rd-party

   Example output:
   
   .. code-block:: console

      /opt/3rd-party/
      ├── bin
      │   └── helloclear.sh
      ├── bundles
      │   └── my-3rd-party-repo
      │       └── usr
      │           ├── bin
      │           │   └── helloclear.sh
      │           ├── lib
      │           │   └── os-release
      │           └── share
      │               ├── clear
      │               │   ├── bundles
      │               │   │   ├── helloclear
      │               │   │   └── os-core
      │               │   ├── update-ca
      │               │   │   └── Swupd_Root.pem
      │               │   ├── version
      │               │   └── versionstamp
      │               └── defaults
      │                   └── swupd
      │                       ├── contenturl
      │                       ├── format
      │                       └── versionurl
      └── repo.ini

      12 directories, 12 files

Create more bundles and add to client
*************************************

From here on, to add new bundles to your mix, follow these steps:

#. Follow the steps above to add a new directory for each app and put content into it.

#. In the mixer workspace, run :command:`mixer versions update`.

#. Follow the remaining mixer process to add and build bundles.  

On the client side:

#. Run :command:`sudo swupd 3rd-party update` to update to the latest version of your mix.

   .. note::
      
      If `swupd autoupdate` is enabled, 3rd-party repositories will update 
      automatically as well during regular swupd update.  

#. Now, you can see and add the new bundles.

Some limitations of 3rd-party bundles
*************************************

#. You cannot upload your bundles to a shared community repo because bundles
   are tied to your particular mix with its own certificate. 
   You have to host your own and share your repo.

#. As with upstream bundles, 3rd-party bundles installation is simply the unpacking 
   of files onto your system.  It cannot perform pre or post-installation actions such as 
   adding a favorite shortcut to the Gnome desktop dock, for example.

Related topics
**************

* :ref:`autospec`
* :ref:`mixer`
* :ref:`bundles`
* :ref:`swupd-guide`

.. _bundles: 
   https://clearlinux.org/software
.. _bundle definition:
   https://docs.01.org/clearlinux/latest/guides/clear/mixer.html#id16
.. _general guidelines:
   https://community.clearlinux.org/t/about-the-3rd-party-sw-category/4072
