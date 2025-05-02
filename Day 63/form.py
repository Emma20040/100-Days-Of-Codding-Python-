from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired

class MyForm(FlaskForm):
    name = StringField('Book Name',
                        [InputRequired(message='book is required')])
    author = StringField('Book Author',
                          [InputRequired(message="please include the author's name so as to avoid confusion")])
    
    rating = StringField('Rating',
                         [InputRequired(message="please we need your to make our sytem better")] )
    
    submit= SubmitField('Submit')