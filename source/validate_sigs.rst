.. _validate_sigs:

Validating signatures
#####################

|CLOSIA| offers a way to validate the content of an image or an update. All
validation of content works by creating and signing a hash. A valid signature
creates a chain of trust.  A broken chain of trust, seen as an invalid
signature, means the content is not valid.

This guide covers how to validate the contents of an image, which is a manual
process, and describes the automatic process ``swupd`` performs internally to
validate an update.

Image content validation
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

#. Generate the SHA256 sum for the certificate.

   .. code-block:: console

      sha256sum ClearLinuxRoot.pem

#. Ensure the generated SHA256 sum of the certificate matches following
   SHA256 sum to verify the integrity of the certificate.

   .. code-block:: console

      4b0ca67300727477913c331ff124928a98bcf2fb12c011a855f17cd73137a890 ClearLinuxRoot.pem

#. Generate the SHA512 sum of the image and save it to a file.

   .. code-block:: console

      sha512sum ./clear-$(curl https://download.clearlinux.org/latest)-installer.img.xz > sha512sum.out

   .. important::

      The ``./`` in the file name must be included because it is part of the
      SHA512 sum of the image. Without it, the validation of the signature
      of the image will fail.

#. Ensure the signature of the SHA512 sum of the image was created using the
   certificate. This validates the image is trusted and it has not been
   modified.

   .. code-block:: console

      openssl smime -verify -in clear-$(curl https://download.clearlinux.org/latest)-installer.img.xz-SHA512SUMS.sig -inform der -content sha512sum.out -CAfile ClearLinuxRoot.pem

#. The output should contain ``Verification successful``.  If the output
   contains ``bad_signature`` anywhere, then the image is not trustworthy.

Update content validation
=========================

``swupd`` validates all update content automatically before applying the
update content. The process ``swupd`` follows internally is illustrated here
with manual steps using the latest |CL| release. There is no need to perform
these steps manually when performing a ``swupd update``.

#. Download the :abbr:`MoM (top-level manifest)` and the signature of the
   MoM.

   .. code-block:: console

      # MoM
      curl -O https://download.clearlinux.org/update/$(curl https://download.clearlinux.org/latest)/Manifest.MoM
      # Signature of MoM
      curl -O https://download.clearlinux.org/update/$(curl https://download.clearlinux.org/latest)/Manifest.sig

   .. note::

      The certificate used for signing the MoM is distributed with |CL|
      at :file:`/usr/share/clear/update-ca/Swupd_Root.pem`. As a result, the
      integrity of the certificate does not require validation; it is already
      trusted.

   .. note::

      The certificate used by ``swupd`` and the certificate used for the
      distribution's image are different because these are different entities
      requiring separate identities.

#. Ensure the signature of the MoM was created using the certificate. This
   signature validates the update content is trustworthy and has not been
   modified.

   .. code-block:: console

      openssl smime -verify -in sha256sums.sig -inform der -content Manifest.MoM -CAfile ClearLinuxRoot.pem

   .. note::

      The SHA512 sum of the MoM is not signed. Instead, the MoM is signed
      directly because it is small in size compared to an image of |CL|.

#. The output should contain ``Verification successful``.  If the output
   contains ``bad_signature`` anywhere, then the MoM cannot be trusted.
   Because the MoM contains a list of hashes for bundle manifests, if the MoM
   cannot be trusted, then the bundle content cannot be trusted.