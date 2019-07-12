# Makefile for Sphinx documentation
#

all:
	make -C source html

htmlall:
	make -C source htmlall

htmlde:
	make -C source htmlde

html:
	make -C source html

linkcheck:
	make -C source linkcheck

py:
	make -C source py

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  html       to make standalone HTML files"

clean:
	make -C source clean

