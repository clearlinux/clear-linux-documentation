man:
	git clone https://github.com/clearlinux/clr-man-pages.git
	git clone https://github.com/clearlinux/clr-power-tweaks.git
	git clone https://github.com/clearlinux/clrtrust.git
	git clone https://github.com/clearlinux/mixer-tools.git
	git clone https://github.com/clearlinux/swupd-client.git
	git clone https://github.com/clearlinux/telemetrics-client.git
	git clone https://github.com/clearlinux/tallow.git
	git clone https://github.com/clearlinux/micro-config-drive.git
	python3 manpages.py
	- mkdir ../../../reference/manpages
	cp *.rst ../../../reference/manpages

clean-man:
	- rm -rf clr-man-pages
	- rm -rf clr-power-tweaks
	- rm -rf clrtrust
	- rm -rf mixer-tools
	- rm -rf swupd-client
	- rm -rf telemetrics-client
	- rm -rf tallow
	- rm -rf micro-config-drive
	- rm *.rst
	- rm ../../../reference/manpages/*.rst
	- rm ../../../reference/man-pages.rst