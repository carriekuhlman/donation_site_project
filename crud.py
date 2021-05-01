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



if __name__ == "__main__": 
    from server import app
    connect_to_db(app)