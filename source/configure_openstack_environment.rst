.. _configure_openstack_environment:


Configure your environment
==========================

Before continuing with the installation process, it's important to understand:

* The :file:`hosts` file; this file defines the roles your machines play in the
  overall scheme of your network mapping.
   **Note**: For more in-depth information, see :ref:`openstack_env_inventory_file`

* The ``group_vars/all`` structuring can be used to override variable
  values. **Note**: For more in-depth information, see :ref:`openstack_conf_vars_about`

Once you understand these components and are comfortable modifying them to affect
the network configuration, you can proceed as follows:

#. Copy ``/usr/share/ansible/examples/openstack`` to your working directory.

#. Move into the copied directory.

#. Edit the :file:`hosts` file to specify node roles.

#. Edit the contents under ``group_vars/all`` to set passwords and other needed
   variables. **Note**: Default variables exist for every role in the
   :file:`roles/<role>/defaults/main.yml` file. To override a default, define
   it with specifications under ``group_vars/all``.


Run the installer
=================

Finally, you can run the installer.

#. Run the installer as follows, replacing ``<ssh_key>`` with the key you've
   previously set up::

    $ ansible-playbook -i hosts openstack_deployment.yml --private-key=<ssh_key>

After running the previous command you should see the output of the tasks 
that are running.

At the end of the execution Ansible* will display a summary of the results.
