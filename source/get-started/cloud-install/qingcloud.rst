.. _qingcloud:

|CL-ATTR| on QingCloud\*
###########################

This tutorial describes how to create and launch a Clear Linux OS instance from the QingCloud QingCloud\* console.

.. contents:: 
   :local:
   :depth: 1


Prerequisites
*************

This tutorial assumes that you have completed the following default
configurations:

*  Your environment can run SSH to access remote Clear Linux OS virtual hosts.
*  You know the absolute path where the browser downloaded the file.
*  You have set up a user account for QingCloud and that the account is
   enabled and logged in to the QingCloud console. To learn more about Qingyun
   and setting up an account, please visit Qingyun's official
   `website <https://www.qingcloud.com>`_.


Select and start |CL| virtual host QingCloud console
*****************************************************

#. In the browser, in the main menu of the QingCloud console, select "Compute"
   , "Host" , then click the "Create" option.

   .. figure:: /_figures/qingcloud/QingCloud-1.png
      :scale: 50 %
      :alt: QingCloud console

   When you select this option, the page jumps to the Create Host page.

#. On the host creation page, first click the "System" option, then click the
   |CL| icon on the far right , and click the "Next" button.

   .. figure:: /_figures/qingcloud/QingCloud-2.png
      :scale: 50 %
      :alt: Select Clear Linux OS to create virtual host

      Select |CL| to create a virtual host

   After that, you will come to the configuration selection interface.

#. In the configuration selection interface, you can see virtual hosts of
   different hardware configuration types, such as adjusting the number of CPU
   cores, memory size, and hard disk and copy backup strategies. Here we will
   choose the default configuration for the next demonstration.

   .. figure:: /_figures/qingcloud/QingCloud-3.png
      :scale: 50 %
      :alt: Configuration selection

      Configuration selection

   After clicking the "Next" button, you will come to the network settings
   interface.

#. In the network settings interface, you can create a private VPC network or
   quickly test the Clear Linux OS to select the base network. Here we choose
   "Basic Network" .

   .. figure:: /_figures/qingcloud/QingCloud-4.png
      :scale: 50 %
      :alt: Network settings

      Network Settings

   In the basic information setting interface, you need to enter the virtual
   host name and set the SSH key login method.

Create an SSH key (Optional)
============================

#. If you haven't created an SSH key before, click the "Create one" button to
   create an SSH key.

   .. figure:: /_figures/qingcloud/QingCloud-6.png
      :scale: 50 %
      :alt: Create SSH key

      Create SSH Key

   After clicking the "Create a" button, the page will jump to the SSH key
   creation interface.

#. In the SSH key creation interface, you can fill in the key name, and select
   the encryption method you need. After confirming that it is correct, click
   the "Submit" button.

   .. figure:: /_figures/qingcloud/QingCloud-6.png
      :scale: 50 %
      :alt: New SSH key

      New SSH Key

   After submission, the key download button will pop up.

#. After the key download button appears, please click the download button
   within 10 minutes to complete the download of the key, and save the key to
   a local place for later connection to the virtual host.

   .. figure:: /_figures/qingcloud/QingCloud-7.png
      :scale: 50 %
      :alt: Download SSH key

      Download SSH Key

   After closing the download dialog, the interface will jump to the previous
   "Basic Information Settings" interface

After ensuring that the SSH key has been properly downloaded and saved,
check the basic information of the virtual host. After confirming that it is
correct, click the "Create" button.

   .. figure:: /_figures/qingcloud/QingCloud-8.png
      :scale: 50 %
      :alt: Confirm the information and create a virtual host

      Confirm the information and create a virtual host

After confirming, QingCloud will create the Clear Linux OS virtual host. You
can check the current status of the virtual host in the new interface.

Apply for a public IP and add it to the virtual 
***********************************************

#. Since QingCloud does not automatically assign a public IP address to a
   virtual host created using the default network, we need to manually apply
   and add it to the virtual host. Click the "Network and CDN" button on the
   left side of the navigation bar .

   .. figure:: /_figures/qingcloud/QingCloud-9.png
      :scale: 50 %
      :alt: Network and CDN

      Network and CDN

   After clicking, you will come to the network and CDN configuration
   interface.

#. In the new page, as shown in Figure 10, click the "Public IP" button on the
   left , and click the "Apply" button in the middle to create a public IP.

   .. figure:: /_figures/qingcloud/QingCloud-10.png
      :scale: 50 %
      :alt: Apply for public IP

      Apply for public IP   

   After clicking the application, the prompt bar will pop up, read it
   carefully and click the "Continue to apply for public IP" button.

   .. figure:: /_figures/qingcloud/QingCloud-11.png
      :scale: 50 %
      :alt: Confirmation in the prompt bar

      Confirmation in the prompt bar

After that, it will jump to the interface for applying for public IP.

#. On the application for public network IP page, confirm and fill in the
   relevant information, including the charging mode and bandwidth limit (the 
   flow rate mode is used in this tutorial and the 2Mbps bandwidth limit is
   set). After confirming that it is correct, click "Submit" Button.

   .. figure:: /_figures/qingcloud/QingCloud-12.png
      :scale: 50 %
      :alt: Confirmation of Public IP Application

      Confirmation of Public IP Application

#. After that, click the "Calculate" and "Network Card" buttons in the
   navigation bar to come to the network card interface.

   .. figure:: /_figures/qingcloud/QingCloud-13.png
      :scale: 50 %
      :alt: NIC interface

      Network Interface

#. On the network card interface, select the network card of the |CL| host
   that you just created, and click the "More Actions" button above , and then
   click the "Binding Public Network IPv4" button.

   .. figure:: /_figures/qingcloud/QingCloud-14.png
      :scale: 50 %
      :alt: Bind selected

      Bind selected

#. On the binding public network IP confirmation interface, select the public
   IP address that has just been applied for, and click the "Submit" button below . After waiting a moment, the status will change.

   .. figure:: /_figures/qingcloud/QingCloud-15.png
      :scale: 50 %
      :alt: Commit binding

      Commit binding

   .. figure:: /_figures/qingcloud/QingCloud-16.png
      :scale: 50 %
      :alt: Public network IP binding succeeded

      Public network IP binding succeeded

Connect to |CL| virtual 
*********************************

Please click the "Calculate" and "Host" buttons on the left side of the
navigation bar to confirm that the current virtual host is running and has a
public IP address bound.

.. figure:: /_figures/qingcloud/QingCloud-17.png
   :scale: 50 %
   :alt: Confirm that the virtual host is currently in a normal state

   Confirm that the virtual host is currently in a normal state

#. Copy the public IP address of the current Clear Linux OS virtual host and
   connect using an SSH client. Here we need to use the previously saved SSH
   key.

#. In this tutorial, the MobaXterm client is used as an example to demonstrate
   the login process. Check each item as shown. For the user name, we choose
   root. For the key, select the SSH key that was downloaded and saved to the
   local computer .

   .. figure:: /_figures/qingcloud/QingCloud-18.png
      :scale: 50 %
      :alt: SSH login virtual host settings

      SSH login virtual host settings

#. After the setting is successful, click Login to log in to the |CL| virtual
   host.

   .. figure:: /_figures/qingcloud/QingCloud-19.png
      :scale: 50 %
      :alt: SSH login successful

      SSH login successful

Remove |CL| virtual host
************************

This section explains how to delete a |CL| virtual host created on QingCloud.

By the left navigation bar select "Calculate" , "master" , the hosts found |CL|
you just created, as this host 20 is selected, and then click on the top as
shown in the "More Actions" button to select "Delete" , you can Delete the
virtual host.

   .. figure:: /_figures/qingcloud/QingCloud-20.png
      :scale: 50 %
      :alt: Remove Clear Linux OS Virtual Host 

      Remove Clear Linux OS Virtual Host

Delete the applied public IP 
****************************

This section explains how to delete the applied public IP address on QingCloud.

Select "Network and CDN" , "Public IP" from the navigation bar on the left ,
and then find the public IP address just applied. Select this item as shown,
then click the "More Actions" button above and select "Delete" to delete.

   .. figure:: /_figures/qingcloud/QingCloud-21.png
      :scale: 50 %
      :alt: Delete public network IP address

      Delete public network IP address
      