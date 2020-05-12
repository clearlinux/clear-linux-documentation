@ECHO OFF

REM Command file for building man pages

if "%1" == "man" (
    git clone https://github.com/clearlinux/clr-man-pages.git
    git clone https://github.com/clearlinux/clr-power-tweaks.git
    git clone https://github.com/clearlinux/clrtrust.git
    git clone https://github.com/clearlinux/mixer-tools.git
    git clone https://github.com/clearlinux/swupd-client.git
    git clone https://github.com/clearlinux/telemetrics-client.git
    git clone https://github.com/clearlinux/tallow.git
    git clone https://github.com/clearlinux/micro-config-drive.git
    python.exe manpages.py
    mkdir ..\..\..\reference\manpages
    copy *.rst ..\..\..\reference\manpages
    goto end
)

if "%1" == "clean-man" (
    rmdir /q /s clr-man-pages
    rmdir /q /s clr-power-tweaks
    rmdir /q /s clrtrust
    rmdir /q /s mixer-tools
    rmdir /q /s swupd-client
    rmdir /q /s telemetrics-client
    rmdir /q /s tallow
    rmdir /q /s micro-config-drive
    del *.rst
    del ..\..\..\reference\manpages\*.rst
    del ..\..\..\reference\man-pages.rst
    goto end
)

:end