.. _custom-clear-container:

Build a custom |CL-ATTR| based Docker container image
#######################################################

This guide contains the steps to build a custom container image. The official
base |CL-ATTR| container image is published on Docker\* Hub and is updated on a
regular basis.

.. contents::
   :local:
   :depth: 1

Prerequisites
*************

* You must perform these steps on a |CL| system because the
  :abbr:`swupd (software updater)` is used to manage bundles in the
  container.
* You must install the :file:`containers-basic` bundle on the |CL| system
  or Docker will not work.
* You have a basic understanding of Docker.

Build the base container image
******************************

#. Log in and get root privileges.

   .. code-block:: bash

      sudo -s

#. Verify Docker is installed and running.

   .. code-block:: bash

      docker info

   If Docker is installed and running, the output is similar to
   this example:

   .. code-block:: console

      Containers: 0
       Running: 0
       Paused: 0
       Stopped: 0
      Images: 4
      Server Version: 17.05.0-ce
      Storage Driver: overlay
       Backing Filesystem: extfs
       Supports d_type: true
      Logging Driver: json-file
      Cgroup Driver: cgroupfs
      Plugins:
       Volume: local
       Network: bridge host macvlan null overlay
      Swarm: inactive
      Runtimes: runc
      Default Runtime: runc
      Init Binary: docker-init
      containerd version:  (expected: 9048e5e50717ea4497b757314bad98ea3763c145)
      runc version: N/A (expected: 9c2d8d184e5da67c95d601382adf14862e4f2228)
      init version: N/A (expected: )
      Kernel Version: 4.12.7-377.native
      Operating System: Clear Linux OS for Intel Architecture
      OSType: linux
      Architecture: x86_64
      CPUs: 4
      Total Memory: 15.62GiB
      Name: clr-os
      ID: XQHJ:DYEM:3Q4D:DKLM:JOA4:RUSF:GAFR:DLPA:HOJP:W5FF:ULEE:7HZ3
      Docker Root Dir: /var/lib/docker
      Debug Mode (client): false
      Debug Mode (server): false
      Registry: https://index.docker.io/v1/
      Experimental: false
      Insecure Registries:
       127.0.0.0/8
      Live Restore Enabled: false

   If Docker is not installed, enter the commands:

   .. code-block:: bash

      swupd bundle-add containers-basic
      systemctl start docker

#. Use :command:`os-install` to download and install the bundles.

   .. code-block:: bash

      swupd os-install --url https://cdn.download.clearlinux.org/update --statedir "$PWD"/swupd-state --no-boot-update --version 29790 -B os-core-update,editors,network-basic base


   The swupd example uses the following flags:

   * :command:`os-install` tells swupd to download and install.
   * :command:`-V / --version` specifies the version of the |CL| bundles.
   * :command:`--url` specifies the URL of the bundles repository.
   * :command:`--statedir` specifies the state directory where downloaded bundles
     and any state information are stored.
   * :command:`--no-boot-update` tells swupd to skip updating boot files because
     boot files are not required for a container.

   For more information on swupd flags, enter the :command:`swupd os-install -h`
   command.

   Example output:

   .. code-block:: console

      swupd-client software verify 3.12.2
      Copyright (C) 2012-2017 Intel Corporation

      Verifying version 17870
      Attempting to download version string to memory
      Downloading packs...

      Extracting python-basic pack for version 17820
        ...14%
      Extracting perl-basic pack for version 17790
        ...28%
      Extracting openssh-server pack for version 17660
        ...42%
      Extracting editors pack for version 17850
        ...57%
      Extracting network-basic pack for version 17650
        ...71%
      Extracting os-core pack for version 17870
        ...85%
      Extracting os-core-update pack for version 17870
        ...100%
      Adding any missing files
        ...88%
      Inspected 33982 files
        33974 files were missing
          33974 of 33974 missing files were replaced
          0 of 33974 missing files were not replaced
      Calling post-update helper scripts.
      WARNING: boot files update skipped due to --no-boot-update argument
      Fix successful

   .. note::

      The WARNING message is expected and can be ignored.

#. Create a tarball and compress it.

   .. code-block:: bash

      tar -C base -cf base.tar .
      xz -v -T0 base.tar

#. Create the Dockerfile to build the image.

   .. code-block:: bash

      cat > Dockerfile << EOF
      FROM scratch
      MAINTAINER First Last <first.last@example.com>
      ADD base.tar.xz /
      CMD ["/bin/bash"]
      EOF

#. Build the |CL| container image.

   .. code-block:: bash

      docker build -t my-custom-clear-linux-container .

   Example output:

   .. code-block:: console

      Sending build context to Docker daemon  806.5MB
      Step 1/4 : FROM scratch
        --->
      Step 2/4 : MAINTAINER First Last <first.last@example.com>
        ---> Running in 7238f35abcd0
        ---> ec5064287c60
      Removing intermediate container 7238f35abcd0
      Step 3/4 : ADD base.tar.xz /
        ---> 2723b7d20716
      Removing intermediate container 16e3ed0df8da
      Step 4/4 : CMD /bin/bash
        ---> Running in efa893350647
        ---> 5414c3a12993
      Removing intermediate container efa893350647
      Successfully built 5414c3a12993
      Successfully tagged my-custom-clear-linux-container:latest

#. List the newly created |CL| container image.

   .. code-block:: bash

      docker images

   Example output:

   .. code-block:: console

      REPOSITORY                        TAG                 IMAGE ID            CREATED              SIZE
      my-custom-clear-linux-container   latest              5414c3a12993        About a minute ago   616MB

#. Launch the built |CL| container.

   .. code-block:: bash

      docker run -it my-custom-clear-linux-container

Manage bundles in a container
*****************************

You can add and remove bundles from a |CL| container using the
:command:`RUN swupd` command in the Dockerfile.

Add a bundle
============

This example Dockerfile adds the :file:`pxe-server` bundle to an existing |CL|
Docker image:

.. code-block:: bash

   cat > Dockerfile << EOF
   FROM my-customer-clear-linux-container
   MAINTAINER First Last <first.last@example.com>
   RUN swupd bundle-add pxe-server
   CMD ["/bin/bash/bash"]
   EOF

Example output:

.. code-block:: console

   docker build -t my-clearlinux-with-pxe-server-bundle .

   Sending build context to Docker daemon  806.5MB
   Step 1/4 : FROM my-custom-clear-linux-container
    ---> 5414c3a12993
   Step 2/4 : MAINTAINER First Last <first.last@example.com>
    ---> Running in 19b4411cf4bd
    ---> 08d400baffde
   Removing intermediate container 19b4411cf4bd
   Step 3/4 : RUN swupd bundle-add pxe-server
    ---> Running in 3e634d6e0792
   swupd-client bundle adder 3.12.2
      Copyright (C) 2012-2017 Intel Corporation

   Attempting to download version string to memory
   Downloading packs...

   Extracting pxe-server pack for version 17820
   .
   Installing bundle(s) files...
   ..............................................................................
   ..............................................................................
   ..............................................................................
   ..............................................................................
   ..............................................................................
   ..............................................................................
   Calling post-update helper scripts.
   WARNING: systemctl not operable, unable to run systemd update triggers
   Bundle(s) installation done.
    ---> 8ead5f2c0c33
   Removing intermediate container 3e634d6e0792
   Step 4/4 : CMD /bin/bash
    ---> Running in 0ceae320279b
    ---> dcd9adb40611
   Removing intermediate container 0ceae320279b
   Successfully built dcd9adb40611
   Successfully tagged my-clearlinux-with-pxe-server-bundle:latest

.. note::

   The WARNING message can be ignored because systemd does not run inside
   a container.

Remove a bundle
===============

This example Dockerfile removes the :file:`pxe-server` bundle from an existing
|CL| Docker image:

.. code-block:: bash

   cat > Dockerfile << EOF
   FROM my-clearlinux-with-pxe-server-bundle
   MAINTAINER First Last <first.last@example.com>
   RUN swupd bundle-remove pxe-server
   CMD ["/bin/bash/bash"]
   EOF

Example output:

.. code-block:: console

   docker build -t my-clearlinux-remove-pxe-server-bundle .

   Sending build context to Docker daemon  806.5MB
   Step 1/4 : FROM my-clearlinux-with-pxe-server-bundle
    ---> dcd9adb40611
   Step 2/4 : MAINTAINER First Last <first.last@example.com>
    ---> Running in 71b60f15003e
    ---> 742192751c1a
   Removing intermediate container 71b60f15003e
   Step 3/4 : RUN swupd bundle-remove pxe-server
    ---> Running in ad28a3390ecc
   swupd-client bundle remover 3.12.2
      Copyright (C) 2012-2017 Intel Corporation

   Removing bundle: pxe-server
   Deleting bundle files...
   Total deleted files: 92
   Untracking bundle from system...
   Success: Bundle removed
   1 bundle(s) were removed successfully
    ---> d6ee7903e14d
   Removing intermediate container ad28a3390ecc
   Step 4/4 : CMD /bin/bash
    ---> Running in 7694989e97de
    ---> ec23189ef954
   Removing intermediate container 7694989e97de
   Successfully built ec23189ef954
   Successfully tagged my-clearlinux-remove-pxe-server-bundle:latest