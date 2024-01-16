# Makefile for Sphinx documentation

SHELL := /bin/bash

PY_VERSION ?= 3.6

all:
	$(MAKE) -C source html

htmlall:
	$(MAKE) -C source htmlall

htmlzh:
	$(MAKE) -C source htmlzh

htmlde:
	$(MAKE) -C source htmlde

html:
	$(MAKE) -C source html

linkcheck:
	$(MAKE) -C source linkcheck

py:
	$(MAKE) -C source py

man:
	$(MAKE) -C source man

clean-man:
	$(MAKE) -C source clean-man

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  html       to make standalone HTML files"

clean:
	$(MAKE) -C source clean
	rm -rf venv

venv:
	virtualenv venv;\
	source venv/bin/activate; \
	pip3 install -r requirements.txt;
