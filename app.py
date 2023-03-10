import json
import os

import requests
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

"""Link SQLALCHEMY with Mysql"""
"================================================================================================"
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/db_name'
# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://" + os.environ["MYSQL_USER"] + ":" + os.environ[
#     "MYSQL_PASSWORD"] + "@" + os.environ["MYSQL_DATABASE"] + "/VendingMachine"

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:password123@localhost:3306/VendingMachine'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
"================================================================================================"
"""
Create table Machine and Stock
"""
"================================================================================================"


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
"================================================================================================"


@app.route('/')
def hello_world():
    return 'Hello World!'


"""
Delte machine
LOGIC: 1) delete the stock that have machine id same as the machine that we want to delete
       2) delete the machine
"""


@app.route('/delete/machine', methods=['DELETE'])
def remove_machine():
    try:
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            json = request.json
            Stock.query.filter_by(machine_id=json["id"]).delete()
            Machine.query.filter_by(id=json["id"]).delete()
            db.session.commit()
            return json
    except:
        return {'error': "ID does not exist"}


"""
Delte Stock
LOGIC: 1) delete the stock
"""


@app.route('/delete/stock', methods=['DELETE'])
def remove_stock():
    try:
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            json = request.json
            Stock.query.filter_by(id=json["id"]).delete()
            db.session.commit()
            return json
    except:
        return {'error': "ID does not exist"}


@app.route('/add/machine/', methods=['POST'])
def add_machine():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        request_json = request.json
        new_machine = Machine(name=request_json["name"], location=request_json["location"])
        db.session.add(new_machine)
        db.session.commit()
        return request_json


@app.route('/add/stock/', methods=['POST'])
def addStock():
    try:
        content_type = request.headers.get('Content-Type')
        if content_type == 'application/json':
            request_json = request.json
            newStock = Stock(name=request_json["name"], items=request_json["items"], machine_id=request_json["machine_id"])
            db.session.add(newStock)
            db.session.commit()
            return request_json
    except:
        return {'error': "Machine ID does not exist"}


"""
`Get inventory of machine
LOGIC:  1) search stock that have the same id as machine
        2) make it in form of dictionary then convert it to JSON
"""


@app.route('/get/machine/inventory', methods=['GET'])
def getInventory():
    try:
        conteny_type = request.headers.get('Content-Type')
        if (conteny_type == 'application/json'):
            id = request.json["id"]
            inventory = Stock.query.filter_by(machine_id=id).all()
            inventoryMachine = [{'id': s.id, 'machine_id': s.machine_id, 'name': s.name, 'items': s.items} for s in
                                inventory]
            return jsonify(inventoryMachine)
    except:
        return {'error': "Machine ID does not exist"}


@app.route('/edit/machine', methods=['PUT'])
def editMachine():
    try:
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            json = request.json
            updateMachine = Machine.query.filter_by(id=json["id"]).first()
            updateMachine.name = json["name"]
            updateMachine.location = json["location"]
            db.session.commit()
            return json
    except:
        return {'error': "Machine ID does not exist"}


@app.route('/edit/stock', methods=['PUT'])
def editStock():
    try:
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            json = request.json
            updateStock = Stock.query.filter_by(id=json["id"]).first()
            updateStock.name = json["name"]
            updateStock.machine_id = json["machine_id"]
            updateStock.items = json["items"]
            db.session.commit()
            return json
    except:
        return {'error': "Stock ID does not exist"}


@app.route('/get/all/machine', methods=['GET'])
def showAllMachine():
    machine = Machine.query.all()
    allMachines = [{'id': mech.id, 'name': mech.name, 'location': mech.location} for mech in machine]
    return jsonify(allMachines)


@app.route('/get/all/stock', methods=['GET'])
def showAllStock():
    stocks = Stock.query.all()
    allStocks = [{'id': s.id, 'machine_id': s.machine_id, 'name': s.name, 'items': s.items} for s in stocks]
    return jsonify(allStocks)


if __name__ == '__main__':
    app.run()
