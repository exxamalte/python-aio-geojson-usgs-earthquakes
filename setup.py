"""Setup of aio_geojson_usgs_earthquakes library."""

from setuptools import find_packages, setup

from aio_geojson_usgs_earthquakes.__version__ import __version__

NAME = "aio_geojson_usgs_earthquakes"
AUTHOR = "Malte Franken"
AUTHOR_EMAIL = "coding@subspace.de"
DESCRIPTION = "An async GeoJSON client library for the U.S. Geological Survey Earthquake Hazards Program."
URL = "https://github.com/exxamalte/python-aio-geojson-usgs-earthquakes"

REQUIRES = [
    "aio_geojson_client>=0.20",
    "aiohttp>=3.7.4,<4",
    "pytz>=2019.01",
]


with open("README.md") as fh:
    long_description = fh.read()

setup(
    name=NAME,
    version=__version__,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=URL,
    packages=find_packages(exclude=("tests",)),
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    install_requires=REQUIRES,
)
