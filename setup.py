"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

import sys

# Always prefer setuptools over distutils
from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open
from os import path

# Get version from __init__.py
from FCPGtools import __version__

# test the python version
major, minor = sys.version_info[0:2]
if (major, minor) >= (3,7):
	sys.stderr.write('\nPython 3.7 or later is required for this package.\n')
	sys.exit(1)

# get absolute path to this directory
here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding = 'utf-8') as f:
	long_description = f.read()

setup(
	name = "FCPGtools",
	version = __version__,
	author = "Theodore Barnhart",
	author_email = "tbarnhart@usgs.gov",
	description = "Tools to make Flow-Conditioned Parameter Grids (FCPG)",
	long_description = long_description,
	long_description_content_type = "text/x-rst",
	url="https://code.usgs.gov/StreamStats/data-preparation/cpg/FCPGtools",
	packages = find_packages(),
	classifiers = [
		"Natural Language :: English",
		"Programming Language :: Python :: 3.7",
		"Programming Language :: Python :: 3.8",
		"Programming Language :: Python :: 3.9",
		"Programming Language :: Python :: 3.10",
		"Operating System :: POSIX :: Linux",
		"Operating System :: Microsoft :: Windows",
		"Development Status :: 5 - Production/Stable",
		"Topic :: Scientific/Engineering",
        "Topic :: Software Development :: Libraries :: Python Modules",
		"License :: OSI Approved :: MIT License",
	],
	python_requires = '>=3.7',
	)
