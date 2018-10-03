.. _security:

OS Security 
*************************

|CL-ATTR| aims to make systemic and layered security-conscious decisions
that are both performant and practical. This security philosophy is rooted 
within the project's codebase and operating culture.


.. contents:: :local:
   :depth: 2



Security in Updates
===================

The |CL| team believes in the benefits of 
software security through open sourcing, incremental updates, and 
rapidly resolving known security advisories.
 


The latest Linux codebase
-------------------------

|CL| uses the newest version of the Linux kernel which allows the operating 
system to leverage the latest features from the upstream Linux kernel, 
including security fixes. 


 

Automated Effective Updating
----------------------------

|CL| is incrementally updated multiple times per day.

This `rolling release model`_ allows |CL| to consume the latest security
fixes of software packages as soon as they become available. 
There is no waiting for major or minor releases on |CL|. 

An update is not effective if it is just simply downloaded onto a system. 
It needs to be obtained *AND* ensured that the new patched copy is being
used; not an older copy loaded into memory. |CL| will let you know when a 
service needs to be rebooted or do it for your automatically after 
a software update, if desired.


In |CL| updates are delivered automatically, efficiently, 
and effectively. For more information see 
`documentation about Software Updates`_ in |CL|.

 



Automated CVE Scanning and Remediation
--------------------------------------

The sheer number of software packages and security vulnerabilities is growing 
exponentially. Repositories of Common Vulnerabilities and Exposures (CVEs) 
and their fixes, if known, are published by :abbr:`NIST` in a 
National Vulnerability Database \ |NVD|\  and at \ |MITRE|\  .


|CL| employs a proactive and measured approach to addressing known
and fixable :abbr:`CVEs (Common Vulnerabilities and Exposures)`.
Packages are automatically scanned against 
:abbr:`CVEs (Common Vulnerabilities and Exposures)` daily, and security 
patches are deployed as soon as they are available. 

These combined practices minimize the amount of 
time |CL| systems are exposed to unnecessary security risk.

 



Security in Software
====================


Minimized attack surface
-------------------------

|CL| removes legacy, unneeded, or redundant standards and
components as much as possible to enable the use of best known security 
standards. Below are some examples: 

* `RC4`, `SSLv3`, `3DES`, and `SHA-1` ciphers which have had known 
  vulnerabilities, have been explicitly disabled within many |CL| packages to 
  avoid their accidental usage. 

* Services and subsystems which expose sensitive system information 
  have been removed such as the `finger` and `tcpwrappers`.

* `SFTP` has been disabled by default due to security 
  considerations. See the `openssh-server reference page`_ for more details. 


Verified trust
--------------

|CL| encourages the use of secure practices such as encryption
and digital signature verification throughout the system and discourages blind
trust. Below are some examples: 

* All update operations from swupd are transparently encrypted and checked 
  against the |CL| maintainers' public key for authenticity. 
  More information can be found in this blog post: 
  `blog post about swupd security`_ 

* Before being built, packages available from |CL| verify checksums and 
  signatures provided by third party project codebases and maintainers.

* |CL| features a unified certificate store, `clrtrust`_ which comes 
  ready to work with well-known Certificate Authorities out of the box. 
  `clrtrust`_ also offers an easy to use command line interface for managing 
  system-wide chains of trust, instead of ignoring foreign certificates. 


 



Compiled with secure options
----------------------------

While |CL| packages are optimized for performance on 
Intel® architecture, security conscious kernel and compiler options are 
sensibly taken advantage of. Below are some examples: 

 
* Kernels shipped with |CL| are signed and disallow the usage of 
  custom kernel modules to maintain verifiable system integrity.

* `Address space layout randomization (ASLR)`_ and 
  `Kernel address space layout randomization (KASLR)`_  are kernel features
  which defend against certain memory based attacks. 
  More information can be found in a `blog post about PIE executables`_ .

* `dm-verity`_ is a kernel mechanism readily available in |CL| 
  which verifies integrity of the devices being written to, like hard disks,
  to help ensure they have not been tampered with.  



  

Security in System Design
=========================

Simple, yet effective, techniques are used throughout the 
|CL| system design to defend against common attack vectors and enable
good security hygiene. Below are some examples: 


* Full disk encryption using `Linux Unified Key Setup`_ (LUKS)  is available 
  during installation.

* |CL| uses the PAM cracklib module to harden user login and password
  security resulting in: 

  - No default username or root password set out of the box with 
    |CL|, you will be asked to set your own password immediately.

  - Simple password schemes, which are known to be easily compromised,
    cannot be set in |CL|.

  - A password blacklist, to avoid system passwords being set to
    passwords which have been compromised in the past.

* `Tallow`_, a lightweight service which monitors and blocks suspicious SSH 
  login patterns, is installed with the :command:`openssh-server` bundle. 
        





.. _`documentation about Software Updates`: https://clearlinux.org/documentation/clear-linux/concepts/swupd-about
.. _`cve-check-tool`: https://github.com/clearlinux/cve-check-tool
.. _`openssh-server reference page`: https://clearlinux.org/documentation/clear-linux/reference/bundles/openssh-server
.. _`blog post about swupd security`: https://clearlinux.org/blogs/security-software-update-clear-linux-os-intel-architecture
.. _`rolling release model`: https://en.wikipedia.org/wiki/Rolling_release
.. _`clrtrust`: https://github.com/clearlinux/clrtrust
.. _`Address space layout randomization (ASLR)`: https://en.wikipedia.org/wiki/Address_space_layout_randomization
.. _`Kernel address space layout randomization (KASLR)`: https://lwn.net/Articles/569635/
.. _`dm-verity`: https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/Documentation/device-mapper/verity.txt
.. _`SELinux`: https://github.com/SELinuxProject
.. _`Linux Unified Key Setup`: https://gitlab.com/cryptsetup/cryptsetup/
.. _`blog post about PIE executables`: https://clearlinux.org/blogs/recent-gnu-c-library-improvements 
.. _`Tallow`: https://github.com/clearlinux/tallow

.. |NVD| raw:: html

    <a href="https://nvd.nist.gov/" target="_blank">https://nvd.nist.gov/</a>

.. |MITRE| raw:: html

    <a href="https://cve.mitre.org/" target="_blank">https://cve.mitre.org/</a>

