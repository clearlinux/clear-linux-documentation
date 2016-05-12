.. _vm-kvm:

Using KVM
#########

The easiest way to get started in a virtualized environment is to download
a recent KVM image from the `images`_ directory. Here you'll find a kvm
image file, the UEFI firmware helper, and the KVM start helper script.


Starter script
==============

To start the image, run the `qemu shell script`_ script available in the
`images`_ directory, or modify the following script for your needs and run it
from the command line with ``$ [script name] clr_image``

.. code-block:: bash

    #!/bin/bash
    if [ $#  -eq 0 ] ; then
      echo "Please provide an image to emulate as first argument"
      exit 1
    fi
    image=$1
    shift
    # FIXME: Add a proper MAC address
    macaddr=XX:XX:XX:XX:XX:XX
    qemu-system-x86_64 \
        -usb -device usb-kbd \
        -cpu qemu64,+vmx \
        -enable-kvm \
        -m 512m -bios OVMF.fd \
        -drive file="$image",index=0,if=ide \
        -net nic,model=e1000,macaddr=$macaddr \
        -net user,hostfwd=tcp::2223-:22 \
        -monitor stdio "$@"


SSH is needed for remote logins; however, SSH not enabled by default. To enable
it, log in through serial console with the username ``root``. After setting the
password, enable root login via SSH by configuring :file:`/etc/ssh/sshd_config`
with this line::

    PermitRootLogin yes

Now you may connect from host via SSH through 2223::

    $ ssh -p 2223 root@localhost

Alternatively, there are a few other ways to approach this.

*  To run the script without modifying its permissions::

   $ bash start_qemu.sh clr_image

*  To run it as a background process::

   $ bash start_qemu.sh clr_image &

*  If you'd like to run the script with execute permission::

   $ chmod +x start_qemu.sh
   $ ./start_qemu.sh clr_image

*  And to run it as a background process::

   $ ./start_qemu.sh clr_image &

If you run into any trouble with qemu getting locked up, try editing the `qemu shell script`_
and removing the ``aio=threads``


.. _qemu shell script: http://download.clearlinux.org/image/start_qemu.sh
.. _images: http://download.clearlinux.org/image/