Running in a virtualized environment
##########################################################################

The easiest way to get started running Clear Linux* OS for Intel® Architecture in a virtualized
environment is to download a recent KVM image from the `image
directory <http://download.clearlinux.org/image/>`_. This directory
contains an image file, the UEFI firmware helper and the KVM start
helper script.

Starter script
~~~~~~~~~~~~~~

To start the image, run the ``start_qemu.sh`` script from
`here <http://download.clearlinux.org/image/start_qemu.sh>`_, or modify
the following script for your needs and run it from the command line
with ``$ script clr_image``.

::

     
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

To run this script, connect from host via SSH. Take note that SSH is not
enabled by default. To enable it, log in through serial console with the
username ``root``. After setting the password, enable root login via SSH
by configuring ``/etc/ssh/sshd_config`` with this content:

::

    PermitRootLogin yes

Now you may connect from host via SSH through 2223:

::

    $ ssh -p 2223 root@localhost

Alternately, there are a few other ways to approach this.

-  To run the script without modifying its permissions:

   ::

       $ bash start_qemu.sh clr_image

-  To run it as a background process:

   ::

       $ `bash start_qemu.sh clr_image` &

-  If you'd like to run the script with execute permission:

   ::

       $ chmod +x start_qemu.sh
       $ ./start_qemu.sh clr_image

-  And to run it as a background process:

   ::

       $ `./start_qemu.sh clr_image` &
