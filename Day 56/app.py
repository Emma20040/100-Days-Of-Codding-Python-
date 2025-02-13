from flask import Flask
from markupsafe import escape
from flask import render_template


app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def home(name = None):
    return render_template('index.html', person= name)

@app.route('/website')
def cv_page():
    return render_template('website.html')
# url_for('static', filename='style.css')