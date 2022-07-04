from loguru import logger
import config
from weather_api_service import get_yandex_weather
from city_geocoder import get_coordinates
from save_weather_in_excel import save_weather_in_exel
from save_weather_in_bd import save_weather_in_db


def main(city_name: str):
    weather = None
    try:
        coordinates = get_coordinates(city_name)
        if coordinates == False:
            return False
        weather = get_yandex_weather(coordinates)
        save_weather_in_exel(weather, city_name)
    except Exception as e:
        logger.debug(e)
    finally:    
        save_weather_in_db(weather)


if __name__=='__main__':
    main("Mo")