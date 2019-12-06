.. _aws-web:

|CL-ATTR| on Amazon Web Services\*
##################################

This tutorial explains how to create and launch a |CL|
:abbr:`AMI (Amazon Machine Image)` instance from the
:abbr:`AWS\* (Amazon Web Services)` console and complete the following tasks:

#. Locate and select the |CL| OS Basic AMI in the AWS Marketplace.
#. Create a new public and private key pair to allow you to connect to your
   |CL| instance securely.
#. Launch the new |CL| instance and connect to it.
#. Update your instance of |CL| using the :command:`swupd` command.
#. Stop the |CL| instance.

.. contents::
   :local:
   :depth: 1

Prerequisites
*************

This tutorial assumes the following statements are true:

* You are using a linux-based system to access AWS and can run :command:`SSH`
  to access the remote |CL| AWS image.
* Your browser puts downloaded files in the :file:`$HOME/Downloads`
  directory.
* You have already set up an AWS user account and logged into the AWS
  console.

.. note::
   This tutorial uses a |CL| AMI t2.micro instance that is eligible for the
   AWS free tier. To learn more about AWS and setting up an account, visit the
   AWS website at http://aws.amazon.com.

Locate, select, and launch the |CL| Basic AMI
*********************************************

#. Start from your main AWS services console menu in your browser and select
   the :guilabel:`EC2` text as shown in Figure 1:

   .. figure:: /_figures/aws/aws-web-1.png
      :scale: 50 %
      :alt: AWS Console

      Figure 1: :guilabel:`AWS Console`

   This selection brings up your :guilabel:`EC2 Dashboard` menu.

#. To create a new |CL| instance from the :guilabel:`EC2 Dashboard` menu,
   select the :guilabel:`Launch Instance` button as shown in Figure 2:

   .. figure:: /_figures/aws/aws-web-2.png
      :scale: 50 %
      :alt: EC2 Dashboard

      Figure 2: :guilabel:`EC2 Dashboard`

   This selection takes you to the
   :guilabel:`Step 1: Choose an Amazon Machine Image (AMI)` menu.

#. To find the :guilabel:`Clear Linux OS Basic` AMI in the
   :guilabel:`Step 1: Choose an Amazon Machine Image (AMI)` menu, do the
   following:

   #. In the lefthand navigation window, select the
      :guilabel:`AWS Marketplace` menu item to bring up the search bar to
      :guilabel:`Search AWS Marketplace Products`.

   #. In the search bar, type "clear linux os" and press the :kbd:`Enter` key
      to search for and locate the :guilabel:`Clear Linux OS Basic` AMI.

   #. Select the :guilabel:`Clear Linux OS Basic` AMI by clicking the
      :guilabel:`Select` button as shown in Figure 3:

      .. figure:: /_figures/aws/aws-web-3.png
         :scale: 50 %
         :alt: Step 1: Choose AMI

         Figure 3: :guilabel:`Step 1: Choose AMI`

   #. A pop-up dialog box appears showing you more information about the
      :guilabel:`Clear Linux OS Basic` AMI along with the pricing details for
      running |CL| on different platform configurations as shown in Figure 4.
      Select the :guilabel:`Continue` button.

      .. figure:: /_figures/aws/aws-web-4.png
         :scale: 50 %
         :alt: Clear Linux OS Basic

         Figure 4: :guilabel:`Clear Linux OS Basic`

#. The :guilabel:`Choose Instance Type` menu appears as shown in Figure 5.

   .. figure:: /_figures/aws/aws-web-5.png
      :scale: 50 %
      :alt: Choose an Instance Type

      Figure 5: :guilabel:`Choose an Instance Type`

   Select the :guilabel:`t2.micro` type by clicking the box on the left side
   of the instance and then select the :guilabel:`Review and Launch` button to
   move to the :guilabel:`Step 7: Review the Instance Launch` menu.

   .. note::

      You can configure the instance details, add additional storage, add
      tags, and configure the security group before selecting the
      :guilabel:`Review and Launch` button if you want to further customize
      this |CL| instance.

#. The :guilabel:`Step 7: Review the Instance Launch` menu, shown in Figure 6,
   allows you to :guilabel:`Cancel` the process, return to
   the :guilabel:`Previous` screen to change the configuration
   or :guilabel:`Launch` the instance defined.

   .. figure:: /_figures/aws/aws-web-6.png
      :scale: 50 %
      :alt: Step 7: Review the Instance Launch

      Figure 6: :guilabel:`Step 7: Review the Instance Launch`

   #. Select the :guilabel:`Launch` button. A dialog box appears, as shown in
      Figure 7, asking you to
      :guilabel:`Select an existing key pair or create a new pair`.

      .. figure:: /_figures/aws/aws-web-7.png
         :scale: 50 %
         :alt: Select an existing key pair or create a new pair

         Figure 7: :guilabel:`Select an existing key pair or create a new pair`

      #. Select the :guilabel:`Create a new key pair` option.

      #. For the :guilabel:`Key pair name` field, enter `AWSClearTestKey`.

      #. Select the :guilabel:`Download Key Pair` button to download the
         :file:`AWSClearTestKey.pem` to your browser's defined
         :file:`Downloads` directory.

      #. When the file finishes downloading, select the
         :guilabel:`Launch Instances` button to proceed to the
         :guilabel:`Launch Status` menu shown in Figure 8.

         .. figure:: /_figures/aws/aws-web-8.png
            :scale: 50 %
            :alt: Launch Status

            Figure 8: :guilabel:`Launch Status`

   #. Once the :guilabel:`Launch Status` page changes to what is shown in
      Figure 9, select the :guilabel:`View Instances` button to view your
      :guilabel:`Instances` dashboard.

      .. figure:: /_figures/aws/aws-web-9.png
         :scale: 50 %
         :alt: View Instance

         Figure 9: :guilabel:`View Instance`

Connect to your Clear Linux OS basic instance
*********************************************

Your :guilabel:`Instances` Dashboard is shown in Figure 10 with the new |CL|
OS basic instance already selected and in the running state. If there are
other instances available, they are also listed but not selected.

.. figure:: /_figures/aws/aws-web-10.png
   :scale: 50 %
   :alt: Instance Dashboard

   Figure 10: :guilabel:`Instance Dashboard`

#. To connect to your running instance, click the :guilabel:`Connect` button
   located at the top of your dashboard. AWS brings up the pop-up dialog
   box shown in Figure 11 describing how to connect to your running instance.

.. _fig-aws-web-11:

.. figure:: /_figures/aws/aws-web-11.png
   :scale: 50 %
   :alt: Connect to Your Instance

   Figure 11: :guilabel:`Connect to Your Instance`

#. Open a terminal on your system. You should be in your :file:`$HOME`
   directory.

#. Copy the previously downloaded keyfile from the :file:`Downloads`
   directory to the current directory.

   .. code-block:: console

      cp Downloads/AWSClearTestKey.pem .

#. Change the attributes of the :file:`AWSClearTestKey.pem` using the
   :command:`chmod` command as instructed in the dialog box shown in Figure
   11.

   .. code-block:: console

      chmod 400 AWSClearTestKey.pem

#. Copy the text highlighted in the :guilabel:`Example:` section that is
   shown in :ref:`figure 11<fig-aws-web-11>`. Paste the copied text into your
   terminal, change the text before the `@` sign to the username `clear`, and
   press the :kbd:`Enter` key to execute the command.

   .. code-block:: console

      ssh -i "AWSClearTestKey.pem" clear@ec2-34-209-39-184.us-west-2.compute.amazonaws.com

#. A message appears on the terminal stating the authenticity of the host
   can't be established and prompts you with the message:

   .. code-block:: console

      The authenticity of host 'ec2-34-209-39-184.us-west-2.compute.amazonaws.com (34.209.39.184)' can't be established.
      ECDSA key fingerprint is SHA256:LrziT5Ar66iBTfia8qmiIsrfBUm/UGam76U8bDR6yJc.
      Are you sure you want to continue connecting (yes/no)?

#. Type `yes` and press the :kbd:`Enter` key. Another warning is printed to
   the terminal and you are now at the command prompt of your new |CL|
   instance.

   .. code-block:: console

      Warning: Permanently added 'ec2-34-209-39-184.us-west-2.compute.amazonaws.com,34.209.39.184' (ECDSA) to the list of known hosts.
      clear@clr-96a8565d0ca54b0c80364a1e5e7b0f88 ~ $

Update the |CL| instance
************************

Run the :command:`sudo swupd update` command to update the operating
system as shown in Figure 12:

.. figure:: /_figures/aws/aws-web-12.png
   :scale: 50 %
   :alt: sudo swupd update

   Figure 12: :guilabel:`sudo swupd update`

In this example, we updated from version 18940 to 19100.

Stop the |CL| instance
**********************

When you are finished using your AWS |CL| instance, you must stop it using
the :guilabel:`Instances` dashboard to stop accruing charges. Complete the
following steps from the :guilabel:`Instances` dashboard to stop your AWS |CL|
instance from running.

#. Select the :guilabel:`Actions` button to bring up a pull-down menu.

#. Select the :guilabel:`Instance State` menu item to expand the options.

#. Select :guilabel:`Stop` menu item to shut down the running instance.

   Figure 13 illustrates these steps.

   .. figure:: /_figures/aws/aws-web-13.png
      :scale: 50 %
      :alt: Stop Instance

      Figure 13: :guilabel:`Stop Instance`

#. A pop-up dialog box appears warning you that any ephemeral storage of
   your instance will be lost. Select the :guilabel:`Yes, Stop` button to stop
   your |CL| instance.

.. figure:: /_figures/aws/aws-web-14.png
   :scale: 50 %
   :alt: Stop Instances

   Figure 14: :guilabel:`Stop Instances`

Congratulations! You are up and running with |CL| on AWS. To see what you
can do with your |CL| instance, visit our :ref:`tutorials <tutorials>`
section for examples on using your |CL| system.

Related topics
**************

* :ref:`azure`
* :ref:`gce`
* :ref:`clr-digitalocean`
