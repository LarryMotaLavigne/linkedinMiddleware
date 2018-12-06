import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django_linkedin_middleware',
    version='0.1.2',
    packages=find_packages(),
    include_package_data=True,
    license='Apache License',
    description='Django Middleware for LinkedIn API',
    long_description=README,
    long_description_content_type='text/markdown',
    author='Larry Mota--Lavigne',
    author_email='larry.motalavigne@gmail.com',
    url="https://github.com/Squalex/LinkedinMiddleware",
    install_requires=['django', 'linkedin', 'mock', 'python3-linkedin']
)