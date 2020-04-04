.. _clr-digitalocean:

|CL-ATTR| on DigitalOcean\*
###########################

This guide explains how to import a |CL-ATTR| image to `DigitalOcean`_
and then deploy a VM instance. 

.. contents::
   :local:
   :depth: 1

Prerequisites
*************

* Set up a DigitalOcean account.

* Create an SSH key on your client system that you will use to remote 
  into the VM. You can follow the `DigitalOcean's SSH key creation guide`_.  

Add |CL| Image to DigitalOcean
******************************

Before you can deploy a |CL| instance on DigitalOcean, you need to add
an image since it's currently not available in its marketplace.
You can use our pre-built image or you can build your own custom image.  

Use pre-built image
===================

.. note::
   Our cloud images (`clear-<release version>-digitalocean.img.gz`) for 
   DigitalOcean are considered **Beta** until we finish setting up our 
   automated testing of the images against the DigitalOcean environment. 
   Apart from the initial version, `clear-31870-digitalocean.img.gz`_, we 
   cannot guarantee that future versions and updates to the initial 
   version is problems-free.    

.. bktan8 - commented out until the images are fully validated by DevOps
   and go live on official Downloads page.  
   Go to the |CL| `downloads` page and copy the URL for the
   **Cloud Guest Legacy** image. See Figure 1.
   figure:: ../../_figures/digitalocean/01-digitalocean.png
   :scale: 100 %
   :alt: Cloud Guest Legacy image
   Figure 1: Cloud Guest Legacy image

#. Copy the URL for `clear-31870-digitalocean.img.gz`_.

#. Skip to the `Upload image`_ section.

Build custom image
==================

For this method, you need a |CL| system to generate an image using
the *clr-installer* tool.

#. Add the *clr-installer* and *gzip* bundles.  

   .. code-block:: bash
      
      sudo swupd bundle-add clr-installer gzip

#. Create an image configuration YAML file.
   See `Installer YAML Syntax`_ for more information on the clr-installer 
   configuration YAML syntax.

   .. code-block:: bash

      cat > clear-digitalocean.yaml << EOF
      #clear-linux-config

      # switch between aliases if you want to install to an actual block device
      # i.e /dev/sda
      block-devices: [
         {name: "bdevice", file: "clear-digitalocean.img"}
      ]

      targetMedia:
      - name: \${bdevice}
        size: "800M"
        type: disk
        children:
        - name: \${bdevice}1
          fstype: ext4
          options: -O ^64bit
          mountpoint: /
          size: "800M"
          type: part

      bundles: [
          bootloader,
          openssh-server,
          os-cloudguest,
          os-core,
          os-core-update,
          systemd-networkd-autostart
        ]

      autoUpdate: false
      postArchive: false
      postReboot: false
      telemetry: false
      legacyBios: true

      keyboard: us
      language: en_US.UTF-8
      kernel: kernel-kvm

      version: 0
      EOF

   The settings that are required in order to make the image
   work on DigitalOcean are:

   * *os-cloudguest* bundle: Allows DigitalOcean to provision the 
     image with settings such as hostname, resource (CPU, memory, 
     storage) sizing, and user creation.
   * *legacyBios: true*: The image need to support legacy BIOS to boot 
     on DigitalOcean.
 
#. Generate the image.

   .. code-block:: bash

      sudo clr-installer -c clear-digitalocean.yaml

   The output should be :file:`clear-digitalocean.img`.

#. Compress the image with *gzip* to save bandwidth and upload time.

   .. code-block:: bash

      gzip clear-digitalocean.img

   The output should be :file:`clear-digitalocean.img.gz`.

   .. note::
      
      *bzip2* is the other compression format DigitalOcean accepts.

Upload image
============

#. On DigitalOcean's website, go to :menuselection:`MANAGE --> Images 
   --> Custom Images`.  

   See Figure 1.

   .. figure:: ../../_figures/digitalocean/01-digitalocean.png
      :scale: 100 %
      :alt: DigitalOcean - Upload custom images

      Figure 1: DigitalOcean - Upload custom images

#. Select an upload method.

   * To import a pre-built image from |CL| `downloads`_, click 
     :guilabel:`Import via URL`, paste the URL, and click :guilabel:`Next`.

     See Figure 2.

     .. figure:: ../../_figures/digitalocean/02-digitalocean.png
        :scale: 100 %
        :alt: DigitalOcean - Import via URL

        Figure 2: DigitalOcean - Import via URL

   * To import your custom image, click :guilabel:`Upload Image` 
     and select the image from your client system.

#. Set the :guilabel:`DISTRIBUTION` type as :guilabel:`Unknown`.

   See Figure 3.

   |

#. Choose your preferred datacenter region.  

#. Click :guilabel:`Upload Image`.
   Wait for the upload to finish before proceeding to the next section. 

   .. figure:: ../../_figures/digitalocean/03-digitalocean.png
      :scale: 100 %
      :alt: DigitalOcean - Set image distribution type, region, tag

      Figure 3: DigitalOcean - Set image distribution type, region, tag

Create and Deploy a |CL| Instance
*********************************

#. On DigitalOcean's website, go to :menuselection:`MANAGE --> Droplets` 
   and then click :guilabel:`Create Droplet`.

   See Figure 4.

   .. figure:: ../../_figures/digitalocean/04-digitalocean.png
      :scale: 100 %
      :alt: DigitalOcean - Create Droplet

      Figure 4: DigitalOcean - Create Droplet

#. Under :guilabel:`Choose an image`, select :guilabel:`Custom images`.

   See Figure 5.

   |

#. Select your uploaded |CL| image.
  
   .. figure:: ../../_figures/digitalocean/05-digitalocean.png
      :scale: 100 %
      :alt: DigitalOcean - Choose custom image

      Figure 5: DigitalOcean - Choose custom image

#. Under :guilabel:`Choose a plan`, select your preferred plan.

   See Figure 6.

   .. figure:: ../../_figures/digitalocean/06-digitalocean.png
      :scale: 100 %
      :alt: DigitalOcean - Choose plan

      Figure 6: DigitalOcean - Choose plan

#. Under :guilabel:`Choose a datacenter region`, select the region you 
   want the instance deployed to.

   See Figure 7.

   .. figure:: ../../_figures/digitalocean/07-digitalocean.png
      :scale: 100 %
      :alt: DigitalOcean - Choose datacenter region

      Figure 7: DigitalOcean - Choose datacenter region

#. Assign SSH key to default *clear* user.  

   By default, the user *clear* will be added to the instance and
   an SSH key must be assigned to this account.  

   a. Under :guilabel:`Authentication`, select :guilabel:`SSH keys` and 
      click :guilabel:`New SSH Key`.  

      See Figure 8.

      .. figure:: ../../_figures/digitalocean/08-digitalocean.png
         :scale: 100 %
         :alt: DigitalOcean - Add SSH key

         Figure 8: DigitalOcean - Add SSH key
   
   #. Copy and paste your SSH public key in the :guilabel:`SSH key content` 
      text field.

      See Figure 9.

      |

   #. Give a name for the SSH key.

   #. Click :guilabel:`Add SSH Key`.

      .. figure:: ../../_figures/digitalocean/09-digitalocean.png
         :scale: 100 %
         :alt: DigitalOcean - Add public SSH key

         Figure 9: DigitalOcean - Add public SSH key
   
   .. note::
     
      If you need to add additional users to the instance, you can do that
      wth a YAML-formatted *cloud-config* user data script.  
      For more information on cloud-config scripting for |CL|, see our 
      subset implementation of cloud-init called `micro-config-drive`_.  

      a. Under :guilabel:`Select additional options`, 
         select :guilabel:`User data`.

      #. Add your YAML-formatted *cloud-config* user data in the field below.  
         Here is a simple example:

         .. code-block:: console

            #cloud-config

            users:
            - name: foobar
              gecos: Foo B. Bar
              homedir: /home/foobar
              ssh-authorized-keys:
                - ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC65OihS4UP27xKOpqKWgT9
                  mgUNwEqhUEpTGGvopjT65Y/KU9Wfj6EYsdGzbHHcMUhFSTxAUAV4POH5d0LR
                  MzI7sXMe528eCmpm2fTOHDDkVrurP/Jr2bjB9IrfSMkBYS8uRd603xNg/RDq
                  EH3XzVeEDdEAxoej0mzsJ2UkQSBi+PD1J7JeCbX2lsb55x2yWzaUa+BTai7+
                  /TU4UabTRDtFTiXhx2rImSSguofDISVll6W5TTzbGmHdoEI+8DIAFU66ZgC9
                  SzL75LQi1YAWlj5XG+dXhN6Ev6KFM34odvWdxeCj0jcx5UIXcieBfOuLujEH
                  dVybwNLG7hxDy/67BA1j username@mydomain.com
              sudo:
                - [ "ALL=(ALL) NOPASSWD:ALL" ]

#. Under :guilabel:`Finalize and create`:
   
   a. Set the number of instances you want to deploy.

   #. Set the hostname for the instance.

   See Figure 10.

   |

#. Click :guilabel:`Create Droplet` to deploy the instance.

   .. figure:: ../../_figures/digitalocean/10-digitalocean.png
      :scale: 100 %
      :alt: DigitalOcean - Finalize and create Droplet

      Figure 10: DigitalOcean - Finalize and create Droplet

Connect to Your |CL| Instance
*****************************

#. On DigitalOcean's website, go to :menuselection:`MANAGE --> Droplets`.

   See Figure 11.

   |

#. Get the IP address of your |CL| instance.  

   .. figure:: ../../_figures/digitalocean/11-digitalocean.png
      :scale: 100 %
      :alt: DigitalOcean - Get Droplet IP address

      Figure 11: DigitalOcean - Get Droplet IP address

#. On your client system, SSH into your instance.
   For example:

   .. code-block:: bash
      
      ssh clear@<IP-address-of-instance> -i <SSH-private-key>
   
 
Related topics
**************

* :ref:`gce`
* :ref:`azure`
* :ref:`aws-web`

.. _clear-31870-digitalocean.img.gz: https://cdn.download.clearlinux.org/releases/31870/clear/clear-31870-digitalocean.img.gz 

.. _DigitalOcean: https://www.digitalocean.com/

.. _DigitalOcean's SSH key creation guide: https://www.digitalocean.com/docs/droplets/how-to/add-ssh-keys/create-with-openssh/

.. _downloads: https://clearlinux.org/downloads

.. _Installer YAML Syntax:
   https://github.com/clearlinux/clr-installer/blob/master/scripts/InstallerYAMLSyntax.md

.. _micro-config-drive: https://github.com/clearlinux/micro-config-drive
