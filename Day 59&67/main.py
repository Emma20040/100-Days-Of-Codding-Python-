from flask import Flask
from markupsafe import escape
from flask import render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_ckeditor import CKEditor
from form import PostForm
import requests
from datetime import datetime

app = Flask(__name__)
app.secret_key ='d5jkk%JjaI&NX|MNSA,K&JAK@DSklasl'

# ckeditor
ckeditor = CKEditor(app)

# database congiguration
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///All Posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# models
class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(150), unique=False, nullable=False)
    subtitle = db.Column(db.String(250), unique=False, nullable=False)
    image_url = db.Column(db.String(250), unique=False, nullable=False)
    blog_content= db.Column(db.Text(10000), unique=False, nullable=False)
    author = db.Column(db.String(250), unique=False, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

with app.app_context():
    db.create_all()

# route to create new post
@app.route('/create', methods =['GET', 'POST'])
def create_post():
    form = PostForm()
    if form.validate_on_submit():
        blog = Posts(title = form.title.data,
                     subtitle =form.subtitle.data, 
                     image_url = form.image.data,
                     blog_content =form.content.data, 
                     author = form.author.data)
        db.session.add(blog)
        db.session.commit()
        return redirect(url_for('home_page'))
    return render_template('create_post.html', form= form)


#home route 
@app.route('/')
def home_page():
    
    # post = db.session.query(Posts).filter(Posts.id == post_id)
    # post_at =post.created_at.strftime("%B %d, %Y")
    all_post = Posts.query.all()
    current_year = datetime.now()
    current_year =current_year.strftime("%B %d, %Y")
    return render_template('index.html', posts =all_post, year= current_year)

# route to display image and content of post
@app.route('/full_post/<int:post_id>', methods =['GET', 'POST'])
def full_post(post_id):
    post =db.session.query(Posts).filter(Posts.id == post_id).first()
    return render_template('content_img.html', posts =post)

@app.route('/about')
def about_page():
    current_year = datetime.now()
    current_year =current_year.strftime("%B %d, %Y")
    return render_template('about.html', year= current_year)

@app.route('/contact')
def contact_page():
    current_year = datetime.now().year
    return render_template('contact.html', year=current_year)

@app.route('/post')
def post_page():
    blog_url ='https://www.npoint.io/docs/472feba5772ba725212f'
    # blog_url =('https://dummyjson.com/auth/RESOURCE', 
            #    {
#   method: 'GET', 
#   headers: {
#     'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...', 
#     'Content-Type': 'application/json'
#   }, 
# })
    response = requests.get(blog_url)
    post = response.json()
    print(response.status_code)
    print(response.text)
    current_year = datetime.now().year
    
    return render_template('post.html', post= post,  year = current_year)

@app.route('/edit<int:id>', methods=['GET', 'POST'])
def edit_post(id):
    # movie_id = request.args.get('id')
    post = Posts.query.get(id)
    form= PostForm(obj=post) # the obj= movies makes sures that the form is prepopulated with the data before editing
    if form.validate_on_submit():
        print('\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\')
        post.title = form.title.data
        post.subtitle = form.subtitle.data
        post.image_url = form.image.data
        post.blog_content =form.content.data
        post.author = form.author.data
        db.session.commit()
        return redirect(url_for('home_page'))
    return render_template('edit_post.html', form= form, post=post)

# delete route
@app.route('/delete/<int:post_id>', methods=['GET', 'POST'])
def delete_post(post_id):
    # Fetch the post from the database
    post = Posts.query.get_or_404(post_id)

    if request.method == 'POST':
        db.session.delete(post)
        db.session.commit()

        # Flash a success message
        flash('Post deleted successfully!', 'success')
        return redirect(url_for('home_page'))

    return render_template('confirm_delete.html', post=post)
