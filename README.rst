Documentation Build Instructions
================================

ClearLinux Docs are written in :abbr:`ReStructuredText (ReST)` AKA ``.rst``, which
makes for easily-parsable, command-line readable, indexed and search-friendly
documentation and APIs.  

Building with `Sphinx`_, however, requires a few prerequisites: 

* `GNU make`_ 
* `Python`_ 
* `PIP`_  

The instructions for installing these varies according to OS.  On a basic
out-of-the-box Ubuntu-like (which usually has Python installed by default),
you might need something like:

.. codeblock:: shell-session

   $ sudo apt-get install python-pip
   $ sudo pip install -U sphinx sphinx-autobuild

.. codeblock:: shell-session 
	
	$ python -c 'print __import__("sphinx").__version__'
	  1.3.1

Dependencies fulfilled, let's now clone that gitlab repo: 

.. codeblock:: shell-session

	$ git clone git@clrgitlab.intel.com:clr-documentation/project-docs.git
	Cloning into 'project-docs'...
	remote: Counting objects: 631, done.
	remote: Compressing objects: 100% (583/583), done.
	remote: Total 631 (delta 349), reused 108 (delta 35)
	Receiving objects: 100% (631/631), 2.10 MiB | 0 bytes/s, done.
	Resolving deltas: 100% (349/349), done.
	Checking connectivity... done.

Before running Sphinx, we need to correct some of the problems in the Gitlab repo.
Running :command:`make` straightaway from our clone won't work.  We need to delete the
existing conf.py file and also rename the existing index file so it can generate a new one
with the correct parameters. These files in the Gitlab repo are remnant of a build on a Windows
box, and they don't quite work on Linux. These should be removed from ``master`` eventually.

.. codeblock:: shell-session

	$ cd project-docs/
	$ ls
	make.bat  Makefile  source/
	$ rm -rf Makefile make.bat
	$ rm -rf source/conf.py 
	$ mv source/index.rst source/oldindex.rst


In the cloned source directory, we have all the .rst files we need to build the docs.  We 
run a native instance of :command:`sphinx-quickstart`. The program will run you through
a series of questions. The main things to be conscious of here:

* Tell it to use the existing :file:`source/` directory as the Root path for 
  the documentation; this is what it looks in, in order to generate the HTML
* It's better to tell it to **not** separate the source and build directories; the Sphinx
  will generate *another* :file:`source/` directory, which can be confusing. 

What follows here is a log from a successful :command:`sphinx-quickstart` build started from 
within the :file:`project-docs/` directory.

.. codeblock:: shell-session

	$ sphinx-quickstart
	Welcome to the Sphinx 1.3.1 quickstart utility.

	Please enter values for the following settings (just press Enter to
	accept a default value, if one is given in brackets).

	Enter the root path for documentation.
	> Root path for the documentation [.]: source/

	You have two options for placing the build directory for Sphinx output.
	Either, you use a directory "_build" within the root path, or you separate
	"source" and "build" directories within the root path.
	> Separate source and build directories (y/n) [n]: n

	Inside the root directory, two more directories will be created; "_templates"
	for custom HTML templates and "_static" for custom stylesheets and other static
	files. You can enter another prefix (such as ".") to replace the underscore.
	> Name prefix for templates and static dir [_]: 

	The project name will occur in several places in the built documentation.
	> Project name: ClearLinux Docs
	> Author name(s): Intel OTC

	Sphinx has the notion of a "version" and a "release" for the
	software. Each version can have multiple releases. For example, for
	Python the version is something like 2.5 or 3.0, while the release is
	something like 2.5.1 or 3.0a1.  If you don't need this dual structure,
	just set both to the same value.
	> Project version: 1.0.0
	> Project release [1.0.0]: 1.0.0

	If the documents are to be written in a language other than English,
	you can select a language here by its language code. Sphinx will then
	translate text that it generates into that language.

	For a list of supported codes, see
	http://sphinx-doc.org/config.html#confval-language.
	> Project language [en]: en

	The file name suffix for source files. Commonly, this is either ".txt"
	or ".rst".  Only files with this suffix are considered documents.
	> Source file suffix [.rst]: .rst

	One document is special in that it is considered the top node of the
	"contents tree", that is, it is the root of the hierarchical structure
	of the documents. Normally, this is "index", but if your "index"
	document is a custom template, you can also set this to another filename.
	> Name of your master document (without suffix) [index]: 

	Sphinx can also add configuration for epub output:
	> Do you want to use the epub builder (y/n) [n]: n

	Please indicate if you want to use one of the following Sphinx extensions:
	> autodoc: automatically insert docstrings from modules (y/n) [n]: n
	> doctest: automatically test code snippets in doctest blocks (y/n) [n]: n
	> intersphinx: link between Sphinx documentation of different projects (y/n) [n]: n
	> todo: write "todo" entries that can be shown or hidden on build (y/n) [n]: n
	> coverage: checks for documentation coverage (y/n) [n]: n
	> pngmath: include math, rendered as PNG images (y/n) [n]: n
	> mathjax: include math, rendered in the browser by MathJax (y/n) [n]: y
	> ifconfig: conditional inclusion of content based on config values (y/n) [n]: y
	> viewcode: include links to the source code of documented Python objects (y/n) [n]: y

	A Makefile and a Windows command file can be generated for you so that you
	only have to run e.g. `make html' instead of invoking sphinx-build
	directly.
	> Create Makefile? (y/n) [y]: y
	> Create Windows command file? (y/n) [n]: n

	Creating file source/conf.py.
	Creating file source/index.rst.
	Creating file source/Makefile.

	Finished: An initial directory structure has been created.

	You should now populate your master file source/index.rst and create other documentation
	source files. Use the Makefile to build the docs, like so:
	   make builder
	where "builder" is one of the supported builders, e.g. html, latex or linkcheck.

Finally are we ready to run :command:`make`.  Be sure to :command:`cd` to the :file:`source/`
directory before running :command:`make` . 

.. codeblock:: make

	$ make html
	sphinx-build -b html -d _build/doctrees   . _build/html
	Running Sphinx v1.3.1
	making output directory...
    	.
    	.
    	.
	build succeeded, 9 warnings.

	Build finished. The HTML pages are in _build/html.

Open one of these pages in a web browser to view the rendered documentation.  You can copy the
contents of the oldindex.rst into the generated index file, re-run :command:`make`, to generate
the new HTML, and your local Table of Contents should index and update accordingly.      

For extra help and tips for contributing documentation which will render beautifully on websites,
despite being written in .rst see:  `Theming_Sphinx`_. 

.. _GNU make: https://www.gnu.org/software/make/
.. _Python: https://www.python.org/
.. _PIP: https://pypi.python.org/pypi/pip/
.. _Theming Sphinx: https://github.com/otcshare/tcs-hub/blob/master/theming-sphinx.rst