from functools import wraps
import secrets

from flask import request, jsonify

from hikes_inventory.models import User, Hike

def token_required(our_flask_function):
    @wraps(our_flask_function)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token'].split(" ")[1]
            print(token)
        if not token:
            print(token)
            return jsonify({'message': 'Token is missing!'}), 401
        
        try:
            current_user_token = User.query.filter_by(token = token).first()
            print(token)
        except:
            hiker = User.query.filter_by(token = token).first()

            if token != hiker.token and secrets.compare_digest(token, hiker.token):
                return jsonify({'message': 'Invalid Token, try again'})
        return our_flask_function(current_user_token, *args, **kwargs)
    return decorated

import decimal
from flask import json

class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            # convert any decimal values (price, cost_of_prod)
            return str(obj)
        return (JSONEncoder,self).default(obj)