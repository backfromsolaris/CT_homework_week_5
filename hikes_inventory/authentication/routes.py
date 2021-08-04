from flask import Blueprint, render_template, request
from hikes_inventory.forms import UserForm


auth = Blueprint('auth', __name__, template_folder='auth_templates')



@auth.route('/signup', methods = ['GET', 'POST'])
def signup():
    # instantiation of class created in forms.py, to be referenced in html as 'form'
    form = UserForm()
    if request.method == 'POST' and form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        print([email, password])
    return render_template('signup.html', form=form)

@auth.route('/signin')
def signin():
    return render_template('signin.html')