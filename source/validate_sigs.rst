.. _validate_sigs:

Validating Signatures
#####################

|CLOSIA| offers a way to validate the content of an image or an update.
Validation of all content works by creating a hash and then signing the hash. If
the signature of the hash is valid, then that implies the content is valid by
creating a chain of trust.

This guide covers how to validate the content of an image, which is a manual
process, and the automatic process which occurs to validate an update that
``swupd`` performs internally.

Image Content Validation
========================

For the outlined steps, the installer image of the latest release of |CL| is
used for illustrative purposes. You may use any image of |CL| you choose.

#. Download the image, the signature of the SHA512 sum of the image, and the
   certificate used for signing the SHA512 sum.

   .. code-block:: console

      # Image
      curl -O https://download.clearlinux.org/current/clear-$(curl https://download.clearlinux.org/latest)-installer.img.xz
      # Signature of SHA512 sum of image
      curl -O https://download.clearlinux.org/current/clear-$(curl https://download.clearlinux.org/latest)-installer.img.xz-SHA512SUMS.sig
      # Certificate
      curl -O https://download.clearlinux.org/releases/$(curl https://download.clearlinux.org/latest)/clear/ClearLinuxRoot.pem

#. Generate the SHA256 sum of the certificate.

   .. code-block:: console

      sha256sum ClearLinuxRoot.pem

#. Ensure the generated SHA256 sum of the certificate matches following SHA256
   sum to verify the integrity of the certificate.

   .. code-block:: console

      4b0ca67300727477913c331ff124928a98bcf2fb12c011a855f17cd73137a890  ClearLinuxRoot.pem

#. Generate the SHA512 sum of the image and save it to a file.

   .. code-block:: console

      sha512sum ./clear-$(curl https://download.clearlinux.org/latest)-installer.img.xz > sha512sum.out

   .. important::

      The ``./`` in the file name must be included because it is part of the
      SHA512 sum of the image.  Without it, the validation of the signature of
      the image will fail.

#. Ensure the signature of the SHA512 sum of the image was signed using the
   certificate.  This validates that the image is trusted and that it has not
   been modified.

   .. code-block:: console

      openssl smime -verify -in clear-$(curl https://download.clearlinux.org/latest)-installer.img.xz-SHA512SUMS.sig -inform der -content sha512sum.out -CAfile ClearLinuxRoot.pem

#. The output should contain ``Verification successful``.  If the output
   contains ``bad_signature`` at all, then the image cannot be trusted.

Update Content Validation
=========================

All update content processed by ``swupd`` is validated automatically before
being applied.  What follows is the process ``swupd`` follows internally,
illustrated with manual steps for the latest release.  There is no need to
perform this manually as a part of performing a ``swupd update``.


#. Download the :abbr:`MoM (top-level manifest)` and the signature of the MoM.

   .. code-block:: console

      # MoM
      curl -O https://download.clearlinux.org/update/$(curl https://download.clearlinux.org/latest)/Manifest.MoM
      # Signature of MoM
      curl -O https://download.clearlinux.org/update/$(curl https://download.clearlinux.org/latest)/Manifest.sig

   .. note::

      The certificate used for signing the MoM is distributed with |CL| and can
      be found at ``/usr/share/clear/update-ca/Swupd_Root.pem``.  As a result,
      the integrity of the certificate does not need validated.  It is already
      trusted.

   .. note::

      The certificate used by ``swupd`` and the certificate used for the
      distribution are different because these are different entities that
      require separate identities.

#. Ensure the signature of the MoM was signed using the certificate.  This
   validates that the update content is trusted and that it has not been
   modified.

   .. code-block:: console

      openssl smime -verify -in sha256sums.sig -inform der -content Manifest.MoM -CAfile ClearLinuxRoot.pem

   .. note::

      The SHA512 sum of the MoM is not signed.  Instead, the MoM is signed
      directly because it is small in size compared to an image of |CL|.

#. The output should contain ``Verification successful``.  If the output
   contains ``bad_signature`` at all, then the MoM cannot be trusted.  Because
   the MoM contains a list of hashes for bundle manifests, if the MoM cannot be
   trustes, then bundle content cannot be trusted.