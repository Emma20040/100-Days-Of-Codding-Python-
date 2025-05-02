from flask import  Flask
from flask import render_template, redirect, url_for, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from form import MyForm
import random

app =Flask(__name__)

# secrete key
app.secret_key ='sdjksd49fij48vul$^(ka)'

# database configuration
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///cafes-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# db
class Cafes(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(250), unique=False, nullable=False)
    url = db.Column(db.String(), nullable=False, unique=False)
    opening_time =db.Column(db.Time, unique=False, nullable=False) 
    clossing_time =db.Column(db.Time, unique=False, nullable=False) 
    price = db.Column(db.Integer,  unique=False, nullable=False)
    rating=db.Column(db.String(250), unique=False, nullable=False)
    wifi =db.Column(db.String(250), unique=False, nullable=False)
    power =db.Column(db.String(250), unique=False, nullable=False)

    def to_dict(self):
        # Convert the model instance into a dictionary
        return {
            'id': self.id,
            'name': self.name,
            'url': self.url,
            'opening Time': self.opening_time.strftime("%H:%M:%S"), # Convert time to string since object cannot be directly serialized into JSON
            'clossing time': self.clossing_time.strftime("%H:%M:%S"),
            'price': self.price,
            'rating':self.rating,
            'wifi strenght': self.wifi,  
            'power':self.power,
        }


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/form', methods=['POST', 'GET'])
def form_page():
    form = MyForm()
    if form.validate_on_submit():
        cafe =Cafes(name = form.cafe_name.data,
        url = form.cafe_url.data,
        opening_time = form.opening_time.data,
        clossing_time = form.clossing_time.data,
        price= form.price.data,
        rating = form.rating.data,
        wifi = form.wifi_strnght.data,
        power = form.power_a.data)
        
        # adding data to database
        db.session.add(cafe)
        db.session.commit()
        return redirect(url_for('all_cafes'))
    
    return render_template('form.html', form=form)


@app.route('/cafes')
def all_cafes():
    data = Cafes.query.all()
    return render_template('cafes.html', data =data)


with app.app_context():
    db.create_all()


# Building REST API

# endpoint to get random cafe from  database
@app.route('/random', methods =['GET'])
def fetch_random_data():
    results =db.session.query(Cafes).all()
    row_count = Cafes.query.count()
    print(f'\\\\\\\\\\{row_count}')
    random_data = random.choice(results)
    return jsonify(cafe ={
        'id':random_data.id,
        'name': random_data.name,
        'url': random_data.url,
        'Opening time': random_data.opening_time.strftime("%H:%M:%S"),
        'Closiing_time': random_data.clossing_time.strftime("%H:%M:%S"),
        'price':random_data.price,
        'Rating':random_data.rating,
        'wifi-strenght':random_data.wifi,
        'power':random_data.power
    })


# endpoint to get all cafe from database
@app.route('/all', methods=['GET'])
def get_all():
    results= db.session.query(Cafes).all() 
    return jsonify(cafes=[cafe.to_dict() for cafe in results])


# search route to search a particular cafe
@app.route('/search', methods =['GET'])
def get_cafe_by_name():
    query_name = request.args.get("name")
    cafe = db.session.query(Cafes).filter_by(name = query_name).first()
    if cafe:
        return jsonify(cafe = cafe.to_dict())
    else:
        return jsonify(error={"Not Found": "Sorry, we don't that cafe in our database."})
    

# endpoint to add cafe
@app.route('/add', methods=['POST'])
def add():
    new_cafe = Cafes(
        name=request.form.get('name'),
        url=request.form.get('url'),
        opening_time=request.form.get('opening_time'),
        clossing_time=request.form.get('clossing_time'),
        # can_take_calls=bool(request.form.get("calls")),
        price =request.form.get('price'),
        rating=request.form.get('rating'),
        wifi_strenght=request.form.get('wifi'),
        power=request.form.get('power'),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


# endpoint to update price using the patch method
@app.route('/update-price<int:id>', methods =['PATCH'])
def update_price(id):
    new_price = request.args.get("new_price")
    cafe =db.session.query(Cafes).get(id)
    if cafe:
        cafe.price =new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."})
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."})
    

# endpoint for deleting cafe
@app.route('/delete-cafe<int:id>', methods =['DELETE'])
def delete(id):
    api_key = request.args.get("api-key")
    if api_key == 'hjsd7bsh6Dsj&a$cn[sja]12@asshasgz9asn.sa/jj':
        cafe = db.session.query(Cafes).get(id)
        if cafe:
            db.session.delete()
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the cafe from the database."}), 200
        else:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    else:
        return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403