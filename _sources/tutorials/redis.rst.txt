.. _redis:

Redis\*
#######

In this tutorial, you'll install :abbr:`Redis (REmote DIctionary Server)`
and launch a `Redis-server` on |CL-ATTR|. We invite you to pull our
`Clear Linux Redis instance`_ on Docker Hub\* for application or
infrastructure development.

.. contents::
   :local:
   :depth: 1

Description
***********

Redis is an in-memory key:value store designed for quick lookups, accessible 
over a network. While the `redis data structure store`_ can serve
as a NoSQL database for a web application, it's also easy to integrate into an
existing stack. For example, you could use the Redis caching layer for
real-time responses on a leaderboard in a gaming app. Redis offers many client
libraries with language-specific bindings for Python\*, Perl\*, Ruby, and more.

Install the Redis bundle
************************

#. Log in as a user with administrative privilege.

#. Open a terminal.

#. Update your |CL| to the latest version.

   .. code-block:: bash

      sudo swupd update

#. Install the `redis-native` bundle.

   .. code-block:: bash

      sudo swupd bundle-add redis-native

Start the Redis-server
**********************

A :command:`systemd` service unit is available to control the Redis-server.
By default, Redis runs on port 6379.

#. Start the service and set it to start automatically on boot.

   .. code-block:: bash

      sudo systemctl enable --now redis

#. Confirm the service is running.

   .. code-block:: bash

      sudo systemctl status redis

#. Verify that the Redis-server sends a reply.

   .. code-block:: bash

      redis-cli ping

   Expected output: 

   .. code-block:: console

      PONG

.. note::

   If you wish to customize settings for Redis, copy the
   default :file:`/usr/share/defaults/etc/redis.conf` file into the 
   /etc/ directory, make changes as needed, and restart the service.

   .. code-block:: bash

      sudo cp -v /usr/share/defaults/etc/redis.conf /etc/

The Redis-server is now ready to use on |CL|. Try some of the examples shown
below.

Example 1: Use the redis-cli and commands
*****************************************

One advantage of Redis over other NoSQL databases is that developers can
easily access data structures like lists, sets, sorted sets, strings, and
hashes using collection operations commands similar to those found in many
programming languages. These exercises are inspired by `try redis io`_.

After your Redis-server is running, try some basic commands.

#. Start `redis-cli`. It provides syntax suggestions as you type.

   .. code-block:: bash

      redis-cli

#. :command:`SET` a key to hold a string value. In the set, create connections
   and increment.

   .. code-block:: none

      SET server:name "clearlinux"

   .. code-block:: none

      MGET server:name

   .. note::

      If the key does not exist or hold a key value, `nil` is returned.

   .. code-block:: none

      SET connections 100

   .. code-block:: none

      INCR connections

   .. code-block:: none

      INCR connections

   .. code-block:: none

      DEL connections

#. Create a `friends` list and insert new values at the end of the list.

   .. code-block:: none

      RPUSH friends "Deb"

   .. code-block:: none

      RPUSH friends "David"

   .. code-block:: none

      RPUSH friends "Mary"

#. Modify the `friends` list, using a common slice method with a 0-index.

   .. code-block:: none

      LRANGE friends 0 1

   .. code-block:: none

      LLEN friends

   .. code-block:: none

      LPOP friends

   .. code-block:: none

      RPOP friends

   .. code-block:: none

      LLEN friends

#. Consider using a hash, which maps string fields and string values, and
   offers multiple lookup methods.

   Enter many user key:values with `HMSET`. Then try `HGET` and `HGETALL`.

   .. code-block:: none

      HMSET user:1000 name "Robert Noyce" password "SuperEngi9eer" email "robert.noyce@intel.com"

   .. code-block:: none

      HGET user:1000 name

   .. code-block:: none

      HGET user:1000 email

   .. code-block:: none

      HGETALL user:1000


Example 2: Run the |CL| Redis Docker\* image
********************************************

We also provide a `Clear Linux Redis instance`_, which is
updated continuously and maintained by |CL| development.

.. code-block:: bash

   sudo swupd bundle-add containers-basic

.. code-block:: bash

   sudo systemctl start docker

.. code-block:: bash

   sudo -E docker pull clearlinux/redis

Next Steps
**********

* Follow the `redis quickstart tutorial`_ to expand potential uses.

* Learn how to use :ref:`docker`.

.. _try redis io: http://try.redis.io/

.. _Clear Linux Redis instance: https://hub.docker.com/r/clearlinux/redis

.. _redis data structure store: https://redis.io/

.. _redis quickstart tutorial: https://redis.io/topics/quickstart
