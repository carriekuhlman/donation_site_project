"""Script to seed database."""

import os 
from random import choice, randint

import crud 
import model 
import server 

os.system('dropdb donations')
os.system('createdb donations')

model.connect_to_db(server.app)
model.db.create_all()

# Create list to store user objects, create 10 users

users_in_db = []

for a in range(1, 11):
    email = f"user{a}@test.test"
    password = "test"

    user = crud.create_user(email, password)

    users_in_db.append(user)

# Create 5 donors, link to a random user

for i in range(1, 6): 
    fname = f"Donor{i}"
    lname = f"Lastname"

    donor_random_user = choice(users_in_db)
    users_in_db.remove(donor_random_user)
    donor = crud.create_donor(fname, lname, donor_random_user)

# #Create list to store org objects, Create 5 orgs, link to a random user

orgs_in_db = []

for y in range(1, 6): 

    org_name = f"Org{y}"
    org_description = f"Org #{y} is really cool."
    org_website = f"www.org{y}.test"

    org_random_user = choice(users_in_db)
    users_in_db.remove(org_random_user)

    org = crud.create_org(org_name, 
                        org_random_user, 
                        org_description, 
                        org_website)

    orgs_in_db.append(org)

# #Create list to store location objects, Create 5 locations, link to a random org

locations_in_db = []
t_or_f = [True, False]

for x in range(1, 6): 

    phone = f"({x}{x}{x}) {x}{x}{x}-{x}{x}{x}{x}"
    street_address = f"{x}{x}{x} Fake St."
    city = "Canoga Park"
    state = "CA"
    zip_code = "91303"
    accept_in_person = choice(t_or_f)

    if accept_in_person:
        donation_hours = f"{x}am to {x}pm"
    else:
        donation_hours = None

    random_org = choice(orgs_in_db)
    orgs_in_db.remove(random_org)

    location = crud.create_location(phone, 
                                street_address, 
                                city, 
                                state, 
                                zip_code, 
                                accept_in_person, 
                                random_org, 
                                donation_hours)

    locations_in_db.append(location)

# #Create 20 items, link to random location

conditions = ["New", "Lightly Used", "For Scraps"]

for z in range(1, 21): 
    
    item_name = f"{z}_item"
    condition_accepted = choice(conditions)
    qty_needed = randint(1, 40)

    random_location = choice(locations_in_db)

    item = crud.create_item(item_name, 
                        condition_accepted, 
                        random_location, 
                        qty_needed)


