import os.path
from flask import render_template, send_file, request, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
from config import app
from weather import main


class CityForm(FlaskForm):
    cityname = StringField(label=('Введите название города:'),
            validators=[DataRequired(), Length(min=3)])
    submit = SubmitField(label=('Скачать'))


@app.route("/", methods=['GET', 'POST'])
@app.route("/index", methods=['GET', 'POST'])
def hello_world():  
    form = CityForm() 
    return render_template('index.html', form=form)


@app.route("/download", methods=['GET', 'POST'])
def downloadFile():
    if request.method == 'POST':
        city_name = request.form.get('cityname')
        response = main(city_name)
        if response == False:
            form = CityForm() 
            flash("Город не найден, попробуйте ввести так 'Москва'", category="error")
            return render_template('index.html', form=form)
        filename = f"weather_in_city_{city_name}_on_7_days.xlsx"
        path = f'excel_docs/{filename}'
        if os.path.exists(path):
            return send_file(path, as_attachment=True)
    if request.method == 'GET':
        return render_template('index', form=form)


        
if __name__ == "__main__":
    app.run()