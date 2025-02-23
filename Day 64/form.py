from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,FloatField, IntegerField
from wtforms.validators import InputRequired

class EditForm(FlaskForm):
    rating = StringField("Your Rating Out of 10 e.g. 7.5")
    review = StringField("Your Review")
    submit = SubmitField("Done")



class CreateForm(FlaskForm):
    title =StringField('Title', [InputRequired()])
    year = StringField('Year', [InputRequired()])
    description= StringField('Description')
    rating =FloatField('Rating', [InputRequired()])
    ranking = IntegerField('Ranking', [InputRequired()])
    review = StringField('Review')
    img_url= StringField('image')
    submit = SubmitField('submit')