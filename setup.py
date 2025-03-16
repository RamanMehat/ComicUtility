# setup.py

""" Python setup file to install Comic Utility as a python package. """

# Import statement
from setuptools import setup
from os import path

import re

here = path.abspath(path.dirname(__file__))
project_requirements = path.join(here, 'requirements.txt')

with open(project_requirements) as req:
    requirements = req.read().splitlines()

name = re.search(
    '^name\s*=\s*"(.*)"',
    open('__init__.py').read(),
    re.M
).group(1)

version = re.search(
    '^version\s*=\s*"(.*)"',
    open('__init__.py').read(),
    re.M
).group(1)

setup(
    name=name,
    version=version,
    description="Comic Utility to Alter Comic books.",
    install_requires=requirements,
    entry_points={'console_scripts': ["cu = ComicUtility.ComicUtility:main()"]},
    author="Raman Mehat",
    author_email="raman.mehat@protonmail.com",
)
