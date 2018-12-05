.. _inline:

Inline Markup
*************

Sphinx supports a large number of inline markup elements called roles. The
|CL-ATTR| documentation encourages the use of as many roles as
possible. Thus, you can use any additional roles supported by Sphinx
not listed here. Please refer to the `Sphinx reStructuredText Markup`_
documentation for the full list of supported roles.

The following markup is required in every instance unless otherwise
specified. Each item provides a syntax example followed by the rendered
result.

Abbreviations
  Use the `:abbr:` abbreviation role to define an acronym or an initialism.
  Add the abbreviation markup only once per file. After the abbreviation, the
  acronym can be used without further definition or markup. Do not use
  abbreviation markup on headings.

  ::

     :abbr:`API (Application Program Interface)`

  .. parsed-literal::

     :abbr:`API (Application Program Interface)`

OS Commands
  Use the `:command:` role when the name of a specific command is used in a
  paragraph for emphasis. Use the ``.. code-block::`` directive for fully
  actionable commands in a series of steps.

  ::

     :command:`make`

  .. parsed-literal::

     :command:`make`

Commandline Options
  In most cases, use asterisks "*" to emphasize the name of a command
  option. 

  ::

     Use the *-p* option to print the file.

  .. parsed-literal::

     Use the *-p* option to print the file.

  However, if you have defined an ``.. option::`` directive, you may
  use the `:option:` role. Note that the result links back to the 
  option definition.

  .. code-block:: rest

     .. option: -o <output.xsl>

        Description of the -o option 

     The :command:`pandoc` command can be used without :option:`-o`

  .. option:: -o <output.xsl>

     Description of the -o option

  .. parsed-literal::

     The :command:`pandoc` command can be used without :option:`-o` 

Files
  Use the `:file:` role to emphasize a filename or directory. Do not use the
  role inside a code-block but use it inside all notices that contain files
  or directories. Place variable parts of the path or filename in brackets
  `{}`.

  .. code-block:: rest

     :file:`collaboration.rst`

     :file:`doc/{user}/collaboration/figures`

  .. parsed-literal::

     :file:`collaboration.rst`

     :file:`doc/{user}/collaboration/figures`

GUI Objects
  Use the `:guilabel:` role to emphasize elements of a graphic
  user interface within a description. It replaces the use of quotes
  when referring to windows' names, button labels, options, or single
  menu elements. Always follow the marked element with the appropriate
  noun. For example:

  ::

     In the :guilabel:`Tools` menu, click :guilabel:`settings`.

  .. parsed-literal::

     In the :guilabel:`Tools` menu, click :guilabel:`settings`.

Menu Navigation
  Use the `:menuselection:` role to indicate the navigation through a menu
  ending with a selection. Every `:menuselection:` element can have up to two
  menu steps before the selected item. If more than two steps are required,
  it can be combined with a `:guilabel:` or with another `:menuselection:`
  element. For example:

  ::

     Go to :guilabel:`File` and select :menuselection:`Import --> Data Base --> MySQL`.

     Go to :menuselection:`Window --> View` and select :menuselection:`Perspective --> Other --> C++`

  .. parsed-literal::

     Go to :guilabel:`File` and select :menuselection:`Import --> Data Base --> MySQL`.
  
     Go to :menuselection:`Window --> View` and select :menuselection:`Perspective --> Other --> C++`

Makefile Variables
  Use the `:makevar:` role to emphasize the name of a Makefile variable.
  The role can include only the name of the variable or the variable
  plus its value.

  ::

     :makevar:`PLATFORM_CONFIG`

     :makevar:`PLATFORM_CONFIG=basic_atom`

  .. parsed-literal::

     :makevar:`PLATFORM_CONFIG`

     :makevar:`PLATFORM_CONFIG=basic_atom`

Environment Variables
  Use the `:envvar:` role to emphasize the name of environment
  variables. Just as with `:makevar:`, the markup can include only the
  name of the variable or the variable plus its value.

  ::

     :envvar:`ZEPHYR_BASE`
   
     :envvar:`QEMU_BIN_PATH=/usr/local/bin`

  .. parsed-literal::

     :envvar:`ZEPHYR_BASE`
   
     :envvar:`QEMU_BIN_PATH=/usr/local/bin`

.. _Sphinx reStructuredText Markup:
   http://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html