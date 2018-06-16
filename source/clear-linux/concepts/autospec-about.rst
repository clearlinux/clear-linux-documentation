.. _autospec-about: 

.. _autospec-overview: 

Autospec overview
#################

Whereas a standard RPM build process using ``rpmbuild`` requires a tarball 
and ``spec`` file to start, ``autospec`` only requires a tarball. 
``autospec`` analyzes the source code and :file:`Makefile` information in 
order to generate a ``spec`` file for you. Although not required, you can 
influence ``autospec`` by providing control files. 

.. code-block:: console 

   buildreq_add
   buildreq__ban
   pkgconfig_add
   pkgconfig_ban
   requires_add
   requires_ban
   options.conf
   build_pattern

These files should be located in same directory as the resulting ``spec`` 
file. 

.. note:: 

   For a comprehensive list of control files, view the `autospec readme`_.  

Control files are explained in Table 1.

.. list-table:: **Table 1. Control Files**
   :widths: 20 80
   :header-rows: 1
   
   * - Filename
     - Description
   * - buildreq_add
     - Each line in the file provides the name of a package to add as a
       build dependency to the ``spec``.
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
       style when generating the ``spec``.
   * - pkgconfig_ban
     - Each line in this file is a pkgconfig() build dependency that should
       not be added automatically to the build, much the same as 
       `` buildreq_ban``. As with ``pkgconfig_add``, these names are 
       automatically transformed by ``autospec`` into their correct 
       ``pkgconfig($name))`` style.   
   * - requires_add
     - Each line in the file provides the name of a package to add as a
       runtime dependency to the ``spec``.    
   * - requires_ban
     - Each line in the file is a runtime dependency that under no
       circumstance should be automatically added to the runtime 
       dependencies. This is useful to block automatic configuration 
       routines adding undesired functionality, or to omit any automatically 
       discovered dependencies during tarball scanning.
   * - build_pattern
     - In certain situations, the automatically detected build pattern may
       not work for the given package. This one line file allows you to 
       override the build pattern that ``autospec`` will use.
   * - options.conf 
     - Further control of the build can be achieved through the use of the
       ``options.conf`` file. If this file does not exist it is created by
       autospec with default values. If certain deprecated configuration 
       files exists autospec will use the value indicated by those files and
       remove them. 

How autospec works
******************

Autospec attempts to infer the requirements of the ``spec`` file. If 
autospec infers correctly, the control files (Table 1) will automatically 
correct the build requirements. These control files are used to influence
the ``spec`` file generation. 

#. The :command:`make autospec` command generates a ``spec`` file from the 
   control files.  

#. ``autospec`` creates a ``chroot`` with ``mock`` config. 
   
#. ``autospec`` attempts to build an RPM from the generated ``spec`` file.
   
#. ``autospec`` detects any missed definitions in the ``spec`` file. 

.. note:: 

   * If there are missed definitions, ``autospec`` creates another ``mock``
     ``chroot`` and starts building again at Step 1. 
   * If a build error occurs, ``autospec`` stops for user inspection. 
   * If no build errors occur, RPM packages are successfully built.       

``autospec`` continuously runs updated builds, based on new information 
discovered from build failures until it has a valid ``spec`` file. 

.. _autospec readme: https://github.com/clearlinux/autospec
