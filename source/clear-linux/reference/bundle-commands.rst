.. _bundle-commands:

Useful bundle commands
######################



To see a list of currently installed bundles, enter:

    :command:`swupd` :option:`bundle-list`


To see the list of all available bundles, enter:

    :command:`swupd` :option:`bundle-list --all`


    Alternatively, you may reference the `available bundle list`_ webpage.


To search for bundles and their contents, enter:

    .. code-block:: console

        # swupd search [bundle name]


To add a bundle, enter:

    .. code-block:: console

        # swupd bundle-add [bundle name]




Additional information 
======================

For additional :command:`swupd` commands, enter:

    .. code-block:: console

        # swupd --help 

or reference the :command:`swupd` man page, enter:

    .. code-block:: console

        # man swupd


.. _available bundle list: https://clearlinux.org/documentation/clear-linux/reference/bundles/available-bundles#bundle-list
