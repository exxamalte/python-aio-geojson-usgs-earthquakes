# Changes

## 0.3 (26/01/2024)
* Bumped version of upstream aio_geojson_client library to 0.20.
* Improved JSON parsing error handling, especially when not using Python's built-in JSON parsing library.
* Code quality improvements.
* Added Python 3.12 support.
* Bumped library versions: black, flake8, isort.
* Migrated to pytest.

## 0.2 (25/01/2023)
* Added Python 3.11 support.
* Removed deprecated asynctest dependency.
* Bumped version of upstream aio_geojson_client library to 0.18.

## 0.1 (18/03/2022)
* Initial release with support for USGS Earthquake Hazards Program feed.
* Calculating distance to home coordinates.
* Support for filtering by distance and minimum magnitude.
* Supporting all the features available in non-async library 
  ([python-geojson-client](https://github.com/exxamalte/python-geojson-client)).
