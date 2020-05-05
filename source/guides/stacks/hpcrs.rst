.. _hpcrs:

High Performance Computing Reference Stack
##########################################

This guide gives examples for converting Docker* containers, such as those provided by the :ref:`dlrs` into Singularity* containers suited for HPC, and then walking through a multi-node benchmarking example with TensorFlow*.

.. contents::
   :local:
   :depth: 1


Overview
********

The High Performance Computing Reference Stack (HPCRS) meets the needs of deploying HPC and AI workloads on the same system. This software solution reduces the complexities associated with integrating software components for High Performance Computing (HPC) Platforms.  `Singularity`_ is an open source container platform to package entire scientific workflows, software and libraries, and even data.


Installing Singularity
**********************
The installation instructions are for Linux* systems, and have been enabled for installation on |CL-ATTR|.

.. note::

   The steps for installation can also be found on the `Singularity quick-start`_ https://sylabs.io/guides/3.0/user-guide/quick_start.html#quick-installation

#. Install Go*.

   This guide requires version 1.13 of Go, for compatibility with Singularity v3.0.0. Please use these steps to ensure the correct version of Go is installed:

   .. code-block:: bash

      $ export VERSION=1.13 OS=linux ARCH=amd64 && \
      wget https://dl.google.com/go/go$VERSION.$OS-$ARCH.tar.gz && \
      sudo tar -C /usr/local -xzvf go$VERSION.$OS-$ARCH.tar.gz && \
      rm go$VERSION.$OS-$ARCH.tar.gz

#. Setup the environment for Go.

   .. code-block:: bash

      echo 'export GOPATH=${HOME}/go' >> ~/.bashrc && \
      echo 'export PATH=/usr/local/go/bin:${PATH}:${GOPATH}/bin' >> ~/.bashrc && \
      source ~/.bashrc

#. Install :command:`dep` for dependency resolution with Singularity v3.0.0.

   .. code-block:: bash

      go get -u github.com/golang/dep/cmd/dep

#. Download Singularity.

   .. code-block:: bash

      go get -d github.com/sylabs/singularity


   .. note::

      Go will complain that there are no Go files, but it will still download the Singularity source code to the appropriate directory within the $GOPATH.

#. Checkout version 3.0.0 of Singularity.

   .. code-block:: bash

      export VERSION=v3.0.3 # or another tag or branch if you like && \
      cd $GOPATH/src/github.com/sylabs/singularity && \
      git fetch && \
      git checkout $VERSION # omit this command to install the latest bleeding edge code from master

#. Build Singularity.

   Singularity uses a custom build system called makeit. mconfig is called to generate a Makefile and then make is used to compile and install.
   The devpkg-openssl, devpkg-util-linux  package may be required and can be installed using the :command:`sudo swupd bundle-add <pkg-name>`.

   .. code-block:: bash

      ./mconfig && \
      make -C ./builddir && \
      sudo make -C ./builddir install


#. Configure bash completion (optional).

   To enjoy bash completion with Singularity commands and options, source the bash completion file. Add this command to your ~/.bashrc file so that bash completion continues to work in new shells

   .. code-block:: bash

      . /usr/local/etc/bash_completion.d/singularity


Converting Docker images to Singularity Images
**********************************************

#. Download d2s.

   :command:`d2s` os an open source tool to convert Docker images to
   Singularity images. You can use the script in the location where it is 
   downloaded, or install it using the included :file:`setup.py` file with 
   the :command:`python setup.py install`


   .. code-block:: bash

      git clone https://github.com/intel/stacks.git
      cd stacks/hpcrs/d2s

#. List local Docker images.

   .. code-block:: bash

      python d2s.py --list_docker_images

   Your output can appear like this:

   .. code-block:: console

      ==============================
      Docker images present locally
      ==============================
      ID         NAME
      0: clearlinux/stacks-dlrs-mkl
      1: clearlinux/stacks-dlrs_2-mkl
      ==============================

#. Convert to Singularity images.

   To convert the Docker images to Singularity images, use the :command:`d2s`
   script with the ID numbers of the images you wish to convert.
   We strongly recommend using one of the :file:`clearlinux/stacks-dlrs-mkl` 
   or :file:`sysstacks/stacks-dlrs-mkl` based images for this guide.  Other 
   images may be incompatible with expected configuration or filesystem 
   options.

   .. code-block:: bash

      python d2s.py --convert_docker_images <ID_1> <ID_2>

#. Use the Singularity image.

   To use the container shell to run workloads, launch the image and you
   will be dropped into the shell. The Singularity image name will be the 
   same as the name of the Docker image, with slashes converted to 
   underscores.

   .. code-block:: bash

      singularity shell <singularity image>

   Using the example output above, after conversion you could launch the clearlinux/stacks-dlrs-mkl Singularity image with
   :command:`singularity shell clearlinux_stacks-dlrs-mkl`

Execute a multi-node benchmark on an HPC cluster
************************************************
The following example was executed on an Intel(r) Xeon(r) Processor-based 
HPC infrastructure. The following steps may need to be adjusted for 
different environments. See this `Intel Whitepaper`_ for more information.

Running a ResNet50 workload multi-node
--------------------------------------

#. Download the TensorFlow benchmark.

   .. code-block:: bash

      git clone http://github.com/tensorflow/benchmarks -b cnn_tf_v1.13_compatible

#. Copy the Singularity image and the benchmark files to the HPC cluster 
   environment.

#. Install OpenMPI* if needed.

   .. note::

      If the HPC host does not have OpenMPI installed, install a custom
      local version in the user's home directory. This version must be the 
      same as the version installed in the DLRS container. Follow the steps 
      for `building OpenMPI`_ from their documentation.

#. Adjust PATH variables.

   Include the OpenMPI install locations in the PATH and LD_LIBRARY_PATH 
   environment variables.

   .. code-block:: bash

      export PATH="$PATH:<openmpi install path>/bin"
      export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:<openmpi install path>/lib/"

#. Execute the TF benchmark script on single or multiple nodes using OpenMPI 
   through the :command:`mpirun` command. Replace variables in {} braces to 
   reflect your environment.

   .. code-block:: bash

      mpirun --np ${NUM_COPIES}  \
      -bind-to none \
      -map-by slot \
      --display-map \
      -host ${HOSTNAMES} \
      --report-bindings \
      --oversubscribe \
      -x LD_LIBRARY_PATH \
      -x PATH \
      -x HOROVOD_FUSION_THRESHOLD \
      -x OMP_NUM_THREADS=${OMP_NUM_THREADS} \
      singularity exec ${PATH_TO_SING_IMAGE} \
      python ${PATH_TO_TF_BENCH}/scripts/tf_cnn_benchmarks/tf_cnn_benchmarks.py \
      --batch_size=128 \
      --model=resnet50 \
      --num_intra_threads=${NUM_INTRA_THREADS} \
      --num_inter_threads=${NUM_INTER_THREADS} \
      --data_format=NHWC \
      --device=cpu \
      --variable_update=horovod \
      --horovod_device=cpu

   .. note::

      Refer to the `DLRS script`_ for recommended values for setting environment variables in the :command:`mpirun` command.

   .. note::

      You may see an error regarding a missing library while executing the DLRS container.
      “tensorflow.python.framework.errors_impl.NotFoundError: libnuma.so.1: cannot open shared object file: No such file or directory”

      A workaround for this error is to bind the path to the library from the host.

      .. code-block:: bash

         --bind /usr/lib64/libnuma.so.1:/usr/lib64/libnuma.so.1

.. _Singularity: https://sylabs.io/

.. _Singularity quick-start: https://sylabs.io/guides/3.0/user-guide/quick_start.html#quick-installation

.. _Intel Whitepaper: https://www.intel.com/content/www/us/en/artificial-intelligence/solutions/best-known-methods-for-scaling-deep-learning-with-tensorflow-on-xeon-processor-based-clusters.html

.. _building OpenMPI: https://www.open-mpi.org/faq/?category=building#easy-build

.. _DLRS script: https://github.com/intel/stacks/blob/master/dlrs/clearlinux/tensorflow_2/mkl/scripts/set_env.sh
