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


@app.route('/delete/machine', methods=['DELETE'])
def removeMachine():
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

@app.route('/delete/stock', methods=['DELETE'])
def removeStock():
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
def addMachine():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        newMachine = Machine(name=json["name"], location=json["location"])
        db.session.add(newMachine)
        db.session.commit()
        return json


@app.route('/add/stock/', methods=['POST'])
def addStock():
    try:
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            json = request.json
            newStock = Stock(name=json["name"], items=json["items"], machine_id=json["machine_id"])
            db.session.add(newStock)
            db.session.commit()
            return json
    except:
        return {'error': "Machine ID does not exist"}


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
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        updateMachine = Machine.query.filter_by(id=json["id"]).first()
        updateMachine.name = json["name"]
        updateMachine.location = json["location"]
        db.session.commit()
        return json


@app.route('/edit/stock', methods=['PUT'])
def editStock():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        updateStock = Stock.query.filter_by(id=json["id"]).first()
        updateStock.name = json["name"]
        updateStock.machine_id = json["machine_id"]
        updateStock.items = json["items"]
        db.session.commit()
        return json


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
