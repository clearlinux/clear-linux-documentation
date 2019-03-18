.. _kvm:

Run |CL-ATTR| as a KVM guest OS
###############################

This section explains how to run |CL-ATTR| in a virtualized environment using
:abbr:`KVM (Kernel-based Virtual Machine)`.

Install QEMU-KVM
****************

#. Enable the `Intel® Virtualization Technology`_ (Intel® VT) and the
   `Intel®Virtualization Technology for Directed I/O`_ (Intel® VT-d) in the
   host machine’s BIOS.

#. Log in, open a terminal emulator, and get root privilege on the host
   machine:

   .. code-block:: bash

      sudo -s

#. Install `QEMU*-KVM` on the host machine. Below are some example distros.

   * On |CL|:

     .. code-block:: bash

        swupd bundle-add desktop-autostart kvm-host

   * On Ubuntu\* 16.04 LTS Desktop:

     .. code-block:: bash

        apt-get install qemu-kvm

   * On Mint\* 18.1 “Serena” Desktop:

     .. code-block:: bash

        apt-get install qemu-kvm

   * On Fedora\* 25 Workstation:

     .. code-block:: bash

        dnf install qemu-kvm

Download and launch the virtual machine
***************************************

#. Download the latest pre-built |CL| KVM image file from
   the `image <https://cdn.download.clearlinux.org/image/>`_ directory. Look for
   ``clear-<version>-kvm.img.xz``.  You can also use this command: 

   .. code-block:: bash

      curl -O https://cdn.download.clearlinux.org/image/$(curl https://cdn.download.clearlinux.org/image/latest-images | grep '[0-9]'-kvm)

#. Uncompress the downloaded image:

   .. code-block:: bash

      unxz clear-<version>-kvm.img.xz

#. Download the `OVMF file`_ file that provides UEFI support for
   virtual machines from the `image <https://cdn.download.clearlinux.org/image/>`_ directory.

#. Copy :file:`OVMF.fd` to the working directory, as shown below.

   .. code-block:: bash

      cp /usr/share/qemu/OVMF.fd <working_directory>

   .. note::

      Replace <working_directory> with your own.

      For non-Clear Linux hosts, the preferred approach is to download it from https://cdn.download.clearlinux.org/image/OVMF.fd

#. Download the sample `QEMU-KVM launcher`_ script from the
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

      ./start_qemu.sh clear-<version>-kvm.img

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

#. Start SSH server in the |CL| VM:

   .. code-block:: bash

      systemctl start sshd

#. From the host, SSH into the |CL| VM.  The port number ``10022`` is defined
   in the ``start_qemu.sh`` script.  

   .. code-block:: bash

      ssh -p 10022 root@localhost

Add the GNOME Display Manager (GDM)
***********************************

To add :abbr:`GDM (GNOME Display Manager)` to the |CL| VM, follow these steps:

#. Shutdown the active |CL| VM.

   .. code-block:: bash

      shutdown now
          
#. Install a VNC viewer on the host machine.  Below are some example distros.

   * On Clear Linux:

     .. code-block:: bash

        swupd bundle-add tigervnc

   * On Ubuntu\* 16.04 LTS Desktop:

     .. code-block:: bash

        apt-get install vncviewer

   * On Mint\* 18.1 “Serena” Desktop:

     .. code-block:: bash

        apt-get install vncviewer

   * On Fedora\* 25 Workstation:

     .. code-block:: bash

        dnf install tigervnc

#. Modify the :file:`start_qemu.sh` script to increase memory (``-m``), add
   graphics driver (``-vga``), and add VNC (``-vnc``, ``-usb``, and
   ``-device``) support.

   .. code-block:: console

      qemu-system-x86_64 \
          -enable-kvm \
          -bios OVMF.fd \
          -smp sockets=1,cpus=4,cores=2 -cpu host \
          -m 4096 \
          -vga qxl \
          -vnc :0 -nographic \
          -usb \
          -device usb-tablet \
          -drive file="$IMAGE",if=virtio,aio=threads,format=raw \
          -netdev user,id=mynet0,hostfwd=tcp::${VMN}0022-:22,hostfwd=tcp::${VMN}2375-:2375 \
          -device virtio-net-pci,netdev=mynet0 \
          -debugcon file:debug.log -global isa-debugcon.iobase=0x402 $@

#. Due to changes in the :file:`start_qemu.sh` script from the previous step,
   the UEFI :file:`NvVars`
   information for the previously-booted |CL| VM will need to be reset.

   #. Relaunch the |CL| VM.  The UEFI shell will appear.

      .. code-block:: bash

         ./start_qemu.sh clear-<version>-kvm.img

   #. At the UEFI shell, delete the :file:`NvVars` file:

      .. code-block:: bash

         Shell> del FS0:\NvVars

   #. Exit out of the UEFI shell:

      .. code-block:: bash

         Shell> reset -s

   #. Relaunch the |CL| VM:

      .. code-block:: bash

         ./start_qemu.sh clear-<version>-kvm.img

#. From the host machine, open a new terminal emulator window and VNC into the
   |CL| VM:

   .. code-block:: bash

      vncviewer 0.0.0.0

#. Log in as ``root`` user into the |CL| VM.

#. Add GDM to the |CL| VM:

   .. code-block:: bash

      swupd bundle-add desktop-autostart

#. Reboot the |CL| VM to enable GDM:

   .. code-block:: bash

      reboot
      
#. Go through GDM's out-of-box experience (OOBE).

#. The default aspect ratio of the GDM GUI for the |CL| VM is 4:3.  To change
   it, use GDM's ``Displays`` setting tool (located at the top-right corner).


.. _Intel® Virtualization Technology: https://www.intel.com/content/www/us/en/virtualization/virtualization-technology/intel-virtualization-technology.html
.. _Intel®Virtualization Technology for Directed I/O: https://software.intel.com/en-us/articles/intel-virtualization-technology-for-directed-io-vt-d-enhancing-intel-platforms-for-efficient-virtualization-of-io-devices
.. _QEMU-KVM launcher: https://cdn.download.clearlinux.org/image/start_qemu.sh
.. _OVMF file: https://cdn.download.clearlinux.org/image/OVMF.fd
