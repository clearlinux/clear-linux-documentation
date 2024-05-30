.. _kvm:

|CL-ATTR| on KVM
################

This page explains how to run |CL-ATTR| in a virtualized environment using
:abbr:`KVM (Kernel-based Virtual Machine)`.

.. contents::
   :local:
   :depth: 1

Install QEMU-KVM
****************

#. Enable the `Intel® Virtualization Technology`_ (Intel® VT) and the
   `Intel® Virtualization Technology for Directed I/O`_ (Intel® VT-d) in the
   host machine’s BIOS.

#. Log in and open a terminal emulator.

#. Install `QEMU*-KVM` on the host machine. Below are some example distros.

   * On |CL|:

     .. code-block:: bash

        sudo swupd bundle-add kvm-host

   * On Ubuntu\* 18.04 LTS Desktop:

     .. code-block:: bash

        sudo apt-get install qemu-kvm

   * On Mint\* 19.1 “Cinnamon” Desktop:

     .. code-block:: bash

        sudo apt-get install qemu-kvm

   * On Fedora\* 30 Workstation:

     .. code-block:: bash

        sudo dnf install qemu-kvm

Download and launch the virtual machine
***************************************

#. Download the latest pre-built |CL| KVM image file from
   the `image <https://cdn.download.clearlinux.org/image/>`_ directory. Look for
   ``clear-<version>-kvm.img.xz``.  You can also use this command:

   .. code-block:: bash

      curl -O https://cdn.download.clearlinux.org/image/$(curl https://cdn.download.clearlinux.org/image/latest-images | grep '[0-9]'-kvm'\.')

#. Uncompress the downloaded image:

   .. code-block:: bash

      unxz -v clear-<version>-kvm.img.xz

#. Download the 3 OVMF files (`OVMF.fd`, `OVMF_CODE.fd`, `OVMF_VARS.fd`) that
   provides UEFI  support for virtual machines.

   .. code-block:: bash

      curl -O https://cdn.download.clearlinux.org/image/OVMF.fd
      curl -O https://cdn.download.clearlinux.org/image/OVMF_CODE.fd
      curl -O https://cdn.download.clearlinux.org/image/OVMF_VARS.fd

   .. note::

      The default OVMF files from |CL| may not work for some distro version(s).
      You may get an `ASSERT` in the `debug.log` file when starting the VM.
      If that is the case, use the distro-specific-OVMF files instead.
      For example, the |CL| OVMF files work for Ubuntu 18.04 LTS, but not for Ubuntu 19.04 LTS.
      Installing and using the OVMF files for Ubuntu 19.04 LTS resolved the `ASSERT` issue.

#. Download the `start_qemu.sh`_ script from the
   `image <https://cdn.download.clearlinux.org/image/>`_ directory.  This script
   will launch the |CL| VM and provide console interaction within the same
   terminal emulator window.

   .. code-block:: bash

      curl -O https://cdn.download.clearlinux.org/image/start_qemu.sh

#. Make the script executable:

   .. code-block:: bash

      chmod +x start_qemu.sh

#. Start the |CL| KVM virtual machine:

   .. code-block:: bash

      sudo ./start_qemu.sh clear-<version>-kvm.img

#. Log in as ``root`` user and set a new password.

SSH access into the virtual machine
***********************************

To interact with the |CL| VM through SSH instead of the console it was
launched from, follow these steps.

#. Configure SSH in the |CL| VM to allow root login:

   .. code-block:: bash

      cat > /etc/ssh/sshd_config << EOF
        PermitRootLogin yes
        EOF

#. Enable and start SSH server in the |CL| VM:

   .. code-block:: bash

      systemctl enable sshd
      systemctl start sshd

#. Determine the IP address of the host on which you will launch the VM.
   Substitute <ip-addr-of-kvm-host> in the next step with this information.

   .. code-block:: bash

      ip a

#. SSH into the |CL| VM using the default port of  `10022`:

   .. code-block:: bash

      ssh -p 10022 root@<ip-addr-of-kvm-host>

Optional: Add the GNOME Display Manager (GDM)
*********************************************

To add :abbr:`GDM (GNOME Display Manager)` to the |CL| VM, follow these steps:

#. Shutdown the active |CL| VM.

   .. code-block:: bash

      poweroff

#. Install the Spice viewer on the local host or remote system. Below are some
   example distros.

   * On Clear Linux:

     .. code-block:: bash

        sudo swupd bundle-add virt-viewer

   * On Ubuntu\* 18.04 LTS Desktop:

     .. code-block:: bash

        sudo apt-get install virt-viewer

   * On Mint\* 19.1 “Cinnamon” Desktop:

     .. code-block:: bash

        sudo apt-get install virt-viewer

   * On Fedora\* 30 Workstation:

     .. code-block:: bash

        sudo dnf install virt-viewer

#. Modify the :file:`start_qemu.sh` script to increase memory (`-m`), add
   graphics driver (`-vga`), and add Spice (`-spice`, `-usb`, and
   `-device`) support.

   .. code-block:: console

      qemu-system-x86_64 \
          -enable-kvm \
          ${UEFI_BIOS} \
          -smp sockets=1,cpus=4,cores=2 -cpu host \
          -m 4096 \
          -vga qxl \
          -nographic \
          -spice port=5924,disable-ticketing \
          -usb \
          -device usb-tablet,bus=usb-bus.0 \
          -drive file="$IMAGE",if=virtio,aio=threads,format=raw \
          -netdev user,id=mynet0,hostfwd=tcp::${VMN}0022-:22,hostfwd=tcp::${VMN}2375-:2375 \
          -device virtio-net-pci,netdev=mynet0 \
          -debugcon file:debug.log -global isa-debugcon.iobase=0x402 $@

#. Due to changes in the :file:`start_qemu.sh` script from the previous step,
   using the same OVMF files will result in the VM not booting properly and
   you end up in the the UEFI shell.  The easiest way to avoid this is to delete
   the OVMF files and restore the originals before relaunching the VM.

#. Increase the size of the VM by 10GB to accommodate the GDM installation:

   .. code-block:: bash

      qemu-img resize -f raw clear-<version>-kvm.img +10G

#. Relaunch the |CL| VM:

   .. code-block:: bash

      sudo ./start_qemu.sh clear-<version>-kvm.img

#. Determine the IP address of the host on which you will launch the VM.
   Substitute <ip-addr-of-kvm-host> in the next step with this information.

   .. code-block:: bash

      ip a

#. From the local host or remote system, open a new terminal emulator window
   and connect into the |CL| VM using the Spice viewer:

   .. code-block:: bash

      remote-viewer spice://<ip-address-of-kvm-host>:5924

#. Log in as `root` user into the |CL| VM.

#. Follow these steps from :ref:`increase-virtual-disk-size` to resize the partition of the virtual disk of the VM.

#. Add GDM to the |CL| VM:

   .. code-block:: bash

      swupd bundle-add desktop-autostart

#. Reboot the |CL| VM to start GDM:

   .. code-block:: bash

      reboot

#. Go through the GDM out-of-box experience (OOBE).

#. The default aspect ratio of the GDM GUI for the |CL| VM is 4:3. To change
   it, use GDM's `Devices > Displays` setting tool (located at the top-right corner).


.. _Intel® Virtualization Technology: https://www.intel.com/content/www/us/en/virtualization/virtualization-technology/intel-virtualization-technology.html
.. _Intel® Virtualization Technology for Directed I/O: https://software.intel.com/en-us/articles/intel-virtualization-technology-for-directed-io-vt-d-enhancing-intel-platforms-for-efficient-virtualization-of-io-devices
.. _start_qemu.sh: https://cdn.download.clearlinux.org/image/start_qemu.sh
