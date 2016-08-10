.. _validate_sigs:

Validating Signatures
#####################

Clear Linux* OS for Intel® Architecture offers a way to validate signatures
to create verified build artifacts. Validations can be obtained by users and
by code to confirm that we are indeed dealing with official outputs.

Multiple types of artifacts have signing/verifying:

* Image checksums files; for example,  `release 8890`_ has 
    * ``clear-*.img.xz`` image files, 
    * ``clear-*.img.xz-SHA512SUMS`` checksum files, and
    * ``clear-*.img.xz-SHA512SUMS.sig`` signature files.
* The :command:`swupd` Manifest of Manifests (aka :abbr:`MoM (Manifest of Manifests)`)
  ``https://download.clearlinux.org/update/8890/`` has ``Manifest.MoM``
  and ``Manifest.MoM.sig`` signature file.

Verifying a Clear Linux OS for Intel Architecture image
=======================================================

Verification of images is done by humans when they download an image via the following steps:

#. Download the current ``ClearLinuxRoot.pem`` certificate; this is provided
   with the release being downloaded. For example, if you're interested in verifying
   the ``8970`` release, obtain the certificate from https://download.clearlinux.org/releases/8970/clear/ClearLinuxRoot.pem.
#. Download the desired OS image, as well as the ``[image]-SHA512SUMS.sig`` file.
#. Download and validate the release's OS ``ClearLinuxRoot.pem`` certificate:

     * Validate the certificate by comparing the downloaded certificate's
       ``sha256sum`` hash with what is published here:

        .. code-block:: console

           $ sha256sum ClearLinuxRoot.pem

        You should see this (accurate as of 2016-06-16 00:00 UTC):

        .. code-block:: console

           4b0ca67300727477913c331ff124928a98bcf2fb12c011a855f17cd73137a890  ClearLinuxRoot.pem

     * Now we verify that the signature file is valid, which also proves
       the OS image tarball is as trusted as the ``ClearLinuxRoot`` certificate. 
       To do this, create the **SHA512SUMS** file of the tarball. This is the
       content which is actually signed by the release team.

        .. code-block:: console

           $ sha512sum ./[image-####].img.xz > sha512sum.out

     * Finally, we can use :command:`openssl` to validate the signed
       :file:`SHA512SUMS.sig` was signed by the ``ClearLinuxRoot`` certificate:

        .. code-block:: console

            $ openssl smime -verify -in [image]-SHA512SUMS.sig -inform der -content sha512sum.out -CAfile ClearLinuxRoot.pem -out /dev/null

        After running this, you should see: :code:`Verification successful`.
        If you do not see this, you cannot be certain the OS you downloaded
        can be trusted.


Verification of the signed MoM
==============================

An overview of the mechanism used internal to :command:`swupd` 
(implemented in C calls to the openssl library API) is as follows:

#. A trusted certificate is distributed with all Clear Linux
   OS for Intel Architecture releases in :file:`/usr/share/clear/update-ca/ClearLinuxRoot.pem`.

#. :command:`swupd` downloads the top-level manifest (MoM), as
   well as the signed :file:`MoM.sig` for the currently-installed
   image, and for the release being updated to in the case of an update.

#. :command:`swupd` generates a ``sha256sum`` of the MoM.

#. :command:`swupd` uses the :file:`MoM.sig` downloaded in step 1,
   as well as the ``sha256sum``; and, using the openssl API, it makes
   an equivalent call to the verification command:

   .. code-block:: c

      openssl smime -verify -in sha256sums.sig -inform der -content sha512sum.out -CAfile ClearLinuxRoot.pem

   Note that the actual API call is to ``PKCS7_verify())``.

#. With a successful verification, we can proceed to trust this
   MoM and its contents, which consist of hashes of the contents
   of all bundle manifests.

   * **Success** When a successful signature verification occurs, you
     should see the following message as part of the :command:`swupd`
     output:

     .. code-block:: console

        Signature check succeeded

   * **Fail** Should verification fail, you will see:

     .. code-block:: console

        WARNING!!! FAILED TO VERIFY SIGNATURE OF Manifest.MoM

#. As :command:`swupd` then uses or installs bundle manifests, that
   bundle manifest hash is matched to the trusted MoM, extending the
   chain of trust from the MoM, to the bundle manifests, and out to
   every file installed. 

Clear Linux* OS for Intel® Architecture Public Key as of 06/16/2016 00:00 UTC
-----------------------------------------------------------------------------

.. code-block:: raw  

  -----BEGIN PUBLIC KEY-----
  MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAwfnY2m665SwYxr4/R+8L
  X1IMAkVYmvNiI5KmV815WvVQwUQDDCY1HUag+wb2BhTxkotKUdm6LGY1ck+Eb742
  rdICMToX+32vFM3XvIK16TKM6ficPsGA4xmbE/9qp01bn0O4MCwKjPAmxJkW+UOO
  L5u8p9VBZ1MYMnsRkECPZif/fULqIU73aYD3HYtcYEk1+N8n1AcNkpRY9p3Qd92M
  9aRlCNl1sb2g5DwSx9G0dWTS+YPchpclV7fBGQUiTuxb72hpVRE66CfR8tTd14np
  IbsKGq0S5PzkR9ubilDywFQ/6XPc1Rur/4g0rm6pPPx7DLQK3EqC8d4Z/C2nywje
  PwIDAQAB
  -----END PUBLIC KEY-----


You can re-create this when given a cert with the command:

.. code-block:: console

   $ openssl x509 -pubkey -noout -in ClearLinuxRoot.pem



.. _release 8890: https://download.clearlinux.org/releases/8890/clear/