"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Character, Planet, Vehicle, FavoritesCharacters, FavoritesPlanets, FavoritesVehicles
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def handle_hello():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200

@app.route('/users', methods=['GET'])
def get_all_users():

    query_results = User.query.all()
    results = list(map(lambda item: item.serialize(), query_results))
   
    if results == []:
        return jsonify({"msg" : "There is no users"}), 404

    response_body = {
        "msg": "Hello, this are the users ",
        "results": results
    }


    return jsonify(response_body), 200

@app.route('/people', methods=['GET'])
def get_all_people():

    query_results = Character.query.all()
    results = list(map(lambda item: item.serialize(), query_results))
   
    if results == []:
        return jsonify({"msg" : "There is no characters"}), 404

    response_body = {
        "msg": "Hello, this is your GET /user response ",
        "results": results
    }


    return jsonify(response_body), 200

@app.route('/favorite/people', methods=['GET'])
def get_all_favorite_people():

    query_results = FavoritesCharacters.query.all()
    results = list(map(lambda item: item.serialize(), query_results))
   
    if results == []:
        return jsonify({"msg" : "There is no favorite characters"}), 404

    response_body = {
        "msg": "Hello, this are the favorite characters ",
        "results": results
    }


    return jsonify(response_body), 200

@app.route('/people/<int:people_id>', methods=['GET'])
def get_character(people_id):

    character = Character.query.get(people_id)
   
    if character == None:
        return jsonify({"msg" : "There is no such character"}), 404

    return jsonify(character.serialize()), 200

@app.route('/favorite/people/<int:people_id>', methods=['POST'])
def create_favorite_character(people_id):
    
    body = request.json
    check_user = User.query.filter_by(id=body["id"]).first()
    if check_user is None:
        return jsonify({"msg" : "User doesn't exist"}), 404
    else:
        check_character = Character.query.filter_by(id=people_id).first()
        if check_character is None:
            return jsonify({"msg" : "Character doesn't exist"}), 404
        else:
            check_favorite_character = FavoritesCharacters.query.filter_by(character_id=people_id, user_id=body["id"]).first()
            
            if check_favorite_character is None:
                new_favorite_character = FavoritesCharacters(user_id=body["id"], character_id=people_id)
                db.session.add(new_favorite_character)
                db.session.commit()
                return jsonify({"msg" : "Character added to favorites"}), 200
            
            else:
                return jsonify({"msg" : "Character repeated"}), 400


@app.route('/favorite/people/<int:people_id>', methods=['DELETE'])
def delete_favorite_people(people_id):
    
    body = request.json
    check_user = User.query.filter_by(id=body["id"]).first()
    if check_user is None:
        return jsonify({"msg" : "User doesn't exist"}), 404
    else:
        check_character = Character.query.filter_by(id=people_id).first()
        if check_character is None:
            return jsonify({"msg" : "Character doesn't exist"}), 404
        else:
            check_favorite_character = FavoritesCharacters.query.filter_by(character_id=people_id, user_id=body["id"]).first()
            if check_favorite_character is None:
                return jsonify({"msg" : "Character not found"}), 400
            else:
                delete_favorite_character = FavoritesCharacters.query.filter_by(character_id=people_id, user_id=body["id"]).first()
                db.session.delete(delete_favorite_character)
                db.session.commit()
                return jsonify({"msg" : "Character deleted from favorites"}), 200

@app.route('/planets', methods=['GET'])
def get_all_planets():

    query_results = Planet.query.all()
    results = list(map(lambda item: item.serialize(), query_results))
   
    if results == []:
        return jsonify({"msg" : "There is no planets"}), 404

    response_body = {
        "msg": "Hello, this is your GET /user response ",
        "results": results
    }


    return jsonify(response_body), 200

@app.route('/favorite/planets', methods=['GET'])
def get_all_favorite_planets():

    query_results = FavoritesPlanets.query.all()
    results = list(map(lambda item: item.serialize(), query_results))
   
    if results == []:
        return jsonify({"msg" : "There is no favorite planets"}), 404

    response_body = {
        "msg": "Hello, this are the favorite planets ",
        "results": results
    }


    return jsonify(response_body), 200

@app.route('/planets/<int:planet_id>', methods=['GET'])
def get_planet(planet_id):

    planet = Planet.query.get(planet_id)
   
    if planet == None:
        return jsonify({"msg" : "There is no such planet"}), 404

    return jsonify(planet.serialize()), 200

@app.route('/favorite/planet/<int:planet_id>', methods=['POST'])
def create_favorite_planet(planet_id):
    
    body = request.json
    check_user = User.query.filter_by(id=body["id"]).first()
    if check_user is None:
        return jsonify({"msg" : "User doesn't exist"}), 404
    else:
        check_planet = Planet.query.filter_by(id=planet_id).first()
        if check_planet is None:
            return jsonify({"msg" : "Planet doesn't exist"}), 404
        else:
            check_favorite_planet = FavoritesPlanets.query.filter_by(planet_id=planet_id, user_id=body["id"]).first()
            if check_favorite_planet is None:
                new_favorite_planet = FavoritesPlanets(user_id=body["id"], planet_id=planet_id)
                db.session.add(new_favorite_planet)
                db.session.commit()
                return jsonify({"msg" : "Planet added to favorites"}), 200

            else:
                return jsonify({"msg" : "Planet repeated"}), 400

@app.route('/favorite/planet/<int:planet_id>', methods=['DELETE'])
def delete_favorite_planet(planet_id):
    
    body = request.json
    check_user = User.query.filter_by(id=body["id"]).first()
    if check_user is None:
        return jsonify({"msg" : "User doesn't exist"}), 404
    else:
        check_planet = Planet.query.filter_by(id=planet_id).first()
        if check_planet is None:
            return jsonify({"msg" : "Planet doesn't exist"}), 404
        else:
            check_favorite_planet = FavoritesPlanets.query.filter_by(planet_id=planet_id, user_id=body["id"]).first()
            if check_favorite_planet is None:
                return jsonify({"msg" : "Planet not found"}), 400
            else:
                delete_favorite_planet = FavoritesPlanets.query.filter_by(planet_id=planet_id, user_id=body["id"]).first()
                db.session.delete(delete_favorite_planet)
                db.session.commit()
                return jsonify({"msg" : "Planet deleted from favorites"}), 200

@app.route('/vehicles', methods=['GET'])
def get_all_vehicles():

    query_results = Vehicle.query.all()
    results = list(map(lambda item: item.serialize(), query_results))
   
    if results == []:
        return jsonify({"msg" : "There is no vehicles"}), 404

    response_body = {
        "msg": "Hello, this is your GET /user response ",
        "results": results
    }


    return jsonify(response_body), 200

@app.route('/vehicles/<int:vehicle_id>', methods=['GET'])
def get_vehicle(vehicle_id):

    vehicle = Vehicle.query.get(vehicle_id)
   
    if vehicle == None:
        return jsonify({"msg" : "There is no such vehicle"}), 404

    return jsonify(vehicle.serialize()), 200

@app.route('/favorite/vehicles', methods=['GET'])
def get_all_favorite_vehicles():

    query_results = FavoritesVehicles.query.all()
    results = list(map(lambda item: item.serialize(), query_results))
   
    if results == []:
        return jsonify({"msg" : "There is no favorite vehicles"}), 404

    response_body = {
        "msg": "Hello, this are the favorite vehicles ",
        "results": results
    }


    return jsonify(response_body), 200

@app.route('/favorite/vehicle/<int:vehicle_id>', methods=['POST'])
def create_favorite_vehicle(vehicle_id):
    
    body = request.json
    check_user = User.query.filter_by(id=body["id"]).first()
    if check_user is None:
        return jsonify({"msg" : "User doesn't exist"}), 404
    else:
        check_vehicle = Vehicle.query.filter_by(id=vehicle_id).first()
        if check_vehicle is None:
            return jsonify({"msg" : "Vehicle doesn't exist"}), 404
        else:
            check_favorite_vehicle = FavoritesVehicles.query.filter_by(vehicle_id=vehicle_id, user_id=body["id"]).first()
            if check_favorite_vehicle is None:
                new_favorite_vehicle = FavoritesVehicles(user_id=body["id"], vehicle_id=vehicle_id)
                db.session.add(new_favorite_vehicle)
                db.session.commit()
                return jsonify({"msg" : "Vehicle added to favorites"}), 200
            
            else:
                return jsonify({"msg" : "Vehicle repeated"}), 400
            
@app.route('/favorite/vehicle/<int:vehicle_id>', methods=['DELETE'])
def delete_favorite_vehicle(vehicle_id):
    
    body = request.json
    check_user = User.query.filter_by(id=body["id"]).first()
    if check_user is None:
        return jsonify({"msg" : "User doesn't exist"}), 404
    else:
        check_vehicle = Vehicle.query.filter_by(id=vehicle_id).first()
        if check_vehicle is None:
            return jsonify({"msg" : "Vehicle doesn't exist"}), 404
        else:
            check_favorite_vehicle = FavoritesVehicles.query.filter_by(vehicle_id=vehicle_id, user_id=body["id"]).first()
            if check_favorite_vehicle is None:
                return jsonify({"msg" : "Vehicle not found"}), 400
            else:
                delete_favorite_vehicle = FavoritesVehicles.query.filter_by(vehicle_id=vehicle_id, user_id=body["id"]).first()
                db.session.delete(delete_favorite_vehicle)
                db.session.commit()
                return jsonify({"msg" : "Vehicle deleted from favorites"}), 200

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
