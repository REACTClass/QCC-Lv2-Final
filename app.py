from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os
import psycopg2


app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://wflzgjtn:bBu6nVUDX5W_jeTWRX3ScV3PBAiYg7BW@fanny.db.elephantsql.com/wflzgjtn'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Burger(db.Model):
    __tablename__ = 'reservations'
    id = db.Column(db.Integer, primary_key = True)
    guests = db.Column(db.Integer)
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    date_of_res = db.Column(db.Date)
    time_of_res = db.Column(db.Time)

    def __init__(self, guests, first_name, last_name, date_of_res, time_of_res):
        self.guests = guests
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_res = date_of_res
        self.time_of_res = time_of_res

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        guests = request.form['guest']
        first_name = request.form['firstName']
        last_name = request.form['lastName']
        date_of_res = request.form['date']
        time_of_res = request.form['time']
        print(guests,first_name,last_name, date_of_res, time_of_res)
        data = Burger(guests, first_name, last_name, date_of_res, time_of_res)
        db.session.add(data)
        db.session.commit()
        return render_template('confirmation.html')


if __name__ == '__main__':
    app.debug = False
    app.run()
