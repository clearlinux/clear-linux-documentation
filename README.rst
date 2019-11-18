Documentation build instructions
################################

.. todo add comment re not using standards here.

`Clear Linux\* OS documentation`_ is written using `reStructuredText`_ and
built using `Sphinx`_. Follow the instructions in this README to build the
documentation locally for development and testing.

Please make yourself familiar with our `contribution guidelines`_ before
submitting a contribution.

Clone the documentation repository
**********************************

Clone the documentation repository to your local machine.

.. code-block:: bash

   git clone https://github.com/clearlinux/clear-linux-documentation

Requirements
************

Make sure you have Python 3 installed to start.

The Sphinx documentation provides `instructions for installing Sphinx`_
on various platforms.

Use pip3 to install additional Python dependencies listed in the
requirements.txt file found in the repository:

.. code-block:: bash

   pip3 install -r requirements.txt

Run the build
*************

We build our documentation using Sphinx. In the source directory of your
local clear-linux-documentation repository, preview changes to the
documentation by building the docs in the default language (English) by
running ``make html``:

.. code-block:: bash

   make html

.. code-block:: console

   sphinx-build -b html -d _build/doctrees   . _build/html
   Running Sphinx v1.8.0
   making output directory...
   .
   .
   .
   build succeeded, 0 warnings.

   The HTML pages are in _build/html.

   Build finished. The HTML pages are in _build/html.

Open one of the HTML pages found in ``source/_build/html`` in a web browser
to view the rendered documentation.

If you want to build the documentation exactly as seen on the website, use
``make py`` followed by ``make htmlall``. This builds some
external dependencies and all supported languages.

Additional help
***************

Cleaning up
===========

When testing changes in the documentation, make sure to remove the previous
build before building again by running ``make clean``:

.. code-block:: bash

   make clean

This will completely remove the previous build output.

Convenience script
==================

This bash script (Linux only) includes both ``make clean`` and
``make html``. It also starts a simple Python web server that
displays a preview of the site at http://localhost:8000 on your local machine.

.. code-block:: bash

   ./checkwork.sh

To stop the web server simply use ``ctrl-c``.

.. _Clear Linux\* OS documentation:  https://docs.01.org/clearlinux/
.. _Sphinx: http://sphinx-doc.org/
.. _reStructuredText: http://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html
.. _contribution guidelines: https://docs.01.org/clearlinux/latest/collaboration/collaboration.html
.. _instructions for installing Sphinx: https://www.sphinx-doc.org/en/master/usage/installation.html

