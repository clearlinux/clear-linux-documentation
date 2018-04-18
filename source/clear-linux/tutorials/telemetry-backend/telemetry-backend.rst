.. _telemtry-backend:

Create a telemetry backend server in Clear Linux
################################################

|CLOSIA| includes a telemetry and analytics solution, also known as
telemetrics, as part of the OS that records events of interest and reports
them back to the development team using the :command:`telemd` telemetrics
daemon.

End users can enable or disable the telemetry client component of |CL| and
also redirect where records go if they wish to collect records for themselves
by setting up and using their own telemetry backend server.

A telemetry backend server consists of two Flask applications:

* The :guilabel:`collector` is an ingestion app for records received from the
  :guilabel:`telemetrics-client` probes.
* The :guilabel:`telemetryui` web app exposes several visualizations of the
  telemetry data. The :guilabel:`telemetryui` app also provides a
  REST API to perform queries on the data.

The applications run within a web stack, using the :guilabel:`nginx` web
server, the :guilabel:`uWSGI` application server, and
:guilabel:`PostgreSQL` as the underlying database server. For a detailed
description, visit the `Clear Linux telemetry backend server overview`_.

This tutorial walks you through creating a telemetrics backend server on
your local |CL| machine. The tutorial uses the :command:`deploy.sh` bash
shell script that is maintained in a GitHub repository at
https://github.com/clearlinux/telemetrics-backend. Once the backend server is
up and running, we show you how to redirect telemetry records from the system
you set up to this new server location.

.. note::
   The telemetrics functionality adheres to `Intel privacy policies`_
   regarding the collection and use of :abbr:`PII (Personally Identifiable
   Information)` and is open Source. Specifically, no intentionally
   identifiable information about the user or system owner is collected.

Prerequisites
*************

For this tutorial, start with a clean installation of |CL| on a new system
using the :ref:`bare-metal-install` getting started guide:

#. Choose to install |CL|.
#. Join the :guilabel:`Stability Enhancement Program` to install and
   enable the telemetrics components.
#. Select the manual installation method with the following settings:

   * Set the hostname to :guilabel:`clr-telem-server`,
   * Create an administrative user named :guilabel:`clear` and add this user
     to sudoers,
   * Add all additional software bundles.

Download the clearlinux/telemetrics-backend Git repository
**********************************************************

With all prerequisite software bundles installed and logged in with your
administrative user, from your :file:`$HOME` directory, run :command:`git`
to clone the :guilabel:`telemetrics-backend` repository into the
:file:`$HOME/telemetrics-backend` directory:

.. code-block:: console

   git clone https://github.com/clearlinux/telemetrics-backend

.. note::
   You may need to set up the :envvar:`https_proxy` environment variable
   if you have issues reaching github.com.

Run the deploy.sh script to install the backend server
******************************************************

#. Change your current working directory to :file:`telemetrics-backend/scripts`.
#. Run the :command:`./deploy.sh -h` to see the list of options for the
   :command:`deploy.sh` script:

.. code-block:: console

   cd telemetrics-backend/scripts
   ./deploy.sh -h
  
   Deploy snapshot of the telemetrics-backend

     -a    Perform specified action (deploy, install, migrate, resetdb,
           restart, uninstall; default: deploy)
     -d    Distro to deploy to (ubuntu, centos or clr; default: ubuntu)
     -h    Print these options
     -H    Set domain for deployment (only accepted value is "localhost" for
           now)
     -r    Set repo location to deploy from
           (default: https://github.com/clearlinux/telemetrics-backend)
     -s    Set source location (default: "master" branch from git repo)
     -t    Set source type (tarball, or git; default: git)
     -u    Perform complete uninstallation

The :command:`deploy.sh` is a bash shell script that allows you to perform the
following actions:

* :option:`deploy` - install a complete instance of the telemetrics backend
  server and all required components. This is the default action if no
  :option:`-a` argument is given on the command line.
* :option:`install` - installs and enables all required components for the
  telemetrics backend server.
* :option:`migrate` - migrate database to new schema.
* :option:`resetdb` - reset the database.
* :option:`restart` - restart the nginx and uWSGI services.
* :option:`uninstall` - uninstall all packages.

  ..note::
  
  The :option:`uninstall` option does not perform any actions if the distro is
  set to |CL| and will only uninstall packages if the distro is Ubuntu

Next, we install the telemetrics backend server with the following options:

* :option:`-a install` to perform an install
* :option:`-d clr` to install to a |CL| distro
* :option:`-H localhost` to set the domain to localhost

We do not need to set the following options since the values are set to the
correct values we want by default:

* :option:`-r https://github.com/clearlinux/telemetrics-backend` sets the
  repo location for :command:`git` to clone from.
* :option:`-s master` to set the location, or branch.
* :option:`-t git` to set the source type to git.

.. caution::
   The :file:`deploy.sh` shell script has minimal error checking and makes
   several changes to your system.  Be sure that the options you define on the
   cmdline are correct before proceeding.

To begin the installation with the options defined:

#. Run the shell script from the :file:`$HOME/telemetrics-backend/scripts`
   directory:

   .. code-block:: console

      ./deploy.sh -H localhost -a install -d clr

   The script will start and list all the defined options and prompt you for the
   :guilabel:`PostgreSQL` database password as shown below:

   .. code-block:: console

      Options:
        host: localhost
        distro: clr
        action: install
        repo: https://github.com/clearlinux/telemetrics-backend
        source: master
        type: git
      DB password: (default: postgres):

#. For the :guilabel:`DB password:`, press the :kbd:`Enter` key to accept the
   default password `postgres`.
   
The :command:`swupd` begins installing the required software bundles to set
up the telemetrics backend server. The output will look similar to what is
shown below:

.. code-block:: console

   swupd-client bundle adder 3.12.7
      Copyright (C) 2012-2017 Intel Corporation

   Downloading packs...

   Extracting application-server pack for version 18740
        ...5%
   Extracting database-basic-dev pack for version 18670
        ...10%
   Extracting database-basic pack for version 18670
        ...15%
   Extracting os-clr-on-clr pack for version 18740
        ...21%
   Extracting sysadmin-basic-dev pack for version 18740
        ...26%
   Extracting storage-utils-dev pack for version 18770
        ...31%
   Extracting os-core-update-dev pack for version 18760
        ...36%
   Extracting network-basic-dev pack for version 18760
        ...42%
   Extracting mixer pack for version 18790
        ...47%
   Extracting os-installer pack for version 18800
        ...52%
   Extracting mail-utils-dev pack for version 18760
        ...57%
   Extracting koji pack for version 18800
        ...63%
   Extracting go-basic pack for version 18800
        ...68%
   Extracting dev-utils-dev pack for version 18820
        ...73%
   Extracting python-basic-dev pack for version 18750
        ...78%
   Extracting perl-basic-dev pack for version 18610
        ...84%
   Extracting c-basic pack for version 18800
        ...89%
   Extracting os-core-dev pack for version 18800
        ...94%
   Extracting web-server-basic pack for version 18680
        ...100%
   Installing bundle(s) files...
        ...100%
   Calling post-update helper scripts.
   Possible filedescriptor leak : 8 (socket:[30833])
   Bundle(s) installation done.

.. note::

   This script uses :command:`sudo` to run commands and you may be prompted to
   enter your user password at any time while the script is executing. If this
   occurs, enter your user password to execute the :command:`sudo` command.

   .. code-block:: console

      Password:

   You may also see an informational message about setting the
   :envvar:`https_proxy` environment variable if this variable isn't set.

Once the :command:`swupd` command is complete, the script begins processing
the requirements to install and implement the telemetrics server. Finally,
the script enables the server and provides output similar to:

.. code-block:: console
   
   Collecting uwsgitop
     Downloading uwsgitop-0.10.tar.gz
   Requirement already satisfied: simplejson in /usr/lib/python3.6/site-packages (from uwsgitop)
   Collecting argparse (from uwsgitop)
     Downloading argparse-1.4.0-py2.py3-none-any.whl
   Building wheels for collected packages: uwsgitop
     Running setup.py bdist_wheel for uwsgitop ... done
     Stored in directory: /root/.cache/pip/wheels/8a/99/e9/accc80bcaa989218da65daaae4205dc4f6288d3551655aa638
   Successfully built uwsgitop
   Installing collected packages: argparse, uwsgitop
   Successfully installed argparse-1.4.0 uwsgitop-0.10
   mkdir: created directory '/var/www'
   mkdir: created directory '/var/www/telemetry'
   Already using interpreter /usr/bin/python3
   Using base prefix '/usr'
   New python executable in /var/www/telemetry/venv/bin/python3
   Also creating executable in /var/www/telemetry/venv/bin/python
   Installing setuptools, pip, wheel...done.
   Collecting alembic==0.9.5 (from -r /tmp/requirements.txt.KDI3uU (line 1))
     Downloading alembic-0.9.5.tar.gz (990kB)
       100% |████████████████████████████████| 993kB 2.1MB/s
   Collecting click==6.7 (from -r /tmp/requirements.txt.KDI3uU (line 2))
     Downloading click-6.7-py2.py3-none-any.whl (71kB)
       100% |████████████████████████████████| 71kB 8.3MB/s
   Collecting Flask==0.12.2 (from -r /tmp/requirements.txt.KDI3uU (line 3))
     Downloading Flask-0.12.2-py2.py3-none-any.whl (83kB)
       100% |████████████████████████████████| 92kB 10.2MB/s
   Collecting Flask-Migrate==2.1.0 (from -r /tmp/requirements.txt.KDI3uU (line 4))
     Downloading Flask-Migrate-2.1.0.tar.gz
   Collecting Flask-SQLAlchemy==2.2 (from -r /tmp/requirements.txt.KDI3uU (line 5))
     Downloading Flask_SQLAlchemy-2.2-py2.py3-none-any.whl
   Collecting Flask-WTF==0.14.2 (from -r /tmp/requirements.txt.KDI3uU (line 6))
     Downloading Flask_WTF-0.14.2-py2.py3-none-any.whl
   Collecting itsdangerous==0.24 (from -r /tmp/requirements.txt.KDI3uU (line 7))
     Downloading itsdangerous-0.24.tar.gz (46kB)
       100% |████████████████████████████████| 51kB 12.4MB/s
   Collecting Jinja2==2.9.6 (from -r /tmp/requirements.txt.KDI3uU (line 8))
     Downloading Jinja2-2.9.6-py2.py3-none-any.whl (340kB)
       100% |████████████████████████████████| 348kB 3.5MB/s
   Collecting Mako==1.0.7 (from -r /tmp/requirements.txt.KDI3uU (line 9))
     Downloading Mako-1.0.7.tar.gz (564kB)
       100% |████████████████████████████████| 573kB 1.9MB/s
   Collecting MarkupSafe==1.0 (from -r /tmp/requirements.txt.KDI3uU (line 10))
     Downloading MarkupSafe-1.0.tar.gz
   Collecting psycopg2==2.7.3 (from -r /tmp/requirements.txt.KDI3uU (line 11))
     Downloading psycopg2-2.7.3.tar.gz (425kB)
       100% |████████████████████████████████| 430kB 4.0MB/s
   Collecting python-dateutil==2.6.1 (from -r /tmp/requirements.txt.KDI3uU (line 12))
     Downloading python_dateutil-2.6.1-py2.py3-none-any.whl (194kB)
       100% |████████████████████████████████| 194kB 6.8MB/s
   Collecting python-editor==1.0.3 (from -r /tmp/requirements.txt.KDI3uU (line 13))
     Downloading python-editor-1.0.3.tar.gz
   Collecting six==1.10.0 (from -r /tmp/requirements.txt.KDI3uU (line 14))
     Downloading six-1.10.0-py2.py3-none-any.whl
   Collecting SQLAlchemy==1.1.13 (from -r /tmp/requirements.txt.KDI3uU (line 15))
     Downloading SQLAlchemy-1.1.13.tar.gz (5.2MB)
       100% |████████████████████████████████| 5.2MB 394kB/s
   Collecting uWSGI==2.0.15 (from -r /tmp/requirements.txt.KDI3uU (line 16))
     Downloading uwsgi-2.0.15.tar.gz (795kB)
       100% |████████████████████████████████| 798kB 1.5MB/s
   Collecting Werkzeug==0.12.2 (from -r /tmp/requirements.txt.KDI3uU (line 17))
     Downloading Werkzeug-0.12.2-py2.py3-none-any.whl (312kB)
       100% |████████████████████████████████| 317kB 2.2MB/s
   Collecting WTForms==2.1 (from -r /tmp/requirements.txt.KDI3uU (line 18))
     Downloading WTForms-2.1.zip (553kB)
       100% |████████████████████████████████| 563kB 1.7MB/s
   Skipping bdist_wheel for psycopg2, due to binaries being disabled for it.
   Building wheels for collected packages: alembic, Flask-Migrate, itsdangerous, Mako, MarkupSafe, python-editor, SQLAlchemy, uWSGI, WTForms
     Running setup.py bdist_wheel for alembic ... done
     Stored in directory: /root/.cache/pip/wheels/d1/0e/b9/fb570150b350298e1d8f1ff38a400ae709580b36e43bc3ac91
     Running setup.py bdist_wheel for Flask-Migrate ... done
     Stored in directory: /root/.cache/pip/wheels/3d/29/d4/66747eca8b8a28973aa639f39e96a402b3dcab335e608048dd
     Running setup.py bdist_wheel for itsdangerous ... done
     Stored in directory: /root/.cache/pip/wheels/fc/a8/66/24d655233c757e178d45dea2de22a04c6d92766abfb741129a
     Running setup.py bdist_wheel for Mako ... done
     Stored in directory: /root/.cache/pip/wheels/33/bf/8f/036f36c35e0e3c63a4685e306bce6b00b6349fec5b0947586e
     Running setup.py bdist_wheel for MarkupSafe ... done
     Stored in directory: /root/.cache/pip/wheels/88/a7/30/e39a54a87bcbe25308fa3ca64e8ddc75d9b3e5afa21ee32d57
     Running setup.py bdist_wheel for python-editor ... done
     Stored in directory: /root/.cache/pip/wheels/84/d6/b8/082dc3b5cd7763f17f5500a193b6b248102217cbaa3f0a24ca
     Running setup.py bdist_wheel for SQLAlchemy ... done
     Stored in directory: /root/.cache/pip/wheels/f0/50/ca/3cb6e78527eb05e180d19632343ee14d2e5c164da2e61fbd2d
     Running setup.py bdist_wheel for uWSGI ... done
     Stored in directory: /root/.cache/pip/wheels/26/d0/48/e7b0eed63b5d191e89d94e72196aafae93b2b6505a9feafdd9
     Running setup.py bdist_wheel for WTForms ... done
     Stored in directory: /root/.cache/pip/wheels/36/35/f3/7452cd24daeeaa5ec5b2ea13755316abc94e4e7702de29ba94
   Successfully built alembic Flask-Migrate itsdangerous Mako MarkupSafe python-editor SQLAlchemy uWSGI WTForms
   Installing collected packages: SQLAlchemy, MarkupSafe, Mako, python-editor, six, python-dateutil, alembic, click, Werkzeug, Jinja2, itsdangerous, Flask, Flask-SQLAlchemy, Flask-Migrate, WTForms, Flask-WTF, psycopg2, uWSGI
     Running setup.py install for psycopg2 ... done
   Successfully installed Flask-0.12.2 Flask-Migrate-2.1.0 Flask-SQLAlchemy-2.2 Flask-WTF-0.14.2 Jinja2-2.9.6 Mako-1.0.7 MarkupSafe-1.0 SQLAlchemy-1.1.13 WTForms-2.1 Werkzeug-0.12.2 alembic-0.9.5 click-6.7 itsdangerous-0.24 psycopg2-2.7.3 python-dateutil-2.6.1 python-editor-1.0.3 six-1.10.0 uWSGI-2.0.15
   mkdir: created directory '/var/log/uwsgi'

Once all the server components have been installed you are prompted to enter
the :guilabel:`PostgreSQL` database password to change it as illustrated below:

.. code-block:: console
   
   Enter password for 'postgres' user:
   New password:
   Retype new password:
   passwd: password updated successfully

Enter `postgres` for the current value of the password and then enter a new
password, retype it to verify the new password and the :guilabel:`PostgreSQL`
database password will be updated.

The script finalizes installation and finishes.

.. code-block:: console
   
   Created symlink /etc/systemd/system/multi-user.target.wants/postgresql.service → /usr/lib/systemd/system/postgresql.service.
   Cloning into 'telemetrics-backend'...
   remote: Counting objects: 344, done.
   remote: Compressing objects: 100% (53/53), done.
   remote: Total 344 (delta 30), reused 50 (delta 20), pack-reused 268
   Receiving objects: 100% (344/344), 130.20 KiB | 1.40 MiB/s, done.
   Resolving deltas: 100% (177/177), done.
   '/tmp/telemetrics-backend/scripts/collector_uwsgi.ini' -> '/tmp/telemetrics-backend/collector/collector_uwsgi.ini'
   '/tmp/telemetrics-backend/scripts/telemetryui_uwsgi.ini' -> '/tmp/telemetrics-backend/telemetryui/telemetryui_uwsgi.ini'
   mkdir: created directory '/var/www/telemetry/collector/uwsgi-spool'
   mkdir: created directory '/var/www/telemetry/telemetryui/uwsgi-spool'
   '/tmp/telemetrics-backend/scripts/uwsgi.service' -> '/etc/systemd/system/uwsgi.service'
   mkdir: created directory '/etc/nginx'
   mkdir: created directory '/etc/nginx/conf.d'
   '/usr/share/nginx/conf/nginx.conf.example' -> '/etc/nginx/nginx.conf'
   Created symlink /etc/systemd/system/multi-user.target.wants/nginx.service → /usr/lib/systemd/system/nginx.service.
   mkdir: created directory '/etc/uwsgi'
   mkdir: created directory '/etc/uwsgi/vassals'
   Created symlink /etc/systemd/system/multi-user.target.wants/uwsgi.service → /etc/systemd/system/uwsgi.service.
   ALTER ROLE
   sed: can't read /tmp/telemetrics-backend/collector/config.py: No such file or directory
   cp: cannot stat '/tmp/telemetrics-backend/collector/config.py': No such file or directory
   sed: can't read /tmp/telemetrics-backend/telemetryui/config.py: No such file or directory
   cp: cannot stat '/tmp/telemetrics-backend/telemetryui/config.py': No such file or directory
   Already using interpreter /usr/bin/python3
   Using base prefix '/usr'
   New python executable in /var/www/telemetry/venv/bin/python3
   Not overwriting existing python script /var/www/telemetry/venv/bin/python (you must use /var/www/telemetry/venv/bin/python3)
   Installing setuptools, pip, wheel...done.
   INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
   INFO  [alembic.runtime.migration] Will assume transactional DDL.
   INFO  [alembic.runtime.migration] Running upgrade  -> 3230c615d6e0, empty message
   INFO  [alembic.runtime.migration] Running upgrade 3230c615d6e0 -> 466cf2f35d67, empty message

   Install complete (installation folder: /var/www/telemetry)

Once the installation is complete you can use your web browser and view the
new server by opening the web browser on the system you installed the backend
server onto and type in ``localhost`` in the address bar.  You should see a
web page similar to the one shown in figure 1:

.. figure:: figures/telemetry-backend-1.png
   :scale: 50 %
   :alt: Telemetry UI

   Figure 1: :guilabel:`Telemetry UI`


Redirect telemetry records
**************************

Telemetry records from your system are sent to the server location defined in
the :file:`/usr/share/defaults/telemetrics/telemetrics.conf` configuration
file. You can customize this by copying this file to
:file:`/etc/telemetrics/telemetrics.conf` and changing the ``server=``
setting to your new server location.

#. Create the :file:`/etc/telemetrics` directory and make it your current
   working directory.

   .. code-block:: console

      sudo mkdir -p /etc/telemetrics
      cd /etc/telemetrics


#. Copy the default :file:`telemetrics.conf` file to the new
   :file:`/etc/telemetrics` directory.

   .. code-block:: console

      sudo cp /usr/share/defaults/telemetrics/telemetrics.conf .

#. Edit the new :file:`/etc/telemetrics/telemetrics.conf` file with your
   editor using the :command:`sudo` directive and change the
   :guilabel:`server=` setting to ``http://localhost/v2/collector`` and save
   this change in the new file.

   .. code-block:: console

      server=http://localhost/v2/collector

   You can also use the fully qualified domain name for your server instead of
   :guilabel:`localhost`.

#. Restart the :command:`telemd` daemon to reload the configuration file.

   .. code-block:: console

      systemctl restart telemd

Test the new telemetry backend server
*************************************

|CL| includes a telemetry test probe called :command:`hprobe` that will send a
``hello`` record to the telemetry backend server.  To test that the telemetry
records are now going to your new destination, run the :command:`hprobe`
command to send a ``hello`` record to the server as follows:

.. code-block:: console

   hprobe

The record should show up on your new server console as shown in figure 2:

.. figure:: figures/telemetry-backend-2.png
   :scale: 50 %
   :alt: Telemetry UI

   Figure 2: :guilabel:`Telemetry UI`

Congratulations!  You've just set up and enabled a new telemetrics backend
server, redirected the records from your local machine to this new server and
tested it using the :command:`hprobe` command to send a ``hello`` record to
it.

Additional resources
********************

https://clearlinux.org/features/telemetry

https://github.com/clearlinux/telemetrics-client

https://github.com/clearlinux/telemetrics-backend

.. _`Clear Linux telemetry backend server overview`:
   https://github.com/clearlinux/telemetrics-backend

.. _`Intel privacy policies`:
   https://www.intel.com/content/www/us/en/privacy/intel-privacy-notice.html
