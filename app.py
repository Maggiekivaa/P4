# app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask, request, jsonify


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_db.sqlite3'  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  


db = SQLAlchemy(app)
migrate = Migrate(app, db)




from models import Hero, Power, HeroPower

@app.route('/')
def home():
    return "Welcome to the Superhero API!"


@app.route('/heroes', methods=['GET'])
def get_all_heroes():
    all_heroes = Hero.query.all()
    heroes_list = [hero.to_dict() for hero in all_heroes]
    return jsonify(heroes_list)

@app.route('/heroes/<int:heroes_id>', methods=['GET'])
def get_heroes(heroes_id):
    """Returns a single heroes by ID."""
    heroes = heroes.query.get(heroes_id)
    if not heroes:
        return jsonify({"error": "hero not found"}), 404
    return jsonify(heroes.to_dict())

    @app.route('/heroes', methods=['POST'])
    def create_heroes():
     """Creates a new heroes."""
    data = request.get_json()
    if not data:
        return jsonify({ "errors": ["validation errors"]}), 400
    try:
        new_heroes = heroes(name=data['name'])
        db.session.add(new_heroes)
        db.session.commit()
        return jsonify(new_heroes.to_dict()), 201
    except KeyError:
        return jsonify({ "errors": ["validation errors"]}), 400
    
@app.route('/heroes/<int:heroes_id>', methods=['PATCH'])
def update_heroes(heroes_id):
    """Updates heroes information by ID."""
    heroe = heroe.query.get(heroes_id)
    if not heroe:
        return jsonify({"error": "validation errors"}), 404
    data = request.get_json()
    if not data:
        return jsonify({"error": "validation errors"}), 400
    try:
        if 'power' in data:
            heroe.power = data['power']
        db.session.commit()
        return jsonify(heroe.to_dict())
    except KeyError:
        return jsonify({"error": "power not found"}), 400
    
@app.route('/heroes', methods=['POST'])
def create_heroe():
    """Creates a new heroe."""
    data = request.get_json()
    if not data:
        return jsonify({"error": "validation"}), 400
    try:
        new_heroe = heroe(name=data['name'])
        db.session.add(new_heroe)
        db.session.commit()
        return jsonify(new_heroe.to_dict()), 201
    except KeyError:
        return jsonify({"error": "validation error"}), 400



if __name__ == '__main__':
    app.run(debug=True)
