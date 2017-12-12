.. _inline:

Inline Markup
*************

Sphinx supports a large number of inline markup elements called roles. The
|CLOSIA| documentation encourages the use of as many roles as
possible. Thus, you can use any additional roles supported by Sphinx
even if not listed here. Please refer to the `Sphinx Inline Markup`_
documentation for the full list of supported roles.

The following markup is required in every instance unless otherwise
specified. Each item provides examples and a template for the correct use of
the roles.

* Use the `:abbr:` abbreviation role to define an acronym or an initialism.
  Add the abbreviation markup only once per file. After the abbreviation, the
  acronym can be used without further definition or markup. Do not use
  abbreviation markup on headings.

   :abbr:`API (Application Program Interface)`

   Template:

   ``:abbr:`TIA (This Is an Abbreviation)```

* Use the `:command:` role when the name of a specific command is used in a
  paragraph for emphasis. Use the ``.. code-block::`` directive for fully
  actionable commands in a series of steps.

   :command:`make`

   Template:

   ``:command:`command```

* Use the `:option:` role to emphasize the name of a command option
  with or without its value. This markup is usually employed in
  combination with the `:command:` role. For example:

   :option:`-f`
   :option:`--all`
   :option:`-o output.xsl`
   The :command:`pandoc` command can be used without the :option:`-o`
   option, creating an output file with the same name as the source
   but a different extension.

   Template:

   ``:option:`Option```

* Use the `:file:` role to emphasize a filename or directory. Do not use the
  role inside a code-block but use it inside all notices that contain files
  or directories. Place variable parts of the path or filename in brackets
  `{}`.

   :file:`collaboration.rst` :file:`doc/{user}/collaboration/figures`

   Template:

   ``:file:`filename.ext` :file:`path/or/directory```

* Use the `:guilabel:` role to emphasize elements of a graphic
  user interface within a description. It replaces the use of quotes
  when referring to windows' names, button labels, options, or single
  menu elements. Always follow the marked element with the appropriate
  noun. For example:

   In the :guilabel:`Tools` menu.
   Press the :guilabel:`OK` button.
   In the :guilabel:`Settings` window you find the :guilabel:`Hide
   Content` option.

   Template:

   ``:guilabel:`UI-Label```

* Use the `:menuselection:` role to indicate the navigation through a menu
  ending with a selection. Every `:menuselection:` element can have up to two
  menu steps before the selected item. If more than two steps are required,
  it can be combined with a `:guilabel:` or with another `:menuselection:`
  element. For example:

   :menuselection:`File --> Save As --> PDF`
   Go to :guilabel:`File` and select :menuselection:`Import --> Data
   Base --> MySQL`.
   Go to :menuselection:`Window --> View` and select :menuselection:`
   Perspective --> Other --> C++`

   Template:

   ``:menuselection:`1stMenu --> 2ndMenu --> Selection```

* Use the `:makevar:` role to emphasize the name of a Makefile variable.
  The role can include only the name of the variable or the variable
  plus its value.

   :makevar:`PLATFORM_CONFIG`
   :makevar:`PLATFORM_CONFIG=basic_atom`

   Template:

   ``:makevar:`VARIABLE```

* Use the `:envvar:` role to emphasize the name of environment
  variables. Just as with `:makevar:`, the markup can include only the
  name of the variable or the variable plus its value.

   :envvar:`ZEPHYR_BASE`
   :envvar:`QEMU_BIN_PATH=/usr/local/bin`

   Template:

   ``:envvar:`ENVIRONMENT_VARIABLE```

.. _Sphinx Inline Markup:
   http://sphinx-doc.org/markup/inline.html#inline-markup
