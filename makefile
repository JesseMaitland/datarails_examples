#!/bin/bash

export PROJECT_DIR = datarails

.PHONY: help
help:                  ## Show help messages and exit.
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'


.PHONY: venv
venv:                  ## Create local python venv for development
	if [[ -d ./venv ]]; then rm -rf venv; fi
	python -m venv venv && pip install --upgrade pip

.PHONY: install
install:               ## Install project requirements
	. venv/bin/activate && pip install -r requirements.txt


.PHONY: build-mkdocs
serve-mkdocs:          ## Serve mkdocs documentation
	. venv/bin/activate && mkdocs serve


.PHONY: build-mkdocs
jupyter-lab:           ## Start Jupiter Labs
	. venv/bin/activate && jupyter lab
