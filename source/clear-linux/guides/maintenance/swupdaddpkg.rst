.. _swupdaddpkg:

Create and add custom bundles to your upstream Clear Linux System
#################################################################

|CLOSIA| offers many curated bundles that you can install on your system to
create your desired capabilities. If the available upstream bundles do not
meet your needs, you can create and add your own custom bundles to your
system using one of two methods. Note: Upstream refers to the official version of |CL|.

The first method is to use the :ref:`mixer tool<mixer>` to create your own
|CL| image and adding your bundles to it.  Mixing your own |CL| image can
give you great control and flexibility, but you have to become your own OSV
and maintain your own releases and updates because you’ve forked from
upstream.  

The second method is to use the :command:`swupd-add-pkg` tool, which also makes
use of mixer to create custom bundles that you can add to your upstream |CL|
system.  In comparison, this method is simpler. It is a “light” forking from
upstream, which means you can continue to get upstream bundles and updates.
Also, if needed, you can revert your system back to 100% upstream in a
pinch. 

This guide shows you how to accomplish the second method by following these
steps:

#. Set up the workspace
#. Copy your custom RPM package to the workspace
#. Create a bundle with your custom RPM package
#. Migrate your |CL| system to your custom mix
#. Add your custom bundle to your system
#. Optional: Revert your system back to 100% upstream

Set up the workspace
********************

#. Log in and get root privileges: 

   .. code-block:: console

      $ sudo -s

#. Install the mixer bundle to enable mixer:
   
   .. code-block:: console 

      # swupd bundle-add mixer

#. Create the workspace:

   .. code-block:: console

      # swupd bundle-add mixer

Copy your custom RPM package to the workspace
*********************************************

.. note::

   You cannot simply use RPMs from other Linux distros on |CL|.  You must
   build RPMs specifically for |CL| in order for them to work properly.
   Follow the `Developer tooling framework for Clear Linux`_ on 
   on how to build RPMs.  

Copy your RPM to the workspace.

.. code-block:: console

   # cp [RPM] /usr/share/mix/rpms

Create a bundle with your custom RPM package
********************************************

Use the :command:`swupd-add-pkg` command to create a bundle with the RPM
package.

.. code-block:: console

   # swupd-add-pkg [RPM] [bundle-name]

To add more than one RPM to your previously-created bundle, repeat
the :command:`swupd-add-pkg` command and just change the RPM name.

.. note:: 
   
   The first time you run the :command:`swupd-add-pkg` command, mixer will
   create a new OS version by taking your current upstream |CL| version and
   multiplying it by 1000.  For example, if your upstream version is 21530,
   your custom version will be 21530000.  For each subsequent call to
   swupd-add-pkg, mixer will increment the version by 10.  For example,
   21530010, 21530020, etc. 

Migrate your |CL| system to your custom mix
*******************************************

Before your custom bundle can be used, you must “migrate” your |CL| system
to your custom mix to make them accessible.

.. code-block:: console
   
   # swupd update --migrate

After you migrate, you will notice that the version of your |CL| system will
switch over to your last custom version number as noted in the previous
section. 

You can continue to create new bundles with :command:`swupd-add-pkg` even
while you’re in your custom version of |CL|.  Just be sure to migrate again
to make your new bundles accessible.

Add your custom bundle to your system
*************************************

#. Get a listing of your newly-created bundle.

   .. code-block:: console

      # swupd bundle-list -a

   The listing will include all upstream bundles as well.

#. Add your bundle.

   .. code-block:: console

      # swupd bundle-add [bundle-name]

.. note:: 

   You can also update your system to the latest upstream version by using
   this command:   
   
   .. code-block:: console

      # swupd update

Optional: Revert your system back to 100% upstream
**************************************************

Should you decide to switch your |CL| system back to the official upstream version, you can do so with this command:

.. code-block:: console
   
   # swupd verify --fix --force --picky -m [upstream-version-number] -C /usr/share/clear/update-ca/Swupd_Root.pem

All of your custom RPMs and bundles will no longer be available because 
:file:`/usr/share/mix` will be deleted as part of the rollback process.  

.. _Developer tooling framework for Clear Linux:
   https://github.com/clearlinux/common
