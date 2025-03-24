from flask import Flask
from flask import redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

from datetime import datetime
from form import CreateTodo


app = Flask(__name__)
app.secret_key='gy64qef$2d@hkkjogfdfiu|'

app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///todos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# creating db
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    todo =db.Column(db.String(250), unique=False, nullable=False)
    created_at =db.Column(db.DateTime, default= datetime.utcnow)
    completed = db.Column(db.Boolean, default = False)

    def __repr__(self):
        return '<Task %r>' % self.id
    
    
with app.app_context():
    db.create_all()  

@app.route('/')
def home():
    tasks = Todo.query.all()
    return render_template('index.html', task=tasks )

@app.route('/create', methods=["GET", "POST"])
def  create():
    form = CreateTodo()
    if form.validate_on_submit():
        print('||||||||||||||||||||||||||||||')
        task = Todo(todo=form.todo.data)
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html', form= form)

