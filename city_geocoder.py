import os
from loguru import logger
import geocoder
import config
from validation import Coordinates

if not os.environ.get("API_KEY_GEOCODER"):
    logger.debug("API_KEY_GEOCODER not found")
    exit()
    
API_KEY_GEOCODER = os.environ.get('API_KEY_GEOCODER')

def get_coordinates(city: str) -> Coordinates:
    """Getting coordinates by city name"""
    params ={
            'apikey': API_KEY_GEOCODER,
            'kind': 'locality'
            }
    coordinates = geocoder.yandex(city, params=params)

    if str(coordinates).startswith('<[ERROR - No results found]'):
        logger.debug("City not found")
        return False, None
           
    longitude, latitude= coordinates.geojson.get('features')[0].get('geometry').get('coordinates')
    city = coordinates.geojson.get('features')[0].get('properties').get('raw').get('name')

    return Coordinates(latitude=latitude, longitude=longitude), city





