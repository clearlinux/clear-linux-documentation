.. _telemetry-about:

Telemetrics
###########

Telemetry is one of the key features of |CLOSIA|. The |CL| team is focused on
the quality of the telemetry data, and is moving from issues that are detected
and reported by users to issues detected and repaired by providers. Ideally,
these issues will be undetected by users.

On the |CL| team, we refer to *telemetrics*, which is a combination word made from:

*	Telemetry which is sensing and reporting data.
*	Analytics which is using visualization and statistical inferencing to make
	sense of the reported data.

|CL| telemetry reports system-level debug/crash information using specialized probes. The
probes monitor system tasks such as :abbr:`swupd (software updater)`, kernel
oops, machine error checks, and BIOS error report table for unhandled hardware
failures. Telemetry enables real-time issue reporting to allow system
developers to quickly focus on an issue and monitor corrective actions.

|CL| telemetry is fully customizable and can be used during software development
for debugging purposes. You can use libtelemetry in your code to create custom
telemetry records. You can also use telem-record-gen in script files or call
it from another program.

Architecture
************

|CL| telemetry has two fundamental components, which are shown in figure 1:

*	Client:  generates and delivers records to the backend server via the network.
*	Backend: captures records sent from the client and displays the cumulative
	content through a specialized interface.

Note: To capture records for analysis, you must set up your own backend server.

.. figure:: figures/telemetry-about-1.png
   :scale: 75%
   :alt: Clear Linux Telemetry Architecture.

   Figure 1: Clear Linux Telemetry Architecture.

The telemetry client provides the front end of a complete telemetrics solution
and includes the following components:

*	telemd, a daemon that prepares the records to send to a telemetrics server or
	spools the records on disk in case it cannot successfully deliver them.
*	Probes that collect specific types of data from the operating system.
*	libtelemetry, that telemetrics probes use to create telemetrics records and
	send them to the telemd daemon for further processing.

The telemetry backend provides the server-side component of a complete telemetrics solution and
consists of:

*	Nginx web server.
*	Two Flask apps:

	*	Collector, an ingestion web app for records received from telemetrics-client probes.
	*	TelemetryUI, a web app that exposes several views to visualize the telemetry data
		and also provides a REST API to perform queries.

*	PostgreSQL as the underlying database server.

Next steps
**********

To put this concept into practice, see the following resources:

*	:ref:`Enable and disable telemetry in Clear Linux<telemetry-enable>`
*	:ref:`Create a telemetry backend server in Clear Linux<telemetry-backend>`
*	`Telemetry feature description`_

.. _`Telemetry feature description:
	`https://clearlinux.org/features/telemetry
