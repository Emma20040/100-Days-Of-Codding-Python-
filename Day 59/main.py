from flask import Flask
from markupsafe import escape
from flask import render_template
import requests
import datetime

app = Flask(__name__)

@app.route('/')
def home_page():
    current_year = datetime.datetime.now().year
    return render_template('index.html', year= current_year)

@app.route('/about')
def about_page():
    current_year = datetime.datetime.now().year
    return render_template('about.html', year= current_year)

@app.route('/contact')
def contact_page():
    current_year = datetime.datetime.now().year
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
    current_year = datetime.datetime.now().year
    
    return render_template('post.html', post= post,  year = current_year)
