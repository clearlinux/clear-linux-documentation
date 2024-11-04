=======
os-core
=======

----------------------------------------------------
Base files for Clear Linux OS for Intel Architecture
----------------------------------------------------

:Copyright: \(C\) 2017 Intel Corporation, CC-BY-SA-3.0
:Manual section: 7


SYNOPSIS
========

* ``init``
* ``root filesystem``
* ``shell``


DESCRIPTION
===========

os-core provides a minimal base for the Clear Linux OS for Intel
Architecture. It contains required utilities for running the init
program systemd, letting users log in and run bash shell commands. The
core also contains pieces of packages that are required to run any
other package in the distribution.

This is the only required bundle for Clear Linux OS and can not be
removed as all other bundles depend upon it.


SEE ALSO
========

`<https://clearlinux.org/documentation/>`_
