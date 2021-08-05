# importing Blueprint class
# below, registers the location of the blueprint
# method render_template helps to render html; gives a way to serve up html
from flask import Blueprint, render_template
from flask_login import login_required



# good practice to follow folder name for variable naming convention
# keeps things organized, though not technically required

# takes in a string name for blueprint, directory location, 
#     define a template folder:  where does the html come from
#     that we are serving up from this blueprint (houses site html files)
site = Blueprint('site', __name__, template_folder='site_templates')



# decorator, allows us to use render_template
# specify blueprint name .route('slash assumes this is the home page')
@site.route('/')

# when going to this route^^, we want python to run some sort of functionality
def home():
    # looking for a string of whatever your file is called
    # render_template says 'i'm inside of a blueprint,
    # where is my template at?'
    # 
    return render_template('index.html')

@site.route('/profile')
@login_required
def profile():
    return render_template('profile.html')