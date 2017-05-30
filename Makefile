# Makefile for Sphinx documentation
#

all:
	make -C source html

html:
	make -C source html

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  html       to make standalone HTML files"

clean:
	make -C source clean

