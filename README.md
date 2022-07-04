# Weather forecast service
## Build config.py
  
    import os
    from os.path import join, dirname
    from dotenv import load_dotenv
    from flask import Flask

    try:
        dotenv_path = join(dirname(__file__), '.env')
        load_dotenv(dotenv_path)
    except:
        print("file missing .env")
        exit()

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weather.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['FLASK_ENV'] = 'development'
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY_FLASK')  
    
 ## Add requirements
 
    pip install requirements.txt
 ## Add API-KEY in file .env
    API_KEY_WEATHER = ###
    API_KEY_GEOCODER = ###
    SECRET_KEY_FLASK = ###
    
## Run program
    
    python3 app.py
