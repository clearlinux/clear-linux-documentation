.. _validate_sigs:

Validating Signatures
#####################

Clear Linux offers a way to validate signatures to create verifiable build 
artifacts. Validations can be obtained by users and by code to confirm
that we are indeed dealing with official ClearLinux outputs. 

Multiple types of artifacts have signing/verifying:

* Image checksums files; for example, the release
  ``https://download.clearlinux.org/releases/8890/clear/`` has ``clear-*.img.xz``
  image files, ``clear-*.img.xz-SHA512SUMS`` checksum files, and 
  ``clear-*.img.xz-SHA512SUMS.sig`` signature files.
.. * Software Update :command:`swupd`; :abbr:`Manifest of Manifests (MoM)`: 
  ``https://download.clearlinux.org/update/8890/`` has ``Manifest.MoM`` and
  ``Manifest.MoM.sig`` validations. ..

Verifying a Clear OS Image
==========================

Verification of images is done by humans when they download an image via the following steps:

#. Download the current Clear Linux public ``.pem`` certificate; this is provided
   with the release being downloaded. For example, if you're interested in verifying
   the ``8970`` release, obtain the certificate from `https://download.clearlinux.org/releases/8970/clear/ClearLinuxRoot.pem`_.
#. Download the desired OS image, as well as the ``[image]-SHA512SUMS.sig`` file
   to a directory. For simplification purposes here, we'll call it ``~/download``
#. Download and validate the release's OS ``ClearLinuxRoot.pem`` certificate:

     * Validate the certificate by comparing the downloaded certificate's
       ``sha256sum`` hash with what is published here:

        .. code-block:: console

           $ sha256sum ClearLinuxRoot.pem

        You should see this:

        .. code-block:: console_output

           4b0ca67300727477913c331ff124928a98bcf2fb12c011a855f17cd73137a890  ClearLinuxRoot.pem

     * Now we verify that the signature file is valid, which also proves
       the OS image tarball is as trusted as the ClearLinuxRoot certificate
       that we have in ``~/download``. To do this, create the **SHA512SUMS**
       file of the tarball. This is the content which is actually signed by
       the Clear Linux release team.

        .. code-block:: console

           $ sha512sum [image].tar.xz > sha512sum.out

     * Finally, we can use openssl to validate the signed :file:`SHA512SUMS.sig`
       was signed by the Clear Linux Root certificate:

        .. code-block:: console

            $ openssl smime -verify -in [image]-SHA512SUMS.sig -inform der -content sha512sum.out -CAfile ClearLinuxRoot.pem -out /dev/null

        After running this, you should see: :code:`Verification successful`.
        If you do not see this, you cannot be certain the OS you downloaded
        can be trusted.
