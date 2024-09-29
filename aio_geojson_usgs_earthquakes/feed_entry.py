"""USGS Earthquake Hazards Program feed entry."""

from __future__ import annotations

import datetime
import logging

from aio_geojson_client.feed_entry import FeedEntry
from geojson import Feature

from .consts import (
    ATTR_ALERT,
    ATTR_ID,
    ATTR_MAG,
    ATTR_PLACE,
    ATTR_STATUS,
    ATTR_TIME,
    ATTR_TITLE,
    ATTR_TYPE,
    ATTR_UPDATED,
)

_LOGGER = logging.getLogger(__name__)


class UsgsEarthquakeHazardsProgramFeedEntry(FeedEntry):
    """USGS Earthquake Hazards Program feed entry."""

    def __init__(
        self, home_coordinates: tuple[float, float], feature: Feature, attribution: str
    ):
        """Initialise this service."""
        super().__init__(home_coordinates, feature)
        self._attribution = attribution

    @property
    def attribution(self) -> str | None:
        """Return the attribution of this entry."""
        return self._attribution

    @property
    def external_id(self) -> str:
        """Return the external id of this entry."""
        return self._search_in_feature(ATTR_ID)

    @property
    def title(self) -> str:
        """Return the title of this entry."""
        return self._search_in_properties(ATTR_TITLE)

    @property
    def place(self) -> str:
        """Return the place of this entry."""
        return self._search_in_properties(ATTR_PLACE)

    @property
    def magnitude(self) -> float:
        """Return the magnitude of this entry."""
        return self._search_in_properties(ATTR_MAG)

    @property
    def time(self) -> datetime:
        """Return the time when this event occurred."""
        publication_date = self._search_in_properties(ATTR_TIME)
        if publication_date:
            # Parse the date. Timestamp in microseconds from unix epoch.
            publication_date = datetime.datetime.fromtimestamp(
                publication_date / 1000, tz=datetime.timezone.utc
            )
        return publication_date

    @property
    def updated(self) -> datetime:
        """Return the updated date of this entry."""
        updated_date = self._search_in_properties(ATTR_UPDATED)
        if updated_date:
            # Parse the date. Timestamp in microseconds from unix epoch.
            updated_date = datetime.datetime.fromtimestamp(
                updated_date / 1000, tz=datetime.timezone.utc
            )
        return updated_date

    @property
    def alert(self) -> str:
        """Return the alert level of this entry."""
        return self._search_in_properties(ATTR_ALERT)

    @property
    def type(self) -> str:
        """Return the type of this entry."""
        return self._search_in_properties(ATTR_TYPE)

    @property
    def status(self) -> str:
        """Return the status of this entry."""
        return self._search_in_properties(ATTR_STATUS)
