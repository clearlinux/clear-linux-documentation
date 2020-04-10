.. _kernel-boot-msg:

Capture Kernel Boot Messages in the Journal
###########################################

By default |CL| does not capture kernel boot messages in the journal logs, 
where they're reported as "Missed" messages.  This design decision was made 
to provide a faster boot performance.  On the other hand, if you wish to 
see the messages, follow this guide.

Here's an example a journal log with "Missed" messages:

.. code-block:: console
   :linenos:
   :emphasize-lines: 4

   -- Reboot --
   Apr 10 19:55:43 kernel systemd-journald[300]: Journal started
   Apr 10 19:55:43 kernel systemd-journald[300]: Runtime Journal (/run/log/journal/d01862ca79d1064ea379cd715cfdd53a) is 5.8M, max 47.0M, 41.1M free.
   Apr 10 19:55:43 kernel systemd-journald[300]: Missed 2233 kernel messages
   Apr 10 19:55:43 kernel systemd[1]: Started Journal Service.

.. contents::
   :local:
   :depth: 1
 
Prerequisites
*************

* `systemd-journald` version 245 and higher 

Enable journaling of kernel boot messages
*****************************************

#. Open a terminal window.

#. Create a base journald configuration file.

   .. code-block:: bash

      sudo mkdir -p /etc/systemd/journald.conf.d
      sudo cp /usr/lib/systemd/journald.conf.d/clear.conf /etc/systemd/journald.conf.d/

#. Append :command:`BootKMsg=true` to it.
   
   .. code-block:: bash

      echo "BootKMsg=true" | sudo tee -a /etc/systemd/journald.conf.d/clear.conf

#. Reboot.  

.. tip::

   If you need to increase the kernel buffer length (for example, 1M), do this: 

   .. code-block:: bash
   
      sudo mkdir -p /etc/kernel/cmdline.d/
      echo "log_buf_len=1M" | sudo tee /etc/kernel/cmdline.d/log_buf_len.conf
      sudo clr-boot-manager update

Alternative
***********

An alternative is to use :command:`dmesg`.  

.. code-block:: bash

   sudo dmesg 
