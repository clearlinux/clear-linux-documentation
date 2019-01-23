.. _structure-formatting:

Structure and formatting
########################

Content should be organized to support scanning. Consistent organization,
formatting, and writing style helps readers quickly find what they need and to
understand the content more effectively. This document describes our
organization and formatting guidelines.

Refer to :ref:`writing-guide` to learn how we keep our documents clear and
concise.

.. contents:: :local:
   :depth: 1

Markup
******

Our documentation is written in the reStructuredText markup language, using
Sphinx roles and directives. We use Sphinx to generate the final documentation.
You can read more about reStructuredText and Sphinx on their respective
websites:

* `Sphinx documentation`_
* `reStructuredText Primer`_

You can view the content directly in the .rst markup files, or generate the HTML
content by installing and building the documentation locally. To run the
documentation locally, follow the instructions found in the
`documentation repository`_ README.

New pages
=========

There are a few additional steps to consider when adding a new page to the
documentation. First, identify where your new page should be located within the
existing `Documentation organization`_. Second, make sure the new page is picked
up in the Sphinx build and easily linkable from other content.

Each page must be included in a `Sphinx toctree`_ in order to be included in the
documentation content tree. Typically, pages are added to the section landing
page toctree.

For example, the :ref:`collaboration` page toctree looks like:

.. code-block:: rest

   .. toctree::
      :maxdepth: 1

      writing-guide
      structure-formatting

Additionally, each page must include a uniquely named reST label directly before
the page title, to enable the `Sphinx ref role`_ for linking to a page.

For example, this page "Structure and formating" has the label
``.. _structure-formatting``:

.. code-block:: rest

   .. _structure-formatting:

   Structure and formatting
   ########################

This page can then be referenced from other pages in the documentation using the
`:ref:` role:

.. code-block:: rest

   :ref:`structure-formatting`

Documentation organization
**************************

The documentation is organized into five general sections:

#. **Concepts**: Introduction and overview of |CL| specific concepts or
   features.
#. **Get started**: Information about getting started with |CL|.
#. **Guides**: Detailed information and instruction on using |CL| features.
#. **Tutorials**: Step-by-step instruction for using |CL| in specific use cases.
#. **Reference**: Supplementary and reference information for |CL|.

Page structure
==============

Each page in the documentation should follow the basic format of:

* Overview: 1-2 sentences describing what this page shows and why it matters
* Prerequisites: Describe any pre-work necessary to the content (if appropriate)
* Content
* Next steps: List links to next steps (if appropriate)
* Related topics: List links to related content (if appropriate)

Headings
========

Use headings to section and organize your content for better readability and
clarity.

* All files must have a top level heading, which is the title for the page.
* Up to three additional levels of headings are allowed under the title heading.
* Each heading should be followed by at least one paragraph of content. Avoid
  two or more consecutive headings.

Refer to the :ref:`writing-guide` for tips on using headings to create
:ref:`scannable content <scannable-content>`.

To mark up headings in the .rst file:

* Use hash-tags to underline the file's main title:

  .. code-block:: rest

     Main title
     ##########

* Use asterisks to underline the file's first level headings:

  .. code-block:: rest

     First level heading
     *******************

* Use equal signs to underline the file's second level of headings:

  .. code-block:: rest

     Second level heading
     ====================

* Use dashes to underline the file's third level of headings:

  .. code-block:: rest

     Third level heading
     -------------------

In-page navigation
==================

If a page has three or more sections, provide quick links to each section. Place
the quick links after the overview section.

Use the standard `reST contents directive`_ with depth: 1 for quick links.

Inline text formatting
**********************

We use the `Microsoft Writing Style Guide`_ as our starting point for text
formatting. We apply the formatting using reST and Sphinx markup.

Use our quick reference for the most commonly used inline text elements:

+--------------------------------+---------------------------------------+-----------------------------+
| **Element**                    | **Convention**                        | **reST/Sphinx**             |
+--------------------------------+---------------------------------------+-----------------------------+
| Acronyms                       | Define acronym when first used. After | Use the ``:abbr:`` role, in |
|                                | first use and definition, use the     | the following format:       |
|                                | acronym only.                         |                             |
|                                |                                       | ``:abbr:`Acronym (Def)```   |
+--------------------------------+---------------------------------------+-----------------------------+
| Bundle names                   | Bold                                  | Use the ``:command:`` role. |
+--------------------------------+---------------------------------------+-----------------------------+
| Callouts                       |                                       | Use ``.. note::``           |
+--------------------------------+---------------------------------------+-----------------------------+
| Code/command examples          | Monospace, visually distinct          | Use ``.. code-block::``     |
|                                | from rest of text. Use an             | with the correct language   |
|                                | indented call-out box.                | setting.                    |
+--------------------------------+---------------------------------------+-----------------------------+
| Commands                       | Bold                                  | Use the ``:command:`` role. |
+--------------------------------+---------------------------------------+-----------------------------+
| Command flags                  | Bold                                  | Use the ``:command:`` role. |
+--------------------------------+---------------------------------------+-----------------------------+
| Console output                 | Monospace, visual distinction         | Use ``.. code-block::``     |
|                                | from rest of text. Use an             | with console as the         |
|                                | indented call-out box.                | language setting.           |
+--------------------------------+---------------------------------------+-----------------------------+
| Emphasis                       | Italic                                | ``*strong*``                |
+--------------------------------+---------------------------------------+-----------------------------+
| Environment variables          | Use the case format of the            | Use ``:envvar:``            |
|                                | environment variable.                 |                             |
+--------------------------------+---------------------------------------+-----------------------------+
| Example commands with          | Use angle brackets for swapping       |                             |
| optional or replaceable        | in the specific name,                 |                             |
| parts                          | e.g. <package-name>.                  |                             |
|                                |                                       |                             |
|                                | Use square brackets for optional      |                             |
|                                | parts,                                |                             |
|                                | e.g. [--build].                       |                             |
+--------------------------------+---------------------------------------+-----------------------------+
| Example URLs (not linked)      | Plain text                            |                             |
+--------------------------------+---------------------------------------+-----------------------------+
| File extensions                | Lowercase                             |                             |
+--------------------------------+---------------------------------------+-----------------------------+
| File names, directories, paths | Title style capitalization            | Use the ``:file:`` role.    |
+--------------------------------+---------------------------------------+-----------------------------+
| GUI labels                     |                                       | Use ``:guilabel:``          |
+--------------------------------+---------------------------------------+-----------------------------+
| Inline comments                |                                       | Use ``..``                  |
+--------------------------------+---------------------------------------+-----------------------------+
| Keystrokes                     |                                       | Use ``:kbd:``               |
+--------------------------------+---------------------------------------+-----------------------------+
| Local navigation               |                                       | ``.. contents:: :local:``   |
|                                |                                       | with a depth of 1           |
+--------------------------------+---------------------------------------+-----------------------------+
| Menu selection                 |                                       | Use ``:menuselection:``     |
+--------------------------------+---------------------------------------+-----------------------------+
| New terms                      | Italic for first use, normal for all  | ``*term*``                  |
|                                | subsequent uses.                      |                             |
|                                |                                       |                             |
|                                | If it is used outside of the source   |                             |
|                                | of definition, link the term.         |                             |
+--------------------------------+---------------------------------------+-----------------------------+
| Product name                   | Follow correct trademark and          |                             |
|                                | attribution guidelines.               |                             |
+--------------------------------+---------------------------------------+-----------------------------+
| Tool names                     | Correctly capitalized, no quotes,     |                             |
|                                | bold, or italics as the basic rule.   |                             |
|                                |                                       |                             |
|                                | If the tool name is the command, like |                             |
|                                | most Linux tools, treat it like a     |                             |
|                                | command.                              |                             |
|                                |                                       |                             |
|                                | If the tool name is lowercase and     |                             |
|                                | used at the start of a sentence, use  |                             |
|                                | bold.                                 |                             |
+--------------------------------+---------------------------------------+-----------------------------+

White space and line length
===========================

Limit line length to 78 characters. The GitHub web interface forces this
limitation for readability.

Remove trailing whitespace from your documents.

Code blocks and examples
************************

When providing example code or commands use the `Sphinx code-block directive`_.
Select the appropriate syntax highlighting for the example command or code.

For example, if showing console output, use console highlighting:

.. code-block:: rest

   .. code-block:: console

Sphinx provides other ways of `marking up example code`_ if needed.

Lists and instructions
**********************

Use a numbered list when the order or priority of the items is important, such
as step-by-step instructions.

Use a bulleted list when the order of the items is not important.

For both list types, keep all items in the list parallel. See
:ref:`parallelism`.

Use standard `reST list markup`_.

Numbered lists
==============

Numbered lists are most frequently used for procedures. Use numbered lists to
show sequence for the items. Follow our guidelines for numbered lists:

* Make sure the list is sequential and not just a collection of items.
* Introduce a numbered list with a sentence. End the setup text with a
  colon. Example: "To configure the unit, perform the following steps:"
* Each item in the list should be parallel.
* Treat numbered list items as full sentences with correct ending
  punctuation.
* You may interrupt numbered lists with other content, if relevant,
  e.g. explanatory text, commands, or code.
* Second-level steps are acceptable; avoid third-level steps.
* Avoid single-step procedures; the minimum number of steps in a procedure
  is two.
* Do not create numbered lists that emulate flowcharts. The reader should be
  able to execute the list of steps from first to last without branching or
  looping.
* Avoid over-using numbered lists, except in procedural documents such as
  tutorials and step-by-step guides.

Bulleted lists
==============

Use bulleted lists to reduce wordiness and paragraph density, especially when
a sequence is not required. Here are some guidelines for bulleted lists:

* Introduce a bulleted list with a sentence. End the setup text with a
  colon. Example: "To repair the unit, you will need the following items:"
* Each item in the list should be parallel.
* Avoid interrupting bulleted lists with other paragraph styles.
* Second-level bullets are acceptable; avoid third-level bullets.

Use the correct ending punctuation for sentence style bullet lists. For example:

**Use this:**

::

  When setting the user code, remember:

  * Use a number that has a meaning for you.
  * Change the code once a month.
  * Do not disclose the user code to anyone, including the security company.

**Not this:**

::

  When setting the user code remember:

  * make the user code easy to remember. Use a number that has a meaning for you
  * change the code once a month
  * do not disclose the user code to anyone else. This includes the security
    company

Instructions
============

When presenting instructions, such as in a tutorial, present them in a numbered
list according to these guidelines:

* Each step (list item) should describe one action.

* If the same steps are repeated, refer to the earlier steps rather than
  repeating them.

* When a step includes a command or code block as an example, put the command
  or code block after the step that includes them.

* Use supporting images where appropriate. If the series of steps is supported
  by one figure, refer to the figure in the introductory text.

  For example: "See Figure 15 and do the following:"

  When a series of steps is supported by two or more figures, refer to the
  specific figure in the relevant step and show the figure immediately after
  the reference. **Do not write**: "See figures 15 through 22 and do the
  following:"

Notices
*******

We use four special types of notices: notes, cautions, warnings, and dangers.
Here are some specific rules and tips regarding use of these notices:

* Do not use a notice directly after a heading. Notices must follow a variant of
  body text.
* Do not include more than one notice in a single notice block.
* Avoid back-to-back notices.
* If back-to-back notices are not avoidable, make sure each distinct notice in
  the notice block is clearly defined.

Use the standard `reST admonition directive`_.

Notes, cautions, and warnings
=============================

Use notes sparingly. Avoid having more than one note per section. If you exceed
this number consistently, consider rewriting the notes as main body text.

Use cautions and warnings to alert readers of potential problems or pitfalls.
Use conditional phrases in cautions and warnings, such as "If you do X, then Y
will occur."

These are examples of typical notices and the conditions for their usage:

.. note::
   Notes are extra bits of information that supplement the main content. Notes
   should be relatively short.

.. caution::
   Cautions are low-level hazard messages that alert the user of possible
   equipment, product, and software damage, including loss of data.

.. warning::
   Warnings are mid-level hazards that are likely to cause product damage.

Links
*****

Use the standard `reST markup for links`_.

To add a cross-reference to another documentation page, use the `:ref:` role:

.. code-block:: rest

   :ref:`structure-formatting`

To add an external link, we use named references that refer to a defined
link/label at the bottom of the page.

For example, an external link is defined at the bottom of the page like this:

.. code-block:: rest

   .. _wiki about dogs: https://en.wikipedia.org/wiki/Dog

The defined link is then used in the content like this:

.. code-block:: rest

   Check out the great `wiki about dogs`_.

Images
******

Use images or figures to convey information that may be difficult to explain
using words alone. Well-planned graphics reduce the amount of text required to
explain a topic or example.

Follow these guidelines when using graphics in support of your documentation:

* Keep it simple. Use images that serve a specific purpose in your document,
  and contain only the information the reader needs.

* Avoid graphics that will need frequent updating. Don't include information in
  a graphic that might change with each release, such as product versions.

* Use either PNG or JPEG bitmap files for screenshots and SVG files for vector
  graphics.

* Place the image immediately after the text it helps clarify, or as close as
  possible.

* Use the `Sphinx figure directive`_ to insert images and figures into the
  document. Include both alt text, a figure name, and caption.

  For example:

  .. code-block:: rest

     .. figure:: figures/topic-1.png
        :alt: An image supporting the topic.

        Figure 1: This is the figure 1 caption.

* Include at least one direct reference to an image from the main text, using
  the figure number. For example:

  **Use this:** ::

    Figure 1

  **Not this:** ::

    The figure above or below

Images should follow these naming and location conventions:

* Save the image files in a :file:`figures` folder at the same level as the file
  that will reference the image.
* Name image files according to the following rules:

  * Use only lower case letters.
  * Separate multiple words in filenames using dashes.
  * Name images using the filename of the file they appear on and add a number
    to indicate their place in the file. For example, the third figure added to
    the :file:`welcome.rst` file must be named :file:`welcome-3.png`.

.. _Sphinx documentation: http://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html
.. _reStructuredText Primer: http://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html
.. _documentation repository: https://github.com/clearlinux/clear-linux-documentation
.. _Sphinx toctree: https://www.sphinx-doc.org/en/master/usage/quickstart.html?highlight=toctree#defining-document-structure
.. _Sphinx ref role: https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#role-ref
.. _reST contents directive: http://docutils.sourceforge.net/docs/ref/rst/directives.html#table-of-contents
.. _Microsoft Writing Style Guide: https://docs.microsoft.com/en-us/style-guide/welcome/
.. _Sphinx code-block directive: http://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-code-block
.. _marking up example code: http://www.sphinx-doc.org/en/1.6/markup/code.html
.. _reST list markup: http://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#lists-and-quote-like-blocks
.. _reST admonition directive: http://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#directives
.. _reST markup for links: http://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#hyperlinks
.. _Sphinx figure directive: http://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#directives
