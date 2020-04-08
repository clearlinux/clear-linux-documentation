man:
	git clone git@github.com:clearlinux/clr-man-pages.git
	git clone git@github.com:clearlinux/clr-power-tweaks.git
	git clone git@github.com:clearlinux/clrtrust.git
	git clone git@github.com:clearlinux/mixer-tools.git
	git clone git@github.com:clearlinux/swupd-client.git
	git clone git@github.com:clearlinux/telemetrics-client.git
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
	- rm *.rst
	- rm ../../../reference/manpages/*.rst