.. _telemetry-enable:

Enable and disable telemetry in Clear Linux* OS
###############################################

|CL-ATTR| includes a telemetry solution as part of the OS that records events
of interest and reports them back to the development team via the telemetrics
client daemons, **telempobd** and **telempostmd**. This functionality is
maintained in the **telemetrics** software bundle.

.. note::
   The telemetry functionality adheres to `Intel privacy policies`_
   regarding the collection and use of :abbr:`PII (Personally Identifiable
   Information)` and is open source. Specifically, no intentionally
   identifiable information about the user or system owner is collected.

End users may enable or disable the telemetry component of |CL| or even
redirect where the records go if they wish to collect records for themselves.

Install the telemetry software bundle
*************************************

During the initial installation of |CL|, you are requested to join the
stability enhancement program and allow |CL| to collect anonymous reports
to improve system stability. If you choose not to join this program, then the
telemetry software bundle is not added to your system.

To install the telemetry bundle, enter the following command as either the
root user or with :command:`sudo` privileges:

.. code-block:: bash

	sudo swupd bundle-add telemetrics

This adds the telemetrics-client to your system and you will automatically
opt-in for the service.

Enable Telemetry
*****************

To start telemetry on your system, run the following command:

.. code-block:: bash

   sudo telemctl start

This enables and starts the :command:`telemprobd` and :command:`telempostd` daemons and your system will
begin to send telemetry data to the server defined in the file
:file:`/etc/telemetrics/telemetrics.conf`. If this file does not exist, the
:command:`telemd` daemon will use the file
:file:`/usr/share/defaults/telemetrics/telemetrics.conf`.

Disable Telemetry
*****************

To disable both of the telemetry daemons, run the following command:

.. code-block:: bash

   sudo telemctl stop

Opt-out of telemetry
********************

To stop sending telemetrics data from your system, opt out of the
telemetry service:

.. code-block:: bash

   sudo telemctl opt-out

This creates the file :file:`/etc/telemetrics/opt-out` and stops the
telemetry services.

Opt-in to telemetry
*******************

Conversely, to opt-in to the telemetry services, simply enter the opt-in
command and start the service:

.. code-block:: bash

   sudo telemctl opt-in

This removes the file :file:`/etc/telemetrics/opt-out` file, if it exists,
and starts the telemetry services.

.. note::
	
   To opt-in but not immediately start telemetry services, you will need to
   run the command :command:`sudo telemctl stop` after the :command:`opt-in`
   command is entered. Once you are ready to start the service, enter the
   command :command:`sudo telemctl start`.

Remove the telemetry software bundle
************************************

To completely remove telemetrics from your system, use the command
:command:`swupd` to remove the telemetry software bundle:

.. code-block:: bash

   sudo swupd bundle-remove telemetrics

Additional resources
********************

*	`Telemetry feature description`_
*	:ref:`Telemetry architecture<telemetry-about>`
*	:ref:`telemetry-backend`
*	https://github.com/clearlinux/telemetrics-client

.. _Intel privacy policies: https://www.intel.com/content/www/us/en/privacy/intel-privacy-notice.html

.. _`Telemetry feature description`:
	https://clearlinux.org/features/telemetry
