.. _tables:

Tables
######

Tables must only be used for information that is either too numerous or too
related for a list to be appropriate. The smallest acceptable table is 2x2
not counting the table header. The |CL-ATTR| uses special ReStructuredText
markup to make including tables easier. If you plan on adding a table
consider transforming it into a list before you embark on creating a table.
Follow these general guidelines:

* Use tables sparingly.

* Stick to the 72-78 characters line length limit.

* Indent the contents correctly. This allows the content to be read even if
  it is not rendered.

* Only create a table if the body of the table contains six or more cells,
  which is a minimum table size of at least 2x3 or 3x2.

ReST supports several types of tables. |CL| uses grid and
:abbr:`CSV-tables (Comma Separated Values tables)`. Grid tables are only
suited for very short content since they must be fully drawn. CSV-tables
support multi-lined cells, are easy to update and allow more layout
options.

Use grid tables for small tables where the layout needs to be determined
manually. For example:

+-----------------+------------------------+--------------+------------+
| Name            | Purpose                | Known        | References |
| (or brand name) |                        | Applications |            |
+=================+========================+==============+============+
| Super Glue      | Glues things together  | Small car    | Quick Fix, |
|                 | with extra strength.   | repairs.     |  2010.     |
+-----------------+------------------------+--------------+------------+
| Masking Tape    | Stops paint from       | Painting     | Master     |
|                 | covering a surface     | walls.       | Painter,   |
|                 | allowing for sharp     |              | 2007.      |
|                 | edges.                 |              |            |
+-----------------+------------------------+--------------+------------+

Use '=' between the table heading and the rows to define the table header. Do
not add emphasis to the contents of the table header using \*\*.


This template can help you create grid tables:

.. code-block:: rst

   +------------------------+------------+----------+----------+
   | Header row, column 1   | Header 2   | Header 3 | Header 4 |
   | (header rows optional) |            |          |          |
   +========================+============+==========+==========+
   | body row 1, column 1   | column 2   | column 3 | column 4 |
   +------------------------+------------+----------+----------+
   | body row 2             | ...        | ...      |          |
   +------------------------+------------+----------+----------+

CSV-tables are more flexible than grid tables. They can be updated easily and
support several layout options. For example:

.. csv-table:: Frozen Delights!
   :header: "Treat", "Quantity", "Description"
   :widths: 15, 10, 30

   "Albatross", 2.99, "On a stick!"
   "Crunchy Frog", 1.49, "If we took the bones out, it wouldn't be
   crunchy, now would it?"
   "Gannet Ripple", 1.99, "On a stick!"

Some of the options available with CSV-tables are table titles, an optional
header row separate from the rest of the table, and customizable column width.
See the Sphinx `CSV-tables documentation`_ to learn all the possible options
available.

This template can help you create CSV-tables:

.. code-block:: rst

   .. csv-table:: Table title (optional)
      :header: The header, values, for each column
      :widths: 15, 10, 30

      If the values, in the, "table go beyond the line length, use quotes to
      keep the content together."
      Numbers like, 10, are never surrounded by quotes.
      Text can, "be", in quotes but it is only needed for longer lines.

The template renders as:

.. csv-table:: Table title (optional)
   :header: The header, values, for each column
   :widths: 15, 10, 30

   If the values, in the, "table go beyond the line length, use quotes to keep
   the content together."
   Numbers like, 10, are never surrounded by quotes.
   Text can, "be", in quotes but it is only needed for longer lines.



.. _CSV-tables documentation:
   http://docutils.sourceforge.net/docs/ref/rst/directives.html#csv-table