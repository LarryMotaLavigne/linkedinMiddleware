import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-linkedin-middleware',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    # license='BSD License',  # example license
    description='Django Middleware for LinkedIn API',
    long_description=README,
    author='Larry Mota--Lavigne',
    author_email='larry.motalavigne@gmail.com',
    install_requires=['django']
)