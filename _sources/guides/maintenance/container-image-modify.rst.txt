.. _container-image-modify:

Modify a |CL|-based container image
###################################

This guide describes how to customize |CL-ATTR|-based container
`images on Docker Hub`_, which include popular applications and runtimes.

.. contents::
   :local:
   :depth: 1

Overview
********

Most of these images utilize a Docker build feature called a `multi-stage
build to reduce image size`_ while some use single-stage build Dockerfiles. An
official base `clearlinux image on Docker Hub`_ is also available. To create a
generic |CL| container image, see :ref:`our guide <container-image-new>`.

Prerequisites
*************

* Set up a functional Docker environment as described in :ref:`docker`.

* Download the |CL| microservice Dockerfile repo with the following
  command:

  .. code-block:: bash

     git clone https://github.com/clearlinux/dockerfiles.git

* Navigate to and operate from the cloned :file:`dockerfiles` directory.

   .. code-block:: bash   

      cd dockerfiles/


Example 1: Add a bundle
***********************

In this example, we add :command:`wget` to the **clearlinux/redis**
Dockerfile.

#. Enter :command:`swupd search wget` to discover which |CL| bundle includes
   the software. The output should tell you that :command:`wget` is available
   in the *wget* bundle.

#. Open a an editor to modify the Dockerfile.

   .. code-block:: bash   

      $EDITOR redis/Dockerfile

#. Append the :command:`wget` bundle to the :command:`--bundles=` parameter
   of the :command:`swupd os-install` command.

#. Run :command:`git diff`.

   The output shows the edits made after adding :command:`wget` in the
   clearlinux/redis Dockerfile.

   .. code-block:: diff

      diff --git a/redis/Dockerfile b/redis/Dockerfile
      index af977cb..b1effab 100644
      --- a/redis/Dockerfile
      +++ b/redis/Dockerfile
      @@ -15,7 +15,7 @@ RUN source /os-release && \
          mkdir /install_root \
          && swupd os-install -V ${VERSION_ID} \
          --path /install_root --statedir /swupd-state \
       -    --bundles=redis-native,findutils,su-exec --no-boot-update
       +    --bundles=redis-native,findutils,su-exec,wget --no-boot-update

#. Build the Dockerfile and apply a unique tag name. In this this example,
   we use :command:`wget_added` and add proxies.

   .. code-block:: bash

      docker build \
      --no-cache \
      --build-arg http_proxy=$http_proxy \
      --build-arg https_proxy=$https_proxy \
      --tag clearlinux/redis:wget_added \
      redis/

#. Run the Dockerfile with the `wget --version` command to verify that
   :command:`wget` has been added to the image.

   .. code-block:: bash

      docker run clearlinux/redis:wget_added wget --version

#. The output shows:

   .. code-block:: console

      GNU Wget 1.20.3 built on linux-gnu.

      -cares +digest -gpgme +https +ipv6 -iri +large-file -metalink +nls
      -ntlm +opie -psl +ssl/openssl

Example 2: Change |CL| version (single-stage build)
***************************************************

This example shows how to rebuild single-stage containers against a specific
OS version, :file:`<CL_VERSION>`, by adding a new argument to the Docker build
command line. 

#. Rebuild the :file:`clearlinux/machine-learning-ui`. Add an extra build
   argument :command:`swupd_args="-m <CL_VERSION>"`; in this case, the build
   version is 31110.

   .. code-block:: bash
      :linenos:
      :emphasize-lines: 5

      docker build \
      --no-cache \
      --build-arg http_proxy=$http_proxy \
      --build-arg https_proxy=$https_proxy \
      --build-arg swupd_args="-m 31110" \      
      --tag clearlinux/machine-learning-ui:31110 \
      machine-learning-ui/

#. Run the docker container image:

   .. code-block:: bash

      docker run clearlinux/machine-learning-ui:31110 swupd info

#. Sample output shows:

   .. code-block:: console

      Distribution:      Clear Linux OS
      Installed version: 31110
      Version URL:       https://cdn.download.clearlinux.org/update
      Content URL:       https://cdn.download.clearlinux.org/update


Example 3: Change |CL| version (multi-stage build)
**************************************************

This example shows how to rebuild the cgit Dockerfile to use a specific |CL|
version. The clearlinux/cgit Dockerfile has a multi-stage build with multiple
layers: *os-core*, *httpd*, and *cgit*. This can be used as reference for
building other multi-stage images with any number of layers. 


.. important::

   All upper layers of multi-stage Dockerfiles inherit the |CL| version from
   the base layer. Rebuild the all underlying base layers against the desired
   OS version. In this example, four base layers must be rebuilt.


First layer: os-core
--------------------

#. Rebuild the first layer, *os-core*. Add an extra build argument
   :command:`swupd_args="-m <CL_VERSION>"`; in this case, the build
   version is 31110.

   .. code-block:: bash
      :linenos:
      :emphasize-lines: 5

      docker build \
      --no-cache \
      --build-arg http_proxy=$http_proxy \
      --build-arg https_proxy=$https_proxy \
      --build-arg swupd_args="-m 31110" \      
      --tag clearlinux/os-core:31110 \
      os-core/

#. Verify the version-specific image is available:

   .. code-block:: bash
      
       docker images clearlinux/os-core:31110


Second layer: httpd
-------------------

The next layer is :file:`clearlinux/httpd`.

#. Change the :file:`httpd/Dockerfile` to use the version-specific
   *os-core:31110* image that was previously built.

   .. code-block:: bash

      $EDITOR httpd/Dockerfile

#. Run :command:`git diff`.

   The output shows a diff of a modified :file:`clearlinux/httpd` Dockerfile
   that uses the previously built clearlinux/os-core:31110.

   .. code-block:: diff

      diff --git a/httpd/Dockerfile b/httpd/Dockerfile
      index 6b2a6bf..9df89e4 100644
      --- a/httpd/Dockerfile
      +++ b/httpd/Dockerfile
      @@ -7,7 +7,7 @@ RUN swupd update --no-boot-update $swupd_args

      # Grab os-release info from the minimal base image so
      # that the new content matches the exact OS version
      -COPY --from=clearlinux/os-core:latest /usr/lib/os-release /
      +COPY --from=clearlinux/os-core:31110 /usr/lib/os-release /

      # Install additional content in a target directory
      # using the os version from the minimal base
      @@ -26,7 +26,7 @@ COPY --from=clearlinux/os-core:latest / /
      os_core_install/
      RUN cd / && \
          find os_core_install | sed -e 's/os_core_install/install_root/' | xargs rm -d &> /dev/null || true

      -FROM clearlinux/os-core:latest
      +FROM clearlinux/os-core:31110

#. Build Dockerfile.

   .. code-block:: bash

      docker build \
      --no-cache \
      --build-arg http_proxy=$http_proxy \
      --build-arg https_proxy=$https_proxy \
      --tag clearlinux/httpd:31110 \
      httpd/

Third layer: cgit
-----------------

The next layer is :file:`clearlinux/cgit`.

#. Change the :file:`cgit/Dockerfile` to use the desired OS
   version; in this case, the build version is 31110.

   .. code-block:: bash

      $EDITOR cgit/Dockerfile

#. Run :command:`git diff`.

   The output shows:

   .. code-block:: diff

      diff --git a/cgit/Dockerfile b/cgit/Dockerfile
      index 9a3796d..59260fe 100644
      --- a/cgit/Dockerfile
      +++ b/cgit/Dockerfile
      @@ -7,7 +7,7 @@ RUN swupd update --no-boot-update $swupd_args

      # Grab os-release info from the minimal base image so
      # that the new content matches the exact OS version
      -COPY --from=clearlinux/httpd:latest /usr/lib/os-release /
      +COPY --from=clearlinux/httpd:31110 /usr/lib/os-release /

      # Install additional content in a target directory
      # using the os version from the minimal base
      @@ -22,11 +22,11 @@ RUN source /os-release && \
      # file exists on different layers. To minimize docker
      # image size, remove the overlapped files before copy.
      RUN mkdir /os_core_install
      -COPY --from=clearlinux/httpd:latest / /os_core_install/
      +COPY --from=clearlinux/httpd:31110 / /os_core_install/
      RUN cd / && \
          find os_core_install | sed -e 's/os_core_install/install_root/' | xargs rm -d &> /dev/null || true

      -FROM clearlinux/httpd:latest
      +FROM clearlinux/httpd:31110

#. Build Dockerfile.

   .. code-block:: bash

      docker build \
      --no-cache \
      --build-arg http_proxy=$http_proxy \
      --build-arg https_proxy=$https_proxy \
      --tag clearlinux/cgit:31110 \
      cgit/

#. Verify the installed OS version by noting the :command:`VERSION_ID` value
   in the :file:`/usr/lib/os-release` file in the container filesystem.

   .. code-block:: bash
      :linenos:
      :emphasize-lines: 6

      docker run clearlinux/cgit:31110 cat /usr/lib/os-release
      NAME="Clear Linux OS"
      VERSION=1
      ID=clear-linux-os
      ID_LIKE=clear-linux-os
      VERSION_ID=31110
      PRETTY_NAME="Clear Linux OS"
      ANSI_COLOR="1;35"
      HOME_URL="https://clearlinux.org"
      SUPPORT_URL="https://clearlinux.org"
      BUG_REPORT_URL="mailto:dev@lists.clearlinux.org"
      PRIVACY_POLICY_URL=http://www.intel.com/privacy


Example 4: Customize an application image at runtime
****************************************************

This section describes how to modify a published |CL| container at runtime.
In this example, we add Tensorflow\* into a :command:`clearlinux/python`
container. This approach can help accelerate the feature development process.

In this example, three separate console windows are used to easily interact
inside and outside of the container.

First console: Start the container
----------------------------------

#. Launch the clearlinux/python container.

   .. code-block:: bash

      docker run -it --rm clearlinux/python
      Python 3.7.3 (default, Jun 17 2019, 00:47:04)
      [GCC 9.1.1 20190616 gcc-9-branch@272336] on linux
      Type "help", "copyright", "credits" or "license" for more information.

#. Try to import Tensorflow inside the container using the command:
   :command:`import tensorflow as tf`. The example below shows the expected
   error message because the Docker image does not yet include the Tensorflow
   module.

   .. code-block:: bash

      >>> import tensorflow as tf
      Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      ModuleNotFoundError: No module named 'tensorflow'
      >>>

Second console: Add a bundle
----------------------------

#. In another console, find the :command:`<Container_ID>` of
   clearlinux/python launched. This example Container ID is d4ce9d526fa6.

   .. code-block:: bash

      docker ps

#. The output shows:

   .. code-block:: console

     CONTAINER ID   IMAGE               COMMAND   CREATED             STATUS              PORTS          NAMES
     d4ce9d526fa6   clearlinux/python   python3   About a minute ago  Up About a minute                  amazing_villani

#. Connect to the running clearlinux/python container.

   .. code-block:: bash

      docker exec -it d4ce9d526fa6 /usr/bin/bash
      root@d4ce9d526fa6/ #


#.  Use :command:`swupd` to install the machine-learning-tensorflow bundle.

    .. code-block:: bash

       root@d4ce9d526fa6/ # swupd bundle-add machine-learning-tensorflow
       Loading required manifests...
       Downloading packs (692.32 Mb) for:
       - machine-learning-tensorflow
       … …
       ...100%
       Finishing packs extraction...
       No extra files need to be downloaded
       Installing bundle(s) files...
       ...100%
       Calling post-update helper scripts.
       Successfully installed 1 bundle

#. After the machine-learning-tensorflow bundle is installed in the
   container, in the first console, import Tensorflow, which will be
   successful now. You could also save the updated container using the
   command :command:`docker commit <Container_ID>`.

   .. code-block:: bash

      >>> import tensorflow as tf
      >>> tf.__version__
      '1.13.1'

Third console: Save the modified container
------------------------------------------

#. In a third console, save the container with a new tag. Our example uses
   the tag `tensorflow_added` to identify our modified container.

   .. code-block:: bash

      docker commit d4ce9d526fa6 clearlinux/python:tensorflow_added

#. Launch the modified container, and then import Tensorflow with success.

   .. code-block:: bash

      docker run -it clearlinux/python:tensorflow_added
      Python 3.7.3 (default, Jun 17 2019, 00:47:04)
      [GCC 9.1.1 20190616 gcc-9-branch@272336] on linux
      Type "help", "copyright", "credits" or "license" for more information.

   .. code-block:: bash

      >>> import tensorflow as tf
      >>> tf.__version__
      '1.13.1'
      >>>

Background
**********

Multi-stage Dockerfiles contain more than one :command:`FROM` directive. All
of the multi-stage Clear Linux OS Dockerfiles share a common base layer
called :command:`clearlinux/os-core:latest`. All of the higher level layers
inherit the Clear Linux OS version from this base layer.

For details on how we leveraged multi-stage Docker builds, see the article
`Minimizing Clear Linux OS container sizes`_.

#. :command:`clearlinux/os-core` is built once per day. It is a container
   containing a minimal Linux userspace.

#. The target container image uses either :command:`clearlinux/os-core` as a
   base layer or another container image :command:`clearlinux/` as a base
   layer.

#. Bundle(s) containing the application are downloaded during the first stage
   of the build process using :command:`swupd`.

#. The final container image is a composition of its base layer and the
   specific feature layer, via :command:`FROM clearlinux/<base layer>:latest
   , such as: os-core, httpd, and via :command:`COPY --from=builder /
   install_root /`. Using this method, the target container images are kept
   up to date without file duplication. For application-centric containers,
   `os-core-update` is excluded to improve size optimization.

Related topics
**************

*	:ref:`docker`
*	:ref:`container-image-new`

.. _images on Docker Hub: https://hub.docker.com/u/clearlinux
.. _GitHub\*: https://github.com/clearlinux/dockerfiles
.. _clearlinux image on Docker Hub: https://hub.docker.com/_/clearlinux
.. _clearlinux microservice dockerfile repo: https://github.com/clearlinux/dockerfiles

.. _multi-stage build: https://docs.docker.com/develop/develop-images/multistage-build/

.. _Minimizing Clear Linux OS container sizes: https://clearlinux.org/blogs-news/minimizing-clear-linux-os-container-sizes

.. _multi-stage build to reduce image size: https://clearlinux.org/blogs-news/minimizing-clear-linux-os-container-sizes
