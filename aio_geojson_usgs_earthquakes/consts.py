"""USGS Earthquake Hazards Program constants."""

ATTR_ALERT = "alert"
ATTR_ATTRIBUTION = "attribution"
ATTR_CATEGORY = "category"
# ATTR_DESCRIPTION = "description"
ATTR_ID = "id"
ATTR_MAG = "mag"
ATTR_PLACE = "place"
# ATTR_PUB_DATE = "pubDate"
ATTR_STATUS = "status"
ATTR_TIME = "time"
ATTR_TITLE = "title"
ATTR_TYPE = "type"
ATTR_UPDATED = "updated"

FILTER_MINIMUM_MAGNITUDE = "minimum_magnitude"
# FILTER_RADIUS = "radius"

URL_PREFIX = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/"
URLS = {
    "past_hour_significant_earthquakes": URL_PREFIX + "significant_hour.geojson",
    "past_hour_m45_earthquakes": URL_PREFIX + "4.5_hour.geojson",
    "past_hour_m25_earthquakes": URL_PREFIX + "2.5_hour.geojson",
    "past_hour_m10_earthquakes": URL_PREFIX + "1.0_hour.geojson",
    "past_hour_all_earthquakes": URL_PREFIX + "all_hour.geojson",
    "past_day_significant_earthquakes": URL_PREFIX + "significant_day.geojson",
    "past_day_m45_earthquakes": URL_PREFIX + "4.5_day.geojson",
    "past_day_m25_earthquakes": URL_PREFIX + "2.5_day.geojson",
    "past_day_m10_earthquakes": URL_PREFIX + "1.0_day.geojson",
    "past_day_all_earthquakes": URL_PREFIX + "all_day.geojson",
    "past_week_significant_earthquakes": URL_PREFIX + "significant_week.geojson",
    "past_week_m45_earthquakes": URL_PREFIX + "4.5_week.geojson",
    "past_week_m25_earthquakes": URL_PREFIX + "2.5_week.geojson",
    "past_week_m10_earthquakes": URL_PREFIX + "1.0_week.geojson",
    "past_week_all_earthquakes": URL_PREFIX + "all_week.geojson",
    "past_month_significant_earthquakes": URL_PREFIX + "significant_month.geojson",
    "past_month_m45_earthquakes": URL_PREFIX + "4.5_month.geojson",
    "past_month_m25_earthquakes": URL_PREFIX + "2.5_month.geojson",
    "past_month_m10_earthquakes": URL_PREFIX + "1.0_month.geojson",
    "past_month_all_earthquakes": URL_PREFIX + "all_month.geojson",
}
