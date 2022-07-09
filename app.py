import os.path
from flask import render_template, send_file, request, flash, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
from config import app
from weather import main


class CityForm(FlaskForm):
    cityname = StringField(label=('Введите название города:'),
            validators=[DataRequired(), Length(min=3, max=15)])
    submit = SubmitField(label=('Скачать'))


@app.route("/", methods=['GET'])
@app.route("/index", methods=['GET'])
def index():  
    form = CityForm() 
    return render_template('index.html', form=form)


@app.route("/download", methods=['GET', 'POST'])
def downloadFile():
    if request.method == 'POST':
        city_name = request.form.get('cityname')
        response = main(city_name)

        if not response:
            flash(f"Город {city_name} не найден", category="error")
            return redirect('/')

        filename = f"weather_in_city_{response}_on_7_days.xlsx"
        path = f'excel_docs/{filename}'
        if os.path.exists(path):
            return send_file(path, as_attachment=True)

    if request.method == 'GET':
        return redirect('/')


        
if __name__ == "__main__":
    app.run()