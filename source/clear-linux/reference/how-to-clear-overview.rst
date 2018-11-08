.. _how-to-clear-overview:

How to Clear training overview
##############################

The existing Linux\* ecosystem can be challenging to users because of long
intervals between :abbr:`OS (operating system)` updates, which leads to large
update downloads. Users can also be frustrated when managing complicated
component dependencies. |CL-ATTR| solves these problems by:

*	Allowing you to update frequently, even multiple times per day
*	Preventing you from combining incompatible components

The |CL| team delivers technology advances with the |CL| OS and its tooling,
concepts, and content. The team has created training materials as a GitHub\*
project to get you up and running quickly.

The training provides complete details on the methods used to create updates
and how to deploy the updates to targets. The following items provide an
overview of these |CL| mechanisms:

*   Update server: an https-enabled web server where the content files are served
    as static content. |CL| periodically queries the data on the update server and
    determines whether updates are available. The update content files provide the
    data and metadata to perform the required actions.

*   Software delivery mechanism: :abbr:`swupd (software updater)`
    queries metadata from the update server and calculates what to do and which
    content to use.

*   Tools: `mixer-tools` software suite generates the update server content using |CL|
    official software update content, local bundle definitions, and local RPM files.

The training helps you create a customized OS that is based on |CL|. The
training content is self-contained and hosted on GitHub. You need a clean
|CL| installation and a functional network connection to complete the
training. For convenience, the project includes the training files you need
for the exercises.

We appreciate your feedback and comments, especially in the form of Pull
Requests. Please visit the `how-to-clear project`_ page to access the training
materials, open a ticket, or clone/branch the training and help us improve
|CL|.

.. _how-to-clear project: https://github.com/clearlinux/how-to-clear

