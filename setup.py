# noqa: D100
import os
from typing import List

from setuptools import find_packages, setup

_pkg: str = "smallmatter"


def read(fname):
    """Read content on file name."""
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def read_version():
    """Read version indicated in VERSION."""
    return read("VERSION").strip()


# Declare minimal set for installation
required_packages: List[str] = []

# Specific use case dependencies
# fmt: off
extras = {
    "all": ["s3fs"],
    "pathlib": ["s3fs"],
}
# fmt: on

setup(
    name=_pkg,
    packages=find_packages(),
    version=read_version(),
    description="Collection of fine-grained utilities for data science works on AWS.",
    long_description=read("README.md"),
    author="Verdi March",
    author_email="first.last@email.com",
    url=f"https://github.com/abcd/{_pkg}/",
    download_url="",
    project_urls={
        "Bug Tracker": f"https://github.com/verdimrc/{_pkg}/issues/",
        "Documentation": f"https://{_pkg}.readthedocs.io/en/stable/",
        "Source Code": f"https://github.com/verdimrc/{_pkg}/",
    },
    license="MIT",
    keywords="data science AWS",
    platforms=["any"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.6.0",
    install_requires=required_packages,
    extras_require=extras,
    include_package_data=True,
)
