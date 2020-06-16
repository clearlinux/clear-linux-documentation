.. _mers:

Media Reference Stack
#####################

The Media Reference Stack (MeRS) is a highly optimized software stack for
Intel® Architecture Processors (the CPU) and Intel® Processor Graphics (the
GPU) to enable media prioritized workloads, such as transcoding and analytics.

This guide explains how to use the pre-built |MERS| container image, build
your own |MERS| container image, and use the reference stack.

.. contents::
   :local:
   :depth: 1

Overview
********

Developers face challenges due to the complexity of software integration for
media tasks that require investing time and engineering effort.
For example:

   * Finding the balance between quality and performance.
   * Understanding available standard-compliant encoders.
   * Optimizing across the hardware-software stack for efficiency.

|MERS| abstracts away the complexity of integrating multiple software
components and specifically tunes them for Intel platforms. |MERS| enables
media and visual cloud developers to deliver experiences using a simple
containerized solution.


Releases
********

Refer to the `System Stacks for Linux* OS repository
<https://github.com/intel/stacks>`_ for information and download links for the
different versions and offerings of the stack.

* MeRS V0.2.0 release announcement including media processing on GPU and
  analytics on CPU. 

* MeRS V0.1.0 including media processing and analytics CPU.

* `MeRS Release notes on Github*
  <https://github.com/intel/stacks/blob/master/mers/NEWS.md>`_ for the
  latest release of Deep Learning Reference Stack


Prerequisites
=============

|MERS| can run on any host system that supports Docker\*. This guide uses
|CL-ATTR| as the host system.

- To install |CL| on a host system, see how to 
  :ref:`install Clear Linux* OS from the live desktop
  <bare-metal-install-desktop>`. 

- To install Docker* on a |CL| host system, see
  the :ref:`instructions for installing Docker* <docker>`.

.. important:: 

   For optimal media analytics performance, a processor with Vector Neural
   Network Instructions (VNNI) should be used. VNNI is an extension of Intel®
   Advanced Vector Extensions 512 (Intel® AVX-512) and is available starting
   with the 2nd generation of Intel® Xeon® Scalable processors, providing AI
   inference acceleration.

Stack features
==============

The |MERS| provides a `pre-built Docker image available on DockerHub
<https://hub.docker.com/r/sysstacks/mers-clearlinux>`_, which includes
instructions on building the image from source. |MERS| is open-sourced to
make sure developers have easy access to the source code and are able to
customize it. |MERS| is built using the latest *clearlinux/os-core* Docker
image and aims to support the latest |CL| version.

|MERS| provides the following libraries and drivers:

.. list-table::
   :widths: 15 85

   * - SVT-HEVC
     - Scalable Video Technology for HEVC encoding, also known as H.265
   * - SVT-AV1
     - Scalable Video Technology for AV1 encoding
   * - x264
     - x264 for H.264/MPEG-4 AVC encoding
   * - dav1d
     - `dav1d <https://code.videolan.org/videolan/dav1d>`_ for AV1 decoding
   * - libVA
     - `VAAPI (Video Acceleration API) open-source library (LibVA),
       <https://github.com/intel/libva>`_ which provides access to graphics
       hardware acceleration capabilities.
   * - media-driver
     - `Intel® Media Driver for VAAPI <https://github.com/intel/media-driver/>`_
       for supporting hardware acceleration on Intel® Gen graphics hardware
       platforms.
   * - gmmlib
     - `Intel® Graphics Memory Management Library
       <https://github.com/intel/gmmlib>`_ provides device specific and buffer
       management for the Intel® Graphics Compute Runtime for oneAPI Level Zero 
       and OpenCL™ Driver and the Intel Media Driver for VAAPI.

Components of the |MERS| include:

* |CL| as a base for performance and security.

* `OpenVINO™ toolkit
  <https://01.org/openvinotoolkit>`_ for inference.

* `FFmpeg* <https://www.ffmpeg.org>`_ with plugins for:

   - `Scalable Video Technology (SVT)
     <https://01.org/svt>`_

* `GStreamer* <https://gstreamer.freedesktop.org/>`_  with plugins for:

   - `Scalable Video
     Technology (SVT) <https://01.org/svt>`_
   - `OpenVINO™ toolkit
     <https://01.org/openvinotoolkit>`_
   - `VAAPI <https://github.com/GStreamer/gstreamer-vaapi>`_

* `Intel® Media SDK <https://github.com/Intel-Media-SDK/MediaSDK>`_ 

.. note::

   The |MERS| is validated on 11th generation Intel Processor Graphics and
   newer. Older generations should work but are not tested against.

.. note::

   The pre-built |MERS| container image configures FFmpeg without certain
   elements (specific encoder, decoder, muxer, etc.) that you may require. If
   you require changes to FFmpeg we suggest starting at
   :ref:`building-the-mers-container-image`.

.. note::

   The Media Reference Stack is a collective work, and each piece of software
   within the work has its own license. Please see the `MeRS Terms of Use
   <https://clearlinux.org/stacks/media/terms-of-use>`_ for more details about
   licensing and usage of the Media Reference Stack.


Get the pre-built |MERS| container image
****************************************

Pre-built |MERS| Docker images are available on DockerHub* at
https://hub.docker.com/r/sysstacks/mers-clearlinux


To use the |MERS|:

#. Pull the image directly from `Docker Hub
   <https://hub.docker.com/r/sysstacks/mers-clearlinux>`_. 

   .. code-block:: bash

      docker pull sysstacks/mers-clearlinux

   .. note ::

      The |MERS| docker image is large in size and will take some time to
      download depending on your Internet connection.

      If you are on a network with outbound proxies, be sure to configure
      Docker to allow access. See the `Docker service proxy
      <https://docs.docker.com/config/daemon/systemd/#httphttps-proxy>`_ and
      `Docker client proxy
      <https://docs.docker.com/network/proxy/#configure-the-docker-client>`_
      documentation for more details.
      
#. Once you have downloaded the image, run it using the following command:

   .. code-block:: bash

      docker run -it sysstacks/mers-clearlinux

   This will launch the image and drop you into a bash shell inside the
   container. GStreamer and FFmpeg programs are installed in the container
   image and accessible in the default $PATH. Use these programs as you would
   outside of |MERS|.

   Paths to media files and video devices, such as cameras, can be shared from
   the host to the container with the :command:`--volume` switch `using Docker
   volumes <https://docs.docker.com/storage/volumes/>`_.

.. _building-the-mers-container-image:

Build the |MERS| container image from source
********************************************

If you choose to build your own MeRS container image, you can optionally add
customizations as needed. The :file:`Dockerfile` for the MeRS is available on
`GitHub <https://github.com/intel/stacks/tree/master/mers>`_ and can be used
as a reference when creating your own container image.

#. The |MERS| image is part of the dockerfiles repository inside the |CL|
   organization on GitHub. Clone the :file:`stacks` repository.

   .. code-block:: bash

      git clone https://github.com/intel/stacks.git

#. Navigate to the :file:`stacks/mers/clearlinux` directory which contains 
   the Dockerfile for the |MERS|.
   
   .. code-block:: bash

      cd ./stacks/mers/clearlinux
       
#. Use the :command:`docker build` command with the :file:`Dockerfile` to
   build the MeRS container image.

   .. code-block:: bash

      docker build --no-cache -t sysstacks/mers-clearlinux .

Use the |MERS| container image
******************************

This section shows examples of how the |MERS| container image can be used to
process media files.

The models and video source can be substituted from your use-case. Some
publicly licensed sample videos are available at `sample-videos repository
<https://github.com/intel-iot-devkit/sample-videos>`_ for testing.


Media Transcoding
=================

The examples below show transcoding using the GPU or CPU for processing.

#. On the host system, setup a workspace for data and models:

   .. code:: bash

      mkdir ~/ffmpeg
      mkdir ~/ffmpeg/input
      mkdir ~/ffmpeg/output

#. Copy a video file to :file:`~/ffmpeg/input`. 

   .. code:: bash

      cp </path/to/video> ~/ffmpeg/input

#. Run the *sysstacks/mers-clearlinux* Docker image, allowing shared access to
   the workspace on the host:

   .. code:: bash

      docker run -it \
      --volume ~/ffmpeg:/home/mers-user:ro \
      --device=/dev/dri \
      --env QSV_DEVICE=/dev/dri/renderD128 \
      sysstacks/mers-clearlinux:latest

   .. note::

      The :command:`--device` parameter and the **GSV_DEVICE** environment
      variable allow shared access to the GPU on the host system. The values
      needed may be different depending on host's graphics configuration.      

   After running the :command:`docker run` command, you enter a bash shell
   inside the container. 

#. From the container shell, you can run FFmpeg and
   GStreamer commands against the videos in :file:`/home/mers-user/input` as
   you would normally outside of |MERS|.

   Some sample commands are provided for reference. 

   For more information on using the *FFmpeg* commands, refer to the `FFmpeg
   documentation <https://ffmpeg.org/documentation.html>`_.

   For more information on using the *GStreamer* commands, refer to the
   `GStreamer documentation
   <https://gstreamer.freedesktop.org/documentation>`_.


Example: Transcoding using GPU
-------------------------------

The examples below show transcoding using the GPU for processing.


Using a FFmpeg to transcode raw content to SVT-HEVC and mp4:

.. code:: bash

   ffmpeg -y -vaapi_device /dev/dri/renderD128 -f rawvideo -video_size 320x240 -r 30 -i </home/mers-user/input/test.yuv> -vf 'format=nv12, hwupload' -c:v h264_vaapi -y </home/mers-user/output/test.mp4>

Using a GStreamer to transcode H264 to H265:

.. code:: bash

   gst-launch-1.0 filesrc location=</home/mers-user/input/test.264> ! h264parse ! vaapih264dec ! vaapih265enc rate-control=cbr bitrate=5000 ! video/x-h265,profile=main ! h265parse ! filesink location=</home/mers-user/output/test.265>

|MERS| builds FFmpeg with `HWAccel
<https://trac.ffmpeg.org/wiki/HWAccelIntro>`_ enabled which supports VAAPI.
Refer to the `FFmpeg wiki on VAAPI
<https://trac.ffmpeg.org/wiki/Hardware/VAAPI>`_ and `GStreamer with Media-SDK
wiki
<https://github.com/Intel-Media-SDK/MediaSDK/wiki/Build-and-use-GStreamer-with-MediaSDK#usage-examples>`_
for more usage examples and compatibility information.


Example: Transcoding using CPU
------------------------------

The example below shows transcoding of raw yuv420 content to SVT-HEVC and mp4,
using the CPU for processing.

.. code:: bash

   ffmpeg -f rawvideo -vcodec rawvideo -s 320x240 -r 30 -pix_fmt yuv420p -i </home/mers-user/input/test.yuv> -c:v libsvt_hevc -y </home/mers-user/output/test.mp4>

Additional generic examples of FFmpeg commands can be found in the
`OpenVisualCloud repository
<https://github.com/OpenVisualCloud/Dockerfiles/blob/master/doc/ffmpeg.md>`_
and used for reference with |MERS|.


Media Analytics
===============

This example shows how to perform analytics and inferences with GStreamer
using the CPU for processing.

The steps here are referenced from the `gst-video-analytics Getting Started
Guide <https://github.com/opencv/gst-video-analytics/wiki>`_ except simply
substituting the *gst-video-analytics* docker image for the
*sysstacks/mers-clearlinux* image.

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

#. Run the *sysstacks/mers-clearlinux* docker image, allowing shared access 
   to the X server and workspace on the host:

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
      sysstacks/mers-clearlinux:latest

   .. note:: 

      In the :command:`docker run` command above:

      - :command:`--runtime=runc` specifies the container runtime to be
        *runc* for this container. It is needed for correct interaction with X
        server.

      - :command:`--net=host` provides host network access to the container.
        It is needed for correct interaction with X server.
      
      - Files :file:`~/.Xauthority` and :file:`/tmp/.X11-unix` mapped to the
        container are needed to ensure smooth authentication with X server.
      
      - :command:`-v` instances are needed to map host system directories
        inside the Docker container.
      
      - :command:`-e` instances set the Docker container environment
        variables. Some examples need these variables set correctly in order
        to operate correctly. Proxy variables are needed if host is behind a
        firewall.
      

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


Add AOM support
***************

The current version of |MERS| does not include the `Alliance for Open Media
<https://aomedia.org/>`_ Video Codec (AOM). AOM can be built from source on an
individual basis.

To add AOM support to the |MERS| image:


#. The following programs are needed to add AOM support to |MERS|: **docker,
   git, patch**. On |CL| these can be  installed with the commands below. For
   other operating systems, install the appropriate packages. 

   .. code:: bash

      sudo swupd bundle-add containers-basic dev-utils


#. Clone the Intel Stacks repository from GitHub.

   .. code:: bash

      git clone https://github.com/intel/stacks.git 

#. Navigate to the directory for the |MERS| image.

   .. code:: bash 

      cd stacks/mers/clearlinux/

#. Apply the patch to the :file:`Dockerfile`.

   .. code:: bash

      patch -p1 < aom-patches/stacks-mers-v2-include-aom.diff

#. Use the :command:`docker build` command to build a local copy of the
   MeRS container image tagged as *aom*.

   .. code-block:: bash

      docker build --no-cache -t sysstacks/mers-clearlinux:aom .

Once the build has completed successfully, the local image can be used
following the same steps in this tutorial by substituting the image name with
*sysstacks/mers-clearlinux:aom*.


*Intel, Xeon, OpenVINO, and the Intel logo are trademarks of Intel
Corporation or its subsidiaries. OpenCL and the OpenCL logo are trademarks of
Apple Inc. used by permission by Khronos.*
