"""Test for the USGS Earthquake Hazards Program feed general setup."""

from aio_geojson_usgs_earthquakes import __version__


def test_version():
    """Test for version tag."""
    assert __version__ is not None
