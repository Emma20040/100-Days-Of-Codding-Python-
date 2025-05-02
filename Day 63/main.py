from flask import Flask
from flask import render_template, redirect, url_for
from form import MyForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# secret key
app.secret_key ='sjkc9p]$@dsdas](shjhe57fihe'
# books =[]

app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///books-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# database

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

@app.route('/add', methods=['POST', 'GET'])
def add_book():
    form = Book()
    if form.validate_on_submit():
        name = form.name.data
        author = form.author.data
        rating= form.rating.data
        print(f'{name}|||||{author}||||| {rating}')
        
        # adding data to list
        # books.append({
        #     'name':name,
        #     'author':author,
        #     'rating':rating
        # })
        return redirect(url_for('home'))
    return render_template('add_book.html', form= form)


# getting the lenthg of the list

@app.route('/')
def home():
    number_books = len(books)
    print(f'|||||||{number_books}')
    return render_template('index.html', books= books, num_books= number_books)






