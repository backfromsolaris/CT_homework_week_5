# in order to run/instantiate this as a flask app,
# start importing modules/classes

# i want this whole folder to be one package;
# instantiate this as my entire application

from flask import Flask
# from config import Config

# importing blueprint as var site, register blueprint below
# whenever grabbing anything from entire flask inv specifically blueprints, 
# always start with . to look inside of entire folder (backs out to inv folder)
from .site.routes import site



# create a Flask app & pass everything in it from the directory/inventory
# __name__ takes on the directory it is inside of

app = Flask(__name__)


# registering blueprint as denoted above
app.register_blueprint(site)