Erasure Code Support
####################

Overview of EC Support in Swift
-------------------------------

Erasure Code (EC) is implemented in Swift as a Storage Policy, see Storage Policies for complete details on Storage Policies. Because support is implemented as a Storage Policy, all of the storage devices associated with your cluster’s EC capability can be isolated. It is entirely possible to share devices between storage policies, but for EC it may make more sense to not only use separate devices but possibly even entire nodes dedicated for EC.

Which direction one chooses depends on why the EC policy is being deployed. If, for example, there is a production replication policy in place already and the goal is to add a cold storage tier such that the existing nodes performing replication are impacted as little as possible, adding a new set of nodes dedicated to EC might make the most sense but also incurs the most cost. On the other hand, if EC is being added as a capability to provide additional durability for a specific set of applications and the existing infrastructure is well suited for EC (sufficient number of nodes, zones for the EC scheme that is chosen) then leveraging the existing infrastructure such that the EC ring shares nodes with the replication ring makes the most sense. These are some of the main considerations:

- Layout of existing infrastructure.
- Cost of adding dedicated EC nodes (or just dedicated EC devices).
- Intended usage model(s).

The Swift code base does not include any of the algorithms necessary to perform the actual encoding and decoding of data; that is left to external libraries. The Storage Policies architecture is leveraged to enable EC on a per container basis – the object rings are still used to determine the placement of EC data fragments. Although there are several code paths that are unique to an operation associated with an EC policy, an external dependency to an Erasure Code library is what Swift counts on to perform the low level EC functions. The use of an external library allows for maximum flexibility as there are a significant number of options out there, each with its owns pros and cons that can vary greatly from one use case to another.

PyECLib: External Erasure Code Library
--------------------------------------
PyECLib is a Python Erasure Coding Library originally designed and written as part of the effort to add EC support to the Swift project, however it is an independent project. The library provides a well-defined and simple Python interface and internally implements a plug-in architecture allowing it to take advantage of many well-known C libraries such as:

- Jerasure and GFComplete at http://jerasure.org.
- **Intel(R) ISA-L** at http://01.org/intel%C2%AE-storage-acceleration-library-open-source-version.
- Or write your own!

Using an Erasure Code Policy
----------------------------
To use an EC policy, the administrator simply needs to define an EC policy in ``/etc/swift.conf`` and create/configure the associated object ring. An example of how an EC policy can be setup is shown below::

  [storage-policy:2]
  name = ec104
  policy_type = erasure_coding
  ec_type = jerasure_rs_vand
  ec_num_data_fragments = 10
  ec_num_parity_fragments = 4
  ec_object_segment_size = 1048576


Let’s take a closer look at each configuration parameter:

- ``name``: This is a standard storage policy parameter. See Storage Policies for details.
- ``policy_type``: Set this to erasure_coding to indicate that this is an EC policy.
- ``ec_type``: Set this value according to the available options in the selected PyECLib back-end. This specifies the EC scheme that is to be used. For example the option shown here selects Vandermonde Reed-Solomon encoding while an option of flat_xor_hd_3 would select Flat-XOR based HD combination codes. See the PyECLib page for full details.
- ``ec_num_data_fragments``: The total number of fragments that will be comprised of data.
- ``ec_num_parity_fragments``: The total number of fragments that will be comprised of parity.
- ``ec_object_segment_size``: The amount of data that will be buffered up before feeding a segment into the encoder/decoder. The default value is ``1048576``.
  
To create the EC policy’s object ring
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The only difference in the usage of the swift-ring-builder create command is the replicas parameter. The replicas value is the number of fragments spread across the object servers associated with the ring; replicas must be equal to the sum of ec_num_data_fragments and ec_num_parity_fragments. For example::

  swift-ring-builder object-1.builder create 10 14 1

Note that in this example the replicas value of 14 is based on the sum of 10 EC data fragments and 4 EC parity fragments.

Once you have configured your EC policy in ``/etc/swift.conf`` and created your object ring, your application is ready to start using EC simply by creating a container with the specified policy name and interacting as usual.

Migrating Between Policies
~~~~~~~~~~~~~~~~~~~~~~~~~~

A common usage of EC is to migrate less commonly accessed data from a more expensive but lower latency policy such as replication. When an application determines that it wants to move data from a replication policy to an EC policy, it simply needs to move the data from the replicated container to an EC container that was created with the target durability policy.

Region Support
~~~~~~~~~~~~~~

For at least the initial version of EC, it is not recommended that an EC scheme span beyond a single region, neither performance nor functional validation has be been done in such a configuration.
