.. _documentation:

Documentation contribution guidelines
#####################################

The |CLOSIA| documentation contribution guidelines provide detailed information
about the scope and purpose of the documentation, the accepted writing style,
and the markup used.

The |CL| documentation is hosted in GitHub and welcomes community
contributions. This guide provides rules to write
:ref:`clear, concise<basic>`, and :ref:`consistent content<structures>`. Our
documentation is written using ReStructuredText and we provide
:ref:`examples, templates, and best practices<rest>` for that markup.

To contribute, follow the standard `GitHub flow`_:

#. Clone the `Clear Linux documentation repository`_.

#. Create your own fork of the repository.

#. Create a branch for your contribution.

#. Add your commits.

#. Open a pull request.

#. Discuss, review, and update your contributions.

#. Once the maintainer approves, your contribution is merged and published as
   part of the `documentation section`_.

The |CL| technical content is written in simple American English and our
:ref:`language` contains detailed information on that standard.

This guide includes the following sections:

.. toctree::
   :maxdepth: 2

   basic
   structures
   rest
   language


Scope
*****

The |CL| documentation is divided in five sections:

* **Get started:** Information about installing Clear Linux.
* **Concepts:** Detailed technical information about our features.
* **Guides:** Step-by-step instructions to complete common tasks and
  configuration.
* **Tutorials:** Step-by-step instructions to complete the installation and
  configuration of the tools needed for a specific use case.
* **Reference:** Information providing additional context or details.

If you are unsure on which section to use for your contribution, send an
email to our `mailing list`_ at: dev@lists.clearlinux.org Include the outline
of the contribution you are planning and a brief description of its intended
purpose and scope.

This style guide applies to the following technical content:

* Commit messages
* Technical presentations
* All documents in ReStructuredText within and without the documentation
  repository
* In-code comments
* Release notes

We are always grateful to receive content contributions and are happy to help
via our mailing list or our IRC channel, #clearlinux. If you have found a
problem with one of our documents, please file a bug report. Use our
:ref:`bug-report` to submit the bug.

Tone and audience
*****************

The tone of the |CL| documentation should be clear, concise, confident, and
courteous. We write for our peers and want to be familiar. Use the second
person, you or we, and active voice, we configure or you run, for example.
Remain professional in your writing and carry an undertone of cordiality,
respect, and cooperation.

Assume your audience has about the same level of technical understanding and
expertise as you did when you first started collaborating. Do not talk down to
our readers but do not assume they know everything about the subject.
Offer brief explanations or summaries of "common knowledge" if a
significant portion of readers might benefit.

All contributions must follow our :ref:`code-of-conduct`.

Methodology
***********

This guide differs from other style guides and contains additional material
not found in those sources.

To research a style question, look for the answer in this guide
first. If the question is not answered here, send your question to the
`mailing list`_ at: dev@lists.clearlinux.org.

If the question is answered in the existing style guide or dictionary,
the solution is implemented and enforced as described.

References
**********

In creating and refining the policies in this document, we consulted the
following sources for guidance:

* The Chicago Manual of Style (15th edition), The University of
  Chicago Press;
* Merriam-Webster Dictionary;
* Microsoft Manual of Style for Technical Publications, Microsoft
  Press;
* Microsoft Press Computer Dictionary, Microsoft Press; and
* Read Me First!, Oracle Technical Publications.

These sources do not always concur on questions of style and usage; nor do we
always agree with these sources. In areas where there is disagreement, the
decisions are explained in the respective section.

This guide takes precedence over all other style guides in all cases. In
cases where the guide does not address the issue at hand, please report the
issue to the `mailing list`_ using our :ref:`bug-report`.

Use the Merriam-Webster's Collegiate Dictionary to determine correct
spelling, hyphenation, and usage.

.. _mailing list: https://lists.clearlinux.org/mailman/listinfo/dev
.. _GitHub flow: https://guides.github.com/introduction/flow/
.. _documentation section: https://clearlinux.org/documentation
.. _Clear Linux documentation repository:
   https://github.com/clearlinux/clear-linux-documentation
