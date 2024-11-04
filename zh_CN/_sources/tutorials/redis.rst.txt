.. _redis:

Redis\*
#######

Redis is an in-memory key:value store designed for quick lookups, accessible
over the network. In this tutorial, you'll install redis and launch a
redis-server on |CL|, plus learn a few basic redis commands. We also invite
you to pull our `Clear Linux Redis instance`_ on dockerhub\* for application
or infrastructure development.

While the `redis data structure store`_ can serve as a NoSQL database for a Web application, it's also easy to integrate in an existing stack. For example, you could use the Redis caching layer for real-time responses on a leaderboard in a gaming app. Redis offers many client libraries with language-specific bindings for Python, Perl, Ruby, and more.

.. contents::
   :local:
   :depth: 1

Prerequisites
*************
* Install the `redis-native` bundle in |CL|
* Install the `containers-basic` bundle in |CL| (only required in Example 2)

Install the redis bundle
************************

In |CL|, find redis in the `redis-native` bundle.

#. Open a Terminal and login as an administrative user.

#. Add :file:`redis-native`.

.. code-block:: bash

   sudo swupd bundle-add redis-native

.. note::

   If the bundle already exists, no action is required.

Start the redis-server
**********************

A `systemd` service unit is available to control the redis server.
By default, redis runs on port 6379.

#. Start the service.

   .. code-block:: bash

      systemctl start redis

   .. note::

      To stop redis run :command:`systemctl stop redis`.

#. Assure the service is running.

   .. code-block:: bash

      systemctl status redis

#. Verify the redis-server sends a reply.

   .. code-block:: bash

      redis-cli ping

   .. note::

      Expected output: `PONG`.

#. Optional: If you wish to apply advanced configuration, copy the
   `redis.conf` into /etc/ directory.

   .. code-block:: bash

      sudo cp /usr/share/defaults/etc/redis.conf /etc/

The redis-server is now ready to use on |CL|. Try some examples below.

Example 1: Use the redis-cli and try commands
*********************************************

One advantage of redis over other NoSQL databases is that developers can
easily access data structures like lists, sets, sorted sets, strings, and
hashes using collection operations commands similar to those found in many
programming languages. These exercises are inspired by `try redis io`_.

After your `redis-server` is running, try some basic commands.

#. Enter the `redis-cli`. It provides syntax suggestions as you type.

   .. code-block:: bash

      redis-cli

#. SET key to hold string value. In the set create connections and increment.

   .. code-block:: bash

      SET server:name "clearlinux"

   .. code-block:: bash

      MGET server:name

   .. note::
      If the key does not exist or hold a key value, `nil` is returned.

   .. code-block:: bash

      SET connections 100

   .. code-block:: bash

      INCR connections

   .. code-block:: bash

      INCR connections

   .. code-block:: bash

      DEL connections

#. Create a `friends` list and insert new values at the end of the list.

   .. code-block:: bash

      RPUSH friends "Deb"

   .. code-block:: bash

      RPUSH friends "David"

   .. code-block:: bash

      RPUSH friends "Mary"

#. Modify `friends` list, using a common slice method with a 0-index.

   .. code-block:: bash

      LRANGE friends 0 1

   .. code-block:: bash

      LLEN friends

   .. code-block:: bash

      LPOP friends

   .. code-block:: bash

      RPOP friends

   .. code-block:: bash

      LLEN friends

#. Consider using a hash, a very useful data type, which maps string fields
   and string values, offering multiple lookup methods.

   Enter many user key:values with `HMSET`. Then try `HGET` and `HGETALL`.

   .. code-block:: bash

      HMSET user:1000 name "Robert Noyce" password "SuperEngi9eer" email "robert.noyce@intel.com"

   .. code-block:: bash

      HGET user:1000 name

   .. code-block:: bash

      HGET user:1000 email

   .. code-block:: bash

      HGETALL user:1000


Example 2: Run the |CL| redis docker image
******************************************

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

* Learn to :ref:`docker`.

.. _try redis io: https://try.redis.io/

.. _Clear Linux Redis instance: https://hub.docker.com/r/clearlinux/redis

.. _redis data structure store: https://redis.io/

.. _redis quickstart tutorial: https://redis.io/topics/quickstart
