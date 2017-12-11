.. _code:

Code blocks
###########

Collaborating to the |CLOSIA| is all about code. Therefore, your
documentation must include as many code examples as possible. You can write
code examples directly in the documentation or include them from a source
file. Use these guidelines to insert code blocks to your documentation:

* Include code examples from a source file. Only write the code example
  directly into the documentation if the example is less than 10 lines long.

* Use the ``:linenos:`` option of the `literalinclude` directive to add line
  numbers to your example.

* Specify the programing language of your example. Not only will it
  add syntax highlighting but it also allows the reader to identify code
  efficiently. Use `bash` for console commands, `asm` for assembly code and
  `c` for C code.

* Treat all console commands entered by users as code examples.

Examples
********

This is a code example included from a file. Note how only certain lines of
the source file are included and how the lines are renumbered.

This source:

.. code-block:: rst

   .. literalinclude:: ./hello.c
      :language: c
      :lines: 97-110
      :linenos:

Renders as:

.. literalinclude:: ./hello.c
   :language: c
   :lines: 97-110
   :linenos:


This example shows a series of console commands. Line numbering is not
required. Specify that these are commands using `bash` as the programing
language.

This source:

.. code-block:: rst

   .. code-block:: bash

      $ mkdir ${HOME}/x86-build

      $ mkdir ${HOME}/arm-build

      $ mkdir ${HOME}/cross-src

Renders as:

.. code-block:: bash

   $ mkdir ${HOME}/x86-build

   $ mkdir ${HOME}/arm-build

   $ mkdir ${HOME}/cross-src

.. note::
   You will find instances which use `console` instead of `bash`. We are
   currently in the process of implementing a distinction between the two.
   Moving forward, `bash` will be used for commands entered by readers, and
   `console` will be used for the output users obtain in the command prompt.

Finally, this is a code example that is not part of the |CL| code base. It is
not even valid code but it can illustrate the concept.

This source:

.. code-block:: rest

   .. code-block:: c

      static NANO_CPU_INT_STUB_DECL (deviceStub);

      void deviceDriver (void)

      {

      .
      .
      .

      nanoCpuIntConnect (deviceIRQ, devicePrio, deviceIntHandler,
      deviceStub);

      .
      .
      .

      }

Renders as:

.. code-block:: c

   static NANO_CPU_INT_STUB_DECL (deviceStub);

   void deviceDriver (void)

   {

   .
   .
   .

   nanoCpuIntConnect (deviceIRQ, devicePrio, deviceIntHandler,
   deviceStub);

   .
   .
   .

   }

Templates
*********

We included templates for a basic ``.. code-block::`` directive
and for a ``.. literalinclude::`` directive.

Use ``code-block`` for console commands, brief examples, and examples
outside the |CL| code base.

.. code-block:: rst

   .. code-block:: language

      source

Use ``litteralinclude`` to insert code from a source file. Keep in
mind that you can include the entire contents of the file or just
specific lines.

.. code-block:: rst

   .. literalinclude:: ../path/to/file/file_name.c
      :language: c
      :lines: 5-30, 32, 70-100
      :emphasize-lines: 3
      :linenos:

.. caution::
   The ``:emphasize-lines:`` option uses the line numbering provided
   by ``:linenos:``. The emphasized line in the template will be the
   third one of the example but the eighth one of the source file.

