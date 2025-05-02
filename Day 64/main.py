from flask import Flask
from flask import render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from form import EditForm, CreateForm



app = Flask(__name__)
app.secret_key='gy64qef$2d@hkkjogfdfiu|'

app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///movies-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# creating db
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(250), unique=False, nullable=False)
    year = db.Column(db.String(), nullable=False, unique=False)
    description =db.Column(db.String(250), unique=False, nullable=False)
    rating = db.Column(db.Float(), nullable=False, unique=False)
    ranking= db.Column(db.Integer(), unique=False, nullable=False)
    review= db.Column(db.String(500), unique=False, nullable=True)
    img_url = db.Column(db.String(250), unique=False, nullable=False)


@app.route('/')
def home_page():
    all_movies = Movie.query.all()
    return render_template('index.html', movies=all_movies )

@app.route('/add_movie', methods=['GET', 'POST'])
def add_movie():
    form =CreateForm()
    if form.validate_on_submit():
        print('||||||||||||||||||||||||||||||')
        movie = Movie(title=form.title.data, year= form.year.data,
                       description = form.description.data, rating = form.rating.data,
                       ranking =form.ranking.data, review = form.review.data,
                       img_url= form.img_url.data)
        db.session.add(movie)
        db.session.commit()
        return redirect(url_for('home_page'))
    return render_template('create.html', form= form)


@app.route('/edit<int:id>', methods=['GET', 'POST'])
def edit(id):
    # movie_id = request.args.get('id')
    movie = Movie.query.get(id)
    form= EditForm(obj=movie) # the obj= movies makes sures that the form is prepopulated with the data before editing
    if form.validate_on_submit():
        print('\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\')
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home_page'))
    return render_template('edit.html', form= form, movie=movie)


@app.route("/delete")
def delete_movie():
    movie_id = request.args.get("id")
    movie = Movie.query.get(movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for("home_page"))


with app.app_context():
    db.create_all() 