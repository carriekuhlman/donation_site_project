"""CRUD operations."""

from model import db, User, Donor, Org, Location, Item, connect_to_db

def create_user(email, password): 
    """Create and return a new user."""

    user = User(email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user

def create_donor(fname, lname, user_id):
    """Create and return a new donor."""

    donor = Donor(fname=fname, lname=lname, user_id=user_id)

    db.session.add(donor)
    db.session.commit()

    return donor

def create_org(org_name, user_id, org_description=None, org_website=None):
    """Create and retun a new org."""

    org = Org(org_name=org_name, user_id=user_id, org_description=org_description, org_website=org_website)

    db.session.add(org)
    db.session.commit()

    return org

# def create_location(phone, street_address, city, state, zip_code, accept_in_person, donation_hours, org_id)



if __name__ == "__main__": 
    from server import app
    connect_to_db(app)