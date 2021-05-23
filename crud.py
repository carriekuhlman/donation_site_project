"""CRUD operations."""

from model import db, User, Donor, Org, Location, Item, connect_to_db

def create_user(email, password): 
    """Create and return a new user."""

    user = User(email=email, 
            password=password)

    db.session.add(user)
    db.session.commit()

    return user

def create_donor(fname, lname, user):
    """Create and return a new donor."""

    donor = Donor(fname=fname, 
                lname=lname, 
                user=user)

    db.session.add(donor)
    db.session.commit()

    return donor

def create_org(org_name, user, org_description=None, org_website=None):
    """Create and retun a new org."""

    org = Org(org_name=org_name, 
            user=user, 
            org_description=org_description, 
            org_website=org_website)

    db.session.add(org)
    db.session.commit()

    return org

def create_location(phone, street_address, city, state, zip_code, accept_in_person, org, donation_hours=None): 
     
     location = Location(phone=phone, 
                street_address=street_address, 
                city=city, 
                state=state, 
                zip_code=zip_code, 
                accept_in_person=accept_in_person, 
                donation_hours=donation_hours, 
                org=org)

     db.session.add(location)
     db.session.commit()

     return location

def create_item(item_name, condition_accepted, location, qty_needed=None):

    item = Item(item_name=item_name, 
            condition_accepted=condition_accepted, 
            location=location, 
            qty_needed=qty_needed)

    db.session.add(item)
    db.session.commit()

    return item

def get_items():
    """Return all items."""

    return Item.query.all()

def get_item_by_id(item_id):
    """Get item by item ID."""

    return Item.query.get(item_id)

def search_items(searched_item):
    """Search for item by name."""

    return Item.query.filter(Item.item_name.like(f"%{searched_item}%"))

def get_user_by_email(email): 
    """Return a user by email."""

    return User.query.filter(User.email == email).first()

def verify_credentials(user, password): 
    """Verify user credentials."""

    #check to confirm that username and password match

    return User.query.filter(user.password == password).first()

def org_or_donor(user):
    """Check to see if org or donor."""

    #returns a donor object if user_id is in donor table

    return Donor.query.filter(Donor.user_id == user.user_id).first()
    

if __name__ == "__main__": 
    from server import app
    connect_to_db(app)