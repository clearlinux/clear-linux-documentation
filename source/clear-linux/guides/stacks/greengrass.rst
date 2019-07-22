.. _greengrass:

Enable AWS Greengrass\* and OpenVINO™ toolkit
#############################################

This guide explains how to enable AWS Greengrass\* and OpenVINO™ toolkit.
Specifically, the guide demonstrates how to:

* Set up the Intel® edge device with |CL-ATTR|
* Install the OpenVINO™ toolkit and Amazon Web Services\* (AWS\*)
  Greengrass\* software stacks
* Use AWS Greengrass\* and AWS Lambda\* to deploy the FaaS samples from
  the cloud

.. contents::
   :local:
   :depth: 1

Overview
********

Hardware accelerated Function-as-a-Service (FaaS) enables cloud developers to
deploy inference functionalities [1] on Intel® IoT edge devices with
accelerators (CPU, Integrated GPU, Intel® FPGA, and Intel® Movidius™
technology). These functions provide a great developer experience and
seamless migration of visual analytics from cloud to edge in a secure manner
using a containerized environment. Hardware-accelerated FaaS provides the
best-in-class performance by accessing optimized deep learning libraries on
Intel® IoT edge devices with accelerators.

Supported platforms
*******************

*	Operating System: |CL| latest release
*	Hardware:	Intel® core platforms (that support inference on CPU only)

Sample description
==================

The AWS Greengrass samples are located at `Edge-Analytics-FaaS`_. This
guide uses the 1.0 version of the source code.

|CL| provides the following AWS Greengrass samples:

* `greengrass_classification_sample.py`_

  This AWS Greengrass sample classifies a video stream using classification
  networks such as AlexNet and GoogLeNet and publishes top-10 results on AWS\*
  IoT Cloud every second.

* `greengrass_object_detection_sample_ssd.py`_

  This AWS Greengrass sample detects objects in a video stream and
  classifies them using single-shot multi-box detection (SSD) networks such
  as SSD Squeezenet, SSD Mobilenet, and SSD300. This sample publishes
  detection outputs such as class label, class confidence, and bounding box
  coordinates on AWS IoT Cloud every second.


Install the OS on the edge device
*********************************

Start with a clean installation of |CL| on a new system, using the
:ref:`bare-metal-install-desktop`, found in :ref:`get-started`.

Create user accounts
====================

After |CL| is installed, create two user accounts. Create an administrative
user in |CL| and create a user account for the Greengrass services to use (
see Greengrass user below).

#. Create a new user and set a password for that user. Enter the following
   commands as ``root``:

   .. code-block:: bash

      useradd <userid>
      passwd <userid>

#. Next, enable the :command:`sudo` command for your new <userid>. Add
   <userid> to the `wheel` group:

   .. code-block:: bash

      usermod -G wheel -a <userid>

#. Create a :file:`/etc/fstab` file.

   .. code-block:: bash

      touch /etc/fstab

   .. note::

      By default, |CL| does not create an :file:`/etc/fstab` file.
      You must create this file before the Greengrass service runs.

Add required bundles
====================

Use the :command:`swupd` software updater utility to add the prerequisite bundles
for the OpenVINO software stack:

.. code-block:: bash

   swupd bundle-add os-clr-on-clr desktop-autostart computer-vision-basic

.. note::

   Learn more about how to :ref:`swupd-guide`.

The :command:`computer-vision-basic` bundle installs the OpenVINO™ toolkit,
and the sample models optimized for Intel® edge platforms.

Convert deep learning models
============================

Locate sample models
--------------------

There are two types of provided models that can be used in conjunction with
AWS Greengrass for this guide: classification or object detection.

To complete this guide using an image classification model,
download the BVLC AlexNet model files `bvlc_alexnet.caffemodel`_ and
`deploy.prototxt`_ to the default model_location at
:file:`/usr/share/openvino/models`. Any custom pre-trained classification models
can be used with the classification sample.

For object detection, the sample models optimized for Intel® edge platforms
are included with the computer-vision-basic bundle installation at
:file:`/usr/share/openvino/models`. These models are provided as an example;
you may also use a custom SSD model with the Greengrass object detection sample.

Run model optimizer
-------------------

Follow the instructions in the `Model Optimizer Developer Guide`_ for converting
deep learning models to Intermediate Representation using Model Optimizer. To
optimize either of the sample models described above, run one of the following commands.

For classification using BVLC AlexNet model:

.. code-block:: bash

   python3 mo.py --framework caffe --input_model
   <model_location>/bvlc_alexnet.caffemodel --input_proto
   <model_location>/deploy.prototxt --data_type <data_type> --output_dir
   <output_dir> --input_shape [1,3,227,227]

For object detection using SqueezeNetSSD-5Class model:

.. code-block:: bash

   python3 mo.py --framework caffe --input_model
   <model_location>/'SqueezeNet 5-Class detection'/SqueezeNetSSD-5Class.caffemodel
   --input_proto <model_location>/'SqueezeNet 5-Class detection'/SqueezeNetSSD-5Class.prototxt
   --data_type <data_type> --output_dir <output_dir>

In these examples:

* `<model_location>` is :file:`/usr/share/openvino/models`.

* `<data_type>` is FP32 or FP16, depending on target device.

* `<output_dir>` is the directory where the Intermediate Representation
  (IR) is stored. IR contains .xml format corresponding to the network
  structure and .bin format corresponding to weights. This .xml file should be
  passed to :command:`<PARAM_MODEL_XML>`.

* In the BVLC AlexNet model, the prototxt defines the input shape with
  batch size 10 by default. In order to use any other batch size, the
  entire input shape must be provided as an argument to the model
  optimizer. For example, to use batch size 1, you must provide:
  `--input_shape [1,3,227,227]`


Configure AWS Greengrass group
******************************

For each Intel® edge platform, you must create a new AWS Greengrass group
and install AWS Greengrass core software to establish the connection between
cloud and edge.

#. To create an AWS Greengrass group, follow the instructions in
   `Configure AWS IoT Greengrass on AWS IoT`_.

#. To install and configure AWS Greengrass core on edge platform, follow
   the instructions in `Start AWS Greengrass on the Core Device`_. In
   step 8(b), download the x86_64 Ubuntu\* configuration of the AWS Greengrass
   core software.

   .. note::

      You do not need to run the :file:`cgroupfs-mount.sh` script in step #6
      of Module 1 of the `AWS Greengrass Developer Guide`_ because this is
      enabled already in |CL|.

#. Be sure to download both the security resources and the AWS Greengrass
   core software.

   .. note::

      Security certificates are linked to your AWS account.


Create and package Lambda function
**********************************

#. Complete steps 1-4 of the AWS Greengrass guide at
   `Create and Package a Lambda Function`_.

   .. note::

      This creates the tarball needed to create the AWS Greengrass
      environment on the edge device.


#. In step 5, replace :file:`greengrassHelloWorld.py` with the classification or
   object detection Greengrass sample from `Edge-Analytics-Faas`_:

   * Classification: `greengrass_classification_sample.py`_

   * Object Detection: `greengrass_object_detection_sample_ssd.py`_

#. Zip the selected Greengrass sample with the extracted Greengrass SDK folders
   from the previous step into :file:`greengrass_sample_python_lambda.zip`.

   The zip should contain:

   * greengrasssdk

   * greengrass classification or object detection sample

   For example:

   .. code-block:: bash

      zip -r greengrass_lambda.zip greengrasssdk
      greengrass_object_detection_sample_ssd.py

#. Return to the AWS documentation section called
   `Create and Package a Lambda Function`_ and complete the procedure.

   .. note::

      In step 9(a) of the AWS documentation, while uploading the zip file,
      make sure to name the handler to one of the following, depending on the
      AWS Greengrass sample you are using:

      * greengrass_object_detection_sample_ssd.function_handler
      * greengrass_classification_sample.function_handler


Configure Lambda function
*************************

After creating the Greengrass group and the Lambda function, start
configuring the Lambda function for AWS Greengrass.

#. Follow steps 1-8 in `Configure the Lambda Function for AWS IoT Greengrass`_
   in the AWS documentation.

#. In addition to the details mentioned in step 8, change the Memory limit
   to 2048 MB to accommodate large input video streams.

#. Add the following environment variables as key-value pairs when editing
   the Lambda configuration and click on update:

   .. list-table:: **Table 1.  Environment variables: Lambda configuration**
      :widths: 20 80
      :header-rows: 1

      * - Key
        - Value
      * - PARAM_MODEL_XML
        - <MODEL_DIR>/<IR.xml>, where <MODEL_DIR> is user specified and
          contains IR.xml, the Intermediate Representation file from Intel® Model Optimizer.
          For this guide, <MODEL_DIR> should be set to '/usr/share/openvino/models'
          or one of its subdirectories.
      * - PARAM_INPUT_SOURCE
        - <DATA_DIR>/input.webm to be specified by user. Holds both input and
           output data. For webcam, set PARAM_INPUT_SOURCE to ‘/dev/video0’
      * - PARAM_DEVICE
        - "CPU"
      * - PARAM_CPU_EXTENSION_PATH
        - /usr/lib64/libcpu_extension.so
      * - PARAM_OUTPUT_DIRECTORY
        - <DATA_DIR> to be specified by user. Holds both input and output
          data
      * - PARAM_NUM_TOP_RESULTS
        - User specified for classification sample.
          (e.g. 1 for top-1 result, 5 for top-5 results)

#. Add subscription to subscribe, or publish messages from AWS Greengrass
   Lambda function by completing the procedure in `Configure the Lambda Function for AWS IoT Greengrass`_.

   .. note::

      The optional topic filter field is the topic mentioned inside the Lambda function. In this guide, sample topics include the following:
      :command:`openvino/ssd` or :command:`openvino/classification`

Add local resources
===================

Refer to the AWS documentation `Access Local Resources with Lambda Functions and Connectors`_
for details about local resources and access privileges.

The following table describes the local resources needed for the CPU:

.. list-table:: **Local resources**
    :widths: 20, 20, 20, 20
    :header-rows: 1

    * - Name
      - Resource type
      - Local path
      - Access

    * - ModelDir
      - Volume
      - <MODEL_DIR> to be specified by user
      - Read-Only

    * - Webcam
      - Device
      - /dev/video0
      - Read-Only

    * - DataDir
      - Volume
      - <DATA_DIR> to be specified by user. Holds both input and output
        data.
      - Read and Write

Deploy Lambda function
**********************

Refer to the AWS documentation `Deploy Cloud Configurations to an AWS IoT Greengrass Core Device`_ for instructions on how to deploy the lambda function to AWS
Greengrass core device. Select *Deployments* on the group page and follow the instructions.

Output consumption
==================

There are four options available for output consumption. These options are
used to report, stream, upload, or store inference output at an interval
defined by the variable :command:`reporting_interval` in the AWS Greengrass samples.

#. IoT cloud output:

   This option is enabled by default in the AWS Greengrass samples using the 
   :command:`enable_iot_cloud_output` variable. You can use it to verify the lambda
   running on the edge device. It enables publishing messages to IoT cloud
   using the subscription topic specified in the lambda. (For example, topics
   may include :command:`openvino/classification` for classification and :command:`openvino/ssd`
   for object detection samples.) For classification, top-1 result with class
   label are published to IoT cloud. For SSD object detection, detection
   results such as bounding box coordinates of objects, class label, and
   class confidence are published.

   Refer to the AWS documentation
   `Verify the Lambda Function Is Running on the Device`_ for instructions on
   how to view the output on IoT cloud.

#. Kinesis streaming:

   This option enables inference output to be streamed from the edge device
   to cloud using Kinesis [3] streams when :command:`enable_kinesis_output` is set
   to True. The edge devices act as data producers and continually push
   processed data to the cloud. You must set up and specify
   Kinesis stream name, Kinesis shard, and AWS region in the AWS Greengrass
   samples.

#. Cloud storage using AWS S3 bucket:

   When the :command:`enable_s3_jpeg_output` variable is set to True, it enables
   uploading and storing processed frames (in jpeg format) in an AWS S3
   bucket. You must set up and specify the S3 bucket name in the AWS
   Greengrass samples to store the JPEG images. The images are named using the
   timestamp and uploaded to S3.

#. Local storage:

   When the :command:`enable_s3_jpeg_output` variable is set to True, it enables
   storing processed frames (in jpeg format) on the edge device. The images
   are named using the timestamp and stored in a directory specified by
   :command:`PARAM_OUTPUT_DIRECTORY`.

References
**********

#. AWS Greengrass: https://aws.amazon.com/greengrass/
#. AWS Lambda: https://aws.amazon.com/lambda/
#. AWS Kinesis: https://aws.amazon.com/kinesis/

.. _Edge-Analytics-FaaS: https://github.com/intel/Edge-Analytics-FaaS/tree/v1.0/AWS%20Greengrass

.. _bvlc_alexnet.caffemodel: http://dl.caffe.berkeleyvision.org/bvlc_alexnet.caffemodel

.. _deploy.prototxt: https://github.com/BVLC/caffe/blob/master/models/bvlc_alexnet/deploy.prototxt

.. _greengrass_classification_sample.py: https://github.com/intel/Edge-Analytics-FaaS/blob/v1.0/AWS%20Greengrass/greengrass_classification_sample.py

.. _greengrass_object_detection_sample_ssd.py: https://github.com/intel/Edge-Analytics-FaaS/blob/v1.0/AWS%20Greengrass/greengrass_object_detection_sample_ssd.py

.. _Model Optimizer Developer Guide: https://software.intel.com/en-us/articles/OpenVINO-ModelOptimizer

.. _AWS Greengrass Developer Guide: https://docs.aws.amazon.com/greengrass/latest/developerguide/what-is-gg.html

.. _Configure AWS IoT Greengrass on AWS IoT: https://docs.aws.amazon.com/greengrass/latest/developerguide/gg-config.html

.. _Start AWS Greengrass on the Core Device: https://docs.aws.amazon.com/greengrass/latest/developerguide/gg-device-start.html

.. _Configure the Lambda Function for AWS IoT Greengrass: https://docs.aws.amazon.com/greengrass/latest/developerguide/config-lambda.html

.. _Access Local Resources with Lambda Functions and Connectors: https://docs.aws.amazon.com/greengrass/latest/developerguide/access-local-resources.html

.. _Deploy Cloud Configurations to an AWS IoT Greengrass Core Device: https://docs.aws.amazon.com/greengrass/latest/developerguide/configs-core.html

.. _Verify the Lambda Function Is Running on the Device: https://docs.aws.amazon.com/greengrass/latest/developerguide/lambda-check.html

.. _Create and Package a Lambda Function: https://docs.aws.amazon.com/greengrass/latest/developerguide/create-lambda.html
