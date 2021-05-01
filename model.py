"""Models for donation site."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model): 
    """A user."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String(320), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False)

    def __repr__(self): 
        return f"<User user_id={self.user_id} email={self.email}>"


class Donor(db.Model):
    """A donor."""

    __tablename__ = "donors"

    donor_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    fname = db.Column(db.String(50), nullable=False)
    lname = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)

    def __repr__(self): 
        return f"<Donor donor_id={self.donor_id} name={self.fname} {self.lname}>"


class Org(db.Model):
    """An organization."""

    __tablename__ = "orgs"

    org_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    org_name = db.Column(db.String(100), nullable=False)
    org_description = db.Column(db.Text)
    org_website = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)

    def __repr__(self): 
        return f"<Org org_id={self.org_id} org_name={self.org_name}>"


class Location(db.Model):
    """A location for an organization."""

    __tablename__ = "locations"

    location_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    phone = db.Column(db.String(50))
    street_address = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(2), nullable=False)
    zip_code = db.Column(db.String(10), nullable=False)
    accept_in_person = db.Column(db.Boolean, nullable=False)
    donation_hours = db.Column(db.String(50))
    org_id = db.Column(db.Integer, db.ForeignKey("orgs.org_id"), nullable=False)

    def __repr__(self): 
        return f"<Location location_id={self.location_id} located in {self.city}, {self.state} for {self.org_id}>"


class Item(db.Model):
    """An item that belongs to a location."""

    __tablename__ = "items"

    item_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    item_name = db.Column(db.String(50), nullable=False)
    condition_accepted = db.Column(db.String(50), nullable=False)
    qty_needed = db.Column(db.Integer)
    location_id = db.Column(db.Integer, db.ForeignKey("locations.location_id"), nullable=False)

    def __repr__(self): 
        return f"<Item item_id={self.item_id} item_name={self.item_name} located at {self.location_id}>"


def connect_to_db(flask_app, db_uri="postgresql:///donations", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODFICATIONS"] = False 

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")

if __name__ == "__main__":
    from server import app

    connect_to_db(app)