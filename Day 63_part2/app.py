from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

app=  Flask(__name__)



# configuring the sqlite db
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///books-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(250), unique=False, nullable=False)
    author = db.Column(db.String(250), nullable=False, unique=False)
    rating = db.Column(db.Float, nullable=False, unique=False)

with app.app_context():
    db.create_all() 

    #CREATE RECORD
    new_book = Book(title="Harry", author="Rowling", rating=9)
    db.session.add(new_book)
    db.session.commit()
    print('book added||||||||||||||||')