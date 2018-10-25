.. _autospec-about:

Autospec
########

A standard RPM build process using ``rpmbuild`` requires a tarball and .spec
file to start. The .spec provides information about a package, how to
build it, as well as what should be installed and where.

``autospec`` is a tool to assist in the automated creation and maintenance of
RPM packaging in |CL-ATTR|. Compared to ``rpmbuild``, ``autospec`` requires
only a tarball and package name to start.

How autospec works
******************

``autospec`` attempts to infer the requirements of the .spec file
by analyzing the source code and :file:`Makefile` information.
It will continuously run updated builds based on new information
discovered from build failures until it has a complete and valid .spec file.
You may optionally influence the behavior of ``autospec`` by providing
:ref:`control files <control-files>`.

#. The :command:`make autospec` command generates a .spec based on
   analysis of code and control files, if present.

#. ``autospec`` creates a ``build root`` with ``mock`` config.

#. ``autospec`` attempts to build an RPM from the generated .spec.

#. ``autospec`` detects any missed declarations in the .spec.

#. If a build error occurs, ``autospec`` stops for user inspection and
   editing of control files to resolve issues.

#. After user inspection, ``autospec`` creates another ``mock`` ``chroot``
   and starts building again at Step 1.

Following these steps, ``autospec`` continues to rebuild the package, based on
new information discovered from build failures until it has a valid .spec. If
no build errors occur, RPM packages are successfully built.

.. _control-files:

Control files
*************

It is possible to influence the behavior of ``autospec`` by providing control
files. These files may be used to alter the default behavior of the configure
routine, to blacklist build dependencies, etc. Control files must be located
in the same directory as the resulting .spec.

Table 1 shows control files used to control dependencies, for example.

.. list-table:: **Table 1. Control files to control dependencies**
   :widths: 20 80
   :header-rows: 1

   * - Filename
     - Description
   * - buildreq_add
     - Each line in the file provides the name of a package to add as a
       build dependency to the .spec.
   * - buildreq_ban
     - Each line in the file is a build dependency that under no
       circumstance should be automatically added to the build dependencies.
       This is useful to block automatic configuration routines adding
       undesired functionality, or to omit any automatically discovered
       dependencies during tarball scanning.
   * - pkgconfig_add
     - Each line in the file is assumed to be a pkgconfig() build
       dependency. Add the pkg-config names here, as ``autospec`` will
       automatically transform the names into their ``pkgconfig($name)``
       style when generating the .spec.
   * - pkgconfig_ban
     - Each line in this file is a pkgconfig() build dependency that should
       not be added automatically to the build, much the same as
       `` buildreq_ban``. As with ``pkgconfig_add``, these names are
       automatically transformed by ``autospec`` into their correct
       ``pkgconfig($name))`` style.
   * - requires_add
     - Each line in the file provides the name of a package to add as a
       runtime dependency to the .spec.
   * - requires_ban
     - Each line in the file is a runtime dependency that under no
       circumstance should be automatically added to the runtime
       dependencies. This is useful to block automatic configuration
       routines adding undesired functionality, or to omit any automatically
       discovered dependencies during tarball scanning.

Further control of the build can be achieved through the use of the
``options.conf`` file. If this file does not exist, it is created by
``autospec`` with default values. If certain deprecated configuration
files exists ``autospec`` will use the value indicated by those files and
remove them.

For a comprehensive list of control files, view the `autospec readme`_.

Related topics
**************

* :ref:`autospec`
* :ref:`mixer`
* :ref:`mixin`

.. _autospec readme: https://github.com/clearlinux/autospec
