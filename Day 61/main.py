from flask import Flask
from flask import render_template, url_for, redirect
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from form import MyForm



app = Flask(__name__)

app.secret_key = "s45dfyu8uj0kp;i-9g56edcjh"
@app.route('/login', methods=['GET', 'POST'])
def login_user():
    form = MyForm()
    if form.validate_on_submit():
        name= form.name.data
        email= form.email.data
        password = form.password.data
        print(f'{name}\n {email}\n {password}')
        if email=='admin@gmail.com' and password=='12345678':
            return redirect(url_for('success'))
        else:
            return redirect(url_for('denied_access'))
    return render_template('login_page.html', form= form)

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/denied')
def denied_access():
    return render_template('denied.html')
