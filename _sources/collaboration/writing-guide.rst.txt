.. _writing-guide:

Writing guide
#############

We want our documentation to be easy to read and understand. This document
describes guidelines for writing documentation that is clear, concise,
confident, and courteous.

Refer to :ref:`structure-formatting` for details on organizing content and how
we use reStructuredText and Sphinx.

.. contents:: :local:
   :depth: 1

Use simple English
******************

Write using simple English: Be brief and communicate only the information that
is needed. Be friendly and informative. Emphasize clarity and avoid
unnecessary complicated or technical terms. Make the content accessible to
non-native speakers.

Be brief
========

Use short sentences and paragraphs. Stick to the principle of one main
idea per sentence, plus one additional point if needed. Each paragraph
should address one main idea. Remember the basic structure of a paragraph:
Introduction, body, and conclusion.

Be friendly
===========

We write for our peers and want to be familiar. Take a personal tone as if you
were speaking directly to the reader. Use "you" to address the reader and "we"
to refer to our view. Be professional, respectful, and cooperative.

Assume your audience has the same level of technical understanding and expertise
as you did when you first started collaborating. Do not talk down to our
readers, but also do not assume they know everything about the subject. Offer
brief explanations or summaries of common knowledge if a significant portion of
readers might benefit.

Use simple words
================

Use simple words to increase reader comprehension and reduce ambiguity. Follow
our tips for making good word choices:

* **Avoid jargon**: Write for your audience, using everyday language where
  possible, and technical terms where appropriate. Avoid clichés, idioms, and
  metaphors.
* **Be consistent**: Use one term for each concept or action and use it
  consistently.
* **Avoid "fancy" words and phrases**: If there is a simpler word or phrase,
  use it.

  For example:

  ===================     ===================
   Use this                Not this
  ===================     ===================
   start, begin            commence
   so                      consequently
   more than               in excess of
   if                      in the event of
   before                  prior to
   if you want             should one wish
   use                     utilize
   example                 instance
  ===================     ===================

Avoid overuse of product name
=============================

Use product names only when necessary. Typically, you can rewrite sentences to
remove the product name with no change in meaning, which keeps the content
concise and scannable.

Avoid using the product name in page titles and headings.

.. _scannable-content:

Make content scannable
**********************

Organize your content to make it scannable for the reader, which helps them find
what they need quickly, and to understand the information more efficiently.

* **Put the most important content first.** Make sure your introduction clearly
  communicates what the reader can find on the page. Present the point of the
  document first, and organize supporting information towards the end of the
  page.
* **Write scannable headings.** Expect readers of documentation to skim and scan
  the content, and to leave if they don't find what they need quickly. Good
  headings add organization to your content and help the reader to find and
  understand content more effectively. Follow our guidelines for writing
  effective `Headings`_.
* **Write great link text.** Great link text tells the reader what they can
  expect when they click on a link. It also helps make the page more scannable.
  Follow our guidelines for writing `Link text`_.

Headings
========

Use these guidelines to write effective headings:

* **Be concise and descriptive.** Use only the words necessary to describe the
  section.
* **Use sentence case.** Capitalize only the first word and proper nouns in a
  heading.
* **Avoid punctuation.** Unless your heading is a question, don't use sentence
  punctuation in headings.
* **Use parallel structure.** Headings at the same level should use the same
  grammatical pattern. This provides structure to the document and helps users
  find information more easily. See :ref:`parallelism`.
* **Use strong verbs.** Strong, active verbs get to the point. Avoid -ing verbs,
  such as *Running*, *Testing*, etc.

For example, two headings at the same level:

**Use this:** ::

  Install software

  Configure software

**Not this:** ::

  Installing the Software on the Platform

  Software Configuration.

Link text
=========

All links in content should follow these guidelines:

* **Write descriptive link text**: Link text should describe where the link
  goes, without having to read the surrounding text.
* **Keep link text concise**: Use only the words needed to accurately describe
  the destination.
* **Use unique link text**: Each link on a page should be unique. If users see
  the same link text twice on a page, they'll assume it goes to the same place.
* **Start link text with keywords**: Frontload the link text with the most
  important words to help users scan the text.
* **Avoid generic text**: Don't use generic, uninformative link text such as
  "click here" or "read more".

For example:

**Use this:** ::

  For more information about dogs, read the `dog wiki article`_.

**Not this:** ::

  For more information about dogs, `click here`_.

Use strong verbs
****************

Passive verbs make writing stuffy and formal. Use strong verbs to get to the
point and avoid unnecessary words and phrases.

Use imperatives
===============

Commands, also called imperatives, are the fastest and most direct way of giving
someone instructions. For example:

**Use this:** ::

  Send it to me.

**Not this:** ::

  I would appreciate it if you would send it to me.

Use present tense
=================

Use simple present tense instead of future tense for most text. Search for the
words "will" or "shall" to find future tense instances. Future tense is
acceptable for conditional statements, such as in a caution or a warning. For
example:

**Use this:** ::

  The system operates at a nominal temperature of 180 degrees Fahrenheit.

**Not this:** ::

  The system will operate at a nominal temperature of 180 degrees Fahrenheit.

Avoid nominalizations
=====================

Avoid nominalizations, which are nouns formed from verbs.

For example:

===================== =====================
 Verb 				         Nominalization
===================== =====================
 complete  			       completion
 provide  			       provision
 fail  				         failure
 install  			       installation
===================== =====================

For example:

**Use this:** ::

  We discussed the matter.

**Not this:** ::

  We had a discussion about the matter.

Or:

**Use this:** ::

  IT has installed the software.

**Not this:** ::

  IT has completed the installation of the software.

Avoid words ending in -ing
==========================

Avoid using words ending in -ing unless they are part of a technical name. For
example:

**Use this:** ::

  There is no way to verify this.

**Not this:** ::

  There is no way of verifying this.

Use the active voice
====================

Use active voice whenever possible to show who or what is performing an
action.

* Active voice follows standard English word order: SUBJECT–VERB–OBJECT
  (where the OBJECT is optional).
* Passive voice reverses the order and weakens the verb: OBJECT–be VERB–by
  SUBJECT (where the OBJECT is optional).

For example:

**Use this:** ::

  I made a mistake.

**Not this:** ::

  A mistake was made. *(By whom?)*

Or:

**Use this:** ::

  We released version 2.0 in June.

**Not this:** ::

  Version 2.0 was released in June.

Avoid long noun phrases
***********************

Noun phrases (a noun and other words that describe or modify it) can be
difficult to understand. Try to limit the number of modifiers in a noun phrase
to two. For example:

**Use this:** ::

  Integration policies for power management mechanisms.

**Not this:** ::

  Power management mechanism integration policies.

.. _parallelism:

Parallelism
***********

Parallelism refers to the practice of using similar patterns of grammar, and
sometimes length, to coordinate words, phrases, and clauses.

Use parallel construction in lists. The table below shows some unparallel
structures and how they can be made parallel with a little rewording.

+----------------------------------+----------------------------------+
| Parallel (do)                    | Unparallel (don't)               |
+==================================+==================================+
| 1. Mount the panel.              | 1. Mount the panel.              |
| 2. Install the battery.          | 2. Battery installation.         |
| 3. Wire the keypad.              | 3. Wiring the keypad.            |
+----------------------------------+----------------------------------+
| I like practicing my accordion,  | I like practicing my accordion,  |
| reading sci-fi, and eating       | reading sci-fi, and to eat       |
| peanut butter and pickle         | peanut butter and pickle         |
| sandwiches.                      | sandwiches.                      |
+----------------------------------+----------------------------------+
| For breakfast he likes coffee    | For breakfast he likes coffee    |
| and bacon.                       | and to fry bacon.                |
+----------------------------------+----------------------------------+
| Apples or bananas are a good     | Apples or a banana are a good    |
| snack.                           | snack.                           |
+----------------------------------+----------------------------------+

Grammar and punctuation
***********************

This section covers common grammatical topics relevant to our
documentation. For detailed explanations of correct grammar and punctuation,
use one of our :ref:`preferred references <references>`.

Capitalization
==============

The capitalization style for all documentation is sentence case. Words should
only be capitalized when they are proper nouns or refer to trademarked product
names.

.. note::
   Do not capitalize a word to indicate it is more important than other
   words. Never change the case of variable, function or file names - always
   keep the original case.

Menu capitalization
-------------------

When referring to software menu items by name, use the same capitalization as
seen in the actual menu.

A few other tips when referring to menu items:

* Reference the specific menu item using "Select :menuselection:`File --> New`."

* Put the option to be selected last. "Select
  :menuselection:`View --> Side Bar --> Hide Side Bar`"

* Do not include more than 3 navigation steps in a menu selection. If
  more than three steps are needed, divide the steps using
  ``:guilabel:`` or ``:menuselection:``.

  For example: "Go to :guilabel:`File` and select
  :menuselection:`Print --> Print Preview --> Set Up`."

Software version capitalization
-------------------------------

When listing software or hardware version numbers, the word “version” or letter
"v" are lowercase. The v is closed with the number (no period).

For example:

* Widget Pro version 5.0
* Widget Master v2.1.12

Contractions
============

Avoid using contractions, such as it's, they're, and you're, because they may be
unclear to non-native English-speaking audiences.

Quotation marks
===============

Follow these guidelines for quotation marks:

* Restrict use of quotation marks to terms as terms.
* Do not use quotation marks for emphasis; use *italics* for emphasis.
* Avoid using single-quote marks.

Commas and colons
=================

This section addresses common use of commas, semicolons, and colons in our
documentation. Refer to one of our :ref:`preferred references <references>`
for further details.

Use the serial comma
--------------------

When writing a series of items, use the serial comma before the final *and* and
*or* to avoid confusion and ambiguity. For example:

**Use this:** ::

  Mom, Dad, and I are going to the game.

**Not this:** ::

  Mom, Dad and I are going to the game.

.. _click here: https://en.wikipedia.org/wiki/Dog
.. _dog wiki article: https://en.wikipedia.org/wiki/Dog
