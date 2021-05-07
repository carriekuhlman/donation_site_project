"""Script to seed database."""

import os 
import json

import crud 
import model 
import server 

os.system('dropdb donations')
os.system('createdb donations')

model.db.connect_to_db(server.app)
model.db.create_all()

