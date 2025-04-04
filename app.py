# app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask, jsonify


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



if __name__ == '__main__':
    app.run(debug=True)
