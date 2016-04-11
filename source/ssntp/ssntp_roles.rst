.. _ssntp_roles:

SSNTP Roles
###########

All SSNTP entities must declare their role at connection time, as part
of their signed certificate extended-key usage attributes.  Syntax of this
declaration is::

[role ... extended-key]

SSNTP roles allow for both filtering and routing of frames:

#. **SSNTP frames filtering**: Depending on the previously-declared role
   of the sending entity, the receiving party can choose to discard frames,
   and to optionally send a frame rejection error back.
#. **SSNTP frames routing**: A SSNTP server implementation can be configured
   with frame forwarding rules for multicasting specific received SSNTP frame
   types to all connected SSNTP clients assigned a given role.

There are currently 6 different SSNTP roles:

* **SERVER (0x1)**: A generic SSNTP server.
* **CSR (0x2)**: The CIAO :abbr:`Command and Status Reporting (CSR)` client.
* **AGENT (0x4)**: The CIAO compute node Agent receives workload commands
  from the Scheduler and manages the workload on a given compute node accordingly.
* **SCHEDULER (0x8)**: The CIAO workload Scheduler receives workload-related
  commands from the CSR and schedules them on the available compute nodes.
* **NETAGENT (0x10)**: The CIAO networking compute node NetAgent receives
  networking workload commands from the Scheduler and manages the workload on a
  given networking compute node accordingly.
* **CNCIAGENT (0x20)**: A :abbr:`Compute Node Concentrator Instance Agent (CNCI)`
  runs within the networking node workload, and manages a specific tenant private
  network. Each instance for this tenant will have a GRE tunnel established between
  it and the CNCI; the CNCI acts as the tenant's routing entity.

Next - :ref:`ssntp_connection`