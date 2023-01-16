import json

from flask import Flask, redirect, url_for, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/db_name'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password123@localhost/VendingMachine'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)



class Machine(db.Model):
    __tablename__ = 'Machine'
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(50), nullable=False)





class Stock(db.Model):
    __tablename__ = 'Stock'
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    machine_id = db.Column(db.Integer, db.ForeignKey('Machine.id'), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    items = db.Column(db.Integer, nullable=False)


with app.app_context():
    db.create_all()
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/add/machine/', methods = ['POST'])
def addMachine():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        newMachine = Machine(name=json["name"], location=json["location"])
        db.session.add(newMachine)
        db.session.commit()
        return json


@app.route('/add/stock/', methods = ['POST'])
def addStock():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        newStock = Stock(name=json["name"], items=json["items"], machine_id=json["machine_id"])
        db.session.add(newStock)
        db.session.commit()
        return json


@app.route('/get/machine', methods = ['GET'])
def showMachine():
    machine = Machine.query.all()
    all_users = [{'id': mech.id, 'name': mech.name, 'location': mech.location} for mech in machine]
    return jsonify(all_users)

if __name__ == '__main__':
    app.run()
