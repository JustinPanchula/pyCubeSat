#!/usr/bin/env python
"""PMACS package creation
"""
__author__ = "Justin Panchula"
__copyright__ = "Copyright 2024 UC CubeCats"
__credits__ = ["Justin Panchula"]
__license__ = "MIT"
__version__ = "1.0.0"
__status__ = "Production"
__maintainer__ = None
__contact__ = None

# Imports
import setuptools

# Set package version
version = "0.1.0"

# Gather package requirements
requirements = []
with open("requirements.txt", 'r', encoding='utf-16') as f:
    for req in f.readlines():
        requirements.append(req[:-1])

# Extra requirements
extras_require = {}

# Package Data
package_data = {}

# Get README
with open("requirements.txt", 'r') as f:
    readme = f.read()

# List packages
packages = setuptools.find_packages()

# Setup
setuptools.setup(
    name="pyCubeSat",
    author="Justin Panchula",
    url="github.com/JustinPanchula/pyCubeSat",
    project_urls=[
        "https://uccubecats.github.io/LEOPARDSat-1.html"
    ],
    version=version,
    packages=packages,
    license="MIT",
    description="A Pure Python Package Useful for CubeSat Development",
    long_description=readme,
    long_description_content_type='text/x-rst',
    include_package_data=True,
    install_requires=requirements,
    extras_require=extras_require,
    python_requires='>=3.12.0',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Science/Research",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.12",
        "Topic :: Scientific/Engineering :: Astronomy",
        "Topic :: Scientific/Engineering :: Physics"
        "Typing :: Typed",
    ],
)