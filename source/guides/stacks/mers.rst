.. _mers:

Media Reference Stack
#####################

The Media Reference Stack (MeRS) is a highly optimized software stack for
Intel® architecture to enable media prioritized workloads, such as transcoding and analytics.

This guide explains how to use the pre-built |MERS| container image, build
your own |MERS| container image, and use the reference stack.

.. contents::
   :local:
   :depth: 1

Overview
********

Finding the balance between quality and performance, understanding all of the
complex standard-compliant encoders, and optimizing across the
hardware-software stack for efficiency are all engineering and time
investments for developers.

The Media Reference Stack (MeRS) offers a highly optimized software stack for
Intel Architecture to enable media prioritized workloads, such as transcoding
and analytics. |MERS| abstracts away the complexity of integrating multiple
software components and specifically tunes them for Intel platforms. |MERS|
allows media and visual cloud developers to deliver experiences using a simple
containerized solution. 

Prerequisites
=============

|MERS| can run on any host system that supports Docker\*.

The steps in this guide use |CL-ATTR| as the host system.

- To install |CL| on a host system, see how to 
  :ref:`install Clear Linux* OS from the live desktop
  <bare-metal-install-desktop>`. 

- To install Docker* on a |CL| host system, see
  the :ref:`instructions for installing Docker* <docker>`.

.. important:: 

   For optimal performance, a processor with Vector Neural Network
   Instructions (VNNI) should be used. VNNI is an extension of Intel® 
   Advanced Vector Extensions 512 (Intel® AVX-512) and is available starting 
   with the 2nd generation of Intel® Xeon® Scalable Platform, providing AI 
   inference acceleration.

Stack Features
==============

The |MERS| provides a `pre-built Docker image available on DockerHub
<https://hub.docker.com/r/clearlinux/stacks-mers>`_, which includes
instructions on build the image from source. |MERS| is open-sourced to ensure
developers have easy access to the source code and are able to customize it.
|MERS| is built using the *clearlinux:latest* Docker image and aims to support
the latest |CL| version.

|MERS| provides the following libraries:

.. list-table::
   :widths: auto

   * - SVT-HEVC
     - Scalable Video Technology for HEVC encoding, also known as H.265
   * - SVT-AV1
     - Scalable Video Technology for AV1 encoding
   * - x264
     - x264 for H.264/MPEG-4 AVC encoding
   * - MKL-DNN
     - `Intel® Math Kernel Library for Deep Neural Networks <https://01.org/mkl-dnn>`_

Components of the |MERS| include:

* |CL| as a base for performance and security.

* `Intel® OpenVINO™ toolkit
  <https://01.org/openvinotoolkit>`_ for inference.

* `FFmpeg* <https://www.ffmpeg.org>`_ with `Scalable Video Technology (SVT)
  <https://01.org/svt>`_ plugins for encoding, decoding, and transcoding.

* `GStreamer* <https://gstreamer.freedesktop.org/>`_  with `Scalable Video
  Technology (SVT) <https://01.org/svt>`_ and `Intel® OpenVINO™ toolkit
  <https://01.org/openvinotoolkit>`_ plugins for analytics.

.. note::

   The pre-built |MERS| container image configures :command:`FFmpeg` without
   certain elements (specific encoder, decoder, muxer, etc.) that you may
   require. If you require changes to :command:`FFmpeg` we suggest starting at
   :ref:`building-the-mers-container-image`.

.. note::

   The Media Reference Stack is a collective work, and each piece of software
   within the work has its own license. Please see the `MeRS Terms of Use
   <https://clearlinux.org/stacks/media/terms-of-use>`_ for more details about
   licensing and usage of the Media Reference Stack.


Getting the pre-built |MERS| container image
********************************************

Pre-built |MERS| Docker images are available on DockerHub at
https://hub.docker.com/r/clearlinux/stacks-mers


To use the |MERS|:

#. Pull the image directly from `Docker Hub
   <https://hub.docker.com/r/clearlinux/stacks-mers>`_. 

   .. code-block:: bash

      docker pull clearlinux/stacks-mers

   .. note ::

      The |MERS| docker image is large in size and will take some time to
      download depending on your Internet connection.

      If you are on a network with outbound proxies, be sure to configure
      Docker allow access. See the `Docker service proxy
      <https://docs.docker.com/config/daemon/systemd/#httphttps-proxy>`_ and
      `Docker client proxy
      <https://docs.docker.com/network/proxy/#configure-the-docker-client>`_
      documentation for more details.
      
#. Once you have downloaded the image, run it with:

   .. code-block:: bash

      docker run -it clearlinux/stacks-mers

   This will launch the image and drop you into a bash shell inside the
   container. :command:`GStreamer` and :command:`FFmpeg` programs are
   installed in the container image and accessible in the default $PATH. These
   programs can be used as you would normally outside of |MERS|.

   Paths to media files and video devices, such as cameras, can be shared from
   the host to the container with the :command:`--volume` switch `using Docker
   volumes <https://docs.docker.com/storage/volumes/>`_.

.. _building-the-mers-container-image:

Building the |MERS| container image from source
***********************************************

If you choose to build your own MeRS container image, you can optionally add
customizations as needed. The :file:`Dockerfile` for the MeRS is available on
`GitHub <https://github.com/intel/stacks/tree/master/mers>`_ and
can be used for reference.

#. The |MERS| image is part of the dockerfiles repository inside the |CL|
   organization on GitHub. Clone the :file:`stacks` repository.

   .. code-block:: bash

      git clone https://github.com/intel/stacks.git

#. Navigate to the :file:`stacks/mers/clearlinux` directory which contains 
   the Dockerfile for the |MERS|.
   
   .. code-block:: bash

      cd ./stacks/mers/clearlinux
       
#. Use the :command:`docker build` command with the :file:`Dockerfile` to the
   MeRS container image.

   .. code-block:: bash

      docker build --no-cache -t clearlinux/stacks-mers .

Using the |MERS| container image
********************************

Below are some examples of how the |MERS| container image can be used to
process media files.

The models and video source can be substituted from your use-case. Some
publicly licensed sample videos are available at `sample-videos repsoitory
<https://github.com/intel-iot-devkit/sample-videos>`_ for testing.


Example 1: Transcoding
======================

This example shows how to perform transcoding with :command:`FFmpeg`.

#. On the host system, setup a workspace for data and models:

   .. code:: bash

      mkdir ~/ffmpeg
      mkdir ~/ffmpeg/input
      mkdir ~/ffmpeg/output

#. Copy a video file to :file:`~/ffmpeg/input`. 

   .. code:: bash

      cp </path/to/video> ~/ffmpeg/input

#. Run the *clearlinux/stack-mers* docker image, allowing shared access to the
   workspace on the host:


   .. code:: bash

      docker run -it \
      -v ~/ffmpeg:/home/mers-user:ro \
      clearlinux/stacks-mers:latest

   After running the :command:`docker run` command, you enter a bash shell
   inside the container. 

#. From the container shell, you can run :command:`FFmpeg` against the videos
   in :file:`/home/mers-user/input` as you would normally outside of |MERS|.

   For example, to transcode raw yuv420 content to SVT-HEVC and mp4:

   .. code:: bash

      ffmpeg -f rawvideo -vcodec rawvideo -s 320x240 -r 30 -pix_fmt yuv420p -i </home/mers-user/input/test.yuv> -c:v libsvt_hevc -y </home/mers-user/output/test.mp4>
      
   Some more generic examples of :command:`FFmpeg` commands can be found in
   the `OpenVisualCloud repository
   <https://github.com/OpenVisualCloud/Dockerfiles/blob/master/doc/ffmpeg.md>`_ and used for reference with |MERS|.

   For more information on using :command:`FFmpeg`, refer to the `FFmpeg
   documentation <https://ffmpeg.org/documentation.html>`_.

Example 2: Analytics
====================

This example shows how to perform analytics and inferences with
:command:`GStreamer`.

The steps here are referenced from the `gst-video-analytics Getting Started
Guide <https://github.com/opencv/gst-video-analytics/wiki>`_ except simply
substituting the *gst-video-analytics* docker image for the
*clearlinux/stacks-mers* image.

The example below shows how to use the |MERS| container image to perform video
with object detection and attributes recognition of a video using GStreamer
using pre-trained models and sample video files.

#. On the host system, setup a workspace for data and models:

   .. code:: bash

      mkdir ~/gva
      mkdir ~/gva/data
      mkdir ~/gva/data/models
      mkdir ~/gva/data/models/intel
      mkdir ~/gva/data/models/common
      mkdir ~/gva/data/video

#. Clone the opencv/gst-video-analytics repository into the workspace:

   .. code:: bash

      git clone https://github.com/opencv/gst-video-analytics ~/gva/gst-video-analytics
      cd ~/gva/gst-video-analytics
      git submodule init
      git submodule update

#. Clone the Open Model Zoo repository into the workspace:

   .. code:: bash

      git clone https://github.com/opencv/open_model_zoo.git ~/gva/open_model_zoo
      
#. Use the Model Downloader tool of Open Model Zoo to download ready to use
   pre-trained models in IR format.

   .. note::
      
      If you are on a network with outbound proxies, you will need to
      configure set environment variables with the proxy server. 
      Refer to the documentation on :ref:`proxy` for detailed steps.

      On |CL| systems you will need the *python-extras* bundle. 
      Use :command:`sudo swupd bundle-add python-extras` for the downloader script to work.

   .. code:: bash

      cd ~/gva/open_model_zoo/tools/downloader 
      python3 downloader.py --list ~/gva/gst-video-analytics/samples/model_downloader_configs/intel_models_for_samples.LST -o ~/gva/data/models/intel
  
  
#. Copy a video file in h264 or mp4 format to :file:`~/gva/data/video`. Any
   video with cars, pedestrians, human bodies, and/or human faces can be used.

   .. code:: bash

      git clone https://github.com/intel-iot-devkit/sample-videos.git ~/gva/data/video

   This example simply clones all the video files from the `sample-videos
   repsoitory <https://github.com/intel-iot-devkit/sample-videos>`_.
   
#. From a desktop terminal, allow local access to the X host display. 

   .. code:: bash

      xhost local:root

      export DATA_PATH=~/gva/data
      export GVA_PATH=~/gva/gst-video-analytics
      export MODELS_PATH=~/gva/data/models
      export INTEL_MODELS_PATH=~/gva/data/models/intel
      export VIDEO_EXAMPLES_PATH=~/gva/data/video

#. Run the *clearlinux/stack-mers* docker image, allowing shared access to 
   the X server and workspace on the host:

   .. code:: bash

      docker run -it --runtime=runc --net=host \
      -v ~/.Xauthority:/root/.Xauthority \
      -v /tmp/.X11-unix:/tmp/.X11-unix \
      -e DISPLAY=$DISPLAY \
      -e HTTP_PROXY=$HTTP_PROXY \
      -e HTTPS_PROXY=$HTTPS_PROXY \
      -e http_proxy=$http_proxy \
      -e https_proxy=$https_proxy \
      -v $GVA_PATH:/home/mers-user/gst-video-analytics \      
      -v $INTEL_MODELS_PATH:/home/mers-user/intel_models \
      -v $MODELS_PATH:/home/mers-user/models \
      -v $VIDEO_EXAMPLES_PATH:/home/mers-user/video-examples \
      -e MODELS_PATH=/home/mers-user/intel_models:/home/mers-user/models \      
      -e VIDEO_EXAMPLES_DIR=/home/mers-user/video-examples \
      clearlinux/stacks-mers:latest

   .. note:: 

      In the :command:`docker run` command above:

      - :command:`--runtime=runc` specifies the container runtime to be
        *runc* for this container. It is needed for correct interaction with X
        server.

      - :command:`--net=host` provides host network access to container. It is
        needed for correct interaction with X server.
      
      - Files :file:`~/.Xauthority` and :file:`/tmp/.X11-unix` mapped to the
        container are needed to ensure smooth authentication with X server.
      
      - :command:`-v` instances are needed to map host system directories
        inside Docker container.
      
      - :command:`-e` instances set Docker container environment variables.
        Samples need them some of them set correctly to operate. Proxy variables
        are needed if host is behind firewall.
      

   After running the :command:`docker run` command, it will drop you into a
   bash shell inside the container. 

#. From the container shell, run a sample analytics program in 
   :file:`~/gva/gst-video-analytics/samples` against your video source.

   Below are sample analytics that can be run against the sample videos.
   Choose one to run:

   - Samples with *face detection and classification*:

     .. code:: bash

        ./gst-video-analytics/samples/shell/face_detection_and_classification.sh $VIDEO_EXAMPLES_DIR/face-demographics-walking-and-pause.mp4
        ./gst-video-analytics/samples/shell/face_detection_and_classification.sh $VIDEO_EXAMPLES_DIR/face-demographics-walking.mp4
        ./gst-video-analytics/samples/shell/face_detection_and_classification.sh $VIDEO_EXAMPLES_DIR/head-pose-face-detection-female-and-male.mp4
        ./gst-video-analytics/samples/shell/face_detection_and_classification.sh $VIDEO_EXAMPLES_DIR/head-pose-face-detection-male.mp4
        ./gst-video-analytics/samples/shell/face_detection_and_classification.sh $VIDEO_EXAMPLES_DIR/head-pose-face-detection-female.mp4
      
     When running, a video with object detection and attributes recognition
     (bounding boxes around faces with recognized attributes) should be
     played.
     
     .. figure:: /_figures/stacks/mers-fig-1.png
        :scale: 60%
        :align: center
        :alt: Face detection with the Clear Linux* OS Media Reference Stack

        Figure 1: Screenshot of |MERS| running face detection with GSTreamer
        and OpenVINO.

   - Sample with  *vehicle detection*:

     .. code:: bash

        ./gst-video-analytics/samples/shell/vehicle_detection_2sources_cpu.sh $VIDEO_EXAMPLES_DIR/car-detection.mp4
   
     When running, a video with object detection and attributes recognition
     (bounding boxes around vehicles with recognized attributes) should be
     played.

     .. figure:: /_figures/stacks/mers-fig-2.png
        :scale: 60%
        :align: center
        :alt: Vehicle detection with the Clear Linux* OS Media Reference Stack
        
        Figure 2: Screenshot of |MERS| running vehicle detection with
        GSTreamer and OpenVINO.

   - Sample with *FPS measurement*:

     .. code:: bash

       ./gst-video-analytics/samples/shell/console_measure_fps_cpu.sh $VIDEO_EXAMPLES_DIR/bolt-detection.mp4

