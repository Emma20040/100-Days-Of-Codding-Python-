from flask import Flask
from markupsafe import escape
from flask import render_template
import random
import datetime
import requests

app =Flask(__name__)

@app.route('/')
def main_page():
    random_number = random.randint(1, 20)
    current_year = datetime.datetime.now().year
    context =random_number
    return render_template('index.html', context=context, year = current_year)

@app.route('/guess/<name>')
def guess(name):

    response = requests.get(f'https://api.genderize.io?name={name}')
    data = response.json()
    print(data)
    gender = data['gender']
    age_url = requests.get(f'https://api.agify.io?name={name}')
    age_data = age_url.json()
    print(age_data)
    age = age_data['age']
    return render_template('guess.html', name=name, gender = gender, age=age)

@app.route('/blog/<num>')
def blog_page(num):
    blog_url = 'https://www.npoint.io/docs/161982aa73bcdae93913'
    response = requests.get(blog_url)
    all_blogs = response.json()
    # print(f'{all_blogs.status_code}')
    print(all_blogs)
    return render_template('blog.html', blog= all_blogs)
