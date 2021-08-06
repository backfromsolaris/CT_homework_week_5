# in order to run/instantiate this as a flask app,
# start importing modules/classes

# i want this whole folder to be one package;
# instantiate this as my entire application

from flask import Flask
from flask.json import JSONEncoder
from config import Config
from .authentication.routes import auth
from flask_migrate import Migrate
from .models import db, login_manager, ma
from .api.routes import api
from .helpers import JSONEncoder
from flask_cors import CORS

# importing blueprint as var site, register blueprint below
# whenever grabbing anything from entire flask inv specifically blueprints, 
# always start with . to look inside of entire folder (backs out to inv folder)
from .site.routes import site



# create a Flask app & pass everything in it from the directory/inventory
# __name__ takes on the directory it is inside of

app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(api)


# registering blueprint as denoted above
app.register_blueprint(site)
app.register_blueprint(auth)

db.init_app(app)
ma.init_app(app)

login_manager.init_app(app)

login_manager.login_view = 'auth.signin' #Specify what page to load for NON AUTH users

migrate = Migrate(app, db)

app.json_encoder = JSONEncoder

CORS(app)

from .models import User
