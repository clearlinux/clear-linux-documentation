.. _greengrass:

How to enable Greengrass and OpenVINO on |CL-ATTR|
##################################################

Introduction
************

Hardware accelerated Function-as-a-Service (FaaS) enables cloud developers 
to deploy inference functionalities [1] on Intel IoT edge devices with 
accelerators (Integrated GPU, FPGA, and Movidius).  These functions provide 
a great developer experience and seamless migration of visual analytics from 
cloud to edge in a secure manner using containerized environment. 
Hardware-accelerated FaaS provides the best-in-class performance by 
accessing optimized deep learning libraries on Intel IoT edge devices with 
accelerators.

This document describes implementation of FaaS inference samples (based on 
Python 2.7) using AWS Greengrass [1] and lambdas [2]. These lambdas can be 
created, modified, or updated in the cloud and can be deployed from cloud to 
edge using AWS Greengrass. This document covers description of samples, 
pre-requisites for Intel edge device, configuring a Greengrass group, 
creating and packaging lambda functions, deployment of lambdas and various 
options to consume the inference output.

Supported Platforms
*******************

*	Operating System: Clear Linux Build 25930+
*	Hardware:	Intel core platforms (Release supports inference on CPU only)

Description of Samples
**********************

The Greengrass samples are located at the `Edge-Analytics-FaaS`_.

We provide the following Greengrass samples:

*	greengrass_classification_sample.py

  This Greengrass sample classifies a video stream using classification
  networks such as AlexNet and GoogLeNet and publishes top-10 results on AWS 
  IoT Cloud every second.

*	greengrass_object_detection_sample_ssd.py
  
  This Greengrass sample detects objects in a video stream and classifies 
  them using single-shot multi-box detection (SSD) networks such as SSD 
  Squeezenet, SSD Mobilenet, and SSD300. This sample publishes detection 
  outputs such as class label, class confidence, and bounding box 
  coordinates on AWS IoT Cloud every second.

Converting Deep Learning Models
*******************************

Sample Models
=============

For classification, download the BVLC `Alexnet model`_ as an example from
`caffe`_. Any custom pre-trained classification models can be used with the 
classification sample.

For object detection, the sample models optimized for Intel edge platforms 
are present at <model location>. These models are provided as an example, 
but any custom pre-trained SSD models can be used with the object detection 
sample.

Running Model Optimizer
=======================

Follow these instructions for converting deep learning models to 
Intermediate Representation (IR) `using Model Optimizer`_. instructions. For 
example, for above models use the following commands.

For classification using BVLC Alexnet model:

code-block:: console

python3 mo.py --framework caffe --input_model <
model_location>/bvlc_alexnet.caffemodel --input_proto <
model_location>/deploy.prototxt --data_type <data_type> --output_dir <
output_dir> --input_shape [1,3,227,227]

For object detection using SqueezeNetSSD-5Class model,

code-block:: console

python3 mo.py --framework caffe --input_model 
SqueezeNetSSD-5Class.caffemodel --input_proto SqueezeNetSSD-5Class.prototxt 
--data_type <data_type> --output_dir <output_dir>

where <model_location> is the location where the user downloaded the models, 
<data_type> is FP32 or FP16 depending on target device, and <output_dir> is 
the directory where the user wants to store the IR. IR contains .xml format 
corresponding to the network structure and .bin format corresponding to 
weights. This .xml should be passed to <PARAM_MODEL_XML>. In the BVLC 
Alexnet model, the prototxt defines the input shape with batch size 10 by 
default. In order to use any other batch size, the entire input shape needs 
to be provided as an argument to the model optimizer. For example, if you 
want to use batch size 1, you can provide “--input_shape [1,3,227,227]”.


Installing |CL| on the edge device
**********************************

Start with a clean installation of |CL| on a new system, using the :ref:`bare-metal-install` getting started guide

Create user accounts
====================

After the core OS is installed, create two user accounts.  To create a new 
user and set a password for that user, enter the following

commands as a root user:

.. code-block:: console

   useradd <userid>
   passwd <userid>

Replace the <userid> with the name of the user account you want to create
including the password for that user. The :command:`passwd` command prompts
you to enter a new password. Retype the new password for the new user
account just created.

Next, enable the :command:`sudo` command for your new `<userid>`.

To be able to execute all applications with root privileges, add the
`<userid>` to the `wheel group`_.

#. Add `<userid>` to the `wheel` group:

   .. code-block:: bash

      usermod -G wheel -a <userid>


Create the user and group account for the Greengrass daemon:

.. code-block:: console

   useradd ggc_user
   groupadd ggc_group

Add required bundles
====================

Use the `swupd` software updater utility to add the following bundles to enable the OpenVINO software stack:

.. code-block:: console

   swupd bundle-add os-clr-on-clear desktop-autostart computer-vision-basic

The `computer-vision-basic` bundle will install the OpenVINO software, along with the edge device models needed.


Configuring a Greengrass group
==============================

For each Intel edge platform, we need to create a new Greengrass group and
install Greengrass core software to establish the connection between cloud and edge.
•	To create a Greengrass group, follow the instructions in the AWS Greengrass
 	developer guide at:
  https://docs.aws.amazon.com/greengrass/latest/developerguide/gg-config.html

•	To install and configure Greengrass core on edge platform, follow the
  instructions at https://docs.aws.amazon.com/greengrass/latest/developerguide/gg-device-start.html

.. note::
   You will not need to run the `cgroupfs-mount.sh` script in step #6 of 
   Module 1 of the the AWS Greengrass developer guide, as this is enabled 
   already in |CL|. You will need to create an file: `/etc/fstab` file, as |
   CL| does not create one by default.  To do so, use the command: `sudo 
   touch /etc/fstab`

Creating and Packaging Lambda Functions
=======================================

*	To download the AWS Greengrass Core SDK for python 2.7, follow the steps
  1-4 at: https://docs.aws.amazon.com/greengrass/latest/developerguide/create-lambda.html

*	Replace greengrassHelloWorld.py with Greengrass sample
  (greengrass_classification_sample.py/greengrass_object_detection_sample_ssd.py) and zip it with extracted Greengrass SDK folders from the previous step into greengrass_sample_python_lambda.zip. The zip should contain:

 -	greengrasssdk
 -	greengrass sample(greengrass_classification_sample.py or  greengrass_object_detection_sample_ssd.py)

For example,

code-block:: console

zip -r greengrass_lambda.zip greengrasssdk greengrass_object_detection_sample_ssd.py

*	To complete creating lambdas, follow steps 6-11 at:  
  https://docs.aws.amazon.com/greengrass/latest/developerguide/create-lambda.html

*	In step 9(a), while uploading the zip file, make sure to name the handler
  as below depending on the Greengrass sample you are using:
  greengrass_object_detection_sample_ssd.function_handler (or)
  greengrass_classification_sample.function_handler

Deploying  Lambdas
==================

Configuring the Lambda function
-------------------------------

*	After creating the Greengrass group and the lambda function, start configuring the lambda function for AWS Greengrass by following the steps 1-8 in AWS Greengrass developer guide at: https://docs.aws.amazon.com/greengrass/latest/developerguide/config-lambda.html

*	In addition to the details mentioned in step 8 of the AWS Greengrass developer guide, change the Memory limit to 2048MB to accommodate large input video streams.

*	Add the following environment variables as key-value pair when editing the lambda configuration and click on update:
          Key 	                                  Value
PARAM_MODEL_XML	<MODEL_DIR>/<IR.xml>, where <MODEL_DIR> is user specified and contains IR.xml, the Intermediate Representation file from Intel Model Optimizer

PARAM_INPUT_SOURCE	<DATA_DIR>/input.webm to be specified by user. Holds both input and output data. For webcam, set PARAM_INPUT_SOURCE to ‘/dev/video0’
PARAM_DEVICE	For CPU, specify "CPU"
PARAM_CPU_EXTENSION_PATH	/usr/lib64/libcpu_extension.so
PARAM_OUTPUT_DIRECTORY	<DATA_DIR> to be specified by user. Holds both input and output data
PARAM_NUM_TOP_RESULTS	User specified for classification sample.(e.g. 1 for top-1 result, 5 for top-5 results)

*	Add subscription to subscribe or publish messages from Greengrass lambda function by following the steps 10-14 in AWS Greengrass developer guide at: https://docs.aws.amazon.com/greengrass/latest/developerguide/config-lambda.html. The “Optional topic filter” field should be the topic mentioned inside the lambda function.
      For example, openvino/ssd or openvino/classification

Local Resources
---------------
*	Add local resources and access privileges by following the instructions https://docs.aws.amazon.com/greengrass/latest/developerguide/access-local-resources.html. 

Following are the local resources needed for 

CPU:
Name 	  Resource
    Type	Local path 	Access
ModelDir	 Volume	<MODEL_DIR> to be specified by user	Read-Only
Webcam	 Device	/dev/video0
	Read-Only
DataDir	 Volume	<DATA_DIR> to be specified by user. Holds both input and output data.	Read and Write


Deploy
------

*	To deploy the lambda function to AWS Greengrass core device, select “Deployments” on group page and follow the instructions at: https://docs.aws.amazon.com/greengrass/latest/developerguide/configs-core.html

Output Consumption
------------------

There are four options available for output consumption. These options are used to report/stream/upload/store inference output at an interval defined by the variable ‘reporting_interval’ in the Greengrass samples.
 a. IoT Cloud Output:
This option is enabled by default in the Greengrass samples using a variable ‘enable_iot_cloud_output’.  We can use it to verify the lambda running on the edge device. It enables publishing messages to IoT cloud using the subscription topic specified in the lambda (For example, ‘openvino/classification’ for classification and ‘openvino/ssd’ for object detection samples).  For classification, top-1 result with class label are published to IoT cloud. For SSD object detection, detection results such as bounding box co-ordinates of objects, class label, and class confidence are published. To view the output on IoT cloud, follow the instructions at https://docs.aws.amazon.com/greengrass/latest/developerguide/lambda-check.html

 b. Kinesis Streaming:
This option enables inference output to be streamed from the edge device to cloud using Kinesis [3] streams when ‘enable_kinesis_output’ is set to True. The edge devices act as data producers and continually push processed data to the cloud. The users need to set up and specify Kinesis stream name, Kinesis shard, and AWS region in the Greengrass samples.

 c. Cloud Storage using AWS S3 Bucket:
This option enables uploading and storing processed frames (in JPEG format) in an AWS S3 bucket when ‘enable_s3_jpeg_output’ variable is set to True. The users need to set up and specify the S3 bucket name in the Greengrass samples to store the JPEG images. The images are named using the timestamp and uploaded to S3.

 d. Local Storage:
This option enables storing processed frames (in JPEG format) on the edge device when ‘enable_s3_jpeg_output’ variable is set to True. The images are named using the timestamp and stored in a directory specified by ‘PARAM_OUTPUT_DIRECTORY’.

References
-----------

1. AWS Greengrass: https://aws.amazon.com/greengrass/
2. AWS Lambda: https://aws.amazon.com/lambda/
3. AWS Kinesis: https://aws.amazon.com/kinesis/


.. _Edge-Analytics-FaaS: https://github.com/intel/Edge-Analytics-FaaS/tree/master/AWS%20Greengrass

.. _Alexnet model: deploy.prototxt and bvlc_alexnet.caffemodel

.. _using Model Optimizer: https://software.intel.com/en-us/articles/OpenVINO-ModelOptimizer

.. _caffe: https://github.com/BVLC/caffe/tree/master/models/bvlc_alexnet