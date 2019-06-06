.. _gce:

Launch |CL-ATTR| Compute Engine on Google\* Cloud Platform
##########################################################

This tutorial walks you through the steps to create a virtual machine
instance of |CL-ATTR| on `Google Cloud Platform`_ (GCP).

#. Sign in your Google account on the
   `Google Cloud Console <https://console.cloud.google.com/>`_:

   .. figure:: figures/gce/00-sign-in.png
      :scale: 50 %
      :alt: Sign in Google services

#. Google Cloud Platform uses **Projects** to manage resources.
   Select or create a new project for hosting the |CL| VM.

   .. note::

      Reference the
      `Quickstart Using a Linux VM <https://cloud.google.com/compute/docs/quickstart-linux>`_
      guide to get familiar with the process of creating VM instances on GCP.

#. Navigate to the latest |CL|
   `release folder <https://download.clearlinux.org/releases/current/clear/>`_
   to view currently released ``gce`` image, and download the image archive
   *clear-<release number>-gce.tar.gz*.

   You don't need to uncompress the image archive, the intact file will
   be uploaded to the Google Cloud Storage later.

#. Create a *Storage Bucket* for hosting the |CL| image source archive
   downloaded in the previous step:

   * Click the *Navigation menu* icon on the upper left screen menu.

   * Select the *Storage* item from the side bar on the left. You will
     be sent to the Storage Browser tool or the Cloud Storage overview page.

   .. figure:: figures/gce/01-cloud-storage.png
      :scale: 50 %
      :alt: Browse Google Cloud Storage

   .. note::
      You may need to create a billing account and link to this project
      before you create a bucket.

   .. figure:: figures/gce/02-storage-browser.png
      :scale: 50 %
      :alt: Cloud Storage Broswer tool

   * Click the ``CREATE BUCKET`` button to enter the bucket creation tool.
     The bucket name must be unique as buckets in the Cloud Storage share
     a single global namespace.

     You can leave the rest of options as defaults, and select the
     ``Create`` button at the bottom to create a *Bucket*.

     .. figure:: figures/gce/03-create-bucket.png
        :scale: 50 %
        :alt: Set an unique bucket name

#. Once the bucket is created, press the ``Upload files`` button
   on the Bucket details page to upload the |CL| GCE image archive
   to the named bucket:

   .. figure:: figures/gce/04-bucket-created.png
      :scale: 50 %
      :alt: Cloud Storage bucket is available for storing objects

   .. figure:: figures/gce/10-image-upload.png
      :scale: 50 %
      :alt: Uploading the image source archive file

   .. figure:: figures/gce/11-bucket-uploaded.png
      :scale: 50 %
      :alt: Image archive imported complete

#. Browse the Compute Engine Image library page:

   * Click the *Navigation menu* icon on the upper left screen menu.

   * Hover mouse over the *Compute Engine* menu and select *Images*.

     .. figure:: figures/gce/20-gce-image.png
        :scale: 50 %
        :alt: Go to Google Compute Engine Image library

#. On the Compute Engine Image library page, click the ``[+] CREATE IMAGE``
   menu item to create a custom image:

   .. figure:: figures/gce/20-image-library.png
      :scale: 50 %
      :alt: Create a Google Compute Engine image

#. In the VM image creation page, change the image source type to
   *Cloud Storage file*.

#. Under :guilabel:`Cloud Storage file`, select :guilabel:`Browse`.

#. Locate the *clear-<release number>-gce.tar.gz*,
   and click :guilabel:`Select`.

   .. figure:: figures/gce/21-create-image.png
      :scale: 50 %
      :alt: Create the image using the imported image archive object

   Accept all default options, and click the ``Create`` button
   at the bottom to import the Clear Linux GCE image to the image library.

   .. figure:: figures/gce/22-image-list.png
      :scale: 50 %
      :alt: Clear Linux Compute Engine image is created

#. After the |CL| image is imported, you can launch a VM instance running
   |CL|:

   * Click the *Navigation menu* icon on the upper left screen menu.

   * Hover mouse over the *Compute Engine* menu group and select
     the *VM instances* item.

   .. figure:: figures/gce/30-vm-instances.png
      :scale: 50 %
      :alt: Go to VM instances catalog

#. If no VM instance was created in this project, you will be prompted to
   create one.

#. Alternatively, click the ``CREATE INSTANCE`` button on the VM
   instances page to create a VM instance.

   .. figure:: figures/gce/30-vm-none.png
      :scale: 50 %
      :alt: Prompt for VM creation

   .. figure:: figures/gce/30-vm-catalog.png
      :scale: 50 %
      :alt: List of VM instances

   * In :guilabel:`Region`, decide on a region based on the
     `Best practices for Compute Engine regions selection`_ .

   * Under *Boot disk*, click the ``Change``.

     .. figure:: figures/gce/30-create-vm.png
        :scale: 50 %
        :alt: Use custom image while creating Clear Linux VM instance

   * Select the *Custom images* tab for using Clear Linux OS GCE image.

     .. figure:: figures/gce/31-select-boot-disk.png
        :scale: 50 %
        :alt: Select Clear Linux boot disk to create a VM instance

   * Scroll down to the bottom of the VM instance creation page,
     expand the *Management, security, disks, networking, sole tenancy* group.

     .. figure:: figures/gce/40-clear-vm-security.png
        :scale: 50 %
        :alt: Clear Linux requires setting up SSH keys

     .. note::
        |CL| does not allow SSH login with a root account by default.
        As a result, you need to configure the VM instance with your
        SSH public key, so that you are able to remote access to it.

        Refer also to :ref:`security` for more details.

   * Click the *Security* tab, copy and paste your SSH public key:

     .. figure:: figures/gce/40-ssh-key.png
        :scale: 50 %
        :alt: Set SSH key for remote login

     .. warning::

        The username is assigned from characters preceding ``@`` in the
        email address, included in the SSH key. The dot symbol "." is not
        allowed, as it is an invalid character while creating user accounts
        in |CL|.

   * Click the ``Create`` button to create the |CL| VM.

#. The Clear Linux VM instance is created and offered a public IP address:

   .. figure:: figures/gce/41-vm-created.png
      :scale: 50 %
      :alt: Clear Linux VM instance is created and started

#. You can now SSH login to the VM by using the IP address obtained in the
   previous step, and the username associated with the SSH public key:

   .. figure:: figures/gce/42-ssh-vm.png
      :scale: 50 %
      :alt: SSH log in to the Clear Linux VM

.. _Google Cloud Platform: https://cloud.google.com/

.. _Best practices for Compute Engine regions selection: https://cloud.google.com/solutions/best-practices-compute-engine-region-selection