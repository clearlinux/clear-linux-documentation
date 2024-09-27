.. _yubikey-u2f:

YubiKey\* Support
#################

This tutorial explains how to configure a YubiKey\* for U2F authentication
through a web browser on a |CL-ATTR| system.

.. contents:: :local:
   :depth: 1

Description
***********

YubiKey is a USB security token manufactured by `Yubico`_. Depending on the
model, a YubiKey can support different authentication protocols including
One-Time Password (OTP), Smart card, FIDO2, and Universal 2nd Factor (U2F).

A list of `websites that accept U2F authentication with the YubiKey`_
is available on the Yubico website. See the Yubico website to learn more about
the Yubikey: https://www.yubico.com/getstarted/

Prerequisites
*************

This tutorial assumes you have:

#. |CL| installed and running.

#. Mozilla Firefox installed on |CL|.

#. A YubiKey.

Enable Linux udev rules for YubiKey
***********************************

:command:`udev` is the Linux device manager that handles events when USB
devices are added and removed. Custom rules needs to be created to properly
identify the YubiKey and provide applications access.

These instructions are derived from: `Yubico support article Using Your U2F
YubiKey with Linux
<https://support.yubico.com/support/solutions/articles/15000006449>`_


#. Create the udev rules folder under :file:`/etc`.

   .. code:: bash

      sudo mkdir -p /etc/udev/rules.d/


#. Download the u2f rules from the Yubico GitHub:

   .. code:: bash

      curl -O https://raw.githubusercontent.com/Yubico/libu2f-host/master/70-u2f.rules


#. Move the downloaded :file:`70-u2f.rules` file into the :file:`/etc/udev`
   folder.

   .. code:: bash

      sudo mv 70-u2f.rules /etc/udev/rules.d/


#. The udev rules should automatically be reloaded. However, they can be
   manually reloaded or you can reboot the system.

   .. code:: bash

      sudo udevadm control --reload-rules && sudo udevadm trigger


#. Plugin and validate the YubiKey appears as a USB device.

   .. code:: bash

      lsusb



Enable U2F in Mozilla Firefox
*****************************

Firefox comes with U2F web authentication support disabled by default. U2F
needs to be enabled in the advanced settings.

These instructions are derived from: `Yubico support article Enabling U2F
support in Mozilla Firefox
<https://support.yubico.com/support/solutions/articles/15000017511-enabling-u2f-support-in-mozilla-firefox>`_


#. Launch Mozilla Firefox

#. In the URL bar, type :command:`about:config` to access the advanced
   settings.

   .. code:: bash

      about:config

#. Click the *I accept the risk!* button to continue to the advanced settings

#. Search for the :command:`security.webauth.u2f` and double-click it
   so *Value* becomes **true**.


Your YubiKey is now usable on |CL| with Mozilla Firefox with websites that
support U2F authentication.


Related topics
**************

- |CL| :ref:`security`


.. _`Yubico`: https://www.yubico.com/

.. _`websites that accept U2F authentication with the YubiKey`:
.. https://www.yubico.com/works-with-yubikey/catalog/#protocol=universal-2nd-factor-(u2f)&usecase=all&key=all
