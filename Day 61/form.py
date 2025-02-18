from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired, InputRequired, Length, Email

class MyForm(FlaskForm):
    name = StringField('name', [InputRequired(message="Your name is required")])
    email = EmailField('email',
                        [InputRequired(message="email neeeded"),
                         Email(message='check the email you entered again.', granular_message=False, check_deliverability=False, allow_smtputf8=True, allow_empty_local=False)])
    password = PasswordField('password', 
                             [Length(min=8, max=200, message='your password must be at least 8 characters')])
    submit = SubmitField('submit')