# Makefile for Sphinx documentation

SHELL := /bin/bash

PY_VERSION ?= 3.6

all:
	make -C source html

htmlall:
	make -C source htmlall

htmlzh:
	make -C source htmlzh

htmlde:
	make -C source htmlde

html:
	make -C source html

linkcheck:
	make -C source linkcheck

py:
	make -C source py

man:
	make -C source man

clean-man:
	make -C source clean-man

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  html       to make standalone HTML files"

clean:
	make -C source clean
	rm -rf venv

venv:
	virtualenv venv;\
	source venv/bin/activate; \
	pip3 install -r requirements.txt;
