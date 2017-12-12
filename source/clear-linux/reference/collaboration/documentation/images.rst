.. _images:

Images
######

Images or figures grab the reader's attention and convey information that
sometimes is difficult to explain using words alone. Well-planned graphics
reduce the amount of text required to explain information. Non-native English
readers rely heavily on graphics because graphics enhance their understanding of the text.

Follow these guidelines when creating graphics for the |CLOSIA|:

* Save the image files in a :file:`figures` folder. The folder must be found
  at the same level as the file containing the text.

* Use only lower case letters for image filenames.

* Separate multiple words in filenames using dashes.

* Name figures with the filename of the file they appear on and add a number
  to indicate their place in the file. For example: The third figure added to
  the :file:`fibers.rst` file must be named :file:`fibers-3.png`.

* Include a caption describing the figure's content and to use as a reference.
  All figures must have a caption.

* Use cross-references. Refer to your graphics in the main text flow.
  Create a label using the filename of the image. Use the `:ref:` role to place
  the cross reference, see :ref:`cross` for more details.

* Place the figure immediately after its reference in the text flow or as
  close as possible.

* Keep figures simple. They should only contain the information the
  reader needs.

* Use figures judiciously. Don't use superfluous graphics and don't
  use graphics as mere decorations. They must have purpose. You don't
  need to show a screenshot of every single step or window in a software
  installation procedure, for example.

* Avoid volatility. Don't incorporate information into a graphic that
  might change with each release, for example: product versions or
  codename abbreviations.

* Use only approved image formats. Use either PNG or JPEG bitmap files for
  screenshots and SVG files for vector graphics. If a figure is not a
  photograph or screenshot, please provide figure as a vector graphic to
  ensure it can be changed later on.


Examples
********

These examples follow the guidelines and can be used as a reference.

The fiber context is represented in the diagram either as a box
containing different objects or a :ref:`symbol <fibers-1.svg>`.

.. _fibers-1.svg:

.. figure:: figures/fibers-1.svg
   :scale: 75 %
   :alt: Fibers Execution Context Symbol

   The graphic representation of the fibers execution context.

   This symbol is used to illustrate the actions performed by the
   abstract fibers execution context.

Templates
*********

Use this template to add a figure to your documentation according to
these guidelines.

.. code-block:: rst

   .. _file-name-#.ext:

   .. figure:: figures/file-name-#.ext
      :scale: 75%
      :alt: Alternative text.

      Figure 1: Brief caption detailing the contents of the image.

      Any additional explanation, description or actions depicted in the
      image. It can encompass multiple lines.
