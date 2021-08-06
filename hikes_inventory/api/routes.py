from flask import Blueprint, json, request, jsonify
from flask_migrate import current
from hikes_inventory.helpers import token_required
from hikes_inventory.models import db, User, Hike, hike_schema, hikes_schema



api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/getdata')
def getdata():
    return {'some_value': 52, 'another_value': 800}

# create endpoint
@api.route('/hikes', methods = ['POST'])
@token_required
def create_hike(current_user_token):
    hike_name = request.json['hike_name']
    country = request.json['country']
    district = request.json['district']
    city = request.json['city']
    coordinates = request.json['coordinates']
    length = request.json['length']
    elevation_gain = request.json['elevation_gain']
    hike_type = request.json['hike_type']
    difficulty = request.json['difficulty']
    parking = request.json['parking']
    user_token = current_user_token.token

    print(f'TESTER:  {current_user_token.token}')
    hike = Hike(hike_name,country,district,city,coordinates,length,elevation_gain,hike_type,difficulty,parking,user_token=user_token)

    db.session.add(hike)
    db.session.commit()

    response = hike_schema.dump(hike)
    return jsonify(response)

# retrieve all hikes
@api.route('/hikes', methods = ['GET'])
@token_required
def get_hikes(current_user_token):
    hiker = current_user_token.token
    hikes = Hike.query.filter_by(user_token = hiker).all()
    response = hikes_schema.dump(hikes)
    return jsonify(response)

# retrieve single hike endpoint
@api.route('/hikes/<id>')
@token_required
def get_hike(current_user_token, id):
    hike = Hike.query.get(id)
    response = hike_schema.dump(hike)
    return jsonify(response)

# update a hike by id endpointing
@api.route('/hikes/<id>', methods = ['POST'])
@token_required
def update_hike(current_user_token, id):
    hike = Hike.query.get(id)
    if hike:
        hike = Hike.query.get(id)
        print(hike)
        hike.hike_name = request.json['hike_name']
        hike.country = request.json['country']
        hike.district = request.json['district']
        hike.city = request.json['city']
        hike.coordinates = request.json['coordinates']
        hike.length = request.json['length']
        hike.elevation_gain = request.json['elevation_gain']
        hike.hike_type = request.json['hike_type']
        hike.difficulty = request.json['difficulty']
        hike.parking = request.json['parking']
        hike.user_token = current_user_token.token
        db.session.commit()

        response = hike_schema.dump(hike)
        return jsonify(response)
    else:
        return jsonify({'Error': 'We do not see that hike in our records!'})

# delete hike by id
@api.route('/hikes/<id>', methods = ['DELETE'])
@token_required
def delete_hike(current_user_token, id):
    hike = Hike.query.get(id)
    if hike:
        db.session.delete(hike)
        db.session.commit()

        response = hike_schema.dump(hike)
        return jsonify(response)
    else:
        return jsonify({'Error': 'We do not see that hike in our records!'})