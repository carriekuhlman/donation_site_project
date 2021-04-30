"""Models for donation site."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model): 
    """A user."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String(320), unique=True)
    password = db.Column(db.String(50))

    def __repr__(self): 
        return f"<User user_id={self.user_id} email={self.email}>"

class Donor(db.Model):
    """A donor."""

    __tablename__ = "donors"

    donor_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    fname = db.Column(db.String(50))
    lname = db.Column(db.String(50))
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))

    def __repr__(self): 
        return f"<Donor donor_id={self.donor_id} name={self.fname}{self.lname}>"

class Org(db.Model):
    """An organization."""

class Location(db.Model):
    """A location for an organization."""

class Item(db.Model):
    """An item that belongs to a location."""


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