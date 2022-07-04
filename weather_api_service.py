import os
from datetime import date
from enum import Enum

from loguru import logger
from statistics import mean
from yaweather import YaWeather

from city_geocoder import Coordinates

if os.environ.get("API_KEY_WEATHER") == None:
    logger.debug("API_KEY not found")
    exit()

API_KEY_WEATHER = os.environ.get("API_KEY_WEATHER")

class PleasureType(str, Enum):
    PLESURE_UP = 'Ожидается резкое увеличение атмосферного давления'
    PLESURE_DOWN = 'Ожидается резкое падение атмосферного давления'
    PLESURE_NATURAL = ''

class WeatherEvent(str, Enum):
    CLEAR = "Ясно"
    PARTLY_CLOUDY = "Малооблачно"
    CLOUDY = "Облачно с прояснениям"
    OVERCAST = "Пасмурно"
    DRIZZLE = "Морось"
    LIGHT_RAIN = "Небольшой дождь"
    RAIN = "Дождь"
    MODERATE_RAIN = "Умеренно сильный дождь"
    HEAVY_RAIN = "Сильный дождь"
    CONTINUOUS_HEAVY_RAIN = "Длительный сильный дождь"
    SHOWERS = "Ливень"
    WET_SNOW = "Дождь со снегом"
    LIGHT_SNOW = "Небольшой снег"
    SNOW = "Снег"
    SNOW_SHOWERS = "Снегопад"
    HAIL = "Град"
    THUNDERSTORM = "Гроза"
    THUNDERSTORM_WITH_RAIN = "Дождь с грозой"
    THUNDERSTORM_WITH_HAIL = "Гроза с градом"

   

class TimesOfDay(str, Enum):
    MORNING = "morning"
    DAY = 'day'
    EVENING = 'evening'
    NIGHT = 'night'

    @classmethod
    def values(cls):
        return [x.value for x in cls]

def map_yandex_weather_item(item):
    """parsing yandex weather api"""
    dict_data_weather = dict()
    dict_data_weather_short = dict()

    dict_data_weather = {k: getattr(item.parts, k) for k in TimesOfDay.values()}

    dict_data_weather_short = {
        'forecast_date': get_date(item),
        'average_temperature': get_average_temperature(dict_data_weather),
        'max_min_temperature': get_max_min_temperature(dict_data_weather),
        'plesure': get_plesure(dict_data_weather),
        'humidity': get_humidity(dict_data_weather),
        'condition': get_condition(dict_data_weather),
    }


    return dict_data_weather_short


def get_yandex_weather(coordinates: Coordinates) -> list[dict, ...]:
    """connection to yandex api"""
    with YaWeather(api_key=API_KEY_WEATHER) as weather:
        
        forecast = weather.forecast(coordinates)
       
        return [map_yandex_weather_item(x) for x in forecast.forecasts]

def get_date(current_day: dict) -> date:
    forecast_date = current_day.date
    return forecast_date 

def get_average_temperature(dict_data_weather: dict) -> float:
    """get average temperature and return by time of day"""
    temp_values = [dict_data_weather.get(x).temp_avg for x in (
        TimesOfDay.MORNING, 
        TimesOfDay.DAY, 
        TimesOfDay.EVENING
    )]
    return round(mean(temp_values), 2)


def get_max_min_temperature(dict_data_weather: dict) -> dict:
    """get max and min temperature"""
    dict_max_min_temperature = dict()
    
    for x in TimesOfDay.values():
        dict_max_min_temperature[f'min_temperature_{x}'] = dict_data_weather.get(x).temp_min
        dict_max_min_temperature[f'max_temperature_{x}'] = dict_data_weather.get(x).temp_max


    return dict_max_min_temperature

def get_plesure(dict_data_weather: dict) -> dict:
    """get atmosphere pressure"""
    temp_values = [dict_data_weather.get(x).pressure_mm for x in TimesOfDay.values()]
    plesure = max(temp_values) - min(temp_values)
    if plesure >= 5:
        return PleasureType.PLESURE_UP.value
    elif plesure <= -5:
        return PleasureType.PLESURE_DOWN.value
    else:
        return PleasureType.PLESURE_NATURAL.value

        
def get_humidity(dict_data_weather: dict) -> dict:
    """get air humidity"""
    dict_humidity = dict()
        
    for x in TimesOfDay.values():
        dict_humidity[f'humidity_{x}'] = dict_data_weather.get(x).humidity

    return dict_humidity

def get_condition(dict_data_weather: dict) -> dict:
    """get a weather event"""
    
    return replace_name_condition(dict_data_weather)

def replace_name_condition(dict_data_weather: dict) -> dict:
    dict_condition = dict()
    for x in TimesOfDay.values():
        replace_name = str(dict_data_weather.get(x).condition).replace('-', '_').upper()
        dict_condition[f'condition_{x}'] = WeatherEvent[replace_name].value

    return dict_condition

    
