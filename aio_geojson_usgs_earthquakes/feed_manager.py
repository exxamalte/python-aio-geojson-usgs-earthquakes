"""Feed Manager for USGS Earthquake Hazards Program feed."""
from typing import Awaitable, Callable, List, Tuple

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
        coordinates: Tuple[float, float],
            feed_type: str,
        filter_radius: float = None,
        filter_minimum_magnitude: float = None,
        status_callback: Callable[[StatusUpdate], Awaitable[None]] = None,
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
