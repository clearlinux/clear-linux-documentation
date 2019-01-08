Documentation build instructions
################################

.. todo add comment re not using standards here.

`Clear Linux\* OS documentation`_ is written using `reStructuredText`_ and
built using `Sphinx`_. Documentation may be built locally for development and
testing purposes by following the instructions in this README.

Please make yourself familiar with our `contribution guidelines`_ before
submitting a contribution.

Requirements
************

Make sure you have Python and Sphinx installed. We use Python 3 and
Sphinx 1.7.5

The Sphinx documentation provides `instructions for installing Sphinx`_ on various
platforms.

Clone the documentation repository
**********************************

Once Sphinx is installed, clone the documentation repository to your
local machine.

.. code-block:: console

   $ git clone https://github.com/clearlinux/clear-linux-documentation

Run the build
*************

We build our documentation using . In the source directory of your
local clear-linux-documentation repository, build the documentation by running
**make html**:

.. code-block:: console

   $ make html
   >
   sphinx-build -b html -d _build/doctrees   . _build/html
   Running Sphinx v1.7.5
   making output directory...
   .
   .
   .
   build succeeded, 0 warnings.

   The HTML pages are in _build/html.

   Build finished. The HTML pages are in _build/html.

Open one of the HTML pages in a web browser to view the rendered
documentation.

When testing changes in the documentation, make sure to remove the previous
build before building again by running **make clean**:

.. code-block:: console

   $ make clean
   >
   rm -rf _build/*

This will completely remove the previous build output.

.. _Clear Linux\* OS documentation:  https://clearlinux.org/documentation
.. _Sphinx: http://sphinx-doc.org/
.. _reStructuredText: http://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html
.. _contribution guidelines: https://clearlinux.org/documentation/clear-linux/reference/collaboration
.. _instructions for installing Sphinx: https://www.sphinx-doc.org/en/master/usage/installation.html

