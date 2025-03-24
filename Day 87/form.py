from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import InputRequired

class CreateTodo(FlaskForm):
    todo = TextAreaField('Todo',
                        [InputRequired(message='a task is required')])
    
    submit= SubmitField('Create')