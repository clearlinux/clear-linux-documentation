.. _cross:

Cross-references
################

Sphinx provides different methods to create both internal and
external cross-references. Use only the following methods to increase the
consistency of the documents.

.. _internal-cross:

Internal cross-references
*************************

An internal cross-reference is a reference to a location within the |CLOSIA|
documentation. Use explicit markup labels and the ``:ref:`` role to create
cross references to headings, figures, and code examples as needed. Every
file must have a label before the title, which is identical to the file's 
name, in order to be be cross-referenced within the entire documentation.

Labels' naming conventions:

* Ensure the label is unique throughout the documentation

* Use only full words.

* Use \- to link multiple words.

* Use only as many words as necessary.

These are some examples of proper labels:

.. code-block:: rst

   .. _quick-start:

   .. _gerrit-access:

   .. _building-clear-linux:

Do not use labels like these:

.. code-block:: rst

   .. _QuickStart:

   .. _How to Gain Access to Gerrit:

   .. _building:

As an example, this is an internal reference to the beginning of the :ref:`rest`.

Observe that the ``:ref:`` role is replaced with the title's text.
Similarly, it will be replaced with the figure's caption. If a different
text is needed the ``:ref:`` role can still be used, for example:

This is an internal reference to the beginning of
:ref:`this section <rest>`.

Use the following templates to insert internal cross references properly.

.. code-block:: rst

   .. _label-of-target:

   This is a heading
   -----------------

   This creates a link to the :ref:`label-of-target` using the text of the
   heading.

   This creates a link to the :ref:`target <label-of-target>` using the word
   'target' instead of the heading.

The template renders as:

.. _label-of-target:

This is a heading
-----------------

This creates a link to the :ref:`label-of-target` using the text of the
heading.

This creates a link to the :ref:`target <label-of-target>` using the word
'target' instead of the heading. We use the term 'target' here similar to 
the way'anchor' is used in HTML. 

.. note::

   This type of internal cross reference works across multiple files, is
   independent of changes in the text of the headings, and works on all
   Sphinx builders.

External References
*******************

External references or hyperlinks can be added easily with reST. Only
hyperlinks with a separated target definition are allowed.

Do not use explicit hyperlinks consisting entire URLs. For example, links
like this one, https://clearlinux.org/ must be avoided.

Hyperlinks with a separated target definition allow us to place the URL after
label. They are easier to update and independent of the text, for example:

`Gitg`_ is a great tool to visualize a GIT tree.

.. _Gitg: https://wiki.gnome.org/Apps/Gitg/

Follow these guidelines when inserting hyperlinks:

* The labels for hyperlinks must be grammatically correct and unique within
  the file.

* Do not create labels for hyperlinks using: link, here, this, there, etc.

* Add all target definitions at the end of the file containing the
  hyperlinks.

Use this template to add a hyperlink with a separated definition:

.. code-block:: rst

The state of `Oregon`_ offers a wide range of recreational activities.

The include directive 
*********************

Clear Linux documentation also uses the ``.. include::`` 
directive to include a portion of another reST file. 

Use the ``.. include::`` directive to show a select portion of :ref:`rest`, as shown below. 

.. code-block:: console

   .. include:: rest.rst
      :start-after: incl-restructured-text-overview:
      :end-before: incl-restructured-text-overview-end:

In this example, note that you must: 

* Create a `target` that appears directly above a header (ease of inclusion)
* Ensure that the target is unique, as explained in :ref:`target <internal-cross>`
* Use a `:` at the end of the value of `start-after` and `end-before`. 

Following is the actual inclusion of the rest.rst file: 

.. include:: rest.rst
   :start-after: incl-restructured-text-overview:
   :end-before: incl-restructured-text-overview-end:


.. _Oregon: http://traveloregon.com/
