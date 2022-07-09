from database_sqllite3 import StatusWeather
from database_sqllite3 import db


def save_weather_in_db(data_weather):
    db.create_all()
    if not data_weather:
        status_weather = StatusWeather(status_request='Ошибка')
        db.session.add(status_weather)
        db.session.commit()
    else:
        for day in data_weather:
            status_weather = StatusWeather(
                avg_temperatura = day.get('average_temperature'),
                max_temperature_morning = day.get('max_min_temperature').get('max_temperature_morning'),
                max_temperature_day = day.get('max_min_temperature').get('max_temperature_day'),
                max_temperature_evening = day.get('max_min_temperature').get('max_temperature_evening'),
                max_temperature_night = day.get('max_min_temperature').get('max_temperature_night'),
                min_temperature_morning = day.get('max_min_temperature').get('min_temperature_morning'),
                min_temperature_day = day.get('max_min_temperature').get('min_temperature_day'),
                min_temperature_evening = day.get('max_min_temperature').get('min_temperature_evening'),
                min_temperature_night = day.get('max_min_temperature').get('min_temperature_night'),
                plesure = day.get('plesure'),
                humidity_morning = day.get('humidity').get('humidity_morning'),
                humidity_day = day.get('humidity').get('humidity_day'),
                humidity_evening = day.get('humidity').get('humidity_evening'),
                humidity_night = day.get('humidity').get('humidity_night'),
                condition_morning = day.get('condition').get('condition_morning'),
                condition_day = day.get('condition').get('condition_day'),
                condition_evening = day.get('condition').get('condition_evening'),
                condition_night = day.get('condition').get('condition_night'),
                status_request='Успешно')
            db.session.add(status_weather)
            db.session.commit()