.. _nvidia-cuda:

NVIDIA\* CUDA Toolkit 
#####################

NVIDIA is a manufacturer of graphics processing units (GPU), also known as
graphics cards. 

CUDA is a parallel computing platform and application programming interface
model created by NVIDIA. It allows software developers and software engineers
to use a CUDA-enabled graphics processing unit 

These instructions show how to install the CUDA Toolkit on |CL| after the
:ref:`proprietary NVIDIA drivers <nvidia>` have been installed. 

.. note::
  
   Software installed outside of :ref:`swupd <swupd-guide>` is not updated with |CL|
   updates and must be updated and maintained manually.



.. contents:: :local:
    :depth: 2



Prerequisites 
*************

* A |CL| system with a `CUDA-Enabled NVIDIA device <https://developer.nvidia.com/cuda-gpus>`_
* The :ref:`proprietary NVIDIA drivers <nvidia>` have been installed. 




Compatibility
*************

Check compatibility of NVIDIA components 
========================================

To install the appropriate NVIDIA CUDA Toolkit version, it is important to
understand the compute capability and compatible driver versions of your
NVIDIA hardware.

Information about NVIDIA compute capability, driver, and toolkit compatibility
can be found at: https://developer.nvidia.com/cuda-gpus  and
https://docs.nvidia.com/deploy/cuda-compatibility/ 



Check GCC compatibility
=======================

.. note::

   This is only required for the development or compilation of CUDA
   applications. It is not required to run pre-built applications that have a
   dependency on CUDA. 

From the NVIDIA documentation: 

   The CUDA development environment relies on tight integration with the host
   development environment, including the host compiler and C runtime
   libraries, and is therefore only supported on distribution versions that
   have been qualified for this CUDA Toolkit release. 

Refer to the `NVIDIA documentation on CUDA system requirements
<https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#system-requirements>`_
for the latest kernel and compiler compatibility. 

For example, CUDA 10.2 on a system with the latest Linux kernel requires GCC8,
which is older than the default GCC version for |CL|.

Install the compatible version of GCC, if required:

#. Install the :ref:`bundle <bundles>` with the appropriate GCC version.

   .. code:: bash

      sudo swupd bundle-add c-extras-gcc8
      
#. Create the directory :file:`/usr/local/cuda/bin`:

   .. code:: bash

      sudo mkdir -p /usr/local/cuda/bin


#. Add symlinks to the older GCC version in the
   :file:`/usr/local/cuda/bin` directory. This will cause the older version of
   GCC to be used when :file:`/usr/local/cuda/bin` is in the $PATH environment
   variable.

   .. code:: bash
   
      sudo ln -s /usr/bin/gcc-8 /usr/local/cuda/bin/gcc
      sudo ln -s /usr/bin/g++-8 /usr/local/cuda/bin/g++  


Downloading and Installation
****************************


Download the NVIDIA CUDA Toolkit
================================

#. Go to the `NVIDIA CUDA downloads website`_ to get the latest CUDA Toolkit. 
   If an older version of the CUDA Toolkit is required, go to the `CUDA
   Toolkit Archive <https://developer.nvidia.com/cuda-toolkit-archive>`_.

   Choose the following settings and click *Download*. 
   
   - Operating System: *Linux*
   - Architecture: *x86_64*
   - Distribution: *any*
   - Version: *any*
   - Installer Type: *runfile(local)*



#. Open a terminal and navigate to where the
   :file:`cuda_<VERSION>_linux.run` file was saved. In this
   example, it was saved in the Downloads folder.

   .. code-block:: bash

      cd ~/Downloads/

#. Make the :file:`cuda_<VERSION>_linux.run` file executable:

   .. code-block:: bash

      chmod +x cuda_<VERSION>_linux.run



Install the NVIDIA CUDA Toolkit
===============================

The NVIDIA CUDA installer will be directed to install files under
:file:`/opt/cuda` as much as possible to keep its contents isolated from the
rest of the |CL| files under :file:`/usr`. 

The CUDA installer automatically creates a symbolic link that allows the CUDA
Toolkit to be accessed from :file:`/usr/local/cuda` regardless of where it was
installed.


#. Configure the dynamic linker to look for and cache shared libraries under
   :file:`/opt/cuda/lib64` where the NVIDIA installer will place libraries. 

   .. code-block:: bash
      
      sudo mkdir -p /etc/ld.so.conf.d
      echo "include /etc/ld.so.conf.d/*.conf" |  sudo tee --append /etc/ld.so.conf


   The CUDA installer will automatically create a file
   :file:`/etc/ld.so.conf.d/cuda-<VERSION>.conf`

#. Navigate into the directory where the NVIDIA installer was downloaded:

   .. code-block:: bash

      cd ~/Downloads/   


#. Run the installer with the advanced options below:

   .. code-block:: bash
      
      sudo ./cuda_<VERSION>_linux.run \
      --toolkit \
      --installpath=/opt/cuda \
      --no-man-page \
      --override \
      --silent

#. Validate the CUDA Toolkit was installed by checking the NVIDIA CUDA
   compiler version:

   .. code-block:: bash

      /opt/cuda/bin/nvcc --version
      
      
The CUDA Toolkit is now installed and can be used to compile and run CUDA
applications. 
      

Using the NVIDIA CUDA Toolkit
*****************************
      
#. Verify that the NVIDIA device characters files /dev/nvidia* exist and have
   the correct (0666) file permissions. The character devices should be
   automatically created on system with the NVIDIA driver loaded through X
   server, but will not be on systems that do not automatically load the
   NVIDIA driver.

   .. code::
      
      ls -l /dev/nvidia*


#. If your system does not have the NVIDIA character devices created
   automatically, run the `script from NVIDIA documentation
   <https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#runfile-verifications>`_
   with root privileges. 
   
   
   Alternatively a setuid utility, :command:`nvidia-modprobe`, can be compiled
   and installed to automatically create the device character files on-demand.
   
   
   .. code::
   
      wget https://download.nvidia.com/XFree86/nvidia-modprobe/nvidia-modprobe-<VERSION>.tar.bz2
      tar -xvf nvidia-modprobe-<VERSION>.tar.bz2
      cd nvidia-modprobe-<VERSION>/
      make
      sudo make install PREFIX=/usr/local/cuda/
      
      
#. When the CUDA toolkit is needed, export PATH variables pointing to the CUDA
   directories. This will temporarily add CUDA files to the PATH and use the
   specified linked version of GCC for the terminal session.

   .. code:: bash

      export PATH=/usr/local/cuda/bin:$PATH
      export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH
      
   
Source code for CUDA sample located at
:file:`/usr/local/cuda/NVIDIA_CUDA-<VERSION>_Samples`. See the `CUDA
documentation on compiling samples
<https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#compiling-examples>`_
to learn more.


Uninstalling
************

The NVIDIA drivers and associated software can be uninstalled and nouveau
driver restored by: 

#. Run the :command:`sudo /usr/local/cuda/bin/cuda-uninstaller`.

#. Follow the prompts on the screen and reboot the system. 


Debugging
*********

* The NVIDIA CUDA  installer places logs under
  :file:`/tmp/cuda-installer.log`.
  

Additional resources
********************
* `NVIDIA CUDA Toolkit Documentation <https://docs.nvidia.com/cuda/>`_

* `Why aren't the NVIDIA Linux drivers open source? <https://nvidia.custhelp.com/app/answers/detail/a_id/1849/kw/Linux>`_

* `Where can I get support for NVIDIA Linux drivers? <https://nvidia.custhelp.com/app/answers/detail/a_id/44/kw/linux>`_

* `NVIDIA Accelerated Linux Graphics Driver Installation Guides <https://download.nvidia.com/XFree86/Linux-x86_64/>`_

.. _`nouveau project`:  https://nouveau.freedesktop.org/wiki/

.. _`NVIDIA CUDA downloads website`: https://developer.nvidia.com/cuda-downloads


