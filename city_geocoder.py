import os
from loguru import logger
import geocoder
from validation import Coordinates

if os.environ.get("API_KEY_GEOCODER") == None:
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
        return False
        
    latitude, longitude = coordinates.geojson.get('features')[0].get('geometry').get('coordinates')
    return Coordinates(latitude=latitude, longitude=longitude)




