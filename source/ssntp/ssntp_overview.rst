.. _ssntp_overview:

SSNTP Overview
##############

The :abbr:`Simple and Secure Node Transfer Protocol (SSNTP)` is a custom,
fully-asynchronous and TLS-based application layer protocol. All
:abbr:`Cloud Integrated Advanced Orchestrator (CIAO)` components communicate
with each other over SSNTP.

SSNTP is designed with simplicity, efficiency and security in mind:

* All SSNTP entities are identified with a :abbr:`Universal Unique IDentifier (UUID)`.
* All SSNTP frame headers are identical for easy parsing.
* SSNTP payloads are *optional*.
* SSNTP payloads are YAML formatted.
* SSNTP is a one-way protocol, where senders do not receive a synchronous answer from
  the receivers.
* Any SSNTP entity can asynchronously send a command, status, or event to one of its
  peers.

SSNTP Clients and Servers
=========================

The SSNTP protocol defines two entities: SSNTP clients and SSNTP servers.

A :def:`SSNTP server` listens for and may accept connections from many
SSNTP clients. It never initiates a connection to another SSNTP entity.

A :def:`SSNTP client` initiates a connection to a SSNTP server and can connect to
**only one single server** at a time. When connected, it does not accept incoming
connections from any other SSNTP entity.

Once connected, both clients and servers can initiate SSNTP transfers at any point
in time without having to wait for any kind of SSNTP acknowledgement from the other
end of the connection. SSNTP is a fully asynchronous protocol.

Next - :ref:`ssntp_roles`