.. _validate-signatures:

Validate signatures
###################


This guide describes how to validate the contents of a |CL-ATTR| image.

.. contents::
   :local:
   :depth: 1

Overview
********

Validating the contents of an image is a manual process and is the same process
that :ref:`swupd-guide` performs internally.

|CL| offers a way to validate the content of an image or an update. All
validation of content works by creating and signing a hash. A valid signature
creates a chain of trust. A broken chain of trust, seen as an invalid
signature, means the content is not valid.


.. _image-content-validation:

Image content validation
************************

In the steps below, we used the installer image of the latest release
of |CL|. You may use any image of |CL| you choose.

#. Download the image, the signature of the SHA512 sum of the image, and the
   |CL| certificate used for signing the SHA512 sum.

   .. code-block:: console

      # Image
      curl -O https://cdn.download.clearlinux.org/current/clear-$(curl https://cdn.download.clearlinux.org/latest)-installer.img.xz
      # Signature of SHA512 sum of image
      curl -O https://cdn.download.clearlinux.org/current/clear-$(curl https://cdn.download.clearlinux.org/latest)-installer.img.xz-SHA512SUMS.sig
      # Certificate
      curl -O https://cdn.download.clearlinux.org/releases/$(curl https://cdn.download.clearlinux.org/latest)/clear/ClearLinuxRoot.pem

#. Generate the SHA256 sum of the |CL| certificate.

   .. code-block:: console

      sha256sum ClearLinuxRoot.pem

#. Ensure the generated SHA256 sum of the |CL| certificate matches the
   following SHA256 sum to verify the integrity of the certificate.

   .. code-block:: console

      4b0ca67300727477913c331ff124928a98bcf2fb12c011a855f17cd73137a890  ClearLinuxRoot.pem

#. Generate the SHA512 sum of the image and save it to a file.

   .. code-block:: console

      sha512sum clear-$(curl https://cdn.download.clearlinux.org/latest)-installer.img.xz > sha512sum.out

#. Ensure the signature of the SHA512 sum of the image was created using the
   |CL| certificate. This confirms that the image is trusted and has not
   been modified.

   .. code-block:: console

      openssl smime -verify -purpose any -in clear-$(curl https://cdn.download.clearlinux.org/latest)-installer.img.xz-SHA512SUMS.sig -inform der -content sha512sum.out -CAfile ClearLinuxRoot.pem

   .. note::

      The :command:`-purpose any` option is required when using OpenSSL 1.1.
      If you use an earlier version of OpenSSL, omit this option to perform
      signature validation.  The :command:`openssl version` command may be used
      to determine the version of OpenSSL in use.

#. The output should contain "Verification successful". If the output
   contains "bad_signature" anywhere, then the image is not trustworthy.

Update content validation
*************************

**swupd** validates all update content automatically before applying the
update content. The process swupd follows internally is illustrated here
with manual steps using the latest |CL| release. There is no need to perform
these steps manually when performing a :command:`swupd update`.

#. Download the :abbr:`MoM (top-level manifest)`, the signature of the MoM,
   and the Swupd certificate used for signing the signature of the MoM.

   .. code-block:: console

      # MoM
      curl -O https://cdn.download.clearlinux.org/update/$(curl https://cdn.download.clearlinux.org/latest)/Manifest.MoM
      # Signature of MoM
      curl -O https://cdn.download.clearlinux.org/update/$(curl https://cdn.download.clearlinux.org/latest)/Manifest.MoM.sig
      # Swupd certificate
      curl -O https://cdn.download.clearlinux.org/releases/$(curl https://cdn.download.clearlinux.org/latest)/clear/Swupd_Root.pem

#. Generate the SHA256 sum of the swupd certificate.

   .. code-block:: console

      sha256sum Swupd_Root.pem

#. Confirm that the generated SHA256 sum of the swupd certificate matches the
   SHA256 sum shown below to verify the integrity of the certificate.

   .. code-block:: console

      ff06fc76ec5148040acb4fcb2bc8105cc72f1963b55de0daf3a4ed664c6fe72c  Swupd_Root.pem

#. Confirm that the signature of the MoM was created using the Swupd
   certificate. This signature validates the update content is trustworthy and 
   has not been modified.

   .. code-block:: console

      openssl smime -verify -purpose any -in Manifest.MoM.sig -inform der -content Manifest.MoM -CAfile Swupd_Root.pem

   .. note::

      The :command:`-purpose any` option is required when using OpenSSL 1.1.
      If you use an earlier version of OpenSSL, omit this option to perform
      signature validation.  The :command:`openssl version` command may be used
      to determine the version of OpenSSL in use.

   .. note::

      The SHA512 sum of the MoM is not generated and then signed. Instead, the
      MoM is signed directly because it is small in size compared to an image of
      |CL|.

#. The output should contain "Verification successful". If the output
   contains "bad_signature" anywhere, then the MoM cannot be trusted.
   Because the MoM contains a list of hashes for bundle manifests, if the MoM
   cannot be trusted, then the bundle content cannot be trusted.
