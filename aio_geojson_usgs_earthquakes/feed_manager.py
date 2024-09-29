"""Feed Manager for USGS Earthquake Hazards Program feed."""

from __future__ import annotations

from collections.abc import Awaitable, Callable

from aio_geojson_client.feed_manager import FeedManagerBase
from aio_geojson_client.status_update import StatusUpdate
from aiohttp import ClientSession

from .feed import UsgsEarthquakeHazardsProgramFeed


class UsgsEarthquakeHazardsProgramFeedManager(FeedManagerBase):
    """Feed Manager for USGS Earthquake Hazards Program feed."""

    def __init__(
        self,
        websession: ClientSession,
        generate_callback: Callable[[str], Awaitable[None]],
        update_callback: Callable[[str], Awaitable[None]],
        remove_callback: Callable[[str], Awaitable[None]],
        coordinates: tuple[float, float],
        feed_type: str,
        filter_radius: float | None = None,
        filter_minimum_magnitude: float | None = None,
        status_callback: Callable[[StatusUpdate], Awaitable[None]] | None = None,
    ):
        """Initialize the USGS Earthquake Hazards Program Manager."""
        feed = UsgsEarthquakeHazardsProgramFeed(
            websession,
            coordinates,
            feed_type,
            filter_radius=filter_radius,
            filter_minimum_magnitude=filter_minimum_magnitude,
        )
        super().__init__(
            feed,
            generate_callback,
            update_callback,
            remove_callback,
            status_async_callback=status_callback,
        )
