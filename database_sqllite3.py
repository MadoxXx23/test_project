from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from loguru import logger
from config import app

try:
    db = SQLAlchemy(app)
    date = datetime.utcnow
except NameError as e:
    logger.debug(e)
    exit()

   

class StatusWeather(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    forecast_date = db.Column(db.DateTime, default=date)
    avg_temperatura = db.Column(db.Float)
    max_temperature_morning = db.Column(db.Float)
    max_temperature_day = db.Column(db.Float)
    max_temperature_evening = db.Column(db.Float)
    max_temperature_night = db.Column(db.Float)
    min_temperature_morning = db.Column(db.Float)
    min_temperature_day = db.Column(db.Float)
    min_temperature_evening = db.Column(db.Float)
    min_temperature_night = db.Column(db.Float)
    plesure = db.Column(db.String(20))
    humidity_morning = db.Column(db.Float)
    humidity_day = db.Column(db.Float)
    humidity_evening = db.Column(db.Float)
    humidity_night = db.Column(db.Float)
    condition_morning = db.Column(db.String(20))
    condition_day = db.Column(db.String(20))
    condition_evening = db.Column(db.String(20))
    condition_night = db.Column(db.String(20))
    status_request = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return '<StatusWeather %r>' % self.date_request
