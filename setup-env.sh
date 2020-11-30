#!/bin/sh
set -e

python3 -m venv .venv

. .venv/bin/activate

pip install -U setuptools
pip install -U pip
pip install -r requirements.txt
