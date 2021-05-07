"""Script to seed database."""

import os 
import json

import crud 
import model 
import server 

os.system('dropdb donations')