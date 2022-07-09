from loguru import logger
import config
from weather_api_service import get_yandex_weather
from city_geocoder import get_coordinates
from save_weather_in_excel import save_weather_in_exel
from save_weather_in_bd import save_weather_in_db


def main(city_name: str):
    weather = None
    try:
        coordinates, city_name_eng = get_coordinates(city_name)
        if not coordinates:
            return False
        weather = get_yandex_weather(coordinates)
        save_weather_in_exel(weather, city_name_eng)
    except Exception as e:
        logger.debug(e)
    finally:    
        save_weather_in_db(weather)
        return city_name_eng