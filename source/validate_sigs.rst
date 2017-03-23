.. _validate_sigs:

Validating Signatures
#####################

|CLOSIA| offers a way to validate the content of an image or an update.
Validation of content works by creating a hash and then signing the hash.  If
the signature of the hash is valid, then that implies the content is valid.

This guide covers how to validate the content of an image, which is a manual
process, and the automatic process which occurs to validate an update that
``swupd`` performs in the background.

Image Content Validation
========================

For the outlined steps, the installer image of the latest release of |CL| is
used for illustrative purposes. You may use any image of |CL| you choose.

#. Download the image, the signature of the SHA512 sum of the image, and the certificate used
   to create signatures.

   .. code-block:: console

      # Image
      curl -O https://download.clearlinux.org/current/clear-$(curl https://download.clearlinux.org/latest)-installer.img.xz
      # Signature of SHA512 sum of image
      curl -O https://download.clearlinux.org/current/clear-$(curl https://download.clearlinux.org/latest)-installer.img.xz-SHA512SUMS.sig
      # Certificate
      curl -O https://download.clearlinux.org/releases/$(curl https://download.clearlinux.org/latest)/clear/ClearLinuxRoot.pem

#. Generate the ``sha256sum`` of the certificate.
   
   .. code-block:: console

      sha256sum ClearLinuxRoot.pem

#. Ensure the generated SHA256 sum of the certificate matches following SHA256
   sum to verify the integrity of the certificate.

   .. code-block:: console

      4b0ca67300727477913c331ff124928a98bcf2fb12c011a855f17cd73137a890  ClearLinuxRoot.pem

#. Generate the ``sha512sum`` of the image and save it to a file.
   
   .. code-block:: console

      sha512sum ./clear-$(curl https://download.clearlinux.org/latest)-installer.img.xz > sha512sum.out

   .. important::

      The ``./`` in the file name must be included.  This is part of the
      signature of the SHA512 sum of the image.  Without it, the validation will
      fail.

#. Ensure the signature of the SHA512 sum of the image sum was signed using the
   certificate.  This validates that the image is trusted and that it has not been
   modified.

   .. code-block:: console

      openssl smime -verify -in clear-$(curl https://download.clearlinux.org/latest)-installer.img.xz-SHA512SUMS.sig -inform der -content sha512sum.out -CAfile ClearLinuxRoot.pem

#. The output should be ``Verification successful``.  If the output contains
   ``bad_signature`` at all, then the image cannot be trusted.

Update Content Validation
=========================

All update content processed by ``swupd`` is validated automatically before
being applied.  What follows is the process ``swupd`` follows internally,
illustrated with manual steps:



#. A trusted certificate is distributed with all Clear Linux
   OS for Intel Architecture releases in :file:`/usr/share/clear/update-ca/ClearLinuxRoot.pem`.

#. ``swupd`` downloads the top-level manifest (MoM), as
   well as the signed :file:`MoM.sig` for the currently-installed
   image, and for the release being updated to in the case of an update.

#. ``swupd`` generates a ``sha256sum`` of the MoM.

#. ``swupd`` uses the :file:`MoM.sig` downloaded in step 1,
   as well as the ``sha256sum``; and, using the openssl API, it makes
   an equivalent call to the verification command:

   .. code-block:: c

      openssl smime -verify -in sha256sums.sig -inform der -content sha512sum.out -CAfile ClearLinuxRoot.pem

   Note that the actual API call is to ``PKCS7_verify())``.

#. With a successful verification, we can proceed to trust this
   MoM and its contents, which consist of hashes of the contents
   of all bundle manifests.

   * **Success** When a successful signature verification occurs, you
     should see the following message as part of the ``swupd``
     output:

     .. code-block:: console

        Signature check succeeded

   * **Fail** Should verification fail, you will see:

     .. code-block:: console

        WARNING!!! FAILED TO VERIFY SIGNATURE OF Manifest.MoM

#. As ``swupd`` then uses or installs bundle manifests, that
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