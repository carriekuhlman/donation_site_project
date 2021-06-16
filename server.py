"""Server for donations site."""

from flask import (Flask, render_template, request, flash,
                session, redirect, jsonify)
from model import connect_to_db
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "$JI06eiH!czwY&xGSs*QttAL"
app.jinja_env.undefined = StrictUndefined
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.route('/')
def homepage():
    """View homepage."""

    if 'username' in session: 
            flash("Logged in!")
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

@app.route('/account', methods=['GET', 'POST'])
def verify_user():
    """Verify creds and route to donor or org page."""

    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        user = crud.get_user_by_email(email)

        if user:
            verify = crud.verify_credentials(user, password)
            session['username'] = request.form['email']
            if verify:
                user_type = crud.check_if_donor(user)
                if user_type: 
                    return render_template('donor_home.html')
                else: 
                    org = crud.get_org_by_user(user)
                    locations = crud.view_all_org_locations(org)
                    return render_template('org_home.html', locations=locations) 
            else: 
                flash("Invalid credentials. Try again.")
                return redirect('/login')

        else:     
            flash("An account with this email does not exist. Please create an account.")
        
        return redirect('/')

    elif "username" in session and request.method == "GET": 
        user = crud.get_user_by_email(session["username"])
        user_type = crud.org_or_donor(user)
        if user_type: 
            return render_template('donor_home.html')
        else: 
            org = crud.get_org_by_user(user)
            locations = crud.view_all_org_locations(org)
            return render_template('org_home.html', locations=locations) 

    else:
        flash("Please log in.")
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

    phone = request.form.get('phone')
    address = request.form.get('address')
    city = request.form.get('city')
    state = request.form.get('state')
    zip_code = request.form.get('zip_code')
    in_person = request.form.get('in_person')

    org = crud.get_org_by_user(new_user)

    if in_person == "True": 
        in_person = True
        donation_hours = request.form.get('donation_hours')

    else:
        in_person = False
        donation_hours = None

    crud.create_location(phone, address, city, state, zip_code,
                    in_person, org, donation_hours)
        
        
    flash("Organization account created! Please log in.")
    return redirect('/')

@app.route('/org/<org_id>')
def show_org(org_id):
    """Show details of a particular org."""

    org = crud.get_org_by_id(org_id)

    return render_template('org_details.html', org=org)

@app.route('/location/<location_id>')
def show_location(location_id):
    """Show details of a particular location."""

    location = crud.get_location_by_id(location_id)

    return render_template('location_details.html', location=location)

@app.route('/add-location', methods=["POST"])
def add_location(): 
    """Add location to an organization."""

    user = crud.get_user_by_email(session["username"])
    org = crud.get_org_by_user(user)

    phone = request.form.get('phone')
    address = request.form.get('address')
    city = request.form.get('city')
    state = request.form.get('state')
    zip_code = request.form.get('zip_code')
    in_person = request.form.get('in_person')

    if in_person == "True": 
        in_person = True
        donation_hours = request.form.get('donation_hours')

    else:
        in_person = False
        donation_hours = None

    crud.create_location(phone, address, city, state, zip_code,
                    in_person, org, donation_hours)

    flash("Location added successfully.")
    return redirect('/account')

@app.route('/view-locations')
def view_locations(): 
    """View current locations."""

@app.route('/request-item', methods=["POST"])
def request_item(): 
    """Add item to location."""

    user = crud.get_user_by_email(session["username"])
    org = crud.get_org_by_user(user)

    item_name = request.form.get('item_name')
    condition_accepted = request.form.get('condition')
    qty_needed = int(request.form.get('qty_needed'))
    location_id = int(request.form.get('location'))

    location = crud.get_location_by_id(location_id)

    crud.create_item(item_name, condition_accepted, location, qty_needed)

    flash("Item added successfully.")
    return redirect('/account')

@app.route('/view-items')
def view_items(): 
    """View current items."""

@app.route('/logout')
def user_logout(): 
    """Remove the user from the session"""

    session.pop('username', None)
    flash("Successfully logged out.")

    return redirect('/')

# @app.route("/test.json")
# def testing_ajax():
#     """Testing search functionality all on one page."""

#     searched_item = request.args.get('searched-item')
#     items = crud.search_items(searched_item)

#     return render_template('search_results.html', items=items)

#     zipcode = request.args.get('zipcode')
#     weather_info = WEATHER.get(zipcode, DEFAULT_WEATHER)
#     return jsonify(weather_info)



if __name__ == "__main__": 
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)