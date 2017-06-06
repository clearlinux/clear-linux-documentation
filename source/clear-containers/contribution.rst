.. _cc-contribution:

Contribute to the Intel® Clear Containers OCI runtime
#####################################################

The |CC| :abbr:`OCI (Open Container Initiative)` runtime is an open source
project licensed under the `GPL v2 License`_ .

Coding styles
=============

C code
------

The |CCR| follows code style similar to that used by the Linux kernel
based on the K&R coding style with function names in column 0 and variable
names aligned in declarations.

Additionally, ensure your contributions adhere to the following guidelines to
be merged:

* Write the code as cleanly and as readable as possible.
* Use ``goto`` where possible to simplify error handling and to avoid
  duplicated code.
* Document all functions with a Doxygen header.
* Check all function parameters.
* Ensure all functions return an error when an unexpected value is found.

To comply with the style, set up your editor as follows:

* GNU Emacs: Without auto-newline enabled, apply the following configurations:

.. code-block:: console

   (defun cc-oci-runtime-c-mode-common-hook ()
    (c-set-style "k&r")
    (setq indent-tabs-mode t
          c-basic-offset 8))

* VIM: Use the default configuration and set the following option to fix the
  labels in switch statements:

.. code-block:: console

   setlocal cinoptions=:0

.. note:: ``indent`` can be used to reformat code in a different style:

   .. code-block:: console

      indent -kr -i8 -psl

Go code
-------

The |CCR| follows the Go style enforced by ``gofmt``. Additionally, the
`Go Code Review document`_ provides a few common errors to avoid.

Certificate of origin
=====================

To get a clear contribution chain of trust, the runtime uses the
`signed-off-by language`_ used by the Linux kernel project.

Commit message format
=====================

Beside the signed-off-by footer, we expect each patch to comply with the
following format:

.. code-block:: console

   Subsystem: Change summary (no longer than 75 characters)

   More detailed explanation of your changes: Why and how. Wrap it to 72
   characters.

   Signed-off-by: <contributor@foo.com>

For additional information we recommend `How to Write a GIT Commit Message`_
and the pertinent `Linux Kernel documentation`_.

An example from our repository:

.. code-block:: console

   OCI: Ensure state is updated when kill fails.

   Killing a container involves a number of steps. If any of these fail,
   the container state should be reverted to it's previous value.

   Signed-off-by: James Hunt <james.o.hunt@intel.com>

The body of the message should not be a continuation of the subject line. It
is not used to extend the subject line beyond the length limit. Both body and
subject line should stand alone and be complete sentences or paragraphs.

Each commit should fix one thing. Smaller commits are easier to review and
are more likely to be accepted and merged. Smaller commits make problems more
likely to be picked up during review.

Pull requests
=============

The |CCR| accepts `GitHub pull requests`_. GitHub provides a
`basic introduction to pull requests`.

When submitting a :abbr:`PR (Pull Request)`, comply with the same guidelines
for commit messages. This includes using a prefix for the title with the
subsystem name. GitHub by default copies the message from the first commit.
Please ensure the message is accurate and complete for the whole PR. This
message will become part of the repository's log as the merge message.

Your PR might get some feedback and comments requiring some rework. To rework
your branch we recommend you work on a new clean state and 'force push' it to
GitHub. GitHub understands this action and does sensible things with the
comment history. Do not pile commits on commits to rework your branch. All
relevant information provided in the GitHub comments section must be included
in your commits. Ultimately, the repository log documents the code changes,
not in the GitHub comments.

Adam Spiers provides more information on the GitHub `'force push' workflows`_.

PRs can contain more than one commit - use as many commits as needed to
implement the PR. Each PR should cover only one topic. If different items are
mixed in your commits or PRs, you will most likely be asked to rework them.

Reviews
=======

Before PRs are merged into the main code base, they will be reviewed. Anybody
can review any PR and leave feedback. We encourage you to perform code
reviews.The |CCR| runs a `rotational gatekeeper schedule`_. The gatekeepers
are ultimately responsible for merging the PRs into the main code base.

Using the "acknowledge" system, people can note if they agree or disagree
with a PR. Using some automated systems, GitHub will spot common acknowledge
patterns. These patterns include placing any of following at the beginning of
a comment line:

* LGTM
* lgtm
* +1
* Approve

Contact
=======

The |CCR| community can be reached through its IRC channel
and a dedicated mailing list:

* IRC: ``#clearcontainers @ freenode.net``.
* The `mailing list`_

Issue tracking
==============

If you have identified a problem, please let us know. Use the IRC channel to
quickly and informally bring attention to an issue. The `mailing list`_
is also available as a more durable communication channel.

If the bug has not been documented already, by all means
`open an issue in GitHub`_. Issues provide visibility to the problem for us to
work towards resolving it.

Closing issues
==============

Issues can be closed manually by adding the fixing commit SHA1 to the issue's
comments or automatically by adding the ``Fixes`` keyword to your commit
message, for example:

.. code-block:: console

    Fix handling of semvers with only a single pre-release field

    Fixes #121

    Signed-off-by: James Hunt <james.o.hunt@intel.com>

GitHub will then automatically close issue #121 when it
`parses the commit message`_.

Next steps
==========

All your contributions to the |CCR| code are most welcome. If you are looking
for a place to start, check our list of `open issues`_. Alternatively, you
can head to our list of `pull requests`_ and review some of the pending code
changes.

.. _GPL v2 License:
   https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html

.. _Go Code Review document:
   https://GitHub.com/golang/go/wiki/CodeReviewComments

.. _signed-off-by language:
   https://01.org/community/signed-process

.. _How to Write a GIT Commit Message:
   http://chris.beams.io/posts/git-commit/

.. _Linux Kernel documentation:
   https://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git/tree/Documentation/SubmittingPatches

.. _GitHub pull requests:
   https://GitHub.com/01org/cc-oci-runtime/pulls

.. _basic introduction to pull requests:
   https://help.GitHub.com/articles/using-pull-requests/

.. _'force push' workflows:
   http://blog.adamspiers.org/2015/03/24/why-and-how-to-correctly-amend-GitHub-pull-requests/

.. _rotational gatekeeper schedule:
   https://GitHub.com/01org/cc-oci-runtime/wiki/GateKeeper-Schedule

.. _mailing list: https://lists.01.org/mailman/listinfo/cc-devel

.. _open an issue in GitHub:
   https://GitHub.com/01org/cc-oci-runtime/issues/new

.. _parses the commit message:
   https://help.GitHub.com/articles/closing-issues-via-commit-messages/

.. _open issues:
   https://github.com/01org/cc-oci-runtime/issues

.. _pull requests:
   https://github.com/01org/cc-oci-runtime/pulls
