OpenStack* Telemetry - Verify Operation
############################################################

Verify Operation
------------------

Verify operation of the Telemetry service. These steps only include the Image service meters to reduce clutter. Environments with ceilometer integration for additional services contain more meters.


#. Source the ``admin`` credentials to gain access to admin-only CLI
   commands::

   	$ source admin-openrc.sh

#. List available meters::

    $ ceilometer meter-list
    +--------------+-------+-------+--------------------------------------+---------+------------+
    | Name         | Type  | Unit  | Resource ID                          | User ID | Project ID |
    +--------------+-------+-------+--------------------------------------+---------+------------+
    | image        | gauge | image | acafc7c0-40aa-4026-9673-b879898e1fc2 | None    | cf12a15... |
    | image.size   | gauge | B     | acafc7c0-40aa-4026-9673-b879898e1fc2 | None    | cf12a15... |
    +--------------+-------+-------+--------------------------------------+---------+------------+

#. Download the CirrOS image from the Image service::

    $ IMAGE_ID=$(glance image-list | grep 'cirros' | awk '{ print $2 }')
    $ glance image-download $IMAGE_ID > /tmp/cirros.img

#. List available meters again to validate detection of the image download::

    $ ceilometer meter-list
    +----------------+-------+-------+--------------------------------------+---------+------------+
    | Name           | Type  | Unit  | Resource ID                          | User ID | Project ID |
    +----------------+-------+-------+--------------------------------------+---------+------------+
    | image          | gauge | image | acafc7c0-40aa-4026-9673-b879898e1fc2 | None    | cf12a15... |
    | image.download | delta | B     | acafc7c0-40aa-4026-9673-b879898e1fc2 | None    | cf12a15... |
    | image.serve    | delta | B     | acafc7c0-40aa-4026-9673-b879898e1fc2 | None    | cf12a15... |
    | image.size     | gauge | B     | acafc7c0-40aa-4026-9673-b879898e1fc2 | None    | cf12a15... |
    +----------------+-------+-------+--------------------------------------+---------+------------+

#. Retrieve usage statistics from the image.download meter::

    $ ceilometer statistics -m image.download -p 60

    +--------+---------------------+---------------------+------------+------------+------------+------------+-------+----------+----------------------------+----------------------------+
    | Period | Period Start        | Period End          | Max        | Min        | Avg        | Sum        | Count | Duration | Duration Start             | Duration End               |
    +--------+---------------------+---------------------+------------+------------+------------+------------+-------+----------+----------------------------+----------------------------+
    | 60     | 2015-04-21T12:21:45 | 2015-04-21T12:22:45 | 13200896.0 | 13200896.0 | 13200896.0 | 13200896.0 | 1     | 0.0      | 2015-04-21T12:22:12.983000 | 2015-04-21T12:22:12.983000 |
    +--------+---------------------+---------------------+------------+------------+------------+------------+-------+----------+----------------------------+----------------------------+

#. Remove the previously downloaded image file /tmp/cirros.img::

    $ rm /tmp/cirros.img





