"""USGS Earthquake Hazards Program feed."""
import logging
from datetime import datetime
from typing import Dict, List, Optional, Tuple

from aio_geojson_client.exceptions import GeoJsonException
from aio_geojson_client.feed import GeoJsonFeed
from aiohttp import ClientSession
from geojson import FeatureCollection

from .consts import URLS, ATTR_ATTRIBUTION, FILTER_MINIMUM_MAGNITUDE, \
    ATTR_TITLE
from .feed_entry import UsgsEarthquakeHazardsProgramFeedEntry

_LOGGER = logging.getLogger(__name__)


class UsgsEarthquakeHazardsProgramFeed(
    GeoJsonFeed[UsgsEarthquakeHazardsProgramFeedEntry]
):
    """USGS Earthquake Hazards Program feed."""

    def __init__(
        self,
        websession: ClientSession,
        home_coordinates: Tuple[float, float],
            feed_type,
        filter_radius: float = None,
            filter_minimum_magnitude: float = None,
    ):
        """Initialise this service."""
        if feed_type in URLS:
            super().__init__(websession, home_coordinates, URLS[feed_type],
                             filter_radius=filter_radius)
        else:
            _LOGGER.error("Unknown feed category %s", feed_type)
            raise GeoJsonException(
                "Feed category must be one of %s" % URLS.keys())
        self._filter_minimum_magnitude = filter_minimum_magnitude

    def __repr__(self):
        """Return string representation of this feed."""
        return "<{}(home={}, url={}, radius={}, magnitude={})>".format(
            self.__class__.__name__,
            self._home_coordinates,
            self._url,
            self._filter_radius,
            self._filter_minimum_magnitude,
        )

    def _new_entry(
        self, home_coordinates: Tuple[float, float], feature, global_data: Dict
    ) -> UsgsEarthquakeHazardsProgramFeedEntry:
        """Generate a new entry."""
        attribution = (
            None
            if not global_data and ATTR_ATTRIBUTION not in global_data
            else global_data[ATTR_ATTRIBUTION]
        )
        return UsgsEarthquakeHazardsProgramFeedEntry(
            home_coordinates, feature, attribution
        )

    def _filter_entries_override(self, entries: List[UsgsEarthquakeHazardsProgramFeedEntry], filter_overrides: Dict = None) -> List[UsgsEarthquakeHazardsProgramFeedEntry]:
        """Filter the provided entries."""
        entries = super()._filter_entries_override(entries, filter_overrides)
        filter_minimum_magnitude = (
            filter_overrides[FILTER_MINIMUM_MAGNITUDE]
            if filter_overrides and FILTER_MINIMUM_MAGNITUDE in filter_overrides
            else self._filter_minimum_magnitude
        )
        if filter_minimum_magnitude:
            # Return only entries that have an actual magnitude value, and
            # the value is equal or above the defined threshold.
            return list(
                filter(
                    lambda entry: entry.magnitude
                    and entry.magnitude >= filter_minimum_magnitude,
                    entries,
                )
            )
        return entries

    def _extract_last_timestamp(
        self, feed_entries: List[UsgsEarthquakeHazardsProgramFeedEntry]
    ) -> Optional[datetime]:
        """Determine latest (newest) entry from the filtered feed."""
        if feed_entries:
            dates = sorted([entry.updated for entry in feed_entries],
                           reverse=True)
            return dates[0]
        return None

    def _extract_from_feed(self, feed: FeatureCollection) -> Optional[Dict]:
        """Extract global metadata from feed."""
        global_data = {}
        title = self._search_in_metadata(feed, ATTR_TITLE)
        if title:
            global_data[ATTR_ATTRIBUTION] = title
        return global_data

    @staticmethod
    def _search_in_metadata(feed, name):
        """Find an attribute in the metadata object."""
        if feed and "metadata" in feed and name in feed.metadata:
            return feed.metadata[name]
        return None
