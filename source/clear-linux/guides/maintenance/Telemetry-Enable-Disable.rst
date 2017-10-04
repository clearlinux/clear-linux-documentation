.. _telemetry-enable-disable:

Enable and Disable Telemetry in Clear Linux
###########################################

|CLOSIA| includes a telemetry solution as part of the OS that records events
of interest and reports them back to the development team via the telemetrics
daemon, :command:`telemd`.  This functionality is maintained in the
``telemetrics`` software bundle.

.. Note::
	The telemetrics functionality adheres to `Intel’s privacy policies`_
	regarding the collection and use of Personally Identifiable Information
	(PII) and is Open Source. Specifically, no intentionally identifiable
	information about the user or system owner is collected.

End users may enable or disable the telemetry component of |CL| or even
redirect where records go if they wish to collect records for themselves.

Install the telemetry software bundle
*************************************

During the initial installation of |CL| you are requested to join the
Stability Enhancement Program and allow |CLOSIA| to collect anonymous reports
to improve system stability.  If you chose not to join this program at that
time then the telemetry software bundle was not added to your system.

To install the telemetry bundle, enter the following command as either the
root user or with :command:`sudo` priveleges:

.. code-block:: console

	sudo swupd bundle-add telemetrics

This will add the telemetrics-client to your system and you will automatically
be opted-in for the service.

Enable Telemetry
****************

To start telemetry on your system run the following command:

.. code-block:: console

	sudo telemctl start

This will enable and start the :command:`telemd` daemon and your system will
begin to send telemetry data to the server defined in the file
:file:`/etc/telemetrics/telemetrics.conf` and if this file does not exist it
will use the file :file:`/usr/share/defaults/telemetrics/telemetrics.conf`.

Disable Telemetry
*****************

To disable the telemetry daemon run the following command:

.. code-block:: console

	sudo telemctl stop

Opt-out of telemetry
********************

If you no longer want to send telemetrics data from your system, you can
opt-out of the service by running the command:

.. code-block:: console

	sudo telemctl stop
	sudo telemctl opt-out

This will create the file :file:`/etc/telemetrics/opt-out` and stop the
telemetry services.

Opt-in to telemetry
*******************

Conversely, to opt-in to the telemetry services, simple enter the opt-in
command and start the service:

.. code-block:: console

	sudo telemctl opt-in
	sudo telemctl start

This will remove the file :file:`/etc/telemetrics/opt-out` file if it exists.

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
   http://www.intel.com/content/www/us/en/privacy/intel-privacy.html
