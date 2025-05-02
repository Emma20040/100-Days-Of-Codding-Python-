from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, TimeField, SelectField, SubmitField, IntegerField
from wtforms.validators import InputRequired, Length

class MyForm(FlaskForm):
    cafe_name =StringField('Cafe name',
                            [InputRequired(message='cafe is required')])
    cafe_url = StringField('Cafe url', 
                           [InputRequired(message="link is required")])
    opening_time = TimeField('Opening time e.g. 8AM', 
                             [InputRequired(message="please enter the cafe's oping time")])
    clossing_time = TimeField("Clossing time e.g. 5PM", 
                              [InputRequired('clossing time is needed')])
    price = IntegerField("Price", [InputRequired()])
    rating = SelectField('Coffe Ratting', 
                         choices=[('☕'), ('☕☕'),('☕☕☕' ), ('☕☕☕☕'), ('☕☕☕☕☕')])
    wifi_strnght = SelectField('WIFI strenght ratting',
                               choices=[('💪'), ('💪💪'), ('💪💪💪'), ('💪💪💪💪'), ('💪💪💪💪💪')])
    power_a= SelectField('power socket available',
                         choices=[('🔌'), ('🔌🔌'), ('🔌🔌🔌'), ('🔌🔌🔌🔌'), ('🔌🔌🔌🔌🔌')])
    submit = SubmitField('submit')
