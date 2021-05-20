"""Server for donations site."""

from flask import (Flask, render_template, request, flash,
                session, redirect)
from model import connect_to_db
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.route('/')
def homepage():
    """View homepage."""

    return render_template('homepage.html')

@app.route('/login')
def login():
    """Log in to account."""

    return render_template('login.html')

@app.route('/create-donor')
def create_donor():
    """Create donor account."""

    return render_template('create_donor.html')

@app.route('/create-org')
def create_org():
    """Create org account."""

    return render_template('create_org.html')

@app.route('/items')
def all_items():
    """View all items."""

    items = crud.get_items()

    return render_template('all_items.html', items=items)

@app.route('/items/<item_id>')
def show_item(item_id):
    """Show details of a particular item."""

    item = crud.get_item_by_id(item_id)

    return render_template('item_details.html', item=item)

@app.route('/users', methods=['POST'])
def register_user():
    """Create a new user."""

    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.get_user_by_email(email)
    if user:
        flash("A user with that email address already exists.")
    else:
        crud.create_user(email, password)
        flash("Account created! Please log in.")

    return redirect('/')




if __name__ == "__main__": 
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)