from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired
from flask_ckeditor import CKEditor
from flask_ckeditor import CKEditorField


class PostForm(FlaskForm):
    title = StringField('Title', [InputRequired(message='Please give a title to your post')])
    subtitle = StringField('Subtitle')
    image =StringField('Image_url')
    content =CKEditorField('Blog Content')
    author =StringField('Author', [InputRequired(message='please include the author of this post')])
    submit =SubmitField('submit')