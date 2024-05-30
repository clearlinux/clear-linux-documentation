.. _import-clr-aws:

Import Clear Linux Image and Launch Instance on AWS
###################################################

Clear Linux is available on the AWS marketplace.  However, it may not 
be the latest version because we only update the marketplace on a 
periodic basis, as often as weekly or but maybe monthly as well.  
If you want to use the latest release from us or upload your own 
custom image, follow this guide.  

.. contents::
   :local:
   :depth: 1

Prerequisites
*************

* You are familiar with AWS and how to use it

Download or create a |CL| image for AWS
***************************************

Obtain an AWS |CL| image using one of these methods.  

Download pre-built image
========================
#. Go to the `Downloads`_ page and download the 
   *Amazon\* Web Services (AWS)* image.

#. Uncompress it.  

Create a custom image using clr-installer
=========================================
#. On a |CL| system, open a terminal.

#. Install the `clr-installer` bundle.

   .. code-block:: bash

      sudo swupd bundle-add clr-installer

#. Download a sample `aws.yaml`_ configuration file. 

#. Make changes to the configuration file as needed.
   See `Installer YAML Syntax`_ for more information on clr-installer 
   configuration YAML syntax.

#. Download the `AWS image post-install script`_ and make it executable.

#. Produce an image with clr-installer.

   .. code-block:: bash
      
      clr-installer --template $PWD/aws.yaml

Create an S3 bucket
*******************

#. Log into AWS.

#. Go to :guilabel:`Services`, :guilabel:`Storage`, and select :guilabel:`S3`.
   See Figure 1. 

   .. figure:: ../../_figures/aws/import-clr-aws-01.png
      :scale: 70%
      :alt: AWS Services - S3 Management Console

      Figure 1: AWS Services - S3 Management Console

#. Click :guilabel:`+ Create bucket`.

   .. figure:: ../../_figures/aws/import-clr-aws-02.png
      :scale: 70%
      :alt: AWS S3 - Create bucket

      Figure 2: AWS S3 - Create bucket

#. Set a bucket name and select a region.  
   See Figure 3.

   .. figure:: ../../_figures/aws/import-clr-aws-03.png
      :scale: 70%
      :alt: AWS S3 - Create bucket - Set bucket name and region

      Figure 3: AWS S3 - Create bucket - Set bucket name and region

#. Leave the :guilabel:`Configure options` and :guilabel:`Set permissions`
   settings as is or configure as desired.  See Figure 4 and 5.

   .. figure:: ../../_figures/aws/import-clr-aws-04.png
      :scale: 70%
      :alt: AWS S3 - Create bucket - Configure options

      Figure 4: AWS S3 - Create bucket - Configure options

   .. figure:: ../../_figures/aws/import-clr-aws-05.png
      :scale: 70%
      :alt: AWS S3 - Create bucket - Set permissions

      Figure 5: AWS S3 - Create bucket - Set permissions

#. At the :guilabel:`Review` screen, click :guilabel:`Create bucket`.

   .. figure:: ../../_figures/aws/import-clr-aws-06.png
      :scale: 70%
      :alt: AWS S3 - Create bucket - Review

      Figure 6: AWS S3 - Create bucket - Review

   The created bucket should appear.  See Figure 7.

   .. figure:: ../../_figures/aws/import-clr-aws-07.png
      :scale: 70%
      :alt: AWS S3 - Created bucket

      Figure 7: AWS S3 - Created bucket

Upload the |CL| image into the bucket
*************************************

#. Click on the bucket.
   See Figure 8.

   .. figure:: ../../_figures/aws/import-clr-aws-08.png
      :scale: 70%
      :alt: AWS S3 - Select bucket

      Figure 8: AWS S3 - Select bucket

#. Click :guilabel:`Upload`.
   See Figure 9.

   .. figure:: ../../_figures/aws/import-clr-aws-09.png
      :scale: 70%
      :alt: AWS S3 - Upload

      Figure 9: AWS S3 - Upload

#. Click :guilabel:`Add files` and select the |CL| image file to upload.
   See Figure 10.

   .. figure:: ../../_figures/aws/import-clr-aws-10.png
      :scale: 70%
      :alt: AWS S3 - Add files

      Figure 10: AWS S3 - Add files

#. Click :guilabel:`Next`.  Leave remaining settings as is or set as desired.
   See Figure 11, Figure 12, and Figure 13.

   .. figure:: ../../_figures/aws/import-clr-aws-11.png
      :scale: 70%
      :alt: AWS S3 - Add files

      Figure 11: AWS S3 - Add files

   .. figure:: ../../_figures/aws/import-clr-aws-12.png
      :scale: 70%
      :alt: AWS S3 - Set permissions

      Figure 12: AWS S3 - Set permissions

   .. figure:: ../../_figures/aws/import-clr-aws-13.png
      :scale: 70%
      :alt: AWS S3 - Set properties

      Figure 13: AWS S3 - Set properties

#. Click :guilabel:`Upload` to upload the image.
   See Figure 14.

   .. figure:: ../../_figures/aws/import-clr-aws-14.png
      :scale: 70%
      :alt: AWS S3 - Upload

      Figure 14: AWS S3 - Upload

Add a user to IAM with AWS_CLI privilege
****************************************

#. Go to :guilabel:`Services`, :guilabel:`Security, Identity, & Compliance`,
   and select :guilabel:`IAM`.
   See Figure 15. 

   .. figure:: ../../_figures/aws/import-clr-aws-15.png
      :scale: 70%
      :alt: AWS Services - IAM

      Figure 15: AWS Services - IAM

#. On the left navigation bar under :guilabel:`Access management`, 
   select :guilabel:`Users`.
   See Figure 16.

   .. figure:: ../../_figures/aws/import-clr-aws-16.png
      :scale: 70%
      :alt: AWS AIM - Access management

      Figure 16: AWS AIM - Access management

#. Click :guilabel:`Add user`.
   See Figure 17.
   
   .. figure:: ../../_figures/aws/import-clr-aws-17.png
      :scale: 70%
      :alt: AWS AIM - Add user

      Figure 17: AWS AIM - Add user

#. Under the :guilabel:`Set user details` section, enter a user name.
   See Figure 18.

   .. figure:: ../../_figures/aws/import-clr-aws-18.png
      :scale: 70%
      :alt: AWS AIM - Enter user name and select access type

      Figure 18: AWS AIM - Enter user name and select access type

#. Under the :guilabel:`Select AWS access type` section, 
   checkmark :guilabel:`Programmatic access`.
   See Figure 18.

#. Click :guilabel:`Next: Permissions`.

#. Under :guilabel:`Set permissions`, select :guilabel:`Add user to group`.
   See Figure 19.

   .. figure:: ../../_figures/aws/import-clr-aws-19.png
      :scale: 70%
      :alt: AWS AIM - Set user permissions

      Figure 19: AWS AIM - Set user permissions

#. Under :guilabel:`Add user to group`, enter `AWS_CLI` into search window.
   Checkmark :guilabel:`AWS_CLI`.
   See Figure 19.

#. Click :guilabel:`Next: Tags`.

#. Click :guilabel:`Next: Review`.

#. Click :guilabel:`Create user`.
   See Figure 20.

   .. figure:: ../../_figures/aws/import-clr-aws-20.png
      :scale: 70%
      :alt: AWS AIM - Create user

      Figure 20: AWS AIM - Create user

#. After the user is successfully added, save the :guilabel:`Access key ID`
   and the :guilabel:`Secret access key`.  These will be used when setting up
   the AWS CLI tool at a later step.
   See Figure 21.

   .. figure:: ../../_figures/aws/import-clr-aws-21.png
      :scale: 70%
      :alt: AWS AIM - Access key ID and secret access key

      Figure 21: AWS AIM - Access key ID and secret access key

#. Click :guilabel:`Close`.

Install and configure the AWS CLI tool on your system
*****************************************************

#. To install the tool on |CL|, simply run:

   .. code-block:: bash

      sudo swupd bundle-add cloud-api

   .. note:

      If you are using a different OS, follow the 
      `Installing the AWS CLI version 2`_ guide.

#. Configure it with your security credentials, default region,
   and default output format. See `Configuring the AWS CLI`_ for more information.

   .. code-block:: bash

      aws configure

   Below is an example (using the security credentials that was created in 
   the previous section):

   .. code-block:: console

      AWS Access Key ID [None]: AKIA5LEGQPQ3EUB3JMS7
      AWS Secret Access Key [None]: EcvbWpWr+Gp7NhBoVEacwR3EifzN7xTTg8B1PHvO
      Default region name [None]: us-west-2
      Default output format [None]: json 

#. Verify your credentials are good.

   .. code-block:: bash
      
      aws iam list-access-keys

   If you get something like the example below, then make sure you set your 
   system date and time properly.

   .. code-block:: console

      An error occurred (SignatureDoesNotMatch) when calling the ListAccessKeys operation: Signature expired: 20200305T153154Z is now earlier than 20200305T231847Z (20200305T233347Z - 15 min.)

Import a snapshot of the |CL| image
***********************************

#. Create a :file:`container.json` with the description of the image to import.
   Specify the name of the S3 bucket that was created earlier for the 
   `S3Bucket` field and the name of |CL| image that was uploaded to the S3 bucket
   for the `S3Key`.

   Here's an example:

   .. code-block:: console

      {
        "Description": "My Clear Linux AWS 32400 Image",
        "Format": "raw",
        "UserBucket": {
          "S3Bucket": "my-clearlinux-bucket",
          "S3Key": "clear-32400-aws.img"
        }
      }

#. Import a snapshot of the image.

   .. code-block:: bash

      aws ec2 import-snapshot \
      --description "My Clear Linux AWS 32400 Snapshot" \
      --disk-container file://container.json

   You should get an output similar this example:

   .. code-block:: console

      {
        "Description": "My Clear Linux AWS 32400 Snapshot",
        "ImportTaskId": "import-snap-00fa9ccd98e9b8378",
        "SnapshotTaskDetail": {
            "Description": "My Clear Linux AWS 32400 Snapshot",
            "DiskImageSize": 0.0,
            "Format": "RAW",
            "Progress": "3",
            "Status": "active",
            "StatusMessage": "pending",
            "UserBucket": {
                "S3Bucket": "my-clearlinux-bucket",
                "S3Key": "clear-32400-aws.img"
            }
        }
    }

#. Using the `ImportTaskId` from the previous step, check the status 
   of the import.  For example:

   .. code-block:: bash

      snapshot_id=$(aws ec2 describe-import-snapshot-tasks \
      --import-task-ids "import-snap-00fa9ccd98e9b8378" \
      | grep SnapshotId | awk -F '"' '{print $4}')

   Wait for the `Status` field to show `completed` before proceeding.

   The resulting `snapshot_id` will be used to create an AMI in 
   the next section.

Create an AMI from the snapshot
*******************************

There are 2 methods to create an AMI from the snapshot.

* *AWS CLI Method*:
    
  .. code-block:: bash
    
     aws ec2 register-image \
     --name "My-Clear-Linux-32400-AMI" \
     --description "My Clear Linux 32400 AMI" \
     --architecture x86_64 \
     --virtualization-type hvm \
     --ena-support \
     --root-device-name "/dev/sda1" \
     --block-device-mappings "[ 
       { 
         \”Deviceame\": \"/dev/sda1\", 
         \"Ebs\": {
           \"SnapshotId\": \"$snapshot_id\" 
         } 
       } 
     ]"

* *GUI Method*: 

  #. Go to :guilabel:`Services`, :guilabel:`Compute`, and select 
     :guilabel:`EC2`.
     See Figure 22. 

     .. figure:: ../../_figures/aws/import-clr-aws-22.png
        :scale: 70%
        :alt: AWS Services - EC2

        Figure 22: AWS Services - EC2
    
  #. Click :guilabel:`Snapshots`.
     See Figure 23. 

     .. figure:: ../../_figures/aws/import-clr-aws-23.png
        :scale: 70%
        :alt: AWS Services - Snapshots

        Figure 23: AWS Services - Snapshots

  #. Locate the snaphot using the `Snapshot ID`.
     See Figure 24.

     .. figure:: ../../_figures/aws/import-clr-aws-24.png
        :scale: 70%
        :alt: AWS Services - Snapshots

        Figure 24: AWS Services - Snapshots
    
  #. Right-click it and select :guilabel:`Create Image`.

  #. Configure as follows:
 
     * Enter the name in the :guilabel:`Name` field
     * Enter the description in the :guilabel:`Description` field
     * Set the :guilabel:`Architecture` as `x86_64`
     * Set the :guilabel:`Virtualization type` as `Hardware-assisted virtualization`
     * Set the :guilabel:`Root device name` as `/dev/sda1`

     See Figure 25.

     .. figure:: ../../_figures/aws/import-clr-aws-25.png
        :scale: 70%
        :alt: AWS Services - Snapshots

        Figure 25: AWS Services - Snapshots
    
  #. Click :guilabel:`Create`.

Launch an instance
******************

#. Go to :guilabel:`Services`, :guilabel:`Compute`, and select 
   :guilabel:`EC2`.
   See Figure 26. 

   .. figure:: ../../_figures/aws/import-clr-aws-26.png
      :scale: 70%
      :alt: AWS Services - EC2

      Figure 26: AWS Services - EC2
    
#. Click the :guilabel:`Launch Instance` dropdown and select 
   :guilabel:`Launch Instance`.
   See Figure 27. 

   .. figure:: ../../_figures/aws/import-clr-aws-27.png
      :scale: 70%
      :alt: AWS Services - Launch instance

      Figure 27: AWS Services - Launch instance

#. On the left navigation bar, select :guilabel:`My AMIs`.
   See Figure 28. 

   .. figure:: ../../_figures/aws/import-clr-aws-28.png
      :scale: 70%
      :alt: AWS Services - Select AMI

      Figure 28: AWS Services - Select AMI

#. Find your AMI and click :guilabel:`Select`.

#. From here onward, configure the details of your instance as desired 
   and launch it.
   
Connect to your |CL| instance
*****************************

#. Follow these steps to `connect to your instance`_.

Related topics
**************

* :ref:`azure`
* :ref:`gce`
* :ref:`clr-digitalocean`

.. _Downloads: 
   https://clearlinux.org/downloads
.. _aws.yaml: 
   https://cdn.download.clearlinux.org/current/config/image/aws.yaml
.. _AWS image post-install script:
   https://cdn.download.clearlinux.org/current/config/image/aws-disable-root.sh
.. _Installing the AWS CLI version 2: 
   https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html
.. _Configuring the AWS CLI: 
   https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html
.. _connect to your instance: 
   https://docs.01.org/clearlinux/latest/get-started/cloud-install/aws-web.html#connect-to-your-clear-linux-os-basic-instance
.. _Installer YAML Syntax:
   https://github.com/clearlinux/clr-installer/blob/master/scripts/InstallerYAMLSyntax.md

