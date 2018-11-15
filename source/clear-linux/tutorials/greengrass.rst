.. _greengrass:

Enable AWS Greengrass* and OpenVINO™ on |CL-ATTR|
#################################################

Hardware accelerated Function-as-a-Service (FaaS) enables cloud developers
to deploy inference functionalities [1] on Intel® IoT edge devices with
accelerators (CPU, Integrated GPU, Intel® FPGA, and Intel® Movidius™). These
functions provide a great developer experience and seamless migration of
visual analytics from cloud to edge in a secure manner using a containerized
environment. Hardware-accelerated FaaS provides the best-in-class
performance by accessing optimized deep learning libraries on Intel® IoT
edge devices with accelerators.

This tutorial will demonstrate how to:

* Set up the Intel® edge device with |CL-ATTR|
* Install the OpenVINO™ and AWS Greengrass* software stacks
* Use AWS Greengrass and lambdas to deploy the FaaS samples from the cloud

Supported Platforms
*******************

*	Operating System: |CL| latest release
*	Hardware:	Intel® core platforms (Tutorial supports inference on CPU only)

Description of Samples
**********************

The AWS Greengrass samples are located at the `Edge-Analytics-FaaS`_.

We provide the following AWS Greengrass samples:

* `greengrass_classification_sample.py`_

  This AWS Greengrass sample classifies a video stream using classification
  networks such as AlexNet and GoogLeNet and publishes top-10 results on AWS*
  IoT Cloud every second.

* `greengrass_object_detection_sample_ssd.py`_

  This AWS Greengrass sample detects objects in a video stream and
  classifies them using single-shot multi-box detection (SSD) networks such
  as SSD Squeezenet, SSD Mobilenet, and SSD300. This sample publishes
  detection outputs such as class label, class confidence, and bounding box
  coordinates on AWS IoT Cloud every second.


Installing |CL| on the edge device
**********************************

Start with a clean installation of |CL| on a new system, using the
:ref:`bare-metal-install`, found in :ref:`get-started`.

Create user accounts
====================

After |CL| is installed, create two user accounts. Create an administrative
user in |CL|. You will also create a user account for the Greengrass
services to use (see Greengrass user below).

#. Create a new user and set a password for that user. Enter the following
   commands as ``root``:

   .. code-block:: bash

      useradd <userid>
      passwd <userid>

#. Next, enable the :command:`sudo` command for your new ``<userid>``. Add
   ``<userid>`` to the ``wheel`` group:

   .. code-block:: bash

      usermod -G wheel -a <userid>

#. Create a :file:`/etc/fstab` file.

   .. code-block:: bash

      touch /etc/fstab

   .. note::

      By default |CL| does not create an :file:`/etc/fstab` file.
      The Greengrass service needs to have the file created before
      it will run.

Add required bundles
====================

Use the ``swupd`` software updater utility to add the prerequisite bundles
for the OpenVINO software stack:

.. code-block:: bash

   swupd bundle-add os-clr-on-clr desktop-autostart computer-vision-basic

.. note::

   Learn more about how to :ref:`swupd-guide`.

The ``computer-vision-basic`` bundle will install the OpenVINO software,
along with the edge device models needed.

Converting Deep Learning Models
===============================

Locate Sample Models
--------------------

There are two types of provided models that can be used in conjunction with AWS Greengrass 
for this tutorial: classification or object detection.

To complete this tutorial using an image classification model,
download the BVLC Alexnet model files `bvlc_alexnet.caffemodel`_ and `deploy.prototxt`_
to the default model_location at :file:`/usr/share/openvino/models`.
Any custom pre-trained classification models can be used with the
classification sample.

For object detection, the sample models optimized for Intel® edge platforms
are included with the computer-vision-basic bundle installation at :file:`/usr/share/openvino/models`. 
These models are provided as an example; however, you may also use a custom SSD model 
with the Greengrass object detection sample.

Running Model Optimizer
-----------------------

Follow these instructions for `converting deep learning models to Intermediate Representation using Model Optimizer`_. To optimize either of the afformentioned sample models, run one of the following commands.

For classification using BVLC Alexnet model:

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

* ``<model_location>`` is :file:`/usr/share/openvino/models`

* ``<data_type>`` is FP32 or FP16, depending on target device.

* ``<output_dir>`` is the directory where the user wants to store the
  Intermediate Representation (IR). IR contains .xml format corresponding
  to the network structure and .bin format corresponding to weights. This
  .xml file should be passed to <PARAM_MODEL_XML>.

* In the BVLC Alexnet model, the prototxt defines the input shape with
  batch size 10 by default. In order to use any other batch size, the
  entire input shape needs to be provided as an argument to the model
  optimizer. For example, to use batch size 1, you can provide
  “--input_shape [1,3,227,227]”.


Configuring an AWS Greengrass group
===================================

For each Intel® edge platform, we need to create a new AWS Greengrass group
and install AWS Greengrass core software to establish the connection between
cloud and edge.

#. To create an AWS Greengrass group, follow the
   `AWS Greengrass developer guide`_

#. To install and configure AWS Greengrass core on edge platform, follow
   the instructions at `Start AWS Greengrass on the Core Device`_. In 
   step 8(b), download the x86_64 Ubuntu configuration of the AWS Greengrass
   core software.

   .. note::

      You will not need to run the ``cgroupfs-mount.sh`` script in step #6
      of Module 1 of the `AWS Greengrass developer guide`_ because this is
      enabled already in |CL|.

#. Be sure to download both the security resources and the AWS Greengrass
   core software.

   .. note::

      Security certificates are linked to your AWS* account.


Creating and Packaging Lambda Functions
=======================================

#. Complete steps 1-4 of the tutorial at `Create and Package Lambda Function`_ . 

   .. note::

      This creates the tarball needed to create the AWS Greengrass
      environment on the edge device.


#. In step 5, replace greengrassHelloWorld.py with the classification or object detection 
   Greengrass sample from `Edge-Analytics`Faas`_:

   * Classification: `greengrass_classification_sample.py`_

   * Object Detection: `greengrass_object_detection_sample_ssd.py`_

#. Zip the selected Greengrass sample with the extracted Greengrass SDK folders from the previous
   step into :file:`greengrass_sample_python_lambda.zip`.

   The zip should contain:

   * greengrasssdk

   * greengrass classification or object detection sample

   For example:

   .. code-block:: bash

      zip -r greengrass_lambda.zip greengrasssdk
      greengrass_object_detection_sample_ssd.py

#. Return to the AWS Documentation and follow steps 6-11 to `complete creating lambdas`_.

   .. note::

      In step 9(a) of the AWS documentation, while uploading the zip file,
      make sure to name the handler as below depending on the AWS Greengrass
      sample you are using:

      * greengrass_object_detection_sample_ssd.function_handler (or)
      * greengrass_classification_sample.function_handler

Deploying Lambdas
=================

Configuring the Lambda function
-------------------------------

After creating the Greengrass group and the lambda function, start
configuring the lambda function for AWS Greengrass.

#. Follow steps 1-8 in `Configure the Lambda Function`_ of the AWS
   documentation.

#. In addition to the details mentioned in step 8, change the Memory limit
   to 2048MB to accommodate large input video streams.

#. Add the following environment variables as key-value pairs when editing
   the lambda configuration and click on update:

   .. list-table:: **Table 1.  Environment Variables: Lambda Configuration**
      :widths: 20 80
      :header-rows: 1

      * - Key
        - Value
      * - PARAM_MODEL_XML
        - <MODEL_DIR>/<IR.xml>, where <MODEL_DIR> is user specified and
          contains IR.xml, the Intermediate Representation file from Intel® Model Optimizer. 
          For this tutorial, <MODEL_DIR> should be set to '/usr/share/openvino/models' 
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
   lambda function by following the steps 10-14 in `Configure the Lambda Function`_

   .. note::

      The “Optional topic filter” field should be the topic
      mentioned inside the lambda function.

      For example, openvino/ssd or openvino/classification

Local Resources
---------------
#. Select `this link to add local resources and access privileges`_.

   Following are the local resources needed for the CPU:

   .. list-table:: **Local Resources**
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

Deploy
------

To `deploy the lambda function to AWS Greengrass core device`_, select
“Deployments” on group page and follow the instructions.

Output Consumption
------------------

There are four options available for output consumption. These options are
used to report, stream, upload, or store inference output at an interval
defined by the variable ``reporting_interval`` in the AWS Greengrass samples.

a. IoT Cloud Output:
   This option is enabled by default in the AWS Greengrass samples using a
   variable ``enable_iot_cloud_output``.  We can use it to verify the lambda
   running on the edge device. It enables publishing messages to IoT cloud
   using the subscription topic specified in the lambda (For example,
   ‘openvino/classification’ for classification and ‘openvino/ssd’ for
   object detection samples).  For classification, top-1 result with class
   label are published to IoT cloud. For SSD object detection, detection
   results such as bounding box co-ordinates of objects, class label, and
   class confidence are published.

   Follow the instructions here to `view the output on IoT cloud`_

b. Kinesis Streaming:

   This option enables inference output to be streamed from the edge device
   to cloud using Kinesis [3] streams when ‘enable_kinesis_output’ is set
   to True. The edge devices act as data producers and continually push
   processed data to the cloud. The users need to set up and specify
   Kinesis stream name, Kinesis shard, and AWS region in the AWS Greengrass
   samples.

c. Cloud Storage using AWS S3 Bucket:

   When the ‘enable_s3_jpeg_output’ variable is set to True, it enables uploading and storing processed frames (in JPEG format) in an AWS S3 bucket. The users need to set up and specify the S3 bucket name in the
   AWS Greengrass samples to store the JPEG images. The images are named using the timestamp and uploaded to S3.

d. Local Storage:

   When the ‘enable_s3_jpeg_output’ variable is set to True, it enables storing processed frames (in JPEG format) on the edge device. The
   images are named using the timestamp and stored in a directory specified
   by ‘PARAM_OUTPUT_DIRECTORY’.

References
-----------

1. AWS Greengrass: https://aws.amazon.com/greengrass/
2. AWS Lambda: https://aws.amazon.com/lambda/
3. AWS Kinesis: https://aws.amazon.com/kinesis/

.. _Edge-Analytics-FaaS: https://github.com/intel/Edge-Analytics-FaaS/tree/master/AWS%20Greengrass

.. _bvlc_alexnet.caffemodel: http://dl.caffe.berkeleyvision.org/bvlc_alexnet.caffemodel

.. _deploy.prototxt: https://github.com/BVLC/caffe/blob/master/models/bvlc_alexnet/deploy.prototxt

.. _greengrass_classification_sample.py: https://github.com/intel/Edge-Analytics-FaaS/blob/master/AWS%20Greengrass/greengrass_classification_sample.py

.. _greengrass_object_detection_sample_ssd.py: https://github.com/intel/Edge-Analytics-FaaS/blob/master/AWS%20Greengrass/greengrass_object_detection_sample_ssd.py

.. _converting deep learning models to Intermediate Representation using Model Optimizer: https://software.intel.com/en-us/articles/OpenVINO-ModelOptimizer

.. _AWS Greengrass developer guide: https://docs.aws.amazon.com/greengrass/latest/developerguide/gg-config.html

.. _Start AWS Greengrass on the Core Device: https://docs.aws.amazon.com/greengrass/latest/developerguide/gg-device-start.html

.. _AWS Greengrass Core SDK: https://docs.aws.amazon.com/greengrass/latest/developerguide/create-lambda.html

.. _complete creating lambdas: https://docs.aws.amazon.com/greengrass/latest/developerguide/create-lambda.html

.. _Configure the Lambda Function: https://docs.aws.amazon.com/greengrass/latest/developerguide/config-lambda.html

.. _Add local resources and access privileges: https://docs.aws.amazon.com/greengrass/latest/developerguide/access-local-resources.html

.. _deploy the lambda function to AWS Greengrass core device: https://docs.aws.amazon.com/greengrass/latest/developerguide/configs-core.html

.. _Edge-optmized models repository: https://github.com/intel/Edge-optimized-models

.. _view the output on IoT cloud: https://docs.aws.amazon.com/greengrass/latest/developerguide/lambda-check.html

.. _this link to add local resources and access privileges: https://docs.aws.amazon.com/greengrass/latest/developerguide/access-local-resources.html

.. _Create and Package Lambda Function: https://docs.aws.amazon.com/greengrass/latest/developerguide/create-lambda.html
