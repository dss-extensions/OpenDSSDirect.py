# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from setuptools.command.develop import develop
from subprocess import check_call
import shlex

import logging

import os
from codecs import open

here = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the README file
with open(os.path.join(here, "./README.md"), encoding="utf-8") as f:
    long_description = f.read()

with open(os.path.join(here, "opendssdirect", "_version.py"), encoding="utf-8") as f:
    version = f.read()

version = version.splitlines()[1].split()[2].strip('"').strip("'")

logger = logging.getLogger(__name__)


class PostDevelopCommand(develop):

    def run(self):
        try:
            check_call(shlex.split("pre-commit install"))
        except Exception as e:
            logger.warning("Unable to run 'pre-commit install'")
        develop.run(self)


setup(
    name="OpenDSSDirect.py",
    version=version,
    description="Python direct-mode interface to OpenDSS",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/dss-extensions/OpenDSSDirect.py",
    download_url="https://github.com/dss-extensions/OpenDSSDirect.py",
    # Author details
    author="Dheepak Krishnamurthy",
    author_email="me@kdheepak.com",
    license="BSD-compatible",
    packages=find_packages(),
    install_requires=["future", "six", "dss_python>=0.10.6,<0.11"],
    extras_require={
        "extras": ["pandas", "matplotlib", "networkx"],
        "dev": [
            "pytest",
            "pytest-cov",
            "sphinx-rtd-theme",
            "nbsphinx",
            "black",
            "pre-commit",
        ],
    },
    keywords=["OpenDSS", "cffi"],
    zip_safe=False,
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 4 - Beta",
        # Indicate who your project is intended for
        "Intended Audience :: Science/Research",
        "Intended Audience :: Education",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        # Pick your license as you wish (should match "license" above)
        "License :: Other/Proprietary License",
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    cmdclass={"develop": PostDevelopCommand},
)
