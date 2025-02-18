from flask import Flask
from flask import render_template
from flask import request

app =Flask(__name__)

@app.route('/',  methods=['POST'])
def form():
    if request.method =='POST':
        print('hello')
        data = request.form
        print(data['name'])
        # return 'hello new user'
    return render_template('index.html', data=data)