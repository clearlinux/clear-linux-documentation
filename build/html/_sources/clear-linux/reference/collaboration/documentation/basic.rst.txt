.. _basic:

Basic contribution guide
########################

This list compiles the most common format, markup, structure, and grammar
rules for your convenience. You can find more detailed information in the
referenced sections.

.. contents::
   :local:
   :backlinks: entry

Format
******

* Limit line length to 78 characters. The GitHub web interface forces this
  limitation for readability.

* Remove trailing white space from your documents.

* Use short sentences and paragraphs. Keep sentence length under 20 words.

* Use only lower case letters for filenames.

* Separate multiple words in filenames using dashes.

Markup
******

* Use the appropriate :abbr:`ReST (ReStructuredText)` roles for your content.
  See the `ReST primer`_ for the complete list of roles.

* Use the :abbr: role to define the first instance of an abbreviation, for
  example: :abbr:\`CL (Clear Linux)\`.

* Use hash-tags to underline the file's main title.

* Use asterisks to underline the file's first level headings.

* Use equal signs to underline the file's second level of headings.

* Use dashes to underline the file's third level of headings.

* Use labels to reference documentation sections. Do not reference
  sections with URLs. See :ref:`cross` for details.

* Don't use explicit URLs as links, for example https://clearlinux.org/.

* Always include descriptive link text. For example:
  Visit the `Clear Linux website`_. Do not use "here", "this", or similar
  references for link text.

Structure
*********

* All files must have a main title and up to three levels of headings.
  Restructure the content in multiple files as needed to comply.

* Use descriptive headings.

* Follow all headings with at least one paragraph of content. There should
  never be two consecutive headings.

* Separate the link and the target definition. All target definitions must be
  included at the end of the file. See :ref:`cross` for details.

* Use parallelism in headings, sentences, and lists. See our
  :ref:`parallelism` for details.

* Put conditional phrases first in cautions and warnings. For example:
  "If you do X, then Y will occur." See our :ref:`notices` guide.

* Place figures and tables immediately after related text.

* Place code or commands immediately after the leading text in a new line,
  see our :ref:`code`.

* Reference figures, code examples, and tables by number.
  For example, use "Figure 1," instead of "The figure above or below". See
  :ref:`cross` and :ref:`images`.

* Include at least one direct reference to any table or figure you add. See
  :ref:`tables`.

Grammar
*******

* Include only one main idea in a sentence. See :ref:`simple`.

* Limit the number of clauses you use to no more than two. See :ref:`simple`.

* Limit the number of sentences per paragraph to about six. See :ref:`simple`.

* Use strong verbs. See :ref:`simple`.

* Use action verbs. See :ref:`simple`.

* Avoid weak verbs like be, have, make, and do. See :ref:`simple`.

* Use short direct commands and avoid niceties such as the word
  "please".

* Use the present tense wherever possible and avoid past and future
  tense verbs. See :ref:`simple`.

* Use Active voice. Write, "Someone does something"; don't write,
  "Something is done by someone" or "Something is done." See :ref:`simple`.

* Use "we" for recommendations. Write "We recommend..." as opposed to
  "It is recommended...." See :ref:`simple`.

* Use "you" rather than "the user" in your instructions.

* Use short common English words whenever possible, see our :ref:`simple`
  guide.

* Avoid contractions. See :ref:`grammar`.

* Use articles such as 'a', 'an', and 'the' to reduce ambiguity.

Additional information
**********************

Learn more about the accepted rules of grammar, punctuation, and word use in
our :ref:`language`. If you are looking for tips on how to write shorter,
clearer, and more concise content, visit our :ref:`simple` guide.

.. _Clear Linux website: https://clearlinux.org/
.. _ReST primer: http://docutils.sourceforge.net/docs/user/rst/quickstart.html
