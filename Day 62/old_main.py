from flask import  Flask
from flask import render_template, redirect, url_for
from form import MyForm

app =Flask(__name__)

# secrete key
app.secret_key ='sdjksd49fij48vul$^(ka)'
user_data =[]

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/form', methods=['POST', 'GET'])
def form_page():
    form = MyForm()
    if form.validate_on_submit():
        name = form.cafe_name.data
        url = form.cafe_url.data
        opening_time = form.opening_time.data
        clossing_time = form.clossing_time.data
        rating = form.rating.data
        wifi_strength = form.wifi_strnght.data
        power = form.power_a.data
        print(f'{name}\n {url}\n {opening_time}\n {clossing_time}\n {rating}\n {wifi_strength}\n {power}')
        # appending the submitted data into the list
        user_data.append({
            'name':name,
            'url':url,
            'opening_time':opening_time,
            'clossing_time': clossing_time,
            'ratting':rating,
            'wifi_strenght': wifi_strength,
            'power_supply': power
        })
        return redirect(url_for('all_cafes'))
    print(user_data)
    return render_template('form.html', form=form)


@app.route('/cafes')
def all_cafes():
    return render_template('cafes.html', data =user_data)