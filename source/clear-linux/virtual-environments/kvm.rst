.. _kvm:

Running Clear Linux as a KVM guest OS
#####################################

This section explains how to run |CLOSIA| in a virtualized environment using
abbr:`KVM (Kernel-based Virtual Machine)`.

Install QEMU-KVM
===========

#. Enable `Intel® Virtualization Technology`_ (Intel® VT) and
   `Intel®Virtualization Technology for Directed I/O`_ (Intel® VT-d) in the
   host machine’s BIOS.

#. Log in and get root privilege on the host machine:

   .. code-block:: console

    $ sudo -s

#. Install `QEMU-KVM` on the host machine. Below are some example distros.

   * |CL|:

     .. code-block:: console

        # swupd bundle-add desktop-autostart kvm-host

   * Ubuntu 16.04 LTS Desktop:

     .. code-block:: console

        # apt-get install qemu-kvm

   * Mint 18.1 “Serena” Desktop:

     .. code-block:: console

        # apt-get install qemu-kvm

   * Fedora 25 Workstation:

     .. code-block:: console

        # dnf install qemu-kvm

Download and Launch |CL| VM
========================

#. Download the latest pre-built Clear Linux _`KVM image` file from
   the _`image` directory.

#. Uncompress the downloaded image

   .. code-block:: console

      unxz clear-<version number>-kvm.img.xz

#. Download the :file:`OVMF.fd` file that provides UEFI support for
   virtual machines from the _`images` directory.

#. Download the sample _`QEMU-KVM launcher` script from the _`image` directory.

#. Make the script executable

   .. code-block:: console

      # chmod +x start_qemu.sh

#. Start the |CL| KVM virtual machine:

     .. code-block:: console

        # ./start_qemu.sh clear-<version number>-kvm.img

#. Log in and set the root password.

#. To SSH into the |CL| VM, follow these steps:

    a. Enable SSH access in the |CL| VM

       .. code-block:: console

          # cat > /etc/ssh/sshd_config << EOF
            PermitRootLogin yes
            EOF

    b. From the host, SSH into the Clear Linux VM:

       .. code-block:: console

          # ssh -p 10022 root@localhost

Add GNOME Display Manager
=========================

To add the GNOME Display Manager (GDM) to the |CL| VM, follow these steps:

#. Shutdown the active |CL| VM.

#. Install VNCViewer on the host machine.  Below are some example distros.

   * On Clear Linux:

     .. code-block:: console

        # swupd bundle-add desktop-apps 

   * On Ubuntu 16.04 LTS Desktop:

     .. code-block:: console

        # apt-get vncviewer

   * On Mint 18.1 “Serena” Desktop:

     .. code-block:: console

        # apt-get vncviewer

   * On Fedora 25 Workstation:

     .. code-block:: console

        # dnf install tigervnc

#. Modify the :file:`start_qemu.sh` script to increase memory (-m), add
   graphics driver (-vga), and add VNC (-vnc and -usbdevice) support.

   .. code-block:: console

      qemu-system-x86_64 \
          -enable-kvm \
          -bios OVMF.fd \
          -smp sockets=1,cpus=4,cores=2 -cpu host \
          -m 4096 \
          -vga qxl \
          -vnc :0 -nographic \
          -usbdevice tablet \
          -drive file="$IMAGE",if=virtio,aio=threads,format=raw \
          -netdev user,id=mynet0,hostfwd=tcp::${VMN}0022-
          :22,hostfwd=tcp::${VMN}2375-:2375 \
          -device virtio-net-pci,netdev=mynet0 \
          -debugcon file:debug.log -global isa-debugcon.iobase=0x402 $@

Reset UEFI NvVars information
=============================

Due to changes in :file:`start_qemu.sh` script, the UEFI :file:`NvVars`
information for the previously-booted |CL| VM will need to be reset.

#. Relaunch the |CL| VM.  The EFI shell will appear:

   .. code-block:: console

      # ./start_qemu.sh clear-<version number>-kvm.img

#. At the UEFI shell, delete the :file:`NvVars` file:

   .. code-block:: console

      Shell> del FS0:\NvVars

#. Proceed with booting the |CL| VM:

   .. code-block:: console

      Shell> FS0:\EFI\Boot\BOOTX64.EFI

Enable GNOME Display Manager
============================

#. From the host machine, VNC into the |CL| VM:

   .. code-block:: console

      # vncviewer 0.0.0.0

#. Log into the |CL| VM.

#. Get root privilege:

   .. code-block:: console

      $ sudo -s

#. Add GDM to |CL| VM:

   .. code-block:: console

      # swupd bundle-add desktop-autostart

#. Reboot the |CL| VM to enable GDM:

   .. code-block:: console

      # reboot

.. _Intel® Virtualization Technology: https://www.intel.com/content/www/us/en/virtualization/virtualization-technology/intel-virtualization-technology.html
.. _Intel®Virtualization Technology for Directed I/O: https://software.intel.com/en-us/articles/intel-virtualization-technology-for-directed-io-vt-d-enhancing-intel-platforms-for-efficient-virtualization-of-io-devices
.. _image: https://download.clearlinux.org/image/
.. _QEMU-KVM launcher: https://download.clearlinux.org/image/start_qemu.sh
