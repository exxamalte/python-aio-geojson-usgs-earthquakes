"""Test for the USGS Earthquake Hazards Program feed."""

import asyncio
import datetime
from http import HTTPStatus

from aio_geojson_client.consts import UPDATE_OK
from aio_geojson_client.exceptions import GeoJsonException
import aiohttp
import pytest

from aio_geojson_usgs_earthquakes import UsgsEarthquakeHazardsProgramFeed
from tests.utils import load_fixture


@pytest.mark.asyncio
async def test_update_ok(mock_aioresponse):
    """Test updating feed is ok."""
    home_coordinates = (-31.0, 151.0)
    mock_aioresponse.get(
        "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/significant_hour.geojson",
        status=HTTPStatus.OK,
        body=load_fixture("earthquakes-1.json"),
    )

    async with aiohttp.ClientSession(loop=asyncio.get_running_loop()) as websession:
        feed = UsgsEarthquakeHazardsProgramFeed(
            websession, home_coordinates, "past_hour_significant_earthquakes"
        )
        assert (
            repr(feed) == "<UsgsEarthquakeHazardsProgramFeed("
            "home=(-31.0, 151.0), "
            "url=https://earthquake.usgs.gov/earthquakes/"
            "feed/v1.0/summary/significant_hour.geojson, "
            "radius=None, magnitude=None)>"
        )
        status, entries = await feed.update()
        assert status == UPDATE_OK
        assert entries is not None
        assert len(entries) == 3

        feed_entry = entries[0]
        assert feed_entry.title == "Title 1"
        assert feed_entry.external_id == "1234"
        assert feed_entry.coordinates == (-32.2345, 149.1234)
        assert round(abs(feed_entry.distance_to_home - 224.5), 1) == 0
        assert repr(feed_entry) == "<UsgsEarthquakeHazardsProgramFeedEntry(id=1234)>"
        assert feed_entry.place == "Place 1"
        assert feed_entry.magnitude == 3.0
        assert feed_entry.time == datetime.datetime(
            2018, 9, 22, 8, 0, tzinfo=datetime.timezone.utc
        )
        assert feed_entry.updated == datetime.datetime(
            2018, 9, 22, 8, 30, tzinfo=datetime.timezone.utc
        )
        assert feed_entry.alert == "Alert 1"
        assert feed_entry.type == "Type 1"
        assert feed_entry.status == "Status 1"
        assert feed_entry.attribution == "Feed Title"

        feed_entry = entries[1]
        assert feed_entry is not None
        assert feed_entry.title == "Title 2"
        assert feed_entry.magnitude == 1.25
        assert feed_entry.status is None

        feed_entry = entries[2]
        assert feed_entry.title == "Title 3"
        assert feed_entry.magnitude is None


@pytest.mark.asyncio
async def test_update_ok_with_minimum_magnitude(mock_aioresponse):
    """Test updating feed is ok, filtered by category."""
    home_coordinates = (-31.0, 151.0)
    mock_aioresponse.get(
        "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/significant_hour.geojson",
        status=HTTPStatus.OK,
        body=load_fixture("earthquakes-1.json"),
    )

    async with aiohttp.ClientSession(loop=asyncio.get_running_loop()) as websession:
        feed = UsgsEarthquakeHazardsProgramFeed(
            websession,
            home_coordinates,
            "past_hour_significant_earthquakes",
            filter_minimum_magnitude=2.5,
        )
        assert (
            repr(feed) == "<UsgsEarthquakeHazardsProgramFeed("
            "home=(-31.0, 151.0), "
            "url=https://earthquake.usgs.gov/earthquakes/"
            "feed/v1.0/summary/significant_hour.geojson, "
            "radius=None, magnitude=2.5)>"
        )
        status, entries = await feed.update()
        assert status == UPDATE_OK
        assert entries is not None
        assert len(entries) == 1

        feed_entry = entries[0]
        assert feed_entry is not None
        assert feed_entry.title == "Title 1"
        assert feed_entry.external_id == "1234"
        assert repr(feed_entry) == "<UsgsEarthquakeHazardsProgramFeedEntry(id=1234)>"


@pytest.mark.asyncio
async def test_empty_feed(mock_aioresponse):
    """Test updating feed is ok when feed does not contain any entries."""
    home_coordinates = (-31.0, 151.0)
    mock_aioresponse.get(
        "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/significant_hour.geojson",
        status=HTTPStatus.OK,
        body=load_fixture("earthquakes-2.json"),
    )

    async with aiohttp.ClientSession(loop=asyncio.get_running_loop()) as websession:
        feed = UsgsEarthquakeHazardsProgramFeed(
            websession, home_coordinates, "past_hour_significant_earthquakes"
        )
        assert (
            repr(feed) == "<UsgsEarthquakeHazardsProgramFeed("
            "home=(-31.0, 151.0), "
            "url=https://earthquake.usgs.gov/earthquakes/"
            "feed/v1.0/summary/significant_hour.geojson, "
            "radius=None, magnitude=None)>"
        )
        status, entries = await feed.update()
        assert status == UPDATE_OK
        assert entries is not None
        assert len(entries) == 0
        assert feed.last_timestamp is None


@pytest.mark.asyncio
async def test_invalid_feed_type():
    """Test detection of invalid feed type."""
    home_coordinates = (-31.0, 151.0)
    async with aiohttp.ClientSession(loop=asyncio.get_running_loop()) as websession:
        with pytest.raises(GeoJsonException):
            UsgsEarthquakeHazardsProgramFeed(websession, home_coordinates, "INVALID")
