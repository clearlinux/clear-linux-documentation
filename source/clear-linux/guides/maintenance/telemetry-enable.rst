.. _telemetry-enable:

Enable and disable telemetry in Clear Linux
###########################################

|CLOSIA| includes a telemetry solution as part of the OS that records events
of interest and reports them back to the development team via the telemetrics
daemon, :command:`telemd`. This functionality is maintained in the
``telemetrics`` software bundle.

.. note::
   The telemetry functionality adheres to `Intel's privacy policies`_
   regarding the collection and use of :abbr:`PII (Personally Identifiable
   Information)` and is open source. Specifically, no intentionally
   identifiable information about the user or system owner is collected.

End users may enable or disable the telemetry component of |CL| or even
redirect where the records go if they wish to collect records for themselves.

Install the telemetry software bundle
*************************************

During the initial installation of |CL| you are requested to join the
stability enhancement program and allow |CLOSIA| to collect anonymous reports
to improve system stability. If you chose not to join this program at that
time then the telemetry software bundle is not added to your system.

To install the telemetry bundle, enter the following command as either the
root user or with :command:`sudo` priveleges:

.. code-block:: console

	sudo swupd bundle-add telemetrics

This adds the telemetrics-client to your system and you will automatically
opt-in for the service.

Enable Telemetry
****************

To start telemetry on your system run the following command:

.. code-block:: console

	sudo telemctl start

This enables and starts the :command:`telemd` daemon and your system will
begin to send telemetry data to the server defined in the file
:file:`/etc/telemetrics/telemetrics.conf`. If this file does not exist, the
:command:`telemd` daemon will use the file
:file:`/usr/share/defaults/telemetrics/telemetrics.conf`.

Disable Telemetry
*****************

To disable the telemetry daemon run the following command:

.. code-block:: console

	sudo telemctl stop

Opt-out of telemetry
********************

To stop sending telemetrics data from your system, opt out of the
telemetry service:

.. code-block:: console

	sudo telemctl opt-out

This creates the file :file:`/etc/telemetrics/opt-out` and stops the
telemetry services.

Opt-in to telemetry
*******************

Conversely, to opt-in to the telemetry services, simply enter the opt-in
command and start the service:

.. code-block:: console

	sudo telemctl opt-in

This removes the file :file:`/etc/telemetrics/opt-out` file, if it exists,
and starts the telemetry services.

.. note::
	To opt-in but not immediately start telemetry services, you will need to
	run the command :command:`sudo telemctl stop` after the :command:`opt-in`
	command is entered. Once you are ready to start the service, enter the
	command	:command:`sudo telemctl start`.

Remove the telemetry software bundle
************************************

To completely remove telemetrics from your system, use the command
:command:`swupd` to remove the telemetry software bundle:

.. code-block:: console

	sudo swupd bundle-remove telemetrics

Additional resources
********************

https://clearlinux.org/features/telemetry

https://github.com/clearlinux/telemetrics-client

.. _`Intel's privacy policies`:
   https://www.intel.com/content/www/us/en/privacy/intel-privacy-notice.html
