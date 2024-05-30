.. _tutorial-ratings:

Tutorial difficulty ratings
###########################

Tutorial difficulty ratings provide a simple way to start using and developing with |CL-ATTR|. If you're new to the distro, we suggest starting with ``Easy`` tutorials and  working towards the more ``Difficult``. Ratings not only expose learning paths but also provide a starting point from which to advance or improve use cases, so be sure to :ref:`share your insights <collaboration>`. Three main metrics help us to determine how to rate a tutorial: 

.. contents::
   :local:
   :depth: 1

The sum total of these metrics, the rating shown in Figure 1, represents the
ability to successfully complete a tutorial based on skill level, balanced against the risk of failure.   

.. figure:: /_figures/reference/tutorial-ratings-01.svg
   :scale: 100%
   :alt: Tutorial difficulty ratings

   Figure 1: Tutorial difficulty ratings

Time and complexity
*******************

Are there about 8 or more *complex* steps? *Complex steps* are those that: 

* Require more than one action 
* Require external reading/review
* Include explanation or context
* Give alternative(s) 

This metric factors in the cognitive load and its impact on a user. 

User experience level
*********************

Our tutorials primarily target two types of Linux users.

**Experienced** A Linux\* user who is familiar with common topics like userspace, networking, sudo privileges, services, and more. 

**Advanced** A Linux user who is beyond Experienced and is familiar with most sysadmin and programming topics. 

This metric establishes a starting point for skills, based on user
experience. 

Impact of failure
******************

The impact of failure calculates the risk of failing to complete a tutorial as a result of entering incorrect data or configuration, or failing to follow the steps in the given order. We estimate the potential state of a system, given these failure scenarios and their severity. This metric also factors in the ability to troubleshoot and recover when faced with errors. Therefore, the final impact incorporates the previous two metrics while it helps to predict an appropriate difficulty rating. 

* Will impact of errors be inconsequential? ``Easy``
* Will impact of errors cause inconvenience (but system still works)? ``Moderate``
* Will impact of errors cause system failure (difficult to recover)? ``Difficult``
