from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length

class LoginForm(FlaskForm):
    name = StringField('Name', [InputRequired(message='please username is required for authentication')])
    email = EmailField('Email', [InputRequired(message='please enter a valid email address')])
    password = PasswordField('Password', [InputRequired(message='please create a password'), Length( max =300, min=8)])
    submit = SubmitField('Sign in')