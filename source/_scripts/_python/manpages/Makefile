man:
	./clone-man-repos.sh
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