from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

"""Link SQLALCHEMY with Mysql"""
"================================================================================================"

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
application_type_json = "application/json"
machine_does_not_exist = "Machine ID does not exist"
@app.route('/delete/machine', methods=['DELETE'])
def remove_machine():
    try:
        content_type = request.headers.get('Content-Type')
        if (content_type == application_type_json):
            json = request.json
            Stock.query.filter_by(machine_id=json["id"]).delete()
            Machine.query.filter_by(id=json["id"]).delete()
            db.session.commit()
            return json
    except Exception as errors:
        return {'error': "ID does not exist", 'check':errors}


"""
Delte Stock
LOGIC: 1) delete the stock
"""


@app.route('/delete/stock', methods=['DELETE'])
def remove_stock():
    try:
        content_type = request.headers.get('Content-Type')
        if content_type == application_type_json:
            json = request.json
            Stock.query.filter_by(id=json["id"]).delete()
            db.session.commit()
            return json
    except Exception:
        return {'error': "ID does not exist"}


@app.route('/add/machine/', methods=['POST'])
def add_machine():
    content_type = request.headers.get('Content-Type')
    if content_type == application_type_json:
        request_json = request.json
        new_machine = Machine(name=request_json["name"], location=request_json["location"])
        db.session.add(new_machine)
        db.session.commit()
        return request_json


@app.route('/add/stock/', methods=['POST'])
def add_stock():
    try:
        content_type = request.headers.get('Content-Type')
        if content_type == application_type_json:
            request_json = request.json
            new_stock = Stock(name=request_json["name"], items=request_json["items"], machine_id=request_json["machine_id"])
            db.session.add(new_stock)
            db.session.commit()
            return request_json
    except Exception:
        return {'error': machine_does_not_exist}


"""
`Get inventory of machine
LOGIC:  1) search stock that have the same id as machine
        2) make it in form of dictionary then convert it to JSON
"""


@app.route('/get/machine/inventory', methods=['GET'])
def get_inventory():
    try:
        conteny_type = request.headers.get('Content-Type')
        if (conteny_type == application_type_json):
            vending_machine_id = request.json["id"]
            inventory = Stock.query.filter_by(machine_id=vending_machine_id).all()
            inventory_machine = [{'id': s.id, 'machine_id': s.machine_id, 'name': s.name, 'items': s.items} for s in
                                inventory]
            return jsonify(inventory_machine)
    except Exception as errors:
        return {'error': machine_does_not_exist, 'reason': errors}


@app.route('/edit/machine', methods=['PUT'])
def edit_machine():
    try:
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            json = request.json
            update_machine = Machine.query.filter_by(id=json["id"]).first()
            update_machine.name = json["name"]
            update_machine.location = json["location"]
            db.session.commit()
            return json
    except Exception:
        return {'error': machine_does_not_exist}


@app.route('/edit/stock', methods=['PUT'])
def edit_stock():
    try:
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            json = request.json
            update_stock = Stock.query.filter_by(id=json["id"]).first()
            update_stock.name = json["name"]
            update_stock.machine_id = json["machine_id"]
            update_stock.items = json["items"]
            db.session.commit()
            return json
    except Exception:
        return {'error': "Stock ID does not exist"}


@app.route('/get/all/machine', methods=['GET'])
def show_all_machine():
    machine = Machine.query.all()
    all_machine = [{'id': mech.id, 'name': mech.name, 'location': mech.location} for mech in machine]
    return jsonify(all_machine)


@app.route('/get/all/stock', methods=['GET'])
def show_all_stock():
    stocks = Stock.query.all()
    all_stocks = [{'id': s.id, 'machine_id': s.machine_id, 'name': s.name, 'items': s.items} for s in stocks]
    return jsonify(all_stocks)


if __name__ == '__main__':
    app.run()
