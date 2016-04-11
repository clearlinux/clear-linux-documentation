.. _ssntp_connection:

SSNTP Connection
################

Before a SSNTP client is allowed to send any frame to a SSNTP server,
or vice versa, both need to successfully go through the SSNTP
connection protocol.

The SSNTP connection is a mandatory step for the client and the
server to verify each other's roles and also to retrieve each other's
UUIDs. The process generally follows this format:

#. SSNTP **client sends a CONNECT command** to the SSNTP server. This
   frame contains the advertised SSNTP client, which should match
   the client's certificate extended-key usage attributes. The server
   will verify that both match; and if they don't, it will send an SSNTP
   error frame back with a ``ConnectionAborted (0x6)`` error code.
   The CONNECT frame destination UUID is the nil UUID because the client
   does not know the server UUID before getting its CONNECTED frame.

#. The **server asynchronously sends a CONNECTED status frame** to the
   client in order to notify it of a successful connection. The
   CONNECTED frame contains the server-advertised role. The client must
   verify that the server role matches its certificate extended-key usage
   attributes. If that verification fails the client must send a SSNTP
   error frame to the server where the error code is ``ConnectionFailure (0x4)``,
   and then must close the TLS connection to the server.

#. **Connection is successfully established**. Both ends of the connection
   can now asynchronously send SSNTP frames.


Next - :ref:`ssntp_frames`