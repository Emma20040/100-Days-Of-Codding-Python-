from flask import Flask
from flask import render_template, redirect, url_for, send_from_directory,request,abort, flash
from flask_bcrypt import Bcrypt, generate_password_hash, check_password_hash
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from flask_sqlalchemy import SQLAlchemy
from form import LoginForm
import os


app=  Flask(__name__)
flask_bcrypt = Bcrypt(app)
app.secret_key='gy64qef$2d@dkjdks0makkjogfdfiu|'

app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///Users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)



# doing some hashing test
# password = 'password'
# pw_hash= flask_bcrypt.generate_password_hash(password, 12)
# print(f'/////////////////{pw_hash}')
# test_password=  'password'
# if flask_bcrypt.check_password_hash(pw_hash, test_password):
#     print('ACCESS GRANTED')
# else:
#     print('ACCESS DENIED')


# creating db
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(250), unique=False, nullable=False)
    email= db.Column(db.String(200),  unique=False, nullable=False)
    password=db.Column(db.String(250), unique=False, nullable=False)

with app.app_context():
    db.create_all()   


# fetch user
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/')
# @login_required
def home():
    return render_template('index.html')


# register route
@app.route('/register', methods=["GET", "POST"])
def register():
    form = LoginForm()
    if request.method == "POST":
        # checking if user already exits withat email
        if User.query.filter_by(email=request.form.get('email')).first():
            #User already exists
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for('login_page'))
        password=  request.form.get('password')
        pw_hash= flask_bcrypt.generate_password_hash(password, 12).decode('utf-8')
        
        
        new_user = User(
            email=form.email.data,
            name=form.name.data,
            password=pw_hash,
        )
        
        db.session.add(new_user)
        db.session.commit()
        
       #Log in and authenticate user after adding details to database.
        login_user(new_user)
        
        return redirect(url_for("home"))

    return render_template("register.html", form=form)




@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if request.method =='POST':
        email =form.email.data.strip() #.strip() to remove trailing whitespace in email
        password = form.password.data

        #Find user by email entered.
        user = User.query.filter_by(email=email).first()

        if user:
        #Check stored hash password against entered password hashed.
            if flask_bcrypt.check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for('home'))
            elif email !=user.email:
                flash('The email you have entered does not exist in our database', 'danger')
                return redirect(url_for('login_page'))
            else:
                # Invalid email or password
                print("invalid password ===================")
                flash('Invalid  password. Please try again.', 'danger')
                return redirect(url_for('login_page'))
        else:
            print("User not found.")
            flash('invalid email.', 'danger')
            return redirect(url_for('login_page'))
        
    return render_template('login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('login_page'))

# @app.route('/secrets')
# @login_required
# def secrets():
    
#     return render_template('secrets.html' )


# @app.route('/download/<cheat_sheet>')
# def download(cheat_sheet):
#     file_path = os.path.join('static', cheat_sheet.pdf)
#     print(f"Requested file: {cheat_sheet}")
#     print(f"Full file path: {file_path}")
#     if not os.path.isfile(file_path):
#         print(f"File not found: {file_path}")
#         abort(404)
#     return send_from_directory('static', cheat_sheet)

