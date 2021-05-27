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
def search_items():
    """Search for item."""

    return render_template('search_items.html')

@app.route('/search-results')
def search_results():
    """View item search results."""

    searched_item = request.args.get('item')
    items = crud.search_items(searched_item)

    return render_template('search_results.html', items=items)

@app.route('/items/<item_id>')
def show_item(item_id):
    """Show details of a particular item."""

    item = crud.get_item_by_id(item_id)

    return render_template('item_details.html', item=item)

@app.route('/users')
def verify_user():
    """Verify creds and route to donor or org page."""

    email = request.args.get('email')
    password = request.args.get('password')
    user = crud.get_user_by_email(email)
    
    if user:
        verify = crud.verify_credentials(user, password)
        if verify:
            user_type = crud.org_or_donor(user)
            if user_type: 
                return render_template('donor_home.html')
            else: 
                return render_template('org_home.html') 
        else: 
            flash("Invalid credentials. Try again.")
            return redirect('/login')

    else:     
        flash("An account with this email does not exist. Please create an account.")
    
    return redirect('/')

@app.route('/donor', methods=['POST'])
def register_donor():
    """Create a new donor."""

    email = request.form.get('email')
    password = request.form.get('password')
    fname = request.form.get('fname')
    lname = request.form.get('lname')

    user = crud.get_user_by_email(email)

    if user:
        flash("A user with that email address already exists.")
    else:
        new_user = crud.create_user(email, password)
        crud.create_donor(fname, lname, new_user)
        flash("Donor account created! Please log in.")

    return redirect('/')

@app.route('/org', methods=['POST'])
def register_org():
    """Create a new org."""

    email = request.form.get('email')
    password = request.form.get('password')
    org_name = request.form.get('org_name')
    org_description = request.form.get('org_description')
    org_website = request.form.get('org_website')

    user = crud.get_user_by_email(email)

    if user:
        flash("A user with that email address already exists.")
    else:
        new_user = crud.create_user(email, password)
        crud.create_org(org_name, new_user, org_description, org_website)
        flash("Organization account created! Please log in.")

    return redirect('/')

@app.route('/org/<org_id>')
def show_org(org_id):
    """Show details of a particular org."""

    org = crud.get_org_by_id(org_id)

    return render_template('org_details.html', org=org)

@app.route('/add-location')
def add_location(): 
    """Add location to an organization."""

    return render_template('create_location.html')

@app.route('/view-locations')
def view_locations(): 
    """View current locations."""

@app.route('/add-item')
def add_item(): 
    """Add item to location."""

@app.route('/view-items')
def view_items(): 
    """View current items."""




if __name__ == "__main__": 
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)