#!/bin/bash

# Clean dist folder and *.egg-info
rm -dfr dist
rm -dfr build
rm -dfr django_linkedin_middleware.egg-info

# Install/Update and create package for delivery
python -m pip install --user --upgrade setuptools wheel
python setup.py sdist bdist_wheel

# Upload to Test-PyPI or PyPI (depending on the commented line)
easy_install twine
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
#twine upload dist/*
