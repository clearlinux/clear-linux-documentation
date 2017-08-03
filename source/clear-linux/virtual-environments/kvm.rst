.. _kvm:

Running Clear Linux as a KVM guest OS
#####################################

To run |CL| in a virtualized environment using abbr:`KVM (Kernel-based
Virtual Machine)`, follow these steps.

1. Enable `Intel® Virtualization Technology`_ (Intel® VT) and
   `Intel®Virtualization Technology for Directed I/O`_ (Intel® VT-d) in the
   host machine’s BIOS.

2. Log in and get root privilege on the host machine::

    $ sudo -s

3. Install `QEMU-KVM` on the host machine. Below are some example distros.

   * |CL|::

     # swupd bundle-add desktop-autostart kvm-host

   * Ubuntu 16.04 LTS Desktop::

     # apt-get install qemu-kvm

   * Mint 18.1 “Serena” Desktop::

     # apt-get install qemu-kvm

   * Fedora 25 Workstation::

     # dnf install qemu-kvm

4. Download the latest pre-built Clear Linux _`KVM image` file from
   the _`image` directory.

5. Uncompress the downloaded image

   .. code-block:: console

      unxz clear-<version number>-kvm.img.xz

6. Download the :file:`OVMF.fd` file that provides UEFI support for
   virtual machines from the _`image` directory.

7. Download the sample _`QEMU-KVM launcher` script from the _`image` directory.

8. Make the script executable::

   # chmod +x start_qemu.sh

9. Start the |CL| KVM virtual machine::

   # ./start_qemu.sh clear-<version number>-kvm.img

#. Log in and set the root password.

#. To SSH into the |CL| VM, follow these steps.

    a. Enable SSH access

       .. code-block:: console

          # cat > /etc/ssh/sshd_config << EOF
            PermitRootLogin yes
            EOF

    b. From the host, SSH into the Clear Linux VM::

       # ssh -p 10022 root@localhost

#. To add the GNOME Display Manager (GDM) to the |CL| VM, follow these steps:

   a. Shutdown the active |CL| VM.

   b. Install VNCViewer on the host machine.  Below are some example distros.

      *  Clear Linux::

         # swupd bundle-add desktop-apps 

      *  Ubuntu 16.04 LTS Desktop::

         # apt-get vncviewer

      *  Mint 18.1 “Serena” Desktop::

         # apt-get vncviewer

      *  Fedora 25 Workstation::

         # dnf install tigervnc

   c. Modify the start_qemu.sh script to increase memory (-m), add graphics
      driver (-vga), and add VNC (-vnc and -usbdevice) support.

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

   d. Due to changes in `start_qemu.sh` script, the UEFI NvVars information for
         the previously-booted |CL| VM will need to be reset.

      i. Relaunch the |CL| VM.  The EFI shell will appear::

         # ./start_qemu.sh clear-<version number>-kvm.img

      ii. At the UEFI shell, delete the NvVars file:

         .. code-block:: console

            Shell> del FS0:\NvVars

      iii. In another terminal window, kill all processes related to `qemu`::

           # pkill -f qemu

   e. Relaunch the |CL| VM::

      # ./start_qemu.sh clear-<version number>-kvm.img

   f. From the host machine, VNC into the |CL| VM::

      # vncviewer 0.0.0.0

   g. Log into the |CL| VM.

   h. Get root privilege::

      $ sudo -s

   i. Add GDM to |CL| VM::

      # swupd bundle-add desktop-autostart

   j. Reboot the |CL| VM to enable GDM::

      # reboot

.. _Intel® Virtualization Technology: https://www.intel.com/content/www/us/en/virtualization/virtualization-technology/intel-virtualization-technology.html
.. _Intel®Virtualization Technology for Directed I/O: https://software.intel.com/en-us/articles/intel-virtualization-technology-for-directed-io-vt-d-enhancing-intel-platforms-for-efficient-virtualization-of-io-devices
.. _image: https://download.clearlinux.org/image/
.. _QEMU-KVM launcher: https://download.clearlinux.org/image/start_qemu.sh