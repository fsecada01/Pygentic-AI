#!/usr/bin/env bash
python -m pip install -U pip pip-tools setuptools wheel -I
pip-compile core_requirements.in
#pip-sync core_requirements.txt
pip install -r core_requirements.txt
