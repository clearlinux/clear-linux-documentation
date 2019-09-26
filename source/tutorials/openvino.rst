 .. _openvino:

OpenVINO™ for Deep Learning
###########################

This tutorial shows how to install OpenVINO™ on |CL-ATTR|, run an
OpenVINO Sample Application for image classification, and run a benchmark_app
for estimating inference performance---using Squeezenet 1.1.

.. contents::
   :local:
   :depth: 1

Prerequisites
*************

* |CL| installed on the host OS

Install OpenVINO
****************

OpenVINO in |CL| offers pre-built OpenVINO Sample Applications with which
developers can try inferencing immediately.

#. In |CL| OpenVINO is included in the :command:`computer-vision-basic`
   bundle. To install OpenVINO, enter:

   .. code-block:: bash

      sudo swupd bundle-add computer-vision-basic

#. OpenVINO Inference Engine libraries are located in :file:`/usr/lib64/`
   To view one added package, enter:

   .. code-block:: bash

      ls /usr/lib64/libinference_engine.so

   If bundle installation is successful, the output shows:

   .. code-block:: console

      /usr/lib64/libinference_engine.so

#. To view the OpenVINO Model Optimizer, enter:

   .. code-block:: console

      ls /usr/share/openvino/model-optimizer

#. To view the OpenVINO Sample Application Executables, enter:

   .. code-block:: bash

      ls /usr/bin/benchmark_app \
      /usr/bin/classification_sample_async \
      /usr/bin/hello_classification \
      /usr/bin/hello_nv12_input_classification \
      /usr/bin/hello_query_device \
      /usr/bin/hello_reshape_ssd \
      /usr/bin/object_detection_sample_ssd \
      /usr/bin/speech_sample \
      /usr/bin/style_transfer_sample \

   .. note::

      If bundle installation is successful, the above files should appear.

#. To view the pre-built OpenVINO Sample Application source code, enter:

   .. code-block:: bash

      ls /usr/share/doc/inference_engine/samples

In the next section, you learn how to use an OpenVINO Sample Application.

Run OpenVINO Sample Application
*******************************

After installing OpenVINO on |CL|, you need a model against which to test.
In this example, we use the public squeezenet 1.1 model for image
classification. Test results vary based on the system used.

Use model to test
=================

#. If you don’t have any model, you can download an
   **intel_model** or a public model using OpenVINVO Model Downloader.

   - Check the list of public models you can download from
     :file:`/usr/share/open_model_zoo/models/public`

   - Check the list of Intel® models you can download from
     :file:`/usr/share/open_model_zoo/intel_models`

#. View the location of OpenVINO Model Downloader:

   .. code-block:: console

      cd /usr/share/open_model_zoo/tools/downloader

#. In general, download models with the following command:

   .. code-block:: bash

      python3 downloader.py --name <model_name> -o <downloading_path>

   .. note::

      * Where :file:`<model_name>` is the one you chose from previous step

      * Where :file:`<downloading_path>` is your project directory

#. For this example, enter:

   .. code-block:: bash

      python3 downloader.py --name squeezenet1.1 -o $HOME/.

#. After running this command, the model appears as downloading at your
   :file:`$HOME/classification/squeezenet/1.1/caffe` as follows:

   .. code-block:: console

      ###############|| Downloading topologies ||###############

      ========= Downloading /$HOME/classification/squeezenet/1.1/caffe/squeezenet1.1.caffemodel
      ... 100%, 4834 KB, 2839 KB/s, 1 seconds passed

      ...

Convert model to IR format
==========================

#. As necessary, follow the instruction on :ref:`convert-dl-models`
   to convert deep learning models.

#. Navigate to the model:

   .. code-block:: bash

	  cd $HOME/classification/squeezenet/1.1/caffe

#. Enter the command:

   .. code-block:: bash

      python3 /usr/share/openvino/model-optimizer/mo.py --input_model squeezenet1.1.caffemodel


   The output will show these files being generated:

   .. code-block:: console

      squeezenet1.1.xml

      squeezenet1.1.bin

#. Finally, enter :command:`ls` to view the newly added model and files.

Run image classification
========================

This sample application demonstrates how to run the Image Classification in asynchronous mode on supported devices. In this example, we use the image of a specific type of automobile to test the inference engine. Squeezenet 1.1 is designed to perform image classification and has been trained on the `ImageNet`_ database.

#. We provide an image of an automobile, shown in Figure 1. For ease of use,
   save this image into the :file:`classification` model directory.

   .. figure:: ../_figures/openvino/automobile.png
      :height: 375 px
      :width: 500 px
      :scale: 100 %
      :alt: Photo by Goh Rhy Yan on Unsplash

      Figure 1: Photo by Goh Rhy Yan on Unsplash

#. To execute the sample application enter the command:

   .. code-block:: bash

      classification_sample_async -i <path_to_image> -m <path_to_model_ir> -d <device>

   .. note::

      * Where :file:`<path_to_image>` is the image that you selected

      * Where :file:`<path_to_model_ir>` is the path to the IR model file

      * Where :file:`<device>` is your choice of CPU, GPU, etc.

#. In this case, we replace the :file:`<path_to_image>` with the previously
   saved image for CPU inferencing.

   .. code-block:: bash

      classification_sample_async -i ./automobile.png -m squeezenet1.1.xml

   .. note::

      If you do not specify the :file:`device`, the CPU is used by default.

#. The results show the highest probability is 67% for a sports car.

   .. code-block:: bash

      classid probability
      ------- -----------
      817     0.6717085
      511     0.1611409

   +-----------------------+-----------------------------------+
   |:command:`classid` 817 | :command:`sports car, sport car`  |
   +-----------------------+-----------------------------------+
   |:command:`classid` 511 |:command:`convertible`             |
   +-----------------------+-----------------------------------+

   .. note:

      Label definitions are provided by `ImageNet`_.

#. Next, add :command:`-d GPU` to the end of the above command for GPU
   inferencing.

   .. code-block:: bash

      classification_sample_async -i ./automobile.png -m squeezenet1.1.xml -d GPU

Run benchmark_app
*****************

This sample application demonstrates how to use benchmark application to
estimate deep learning inference **performance** on supported devices.
We use the same image of an automobile, Figure 1, from the previous section.

#. To execute this sample application, enter:

   .. code-block:: bash

      benchmark_app -i <path_to_image> -m <path_to_model> -d <device>

   .. note::

      * Where :file:`<path_to_image>` is the image that you selected

      * Where :file:`<path_to_model_ir>` is the path to the IR model file

      * Where :file:`<device>` is local your choice of CPU, GPU, etc.

#. Change directory:

   .. code-block:: bash

      cd $HOME/classification/squeezenet/1.1/caffe

#. Enter the following command for CPU inferencing.

   .. code-block:: bash

      benchmark_app -i ./automobile.png -m squeezenet1.1.xml

#. For the CPU, the results show a :guilabel:`Throughput` of 243.202 FPS.

   .. code-block:: console
      :linenos:
      :emphasize-lines: 4

      Count:      1464 iterations
      Duration:   60196.8 ms
      Latency:    164.104 ms
      Throughput: 243.202 FPS

#. Next, add :command:`-d GPU` to the end of the same command for GPU
   inferencing.

   .. code-block:: bash

      benchmark_app -i ./automobile.png -m squeezenet1.1.xml -d GPU

#. For the GPU, the results show a :guilabel:`Throughput` of 372.677 FPS.

   .. code-block:: console
      :linenos:
      :emphasize-lines: 4

      Count:      2240 iterations
      Duration:   60105.7 ms
      Latency:    107.554 ms
      Throughput: 372.677 FPS

.. _ImageNet: http://image-net.org/
